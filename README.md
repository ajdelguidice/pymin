<h2>(Unofficial) Python port of Nimin Fetish Fantasy</h2>
<h4><i>WARNING: PORN</i></h4>
| <a href="https://www.furaffinity.net/view/12638483/">Original game</a> | <a href="https://github.com/ajdelguidice/nimin-source">Game source code</a> |
<br><br><b>DISCLAIMER:</b> This project has nothing to do with the original authors. DO NOT contact them about issues with this port, they will have no idea what you are even talking about.
<br><br>As of version 1.0.7, requires Python>=3.10.
<br>Please read the first section of the <a href="https://github.com/ajdelguidice/python-as3lib/blob/main/README.md">readme for as3lib</a> as well before using.
<br><br>I made this port because I really like the game. I made it mostly for personal use so it only includes quality of life improvements and bug fixes. I will not be developing the game content any further and do not claim any part of the original game as my own. Just plop your original save files into the nimin_saves directory that the game creates on first launch and start playing like you would the original. I plan on making the interface look more like the original but more on that later.
<br><br>Virtual environments are the best way to run this program. I have made a script to set everything up, please use it. On Unix, if the minor verion (the X in 3.X.Y) that you are using changes, you must run the venvscript's update command as python installs packages in version specific locations and creates version specific binaries for c modules. The old virtual environment script I made was super janky and has now been removed from this repo. DO NOT USE IT IF YOU STILL HAVE IT, it was terrible and could break your system.
<br><br><b>Use the version of as3lib that is designated in the release notes of the version you are using.</b> The interface portion of as3lib is not backwards compatible between any version as it is still in alpha.
<br><br>This version of the game tries to keep things as close to the original game as possible, however there are a few changes, some toggleable, some not. The most notable being:
<br>&emsp;The game now has a built in menu bar.
<br>&emsp;The theming for the game (colours, interface style, etc) is slightly different as I used the default tkinter stuff. I have plans to make a ttk theme for the game but progress on that is slow as I have to completely redesign as3lib's interface components to accomodate ttk. The actual theme is mostly done however, it does look a little bit off because tcl/tk 8.6 (what tkinter uses as a backend) does not support svg images so I had to remake everything using png with flat colours. tcl/tk 9.0 add support for svg images but python does not use it yet.
<br>&emsp;The "Save to"/"Load file" buttons can now use files outside of the game's directory and can use any format that the game supports
<br>&emsp;The game now has a wiki intregrated into it. This can be accessed either through the help help menu at the top of the window or by pressing either the tilde key or the numpaddivide key. (The wiki is nowhere near finished yet)
<br>&emsp;The default save file location is now &lt;gamedirectory&gt;/nimin_saves. This can be changed by going to the options menu. (located in File->Options)
<br>&emsp;You can now set a custom font and theme color from within the game. (located in File->Options)
<br>&emsp;The game saves to xml files by default
<br>&emsp;The game now has a debug mode that can be toggled by passing the "--debug" parameter when launching the game.
<br>&emsp;Though not required, a save file converter has been included to convert between save formats. It can be access through the save/load dialog. A standalone save file converter is also included in this repo but it isn't up to date, doesn't work very well, and can't do nim files.
<br><br>&emsp;(not toggleable) The stash now works more like the bag. Holding shift and pressing button 12 while already moving an item allows you to move items between the bag and stash.
<br>&emsp;(not toggleable) Everything in the game now changes color with the background and foreground color settings. (I plan on making a toggle to disable this)
<br><br>&emsp;(toggleable | defualt: off) The save and load dialog has been reworked to be able to save to and load from any file inside of the save folder by default. You still have to click the "save to"/"load file" button to go anywhere else.
<br>&emsp;(toggleable | default: off) The game now has a toggle to force the use of sol files instead of xml files.
<br><br>If you get stuck somewhere or there are no buttons on screen, please let me know, that is a bug not a feature.
<br><br>&emsp;Note: Any of the built-in modules that are required must be installed outside of the virtual environment as they can not be installed by pip. This note is here because some linux distibutions put some of these module in separate packages.
<br><br>Requirements:
<br>&emsp;Built in: math, random, pathlib, xml.etree, tkinter, sys, functools, webbrowser, typing
<br>&emsp;External: <a href="https://pypi.org/project/six/">six</a>, <a href="https://pypi.org/project/setuptools/">setuptools</a> (required by both Mini-AMF and as3lib), <a href="https://pypi.org/project/Mini-AMF/">miniamf</a>, <a href="https://pypi.org/project/as3lib/">as3lib</a>
<br><br>Additional requirements if using the venv script: venv, subprocess, urllib, platform, shutil, <a href="https://pypi.org/project/requests/">requests</a>
<br><br>Unix requirements (this includes MacOS):
<br>&emsp;A bash compatible shell
<br>&emsp;A C compiler recognised by setuptools that implements C99
<br><br>Windows requirements:
<br>&emsp;PyLauncher
<br>&emsp;A C compiler recognised by setuptools (Visual c++ build tools is probably the easiest one to use. Only install the core, MSVC, and the Windows ## SDK. Everything else is unnecessary). Note: The microsoft provided compiler (which is probably what most people will use) does not support C99 or urandom, meaning I had to use major jank to get the crypto c module working.
<br><br>Note: pyminlib/html_parser.py is a modified version of the one from tkhtmlview. tkhtmlview has an MIT license so it should be fine for me to distribute it (license is included in the file itself). <b>DO NOT INSTALL THIS VERSION OUTSIDE OF THIS PROJECT</b>, it has very serious security implications if you are not careful.
