import tkinter
import tkinter.font
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import simple_colors as sc
import tk_html_widgets as tkhtml
import re

fontBold = False
fontSize = 12
fontMain = ("Times New Roman", 12)
theme = 0
fontColor = "#000000"
showSide = True
versionNumber = "0.0001"

class StatPane:
    def __init__():
        global _str_, ment, lib, sen, SexP, coin, day, hour, HP, lust
        global strvallabel, mentvallabel, libvallabel, senvallabel, sexpvallabel, coinvallabel, dayvallabel, hourvallabel, hpvallabel, lustvallabel
    def SetCStats():
        strvallabel["text"] = _str_
        mentvallabel["text"] = ment
        libvallabel["text"] = lib
        senvallabel["text"] = sen
    def SetSCStats():
        sexpvallabel["text"] = SexP
        coinvallabel["text"] = coin
    def SetDHStats():
        dayvallabel["text"] = day
        hourvallabel["text"] = hour + ":00"
    def SetHPStat():
        hpvallabel["text"] = HP
    def SetLustStat():
        lustvallabel["text"] = lust
class SGButton:
    def __init__():
        global savegamebutton
    def Show():
        savegamebutton = tkinter.Button(statframe, text="Save Game")
        savegamebutton.place(anchor=N, height=30, width=100, x=90, y=480)
    def Hide():
        savegamebutton.destroy()
class LGButton:
    def __init__():
        global loadgamebutton
    def Show():
        loadgamebutton = tkinter.Button(statframe, text="Load Game")
        loadgamebutton.place(anchor=N, height=30, width=100, x=90, y=515)
    def Hide():
        loadgamebutton.destroy()
class NGButton:
    def __init__():
        global newgamebutton
    def Show():
        newgamebutton = tkinter.Button(statframe, text="New Game")
        newgamebutton.place(anchor=N, height=30, width=100, x=90, y=550)
    def Hide():
        newgamebutton.destroy()
class PanelButton1:
    def __init__():
        global button1, button1visible
    def Show():
        if button1visible == False:
            button1 = tkinter.Button(buttonpanel, text="Button 1")
            button1.place(anchor=NW, height=46, width=140, x=0, y=0)
            button1visible = True
    def Hide():
        if button1visible == True:
            button1.destroy()
            button1visible = False
class PanelButton2:
    def __init__():
        global button2, button2visible
    def Show():
        if button2visible == False:
            button2 = tkinter.Button(buttonpanel, text="Button 2")
            button2.place(anchor=NW, height=46, width=140, x=160, y=0)
            button2visible = True
    def Hide():
        if button2visible == True:
            button2.destroy()
            button2visible = False 
class PanelButton3:
    def __init__():
        global button3, button3visible
    def Show():
        if button3visible == False:
            button3 = tkinter.Button(buttonpanel, text="Button 3")
            button3.place(anchor=NW, height=46, width=140, x=320, y=0)
            button3visible = True
    def Hide():
        if button3visible == True:
            button3.destroy()
            button3visible = False
class PanelButton4:
    def __init__():
        global button4, button4visible
    def Show():
        if button4visible == False:
            button4 = tkinter.Button(buttonpanel, text="Button 4")
            button4.place(anchor=NW, height=46, width=140, x=480, y=0)
            button4visible = True
    def Hide():
        if button4visible == True:
            button4.destroy()
            button4visible = False
class PanelButton5:
    def __init__():
        global button5, button5visible
    def Show():
        if button5visible == False:
            button5 = tkinter.Button(buttonpanel, text="Button 5")
            button5.place(anchor=NW, height=46, width=140, x=0, y=66)
            button5visible = True
    def Hide():
        if button5visible ==True:
            button5.destroy()
            button5visible = False
class PanelButton6:
    def __init__():
        global button6, button6visible
    def Show():
        if button6visible == False:
            button6 = tkinter.Button(buttonpanel, text="Button 6")
            button6.place(anchor=NW, height=46, width=140, x=160, y=66)
            button6visible = True
    def Hide():
        if button6visible ==True:
            button6.destroy()
            button6visible = False
class PanelButton7:
    def __init__():
        global button7, button7visible
    def Show():
        if button7visible == False:
            button7 = tkinter.Button(buttonpanel, text="Button 7")
            button7.place(anchor=NW, height=46, width=140, x=320, y=66)
            button7visible = True
    def Hide():
        if button7visible == True:
            button7.destroy()
            button7visible = False
class PanelButton8:
    def __init__():
        global button8, button8visible
    def Show():
        if button8visible == False:
            button8 = tkinter.Button(buttonpanel, text="Button 8")
            button8.place(anchor=NW, height=46, width=140, x=480, y=66)
            button8visible = True
    def Hide():
        if button8visible == True:
            button8.destroy()
            button8visible = False
class PanelButton9:
    def __init__():
        global button9, button9visible
    def Show():
        if button9visible == False:
            button9 = tkinter.Button(buttonpanel, text="Button 9")
            button9.place(anchor=NW, height=46, width=140, x=0, y=132)
            button9visible = True
    def Hide():
        if button9visible == True:
            button9.destroy()
            button9visible = False
class PanelButton10:
    def __init__():
        global button10, button10visible
    def Show():
        if button10visible == False:
            button10 = tkinter.Button(buttonpanel, text="Button 10")
            button10.place(anchor=NW, height=46, width=140, x=160, y=132)
            button10visible = True
    def Hide():
        if button10visible == True:
            button10.destroy()
            button10visible = False
class PanelButton11:
    def __init__():
        global button11, button11visible
    def Show():
        if button11visible == False:
            button11 = tkinter.Button(buttonpanel, text="Button 11")
            button11.place(anchor=NW, height=46, width=140, x=320, y=132)
            button11visible = True
    def Hide():
        if button11visible == True:
            button11.destroy()
            button11visible = False
class PanelButton12:
    def __init__():
        global button12, button12visible
    def Show():
        if button12visible == False:
            button12 = tkinter.Button(buttonpanel, text="Button 12")
            button12.place(anchor=NW, height=46, width=140, x=480, y=132)
            button12visible = True
    def Hide():
        if button12visible == True:
            button12.destroy()
            button12visible = False

class ButtonFunctions:
    def __init__():
        global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12
    def Visible(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
        if a1 == 0:
            try:
                PanelButton1.Hide()
            except:
                x = 0
        elif a1 == 1:
            try:
                PanelButton1.Hide()
            finally:
                PanelButton1.Show()
        if a2 == 0:
            try:
                PanelButton2.Hide()
            except:
                x = 0
        elif a2 == 1:
            try:
                PanelButton2.Hide()
            finally:
                PanelButton2.Show()
        if a3 == 0:
            try:
                PanelButton3.Hide()
            except:
                x = 0
        elif a3 == 1:
            try:
                PanelButton3.Hide()
            finally:
                PanelButton3.Show()
        if a4 == 0:
            try:
                PanelButton4.Hide()
            except:
                x = 0
        elif a4 == 1:
            try:
                PanelButton4.Hide()
            finally:
                PanelButton4.Show()
        if a5 == 0:
            try:
                PanelButton5.Hide()
            except:
                x = 0
        elif a5 == 1:
            try:
                PanelButton5.Hide()
            finally:
                PanelButton5.Show()
        if a6 == 0:
            try:
                PanelButton6.Hide()
            except:
                x = 0
        elif a6 == 1:
            try:
                PanelButton6.Hide()
            finally:
                PanelButton6.Show()
        if a7 == 0:
            try:
                PanelButton7.Hide()
            except:
                x = 0
        elif a7 == 1:
            try:
                PanelButton7.Hide()
            finally:
                PanelButton7.Show()
        if a8 == 0:
            try:
                PanelButton8.Hide()
            except:
                x = 0
        elif a8 == 1:
            try:
                PanelButton8.Hide()
            finally:
                PanelButton8.Show()
        if a9 == 0:
            try:
                PanelButton9.Hide()
            except:
                x = 0
        elif a9 == 1:
            try:
                PanelButton9.Hide()
            finally:
                PanelButton9.Show()
        if a10 == 0:
            try:
                PanelButton10.Hide()
            except:
                x = 0
        elif a10 == 1:
            try:
                PanelButton10.Hide()
            finally:
                PanelButton10.Show()
        if a11 == 0:
            try:
                PanelButton11.Hide()
            except:
                x = 0
        elif a11 == 1:
            try:
                PanelButton11.Hide()
            finally:
                PanelButton11.Show()
        if a12 == 0:
            try:
                PanelButton12.Hide()
            except:
                x = 0
        elif a12 == 1:
            try:
                PanelButton12.Hide()
            finally:
                PanelButton12.Show()

    #def WriteText():
    #def WriteCommand():
class SidePanel:
    def __init__():
        global looksbutton, statsbutton, effectsbutton, helpbutton, levelsbutton, gearbutton, titlesbutton, creditsbutton, textside, appearancebutton
    def Show():
        looksbutton = tkinter.Button(sidebar, text="Look")
        looksbutton.place(anchor=NW, width=80, x=0, y=0)
        statsbutton = tkinter.Button(sidebar, text="Stats")
        statsbutton.place(anchor=NW, width=80, x=83, y=0)
        effectsbutton = tkinter.Button(sidebar, text="Effects")
        effectsbutton.place(anchor=NW, width=80, x=166, y=0)
        helpbutton = tkinter.Button(sidebar, text="Help")
        helpbutton.place(anchor=NW, width=80, x=249, y=0)
        levelsbutton = tkinter.Button(sidebar, text="Levels")
        levelsbutton.place(anchor=NW, width=80, x=0, y=30)
        gearbutton = tkinter.Button(sidebar, text="Gear")
        gearbutton.place(anchor=NW, width=80, x=83, y=30)
        titlesbutton = tkinter.Button(sidebar, text="Titles")
        titlesbutton.place(anchor=NW, width=80, x=166, y=30)
        creditsbutton = tkinter.Button(sidebar, text="Credits")
        creditsbutton.place(anchor=NW, width=80, x=249, y=30)
        textside = tkScrolledText(sidebar, cursor="arrow", wrap="word")
        textside.place(anchor=NW, height=300, width=330, x=0, y=80)
        textside.configure(state="disabled")

        appearancebutton.destroy()
    def Hide():
        looksbutton.destroy()
        statsbutton.destroy()
        effectsbutton.destroy()
        helpbutton.destroy()
        levelsbutton.destroy()
        gearbutton.destroy()
        titlesbutton.destroy()
        creditsbutton.destroy()
        textside.destroy()

        appearancebutton = tkinter.Button(sidebar, text="Appearance")
        appearancebutton.place(anchor=CENTER, height=50, width=150, x=167, y=216)

class TextBoxes:
   def __init__():
      global textmain, textside
   def ClearMain():
      textmain.configure(state="normal")
      textmain.delete(1.0,"end")
      textmain.configure(state="disabled")
   def ClearAddMain(text):
      textmain.configure(state="normal")
      textmain.delete(1.0,"end")
      textmain.insert(1.0, text)
      textmain.configure(state="disabled")
   def AddMain(text):
      textmain.configure(state="normal")
      textmain.insert("end", text)
      textmain.configure(state="disabled")
   def GetMain(a, b):
      global textmain
      text = textmain.get(a, b)
      return text
   def DisplayMainHTML():
      global textmain
      text = str(TextBoxes.GetMain("1.0", "end"))
      text = re.sub("(\t)", "    ", text)
      #text = "<pre>" + text + "</pre>"
      textmain.set_html(text, False)
   def ClearSide():
      textside.configure(state="normal")
      textside.delete(1.0,"end")
      textside.configure(state="disabled")
   def ClearAddSide(text):
      textside.configure(state="normal")
      textside.delete(1.0,"end")
      textside.insert(1.0, text)
      textside.configure(state="disabled")
   def AddSide(text):
      textside.configure(state="normal")
      textside.insert("end", text)
      textside.configure(state="disabled")

class UpDown:
    def __init__():
        global strimglabel, mentimglabel, libimglabel, senimglabel, hpimglabel, lustimglabel
    def HideAll():
        strimglabel["image"] = ""
        mentimglabel["image"] = ""
        libimglabel["image"] = ""
        senimglabel["image"] = ""
        hpimglabel["image"] = ""
        lustimglabel["image"] = ""
    def StrImg(img):
        strimglabel["image"] = img
    def MentImg(img):
        mentimglabel["image"] = img
    def LibImg(img):
        libimglabel["image"] = img
    def SenImg(img):
        senimglabel["image"] = img
    def hpImg(img):
        hpimglabel["image"] = img
    def LustImg(img):
        lustimglabel["image"] = img

def ToggleTheme():
   global theme
   theme += 1
   if theme >= 6:
      theme = 0
   UpdateTheme()
   #SavePreferences()

def ChangeBackgroundColor(color):
   global bccolorlabel1, bccolorlabel2, bccolorlabel3, bccolorlabel4, bccolorlabel5, textmain, textside, label1, strlabel, strcolonlabel, strvallabel, strimglabel, mentlabel, mentcolonlabel, mentvallabel, mentimglabel, liblabel, libcolonlabel, libvallabel, libimglabel, senlabel, sencolonlabel, senvallabel, senimglabel, label6, hplabel, hpcolonlabel, hpvallabel, hpimglabel, lustlabel, lustcolonlabel, lustvallabel, lustimglabel, hungerlabel, hungercolonlabel, hungervallabel, label10, currentregionlabel, levellabel, levelcolonlabel, levelvallabel, sexplabel, sexpcolonlabel, sexpvallabel, coinlabel, coincolonlabel, coinvallabel, daylabel, daycolonlabel, dayvallabel, hourlabel, hourcolonlabel, hourvallabel, bagstashlabel, savegamebutton, loadgamebutton, newgamebutton, quitbutton, resetbutton, refreshbutton, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, looksbutton, statsbutton, effectsbutton, helpbutton, levelsbutton, gearbutton, titlesbutton, creditsbutton, appearancebutton, textside, themebutton, textsizedownbutton, textsizeresetbutton, textsizeupbutton, textboldbutton, textcolorbutton, themebutton7, amountlabel1, amountlabel2, amountlabel3, amountlabel4, amountlabel5, amountlabel6, amountlabel7, amountlabel8, amountlabel9, amountlabel10, amountlabel11, amountlabel12, pagelabel
   for i in ["bccolorlabel1", "bccolorlabel2", "bccolorlabel3", "bccolorlabel4", "bccolorlabel5", "textmain", "textside", "label1", "strlabel", "strcolonlabel", "strvallabel", "strimglabel", "mentlabel", "mentcolonlabel", "mentvallabel", "mentimglabel", "liblabel", "libcolonlabel", "libvallabel", "libimglabel", "senlabel", "sencolonlabel", "senvallabel", "senimglabel", "label6", "hplabel", "hpcolonlabel", "hpvallabel", "hpimglabel", "lustlabel", "lustcolonlabel", "lustvallabel", "lustimglabel", "hungerlabel", "hungercolonlabel", "hungervallabel", "label10", "currentregionlabel", "levellabel", "levelcolonlabel", "levelvallabel", "sexplabel", "sexpcolonlabel", "sexpvallabel", "coinlabel", "coincolonlabel", "coinvallabel", "daylabel", "daycolonlabel", "dayvallabel", "hourlabel", "hourcolonlabel", "hourvallabel", "bagstashlabel", "savegamebutton", "loadgamebutton", "newgamebutton", "quitbutton", "resetbutton", "refreshbutton", "button1", "button2", "button3", "button4", "button5", "button6", "button7", "button8", "button9", "button10", "button11", "button12", "looksbutton", "statsbutton", "effectsbutton", "helpbutton", "levelsbutton", "gearbutton", "titlesbutton", "creditsbutton", "appearancebutton", "textside", "themebutton", "textsizedownbutton", "textsizeresetbutton", "textsizeupbutton", "textboldbutton", "textcolorbutton", "themebutton7", "amountlabel1", "amountlabel2", "amountlabel3", "amountlabel4", "amountlabel5", "amountlabel6", "amountlabel7", "amountlabel8", "amountlabel9", "amountlabel10", "amountlabel11", "amountlabel12", "pagelabel"]:
      try:
         if (eval(i).cget("background") != color):
            eval(i)["background"] = color
      except:
         x = 0

def ChangeTextColor(color):
   global bccolorlabel1, bccolorlabel2, bccolorlabel3, bccolorlabel4, bccolorlabel5, textmain, textside, label1, strlabel, strcolonlabel, strvallabel, strimglabel, mentlabel, mentcolonlabel, mentvallabel, mentimglabel, liblabel, libcolonlabel, libvallabel, libimglabel, senlabel, sencolonlabel, senvallabel, senimglabel, label6, hplabel, hpcolonlabel, hpvallabel, hpimglabel, lustlabel, lustcolonlabel, lustvallabel, lustimglabel, hungerlabel, hungercolonlabel, hungervallabel, label10, currentregionlabel, levellabel, levelcolonlabel, levelvallabel, sexplabel, sexpcolonlabel, sexpvallabel, coinlabel, coincolonlabel, coinvallabel, daylabel, daycolonlabel, dayvallabel, hourlabel, hourcolonlabel, hourvallabel, bagstashlabel, savegamebutton, loadgamebutton, newgamebutton, quitbutton, resetbutton, refreshbutton, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, looksbutton, statsbutton, effectsbutton, helpbutton, levelsbutton, gearbutton, titlesbutton, creditsbutton, appearancebutton, textside, themebutton, textsizedownbutton, textsizeresetbutton, textsizeupbutton, textboldbutton, textcolorbutton, themebutton7, amountlabel1, amountlabel2, amountlabel3, amountlabel4, amountlabel5, amountlabel6, amountlabel7, amountlabel8, amountlabel9, amountlabel10, amountlabel11, amountlabel12, pagelabel
   for i in ["bccolorlabel1", "bccolorlabel2", "bccolorlabel3", "bccolorlabel4", "bccolorlabel5", "textmain", "textside", "label1", "strlabel", "strcolonlabel", "strvallabel", "strimglabel", "mentlabel", "mentcolonlabel", "mentvallabel", "mentimglabel", "liblabel", "libcolonlabel", "libvallabel", "libimglabel", "senlabel", "sencolonlabel", "senvallabel", "senimglabel", "label6", "hplabel", "hpcolonlabel", "hpvallabel", "hpimglabel", "lustlabel", "lustcolonlabel", "lustvallabel", "lustimglabel", "hungerlabel", "hungercolonlabel", "hungervallabel", "label10", "currentregionlabel", "levellabel", "levelcolonlabel", "levelvallabel", "sexplabel", "sexpcolonlabel", "sexpvallabel", "coinlabel", "coincolonlabel", "coinvallabel", "daylabel", "daycolonlabel", "dayvallabel", "hourlabel", "hourcolonlabel", "hourvallabel", "bagstashlabel", "savegamebutton", "loadgamebutton", "newgamebutton", "quitbutton", "resetbutton", "refreshbutton", "button1", "button2", "button3", "button4", "button5", "button6", "button7", "button8", "button9", "button10", "button11", "button12", "looksbutton", "statsbutton", "effectsbutton", "helpbutton", "levelsbutton", "gearbutton", "titlesbutton", "creditsbutton", "appearancebutton", "textside", "themebutton", "textsizedownbutton", "textsizeresetbutton", "textsizeupbutton", "textboldbutton", "textcolorbutton", "themebutton7", "amountlabel1", "amountlabel2", "amountlabel3", "amountlabel4", "amountlabel5", "amountlabel6", "amountlabel7", "amountlabel8", "amountlabel9", "amountlabel10", "amountlabel11", "amountlabel12", "pagelabel"]:
      try:
         if (eval(i).cget("foreground") != color):
            eval(i)["foreground"] = color
      except:
         x = 0

def UpdateTheme():
   global theme
   if theme == 0:
      ChangeBackgroundColor("#FFFFFF")
   elif theme == 1:
      ChangeBackgroundColor("#000000")
   elif theme == 2:
      ChangeBackgroundColor("#EF7DB6")
   elif theme == 3:
      ChangeBackgroundColor("#29705C")
   elif theme == 4:
      ChangeBackgroundColor("#4248A6")
   elif theme == 5:
      ChangeBackgroundColor("#721717")
   else:
      ChangeBackgroundColor("#FFFFFF")
      theme = 0

def FontSizeDown():
   global fontSize
   if fontSize > 4:
      fontSize -= 2
   UpdateText()
   #SavePreferences()

def FontSizeReset():
   fontSize = 14
   UpdateText()
   #SavePreferences()

def FontSizeUp():
   global fontSize
   if fontSize < 26:
      fontSize += 2
   UpdateText()
   #SavePreferences()

def ToggleBold():
   global fontBold
   if fontBold == False:
      fontBold = True
   else:
      fontBold = False
   UpdateText()
   #SavePreferences()

def ToggleColor():
   global fontColor
   if fontColor == "#000000":
      fontColor = "#FFFFFF"
   elif fontColor == "#FFFFFF":
      fontColor = "#808080"
   elif fontColor == "#808080":
      fontColor = "#0000FF"
   elif fontColor == "#0000FF":
      fontColor = "#800080"
   elif fontColor == "#800080":
      fontColor = "#FF0000"
   elif fontColor == "#FF0000":
      fontColor = "#FFA500"
   elif fontColor == "#FFA500":
      fontColor = "#FFFF00"
   elif fontColor == "#FFFF00":
      fontColor = "#008000"
   elif fontColor == "#008000":
      fontColor = "#EF7DB6"
   elif fontColor == "#EF7DB6":
      fontColor = "#29705C"
   elif fontColor == "#29705C":
      fontColor = "#000000"
   else:
      fontColor = "#FFFFFF"     
   ChangeTextColor(fontColor)
   #SavePreferences()

def ToggleSide():
   global showSide, themebutton7, Option7Visible
   if showSide == True:
      showSide = False
      SidePanel.Hide()
      themebutton7["text"] = "--"
   elif showside == False:
      showSide = True
      SidePanel.Show()
      UpdateSide()
      themebutton7["text"] = "O"
   else:
      showSide = True
      SidePanel.Hide()
      SidePanel.Show()
      UpdateSide()
      themebutton7["text"] = "O"
   if Option7Visible == True:
      #SavePreferences()
      x = 0

def UTCheckBold():
   global fontBold
   if fontBold == True:
      a = "bold"
      return a
   else:
      return "normal"

def UpdateText():
   global fontMain, textMain, textSide, normal_font, bold_font, italic_font
   a = UTCheckBold()
   #fontMain = "(" + "Times New Roman" + ", " + str(fontSize) + a + ")"
   fontMain = ("Times New Roman", fontSize, a)
   textmain.configure(state="normal")
   textmain["font"] = fontMain
   textmain.configure(state="disabled")
   textside.configure(state="normal")
   textside["font"] = fontMain
   textside.configure(state="disabled")

def Option1Event():
   ToggleTheme()

def Option2Event():
   FontSizeDown()

def Option3Event():
   FontSizeReset()

def Option4Event():
   FontSizeUp()

def Option5Event():
   ToggleBold()

def Option6Event():
   ToggleColor()
   
def Option7Event():
   ToggleSide()

def OutputMainText(texts:str, reset:bool):
   global textmain
   if reset == False:
      TextBoxes.AddMain(texts)
   if reset == True:
      TextBoxes.ClearAddMain(texts)

#window
root = tkinter.Tk()
root.title("Pymin")
root.geometry("1176x662")

#themes
cregionfont = "font=('TimesNewRoman', 24, 'bold')"
"""
#theme1 'cregionstyle', background="#FFFFFF", foreground="#000000", ?bold?, ?textsize24?
#theme2 'textstyle', background="#FFFFFF", foreground="#000000"
"""


#fonts

#images
#quitimg = tkinter.PhotoImage(file="./images/0.png")
quitimg = tkinter.PhotoImage(data='\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\n\x00\x00\x00\n\x08\x04\x00\x00\x00\';\x076\x00\x00\x03\x19zTXtRaw profile type exif\x00\x00x\xda\xed\x97[r\x1c!\x0cE\xffYE\x96\x80\x04Bb9<\xab\xb2\x83,?\x17\x9a\x99\xcc\xd8y\xd8\xe5\xafTMS\r\xb4\xa0%\xa1#\xf5\xd8n\xfc\xf8>\xdd7\\\xec\x83wQ\xd4RN\xc9\xe3\x8a9f.\x98\x98\xbf\xae\xb2{\xf2q\xf7\x8f\xb2\xf5\xfc$w\xf7\x05\x86(`\x0c\xd7\xa3\xa5#\x1f\x903\xf6\xf3\x91\xb7\xa3\xa7@.\x0f\x8a\xf28\x0b\xf5y\xa1\x1cEl\xc7\xc0\xcd\xa3c(\xd0e\xc0\xf7\xa3\xa8\x1cE\x81\x8f\xe5x=\xd7c9e\xd3\xc7#\x9c\xf7\xd6\xf1\xe9\x8c\xfbv\xab\x8bA9I"\x8d\xe8#{\xd5\x9417\xf6Q\x11\xb7\xbe\x1c\x9d\x8d\xf3zO\xea\xa5\xe7\xed\xb3\xbbmE\xe4\x99G\xa0\xe0wo\x97\x97a\xdd\x1c\n\xc6\x8c\x9e\xb0\x07\x87\xda\xf3\x08Y\xc1Z\xdc\xf1\xf5\x0e\xc8\xe0\x02<\xcf\'\xb6\xc3\xdf\xa3\xf9\x14\x9b\xdb\xf8\x87\xcb}\xe4X\'\x1d\x9e\xd3\xe06;i\xe0\xde-\xbcI\x834\x8e<\xbc\xa1\x97\xee\xe3\x96\xbb\xb7\x0b$\xbf\xc7\xbd\x99>x\xa4\xf1n\x98\x9f<\xd2p\xb7\xe1\x1f\xb1\xae{\xcens\x8e\xebt%&\x1c9\x9dC\xddNBn\xa3\x9c\xbd\xae$\xd8\xaf%4\xc5-\x98\xebn\x19\xcdP\x01\r9\xd6}\xf3\x15\xadQ&\x06\xe2I\x91:\x15\x9a\x8e\xc6\x9e4j\xf01\xf2`\xc5\xc8\xdc8l\x99\x81E\xe6\x16\x16\xf4\xb8\x1aMV\xe0\xef\xc1\x80\xbe!U\x02\xa4<\xa7;\xbe\xd0\xb6\x9b\xb7\xbdF\x06\xcb\x9d\xb0\x95\t\xcah\xe7\xd2?\x9a\xfb\xc8\xa6\xbf\xb59W-\x11\xb9S3t\x01\xe6U\x86pc\x91[=\xb6\x81\x08\xcd\x13T\xd9\x01\xbe\xb5\xe7\x84<`\x03\x10\xca\x0e\xb3\xe1\x80\xc5\xd7KE\x15\xfa\x95[a\x83\x0e\xd8\'\x18\xaf\xe2&\xed\xd7\xfbKQ\x84m\x813\x14\x80\xc0\'\nB\x89\xbc2+\x11\x02i\x00T\xc8\x1b\xca\x8a+\x08\x90\x08w8\xc91\x84\x046(\x02\x98vxGi\xefe\xe1K\x8e\xaf$HHHA\xc1\x06\x05\nX1\n\xf2G\xa3!\x87\x8a\x04\x89"\x92D\xc5$KI!E\x87\nKI\xd3\xfa\xdc\x16\r\x1aU4\xa9\xaai\xd6b\xc1\xa2\x89%S3\xcbV2\xe7\x80\xaf\xb1d\x94c\xb6\x9cs)\xb0Y\xa0\xb9$W\xb0\xbf@R\xb9\x86\x1a\xab\xd4T\xb5Z\xcd\xb54\xa4O\x8bMZj\xda\xac\xe5V:\xf7\xd0Q\xc7=u\xed\xd6s/\x83\x06Ri\xc4!n\xa4\xa1\xc3F\x1ee"\xd7f\x98q\xcaLS\xa7\xcd<\xcb\x9d\xda\xa1\xfa\xae}\x82\x1a\x1dj\xbcI\xad}z\xa7\x06\xa9\xea5\xba\x9d/P\xb2\x98\x81\x18G\x02q]\x04\xd6\xe7p1\xf3F1\xf2"\xb7\x98\xf9\xcc\xa8\na8)\x8bM\'_(qt!\x0eb\x99tg\xf7\x8b\xdc\xa7\xb8\xb9\x14\xff\xca\x8d?J\xce-t_$\xb7\xb9\xb9!\x0f\xdc~C\xad\xaf_\xe2\xb6\x89]U\xb8b\xea\x03\xaa\x0f\xeb\xc3\n[Y\xbf\xa2\xc5\xdd&_\x1d_\x8a^\x8a^\x8a^\x8a^\x8a^\x8a^\x8a\xfecE\x13\x7f<\xe0?J\xf7\x13\xa7\xd0\xbc\x08=]s5\x00\x00\x01#iCCPICC profile\x00\x00x\x9c\x9d\x90\xbfJ\xc3P\x14\xc6\x7f\xa9\xe2?\xec\xa48\x14\x87\x0c\xe2Vp1\x93KU\x08B\x85\x18+X\x9d\xd2$\xc5b\x12C\x92R|\x03\xdfD\x1f\xa6\x83 \xf8\x08>\x80\x82\xb3\xdf\x8d\x0e\x0ef\xf1\xc2\xe1\xfbq8\xe7\xfb\xee\xbd\xd0\xb2\x930-\x17\xf7 \xcd\xaa\xc2\xf5{\xc3\xcb\xe1\x95\xbd\xfc\xc6*m\xa0\xc3n\x10\x96y\xcf\xf3\xfa4\x9e\xcfW,\xa3/]\xe3\xd5<\xf7\xe7Y\x8a\xe22\x94\xceUY\x98\x17\x15X\x07bgV\xe5\x86Ul\xde\x0e\xfc#\xf1\x83\xd8\x8e\xd2,\x12?\x89w\xa242lv\xfd4\x99\x86?\x9e\xe66\xebqvqn\xfa\xaam\\N8\xc5\xc3f\xc4\x94\t\t\x15]i\xa6\xce1\x0e\xfbR\x97\x82\x80{JBiB\xac\xdeL3\x157\xa2RN.\x87\xa2\x81H\xb7i\xc8\xeb\xd4y\x9eRF\xf2\x98\xc8\xcb$\xdc\x91\xca\xd3\xe4a\xfe\xf7{\xed\xe3\xac\xde\xb4\xb6\xe6yP\x04ukA\xd5\x1a\x8f\xe1\xfd\x11\xdaC\xd8x\x86\xb5\xeb\x86\xac\x95\xdfok\x98q\xea\x99\x7f\xbe\xf1\x0b\xd6\x9bP\\\x8a\xac\x86\x96\x00\x00\x00\x02bKGD\x00\xff\x87\x8f\xcc\xbf\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x00\x07tIME\x07\xe6\t\r\x00(\x1aS\x8c\xbfC\x00\x00\x00\x19tEXtComment\x00Created with GIMPW\x81\x0e\x17\x00\x00\x00\xddIDAT\x08\x1d\x01\xd2\x00-\xff\x00\x00\x00\x00\x14\x00\xff\x00\x00\x00\xff\x00\xff\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00\x00\x00\xff\x00\xff\x00\x00\x00\xff\x00\xff\x00\x00\x02\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x01\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00/\x16\x10\x1a\xbb\xa6VN\x00\x00\x00\x00IEND\xaeB`\x82')
resetimg = tkinter.PhotoImage(data='\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\n\x00\x00\x00\n\x08\x06\x00\x00\x00\x8d2\xcf\xbd\x00\x00\x01\x84iCCPICC profile\x00\x00(\x91}\x91=H\xc3@\x1c\xc5_S\xa5*\x15\x053\x888D\xa8.Z\x10\x15q\xd4*\x14\xa1B\xa8\x15Zu0\x1f\xfd\x82&\rI\x8a\x8b\xa3\xe0Zp\xf0c\xb1\xea\xe0\xe2\xac\xab\x83\xab \x08~\x808:9)\xbaH\x89\xffK\n-b<8\xee\xc7\xbb{\x8f\xbbw\x00W+)\x9a\xd56\x0eh\xbam&\xe31!\x9dY\x15B\xaf\xe8D/x\x8cbHR,cN\x14\x13\xf0\x1d_\xf7\x08\xb0\xf5.\xca\xb2\xfc\xcf\xfd9\xba\xd5\xac\xa5\x00\x01\x81xV1L\x9bx\x83xz\xd36\x18\xef\x13\xf3JAR\x89\xcf\x89\xc7L\xba \xf1#\xd3e\x8f\xdf\x18\xe7]\xe6X&o\xa6\x92\xf3\xc4<\xb1\x90oa\xb9\x85\x95\x82\xa9\x11O\x11GTM\xa7|.\xed\xb1\xcax\x8b\xb1V\xaa(\x8d{\xb2\x17\x86\xb3\xfa\xca2\xd3i\x0e"\x8eE,A\x84\x00\x19\x15\x14Q\x82\x8d(\xad:)\x16\x92\xb4\x1f\xf3\xf1\x0f\xb8~\x91\\2\xb9\x8aP\xc8\xb1\x8024H\xae\x1f\xec\x0f~wk\xe5&\'\xbc\xa4p\x0ch\x7fq\x9c\x8fa \xb4\x0b\xd4\xab\x8e\xf3}\xec8\xf5\x13 \xf8\x0c\\\xe9M\x7f\xb9\x06\xcc|\x92^mj\x91#\xa0g\x1b\xb8\xb8nj\xf2\x1ep\xb9\x03\xf4?\x19\x92)\xb9R\x90&\x97\xcb\x01\xefg\xf4M\x19\xa0\xef\x16\xe8Z\xf3zk\xec\xe3\xf4\x01HQW\x89\x1b\xe0\xe0\x10\x18\xc9S\xf6\xba\xcf\xbb;Z{\xfb\xf7L\xa3\xbf\x1f\x9d\x90r\xb8\x12I\x12\x89\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x00\x07tIME\x07\xe6\t\x10\x15\x02#\xdb|\x15\xba\x00\x00\x00\x19tEXtComment\x00Created with GIMPW\x81\x0e\x17\x00\x00\x01\xa5IDAT\x18\x19\x01\x9a\x01e\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xff\x00\x00\xff\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x02\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb5\xaf\x13\xf9\xd40\x96{\x00\x00\x00\x00IEND\xaeB`\x82')
refreshimg = tkinter.PhotoImage(data='\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\n\x00\x00\x00\n\x08\x04\x00\x00\x00\';\x076\x00\x00\x01%iCCPICC profile\x00\x00(\x91\x9d\x90\xcdJ\xc3P\x10\x85\xbfV\xf1\x0f\x05\xc1\xe2B\\d\xe1\xb6\xe2\xc6\xae\xdcT\x85PP\x88\xb5\x82\xd1Uz\xd3b0\x89!I)\xbe\x81o\xa2\x0f\xd3\x85 \xf8\x08>\x80\x82k\xcf\x8d.\\\x98\x8d\x17\x86\xf9\x18f\xce\x99\xb9\xd0tb\x93\x14\xf3{\x90\xa4e\xee\xf6\xbb\xfe\xa5\x7f\xe5,\xbe\xb1\xcc:-\xda\xec\x06\xa6\xc8\xba\x9ewB\xed\xfb|\xa5a\xf3K\xdbj\xd5\xf7\xfd\xf9\x16\xc2Qa\x94g\x8a\xd4dy\t\x8d\x03qgZf\x96\x15\xb4n\x07\xfd#\xf1\x83\xd8\t\x934\x14?\x89w\xc2$\xb4lg\xfbI<1?\x9av\x9b\xd5Qzqn\xeb\x8am\\z\x9c\xe2\xe10dBDL\xa9\xdb"RU\x8e\xe9\xb0\xaf\xec\x92\x13pO\x81Q\x8e\x19\xa96UO\xc9\x8d\xa8\x90\x92\xcb\xa1h \xd265~[\x95\x9f\'\x97\xa14"iY\x87;\x12iZ?\xec\xff~\x8f}\x9cU\x93\x8d\xcdY\x16\xe4AU\x9aS4\xc7cx\x7f\x845\x1f6\x9ea\xe5\xba\xc6k\xe9\xf7m5=\x9d\xaa\xe7\x9f7~\x01:\x9cP\x8ei!\xbbN\x00\x00\x00\x02bKGD\x00\xff\x87\x8f\xcc\xbf\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x00\x07tIME\x07\xe6\t\x10\x14:#\xcd!\xc3v\x00\x00\x00\x19tEXtComment\x00Created with GIMPW\x81\x0e\x17\x00\x00\x00\xddIDAT\x08\x1d\x01\xd2\x00-\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x01\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\'2\n\x01*N\xdf\x02\x00\x00\x00\x00IEND\xaeB`\x82')
valupimg = tkinter.PhotoImage(data='\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\r\x00\x00\x00\r\x08\x06\x00\x00\x00r\xeb\xe4|\x00\x00\x01\xedIDATx^\x95\x91\xcdO\xd2\x01\x18\xc7\xfd\x0f\xda:t\xaeu\xe8\x94\xd7\\\xb4U\xae\xa2\x01\xa5\xcd\x86\xb5h\xadt\xad\xb9\xca\xb5\xdaz\xb5\xda\xb2\x8bk\xe5Z\xcb\x03m\xe5fI"\x8b\x10,R\x98B5A\xad\\\x86\xa0\x84 "o?\xe45\n\xb0>a\x1c\xb4\xd1\xa5\xcf\xe5\xb9<\x9f=\xcf\xf3}**V\xd1a\xea\xe2k\xc6\x8b;\xe7\xc7\x9dw\x12#\xc0%e\x0b\xab{\xfe\xc2.L\xe0X\x18e:=\xcaT\xe4\x03\x9f\xe7\xdf\xe2\x08Y\xf0\xf8\xad\x8cEF\xcaE\xd5\x8c\x16\xa3O\xc3\xc8\xb4\x96\xf73:\n\x858\x85\xa5\x0c\x1f\xbdC|Y\xd0a\x13z\xb0x{W\xc4Gf\r\xcf\xdd]\xbc\x9c|\x80\xc1\xf1\x18gr\x02\x96 \xff\x1d\x12d\xb1z\x94\x8c\xcd\xb63\xe0\xee\xe0\x9e\xb9\xbd$*\x9d\xf7i\xb5\xb7\xf2\xd0v\x9d[\xfak\xa4\x84,\xd1\xd4\x0f\xb2\xa94\xb9D\x12\x9b\xdfN\xbf\xeb\x06/\x1c\xb7QO\xb5\x95\xa4&\xf3M\xee\x0c\x9d\xe5\xcax\x0bA\xc1\x890\xe7\'\x10\x08\x12\x88\x86\xf1\xc5\xc2\xcc\x05}\\\xedmB5\xae\xe0\xee\xa7\xd3%\xa9\xee\xd5Qj\xfa\x0e\xb0\x98\x16\x08D`6\xe2"&\x84\x88\xc4\xa3\x04\xe2I\xe2\xd1\x10\xa1p\x8cFc#m\xd6\x13%\xa9J]\xcb\x8e\xfe\xbd\x1c\x1fl\xa6\xae\xa7\x1aO1\xe6D:Bf1A.\x96\xe3\xfc\xbb\x06\xe4\xcf\x8eqyP\xca~\xd5\xe6\x92\xb4\xa7S\xc16C5\x07u\xbb8\xd2\'e\xfe\x97\xabx\xfe7\xb2\xf9\xc2\x9f4.\x0e\xc8h6\xed\xe6\xcc\xb0\x98\xfaa\xc5J\x82U\xda\xc3\x88\xf5R\xea\xf5;\x8b\x93B,\x93\xff\t\xa9b=i\x92q\xea\xf5v6\xa8E\xe5\xbf\xda\xa8\x96SY\x9cVc\x94 5\x88\x91\xbd\x91 7\xeeCb\xaceSq\xedsO.\x94K\xcbTv\x1fb\xbdF\xcc\xda\xce-\xac\xe9\xde\xca\xba\xa7"D\x96\x86\x7f7\xff/\xbf\x01\x7f(s\x97\x8cN\xac\xd0\x00\x00\x00\x00IEND\xaeB`\x82')
valdownimg = tkinter.PhotoImage(data='\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\r\x00\x00\x00\r\x08\x06\x00\x00\x00r\xeb\xe4|\x00\x00\x01\xe1IDATx^\x95\x91=h\x13a\x18\x80?%\xa9\x8a\x15l\'\x1d\xaa\xe2\xeab\x17\x05q\xc9R\x07A\xfc\xc9$U\x043\xa9(\x19D,6\xd4\x1f\x10\x04\xb1H;)\x14\xa9\xe2_ \x14"B\x1c,\x05\x83\xd86\xc6\xaa\xa7\x963M\x93\\r\xb9$w\x97\xc4\xe4rI\xf51\x92B+q\xf1\x81w\xf9x\x9e\xe1\xfd^!V\x91\x7ft\x89\x8f\x17\xb625\xd4\xcd\xcbA\xc1\x07\xdf\x16BC{X\xed\xfcE\xa4\xbf\x87\xf7\xde.\x14\x97\x03\xbdO\xa0\x1f\x16\xc4\xfa\xd7\x139\xdb\xc1\x9b\x01g{8\xd1\xb7\x96\xb4k\x1d\x8dm\x0e\x90\x1fC~\x16T\t\xb2\xd3\xe4\x8el y\xba\x93\xaf\x977\xad\x84\x85\xf1[\x98\xbb\xd7\xa0w\x0b\x96\x9c\x02t\x05\xbbl\x81\x015\xbbA\xc2%0\x0e\t\x92\xc7\x04\xa1\x8b\xcba\xa0\xb7\xf9\xd0\x94\xbf\xed\xdc\x8c\xed\xec\x02m\x9e\x1f5\x8b\xbaa\x91\xad\x95Im\x17\xcc\x1d\xdc\x88\xe1v\x10\xf7v\xb4"{_\x0f\xb9N\'\xb2*S\xacJ\x14J2\x95T\x1eSkM\xa3\xae\xa2\x185>\x9f\xd8\x85\xe6\xdd\xd1\x8aR\xee\xfd\xd0\xe7F\xf2\x1cGM\xd6Y\xc8-\x90O6E%I.\x91\xa1\xb8\x98\xa0\x1a}\x80yf/\xb1+\xbd\xadh\xd1s\x12\xd5\xe3\xc5\xf4\r2?s\x8f\xbaYD\xb1-\xf2U\x9db\xb9D\xf9\x97D\xc2{\x00\xe5\xfa)\xa4\xdb\xe7\x96w\x1a8Jud\x1csx\x84\xec\xfd\xbb4l\x8d\xb2\xd1\x0c\xea\x15lK#r\xc7G\xe6\xe6y\xe4\xb1k\xc4\xfd7V~0\xfel\x98T\xf0\t\x99\x17~\xe4WA*E\x9d\x9fK\x16\x9f\x02O\xc9\x05F\xd1\x02\xcfI\x87F\xdbo\x15\x9f\xf5\xa3\xbc\x9d\xa2\x14\r3\x1d\x9e\xa4\x90\x8e\xa1\xbe{\x8d\x1a\x0e\x91\x96\x82L<\xbc\xda\x1e\xfd!:9F!1C6\xfe\x05=\xf3\x1dM\x9bC)\x84\xff-\xff/\xbf\x01\xaa\xdfn\x93\xd1\x12\xd9\x91\x00\x00\x00\x00IEND\xaeB`\x82')



#main
mainframe = ttk.Frame(root)
mainframe.place(anchor="nw", height=662, width=1176)
mainframe['padding'] = (20,30,0,0)

bccolorlabel1 = ttk.Label(mainframe)
bccolorlabel1.place(anchor="nw", height=662, width=1176, x=-20, y=-30)

#statframe
statframe = ttk.Frame(mainframe)
statframe.place(anchor="nw", height=611, width=180, x=0, y=0)

bccolorlabel2 = ttk.Label(statframe)
bccolorlabel2.place(anchor="nw", height=611, width=180)

"""
label1 = ttk.Label(statframe, text="Base Stats")
label1.place(x=0, y=0)

strlabel = ttk.Label(statframe, text="Strength")
strlabel.place(anchor=NW, x=0, y=40)
strcolonlabel = ttk.Label(statframe, text=":")
strcolonlabel.place(anchor=N, x=90, y=39)
strvallabel = ttk.Label(statframe, text="value")
strvallabel.place(anchor=NW, x=110, y=40)
strimglabel = ttk.Label(statframe)
strimglabel.place(anchor=NW, height=21, width=21, x=154, y=40)

mentlabel = ttk.Label(statframe, text="Mentality")
mentlabel.place(anchor=NW, x=0, y=60)
mentcolonlabel = ttk.Label(statframe, text=":")
mentcolonlabel.place(anchor=N, x=90, y=59)
mentvallabel = ttk.Label(statframe, text="vabel")
mentvallabel.place(anchor=NW, x=110, y=60)
mentimglabel = ttk.Label(statframe)
mentimglabel.place(anchor=NW, height=21, width=21, x=154, y=60)

liblabel = ttk.Label(statframe, text="Libido")
liblabel.place(anchor=NW, x=0, y=80)
libcolonlabel = ttk.Label(statframe, text=":")
libcolonlabel.place(anchor=N, x=90, y=79)
libvallabel = ttk.Label(statframe, text="value")
libvallabel.place(anchor=NW, x=110, y=80)
libimglabel = ttk.Label(statframe)
libimglabel.place(anchor=NW, height=21, width=21, x=154, y=80)

senlabel = ttk.Label(statframe, text="Sensitivity")
senlabel.place(anchor=NW, x=0, y=100)
sencolonlabel = ttk.Label(statframe, text=":")
sencolonlabel.place(anchor=N, x=90, y=99)
senvallabel = ttk.Label(statframe, text="value")
senvallabel.place(anchor=NW, x=110, y=100)
senimglabel = ttk.Label(statframe)
senimglabel.place(anchor=NW, height=21, width=21, x=154, y=100)

label6 = ttk.Label(statframe, text="Combat Stats")
label6.place(anchor=NW, x=0, y=140)

hplabel = ttk.Label(statframe, text="HP")
hplabel.place(anchor=NW, x=0, y=160)
hpcolonlabel = ttk.Label(statframe, text=":")
hpcolonlabel.place(anchor=N, x=90, y=159)
hpvallabel = ttk.Label(statframe, text="value")
hpvallabel.place(anchor=NW, x=110, y=160)
hpimglabel = ttk.Label(statframe)
hpimglabel.place(anchor=NW, height=21, width=21, x=154, y=160)

lustlabel = ttk.Label(statframe, text="Lust")
lustlabel.place(anchor=NW, x=0, y=180)
lustcolonlabel = ttk.Label(statframe, text=":")
lustcolonlabel.place(anchor=N, x=90, y=179)
lustvallabel = ttk.Label(statframe, text="value")
lustvallabel.place(anchor=NW, x=110, y=180)
lustimglabel = ttk.Label(statframe)
lustimglabel.place(anchor=NW, height=21, width=21, x=154, y=180)

hungerlabel = ttk.Label(statframe, text="Hunger")
hungerlabel.place(anchor=NW, x=0, y=200)
hungercolonlabel = ttk.Label(statframe, text=":")
hungercolonlabel.place(anchor=N, x=90, y=199)
hungervallabel = ttk.Label(statframe, text="value")
hungervallabel.place(anchor=NW, x=110, y=200)

label10 = ttk.Label(statframe, justify=CENTER, text="Current Region")
label10.place(anchor=N, x=90, y=250)
currentregionlabel = tkinter.Label(statframe, justify=CENTER, text="Region", font=('TimesNewRoman', 20, 'bold'))
currentregionlabel.place(anchor=N, height=40, width=120, x=90, y=270)

levellabel = ttk.Label(statframe, text="Level")
levellabel.place(anchor=NW, x=0, y=340)
levelcolonlabel = ttk.Label(statframe, text=":")
levelcolonlabel.place(anchor=N, x=90, y=339)
levelvallabel = ttk.Label(statframe, text="value")
levelvallabel.place(anchor=NW, x=110, y=340)

sexplabel = ttk.Label(statframe, text="SexP")
sexplabel.place(anchor=NW, x=0, y=360)
sexpcolonlabel = ttk.Label(statframe, text=":")
sexpcolonlabel.place(anchor=N, x=90, y=359)
sexpvallabel = ttk.Label(statframe, text="value")
sexpvallabel.place(anchor=NW, x=110, y=360)

coinlabel = ttk.Label(statframe, text="Coin")
coinlabel.place(anchor=NW, x=0, y=380)
coincolonlabel = ttk.Label(statframe, text=":")
coincolonlabel.place(anchor=N, x=90, y=379)
coinvallabel = ttk.Label(statframe, text="value")
coinvallabel.place(anchor=NW, x=110, y=380)

daylabel = ttk.Label(statframe, text="Day")
daylabel.place(anchor=NW, x=0, y=420)
daycolonlabel = ttk.Label(statframe, text=":")
daycolonlabel.place(anchor=N, x=90, y=419)
dayvallabel = ttk.Label(statframe, text="value")
dayvallabel.place(anchor=NW, x=110, y=420)
hourlabel = ttk.Label(statframe, text="Hour")
hourlabel.place(anchor=NW, x=0, y=440)
hourcolonlabel = ttk.Label(statframe, text=":")
hourcolonlabel.place(anchor=N, x=90, y=439)
hourvallabel = ttk.Label(statframe, text="value")
hourvallabel.place(anchor=NW, x=110, y=440)

savegamebutton = tkinter.Button(statframe, text="Save Game")
savegamebutton.place(anchor=N, height=30, width=100, x=90, y=480)
"""
loadgamebutton = tkinter.Button(statframe, text="Load Game")
loadgamebutton.place(anchor="n", height=30, width=100, x=90, y=515)
newgamebutton = tkinter.Button(statframe, text="New Game")
newgamebutton.place(anchor="n", height=30, width=100, x=90, y=550)

quitbutton = tkinter.Button(statframe, image=quitimg,command=root.destroy)
quitbutton.place(anchor="nw", height=20, width=20, x=0, y=591)
resetbutton = tkinter.Button(statframe, image=resetimg,command="reset()")
resetbutton.place(anchor="nw", height=20, width=20, x=25, y=591)
refreshbutton = tkinter.Button(statframe, image=refreshimg,command="refreshall()")
refreshbutton.place(anchor="nw", height=20, width=20, x=50, y=591)


buttonpanel = ttk.Frame(mainframe)
buttonpanel.place(anchor="nw", height=179, width=662, x=180, y=0)

bccolorlabel3 = ttk.Label(buttonpanel)
bccolorlabel3.place(anchor="nw", height=179, width=662)

"""button1 = tkinter.Button(buttonpanel, text="Button 1", command=PyminInterfaceActions.PanelButton1.Destroy)
button1.place(anchor=NW, height=46, width=140, x=0, y=0)
button2 = tkinter.Button(buttonpanel, text="Button 2")
button2.place(anchor=NW, height=46, width=140, x=160, y=0)
button3 = tkinter.Button(buttonpanel, text="Button 3")
button3.place(anchor=NW, height=46, width=140, x=320, y=0)
button4 = tkinter.Button(buttonpanel, text="Button 4")
button4.place(anchor=NW, height=46, width=140, x=480, y=0)
button5 = tkinter.Button(buttonpanel, text="Button 5")
button5.place(anchor=NW, height=46, width=140, x=0, y=66)
button6 = tkinter.Button(buttonpanel, text="Button 6")
button6.place(anchor=NW, height=46, width=140, x=160, y=66)
button7 = tkinter.Button(buttonpanel, text="Button 7")
button7.place(anchor=NW, height=46, width=140, x=320, y=66)
button8 = tkinter.Button(buttonpanel, text="Button 8")
button8.place(anchor=NW, height=46, width=140, x=480, y=66)
button9 = tkinter.Button(buttonpanel, text="Button 9")
button9.place(anchor=NW, height=46, width=140, x=0, y=132)
button10 = tkinter.Button(buttonpanel, text="Button 10")
button10.place(anchor=NW, height=46, width=140, x=160, y=132)
button11 = tkinter.Button(buttonpanel, text="Button 11")
button11.place(anchor=NW, height=46, width=140, x=320, y=132)
button12 = tkinter.Button(buttonpanel, text="Button 12")
button12.place(anchor=NW, height=46, width=140, x=480, y=132)"""

#textmain
textmain = tkhtml.HTMLScrolledText(mainframe, cursor="arrow", wrap="word")
textmain.place(anchor="nw", height=430, width=622, x=180, y=180)
textmain.delete(1.0,"end")
textmain.insert(1.0, "yeet")
textmain.configure(state="disabled")


#frame
frame2 = ttk.Frame(mainframe)
frame2.place(anchor="nw", height=179, width=334, x=802, y=0)

bccolorlabel4 = ttk.Label(frame2)
bccolorlabel4.place(anchor="nw", height=179, width=334)

"""bagstashlabel = ttk.Label(frame2, text="BAG 1")
bagstashlabel.place(anchor=NW, height=30, width=80, x=20, y=0)"""
"""
moveitembutton = tkinter.Button(frame2, text="Move Item")
moveitembutton.place(anchor=CENTER, height=46, width=140, x=167, y=90)
"""

#sidebar
sidebar = ttk.Frame(mainframe)
sidebar.place(anchor="nw", height=432, width=334, x=803, y=180)

bccolorlabel5 = ttk.Label(sidebar)
bccolorlabel5.place(anchor="nw", height=432, width=334)

"""looksbutton = tkinter.Button(sidebar, text="Look")
looksbutton.place(anchor=NW, width=80, x=0, y=0)
statsbutton = tkinter.Button(sidebar, text="Stats")
statsbutton.place(anchor=NW, width=80, x=83, y=0)
effectsbutton = tkinter.Button(sidebar, text="Effects")
effectsbutton.place(anchor=NW, width=80, x=166, y=0)
helpbutton = tkinter.Button(sidebar, text="Help")
helpbutton.place(anchor=NW, width=80, x=249, y=0)
levelsbutton = tkinter.Button(sidebar, text="Levels")
levelsbutton.place(anchor=NW, width=80, x=0, y=30)
gearbutton = tkinter.Button(sidebar, text="Gear")
gearbutton.place(anchor=NW, width=80, x=83, y=30)
titlesbutton = tkinter.Button(sidebar, text="Titles")
titlesbutton.place(anchor=NW, width=80, x=166, y=30)
creditsbutton = tkinter.Button(sidebar, text="Credits")
creditsbutton.place(anchor=NW, width=80, x=249, y=30)

"""
textside = tkhtml.HTMLScrolledText(sidebar, cursor="arrow", wrap="word")
textside.place(anchor="nw", height=300, width=330, x=0, y=80)
textside.configure(state="disabled")
"""

appearancebutton = tkinter.Button(sidebar, text="Appearance")
appearancebutton.place(anchor=CENTER, height=50, width=150, x=167, y=216)

"""
themebutton = tkinter.Button(sidebar, text="Theme", command=Option1Event)
themebutton.place(anchor="nw", height=30, width=60, x=0, y=385)
textsizedownbutton = tkinter.Button(sidebar, text="A", command=Option2Event)
textsizedownbutton.place(anchor="nw", height=30, width=30, x=83, y=385)
textsizedownbutton["font"] = ("Times New Roman", 10)
textsizeresetbutton = tkinter.Button(sidebar, text="A", command=Option3Event)
textsizeresetbutton.place(anchor="nw", height=30, width=30, x=118, y=385)
textsizeresetbutton["font"] = ("Times New Roman", 12)
textsizeupbutton = tkinter.Button(sidebar, text="A", command=Option4Event)
textsizeupbutton.place(anchor="nw", height=30, width=30, x=153, y=385)
textsizeupbutton["font"] = ("Times New Roman", 14)
textboldbutton = tkinter.Button(sidebar, text="B", command=Option5Event)
textboldbutton.place(anchor="nw", height=30, width=30, x=200, y=385)
textcolorbutton = tkinter.Button(sidebar, text="C", command=Option6Event)
textcolorbutton.place(anchor="nw", height=30, width=30, x=245, y=385)
themebutton7 = tkinter.Button(sidebar, text="O", command=Option7Event)
themebutton7.place(anchor="nw", height=30, width=30, x=301, y=385)

ChangeBackgroundColor("#FFFFFF")
ChangeTextColor("#000000")
UpdateText()

#OutputMainText("Nimin: Fetish Fantasy\n\tv" + versionNumber + "\n\nClick 'New Game' to begin a new game.\n\nCreated by:\t--Xadera\n\twww.furaffinity.net/user/xadera/\n\nOriginal concept by:\t--Fenoxo\n\tfenoxo.com\n\nCurrently maintained by:\tajdelguidice\n\tgithub.com/ajdelguidice\nFor tutorial/guide, questions, or bug reports, visit github.com/ajdelguidice/pymin/", True)
OutputMainText("Nimin: Fetish Fantasy\n\tv" + versionNumber + "\n\nClick 'New Game' to begin a new game.\n\nCreated by:\t--Xadera\n\twww.furaffinity.net/user/xadera/\n\nOriginal concept by:\t--Fenoxo\n\tfenoxo.com\n\n\nFor tutorial/guide, questions, or bug reports, visit Xadera's page at the link above.", True)
TextBoxes.DisplayMainHTML()

root.mainloop()