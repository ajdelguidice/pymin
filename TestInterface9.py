import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("1176x662")
mainframe = tkinter.Frame(root,background="#000000")
mainframe.place(anchor="nw", height=662, width=1176)
mainframe.configure()
#mainframe['padding'] = (20,30,0,0)
root.mainloop()