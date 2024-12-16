import requests, platform
from shutil import rmtree
from pathlib import Path
from sys import argv
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
    path = Path(dir_)
    if path.exists():
        if path.is_dir():
            return 1
        else:
            if silent == False:
                print("Path exists but is not a directory.")
            return -1
    else:
        path.mkdir(parents=True)

curdir = Path(__file__).resolve().parent #Here because python (Windows) treats the location from which the script is called as ./ instead of the script's directory
venvfolder = "Pymin-venv"
venvpath = curdir / venvfolder

if curdir in (None, "") or venvpath in (None, ""):
    print("Error: Path is empty. Exiting to avoid problems.")
    exit()

if platform.system() == "Windows": #Windows check
    pythonvenvloc = venvpath / "Scripts/python.exe"
else:
    pythonvenvloc = venvpath / "bin/python"

def create(script_url="",as3libversion=""):
    #Sets up the virtual environment
    if (platform.system() == "Windows" and len(str(venvpath)) in (2,3) and venvpath[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and venvpath[1] == ":") or str(venvpath) == "/":
        print("Error: venvpath is set to the root directory. Can not create a virtual environment here.")
        exit()
    print("Creating the environment...")
    #create directory
    checkExistsMakeDir(venvpath)

    #create the virtual environment
    if useuv:
        run(["uv","venv",venvpath])
        use_uv()
    else:    
        run([f"python", "-m" "venv", venvpath])
    if useuvi:
        use_uvi()

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
    urlretrieve(url, venvpath / "Pymin/Pymin.py")
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
    if as3libversion == "latest":
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
    elif (platform.system() == "Windows" and len(str(venvpath)) in (2,3) and venvpath[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and venvpath[1] == ":") or venvpath == "/":
        print("Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...")
        exit()
    else:
        rmtree(venvpath)
    create(url,as3libversion)

def replaceTkhtmlviewParserWithUnsafeOne():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands instead from href tags. Only use this inside of this project's virtual environment.
    if htmlparser == True:
        print("Replacing tkhtmlview html_parser.py with my custom one...")
        urlretrieve("https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/main/pyminlib/html_parser.py", str(check_output(f"{pythonvenvloc} -c 'import importlib.util;print(importlib.util.find_spec(\"tkhtmlview\").origin)'",shell=True))[2:][:-1].replace("\\n","").replace("__init__.py","html_parser.py"))
        print("Done")

def use_uv():
    Path(f"{venvpath}/.USEUV").touch()

def use_uvi():
    Path(f"{venvpath}/.USEUVI").touch()

useuv = False
useuvi = False
defrun = False
pythonm = [pythonvenvloc, "-m"]
runlist = ["pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools"]
args = list(argv)
if Path(f"{venvpath}/.DEFAULTRUN").exists():
    defrun = True
if len(args) < 2 and defrun:
    run([pythonvenvloc, venvpath / "Pymin/Pymin.py"])
elif len(args) < 2 or 1 in (args.indexOf("--help"),args.indexOf("-h")) or 1 in (args.indexOf("install"),args.indexOf("cmd"),args.indexOf("recreate"),args.indexOf("rezero"),args.indexOf("run")) and 2 in (args.indexOf("--help"),args.indexOf("-h")):
    print("venvscript {install|update|run|cmd|recreate|uv} [args]\nCommands:\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it's dependencies.\n\trun\t\t\tRuns the game. All arguement pass to this will be forwarded to the game instead of being used by this script.\n\tcmd\t\t\tEnters the virtual environment (not implemented yet)\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes commands with uv inside of the environment.\n\nArguements:\n\t--version\t\tSpecifies the version of the game to download [default:latest]\n\t--as3libversion\t\tSpecifies the version of as3lib to download [default:latest]\n\t--unverified\t\tBypasses ssl certification and uses the insecure context even when using https\n\t--help\t\t\tDisplays this message\n\t--nohtmlparser\t\tDoes not download my custom html parser for tkhtmlview.\n\t--use-uv\t\tUses uv instead of pip. Needs uv installed outside of venv. (persistent)\n\t--use-uvi\t\tInstalls and uses uv inside of the venv. (persistent)\n\t--default-run\t\tSets run as the default command instead of help. (persistent)\n\t--no-uv\t\t\tOpposite of --use-uv(i)\n\t--default-help\t\tOpposite of --default-run\n\t--overwrite\t\tBypasses the no overwriting restriction on the \"install\" command")
else:
    if args.indexOf("--unverified") != -1:
        import ssl
        ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context()
    if Path(f"{venvpath}/.USEUV").exists():
        useuv = True
    elif Path(f"{venvpath}/.USEUVI").exists():
        useuvi = True
    elif args.indexOf("--use-uv") != -1:
        if venvpath.exists():
            use_uv()
        useuv = True
    elif args.indexOf("--use-uv-int") != -1:
        if venvpath.exists():
            use_uvi()
        useuvi = True
    if args.indexOf("--no-uv") != -1:
        Path(f"{venvpath}/.USEUV").unlink(missing_ok=True)
        Path(f"{venvpath}/.USEUVI").unlink(missing_ok=True)
    if args.indexOf("--default-help") != -1:
        Path(f"{venvpath}/.DEFAULTRUN").unlink(missing_ok=True)
    if args.indexOf("--default-run") != -1:
        Path(f"{venvpath}/.DEFAULTRUN").touch()
    match args[1]:
        case "install":
            if venvpath.exists() and args.indexOf("--overwrite") == -1:
                print("You can not use install in an existing directory. Did you mean \"update\"?")
                exit()
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
            run([pythonvenvloc, venvpath/ "Pymin/Pymin.py", *args[2:]])
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
        case "uv":
            if venvpath.exists():
                if len(args) == 2:
                    run({"uv","--help"})
                else:
                    rl = ["uv",*args[2:],"--python",pythonvenvloc]
                    if useuv:
                        run(rl)
                    elif useuvi:
                        run([pythonvenvloc,"-m"]+rl)
