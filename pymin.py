#Pymin.py

import importlib
import pathlib
import tkinter
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
import pygubu
from dataclasses import dataclass
from PIL import Image
import pyminlib

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "ui/rev1.ui"
IMAGE_37 = PROJECT_PATH / "1.png"
IMAGE_40 = PROJECT_PATH / "2.png"


class PyminApp:
    def __init__(self, master=None):
        # 1: Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        #builder.add_from_string(?UI?)
        builder.add_resource_path(IMAGE_37)
        builder.add_resource_path(IMAGE_40)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('frame1', master)

        # 4: Connect callbacks
        builder.connect_callbacks(self)

    def run(self):
        pyminlib.GameStartup()
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = PyminApp()
    app.run()

DebugVars = list((False))
#SkipExhaustion(true/false)

"""
def LoadGame(x):
	global GameVars[5] = 1
	#LoadFile('Nimin_Save' + x + '.sol')

def LoadFile(x):
	#Readfile(x) into PlayerVars

def SaveGame(x):
    global GameVars[5] = 2
    #SaveFile

def SaveFile
	if x <= 9:
		#WriteFile(Playervars, 'Nimin_Save' + x + '.nim')
	else:
		#WriteFile(PlayerVars, SpecifiedFile)
"""