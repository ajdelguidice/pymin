#!/usr/bin/env python
from io import StringIO
from pathlib import Path, PurePath
from shutil import rmtree, copytree, copyfile
from urllib.request import urlopen
import configparser
import os
import platform
import ssl
import subprocess
import sys
import tempfile


# TODO: Improve compatibility with non-uv setups


CURRENT_DIRECTORY = Path(__file__).resolve().parent

if not CURRENT_DIRECTORY:
    raise Exception('Path is empty. Exiting to avoid problems.')


def checkExistsMakeDir(dir_):
    if dir_.is_dir():
        return 1
    if dir_.exists():
        print('Path exists but is not a directory.')
        return -1
    dir_.mkdir(parents=True)


def getRedirectURL(url):
    return urlopen(url).geturl()


class OverrideDev:
    def __enter__(self):
        self.dev = config['isDevEnv']
        config['isDevEnv'] = False

    def __exit__(self, *args):
        config['isDevEnv'] = self.dev


def create():
    # Sets up the virtual environment
    if venv.path == venv.path.parent:
        raise Exception('Root directory can not be used for venvpath.')
    print('Creating the environment...')

    checkExistsMakeDir(venv.path)  # Create directory

    # Create virtual environment
    if config['uvGlobal']:
        subprocess.run(('uv', 'venv', venv.path))
    else:
        subprocess.run(('python', '-m', 'venv', venv.path))

    # Create config
    move = False
    if (CURRENT_DIRECTORY / 'pymin.toml').exists() and venv.path == CURRENT_DIRECTORY / 'Pymin-venv':
        inp = input('Would you like to move the existing config into the created venv? (y/N)').lower()
        if inp == 'y':
            move = True
    global cfgloc
    if move:
        config['path'] = ''
        cfgloc = venv.getLocalPath('pymin.toml')
        TOML.write(config, cfgloc)
        (CURRENT_DIRECTORY / 'pymin.toml').unlink(missing_ok=True)
    else:
        config['path'] = str(venv.path)

    # Create game directory
    checkExistsMakeDir(venv.getLocalPath('Pymin'))
    print('Done')

    downloadgame()
    installmodules()


def set_as3libversion(rl):
    if '--as3libversion' in sys.argv:
        version = sys.argv[sys.argv.index('--as3libversion') + 1]
    else:
        version = 'latest'
    if version.lower() == 'none':
        rl.remove('as3lib')
    elif version != 'latest':
        rl.remove('as3lib')
        rl.append(f'as3lib={version}')


def installmodules():
    # Installs the required modules using pip inside the virtual environment
    if config['uvLocal']:
        print('Installing UV...')
        venv.runWithPython('-m', 'pip', 'install', 'uv')
        print('Done')
    temp = VenvRunner.REQUIREMENTS.copy()
    print('Installing dependencies...')
    if config['isDevEnv']:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
    else:
        set_as3libversion(temp)
    venv.pipInstall(*temp)
    if not config['isDevEnv']:
        # Install tkhtmlview this way because its dependencies are broken
        venv.pipUpdate('tkhtmlview', '--no-deps')
        patchTkhtmlviewParser()
    print('Done')


def downloadgame():
    # Downloads the game
    if config['isDevEnv']:
        print('Skipped game download.')
        return
    print('Installing game...')
    if '--version' in sys.argv:
        versiontag = sys.argv[sys.argv.index('--version') + 1]
    else:
        versiontag = getRedirectURL('https://github.com/ajdelguidice/pymin/releases/latest').split('/')[-1]
    with urlopen(f'https://github.com/ajdelguidice/pymin/releases/download/{versiontag}/Pymin.py', context=venv.sslContext) as urlfile:
        venv.getLocalPath('Pymin/Pymin.py').write_bytes(urlfile.read())
    print('Done')


def updatemodules():
    # Updates the required modules using pip inside the virtual environment
    if subprocess.check_output((venv.python, '-c', 'from importlib.util import find_spec;import os;print(os.path.exists(find_spec("tkhtmlview").origin.replace("tkhtmlview/__init__.py","Mini_AMF-0.9.1.dist-info")))')).decode('utf-8').strip() == 'True':
        print('Replacing Mini-AMF with as3lib-miniAMF...')
        venv.pipUninstall('Mini-AMF')
        print('Done')
    if config['uvLocal']:
        print('Updating UV...')
        venv.pipUpdate('uv')
        print('Done')
    temp = VenvRunner.REQUIREMENTS.copy()
    print('Updating dependencies...')
    if config['isDevEnv']:
        print('Skipping as3lib and tkhtmlview.')
        temp.remove('as3lib')
    else:
        set_as3libversion(temp)
    venv.pipUpdate(*temp)
    if not config['isDevEnv']:
        # Update tkhtmlview this way because its dependencies are broken
        venv.pipUpdate('tkhtmlview', '--no-deps')
        patchTkhtmlviewParser()
    print('Done')


def recreate_checkWithConfig(withconf):
    if not withconf or not cfgloc.exists():
        return False
    try:
        # Test if relative to venvpath. Raises ValueError if not.
        cfgloc.relative_to(venv.path)
    except ValueError:
        print('Option "withConfig" specified but config not in venv. Config skipped.')
        return False
    return True


def recreate(withconf, withsaves, withgameconf, source_tempdir: PurePath = None):
    if not venv.path.is_dir():
        raise Exception(f'Directory "{venv.path}" either doesn\'t exist or is not a directory.')
    if venv.path == venv.path.parent:
        raise Exception('Root directory can not be used for venvpath.')
    if not venv.getLocalPath('Pymin/Pymin.py').exists():
        raise Exception('venvpath does not look like it contains a valid Pymin virtual environment.')
    withconf = recreate_checkWithConfig(withconf)
    if source_tempdir is not None:
        tempdir = source_tempdir
    elif withconf or withsaves or withgameconf:
        tempdir = Path(tempfile.mkdtemp())
    try:
        if withconf:
            copyfile(cfgloc, tempdir / 'pymin.toml')
        if withsaves:
            copytree(venv.getLocalPath('Pymin/nimin_saves'), tempdir / 'nimin_saves')
        if withgameconf:
            copyfile(venv.getLocalPath('Pymin/Nimin_Prefs.toml'), tempdir / 'Nimin_Prefs.toml')
        rmtree(venv.path)
        with OverrideDev():
            create()
        if withconf:
            copyfile(tempdir / 'pymin.toml', cfgloc)
        if withsaves:
            copytree(tempdir / 'nimin_saves', venv.getLocalPath('Pymin/nimin_saves'))
        if withgameconf:
            copyfile(tempdir / 'Nimin_Prefs.toml', venv.getLocalPath('Pymin/Nimin_Prefs.toml'))
    except Exception as e:
        msg = 'Warning: Failed to recreate venv. '
        if tempdir is not None:
            msg += f'Temp directory at "{tempdir}" that contains files specified with the "--with-*" arguments was not deleted to minimise data loss. '
        # TODO: Try to recover
        raise Exception(msg + 'Manual intervential is required.') from e
    else:
        if source_tempdir is None and tempdir is not None:
            rmtree(tempdir)


def patchTkhtmlviewParser():
    # Replaces tkhtmlview.html_parser with a modified one that can run python commands from href tags. Only use this inside of this project's virtual environment.
    if '--nohtmlparser' not in sys.argv or config['noCustomHTMLParser']:
        temp = subprocess.check_output((venv.python, '-c', 'import importlib.util;print(importlib.util.find_spec("tkhtmlview").origin.replace("__init__.py","html_parser.py"))')).decode('utf-8').strip()
        with urlopen('https://raw.githubusercontent.com/ajdelguidice/pymin/refs/heads/dev/pyminlib/html_parser.py', context=venv.sslContext) as urlfile:
            Path(temp).write_bytes(urlfile.read())
        print('Patched tkhtmlview html_parser.py')


def updatePythonVersion():
    tempdir = Path(tempfile.mkdtemp())
    copytree(venv.getLocalPath('Pymin'), tempdir / 'Pymin')
    try:
        recreate(True, False, False, tempdir)
    except Exception as e:
        raise Exception(f'An error has occurred during the python version change process. The temp directory at "{tempdir}" contains all backed up files. Manual intervention is required.') from e
    else:
        rmtree(venv.getLocalPath('Pymin'))
        copytree(tempdir / 'Pymin', venv.getLocalPath('Pymin'))
        rmtree(tempdir)
        config['pyInstalledVersion'] = platform.python_version()


def migrateConfig():
    conf = {}
    # Config v1
    if venv.getLocalPath('.USEUV').exists():
        conf['uvGlobal'] = True
        venv.getLocalPath('.USEUV').unlink(missing_ok=True)
    if venv.getLocalPath('.USEUVI').exists():
        conf['uvLocal'] = True
        venv.getLocalPath('.USEUVI').unlink(missing_ok=True)
    if venv.getLocalPath('.DEFAULTRUN').exists():
        conf['defaultToRun'] = True
        venv.getLocalPath('.DEFAULTRUN').unlink(missing_ok=True)
    # Config v2
    if (CURRENT_DIRECTORY / 'pymin.cfg').exists() or venv.getLocalPath('pymin.cfg').exists():
        if (CURRENT_DIRECTORY / 'pymin.cfg').exists():
            temploc = CURRENT_DIRECTORY / 'pymin.cfg'
        else:
            temploc = venv.getLocalPath('pymin.cfg')
        c = configparser.ConfigParser()
        c.optionxform = str
        with open(temploc, 'r') as f:
            c.read_file(f)
        if 'path' in c['Options']:
            conf['path'] = c.get('Options', 'path', fallback=str(venv.path))
        if 'pyInstalledVersion' in c['Options']:
            conf['pyInstalledVersion'] = c['Options']['pyInstalledVersion']
        for i in {'uvGlobal', 'uvLocal', 'defaultToRun', 'noSSLVerify', 'noCustomHTMLParser', 'isDevEnv'}:
            if i in c['Options']:
                conf[i] = c.getboolean('Options', i, fallback=False)
        temploc.unlink(missing_ok=True)
        del c
    if not conf:
        print('Nothing to do.')
    return conf


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
        # string
        if value.startswith(('"', "'")) and value.endswith(('"', "'")):
            return value[1: -1]
        # int
        if value.isnumeric() or (value[0] == '-' and value[1:].isnumeric()):
            return int(value)
        # float
        if set(value) - {'.', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} == set() and value.count('.') == 1:
            return float(value)
        # true
        if value.lower() == 'true':
            return True
        # false
        if value.lower() == 'false':
            return False
        # Unknown
        return value

    def ValidateKey(key):
        if key.startswith(('"', "'")) and key.endswith(('"', "'")):  # TODO: Validate these
            return key
        # Bare keys
        if len(key) == 0:
            raise Exception('TOML bare keys can not be empty.')
        if set(key.lower()) - {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '-'} != set():
            raise Exception('TOML bare keys can only contain ASCII letters, ASCII digits, underscores, and dashes.')
        return key

    def ParseTable(strio):
        table = {}
        ParseKey = True
        key = TextObject()
        value = TextObject()
        while (char := strio.read(1)) != '}':
            # No character means end of stream
            if char == '':
                print('Warning: Table was never closed.')
                break
            if char == '{':
                if ParseKey:
                    raise Exception('Tables can not used as keys as they can not be parsed.')
                table[Args.ValidateKey(key.get())] = Args.ParseTable(strio)
                key.clear()
            elif char == '[':
                if ParseKey:
                    raise Exception('Arrays can not used as keys as they can not be parsed.')
                table[Args.ValidateKey(key.get())] = Args.ParseArray(strio)
                key.clear()
            elif char == ',':
                # Arrays and tables parse separately so avoid writing an empty value
                if value.get() != '':
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
        # Write final value if there isn't a trailing comma
        if value.get() != '':
            table[Args.ValidateKey(key.get())] = Args.ParseInner(value.get())
        key.close()
        value.close()
        return table

    def ParseArray(strio):
        arr = []
        value = TextObject()
        while (char := strio.read(1)) != ']':
            # No character means end of stream
            if char == '':
                print('Warning: Array was never closed.')
                break
            if char == '[':
                arr.append(Args.ParseArray(strio))
            elif char == '{':
                arr.append(Args.ParseTable(strio))
            elif char == ',':
                # Arrays and tables parse separately so avoid writing an empty value
                if value.get() != '':
                    arr.append(Args.ParseInner(value.get()))
                value.clear()
            else:
                value.add(char)
        # Write final value if there isn't a trailing comma
        if value.get() != '':
            arr.append(Args.ParseInner(value.get()))
        value.close()
        return arr

    def Parse(value, expectedType):
        if expectedType is bool:
            if value.lower() == 'true':
                return True
            if value.lower() == 'false':
                return False
        if expectedType is list:
            with StringIO() as text:
                text.write(value)
                text.seek(1)
                return Args.ParseArray(text)
        if expectedType is dict:
            with StringIO() as text:
                text.write(value)
                text.seek(1)
                return Args.ParseTable(text)
        return expectedType(value)


class TOML:
    # These were put into a class to work around an issue with global variables
    def Value(value):
        if isinstance(value, PurePath):
            value = str(value).replace('\\', '/')
        if isinstance(value, str):
            return f'"{value}"'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (list, tuple)):
            return TOML.Array(value)
        if isinstance(value, dict):
            return TOML.Table(value)
        return f'{value}'

    def Table(value):
        with StringIO() as text:
            text.write('{')
            for k, v in value.items():
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

    def dictToTOML(valDict):
        nontables = []
        tables = []
        for k, v in valDict.items():
            if isinstance(v, dict):
                tables.append(k)
            else:
                nontables.append(k)
        with StringIO() as text:
            for k in nontables:
                text.write(f'{k} = {TOML.Value(valDict[k])}\n')
            for k in tables:
                text.write(f'\n["{k}"]\n' if str(k).find('.') != -1 else f'\n[{k}]\n')
                for k2, v2 in valDict[k].items():
                    text.write(f'{k2} = {TOML.Value(v2)}\n')
            return text.getvalue()

    def write(file, valDict):
        with open(file, 'w') as f:
            f.write(TOML.dictToTOML(valDict))


hasVenv = True

if sys.hexversion < 0x030b0000:
    import tomli
    TOML.readFile = tomli.load
    require_tomli = True
else:
    import tomllib
    TOML.readFile = tomllib.load
    require_tomli = False


class VenvRunner:
    INSECURE_SSL_CONTEXT = ssl._create_unverified_context()
    REQUIREMENTS = ['numpy', 'Pillow', 'as3lib']
    if require_tomli:
        REQUIREMENTS.append('tomli')

    @property
    def env(self):
        return self._environ

    @property
    def sslContext(self):
        return VenvRunner.INSECURE_SSL_CONTEXT if config['noSSLVerify'] or '--unverified' in sys.argv else None

    @property
    def path(self):
        return self._venv

    @path.setter
    def path(self, value):
        self._venv = value
        self.env['UV_PYTHON'] = self.python

    @property
    def python(self):
        if platform.system() == 'Windows':
            return os.path.join(self.path, 'Scripts', 'python.exe')
        return os.path.join(self.path, 'bin', 'python')

    @property
    def pipCommand(self):
        if config['uvGlobal']:
            return ('uv', 'pip')
        if config['uvLocal']:
            return (self.python, '-m', 'uv', 'pip')
        return (self.python, '-m', 'pip')

    def __init__(self):
        self._environ = os.environ.copy()

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
            self.env['no_proxy'] = '*'

        self.path = CURRENT_DIRECTORY / 'Pymin-venv'

    def getLocalPath(self, path):
        # return os.path.join(self.path, *path)
        return self.path / path

    def runWithEnv(self, *args):
        subprocess.run(args, env=self.env)

    def runWithPython(self, *args):
        self.runWithEnv(self.python, *args)

    def pip(self, *args):
        self.runWithEnv(*self.pipCommand, *args)

    def pipInstall(self, *args):
        self.pip('install', *args)

    def pipUpdate(self, *args):
        self.pip('install', '-U', *args)

    def pipUninstall(self, *args):
        self.pip('uninstall', *args)


venv = VenvRunner()

cfgloc = CURRENT_DIRECTORY / 'pymin.toml'
ORIGINAL_CONFIG = None
config = None

# load config and set venvpath
if (CURRENT_DIRECTORY / 'pymin.toml').exists():
    with open(cfgloc, 'rb') as f:
        ORIGINAL_CONFIG = TOML.readFile(f)
    config = {
        'cfgVersion': ORIGINAL_CONFIG.get('cfgVersion', 1),
        'path': ORIGINAL_CONFIG.get('path', venv.path),
        'pyInstalledVersion': ORIGINAL_CONFIG.get('pyInstalledVersion'),
        'uvGlobal': ORIGINAL_CONFIG.get('uvGlobal', False),
        'uvLocal': ORIGINAL_CONFIG.get('uvLocal', False),
        'defaultToRun': ORIGINAL_CONFIG.get('defaultToRun', False),
        'noSSLVerify': ORIGINAL_CONFIG.get('noSSLVerify', False),
        'noCustomHTMLParser': ORIGINAL_CONFIG.get('noCustomHTMLParser', False),
        'isDevEnv': ORIGINAL_CONFIG.get('isDevEnv', False)
    }
    if config['path'] == '':
        raise Exception('Config is not in the default venv location and venvpath is empty.')
    venv.path = Path(config['path']).resolve()
    if not venv.path.exists():
        hasVenv = False
# load config
elif venv.getLocalPath('pymin.toml').exists():
    cfgloc = venv.getLocalPath('pymin.toml')
    with open(cfgloc, 'rb') as f:
        ORIGINAL_CONFIG = TOML.readFile(f)
    config = {
        'cfgVersion': ORIGINAL_CONFIG.get('cfgVersion', 1),
        'path': ORIGINAL_CONFIG.get('path', ''),
        'pyInstalledVersion': ORIGINAL_CONFIG.get('pyInstalledVersion'),
        'uvGlobal': ORIGINAL_CONFIG.get('uvGlobal', False),
        'uvLocal': ORIGINAL_CONFIG.get('uvLocal', False),
        'defaultToRun': ORIGINAL_CONFIG.get('defaultToRun', False),
        'noSSLVerify': ORIGINAL_CONFIG.get('noSSLVerify', False),
        'noCustomHTMLParser': ORIGINAL_CONFIG.get('noCustomHTMLParser', False),
        'isDevEnv': ORIGINAL_CONFIG.get('isDevEnv', False)
    }
# Load older config
else:
    config = {
        'cfgVersion': 1,
        'pyInstalledVersion': None,
        'uvGlobal': False,
        'uvLocal': False,
        'defaultToRun': False,
        'noSSLVerify': False,
        'noCustomHTMLParser': False,
        'isDevEnv': False
    }
    # Load config v2
    if (CURRENT_DIRECTORY / 'pymin.cfg').exists():
        config.update(migrateConfig())
        if config['path'] == '':
            raise Exception('Config is not in the default venv location and "path" is empty.')
        venv.path = Path(config['path']).resolve()
        if not venv.path.exists():
            hasVenv = False
    elif venv.getLocalPath('pymin.cfg').exists():
        cfgloc = venv.getLocalPath('pymin.toml')
        config.update(migrateConfig())
    # Fallback
    elif venv.path.exists():
        cfgloc = venv.getLocalPath('pymin.toml')
        with open(venv.getLocalPath('pyvenv.cfg'), 'r') as f:
            if hasattr(configparser, 'UNNAMED_SECTION'):
                UNNAMED_SECTION = configparser.UNNAMED_SECTION
                c = configparser.ConfigParser(allow_unnamed_section=True)
                c.optionxform = str
                c.read_file(f)
            else:  # Python < 3.13
                UNNAMED_SECTION = 'UNNAMED_SECTION'
                c = configparser.ConfigParser()
                c.optionxform = str
                c.read_string('[UNNAMED_SECTION]\n' + f.read())
            config['pyInstalledVersion'] = c[UNNAMED_SECTION]['version_info']
        config['path'] = str(venv.path)
        # Load config v1
        if venv.getLocalPath('.USEUV').exists() or venv.getLocalPath('.USEUVI').exists() or venv.getLocalPath('.DEFAULTRUN').exists():
            config.update(migrateConfig())
    # no venv
    else:
        config['pyInstalledVersion'] = platform.python_version()
        hasVenv = False


DOCS_GENERAL_ARGS = 'General arguments:\n\t--unverified\tDisables ssl verification.\n\t--nohtmlparser\tSkips installing the custom html parser.\n\t--version\tThe release tag of the pymin version you want to install. ex: "--version <tag>" [default: latest]\n\t--as3libversion\tThe release tag of the as3lib version you want to install. ex: "--as3libversion <tag>" [default: latest]'
DOCS_FORWARDS_ARGS = 'Forwards all arguments.'
DOCS_NO_ARGS = 'Takes no arguments'
DOCS_PARSING_RULES = 'Custom argument parsing is used for this command. The rules are as follows:\n\t1) Do not use whitespace unless necessary.\n\t2) Escape all special characters recognised by your terminal\n\t   (ex: curly brackets in bash).\n\t3) Do not use brackets [ ] or curly brackets { } in keys, they are not parsed\n\t   correctly.\n\t4) Inline tables must be in the format {key:value,}.\n'
# TODO: Format cfg page better
# TODO: update, recreate commands steps
DOCS_PAGES = {
    'install':        f'Usage: <venvscript> install [args]\n\nInstalls and sets up the virtual environment for Pymin.\n\nThis command will refuse to do anything if <venvpath> is detected to be the root\ndirectory or if it already exists.\n\nSteps followed by this command:\n\t1) Create the directory <venvpath> if it does not exist\n\t2) Run the "venv" command in <venvpath>\n\t3a) If the config exists, ask the user if they want to move it into the venv.\n\t    If not moving the config, set the "path" variable to <venvpath>.\n\t3b) If the config does not exist, create one inside the venv\n\t4) Create the game directory at "<venvpath>/Pymin"\n\t5) Download the game to "<venvpath>/Pymin/Pymin.py"\n\t6) Install the game\'s dependencies\n\n{DOCS_GENERAL_ARGS}\n\nSpecial arguement:\n\t--overwrite\tBypasses the overwrite check. This check is in place because this script manages\n\t\t\tthe entire virtual environment which can cause issues if it contains other data.\n\t\t\tUse at your own risk.',
    'update':         f'Usage: <venvscript> update [args]\n\nUpdates everything in the virtual environment.\n\nSteps followed by this command:\n\tPlaceholder\n\n{DOCS_GENERAL_ARGS}',
    'cfg':            f'Usage: <venvscript> cfg [args]\n\nDisplays and modifies the configuration for this script. These values are\nstored in pymin.toml either in the <venvpath> directory or in the same\ndirectory as this script.\nArguments must be in the format "key=value".\nDisplays the entire config when no arguments are passed.\n\n{DOCS_PARSING_RULES}\n\nThe config values and their function are as follows:\n\tcfgVersion\n\t\tThe version of config used.\n\n\tpath\n\t\tThe path to the virtual environment. Loaded into <venvpath> after processing.\n\t\tThis will be blank if the virtual environment is in the default location with\n\t\tthe config is inside of it.\n\n\tpyInstalledVersion\n\t\tThe version of python used to install the venv. Used for version checks.\n\n\tuvGlobal\n\t\tToggle to make use of a global installation of uv.\n\n\tuvLocal\n\t\tToggle to use a version of uv installed in the virtual environment.\n\n\tdefaultToRun\n\t\tMakes the default command "run" instead of help.\n\n\tnoSSLVerify\n\t\tTurns off ssl verification for downloads made directly by this script. Does not\n\t\tdo anything to uv or pip.\n\n\tnoCustomHTMLParser\n\t\tDisables the installation of the modified version of tkhtmlview.html_parser\n\t\tthat is required for Pymin\'s wiki to work. Does not delete it if it is already\n\t\tinstalled\n\n\tisDevEnv\n\t\tTurns on developer mode for this script. This prevents the updating of Pymin,\n\t\tas3lib, and tkhtmlview.',
    'cfg-game':       f'Usage: <venvscript> cfg-game [args]\n\nDisplays and modifies the configuration for pymin. Only works on game\nversions 12+. These values are stored in <venvpath>/Pymin/nimin_prefs.toml.\nArguments must be in the format "section.key=value".\nDisplays the entire config when no arguments are passed.\n\nUnlike with the cfg command, this one can not give you a description of each\nvalue because they are external and might change.\n\n{DOCS_PARSING_RULES}',
    'migrate-config': f'Usage: <venvscript> migrate-config\n\nMigrates older versions of this script\'s config. Overwrites the current config values.\n\nAutomatically runs if the current config is missing and any of the following\nfiles exist:\n\t<venvpath>/.USEUV\n\t<venvpath>/.USEUVI\n\t<venvpath>/.DEFAULTRUN\n\t<venvpath>/pymin.cfg\n\t./pymin.cfg\n\n{DOCS_NO_ARGS}',
    'run':            f'Usage: <venvscript> run\n\nRuns the game.\nThe game must be at <venvpath>/Pymin/Pymin.py.\n\n{DOCS_FORWARDS_ARGS}',
    'conv':           f'Usage: <venvscript> conv\n\nOpens the save file converter included in the game.\nThe game must be at <venvpath>/Pymin/Pymin.py.\n\n{DOCS_NO_ARGS}',
    'recreate':       f'Usage: <venvscript> recreate [args]\n\nDeletes everything and starts anew.\n\nSteps followed by this command:\n\tPlaceholder\n\n{DOCS_GENERAL_ARGS}\n\nSpecial arguments:\n\t--with-config\t\tPreserves the config for this script (if stored in the venv)\n\t--with-saves\t\tPreserves the <venvpath>/Pymin/nimin_saves directory.\n\t--with-game-config\tPreserves the game\'s config. (only works with Pymin version 12+)',
    'uv':             f'Usage: <venvscript> uv [args]\n\nRuns uv inside of the venv.\nRunning without arguments will run "uv --help".\n\n{DOCS_FORWARDS_ARGS}',
    'pip':            f'Usage: <venvscript> pip [args]\n\nRuns pip inside of the venv.\nRunning without arguments will run "pip --help".\n\n{DOCS_FORWARDS_ARGS}',
}


def getDocumentationPage(page: str = None):
    if page is None:
        return 'Usage: <venvscript> docs [command]\n\nThis command contains simple documentation for this script.\nValid [command]s: ' + ', '.join(DOCS_PAGES.keys())
    return DOCS_PAGES.get(page, f'Page "{page}" does not exist.')


# Arguement parsing logic
if config['defaultToRun'] and len(sys.argv) < 2:
    sys.argv.append('run')
if len(sys.argv) < 2 or sys.argv[1] in {'help', '-h', '--help'}:
    print('Usage: <venvscript> [command] [args]\nCommands:\n\thelp\t\t\tDisplays this message.\n\tdocs\t\t\tAdvanced help information. Put a command after this one to display its docs.\n\tinstall\t\t\tCreates and sets up the virtual environment for the game.\n\tupdate\t\t\tUpdates the game and all of it\'s dependencies.\n\tcfg\t\t\tDisplay and modify the config. Arguments should be in the form "key=value". If no arguments are given, displays config.\n\tcfg-game\t\tDisplay and modify the game\'s config. Same as cfg arguments are formatted as "section.key=value". Only for pymin 12+.\n\tmigrate-config\t\tExplicitly migrate old config versions. Done automatically this script is updated.\n\trun\t\t\tRuns the game. Forwards all arguments.\n\tconv\t\t\tRuns the savefile converter built into the game. Takes no arguments.\n\trecreate\t\tDeletes everything and starts again.\n\tuv\t\t\tExecutes uv inside of the environment. Forwards all arguments.\n\tpip\t\t\tExecutes pip inside of the environment. Forwards all arguments.\n\ncfg/cfg-game parsing rules:\n\tMake sure to escape any special characters recognised by your terminal (ex: curly brackets in bash).\n\tDo not use brackets [ ] or curly brackets { } in keys. They are not parsed correctly.\n\tTables use the python format {key:value,} even though they are used as TOML.\n\nArguements {install, update, recreate}:\n\t--unverified\t\tTemporarily disables ssl verification.\n\t--nohtmlparser\t\tSkips installing the custom html parser once.\n\t--version\t\tThe release tag for pymin to install. ex: "--version <tag>" [default: latest]\n\t--as3libversion\t\tThe release tag for as3lib to install. ex: "--as3libversion <tag>" [default: latest]\n\nOther Command Specific Arguements:\n\t{install}\t--overwrite\t\tBypasses the overwrite restriction. Use at your own risk.\n\t{recreate}\t--with-config\t\tPreserves the config for this script (if stored in the venv)\n\t{recreate}\t--with-saves\t\tPreserves the nimin_saves directory.\n\t{recreate}\t--with-game-config\tPreserves the game\'s config.')
elif sys.argv[1] == 'docs':
    print(getDocumentationPage(None if len(sys.argv) == 2 else sys.argv[2]))
elif sys.argv[1] == 'migrate-config':
    config.update(migrateConfig())
elif sys.argv[1] == 'cfg':
    args = sys.argv[2:]
    if not len(args):
        with StringIO() as text:
            for k, v in config.items():
                text.write(f'{k}: {v}\n')
            print(text.getvalue())
        exit()
    CONFIG_TYPES = {
        'cfgVersion': int,
        'path': str,
        'pyInstalledVersion': str,
        'uvGlobal': bool,
        'uvLocal': bool,
        'defaultToRun': bool,
        'noSSLVerify': bool,
        'noCustomHTMLParser': bool,
        'isDevEnv': bool
    }
    for key, raw_value in (i.split('=') for i in args):
        if key in {'cfgVersion', 'pyInstalledVersion'} and not config['isDevEnv']:
            print(f'Warning: {key} is restricted and should not be changed. Skipping.')
            continue
        if key not in config:
            print(f'Warning: Key {key} does not exist.')
            continue
        try:
            value = Args.Parse(raw_value, CONFIG_TYPES[key])
        except:
            print(f'Warning: Could not parse {key}. Skipping')
            continue
        config[key] = value
elif sys.argv[1] == 'cfg-game' and hasVenv:
    game_config_path = venv.getLocalPath('Pymin/Nimin_Prefs.toml')
    if not game_config_path.exists():
        raise Exception('Game config does not exist.')
    with open(game_config_path, 'rb') as f:
        gameconf = TOML.readFile(f)
    args = sys.argv[2:]
    if len(args):
        for variable, raw_value in (i.split('=') for i in args):
            section, key = variable.split('.')
            if section not in gameconf or key not in gameconf[section]:
                print(f'Warning: {section}.{key} does not exist.')
                continue
            try:
                value = Args.Parse(raw_value, type(gameconf[section][key]))
            except:
                print(f'Warning: Could not parse {section}.{key}. Skipping')
                continue
            gameconf[section][key] = value
        TOML.write(game_config_path, gameconf)
    else:
        with StringIO() as text:
            for k1, v1 in gameconf.items():
                text.write(f'[{k1}]\n')
                for k2, v2 in v1.items():
                    text.write(f'{k2}: {v2}\n')
                text.write('\n')
            print(text.getvalue())
    exit()
elif sys.argv[1] == 'install':
    if hasVenv and '--overwrite' not in sys.argv:
        raise Exception('"install" can not be used in an existing directory. Did you mean "update"?')
    create()
elif sys.argv[1] == 'update' and hasVenv:
    doPythonUpdate = False
    # TODO: Remove config['isDevEnv'] check once this is no longer experimental
    if config['isDevEnv'] and platform.python_version().split('.')[:2] != config['pyInstalledVersion'].split('.')[:2] and platform.system() != 'Windows':
        answer = input('(Experimental) Python major version has changed. Would you like to switch this virtual environment to the new one? (y/N)')
        doPythonUpdate = answer.lower() == 'y'
    if doPythonUpdate:
        updatePythonVersion()
    else:
        downloadgame()
        updatemodules()
elif sys.argv[1] == 'run' and hasVenv:
    venv.runWithPython(venv.getLocalPath('Pymin/Pymin.py'), *sys.argv[2:])
elif sys.argv[1] == 'conv' and hasVenv:
    venv.runWithPython(venv.getLocalPath('Pymin/Pymin.py'), '--converter')
elif sys.argv[1] == 'recreate' and hasVenv:
    recreate('--with-config' in sys.argv, '--with-saves' in sys.argv, '--with-game-config' in sys.argv)
elif sys.argv[1] == 'uv' and hasVenv:
    if not (config['uvGlobal'] or config['uvLocal']):
        raise Exception('uv is not enabled.')
    if len(sys.argv) == 2:
        venv.runWithEnv(*venv.pipCommand[:-1], 'help')
    else:
        venv.runWithEnv(*venv.pipCommand[:-1], *sys.argv[2:])
elif sys.argv[1] == 'pip' and hasVenv:
    if len(sys.argv) == 2:
        venv.pip('--help')
    else:
        venv.pip(*sys.argv[2:])
elif sys.argv[1] in {'cfg-game', 'update', 'run', 'conv', 'recreate', 'uv', 'pip'}:
    raise Exception(f'"{sys.argv[1]}" requires a valid virtual environment.')
else:
    raise Exception(f'Invalid command "{sys.argv[1]}"')

# Check if config was modified
if ORIGINAL_CONFIG != config or not cfgloc.exists():
    TOML.write(cfgloc, config)
