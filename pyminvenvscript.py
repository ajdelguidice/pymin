#!/usr/bin/env python
import requests, platform, configparser, ssl, tempfile, os
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
    os.environ['no_proxy'] = '*'

env = os.environ.copy()

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

class OverrideDev:
    def __init__(self):...
    def __enter__(self):
        self.dev = c2['isDevEnv']
        c2['isDevEnv'] = False
    def __exit__(self, *args):
        c2['isDevEnv'] = self.dev

def create():
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
    elif cfgloc is None:
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

    downloadgame()
    installmodules()

def set_as3libversion(rl):
    if '--as3libversion' in argv:
        version = argv[argv.index('--as3libversion') + 1]
    else:
        version = 'latest'
    if version.lower() == 'none':
        rl.remove('as3lib')
    elif version != 'latest':
        rl.remove('as3lib')
        rl.append(f'as3lib={version}')

def installmodules():
    #Installs the required modules using pip inside the virtual environment
    if c2['uvLocal']:
        print('Installing UV...')
        run((pythonvenvloc, '-m', 'pip', 'install', 'uv'))
        print('Done')
    temp = pipCommand + ['install'] + modlist
    print('Installing dependencies...')
    if c2['isDevEnv']:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
    else:
        set_as3libversion(temp)
    run(temp, env=env)
    if not c2['isDevEnv']:
        # Install tkhtmlview this way because its dependencies are broken
        run(pipCommand + ['install', '-U', 'tkhtmlview', '--no-deps'], env=env)
        patchTkhtmlviewParser()
    print('Done')

def downloadgame():
    #Downloads the game
    if c2['isDevEnv']:
        print('Skipped game download.')
        return
    print('Installing game...')
    if '--version' in argv:
        versiontag = argv[argv.index('--version') + 1]
    else:
        versiontag = requests.get('https://github.com/ajdelguidice/pymin/releases/latest').url.split('/')[-1]
    with urlopen(f'https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py', context=getSSLContext()) as urlfile:
        (venvpath / 'Pymin/Pymin.py').write_bytes(urlfile.read())
    print('Done')

def updatemodules():
    #Updates the required modules using pip inside the virtual environment
    if uninstallMiniAMF:
        print('Replacing Mini-AMF with as3lib-miniAMF...')
        run(pipCommand + ['uninstall', 'Mini-AMF'], env=env)
        print('Done')
    if c2['uvLocal']:
        print('Updating UV...')
        run((*pipCommand, 'install', '-U', 'uv'))
        print('Done')
    temp = pipCommand + ['install', '-U'] + modlist
    print('Updating dependencies...')
    if c2['isDevEnv']:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
    else:
        set_as3libversion(temp)
    run(temp, env=env)
    if not c2['isDevEnv']:
        # Update tkhtmlview this way because its dependencies are broken
        run(pipCommand + ['install', '-U', 'tkhtmlview', '--no-deps'], env=env)
        patchTkhtmlviewParser()
    print('Done')

def recreate(withconf, withsaves, withgameconf):
    if not venvpath.is_dir():
        print(f'Error: Directory "{venvpath}" either doesn\'t exist or is not a directory. Aborting...')
        return
    if venvpath == venvpath.parent:
        print('Error: venvpath is set to the root directory, this operation will harm the system if completed. Aborting...')
        return
    if not (venvpath / 'Pymin/Pymin.py').exists():
        print('Error: venvpath does not look like it contains a valid Pymin virtual environment. Aborting...')
        return
    tempdir = None
    try:
        if withconf or withsaves or withgameconf:
            tempdir = Path(tempfile.mkdtemp())
        if withconf:
            try:
                if cfgloc.exists():
                    cfgloc.relative_to(venvpath)  # Test if relative to venvpath. Will raise ValueError if not.
                    copyfile(cfgloc, tempdir / 'pymin.toml')
                else:
                    withconf = False
            except ValueError:
                print('--with-config specified but config not in venv. Config skipped.')
                withconf = False
        if withsaves:
            copytree(venvpath / 'Pymin/nimin_saves', tempdir / 'nimin_saves')
        if withgameconf:
            copyfile(venvpath / 'Pymin/Nimin_Prefs.toml', tempdir / 'Nimin_Prefs.toml')
        rmtree(venvpath)
        with OverrideDev():
            create()
        if withconf:
            copyfile(tempdir / 'pymin.toml', cfgloc)
        if withsaves:
            copytree(tempdir / 'nimin_saves', venvpath / 'Pymin/nimin_saves')
        if withgameconf:
            copyfile(tempdir / 'Nimin_Prefs.toml', venvpath / 'Pymin/Nimin_Prefs.toml')
    except Exception as e:
        msg = 'Warning: Failed to recreate venv. '
        if tempdir is not None:
            msg += f'Temp directory at {tempdir} that contains files specified with the "--with-*" arguements was not deleted to minimise data loss. '
        print(msg + 'Manual intervential is required.')
        # TODO: Try to recover
        raise e
    else:
        if tempdir is not None:
            rmtree(tempdir)

def patchTkhtmlviewParser():
    #Replaces tkhtmlview.html_parser with a modified one that can run python commands from href tags. Only use this inside of this project's virtual environment.
    if not '--nohtmlparser' in argv or c2['noCustomHTMLParser']:
        temp = check_output((f'{pythonvenvloc}', '-c', 'import importlib.util;print(importlib.util.find_spec("tkhtmlview").origin.replace("__init__.py","html_parser.py"))')).decode('utf-8').replace('\n', '')
        if platform.system() == 'Windows':
            temp = temp.replace('\\', '/').replace('\r', '')
        with urlopen('https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/dev/pyminlib/html_parser.py', context=getSSLContext()) as urlfile:
            Path(temp).write_bytes(urlfile.read())
        print('Patched tkhtmlview html_parser.py')

def updatePythonVersion(version: tuple):
    answer = input('(Experimental) Python major version has changed. Would you like to switch this virtual environment to the new one? (Y/n)')
    if c2['isDevEnv'] and answer.lower() in {'y',''}:
        tempdir = Path(tempfile.mkdtemp())
        withconf = True
        try:
            if cfgloc.exists():
                cfgloc.relative_to(venvpath)
                copyfile(cfgloc, tempdir / 'pymin.toml')
            else:
                withconf = False
        except ValueError:
            withconf = False
        copytree(venvpath / 'Pymin', tempdir / 'Pymin')
        try:
            recreate(False, False, False)
        except Exception as e:
            print(f'Temp directory at {tempdir} that contains backed up game files was not deleted to minimise data loss.')
            raise e
        if withconf:
            copyfile(tempdir / 'pymin.toml', cfgloc)
        rmtree(venvpath / 'Pymin')
        copytree(tempdir / 'Pymin', venvpath / 'Pymin')
        c2['pyInstalledVersion'] = platform.python_version()

def migrateConfig():
    conf = {}
    # Config v1
    if (venvpath / '.USEUV').exists():
        conf['uvGlobal'] = True
        (venvpath / '.USEUV').unlink(missing_ok=True)
    if (venvpath / '.USEUVI').exists():
        conf['uvLocal'] = True
        (venvpath / '.USEUVI').unlink(missing_ok=True)
    if (venvpath / '.DEFAULTRUN').exists():
        conf['defaultToRun'] = True
        (venvpath / '.DEFAULTRUN').unlink(missing_ok=True)
    # Config v2
    if (curdir / 'pymin.cfg').exists() or (venvpath / 'pymin.cfg').exists():
        if (curdir / 'pymin.cfg').exists():
            temploc = curdir / 'pymin.cfg'
        else:
            temploc = venvpath / 'pymin.cfg'
        c = configparser.ConfigParser()
        c.optionxform=str
        with open(temploc,'r') as f:
            c.read_file(f)
        if 'path' in c['Options']:
            conf['path'] = c.get('Options', 'path', fallback=str(venvpath))
        if 'pyInstalledVersion' in c['Options']:
            conf['pyInstalledVersion'] = c['Options']['pyInstalledVersion']
        for i in {'uvGlobal','uvLocal','defaultToRun','noSSLVerify','noCustomHTMLParser','isDevEnv'}:
            if i in c['Options']:
                conf[i] = c.getboolean('Options', i, fallback=False)
        temploc.unlink(missing_ok=True)
        del c
    if not conf:
        print('Nothing to do.')
    return conf

insecure_context = ssl._create_unverified_context()

def getSSLContext():
    return insecure_context if c2['noSSLVerify'] or '--unverified' in argv else None

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
        if key.startswith(('"',"'")) and key.endswith(('"',"'")): # TODO: Validate these
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
        if isinstance(value, (str, PurePath)):
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
            if temp.endswith(','):  # TODO: Make this better
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

hasVenv = True
delconf = None
uninstallMiniAMF = False
pipCommand = None

modlist = ['requests', 'numpy', 'Pillow', 'as3lib', 'as3lib-miniAMF']
try:
    import tomllib
except:
    import tomli as tomllib
    modlist.append('tomli')

cfgloc = curdir / 'pymin.toml'
if (curdir / 'pymin.toml').exists():  # load config and set venvpath
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
else:  # Load older config
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
    # Load config v2
    if (curdir / 'pymin.cfg').exists():
        c2.update(migrateConfig())
        if c2['path'] == '':
            print("Error: path in config is empty. This script will break if this is not set when the config is outside of the venv.")
            exit()
        venvpath = Path(c2['path']).resolve()
        if not venvpath.exists():
            hasVenv = False
    elif (venvpath / 'pymin.cfg').exists():
        cfgloc = venvpath / 'pymin.toml'
        c2.update(migrateConfig())
    # Fallback
    elif venvpath.exists():
        cfgloc = venvpath / 'pymin.toml'
        with open(venvpath / 'pyvenv.cfg', 'r') as f:
            c = configparser.ConfigParser(allow_unnamed_section=True)
            c.optionxform=str
            c.read_file(f)
            c2['pyInstalledVersion'] = c[configparser.UNNAMED_SECTION]['version_info']
        c2['path'] = venvpath
        # Load config v1
        if (venvpath / '.USEUV').exists() or (venvpath / '.USEUVI').exists() or (venvpath / '.DEFAULTRUN').exists():
            c2.update(migrateConfig())
    else:  # no venv
        c2['pyInstalledVersion'] = platform.python_version()
        hasVenv = False

if platform.system() == 'Windows':
    pythonvenvloc = venvpath / 'Scripts/python.exe'
else:
    pythonvenvloc = venvpath / 'bin/python'
pythonm = [pythonvenvloc, '-m']

if c2['uvGlobal']:
    pipCommand = ['uv', 'pip']
    env['UV_PYTHON'] = str(pythonvenvloc)
elif c2['uvLocal']:
    pipCommand = pythonm + ['uv', 'pip']
else:
    pipCommand = pythonm + ['pip']

if hasVenv:
    pyver = c2['pyInstalledVersion'].split('.')[:2]
    if platform.python_version().split('.')[:2] != pyver and platform.system() != 'Windows':
        updatePythonVersion(pyver)
    if check_output((f'{pythonvenvloc}', '-c', 'from importlib.util import find_spec;from pathlib import Path;print(Path(find_spec("tkhtmlview").origin.replace("tkhtmlview/__init__.py","Mini_AMF-0.9.1.dist-info")).exists())')).decode('utf-8').replace('\n', '').replace('\r', '') == 'True':
        uninstallMiniAMF = True

# Arguement parsing logic
if c2['defaultToRun'] and (len(argv) < 2 or argv[1].startswith(('-','--','/'))):
    run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', *argv[1:]))
elif len(argv) < 2 or argv[1] == 'help' or ('--help' in argv or '-h' in argv or '/?' in argv) and argv[1] not in {'uv','pip','run'}:
    print('venvscript [command] [args]\nCommands:\n\thelp\t\t\tDisplays this message. Also --help and -h\n\tdocs\t\t\tAdvanced help information. Put a command after this one to display its docs.\n\tinstall\t\t\tCreates the virtual environment for the game, installs all dependencies, and installs the game.\n\tupdate\t\t\tUpdates the game and all of it\'s dependencies.\n\tcfg\t\t\tFor configuring this script. key/values are in the form "key=value". Use without arguements to list all values.\n\tcfg-game\t\tFor configuring pymin. Works the same as cfg except key/values are in the form "section.key=value". Only works on pymin 12+.\n\tmigrate-config\t\tMigrates the config from a previous version to the current one. This runs automatically if the current config is not present and an old version is detected.\n\trun\t\t\tRuns the game. Forwards all arguements.\n\tconv\t\t\tRuns the savefile converter built into the game. Takes no arguements.\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes uv inside of the environment. Forwards all arguements.\n\tpip\t\t\tExecutes pip inside of the environment. Does not work if the venv was installed with uv. Forwards all arguements.\n\ncfg/cfg-game parsing rules:\n\tDo not use spaces unless they are a part of the value, whitespace is not ignored.\n\tMake sure to escape any curly brackets. They are special characters in the terminal (only tested in bash).\n\tDo not use brackets [ ] or curly brackets { } in table keys. They are currently not parsed correctly.\n\tTables use the python format {key:value,} even though they are used as TOML. I was being lazy and didn\'t want to deal it.\n\nArguements {install, update, recreate}:\n\t--unverified\t\tTemporarily disables ssl verification.\n\t--nohtmlparser\t\tSkips installing the custom html parser once.\n\t--version\t\tThe release tag of the pymin version you want to install. ex: "--version <tag>" [default: latest]\n\t--as3libversion\t\tThe release tag of the as3lib version you want to install. ex: "--as3libversion <tag>" [default: latest]\n\nOther Command Specific Arguements:\n\t{install}\t--overwrite\t\tBypasses the overwrite restriction. Use at your own risk.\n\t{recreate}\t--with-config\t\tReads the config and writes it to the new environment.\n\t{recreate}\t--with-saves\t\tKeeps the nimin_saves directory.\n\t{recreate}\t--with-game-config\tKeeps the game\'s config.')
elif argv[1] == 'docs':
    generalArgs = 'This command takes four general arguements (these only apply for one run):\n\t--unverified\tDisables ssl verification.\n\t--nohtmlparser\tSkips installing the custom html parser.\n\t--version\tThe release tag of the pymin version you want to install. ex: "--version <tag>" [default: latest]\n\t--as3libversion\tThe release tag of the as3lib version you want to install. ex: "--as3libversion <tag>" [default: latest]'
    forwardArgs = 'This command forwards all arguements.'
    parsingRules = 'Custom arguement parsing is used for this command. The rules are as follows:\n  1) Spaces are not ignored, they will always be a part of the result.\n  2) Some terminals use curly brackets as special characters even when inside of\n     quotes. They might have to be escaped using a \\.\n  3) Do not use brackets [ ] or curly brackets { } in table keys, they are not\n     parsed correctly.\n  4) Inline tables must be in the format {key:value,}.\n'

    # TODO: Format cfg page better
    page = {
        'install':       f'Usage: pyminvenvscript.py install [args]\n\nInstalls and sets up the virtual environment for Pymin.\n\nThis command will refuse to do anything if <venvpath> is detected to be the root\ndirectory (using "if venvpath == venvpath.parent") or if it already exists.\n\nSteps followed by this command:\n\t1) Creates the directory <venvpath> if it does not exist\n\t2) Runs the "venv" command in <venvpath>\n\t3a) If the config exists, ask the user if they want to move it into the venv\n\t3b) If not moving the config, set its "path" variable to <venvpath>\n\t3c) If the config does not exist, create one inside the venv\n\t4) Creates the directory for the game (<venvpath>/Pymin)\n\t5) Downloads the game\n\t6) Installs all of the game\'s dependencies\n\n{generalArgs}\n\nThis command takes one special arguement:\n\t--overwrite\tBypasses the overwrite check. This check is in place because this script manages\n\t\t\tthe entire virtual environment which can cause issues if it contains other data.\n\t\t\tUse at your own risk.',
        'update':        f'Usage: pyminvenvscript.py update [args]\n\nUpdates everything in the virtual environment.\n\nPlaceholder (steps)\n\n{generalArgs}',
        'cfg':           f'Usage: pyminvenvscript.py cfg [args]\n\nUsed to display and update the configuration values for this script. These\nvalues are stored in pymin.toml either in the <venvpath> directory or in the\nsame directory as this script. When changing values, they must be in the format\n"key=value". Passing no arguements to this command will display all values.\n\n{parsingRules}\n\nThe config values and their function are as follows:\n\tcfgVersion\n\t\tThe version of config used.\n\n\tpath\n\t\tThe path to the virtual environment. Loaded into <venvpath> after processing.\n\t\tThis will be blank if the virtual environment is in the default location with\n\t\tthe config is inside of it.\n\n\tpyInstalledVersion\n\t\tThe version of python used to install the venv. Used for version checks.\n\n\tuvGlobal\n\t\tToggle to make use of a global installation of uv.\n\n\tuvLocal\n\t\tToggle to use a version of uv installed in the virtual environment.\n\n\tdefaultToRun\n\t\tMakes the default command "run" instead of help.\n\n\tnoSSLVerify\n\t\tTurns off ssl verification for downloads made directly by this script. Does not\n\t\tdo anything to uv or pip.\n\n\tnoCustomHTMLParser\n\t\tDisables the installation of the modified version of tkhtmlview.html_parser\n\t\tthat is required for Pymin\'s wiki to work. Does not delete it if it is already\n\t\tinstalled\n\n\tisDevEnv\n\t\tTurns on developer mode for this script. This prevents the updating of Pymin,\n\t\tas3lib, and tkhtmlview.',
        'cfg-game':      f'Usage: pyminvenvscript.py cfg-game [args]\n\nUsed to display and update the configuration for pymin. Only works on game\nversion 12+. These values are stored in <venvpath>/Pymin/nimin_prefs.toml.\nWhen changing values, they must be in the format "section.key=value". No spaces\nare allowed. Passing no arguements to this command will display all values.\nUnlike with the cfg command, this one can not give you a description of each\nvalue because they are external and might change.\n\n{parsingRules}',
        'migrate-config': 'Usage: pyminvenvscript.py migrate-config\n\nMigrates an older versions of this script\'s config to the current one. This\ncommand does nothing if only the current config version is present.\n\nThis will automatically run if the current config is missing and any of the\nfollowing files exist:\n\t<venvpath>/.USEUV\n\t<venvpath>/.USEUVI\n\t<venvpath>/pymin.cfg\n\t<venvpath>/.DEFAULTRUN\n\t./pymin.cfg\n\nThis command takes no arguements',
        'run':           f'Usage: pyminvenvscript.py run\n\nRuns the game. The game\'s script must be at <venvpath>/Pymin/Pymin.py.\n\n{forwardArgs}',
        'conv':          f'Usage: pyminvenvscript.py conv\n\nOpens the save file converter included in the game. The game\'s script must be\nat <venvpath>/Pymin/Pymin.py.\n\nThis command takes no arguements',
        'recreate':      f'Usage: pyminvenvscript.py recreate [args]\n\nDeletes everything and starts anew.\n\nPlaceholder (steps)\n\n{generalArgs}\n\nThis arguement takes three special arguements:\n\t--with-config\tTransfers the config for this script to the new virtual environment.\n\t--with-saves\tTransfers the <venvpath>/Pymin/nimin_saves directory to the new virtual environment.\n\t--with-game-config\tTransfers the game\'s config to the new virtual environment. (only works with Nimin_Prefs.toml)',
        'uv':            f'Usage: pyminvenvscript.py uv [args]\n\nRuns uv inside of the venv.\n\n{forwardArgs} Running without arguements will run "uv --help".',
        'pip':           f'Usage: pyminvenvscript.py pip [args]\n\nRuns pip inside of the venv.\n\n{forwardArgs} Running without arguements will run "pip --help".',
    }
    if len(argv) == 2:
        msg = f'Usage: pyminvenvscript.py docs [command]\n\nThis command contains simple documentation for this script.\n\nValid [command]s are {", ".join(page.keys())}'
    else:
        msg = page.get(argv[2], f'Page "{argv[2]}" does not exist.')
    print(msg)
elif argv[1] == 'migrate-config':
    c2.update(migrateConfig())
elif argv[1] == 'cfg':
    if cfgloc is None:
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
    tempargs = tuple(tuple(i.split('=')) for i in argv[2:])
    for key,value in tempargs:
        if key in {'cfgVersion','pyInstalledVersion'} and not c2['isDevEnv']:
            print(f'Warning: {key} is restricted and should not be changed. Skipping.')
            continue
        if c2.get(key) is None:
            print(f'Warning: Key {key} does not exist.')
            continue
        value = Args.ParseOuter(value, c2[key])
        if value is None:
            print(f'Warning: Type of {key} could not be determined. Skipping.')
            continue
        c2[key] = value
elif argv[1] == 'cfg-game' and hasVenv:
    if not (venvpath / 'Pymin/Nimin_Prefs.toml').exists():
        print('Error: Can not read game config because it does not exist.')
        exit()
    with open(venvpath / 'Pymin/Nimin_Prefs.toml','rb') as f:
        gameconf = tomllib.load(f)
    if len(argv) == 2:
        with StringIO() as text:
            for k1,v1 in gameconf.items():
                text.write(f'[{k1}]\n')
                for k2,v2 in v1.items():
                    text.write(f'{k2}: {v2}\n')
                text.write('\n')
            print(text.getvalue())
    else:
        tempargs = tuple(tuple(i.split('=')) for i in argv[2:])
        for i in tempargs:
            section, key = i[0].split('.')
            if gameconf.get(section) is None or gameconf.get(section).get(key) is None:
                print(f'Warning: {section}.{key} does not exist.')
                continue
            value = Args.ParseOuter(i[1], gameconf[section][key])
            if value is None:
                print(f'Warning: Type of {section}.{key} could not be determined. Skipping.')
                continue
            gameconf[section][key] = value
        writeTOML(venvpath / 'Pymin/Nimin_Prefs.toml', gameconf)
    exit()
elif argv[1] == 'install':
    if hasVenv and '--overwrite' not in argv:
        print('You can not use install in an existing directory. Did you mean "update"?')
        exit()
    create()
elif argv[1] == 'update' and hasVenv:
    downloadgame()
    updatemodules()
elif argv[1] == 'run' and hasVenv:
    run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', *argv[2:]))
elif argv[1] == 'conv' and hasVenv:
    run((pythonvenvloc, venvpath / 'Pymin/Pymin.py', '--converter'))
elif argv[1] == 'recreate' and hasVenv:
    recreate('--with-config' in argv, '--with-saves' in argv, '--with-game-config' in argv)
elif argv[1] == 'uv' and hasVenv:
    if not (c2['uvGlobal'] or c2['uvLocal']):
        print('Error: uv is not enabled.')
        exit()
    if len(argv) == 2:
        run(pipCommand[:-1] + ['help'], env=env)
    else:
        run(pipCommand[:-1] + argv[2:], env=env)
elif argv[1] == 'pip' and hasVenv:
    if len(argv) == 2:
        run(pipCommand + ['--help'])
    else:
        run(pipCommand + argv[2:])
elif argv[1] in {'cfg-game','update','run','conv','recreate','uv','pip'}:
    print(f'{argv[1]} requires a valid virtual environment.')
else:
    print(f'Invalid command {argv[1]}')

if c1 != c2:  # Check if config was modified
    writeTOML(cfgloc, c2)
if delconf is not None:
    delconf.unlink(missing_ok=True)
