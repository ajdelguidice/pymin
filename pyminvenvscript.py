#!/usr/bin/env python
import requests, platform, configparser, ssl, tempfile
from shutil import rmtree, copytree, copyfile
from pathlib import Path, PurePath
from sys import argv
from subprocess import run, check_output
from urllib.request import urlopen
from io import StringIO

if platform.system() == 'Darwin':
    print('Warning: This script is untested on darwin (MacOS), things might be broken.')
    '''
    This script should not need this because it doesn't use os.fork but it's here just in case.
    https://docs.python.org/3/library/urllib.request.html
    Warning:

    On macOS it is unsafe to use this module in programs using os.fork() because
    the getproxies() implementation for macOS uses a higher-level system API.
    Set the environment variable no_proxy to * to avoid this problem (e.g.
    os.environ["no_proxy"] = "*"). 
    '''
    import os
    os.environ['no_proxy'] = '*'

def checkExistsMakeDir(dir_):
    if dir_.is_dir():
        return 1
    elif dir_.exists():
        print('Path exists but is not a directory.')
        return -1
    else:
        dir_.mkdir(parents=True)

curdir = Path(__file__).resolve().parent  # This is a workaround for python on Windows
venvpath = curdir / 'Pymin-venv'
cfgloc = None

if None in {curdir,venvpath} or '' in {str(curdir),str(venvpath)}:
    print('Error: Path is empty. Exiting to avoid problems.')
    exit()
if not (isinstance(curdir,PurePath) and isinstance(venvpath,PurePath)):
    print('Error: Path is somehow not a pathlib.Path object. Exiting because something is very wrong.')
    exit()

def create(script_url, as3libversion):
    #Sets up the virtual environment
    if venvpath == venvpath.parent:
        print('Error: venvpath is set to the root directory. You can not create a virtual environment here.')
        exit()
    print('Creating the environment...')

    checkExistsMakeDir(venvpath)  # Create directory

    # Create virtual environment
    if c2['uvGlobal']:
        run(('uv', 'venv', venvpath))
    else:    
        run((f'python', '-m', 'venv', venvpath))

    # Create config
    move = False
    if (curdir / 'pymin.toml').exists() and venvpath == curdir / 'Pymin-venv':
        inp = input('Would you like to move the existing config into the created venv? (y/N)').lower()
        if inp == 'y':
            move = True
    global cfgloc, delconf
    if move:
        c2['path'] = ''
        delconf = curdir / 'pymin.toml'
        cfgloc = venvpath / 'pymin.toml'
    elif cfgloc == None:
        cfgloc = venvpath / 'pymin.toml'
        cfgDict = {
            'cfgVersion':1,
            'path':'',
            'pyInstalledVersion':platform.python_version(),
            'uvGlobal':False,
            'uvLocal':False,
            'defaultToRun':False,
            'noSSLVerify':False,
            'noCustomHTMLParser':False,
            'isDevEnv':False
        }
        writeTOML(cfgloc, cfgDict)
    else:
        c2['path'] = str(venvpath)
    
    # Create game directory
    checkExistsMakeDir(venvpath / 'Pymin')
    print('Done')

    downloadgame(script_url)
    installmodules(as3libversion)

def installmodules(as3libversion='latest', overrideDev=False):
    #Installs the required modules using pip inside the virtual environment
    if c2['uvGlobal']:
        temp = ['uv', 'pip', 'install', '--python', pythonvenvloc] + runlist[2:]
    elif c2['uvLocal']:
        print('Installing UV...')
        run((pythonvenvloc, '-m', 'pip', 'install', 'uv'))
        print('Done')
        temp = pythonm + ['uv'] + runlist
    else:
        temp = pythonm + runlist
    print('Installing dependencies...')
    if c2['isDevEnv'] and not overrideDev:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
        temp.remove('tkhtmlview')
    elif as3libversion.lower() == 'none':
        temp.remove('as3lib')
    elif as3libversion != 'latest':
        temp.remove('as3lib')
        temp.append(f'as3lib={as3libversion}')
    run(temp)
    print('Done')
    replaceTkhtmlviewParserWithUnsafeOne()

def downloadgame(url):
    #Downloads the game
    print('Installing game... Please wait.')
    with urlopen(url,context=getSSLContext()) as urlfile:
        (venvpath / 'Pymin/Pymin.py').write_bytes(urlfile.read())
    print('Done')

def updatemodules(as3libversion):
    #Updates the required modules using pip inside the virtual environment
    if uninstallMiniAMF:
        print('Replacing Mini-AMF with as3lib-miniAMF...')
        rl = ['pip', 'uninstall', 'Mini-AMF']
        if c2['uvGlobal']:
            run(['uv'] + rl + ['--python', pythonvenvloc])
        elif c2['uvLocal']:
            run(pythonm + ['uv'] + rl)
        else:
            run(pythonm + rl)
        print('Done')
    if c2['uvGlobal']:
        temp = ['uv', 'pip', 'install', '--python', pythonvenvloc] + runlist[2:]
    elif c2['uvLocal']:
        print('Updating UV...')
        run((pythonvenvloc, '-m', 'uv', 'pip', 'install', '-U', 'uv'))
        print('Done')
        temp = pythonm + ['uv'] + runlist
    else:
        temp = pythonm + runlist
    print('Updating dependencies...')
    temp.insert(temp.index('install') + 1, '-U')
    if c2['isDevEnv']:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
        temp.remove('tkhtmlview')
    elif as3libversion.lower() == 'none':
        temp.remove('as3lib')
    elif as3libversion != 'latest':
        temp.remove('as3lib')
        temp.append(f'as3lib={as3libversion}')
    run(temp)
    print('Done')
    replaceTkhtmlviewParserWithUnsafeOne()

def recreate(url, as3libversion, withconf, withsaves, withgameconf):
    if not venvpath.is_dir():
        print(f'Error: Directory "{venvpath}" either doesn\'t exist or is not a directory. Aborting...')
        return
    if venvpath == venvpath.parent:
        print('Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...')
        return
    if not ((venvpath / 'pymin.toml').exists() and (venvpath / 'Pymin/Pymin.py').exists()):
        print('Error: venvpath does not look like it contains a valid Pymin virtual environment. Aborting...')
        return
    tempdir = None
    cfgDict = None
    try:
        if withconf:
            if (curdir / 'pymin.toml').exists():
                print('--with-config specified but config not in venv. Config skipped.')
                withconf = False
            elif (venvpath / 'pymin.toml').exists():
                with open(venvpath / 'pymin.toml','rb') as f:
                    cfgDict = tomllib.load(f)
        if withsaves or withgameconf:
            tempdir = Path(tempfile.mkdtemp())
        if withsaves:
            copytree(venvpath / 'Pymin/nimin_saves', tempdir / 'nimin_saves')
        if withgameconf:
            copyfile(venvpath / 'Pymin/Nimin_Prefs.toml', tempdir / 'Nimin_Prefs.toml')
        rmtree(venvpath)
        tempdevenv = c2['isDevEnv']
        c2['isDevEnv'] = False
        create(url, as3libversion)
        c2['isDevEnv'] = tempdevenv
        if withconf and cfgDict != None:
            writeTOML(venvpath / 'pymin.toml', cfgDict)
        if withsaves:
            copytree(tempdir / 'nimin_saves', venvpath / 'Pymin/nimin_saves')
        if withgameconf:
            copyfile(tempdir / 'Nimin_Prefs.toml', venvpath / 'Pymin/Nimin_Prefs.toml')
    except Exception as e:
        msg = 'Warning: Failed to recreate venv. '
        if tempdir != None:
            msg += f'Temp directory at {tempdir} that contains files specified with the "--with-*" arguements was not deleted to minimise data loss. '
        print(msg + 'Manual intervential is likely required.')
        #! Try to recover
        raise e
    else:
        if tempdir != None:
            rmtree(tempdir)

def replaceTkhtmlviewParserWithUnsafeOne():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands from href tags. Only use this inside of this project's virtual environment.
    if c2['isDevEnv']:
        print('Skipped custom html_parser.py.')
    elif not (tempnohtmlparser or c2['noCustomHTMLParser']):
        print('Replacing tkhtmlview html_parser.py...')
        temp = check_output((f'{pythonvenvloc}', '-c', 'import importlib.util;print(importlib.util.find_spec("tkhtmlview").origin.replace("__init__.py","html_parser.py"))')).decode('utf-8').replace('\n', '')
        if platform.system() == 'Windows':
            temp = temp.replace('\\', '/').replace('\r', '')
        with urlopen('https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/main/pyminlib/html_parser.py', context=getSSLContext()) as urlfile:
            Path(temp).write_bytes(urlfile.read())
        print('Done')

def updatePythonVersion():
    global c2
    answer = input('(Not Implemented) Python major version has changed. Would you like to switch this virtual environment to the new one? (Y/n)')
    if False and answer.lower() in {'y',''}:
        rmtree(venvpath / f'lib/python{'.'.join(pyvertuple[:2])}')
        run((*pythonm, 'venv', '--upgrade', venvpath))
        installmodules(overrideDev=True)
        c2['pyInstalledVersion'] = platform.python_version()

def migrateConfig():
    tempUV = False
    tempUVI = False
    tempDR = False
    cfgloc = venvpath / 'pymin.toml'
    conf = None
    # Get config v1 values. Do this here because these don't play nice with the others.
    if (venvpath / '.USEUV').exists():
        tempUV = True
        (venvpath / '.USEUV').unlink(missing_ok=True)
    if (venvpath / '.USEUVI').exists():
        tempUVI = True
        (venvpath / '.USEUVI').unlink(missing_ok=True)
    if (venvpath / '.DEFAULTRUN').exists():
        tempDR = True
        (venvpath / '.DEFAULTRUN').unlink(missing_ok=True)
    # Load config
    if (curdir / 'pymin.cfg').exists() or (venvpath / 'pymin.cfg').exists():
        if (curdir / 'pymin.cfg').exists():
            temploc = curdir / 'pymin.cfg'
            cfgloc = curdir / 'pymin.toml'
        else:
            temploc = venvpath / 'pymin.cfg'
        c = configparser.ConfigParser()
        c.optionxform=str
        with open(temploc,'r') as f:
            c.read_file(f)
        conf = {
            'cfgVersion':1,
            'path':c.get('Options','path',fallback=str(venvpath)),
            'pyInstalledVersion':c['Options']['pyInstalledVersion']
        }
        for i in {'uvGlobal','uvLocal','defaultToRun','noSSLVerify','noCustomHTMLParser','isDevEnv'}:
            conf[i] = c.getboolean('Options', i, fallback=False)
        temploc.unlink(missing_ok=True)
        del c
    else:
        pyversion = platform.python_version()
        with open(venvpath / 'pyvenv.cfg','r') as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            pyversion = c[configparser.UNNAMED_SECTION]['version_info']
            del c
        conf = {
            'cfgVersion':1,
            'path':'',
            'pyInstalledVersion':pyversion,
            'uvGlobal':tempUV,
            'uvLocal':tempUVI,
            'defaultToRun':tempDR,
            'noSSLVerify':False,
            'noCustomHTMLParser':False,
            'isDevEnv':False
        }
    if conf == None:
        print('Nothing to do.')
    else:
        writeTOML(cfgloc, conf)

insecure_context = ssl._create_unverified_context()

def getSSLContext():
    return insecure_context if c2['noSSLVerify'] or tempnossl else None

def indexOf(l, item):
    try:
        return l.index(item)
    except:
        return -1

class TextObject:
    def __init__(self):
        self.text = StringIO()
    def clear(self):
        self.text.close()
        self.text = StringIO()
    def get(self):
        return self.text.getvalue()
    def add(self, value):
        self.text.write(value)
    def close(self):
        self.text.close()

class Args:
    # These were put into a class to work around an issue with global variables
    def ParseInner(value):
        if value.startswith(('"',"'")) and value.endswith(('"',"'")): #string
            return value[1:-1]
        if value.isnumeric() or (value[0] == '-' and value[1:].isnumeric()): #int
            return int(value)
        if set(value) - {'.','-','1','2','3','4','5','6','7','8','9','0'} == set() and value.count('.') == 1: #float
            return float(value)
        if value.lower() == 'true':
            return True
        if value.lower() == 'false':
            return False
        return value  # Unknown
    def ValidateKey(key):
        if key.startswith(('"',"'")) and key.endswith(('"',"'")): #!Validate these
            return key
        # Bare keys
        if len(key) == 0:
            print(f'Error: TOML bare keys can not be empty.')
            exit()
        if set(key.lower()) - {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','_','-'} != set():
            print('Error: TOML bare keys can only contain ASCII letters, ASCII digits, underscores, and dashes.')
            exit()
        return key
    def ParseTable(strio):
        table = {}
        ParseKey = True
        key = TextObject()
        value = TextObject()
        while True:
            char = strio.read(1)
            if char == '':  # This should only happen at EOF
                print('Warning: Table was never closed.')
                break
            elif char == '}':
                if value.get() != '':  # Accounts for no trailing comma
                    table[Args.ValidateKey(key.get())] = Args.ParseInner(value.get())
                    key.clear()
                    value.clear()
                break
            elif char == '{':
                if ParseKey:
                    print('Error: Tables can not used as keys as they can not be parsed. Aborting.')
                    exit()
                table[Args.ValidateKey(key.get())] = Args.ParseTable(strio)
                key.clear()
            elif char == '[':
                if ParseKey:
                    print('Error: Arrays can not used as keys as they can not be parsed. Aborting.')
                    exit()
                table[Args.ValidateKey(key.get())] = Args.ParseArray(strio)
                key.clear()
            elif char == ',':
                if value.get() != '':  # Accounts for when tables are parsed
                    table[Args.ValidateKey(key.get())] = Args.ParseInner(value.get())
                value.clear()
                key.clear()
                ParseKey = True
            elif char == ':':
                ParseKey = False
            elif ParseKey:
                key.add(char)
            else:
                value.add(char)
        key.close()
        value.close()
        return table
    def ParseArray(strio):
        arr = []
        value = TextObject()
        while True:
            char = strio.read(1)
            if char == '':  # This should only happen at EOF
                print('Warning: Array was never closed.')
                break
            elif char == ']':
                if value.get() != '':  # Accounts for no trailing comma
                    arr.append(Args.ParseInner(value.get()))
                    value.clear()
                break
            elif char == '[':
                arr.append(Args.ParseArray(strio))
            elif char == '{':
                arr.append(Args.ParseTable(strio))
            elif char == ',':
                if value.get() != '':  # Accounts for when arrays are parsed
                    arr.append(Args.ParseInner(value.get()))
                    value.clear()
            else:
                value.add(char)
        value.close()
        return arr
    def ParseOuter(value, expected):
        if isinstance(expected,str):
            return str(value)
        if isinstance(expected,bool):
            if value.lower() == 'true':
                return True
            if value.lower() == 'false':
                return False
        if isinstance(expected,int):
            return int(value)
        if isinstance(expected,float):
            return float(value)
        if isinstance(expected,list):
            with StringIO() as text:
                text.write(value)
                text.seek(1)
                return Args.ParseArray(text)
        if isinstance(expected,dict):
            with StringIO() as text:
                text.write(value)
                text.seek(1)
                return Args.ParseTable(text)

class TOML:
    # These were put into a class to work around an issue with global variables
    def Value(value):
        if isinstance(value,str):
            return f'"{value}"'
        if isinstance(value,bool):
            return 'true' if value else 'false'
        if isinstance(value,(list,tuple)):
            return TOML.Array(value)
        if isinstance(value,dict):
            return TOML.Table(value)
        return f'{value}'
    def Table(value):
        with StringIO() as text:
            text.write('{')
            for k,v in value.items():
                text.write(f'{k} = {TOML.Value(v)},')
            temp = text.getvalue()
            if temp.endswith(','):  #!Make this better
                return temp[:-1] + '}'
            return temp + '}'
    def Array(value):
        with StringIO() as text:
            text.write('[')
            for i in value:
                text.write(f'{TOML.Value(i)},')
            text.write(']')
            return text.getvalue()

def writeTOML(file, valDict):
    nontables = []
    tables = []
    for k,v in valDict.items():
        if isinstance(v,dict):
            tables.append(k)
        else:
            nontables.append(k)
    with StringIO() as text:
        for k in nontables:
            text.write(f'{k} = {TOML.Value(valDict[k])}\n')
        for k in tables:
            text.write('\n')
            text.write(f'["{k}"]\n' if str(k).find('.') != -1 else f'[{k}]\n')
            for k2,v2 in valDict[k].items():
                text.write(f'{k2} = {TOML.Value(v2)}\n')
        with open(file,'w') as f:
            f.write(text.getvalue())

tempnossl = False
hasVenv = True
tempnohtmlparser = False
delconf = None
uninstallMiniAMF = False

runlist = ['pip', 'install', 'tkhtmlview', 'numpy', 'Pillow', 'as3lib', 'as3lib-miniAMF']
try:
    import tomllib
except:
    import tomli as tomllib
    runlist.append('tomli')

if (venvpath / '.USEUV').exists() or (venvpath / '.USEUVI').exists() or (venvpath / '.DEFAULTRUN').exists() or (curdir / 'pymin.cfg').exists() or (venvpath / 'pymin.cfg').exists():
    print('Old config detected. Automatically migrating to new one.')
    migrateConfig(True)
    print('Done')
if (curdir / 'pymin.toml').exists():  # load config and set venvpath
    cfgloc = curdir / 'pymin.toml'
    with open(cfgloc, 'rb') as f:
        c1 = tomllib.load(f)
    c2 = {
        'cfgVersion':c1.get('cfgVersion',1),
        'path':c1.get('path',venvpath),
        'pyInstalledVersion':c1.get('pyInstalledVersion'),
        'uvGlobal':c1.get('uvGlobal',False),
        'uvLocal':c1.get('uvLocal',False),
        'defaultToRun':c1.get('defaultToRun',False),
        'noSSLVerify':c1.get('noSSLVerify',False),
        'noCustomHTMLParser':c1.get('noCustomHTMLParser',False),
        'isDevEnv':c1.get('isDevEnv',False)
    }
    if c2['path'] == '':
        print("Error: path in config is empty. This script will break if this is not set when the config is outside of the venv.")
        exit()
    venvpath = Path(c2['path']).resolve()
    if not venvpath.exists():
        hasVenv = False
elif (venvpath / 'pymin.toml').exists():  # load config
    cfgloc = venvpath / 'pymin.toml'
    with open(cfgloc, 'rb') as f:
        c1 = tomllib.load(f)
    c2 = {
        'cfgVersion':c1.get('cfgVersion',1),
        'path':c1.get('path',''),
        'pyInstalledVersion':c1.get('pyInstalledVersion'),
        'uvGlobal':c1.get('uvGlobal',False),
        'uvLocal':c1.get('uvLocal',False),
        'defaultToRun':c1.get('defaultToRun',False),
        'noSSLVerify':c1.get('noSSLVerify',False),
        'noCustomHTMLParser':c1.get('noCustomHTMLParser',False),
        'isDevEnv':c1.get('isDevEnv',False)
    }
else:  # Use fallback values because config does not exist
    c1 = None
    c2 = {
        'cfgVersion':1,
        'pyInstalledVersion':None,
        'uvGlobal':False,
        'uvLocal':False,
        'defaultToRun':False,
        'noSSLVerify':False,
        'noCustomHTMLParser':False,
        'isDevEnv':False
    }
    if venvpath.exists():
        with open(venvpath / 'pyvenv.cfg', 'r') as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            c2['pyInstalledVersion'] = c[configparser.UNNAMED_SECTION]['version_info']
        c2['path'] = venvpath
    else:  # no venv
        c2['pyInstalledVersion'] = platform.python_version()
        hasVenv = False


if platform.system() == 'Windows':
    pythonvenvloc = venvpath / 'Scripts/python.exe'
else:
    pythonvenvloc = venvpath / 'bin/python'
pythonm = [pythonvenvloc, '-m']

if hasVenv and check_output((f'{pythonvenvloc}', '-c', 'from importlib.util import find_spec;from pathlib import Path;print(Path(find_spec("tkhtmlview").origin.replace("tkhtmlview/__init__.py","Mini_AMF-0.9.1.dist-info")).exists())')).decode('utf-8').replace('\n', '').replace('\r', '') == 'True':
    uninstallMiniAMF = True

if hasVenv and platform.python_version().split('.')[:2] != c2['pyInstalledVersion'].split('.')[:2] and platform.system() != 'Windows':
    updatePythonVersion()
if len(argv) < 2 and c2['defaultToRun']:
    run([pythonvenvloc, venvpath / 'Pymin/Pymin.py'])
elif len(argv) < 2 or 1 in {indexOf(argv,'--help'),indexOf(argv,'-h'),indexOf(argv,'help')} or 1 in {indexOf(argv,'install'),indexOf(argv,'update'),indexOf(argv,'cfg'),indexOf(argv,'cmd'),indexOf(argv,'recreate')} and 2 in {indexOf(argv,'--help'),indexOf(argv,'-h')}:
    print('venvscript [command] [args]\nCommands:\n\thelp\t\t\tDisplays this message. Also --help and -h\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it\'s dependencies.\n\tcfg\t\t\tFor configuring this script. key/values are in the form "key=value". Use without arguements to list all values.\n\tcfg-game\t\tFor modifying pymin\'s config. Works the same as cfg except key/values are in the form "section.key=value". Only works on pymin 1.0.12+.\n\tmigrate-config\t\tMigrates the config from a previous version to the current one. If an old version is detected, this runs automatically.\n\trun\t\t\tRuns the game. Forwards all arguements.\n\tconv\t\t\tRuns the savefile converter built into the game. Takes no arguements.\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes uv inside of the environment. Forwards all arguements.\n\tpip\t\t\tExecutes pip inside of the environment. Does not work if the venv was installed with uv. Forwards all arguements.\n\ncfg/cfg-game parsing rules:\n\tDo not use spaces unless they are a part of the value, whitespace is not ignored.\n\tMake sure to escape any curly brackets. They are special characters in the terminal (only tested in bash).\n\tDo not use brackets [ ] or curly brackets { } in table keys. They are currently not parsed correctly.\n\tTables use the python format {key:value,} even though they are used as TOML. I was being lazy and didn\'t want to deal it.\n\nArguements {install, update, recreate}:\n\t--unverified\t\tTemporarily disables ssl verification.\n\t--nohtmlparser\t\tSkips installing the custom html parser once.\n\t--version\t\tSpecifies the version of pymin you want to install. ex: "--version x.y.z" [default: latest]\n\t--as3libversion\t\tSpecifies the version of as3lib you want to install. ex: "--as3libversion x.y.z" [default: latest]\n\nOther Command Specific Arguements:\n\t{install}\t--overwrite\t\tBypasses the overwrite restriction. Use at your own risk.\n\t{recreate}\t--with-config\t\tReads the config and writes it to the new environment.\n\t{recreate}\t--with-saves\t\tKeeps the nimin_saves directory.\n\t{recreate}\t--with-game-config\tKeeps the game\'s config.')
elif argv[1] == 'migrate-config':
    migrateConfig()
elif c2['defaultToRun'] and (len(argv) < 2 or argv[1].startswith(('-','--','/'))):
    run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', *argv[1:]))
else:
    if argv[1] in {'install','update','recreate'}:
        if '--unverified' in argv:
            tempnossl = True
        if '--nohtmlparser' in argv:
            tempnohtmlparser = True
        if '--version' in argv:
            versiontag = argv[indexOf(argv,'--version') + 1]
        else:
            versiontag = requests.get('https://github.com/ajdelguidice/pymin/releases/latest').url.split('/')[-1]
        url = f'https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py'
        if '--as3libversion' in argv:
            as3libversiontag = argv[indexOf(argv,'--as3libversion') + 1]
        else:
            as3libversiontag = 'latest'
    if argv[1] == 'cfg':
        if cfgloc == None:
            if not hasVenv:
                cfgloc = curdir / 'pymin.toml'
            else:
                cfgloc = venvpath / 'pymin.toml'
        if len(argv) == 2:
            with StringIO() as text:
                for k,v in c2.items():
                    text.write(f'{k}: {v}\n')
                print(text.getvalue())
            exit()
        else:
            tempargs = tuple(tuple(i.split('=')) for i in argv[2:])
            for key,value in tempargs:
                if key in {'cfgVersion','pyInstalledVersion'} and not c2['isDevEnv']:
                    print(f'Warning: {key} is restricted and should not be changed. Skipping.')
                    continue
                if c2.get(key) == None:
                    print(f'Warning: Key {key} does not exist.')
                    continue
                value = Args.ParseOuter(value, c2[key])
                if value == None:
                    print(f'Warning: Type of {key} could not be determined. Skipping.')
                    continue
                c2[key] = value
    elif argv[1] == 'cfg-game':
        if not (hasVenv and (venvpath / 'Pymin/Nimin_Prefs.toml').exists()):
            print('Error: Can not read game config because it does not exist.')
            exit()
        with open(venvpath / 'Pymin/Nimin_Prefs.toml','rb') as f:
            gameconf = tomllib.load(f)
        if len(argv) == 2:
            with StringIO() as text:
                for k1,v1 in gameconf.items():
                    text.write(f'|{k1}|\n')
                    for k2,v2 in v1.items():
                        text.write(f'{k2}: {v2}\n')
                    text.write('\n')
                print(text.getvalue())
        else:
            tempargs = tuple(tuple(i.split('=')) for i in argv[2:])
            for i in tempargs:
                section, key = i[0].split('.')
                if gameconf.get(section) == None or gameconf.get(section).get(key) == None:
                    print(f'Warning: {section}.{key} does not exist.')
                    continue
                value = Args.ParseOuter(i[1], gameconf[section][key])
                if value == None:
                    print(f'Warning: Type of {section}.{key} could not be determined. Skipping.')
                    continue
                gameconf[section][key] = value
            writeTOML(venvpath / 'Pymin/Nimin_Prefs.toml', gameconf)
        exit()
    elif argv[1] == 'install':
        if hasVevn and '--overwrite' not in argv:
            print('You can not use install in an existing directory. Did you mean "update"?')
            exit()
        create(url, as3libversiontag)
    elif argv[1] == 'update':
        if c2['isDevEnv']:
            print('Skipped game download.')
        else:
            downloadgame(url)
        updatemodules(as3libversiontag)
    elif argv[1] == 'run':
        run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', *argv[2:]))
    elif argv[1] == 'conv':
        run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', '--converter'))
    elif argv[1] == 'recreate' and hasVenv:
        recreate(url, as3libversiontag, '--with-config' in argv, '--with-saves' in argv, '--with-game-config' in argv)
    elif argv[1] == 'uv' and hasVenv:
        if len(argv) == 2:
            rl = ['uv','--help']
            if c2['uvGlobal']:
                run(rl)
            elif c2['uvLocal']:
                run(pythonm + rl)
        else:
            rl = ['uv', *argv[2:], '--python', pythonvenvloc]
            if c2['uvGlobal']:
                run(rl)
            elif c2['uvLocal']:
                run(pythonm + rl)
    elif argv[1] == 'pip' and hasVenv:
        if len(argv) == 2:
            run((*pythonm, 'pip', '--help'))
        else:
            run((*pythonm, 'pip', *argv[2:]))

if c1 != c2:  # Check if config was modified
    writeTOML(cfgloc, c2)
if delconf != None:
    delconf.unlink(missing_ok=True)
