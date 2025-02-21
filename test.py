"""
from os.path import isfile, join
import os
def listFilesInDir(dir_, ext:list=None):
   files = [f for f in os.listdir(dir_) if isfile(join(dir_,f))]
   print("files:",files)
   if ext != None:
      tempext = ext
      ext = []
      for i in tempext:
         if i[:1] == ".":
            ext.append(i[1:])
         else:
            ext.append(i)
      print(ext)
      tempf = []
      for i in files:
         temp = i.split(".")
         print("split:",temp, "len:",len(temp),"-1:",temp[-1])
         if len(temp) == 1 and "" in ext:
            tempf.append(i)
         if temp[-1] in ext:
            tempf.append(i)
         print(tempf)
      return tempf
   return files

print(listFilesInDir("/run/media/ajdel/STUFFDRIVE/pimin/package",[".md",".in"]))
"""
"""
import tkinter
import tkinter.ttk as ttk
root = tkinter.Tk()
root.geometry("500x500")

nb = ttk.Notebook(root)
nb.pack(pady=1,expand=True)

f1 = tkinter.Frame(nb,width=500,height=480)
f2 = tkinter.Frame(nb,width=500,height=480)
f1.pack(fill="both",expand=True)
f2.pack(fill="both",expand=True)

nb.add(f1,text="Test1")
nb.add(f2,text="Test2")

root.mainloop()
"""
"""
def t1(a,b):
   if not a and not b:
      return 1
def t2(a,b):
   if not (a or b):
      return 1
from timeit import timeit
from functools import partial
print(timeit(partial(t1,False,False),number=1000000))
print(timeit(partial(t2,False,False),number=1000000))
"""
def strtobool(a:str):
   """
   Converts a string to a boolean
   """
   match a.lower():
      case "true":
         return True
      case "false":
         return False

def t1(a):
   """
   Converts the string representation of a list to a list of booleans
   """
   b = a[1:-1].split(", ")
   c = []
   for i in b:
      c.append(strtobool(i))
   return c
def t2(a):
   """
   Converts the string representation of a list to a list of booleans
   """
   return [strtobool(i) for i in a[1:-1].split(", ")]

from timeit import timeit
from functools import partial
print(t1("[true, true, false, false]"))
print(t2("[true, true, false, false]"))
print(timeit(partial(t1,"[true, true, false, false]"),number=1000))
print(timeit(partial(t2,"[true, true, false, false]"),number=1000))