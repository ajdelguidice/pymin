#!/usr/bin/env python
import requests, platform, configparser, ssl, tempfile
from shutil import rmtree, copytree
from pathlib import Path, PurePath
from sys import argv
from subprocess import run, check_output
from urllib.parse import urlparse
from urllib.request import urlopen
from io import StringIO

if platform.system() == "Darwin":
    print("Warning: This script is untested on darwin (MacOS), things might be broken.")
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

def checkExistsMakeDir(dir_, silent=False):
    if dir_.is_dir():
        return 1
    elif dir_.exists():
        if silent == False:
            print("Path exists but is not a directory.")
        return -1
    else:
        dir_.mkdir(parents=True)

curdir = Path(__file__).resolve().parent #This is a workaround for python on Windows
venvfolder = "Pymin-venv"
venvpath = curdir / venvfolder
cfgloc = None

if None in {curdir,venvpath} or "" in {str(curdir),str(venvpath)}:
    print("Error: Path is empty. Exiting to avoid problems.")
    exit()
if not (isinstance(curdir,PurePath) and isinstance(venvpath,PurePath)):
    print("Error: Path is somehow not a pathlib.Path object. Something is very wrong.")
    exit()

def create(script_url="",as3libversion="",cfgDict:dict=None):
    #Sets up the virtual environment
    if venvpath == venvpath.parent:
        print("Error: venvpath is set to the root directory. Can not create a virtual environment here.")
        exit()
    print("Creating the environment...")
    #create directory
    checkExistsMakeDir(venvpath)

    #create the virtual environment
    if c2["uvGlobal"]:
        run(["uv","venv",venvpath])
    else:    
        run([f"python", "-m" "venv", venvpath])

    #Create config
    move = False
    if (curdir / "pymin.toml").exists() and venvpath == curdir / "Pymin-venv":
        #Ask if user wants to move the config to venv
        inp = input("Config exists. Would you like to move it into the venv? (y/N)").lower()
        if inp == "y":
            move = True
    global cfgloc
    if move == True:
        c2["path"] = "./"
        (curdir / "pymin.toml").unlink(missing_ok=True)
        cfgloc = venvpath / "pymin.toml"
    elif cfgloc == None or cfgDict != None:
        cfgloc = venvpath / "pymin.toml"
        createConfigInVenv(configDict=cfgDict)
    else:
        c2["path"] = venvpath
    
    #create game directory
    checkExistsMakeDir(venvpath / "Pymin")
    print("Done")

    downloadgame(script_url)
    installmodules(as3libversion)

def installmodules(as3libversion="latest",overrideDev=False):
    #installs the required modules using pip inside the virtual environment
    if c2["uvGlobal"]:
        temp = ["uv", "pip", "install", "--python", pythonvenvloc] + runlist[2:]
    elif c2["uvLocal"]:
        print("Installing UV...")
        run([pythonvenvloc, "-m", "pip", "install", "uv"])
        print("Done")
        temp = pythonm + ["uv"] + runlist
    else:
        temp = pythonm + runlist
    print("Installing dependencies...")
    if c2["isDevEnv"] and not overrideDev:
        print("Skipping as3lib and tkhtmlview.")
        temp.remove("as3lib")
        temp.remove("tkhtmlview")
    elif as3libversion.lower() == "none":
        temp.remove("as3lib")
    elif as3libversion != "latest":
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
    run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def downloadgame(url=""):
    #downloads the game
    print("Installing game... Please wait.")
    with urlopen(url,context=getSSLContext()) as urlfile:
        (venvpath / "Pymin/Pymin.py").write_bytes(urlfile.read())
    print("Done")

def updatemodules(as3libversion="latest"):
    #updates the required modules using pip inside the virtual environment
    if c2["uvGlobal"]:
        temp = ["uv", "pip", "install", "--python", pythonvenvloc] + runlist[2:]
    elif c2["uvLocal"]:
        print("Updating UV...")
        run([pythonvenvloc, "-m", "uv", "pip", "install", "-U", "uv"])
        print("Done")
        temp = pythonm + ["uv"] + runlist
    else:
        temp = pythonm + runlist
    print("Updating dependencies...")
    temp.insert(temp.index("install")+1,"-U")
    if c2["isDevEnv"]:
        print("Skipping as3lib and tkhtmlview.")
        temp.remove("as3lib")
        temp.remove("tkhtmlview")
    elif as3libversion.lower() == "none":
        temp.remove("as3lib")
    elif as3libversion != "latest":
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
    run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def recreate(url,as3libversion,cfgDict:dict=None,withsaves=False):
    if not venvpath.is_dir():
        print(f"Error: Directory \"{venvpath}\" either doesn't exist or is not a directory. Aborting...")
        return
    if venvpath == venvpath.parent:
        print("Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...")
        return
    if not ((venvpath / "pymin.toml").exists() and (venvpath / "Pymin/Pymin.py").exists()):
        print("Error: venvpath does not look like it contains a valid Pymin virtual environment. Aborting...")
        return
    if withsaves:
        with tempfile.TemporaryDirectory() as d:
            tempdir = Path(d)
            copytree(venvpath / "Pymin/nimin_saves", tempdir / "nimin_saves")
            rmtree(venvpath)
            create(url,as3libversion,cfgDict)
            copytree(tempdir / "nimin_saves", venvpath / "Pymin/nimin_saves")
    else:
        rmtree(venvpath)
        create(url,as3libversion,cfgDict)

def replaceTkhtmlviewParserWithUnsafeOne():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands from href tags. Only use this inside of this project's virtual environment.
    if c2["isDevEnv"]:
        print("Skipped custom html_parser.py.")
    elif not (tempnohtmlparser or c2["noCustomHTMLParser"]):
        print("Replacing tkhtmlview html_parser.py with my custom one...")
        temp = check_output(f"{pythonvenvloc} -c \"import importlib.util;print(importlib.util.find_spec('tkhtmlview').origin)\"",shell=True).decode("utf-8").replace("\\n","").replace("__init__.py","html_parser.py")
        if platform.system() == "Windows":
            temp = temp.replace("\\\\","/").replace("\\r","")
        with urlopen("https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/main/pyminlib/html_parser.py",context=getSSLContext()) as urlfile:
            Path(temp).write_bytes(urlfile.read())
        print("Done")

def updatePythonVersion():
    global c2
    answer = input("(Not Implemented) Python major version has changed. Would you like to switch this virtual environment to the new one? (Y/n)")
    #if answer.lower() in {"y","")}
    if False and answer.lower() in {"y",""}:
        rmtree(venvpath / f"lib/python{'.'.join(c2["pyInstalledVersion"].split('.')[:2])}")
        run([*pythonm,"venv","--upgrade",venvpath])
        installmodules(overrideDev=True)
        c2["pyInstalledVersion"] = platform.python_version()

def repairInstall():
    answer = input("Python failed to launch. Would you like to try automated repair? (y/N)")
    if answer.lower() == "y":
        ...

def migrateConfig(save:bool=False,getNew:bool=False):
    tempUV = False
    tempUVI = False
    tempDR = False
    cfgloc = venvpath / "pymin.toml"
    conf = None
    #Get old config values. Check here in case it moves to a different location in the future.
    if (venvpath / ".USEUV").exists():
        tempUV = True
        (venvpath / ".USEUV").unlink(missing_ok=True)
    if (venvpath / ".USEUVI").exists():
        tempUVI = True
        (venvpath / ".USEUVI").unlink(missing_ok=True)
    if (venvpath / ".DEFAULTRUN").exists():
        tempDR = True
        (venvpath / ".DEFAULTRUN").unlink(missing_ok=True)
    #load config
    if getNew and ((curdir / "pymin.toml").exists() or (venvpath / "pymin.toml").exists()):
        if (curdir / "pymin.toml").exists():
            cfgloc = curdir / "pymin.toml"
        with open(cfgloc,"rb") as f:
            conf = tomllib.load(f)
    elif (curdir / "pymin.cfg").exists() or (venvpath / "pymin.cfg").exists():
        if (curdir / "pymin.cfg").exists():
            temploc = curdir / "pymin.cfg"
            cfgloc = curdir / "pymin.toml"
        else:
            temploc = venvpath / "pymin.cfg"
        c = configparser.ConfigParser()
        c.optionxform=str
        with open(temploc,"r") as f:
            c.read_file(f)
        conf = {"cfgVersion":1,"path":"","pyInstalledVersion":c["Options"]["pyInstalledVersion"]}
        conf["path"] = c.get("Options","path",fallback=str(venvpath))
        for i in {"uvGlobal","uvLocal","defaultToRun","noSSLVerify","noCustomHTMLParser","isDevEnv"}:
            conf[i] = c.getboolean("Options",i,fallback=False)
        temploc.unlink(missing_ok=True)
        del c
    else:
        pyversion = platform.python_version()
        with open(venvpath / "pyvenv.cfg","r") as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            pyversion = c[configparser.UNNAMED_SECTION]["version_info"]
            del c
        conf = {"cfgVersion":1,"path":"./","pyInstalledVersion":pyversion,"uvGlobal":tempUV,"uvLocal":tempUVI,"defaultToRun":tempDR,"noSSLVerify":False,"noCustomHTMLParser":False,"isDevEnv":False}
    if conf == None:
        print("Nothing to do.")
    elif save:
        writeTOML(cfgloc,conf)
    else:
        return conf

def TOMLValue(key,value,text):
    text.write(f"{key} = ")
    if isinstance(value,str):
        text.write(f'"{value}"\n')
    elif isinstance(value,bool):
        text.write(("true" if value else "false") + "\n")
    else:
        text.write(f"{value}\n")

def writeTOML(file,valDict,mode="w"):
    with StringIO() as text:
        for k1,v1 in valDict.items():
            if isinstance(v1,dict):
                text.write(f"[{k1}]\n")
                for k2,v2 in v1.items():
                    TOMLValue(k2,v2,text)
                text.write(f"\n")
            else:
                TOMLValue(k1,v1,text)
        with open(file,mode) as f:
            f.write(text.getvalue())

def createConfigInVenv(path="./",pyInstalledVersion=platform.python_version(),uvGlobal=False,uvLocal=False,defaultToRun=False,noSSLVerify=False,noCustomHTMLParser=False,isDevEnv=False,configDict:dict=None):
    if configDict == None:
        configDict = {"cfgVersion":1,"path":path,"pyInstalledVersion":pyInstalledVersion,"uvGlobal":uvGlobal,"uvLocal":uvLocal,"defaultToRun":defaultToRun,"noSSLVerify":noSSLVerify,"noCustomHTMLParser":noCustomHTMLParser,"isDevEnv":isDevEnv}
    writeTOML(venvpath / "pymin.toml",configDict)

insecure_context = ssl._create_unverified_context()

def getSSLContext():
    if c2["noSSLVerify"] or tempnossl:
        return insecure_context
    return None

def indexOf(l, item):
    try:
        return l.index(item)
    except:
        return -1

tempnossl = False
hasVenv = True

runlist = ["pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools","tomli-w"]
try:
    import tomllib
except:
    import tomli as tomllib
    runlist.append("tomli")

if (venvpath / ".USEUV").exists() or (venvpath / ".USEUVI").exists() or (venvpath / ".DEFAULTRUN").exists() or (curdir / "pymin.cfg").exists() or (venvpath / "pymin.cfg").exists():
    print("Old config detected. Automatically migrating to new one.")
    migrateConfig(True)
    print("Done")
if (curdir / "pymin.toml").exists():
    #load config and set venvpath
    cfgloc = curdir / "pymin.toml"
    with open(cfgloc,"rb") as f:
        c1 = tomllib.load(f)
    c2 = {
        "cfgVersion":c1.get("cfgVersion",1),
        "path":Path(c1.get("path",venvpath)).resolve(),
        "pyInstalledVersion":c1.get("pyInstalledVersion"),
        "uvGlobal":c1.get("uvGlobal",False),
        "uvLocal":c1.get("uvLocal",False),
        "defaultToRun":c1.get("defaultToRun",False),
        "noSSLVerify":c1.get("noSSLVerify",False),
        "noCustomHTMLParser":c1.get("noCustomHTMLParser",False),
        "isDevEnv":c1.get("isDevEnv",False)
    }
    venvpath = c2["path"]
elif (venvpath / "pymin.toml").exists():
    #load config
    cfgloc = venvpath / "pymin.toml"
    with open(cfgloc,"rb") as f:
        c1 = tomllib.load(f)
    c2 = {
        "cfgVersion":c1.get("cfgVersion",1),
        "path":c1.get("path",venvpath),
        "pyInstalledVersion":c1.get("pyInstalledVersion"),
        "uvGlobal":c1.get("uvGlobal",False),
        "uvLocal":c1.get("uvLocal",False),
        "defaultToRun":c1.get("defaultToRun",False),
        "noSSLVerify":c1.get("noSSLVerify",False),
        "noCustomHTMLParser":c1.get("noCustomHTMLParser",False),
        "isDevEnv":c1.get("isDevEnv",False)
    }
else:
    #Use fallback values because config does not exist
    c1 = {}
    c2 = {"cfgVersion":1,"pyInstalledVersion":None,"uvGlobal":False,"uvLocal":False,"defaultToRun":False,"noSSLVerify":False,"noCustomHTMLParser":False,"isDevEnv":False}
    if venvpath.exists():
        with open(venvpath / "pyvenv.cfg", "r") as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            c2["pyInstalledVersion"] = c[configparser.UNNAMED_SECTION]["version_info"]
        c2["path"] = venvpath
    else:
        #Fallback
        c2["pyInstalledVersion"] = platform.python_version()
        hasVenv = False


if platform.system() == "Windows":
    pythonvenvloc = venvpath / "Scripts/python.exe"
else:
    pythonvenvloc = venvpath / "bin/python"
pythonm = [pythonvenvloc, "-m"]
if hasVenv:
    if platform.python_version().split(".")[:2] != c2["pyInstalledVersion"].split(".")[:2] and platform.system() != "Windows":
        updatePythonVersion()
    try:
        if venvpath.exists():
            check_output(f"{pythonvenvloc} -V",shell=True)
    except:
        repairInstall()
        exit() #!for some reason, this does not exit
if len(argv) < 2 and c2["defaultToRun"]:
    run([pythonvenvloc, venvpath / "Pymin/Pymin.py"])
elif len(argv) < 2 or 1 in {indexOf(argv,"--help"),indexOf(argv,"-h"),indexOf(argv,"help")} or 1 in {indexOf(argv,"install"),indexOf(argv,"update"),indexOf(argv,"cfg"),indexOf(argv,"cmd"),indexOf(argv,"recreate")} and 2 in {indexOf(argv,"--help"),indexOf(argv,"-h")}:
    print("venvscript [command] [args]\nCommands:\n\thelp\t\t\tDisplays this message. Also --help and -h\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it's dependencies.\n\tcfg\t\t\tFor configuring this script. Use without any arguements will list all current values.\n\tcfg-game\t\tAllows modification of pymin's config. key/values are in the form \"section.key=value\". Displaying values is done the same as cfg. Only works on pymin 1.0.12+.\n\tmigrate-config\t\tMigrates the config from a previous version to the current one. If an old version is detected, this runs automatically.\n\tcmd\t\t\tEnters the virtual environment (not implemented yet)\n\trun\t\t\tRuns the game. Forwards all arguements.\n\tconv\t\t\tRuns the savefile converter built into the game. Takes no arguements.\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes uv inside of the environment. Forwards all arguements.\n\tpip\t\t\tExecutes pip inside of the environment. Does not work if the venv was installed with uv. Forwards all arguements.\n\nArguements {cfg}:\n\t--no-ssl\t\tBypasses ssl certification and uses the insecure context even when using https (persistent)\n\t--use-ssl\t\tOpposite of --no-ssl (persistent)\n\t--uv-global\t\tUses uv instead of pip. uv must be in the path. (persistent)\n\t--uv-local\t\tInstalls and uses uv inside of the venv. (persistent)\n\t--no-uv\t\t\tOpposite of --uv-glocal and --uv-local. Does not uninstall uv from the venv. (persistent)\n\t--default-help\t\tSets help as the default command. (persistent)\n\t--default-run\t\tSets run as the default command. (persistent)\n\t--nohtmlparser\t\tDoes not download my custom html parser for tkhtmlview. (persistent)\n\t--withhtmlparser\tOpposite of --nohtmlparser (persistent)\n\nArguements {install|update|recreate}:\n\t--unverified\t\tSame as --no-ssl but not persistent\n\t--version\t\tSpecifies the version of the game to download [default:latest]\n\t--as3libversion\t\tSpecifies the version of as3lib to download [default:latest]\n\nOther Command Specific Arguements:\n\t{install}\t--overwrite\t\tBypasses the overwrite restriction. Use at your own risk.\n\t{recreate}\t--migrate-config\tReads the config and writes it to the new environment.\n\t{recreate}\t--with-saves\t\tKeeps the nimin_saves directory.")
elif argv[1] == "migrate-config":
    migrateConfig()
elif c2["defaultToRun"] and (len(argv) < 2 or argv[1].startswith(("-","--","/"))):
    run((pythonvenvloc, venvpath / "Pymin/Pymin.py", *argv[1:]))
else:
    if argv[1] in {"install","update","recreate"}:
        if "--unverified" in argv:
            tempnossl = True
        if "--nohtmlparser" in argv:
            tempnohtmlparser = True
        if "--version" in argv:
            versiontag = argv[indexOf(argv,"--version") + 1]
        else:
            versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
        url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
        if "--as3libversion" in argv:
            as3libversiontag = argv[indexOf(argv,"--as3libversion") + 1]
        else:
            as3libversiontag = "latest"
    if argv[1] == "cfg":
        if cfgloc == None:
            if not hasVenv:
                cfgloc = curdir / "pymin.toml"
            else:
                cfgloc = venvpath / "pymin.toml"
        if len(argv) == 2:
            with StringIO() as text:
                for k,v in c2.items():
                    text.write(f"{k}: {v}\n")
                text.write(f"tempNoSSL: {tempnossl}")
                print(text.getvalue())
            exit()
        if "--no-ssl" in argv:
            c2["noSSLVerify"] = True
        elif "--use-ssl" in argv:
            c2["noSSLVerify"] = False
        if "--uv-global" in argv:
            c2["uvGlobal"] = True
            c2["uvLocal"] = False
        elif "--uv-local" in argv:
            c2["uvGlobal"] = False
            c2["uvLocal"] = True
        elif "--no-uv" in argv:
            c2["uvGlobal"] = False
            c2["uvLocal"] = False
        if "--default-help" in argv:
            c2["defaultToRun"] = False
        elif "--default-run" in argv:
            c2["defaultToRun"] = True
        if "--nohtmlparser" in argv:
            c2["noCustomHTMLParser"] = True
        elif "--withhtmlparser" in argv:
            c2["noCustomHTMLParser"] = False
        if "--activateDevMode" in argv:
            #This arguement is meant to be undocumented in the help section
            #All this does is make the script not update anything that I might be working on
            c2["isDevEnv"] = True
            print("Dev mode activated. This is meant for interal use and should not be used by the end user. If you did not mean to enable this, use --deactivateDevMode to disable it.")
        elif "--deactivateDevMode" in argv:
            c2["isDevEnv"] = False
    elif argv[1] == "cfg-game":
        with open(venvpath / "Pymin/Nimin_Prefs.toml","rb") as f:
            gameconf = tomllib.load(f)
        if len(argv) == 2:
            with StringIO() as text:
                for k1,v1 in gameconf.items():
                    text.write(f"|{k1}|\n")
                    for k2,v2 in v1.items():
                        text.write(f"{k2}: {v2}\n")
                    text.write("\n")
                print(text.getvalue())
        else:
            tempargs = tuple(tuple(i.split("=")) for i in argv[3:])
            for i in tempargs:
                section, key = i[0].split(".")
                if gameconf.get(section) == None or gameconf.get(section).get(key) == None:
                    print(f"Key {section}.{key} does not exist.")
                    continue
                temp = gameconf[section][key]
                value = None
                if isinstance(temp,str):
                    value = str(i[1])
                elif isinstance(temp,bool):
                    if i[1].lower() == "true":
                        value = True
                    elif i[1].lower() == "false":
                        value = False
                elif isinstance(temp,int):
                    value = int(i[1])
                elif isinstance(temp,float):
                    value = float(i[1])
                if value == None:
                    print(f"Type could not be determined. Skipping {section}.{key}")
                    continue
                gameconf[section][key] = value
            writeTOML(venvpath / "Pymin/Nimin_Prefs.toml", gameconf)
        exit()
    elif argv[1] == "install":
        if venvpath.exists() and "--overwrite" not in argv:
            print("You can not use install in an existing directory. Did you mean \"update\"?")
            exit()
        create(url,as3libversiontag)
    elif argv[1] == "update":
        if c2["isDevEnv"]:
            print("Skipped game download.")
        else:
            downloadgame(url)
        updatemodules(as3libversiontag)
    elif argv[1] == "run":
        run((pythonvenvloc, venvpath / "Pymin/Pymin.py", *argv[2:]))
    elif argv[1] == "conv":
        run((pythonvenvloc, venvpath / "Pymin/Pymin.py", "--converter"))
    elif argv[1] == "cmd":...
    elif argv[1] == "recreate" and venvpath.exists():
        withsaves = False
        if "--migrate-config" in argv:
            print("Fetching old config.")
            cfgdict = migrateConfig(getNew=True)
            print("Done.")
        if "--with-saves" in argv:
            withsaves = True
        recreate(url,as3libversiontag,cfgdict,withsaves)
    elif argv[1] == "uv" and venvpath.exists():
        if len(argv) == 2:
            rl = ["uv","--help"]
            if c2["uvGlobal"]:
                run(rl)
            elif c2["uvLocal"]:
                run(pythonm+rl)
        else:
            rl = ["uv",*argv[2:],"--python",pythonvenvloc]
            if c2["uvGlobal"]:
                run(rl)
            elif c2["uvLocal"]:
                run(pythonm+rl)
    elif argv[1] == "pip" and venvpath.exists():
        if len(argv) == 2:
            run([*pythonm, "pip","--help"])
        else:
            run([*pythonm, "pip",*argv[2:]])

if c1 != c2: #Check if config was modified
    writeTOML(cfgloc,c2)
