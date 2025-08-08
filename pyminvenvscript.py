#!/usr/bin/env python
import requests, platform, configparser, ssl, tempfile
from shutil import rmtree, copytree, copyfile
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
        if cfgDict == None:
            cfgDict = {"cfgVersion":1,"path":"./","pyInstalledVersion":platform.python_version(),"uvGlobal":False,"uvLocal":False,"defaultToRun":False,"noSSLVerify":False,"noCustomHTMLParser":False,"isDevEnv":False}
        writeTOML(cfgloc,cfgDict)
    else:
        c2["path"] = str(venvpath)
    
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

def recreate(url,as3libversion,cfgDict:dict=None,withsaves=False,withconf=False):
    if not venvpath.is_dir():
        print(f"Error: Directory \"{venvpath}\" either doesn't exist or is not a directory. Aborting...")
        return
    if venvpath == venvpath.parent:
        print("Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...")
        return
    if not ((venvpath / "pymin.toml").exists() and (venvpath / "Pymin/Pymin.py").exists()):
        print("Error: venvpath does not look like it contains a valid Pymin virtual environment. Aborting...")
        return
    tempdir = None
    try:
        if withsaves or withconf:
            tempdir = Path(tempfile.mkdtemp())
        if withsaves:
            copytree(venvpath / "Pymin/nimin_saves", tempdir / "nimin_saves")
        if withconf:
            copyfile(venvpath / "Pymin/Nimin_Prefs.toml", tempdir / "Nimin_Prefs.toml")
        rmtree(venvpath)
        create(url,as3libversion,cfgDict)
        if withsaves:
            copytree(tempdir / "nimin_saves", venvpath / "Pymin/nimin_saves")
        if withconf:
            copyfile(tempdir / "Nimin_Prefs.toml", venvpath / "Pymin/Nimin_Prefs.toml")
    except Exception as e:
        raise e
    finally:
        if tempdir != None:
            rmtree(tempdir)

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

def TOMLValue(key,value):
    if isinstance(value,str):
        return f'{key} = "{value}"\n'
    elif isinstance(value,bool):
        return f'{key} = {"true" if value else "false"}\n'
    else:
        return f"{key} = {value}\n"

def writeTOML(file,valDict,mode="w"):
    with StringIO() as text:
        for k1,v1 in valDict.items():
            if isinstance(v1,dict):
                text.write(f"[{k1}]\n")
                for k2,v2 in v1.items():
                    text.write(TOMLValue(k2,v2))
                text.write(f"\n")
            else:
                text.write(TOMLValue(k1,v1))
        with open(file,mode) as f:
            f.write(text.getvalue())

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

def ParseValue(value,expected):
    if isinstance(expected,str):
        return str(value)
    elif isinstance(expected,bool):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
    elif isinstance(expected,int):
        return int(value)
    elif isinstance(expected,float):
        return float(value)

tempnossl = False
hasVenv = True
tempnohtmlparser = False

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
        "path":c1.get("path",venvpath),
        "pyInstalledVersion":c1.get("pyInstalledVersion"),
        "uvGlobal":c1.get("uvGlobal",False),
        "uvLocal":c1.get("uvLocal",False),
        "defaultToRun":c1.get("defaultToRun",False),
        "noSSLVerify":c1.get("noSSLVerify",False),
        "noCustomHTMLParser":c1.get("noCustomHTMLParser",False),
        "isDevEnv":c1.get("isDevEnv",False)
    }
    venvpath = Path(c2["path"]).resolve()
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
    print("venvscript [command] [args]\nCommands:\n\thelp\t\t\tDisplays this message. Also --help and -h\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it's dependencies.\n\tcfg\t\t\tFor configuring this script. key/values are in the form \"key=value\". Use without arguements to list all values.\n\tcfg-game\t\tFor modifying pymin's config. Works the same as cfg except key/values are in the form \"section.key=value\". Only works on pymin 1.0.12+.\n\tmigrate-config\t\tMigrates the config from a previous version to the current one. If an old version is detected, this runs automatically.\n\tcmd\t\t\tEnters the virtual environment (not implemented yet)\n\trun\t\t\tRuns the game. Forwards all arguements.\n\tconv\t\t\tRuns the savefile converter built into the game. Takes no arguements.\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes uv inside of the environment. Forwards all arguements.\n\tpip\t\t\tExecutes pip inside of the environment. Does not work if the venv was installed with uv. Forwards all arguements.\n\nArguements {install, update, recreate}:\n\t--unverified\t\tTemporarily disables ssl verification.\n\t--nohtmlparser\t\tSkips installing the custom html parser once.\n\t--version\t\tSpecifies the version of pymin you want to install. ex: \"--version x.y.z\" [default: latest]\n\t--as3libversion\t\tSpecifies the version of as3lib you want to install. ex: \"--as3libversion x.y.z\" [default: latest]\n\nOther Command Specific Arguements:\n\t{install}\t--overwrite\t\tBypasses the overwrite restriction. Use at your own risk.\n\t{recreate}\t--with-config\t\tReads the config and writes it to the new environment.\n\t{recreate}\t--with-saves\t\tKeeps the nimin_saves directory.\n\t{recreate}\t--with-game-config\tKeeps the game's config.")
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
        else:
            tempargs = tuple(tuple(i.split("=")) for i in argv[2:])
            for key,value in tempargs:
                if key in {"cfgVersion","pyInstalledVersion"}:
                    print(f"Restricted value {key} can not be changed by this command.")
                if c2.get(key) == None:
                    print(f"Key {section}.{key} does not exist.")
                    continue
                value = ParseValue(value,c2[key])
                if value == None:
                    print(f"Type could not be determined. Skipping {section}.{key}")
                    continue
                c2[key] = value
    elif argv[1] == "cfg-game":
        if not (hasVenv and (venvpath / "Pymin/Nimin_Prefs.toml").exists()):
            print("Can not read game config because it does not exist.")
            exit()
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
            tempargs = tuple(tuple(i.split("=")) for i in argv[2:])
            for i in tempargs:
                section, key = i[0].split(".")
                if gameconf.get(section) == None or gameconf.get(section).get(key) == None:
                    print(f"Key {section}.{key} does not exist.")
                    continue
                value = ParseValue(i[1],gameconf[section][key])
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
        withconf = False
        if "--with-config" in argv:
            cfgdict = migrateConfig(getNew=True)
        if "--with-saves" in argv:
            withsaves = True
        if "--with-game-config" in argv:
            withconf = True
        recreate(url,as3libversiontag,cfgdict,withsaves,withconf)
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
