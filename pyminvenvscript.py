import requests, platform, configparser
from shutil import rmtree
from pathlib import Path, PurePath
from sys import argv
from subprocess import run, check_output
from urllib.parse import urlparse
from urllib.request import urlopen

#Notes:
#len(str(pathlib.Path)) is a workaround for the windows implementation of pathlib.Path not having a length property
if platform.system() == "Darwin":
    """
    This script should not need this because it doesn't use os.fork but it's here just in case.
    https://docs.python.org/3/library/urllib.request.html
    Warning:

    On macOS it is unsafe to use this module in programs using os.fork() because
    the getproxies() implementation for macOS uses a higher-level system API.
    Set the environment variable no_proxy to * to avoid this problem (e.g.
    os.environ["no_proxy"] = "*"). 
    """
    import os
    os.environ["no_proxy"] = "*"

class list(list):
    #Needed because list.index sucks
    def indexOf(self, item):
        try:
            return self.index(item)
        except:
            return -1

def checkExistsMakeDir(dir_, silent=False):
    if path.exists():
        if path.is_dir():
            return 1
        elif silent == False:
            print("Path exists but is not a directory.")
        return -1
    else:
        path.mkdir(parents=True)

curdir = Path(__file__).resolve().parent #Here because python (Windows) treats the location from which the script is called as ./ instead of the script's directory
venvfolder = "Pymin-venv"
venvpath = curdir / venvfolder

if curdir in {None, ""} or venvpath in {None, ""}:
    print("Error: Path is empty. Exiting to avoid problems.")
    exit()
if not isinstance(curdir,PurePath) or not isinstance(venvpath,PurePath):
    print("Error: Path is somehow not a pathlib.Path object. Something is wrong because this shouldn't happen.")
    exit()

def create(script_url="",as3libversion=""):
    #Sets up the virtual environment
    if (platform.system() == "Windows" and len(str(venvpath)) in {2,3} and venvpath[0].isalpha() and venvpath[1] == ":") or str(venvpath) == "/":
        print("Error: venvpath is set to the root directory. Can not create a virtual environment here.")
        exit()
    print("Creating the environment...")
    #create directory
    checkExistsMakeDir(venvpath)

    #create the virtual environment
    if useuv:
        run(["uv","venv",venvpath])
    else:    
        run([f"python", "-m" "venv", venvpath])
    
    #Create config
    createConfigInVenv("./",platform.python_version(),useuv,useuvi,defrun,nossl,nohtmlparser,devenv)
    
    #create game directory
    checkExistsMakeDir(venvpath / "Pymin")
    print("Done")

    downloadgame(script_url)
    installmodules(as3libversion)

def installmodules(as3libversion="latest"):
    global runlist
    #installs the required modules using pip inside the virtual environment
    if useuv:
        runlist = ["uv", "pip", "install", "--python", pythonvenvloc] + runlist[2:]
    elif useuvi:
        print("Installing UV...")
        run([pythonvenvloc, "-m", "pip", "install", "uv"])
        print("Done")
        runlist = pythonm + ["uv"] + runlist
    else:
        runlist = pythonm + runlist
    print("Installing dependencies...")
    temp = runlist.copy()
    if devenv:
        print("Skipping as3lib and tkhtmlview.")
        temp.remove("as3lib")
        temp.remove("tkhtmlview")
        run(temp)
    elif as3libversion == "latest":
        run(temp)
    elif as3libversion.lower() == "none":
        temp.remove("as3lib")
        run(temp) 
    else:
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
        run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def downloadgame(url=""):
    #downloads the game
    print("Installing game... Please wait.")
    with urlopen(url,context=ssl_context) as urlfile:
        (venvpath / "Pymin/Pymin.py").write_bytes(urlfile.read())
    print("Done")

def updatemodules(as3libversion="latest"):
    global runlist
    #updates the required modules using pip inside the virtual environment
    if useuv:
        runlist = ["uv", "pip", "install", "--python", pythonvenvloc] + runlist[2:]
    elif useuvi:
        print("Installing UV...")
        run([pythonvenvloc, "-m", "uv", "pip", "install", "-U", "uv"])
        print("Done")
        runlist = pythonm + ["uv"] + runlist
    else:
        runlist = pythonm + runlist
    print("Updating dependencies...")
    temp = runlist.copy()
    temp.insert(temp.index("install")+1,"-U")
    if devenv:
        print("Skipping as3lib and tkhtmlview.")
        temp.remove("as3lib")
        temp.remove("tkhtmlview")
        run(temp)
    elif as3libversion == "latest":
        run(temp)
    elif as3libversion.lower() == "none":
        temp.remove("as3lib")
        run(temp) 
    else:
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
        run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def rezero(url,as3libversion):
    if venvpath.is_dir() == False:
        print(f"Error: Directory \"{venvpath}\" either doesn't exist or is not a directory.")
        return
    elif (platform.system() == "Windows" and len(str(venvpath)) in {2,3} and venvpath[0].isalpha() and venvpath[1] == ":") or venvpath == "/":
        print("Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...")
        exit()
    else:
        rmtree(venvpath)
    create(url,as3libversion)

def replaceTkhtmlviewParserWithUnsafeOne():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands instead from href tags. Only use this inside of this project's virtual environment.
    if devenv:
        print("Skipped custom html_parser.py.")
    elif nohtmlparser == False:
        print("Replacing tkhtmlview html_parser.py with my custom one...")
        if platform.system() == "Windows":
            path = Path(str(check_output(f"{pythonvenvloc} -c \"import importlib.util;print(importlib.util.find_spec('tkhtmlview').origin)\"",shell=True))[2:][:-1].replace("\\n","").replace("__init__.py","html_parser.py").replace("\\\\","/").replace("\\r",""))
        else:
            path = Path(str(check_output(f"{pythonvenvloc} -c 'import importlib.util;print(importlib.util.find_spec(\"tkhtmlview\").origin)'",shell=True))[2:][:-1].replace("\\n","").replace("__init__.py","html_parser.py"))
        with urlopen("https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/main/pyminlib/html_parser.py",context=ssl_context) as urlfile:
            path.write_bytes(urlfile.read())
        print("Done")

def updatePythonVersion(pyver):
    global c2
    answer = input("(Not Implemented) Python major version has changed. Would you like to switch this virtual environment to the new one? (Y/n)")
    #if answer.lower() in ("y",""):
    if False:
        """
        tempsettings = []
        for i in (".DEFAULTRUN",".USEUV",".USEUVI"):
            if Path(venvpath / i).exists():
                tempsettings.append(True)
            else:
                tempsettings.append(False)
        if Path(venvpath / "Pymin").exists():
            #copy pymin folder to safe location
            ...
        ...
        rmtree(venvpath) #delete the venv folder
        a = input("Which as3lib version? (default latest)")
        create(as3libversion=a,nogame=True) #reinstall venv
        #move saved files back to venv
        #save persistent variables
        """
        if platform.system() == "Windows":
            ...
        else:
            (venvpath / f"bin/python{".".join(pyver.split(".")[:2])}").unlink()
            (venvpath / f"bin/python{".".join(pyver.split(".")[:1])}").unlink()
            (venvpath / "bin/python").unlink()
            rmtree(venvpath / f"lib/python{".".join(pyver.split(".")[:2])}")
            run([*pythonm,"venv","--upgrade",venvpath]) #!Will not work because python was unlinked
            installmodules()
            c2["Options"]["pyInstalledVersion"] = platform.python_version()



def repairInstall():
    answer = input("Python failed to launch. Would you like to try automated repair? (y/N)")
    if answer.lower() == "y":
        ...

def migrateConfig():
    tempUV = False
    tempUVI = False
    tempDR = False
    #Get old config values. Check here in case it moves to a different location in the future.
    if (venvpath / ".USEUV").exists():
        tempUV = True
        Path(venvpath / ".USEUV").unlink(missing_ok=True)
    if (venvpath / ".USEUVI").exists():
        tempUVI = True
        Path(venvpath / ".USEUVI").unlink(missing_ok=True)
    if (venvpath / ".DEFAULTRUN").exists():
        tempDR = True
        Path(venvpath / ".DEFAULTRUN").unlink(missing_ok=True)
    pyversion = platform.python_version()
    with open(venvpath / "pyvenv.cfg","r") as f:
        c = configparser.ConfigParser(allow_unnamed_section=True)
        c.optionxform=str
        c.read_file(f)
        pyversion = c[configparser.UNNAMED_SECTION]["version_info"]
    #Generate new config
    cfgpath = venvpath / "pymin.cfg"
    if cfgpath.exists():
        c = configparser.ConfigParser()
        c.optionxform=str
        with open(cfgpath, 'r') as f:
            c.read_file(f)
        if c.getint("Options","cfgVersion") == 1:
            if tempUV:
                c["Options"]["uvGlobal"] = "True"
                c["Options"]["uvLocal"] = "False"
            elif tempUVI:
                c["Options"]["uvGlobal"] = "False"
                c["Options"]["uvLocal"] = "True"
            if tempDR:
                c["Options"]["defaultToRun"] = "True"
        with open(cfgpath, 'w') as f:
            c.write(f)
        del c
    else:
        createConfigInVenv(path="./",pyInstalledVersion=pyversion,uvGlobal=tempUV,uvLocal=tempUVI,defaultToRun=tempDR,noSSLVerify=False,noCustomHTMLParser=False,isDevEnv=False)

def createConfigInVenv(path="./",pyInstalledVersion=platform.python_version(),uvGlobal=False,uvLocal=False,defaultToRun=False,noSSLVerify=False,noCustomHTMLParser=False,isDevEnv=False,configDict:dict=None):
    global noConfigExists
    if configDict == None:
        configDict = {"Options":{"cfgVersion":1,"path":path,"pyInstalledVersion":pyInstalledVersion,"uvGlobal":uvGlobal,"uvLocal":uvLocal,"defaultToRun":defaultToRun,"noSSLVerify":noSSLVerify,"noCustomHTMLParser":noCustomHTMLParser,"isDevEnv":isDevEnv}}
    c = configparser.ConfigParser()
    c.optionxform=str
    c.read_dict(configDict)
    with open(venvpath / "pymin.cfg", 'w') as f:
        c.write(f)
    del c
    noConfigExists = False

ssl_context = None
noConfigExists = False
args = list(argv)
if (venvpath / ".USEUV").exists() or (venvpath / ".USEUVI").exists() or (venvpath / ".DEFAULTRUN").exists():
    print("Old config detected. Automatically migrating to new one.")
    migrateConfig()
    print("Done")
if (curdir / "pymin.cfg").exists():
    #load config and set venvpath
    cfgloc = curdir / "pymin.cfg"
    c1 = configparser.ConfigParser()
    c1.optionxform=str
    c2 = configparser.ConfigParser()
    c2.optionxform=str
    with open(cfgloc,"r") as f:
        c1.read_file(f)
        c2.read_dict(c1)
    venvpath = Path(c1["Options"]["path"]).resolve()
    defrun = c1.getboolean("Options","defaultToRun",fallback=False)
    useuv = c1.getboolean("Options","uvGlobal",fallback=False)
    useuvi = c1.getboolean("Options","uvLocal",fallback=False)
    nossl = c1.getboolean("Options","noSSLVerify",fallback=False)
    nohtmlparser = c1.getboolean("Options","noCustomHTMLParser",fallback=False)
    pyinstalversion = c1["Options"]["pyInstalledVersion"]
    devenv = c1.getboolean("Options","isDevEnv",fallback=False)
elif (venvpath / "pymin.cfg").exists():
    #load config
    cfgloc = venvpath / "pymin.cfg"
    c1 = configparser.ConfigParser()
    c1.optionxform=str
    c2 = configparser.ConfigParser()
    c2.optionxform=str
    with open(cfgloc,"r") as f:
        c1.read_file(f)
        c2.read_dict(c1)
    defrun = c1.getboolean("Options","defaultToRun",fallback=False)
    useuv = c1.getboolean("Options","uvGlobal",fallback=False)
    useuvi = c1.getboolean("Options","uvLocal",fallback=False)
    nossl = c1.getboolean("Options","noSSLVerify",fallback=False)
    nohtmlparser = c1.getboolean("Options","noCustomHTMLParser",fallback=False)
    pyinstalversion = c1["Options"]["pyInstalledVersion"]
    devenv = c1.getboolean("Options","isDevEnv",fallback=False)
else:
    #Use fallback values because config does not exist
    defrun = False
    useuv = False
    useuvi = False
    nossl = False
    nohtmlparser = False
    if venvpath.exists():
        with open(venvpath / "pyvenv.cfg", "r") as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            pyinstalversion = c[configparser.UNNAMED_SECTION]["version_info"]
    else:
        #Fallback
        pyinstalversion = platform.python_version()
    devenv = False
    c1 = {"Options":{}}
    c2 = {"Options":{"cfgVersion":1,"path":"./","pyInstalledVersion":pyinstalversion,"uvGlobal":False,"uvLocal":False,"defaultToRun":False,"noSSLVerify":False,"noCustomHTMLParser":False,"isDevEnv":False}}
    noConfigExists = True

if platform.system() == "Windows": #Windows check
    pythonvenvloc = venvpath / "Scripts/python.exe"
else:
    pythonvenvloc = venvpath / "bin/python"
pythonm = [pythonvenvloc, "-m"]
runlist = ["pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools"]

if platform.python_version().split(".")[:2] != pyinstalversion.split(".")[:2]:
    updatePythonVersion(pyinstalversion)
try:
    if venvpath.exists():
        check_output(f"{pythonvenvloc} -V",shell=True) #!See if this can be hidden
except:
    repairInstall()
    exit() #!for some reason, this does not exit
if len(args) < 2 and defrun:
    run([pythonvenvloc, venvpath / "Pymin/Pymin.py"])
elif len(args) < 2 or 1 in (args.indexOf("--help"),args.indexOf("-h"),args.indexOf("help")) or 1 in (args.indexOf("install"),args.indexOf("cmd"),args.indexOf("recreate"),args.indexOf("rezero"),args.indexOf("run")) and 2 in (args.indexOf("--help"),args.indexOf("-h")):
    print("venvscript {install|update|run|cmd|recreate|uv} [args]\nCommands:\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it's dependencies.\n\trun\t\t\tRuns the game. All arguement pass to this will be forwarded to the game instead of being used by this script.\n\tcmd\t\t\tEnters the virtual environment (not implemented yet)\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes commands with uv inside of the environment.\n\nArguements:\n\t--version\t\tSpecifies the version of the game to download [default:latest]\n\t--as3libversion\t\tSpecifies the version of as3lib to download [default:latest]\n\t--help\t\t\tDisplays this message\n\t--no-ssl\t\tBypasses ssl certification and uses the insecure context even when using https (persistent)\n\t--unverified\t\tSame as --no-ssl but not persistent\n\t--use-ssl\t\tOpposite of --no-ssl (persistent)\n\t--nohtmlparser\t\tDoes not download my custom html parser for tkhtmlview. (persistent)\n\t--withhtmlparser\tOpposite of --nohtmlparser (persistent)\n\t--uv-global\t\tUses uv instead of pip. uv must be in the path. (persistent)\n\t--uv-local\t\tInstalls and uses uv inside of the venv. (persistent)\n\t--no-uv\t\t\tOpposite of --use-uv(i). Does not uninstall uv from the venv. (persistent)\n\t--default-run\t\tSets run as the default command. (persistent)\n\t--default-help\t\tSets help as the default command. (persistent)\n\t--overwrite\t\tBypasses the overwrite restriction in the \"install\" command\n\t--migrate-config\tMigrates the config from a previous version to the current one. This should run automatically if an old version is detected.")
else:
    if args[1] in {"install","recreate","update","rezero"} or args[1][:2] == "--":
        if "--no-ssl" in args:
            nossl = True
            c2["Options"]["noSSLVerify"] = "True"
        elif "--use-ssl" in args:
            nossl = False
            c2["Options"]["noSSLVerify"] = "False"
        if "--uv-global" in args:
            useuv = True
            c2["Options"]["uvGlobal"] = "True"
            useuvi = False
            c2["Options"]["uvLocal"] = "False"
        elif "--uv-local" in args:
            useuv = False
            c2["Options"]["uvGlobal"] = "False"
            useuvi = True
            c2["Options"]["uvLocal"] = "True"
        elif "--no-uv" in args:
            useuv = False
            c2["Options"]["uvGlobal"] = "False"
            useuvi = False
            c2["Options"]["uvLocal"] = "False"
        if "--default-help" in args:
            defrun = False
            c2["Options"]["defaultToRun"] = "False"
        elif "--default-run" in args:
            defrun =True
            c2["Options"]["defaultToRun"] = "True"
        if "--nohtmlparser" in args:
            nohtmlparser = True
            c2["Options"]["nocustomHTMLParser"] = "True"
        elif "--withhtmlparser" in args:
            nohtmlparser = False
            c2["Options"]["nocustomHTMLParser"] = "False"
        if "--supersecretdevmode" in args:
            #This arguement is meant to be undocumented in the help section
            #Does not have an option to disable because I would never need to disable this
            #All this does is make the script not update anything that I might be working on
            devenv = True
            c2["Options"]["isDevEnv"] = "True"
        if "--migrate-config" in args:
            migrateConfig()
        if nossl or "--unverified" in args:
            import ssl
            ssl_context = ssl._create_unverified_context()
        if "--version" in args:
            versiontag = args[args.indexOf("--version") + 1]
        else:
            versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
        url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
        if "--as3libversion" in args:
            as3libversiontag = args[args.indexOf("--as3libversion") + 1]
        else:
            as3libversiontag = "latest"
    if args[1] == "install":
        if venvpath.exists() and "--overwrite" in args:
            print("You can not use install in an existing directory. Did you mean \"update\"?")
            exit()
        create(url,as3libversiontag)
    elif args[1] == "update":
        if devenv:
            print("Skipped game download.")
        else:
            downloadgame(url)
        updatemodules(as3libversiontag)
    elif args[1] == "run":
        run([pythonvenvloc, venvpath / "Pymin/Pymin.py", *args[2:]])
    elif args[1] == "cmd":
        ...
    elif args[1] in {"recreate","rezero"}:
        rezero(url,as3libversiontag)
    elif args[1] == "uv":
        if venvpath.exists():
            if len(args) == 2:
                run(["uv","--help"])
            else:
                rl = ["uv",*args[2:],"--python",pythonvenvloc]
                if useuv:
                    run(rl)
                elif useuvi:
                    run([pythonvenvloc,"-m"]+rl)
    else:
        if defrun:
            run([pythonvenvloc, venvpath / "Pymin/Pymin.py", *args[1:]])
        else:
            ...
if venvpath.exists():
    if noConfigExists:
        createConfigInVenv(configDict=c2)
    elif c1 != c2 and type(c2) != dict: #Check if config was modified
        #Write modified config to disk
        with open(cfgloc, 'w') as f:
            c2.write(f)
