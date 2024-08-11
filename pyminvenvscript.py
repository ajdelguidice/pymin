import os, pathlib, requests, platform
from sys import argv
from subprocess import run
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

def create(script_url="",as3libversion=""):
    #create directory
    checkExistsMakeDir(f"{venvpath}")

    #create the virtual environment
    run([f"python", "-m" "venv", venvpath])

    #create game directory
    checkExistsMakeDir(f"{venvpath}{sep}Pymin")

    downloadgame(script_url)
    installmodules(as3libversion)

def installmodules(as3libversion="latest"):
    #installs the required modules using pip inside the virtual environment
    if as3libversion == "latest":
        run([pythonvenvloc, "-m", "pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools"])
    else:
        run([pythonvenvloc, "-m", "pip", "install", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", f"as3lib={as3libversion}", "setuptools"])

def downloadgame(url=""):
    #downloads the game
    print("Installing game... Please wait.")
    urlretrieve(url, f"{venvpath}{sep}Pymin{sep}Pymin.py")
    print("Done")

def updatemodules(as3libversion="latest"):
    #updates the required modules using pip inside the virtual environment
    if as3libversion == "latest":
        run([pythonvenvloc, "-m", "pip", "install", "-U", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", "as3lib", "setuptools"])
    else:
        run([pythonvenvloc, "-m", "pip", "install", "-U", "Mini-AMF", "tkhtmlview", "numpy", "Pillow", f"as3lib={as3libversion}", "setuptools"])

args = list(argv)
if args.indexOf("--help") != -1 or args.indexOf("-h") != -1 or args[1] == "help" or len(args) < 2:
    print("venvscript {install|update|run|cmd} [args]\nCommands:\n\tinstall\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\tUpdates the game and all of it's dependencies.\n\trun\t\tRuns the game. All arguement pass to this will be forwarded to the game instead of being used by this script.\n\tcmd\t\tEnters the virtual environment (not implemented yet)\n\nArguements:\n\t--version\t\tSpecifies the version of the game to download [default:latest]\n\t--as3libversion\t\tSpecifies the version of as3lib to download [default:latest]\n\t--unverified\t\tBypasses ssl certification and uses the insecure context even when using https\n\t--help\t\tDisplays this message")
else:
    if args.indexOf("--unverified") != -1:
        import ssl
        ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context()
    match args[1]:
        case "install":
            pass
            if args.indexOf("--version") != -1:
                versiontag = args[args.indexOf("--version") + 1]
            else:
                versiontag = requests.get("https://github.com/ajdelguidice/pymin/releases/latest").url.split("/")[-1]
            url = f"https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py"
            if args.indexOf("--as3libversion") != -1:
                as3libversiontag = args[args.indexOf("--as3libversion") + 1]
            else:
                as3libversiontag = "latest"
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
            downloadgame(url)
            updatemodules(as3libversiontag)
        case "run":
            run([pythonvenvloc, f"{venvpath}{sep}Pymin{sep}Pymin.py", *args[2:]])
        case "cmd":
            pass
