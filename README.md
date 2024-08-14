<h2>(Unofficial) Python port of Nimin Fetish Fantasy</h2>
<h4><i>WARNING: PORN</i></h4>
| <a href="https://www.furaffinity.net/view/12638483/">Original game</a> | <a href="https://github.com/ajdelguidice/nimin-source">Game source code</a> |
<br><br>As of version 1.0.7, requires Python>=3.10.
<br>Please read the first section of the <a href="https://github.com/ajdelguidice/python-as3lib/blob/main/README.md">readme for as3lib</a> as well before using.
<br><br>This port is a personal project of mine that I made because I really like the game. I made it for preservation as well as to fix some annoying bugs and add quality of life improvements (no one wants to have a bad time while having a wank), I will not be developing the game content any further and do not claim any part of the original game as my own. All save files from the original game (at least from v0.975o) can be loaded into the game, however, a save file convert has been included in the save/load file menu if you choose to convert them to the newer format (.nim files are not currently convertable as they are a bit complicated).
<br><br>Virtual environments are the best way to run this program. I have made a script to set everything up, please use it. If the minor verion (the X in 3.X.Y) that you are using changes, you must re-run the venvscript's setup command as python installs packages in version specific locations and creates version specific binaries for c modules. The old virtual environment script I made was super janky and has now been removed from this repo. DO NOT USE IT, the new one is much better and (probably) doesn't break your system.
<br><br><b>Use the version of as3lib that is designated in the release notes of the version you are using.</b> The interface portion of as3lib is not backwards compatible between any version as it is still in alpha.
<br><br>If you get stuck somewhere or there are no buttons on screen, please let me know, that is a bug not a feature.
<br><br>Requirements if using venv:
<br>&emsp;Note: Any of the built-in packages that are required must be installed outside of the virtual environment as they can not be installed by pip. This note is here because some linux distibutions put some of these module in separate packages.
<br>&emsp;venv, os, pathlib, sys, subprocess, urllib, platform (Built-in)
<br>&emsp;<a href="https://pypi.org/project/requests/">requests</a>
<br><br>Requirements:
<br>&emsp;Built in:
<br>&emsp;&emsp;math
<br>&emsp;&emsp;random
<br>&emsp;&emsp;os
<br>&emsp;&emsp;pathlib
<br>&emsp;&emsp;xml.etree
<br>&emsp;&emsp;tkinter
<br>&emsp;&emsp;sys
<br>&emsp;&emsp;functools
<br>&emsp;&emsp;webbrowser
<br>&emsp;&emsp;typing
<br>&emsp;External:
<br>&emsp;&emsp;six
<br>&emsp;&emsp;setuptools(required by both Mini-AMF and as3lib)
<br>&emsp;&emsp;<a href="https://pypi.org/project/Mini-AMF/">miniamf</a>
<br>&emsp;&emsp;<a href="https://pypi.org/project/as3lib/">as3lib</a>
<br><br>Windows specific requirements:
<br>&emsp;PyLauncher (Windows)
<br>&emsp;Visual c++ build tools (installing the visual studios c++ collection is the easiest way to get this. It does come with some garbage so you might want to go over what is included and remove anything that you don't want, like copilot)
