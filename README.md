<h2>(Unofficial) Python port of Nimin Fetish Fantasy</h2>
<h4><i>WARNING: PORN</i></h4>
| <a href="https://www.furaffinity.net/view/12638483/">Original game</a> | <a href="https://github.com/ajdelguidice/nimin-source">Decompiled source code</a> |
<br><br><b>DISCLAIMER:</b> This project has nothing to do with the original authors. DO NOT contact them about issues with this port, they will have no idea what you are even talking about.
<br><br>Version 1.0.7 - 1.0.11 require Python>=3.10.
<br>Version 1.0.12+ require Python>=3.11 or 3.10 with <a href="https://pypi.org/project/tomli/">tomli</a>
<br>Please read the first section of the <a href="https://github.com/ajdelguidice/python-as3lib/blob/main/README.md">readme for as3lib</a> as well before using.
<br><br>I made this port because I really like the game. I made it mostly for personal use so it only includes quality of life improvements and bug fixes. I will not be developing the game content any further and do not claim any part of the original game as my own. I plan on making the interface look more like the original but more on that later.
<br><br>All save files made by the original game are compatible with this port, they just need to be moved into the nimin_saves directory that is created on first launch. Most of the save files made by this port are compatible with the original game if saved in the correct format (.sol or .nim) with two major caviats: <b>1)</b> this port adds some extra data that will be lost if resaved with the original game and <b>2)</b> some settings will make the save files completely incompatible (these are marked in their tooltips).
<br><br>Virtual environments are the best way to run this program. I have made a script to set everything up, please use it. It has <a href="https://github.com/astral-sh/uv">uv</a> support built in, but enabling it requires you to pass an arguement (either --uv-global or --uv-local). On Unix, if python's minor verion (the X in 3.X.Y) changes, you must run the venvscript's update command as python installs packages in version specific locations and creates version specific binaries for c modules. I am working on a way to automatically detect this and fix it if the user desires.
<br><br><b>Use the version of as3lib that is designated in the release notes of the version you are using.</b> The interface portion of as3lib does not retain compatibility between any version because it is just a test interface.
<br><br>If you get stuck somewhere or there are no buttons on screen, please let me know, that is a bug not a feature.
<br><br>Note: pyminlib/html_parser.py is a modified version of tkhtmlview's html_parser.py (original license included in the file) which allows for the in game wiki's page links to work. This is an optional dependency and SHOULD NOT be installed outside of this games virtual environment. It has the potential for arbitrary code execution from html strings if abused and could lead to incompatibility with other things because it does not do its thing in a standard way.
<h3>Requirements</h3>
<b>Game:</b> math, random, pathlib, xml.etree, tkinter, sys, functools, webbrowser, platform, io, <a href="https://pypi.org/project/six/">six</a>, <a href="https://pypi.org/project/setuptools/">setuptools</a>, <a href="https://pypi.org/project/Mini-AMF/">miniamf</a>, <a href="https://pypi.org/project/as3lib/">as3lib</a>, <a href="https://pypi.org/project/tomli-w/">tomli-w</a>
<br><b>Venv script:</b> venv, subprocess, urllib, shutil, configparser, <a href="https://pypi.org/project/requests/">requests</a>
<br><br><b>Note:</b> Any of the built-in modules (the ones that aren't hyperlinks) can not be installed by pip so they must be installed globally. This note is here because some linux distributions package some of python's built in modules as separate packages.
<br><br><b>Unix (including MacOS) requirements:</b>
<br>&emsp;A bash compatible shell
<br>&emsp;A C compiler recognised by setuptools (ex: gcc, clang)
<br>&emsp;urandom
<br><br><b>Windows requirements:</b>
<br>&emsp;PyLauncher
<br>&emsp;A C compiler recognised by setuptools (Visual c++ build tools is the easiest to install. Only install the core, MSVC, and the Windows ## SDK, everything else is unnecessary).
<h3>Notable Changes</h3>
This version of the game tries to keep things as close to the original game as possible, however there are a few changes, some toggleable, some not. The most notable being:
<br><br>&emsp;The game now has a built in menu bar.
<br><br>&emsp;The theming for the game (colours, interface style, etc) is slightly different as I used the default tkinter stuff. I have plans to make a ttk theme for the game but progress on that is slow as I have to completely redesign as3lib's interface components to accomodate ttk. The actual theme is mostly done however, it does look a little bit off because tcl/tk 8.6 (the toolkit used) does not support svg images so I had to remake everything using png with flat colours. tcl/tk 9.0 adds support for svg images but python does not use it yet.
<br><br>&emsp;The "Save to"/"Load file" buttons can now use files outside of the game's directory and can use any format that the game supports.
<br><br>&emsp;The game now has a wiki intregrated into it. This can be accessed either through the help menu at the top of the window or by pressing either the tilde key or the numpaddivide key. (The wiki is nowhere near finished yet)
<br><br>&emsp;The game uses &lt;gamedirectory&gt;/nimin_saves for all saves by default.
<br><br>&emsp;You can now set custom font and theme color from within the game. (located in File->Options)
<br><br>&emsp;The game saves to xml files by default but can use any of the supported formats in any dialog (unlike the original game which only allowed .sol files in the "slots" and .nim files everywhere else).
<br><br>&emsp;The game now has a debug mode that can be toggled by passing the "--debug" arguement when launching the game (opening the debug window will slow down the game considerably because it runs on the same thread as the game).
<br><br>&emsp;Though not required, a save file converter has been included to convert between save formats. It can be access through the save/load dialog or by passing the "--converter" arguement to the game. A standalone save file converter is also included in this repo but not installed by default and isn't always up to date.
<br><br>&emsp;(toggleable | default: on) Everything in the game now changes color with the background and foreground color settings.
<br><br>&emsp;(toggleable | default: off) The game now has a toggle to force the use of save file compatible with the original game.
<br><br>&emsp;You can now customise the look of the game by going to the "Interface" tab of the options window.
<br><br>&emsp;The game has a section in the options called "Game Tweaks". This is where most things that significantly alter the game can be toggled.
<br><br>&emsp;(toggleable | defualt: off) There is a new save/load dialog which is able to save to and load from any file inside of the save folder. You still have to click the "save to"/"load file" button to go anywhere else. (Interface toggle)
<br><br>&emsp;(toggleable | default: off) The stash can now work like the bag. Press button 12 while moving an item to go between the bag and stash. (Interface toggle)
