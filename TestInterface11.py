import tkinter
import math

oldmult = 100
class resize:
   def calculate():
      global root, sizedict, oldmult
      newwidth = root.winfo_width()
      newheight = root.winfo_height()
      xmult = (100*newwidth)/1176
      ymult = (100*newheight)/662
      if xmult > ymult:
         mult = ymult
      elif xmult < ymult:
         mult = xmult
      elif xmult == ymult:
         mult = xmult
      if mult < 22.2789:
         mult = 22.2789
      if oldmult == mult:
         return oldmult
      else:
         oldmult = mult
         #print(mult)
         return mult
   def set_size(mult):
      global displaytestframe, root
      newwidth = root.winfo_width()
      newheight = root.winfo_height()
      displaytestframe.place(anchor="center", width=1176*mult/100, height=662*mult/100, x=newwidth/2, y=newheight/2)
   def doResize(useless):
      mult = resize.calculate()
      resize.set_size(mult)

root = tkinter.Tk()
root.title("Pymin")
root.geometry("1176x662")
root.minsize(262,147)

frame = tkinter.Frame(root, background="#FFFFFF")
frame.pack(fill="both", expand=True)

displaytestframe = tkinter.Frame(frame, background="#000000")
displaytestframe.place(anchor="center", width=1176, height=662, x=588, y=331)

root.bind("<Configure>",resize.doResize)

root.mainloop()