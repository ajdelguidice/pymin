import os, pathlib, requests, platform
from sys import argv, version_info
from subprocess import run, check_output
from urllib.parse import urlparse
from urllib.request import urlretrieve

class list(list):
    #Needed because list.index sucks
    def indexOf(self, item):
        try:
            return self.index(item)
        except:
            return -1

def checkExistsMakeDir(dir_, silent=False):
    dn = os.path.dirname(__file__)
    #workaround for when python puts /. at the end of file paths
    if dn[(len(dn)-2):] == "/.":
        dn = dn[:(len(dn)-1)]
    #resolves local paths
    if dir_[:2]=="./":
        path = dn + dir_[2:]
    else:
        path = dir_
    if pathlib.Path(path).exists():
        if pathlib.Path(path).is_dir():
            return 1
        else:
            if silent == False:
                print("Path exists but is not a directory.")
            return -1
    else:
        os.mkdir(path)

curdir = os.path.dirname(os.path.abspath(__file__)) #current directory
venvfolder = "Pymin-venv"

if platform.system() == "Windows": #Windows check
    pythonvenvloc = f"{curdir}\\{venvfolder}\\Scripts\\python.exe"
    sep = "\\"
else:
    pythonvenvloc = f"{curdir}/{venvfolder}/bin/python"
    sep = "/"

venvpath = f"{curdir}{sep}{venvfolder}" #virtual environment directory

if curdir in (None, "") or venvpath in (None, ""):
    print("Error: Path is empty. Exiting to avoid problems.")
    exit()

def create(script_url="",as3libversion=""):
    #Sets up the virtual environment
    if (platform.system() == "Windows" and len(venvpath) in (2,3) and venvpath[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and venvpath[1] == ":") or venvpath == "/":
        print("Error: venvpath is set to the root directory. Can not create a virtual environment here.")
        exit()
    print("Creating the environment...")
    #create directory
    checkExistsMakeDir(f"{venvpath}")

    #create the virtual environment
    if useuv:
        run(["uv","venv",venvpath])
        use_uv()
    else:    
        run([f"python", "-m" "venv", venvpath])
    if useuvi:
        use_uvi()

    #create game directory
    checkExistsMakeDir(f"{venvpath}{sep}Pymin")
    print("Done")

    downloadgame(script_url)
    installmodules(as3libversion)

def installmodules(as3libversion="latest"):
    global runlist
    #installs the required modules using pip inside the virtual environment
    if useuv:
        runlist = ["uv", "pip", "install", "--python", f"{pythonvenvloc}"] + runlist[2:]
    elif useuvi:
        print("Installing UV...")
        run([pythonvenvloc, "-m", "pip", "install", "uv"])
        print("Done")
        runlist = pythonm + ["uv"] + runlist
    print("Installing dependencies...")
    if as3libversion == "latest":
        run(runlist)
    else:
        temp = runlist.copy()
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
        run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def downloadgame(url=""):
    #downloads the game
    print("Installing game... Please wait.")
    urlretrieve(url, f"{venvpath}{sep}Pymin{sep}Pymin.py")
    print("Done")

def updatemodules(as3libversion="latest"):
    global runlist
    #updates the required modules using pip inside the virtual environment
    if useuv:
        runlist = ["uv", "pip", "install", "--python", f"{pythonvenvloc}"] + runlist[2:]
    elif useuvi:
        print("Installing UV...")
        run([pythonvenvloc, "-m", "uv", "pip", "install", "-U", "uv"])
        print("Done")
        runlist = pythonm + ["uv"] + runlist
    print("Updating dependencies...")
    temp = runlist.copy()
    temp.insert(temp.index("install")+1,"-U")
    if as3libversion == "latest":
        run(temp)
    else:
        temp.remove("as3lib")
        temp.append(f"as3lib={as3libversion}")
        run(temp)
    print("Done")
    replaceTkhtmlviewParserWithUnsafeOne()

def rezero(url,as3libversion):
    if pathlib.Path(venvpath).is_dir() == False:
        print(f"Error: Directory \"{venvpath}\" either doesn't exist or is not a directory.")
        return
    elif (platform.system() == "Windows" and len(venvpath) in (2,3) and venvpath[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and venvpath[1] == ":") or venvpath == "/":
        print("Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...")
        exit()
    else:
        os.rmdir(venvpath)
    create(url,as3libversion)

def replaceTkhtmlviewParserWithUnsafeOne():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands instead from href tags. Only use this inside of this project's virtual environment.
    if htmlparser == True:
        print("Replacing tkhtmlview html_parser.py with my custom one...")
        urlretrieve("https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/main/pyminlib/html_parser.py", str(check_output(f"{pythonvenvloc} -c 'import importlib.util;print(importlib.util.find_spec(\"tkhtmlview\").origin)'",shell=True))[2:][:-1].replace("\\n","").replace("__init__.py","html_parser.py"))
        print("Done")

def use_uv():
    pathlib.Path(f"{venvpath}/.USEUV").touch()

def use_uvi():
    pathlib.Path(f"{venvpath}/.USEUVI").touch()

useuv = False
useuvi = False
defrun = False
pythonm = [pythonvenvloc, "-m"]
runlist = ["pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools"]
args = list(argv)
if pathlib.Path(f"{venvpath}/.DEFAULTRUN").exists():
    defrun = True
if len(args) < 2 and defrun:
    run([pythonvenvloc, f"{venvpath}{sep}Pymin{sep}Pymin.py"])
elif len(args) < 2 or args.indexOf("--help") != -1 or args.indexOf("-h") != -1 or args[1] == "help":
    print("venvscript {install|update|run|cmd} [args]\nCommands:\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it's dependencies.\n\trun\t\t\tRuns the game. All arguement pass to this will be forwarded to the game instead of being used by this script.\n\tcmd\t\t\tEnters the virtual environment (not implemented yet)\n\trecreate\t\tDeletes everything and starts again.\n\nArguements:\n\t--version\t\tSpecifies the version of the game to download [default:latest]\n\t--as3libversion\t\tSpecifies the version of as3lib to download [default:latest]\n\t--unverified\t\tBypasses ssl certification and uses the insecure context even when using https\n\t--help\t\t\tDisplays this message\n\t--nohtmlparser\t\tDoes not download my custom html parser for tkhtmlview.\n\t--use-uv\t\tUses uv instead of pip. Needs uv installed outside of venv. (persistent)\n\t--use-uvi\t\tInstalls and uses uv inside of the venv. (persistent)\n\t--default-run\t\tSets run as the default command instead of help. (persistent)")
else:
    if args.indexOf("--unverified") != -1:
        import ssl
        ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context()
    if pathlib.Path(f"{venvpath}/.USEUV").exists():
        useuv = True
    elif pathlib.Path(f"{venvpath}/.USEUVI").exists():
        useuvi = True
    elif args.indexOf("--use-uv") != -1:
        if pathlib.Path(venvpath).exists():
            use_uv()
        useuv =True
    elif args.indexOf("--use-uv-int") != -1:
        if pathlib.Path(venvpath).exists():
            use_uvi()
        useuvi = True
        runlist.insert(runlist.index("-m")+1,"uv")
    if args.indexOf("--default-run") != -1:
        pathlib.Path(f"{venvpath}/.DEFAULTRUN").touch()
    match args[1]:
        case "install":
            if args.indexOf("--version") != -1:
                versiontag = args[args.indexOf("--version") + 1]
            else:
                versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
            url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
            if args.indexOf("--as3libversion") != -1:
                as3libversiontag = args[args.indexOf("--as3libversion") + 1]
            else:
                as3libversiontag = "latest"
            if args.indexOf("--nohtmlparser") != -1:
                htmlparser = False
            else:
                htmlparser = True
            create(url,as3libversiontag)
        case "update":
            if args.indexOf("--version") != -1:
                versiontag = args[args.indexOf("--version") + 1]
            else:
                versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
            url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
            if args.indexOf("--as3libversion") != -1:
                as3libversiontag = args[args.indexOf("--as3libversion") + 1]
            else:
                as3libversiontag = "latest"
            if args.indexOf("--nohtmlparser") != -1:
                htmlparser = False
            else:
                htmlparser = True
            downloadgame(url)
            updatemodules(as3libversiontag)
        case "run":
            run([pythonvenvloc, f"{venvpath}{sep}Pymin{sep}Pymin.py", *args[2:]])
        case "cmd":
            pass
        case "recreate" | "rezero":
            if args.indexOf("--version") != -1:
                versiontag = args[args.indexOf("--version") + 1]
            else:
                versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
            url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
            if args.indexOf("--as3libversion") != -1:
                as3libversiontag = args[args.indexOf("--as3libversion") + 1]
            else:
                as3libversiontag = "latest"
            if args.indexOf("--nohtmlparser") != -1:
                htmlparser = False
            else:
                htmlparser = True
            rezero(url,as3libversiontag)
