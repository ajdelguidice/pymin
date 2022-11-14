import tkinter
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

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
   global bccolorlabel1, bccolorlabel2, bccolorlabel3, bccolorlabel4, bccolorlabel5, textmain, textside, label1, strlabel, strcolonlabel, strvallabel, strimglabel, mentlabel, mentcolonlabel, mentvallabel, mentimglabel, liblabel, libcolonlabel, libvallabel, libimglabel, senlabel, sencolonlabel, senvallabel, senimglabel, label6, hplabel, hpcolonlabel, hpvallabel, hpimglabel, lustlabel, lustcolonlabel, lustvallabel, lustimglabel, hungerlabel, hungercolonlabel, hungervallabel, label10, currentregionlabel, levellabel, levelcolonlabel, levelvallabel, sexplabel, sexpcolonlable, sexpvallabel, coinlabel, coincolonlabel, coinvallabel, daylabel, daycolonlabel, dayvallabel, hourlabel, hourcolonlabel, hourvallabel, bagstashlabel, savegamebutton, loadgamebutton, newgamebutton, quitbutton, resetbutton, refreshbutton, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, looksbutton, statsbutton, effectsbutton, helpbutton, levelsbutton, gearbutton, creditsbutton, appearancebutton, themebutton, textsizedownbutton, textsizeresetbutton, textsizeupbutton, textboldbutton, textcolorbutton, themebutton7
   try:
      bccolorlabel1["background"] = color
   except:
      x = 0
   try:
      bccolorlabel2["background"] = color
   except:
      x = 0
   try:
      bccolorlabel3["background"] = color
   except:
      x = 0
   try:
      bccolorlabel4["background"] = color
   except:
      x = 0
   try:
      bccolorlabel5["background"] = color
   except:
      x = 0
   try:
      textmain["background"] = color
   except:
      x = 0
   try:
      textside["background"] = color
   except:
      x = 0
   try:
      label1["background"] = color
   except:
      x = 0
   try:
      strlabel["background"] = color
   except:
      x = 0
   try:
      strcolonlabel["background"] = color
   except:
      x = 0
   try:
      strvallabel["background"] = color
   except:
      x = 0
   try:
      strimglabel["background"] = color
   except:
      x = 0
   try:
      mentlabel["background"] = color
   except:
      x = 0
   try:
      mentcolonlabel["background"] = color
   except:
      x = 0
   try:
      mentvallabel["background"] = color
   except:
      x = 0
   try:
      mentimglabel["background"] = color
   except:
      x = 0
   try:
      liblabel["background"] = color
   except:
      x = 0
   try:
      libcolonlabel["background"] = color
   except:
      x = 0
   try:
      libvallabel["background"] = color
   except:
      x = 0
   try:
      libimglabel["background"] = color
   except:
      x = 0
   try:
      senlabel["background"] = color
   except:
      x = 0
   try:
      sencolonlabel["background"] = color
   except:
      x = 0
   try:
      senvallabel["background"] = color
   except:
      x = 0
   try:
      senimglabel["background"] = color
   except:
      x = 0
   try:
      label6["background"] = color
   except:
      x = 0
   try:
      hplabel["background"] = color
   except:
      x = 0
   try:
      hpcolonlabel["background"] = color
   except:
      x = 0
   try:
      hpvallabel["background"] = color
   except:
      x = 0
   try:
      hpimglabel["background"] = color
   except:
      x = 0
   try:
      lustlabel["background"] = color
   except:
      x = 0
   try:
      lustcolonlabel["background"] = color
   except:
      x = 0
   try:
      lustvallabel["background"] = color
   except:
      x = 0
   try:
      lustimglabel["background"] = color
   except:
      x = 0
   try:
      hungerlabel["background"] = color
   except:
      x = 0
   try:
      hungercolonlabel["background"] = color
   except:
      x = 0
   try:
      hungervallabel["background"] = color
   except:
      x = 0
   try:
      label10["background"] = color
   except:
      x = 0
   try:
      currentregionlabel["background"] = color
   except:
      x = 0
   try:
      levellabel["background"] = color
   except:
      x = 0
   try:
      levelcolonlabel["background"] = color
   except:
      x = 0
   try:
      levelvallabel["background"] = color
   except:
      x = 0
   try:
      sexplabel["background"] = color
   except:
      x = 0
   try:
      sexpcolonlabel["background"] = color
   except:
      x = 0
   try:
      sexpvallabel["background"] = color
   except:
      x = 0
   try:
      coinlabel["background"] = color
   except:
      x = 0
   try:
      coincolonlabel["background"] = color
   except:
      x = 0
   try:
      coinvallabel["background"] = color
   except:
      x = 0
   try:
      daylabel["background"] = color
   except:
      x = 0
   try:
      daycolonlabel["background"] = color
   except:
      x = 0
   try:
      dayvallabel["background"] = color
   except:
      x = 0
   try:
      hourlabel["background"] = color
   except:
      x = 0
   try:
      hourcolonlabel["background"] = color
   except:
      x = 0
   try:
      hourvallabel["background"] = color
   except:
      x = 0
   try:
      bagstashlabel["background"] = color
   except:
      x = 0

   try:
      savegamebutton["background"] = color
   except:
      x = 0
   try:
      savegamebutton["background"] = color
   except:
      x = 0
   try:
      loadgamebutton["background"] = color
   except:
      x = 0
   try:
      newgamebutton["background"] = color
   except:
      x = 0
   try:
      quitbutton["background"] = color
   except:
      x = 0
   try:
      resetbutton["background"] = color
   except:
      x = 0
   try:
      refreshbutton["background"] = color
   except:
      x = 0
   try:
      button1["background"] = color
   except:
      x = 0
   try:
      button2["background"] = color
   except:
      x = 0
   try:
      button3["background"] = color
   except:
      x = 0
   try:
      button4["background"] = color
   except:
      x = 0
   try:
      button5["background"] = color
   except:
      x = 0
   try:
      button6["background"] = color
   except:
      x = 0
   try:
      button7["background"] = color
   except:
      x = 0
   try:
      button8["background"] = color
   except:
      x = 0
   try:
      button9["background"] = color
   except:
      x = 0
   try:
      button10["background"] = color
   except:
      x = 0
   try:
      button11["background"] = color
   except:
      x = 0
   try:
      button12["background"] = color
   except:
      x = 0
   try:
      looksbutton["background"] = color
   except:
      x = 0
   try:
      statsbutton["background"] = color
   except:
      x = 0
   try:
      effectsbutton["background"] = color
   except:
      x = 0
   try:
      helpbutton["background"] = color
   except:
      x = 0
   try:
      levelsbutton["background"] = color
   except:
      x = 0
   try:
      gearbutton["background"] = color
   except:
      x = 0
   try:
      titlesbutton["background"] = color
   except:
      x = 0
   try:
      creditsbutton["background"] = color
   except:
      x = 0
   try:
      appearancebutton["background"] = color
   except:
      x = 0
   try:
      themebutton["background"] = color
   except:
      x = 0
   try:
      textsizedownbutton["background"] = color
   except:
      x = 0
   try:
      textsizeresetbutton["background"] = color
   except:
      x = 0
   try:
      textsizeupbutton["background"] = color
   except:
      x = 0
   try:
      textboldbutton["background"] = color
   except:
      x = 0
   try:
      textcolorbutton["background"] = color
   except:
      x = 0
   try:
      themebutton7["background"] = color
   except:
      x = 0

def ChangeTextColor(color):
   global bccolorlabel1, bccolorlabel2, bccolorlabel3, bccolorlabel4, bccolorlabel5, textmain, textside, label1, strlabel, strcolonlabel, strvallabel, strimglabel, mentlabel, mentcolonlabel, mentvallabel, mentimglabel, liblabel, libcolonlabel, libvallabel, libimglabel, senlabel, sencolonlabel, senvallabel, senimglabel, label6, hplabel, hpcolonlabel, hpvallabel, hpimglabel, lustlabel, lustcolonlabel, lustvallabel, lustimglabel, hungerlabel, hungercolonlabel, hungervallabel, label10, currentregionlabel, levellabel, levelcolonlabel, levelvallabel, sexplabel, sexpcolonlable, sexpvallabel, coinlabel, coincolonlabel, coinvallabel, daylabel, daycolonlabel, dayvallabel, hourlabel, hourcolonlabel, hourvallabel, bagstashlabel, savegamebutton, loadgamebutton, newgamebutton, quitbutton, resetbutton, refreshbutton, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, looksbutton, statsbutton, effectsbutton, helpbutton, levelsbutton, gearbutton, creditsbutton, appearancebutton, themebutton, textsizedownbutton, textsizeresetbutton, textsizeupbutton, textboldbutton, textcolorbutton, themebutton7
   try:
      bccolorlabel1["foreground"] = color
   except:
      x = 0
   try:
      bccolorlabel2["foreground"] = color
   except:
      x = 0
   try:
      bccolorlabel3["foreground"] = color
   except:
      x = 0
   try:
      bccolorlabel4["foreground"] = color
   except:
      x = 0
   try:
      bccolorlabel5["foreground"] = color
   except:
      x = 0
   try:
      textmain["foreground"] = color
   except:
      x = 0
   try:
      textside["foreground"] = color
   except:
      x = 0
   try:
      label1["foreground"] = color
   except:
      x = 0
   try:
      strlabel["foreground"] = color
   except:
      x = 0
   try:
      strcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      strvallabel["foreground"] = color
   except:
      x = 0
   try:
      strimglabel["foreground"] = color
   except:
      x = 0
   try:
      mentlabel["foreground"] = color
   except:
      x = 0
   try:
      mentcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      mentvallabel["foreground"] = color
   except:
      x = 0
   try:
      mentimglabel["foreground"] = color
   except:
      x = 0
   try:
      liblabel["foreground"] = color
   except:
      x = 0
   try:
      libcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      libvallabel["foreground"] = color
   except:
      x = 0
   try:
      libimglabel["foreground"] = color
   except:
      x = 0
   try:
      senlabel["foreground"] = color
   except:
      x = 0
   try:
      sencolonlabel["foreground"] = color
   except:
      x = 0
   try:
      senvallabel["foreground"] = color
   except:
      x = 0
   try:
      senimglabel["foreground"] = color
   except:
      x = 0
   try:
      label6["foreground"] = color
   except:
      x = 0
   try:
      hplabel["foreground"] = color
   except:
      x = 0
   try:
      hpcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      hpvallabel["foreground"] = color
   except:
      x = 0
   try:
      hpimglabel["foreground"] = color
   except:
      x = 0
   try:
      lustlabel["foreground"] = color
   except:
      x = 0
   try:
      lustcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      lustvallabel["foreground"] = color
   except:
      x = 0
   try:
      lustimglabel["foreground"] = color
   except:
      x = 0
   try:
      hungerlabel["foreground"] = color
   except:
      x = 0
   try:
      hungercolonlabel["foreground"] = color
   except:
      x = 0
   try:
      hungervallabel["foreground"] = color
   except:
      x = 0
   try:
      label10["foreground"] = color
   except:
      x = 0
   try:
      currentregionlabel["foreground"] = color
   except:
      x = 0
   try:
      levellabel["foreground"] = color
   except:
      x = 0
   try:
      levelcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      levelvallabel["foreground"] = color
   except:
      x = 0
   try:
      sexplabel["foreground"] = color
   except:
      x = 0
   try:
      sexpcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      sexpvallabel["foreground"] = color
   except:
      x = 0
   try:
      coinlabel["foreground"] = color
   except:
      x = 0
   try:
      coincolonlabel["foreground"] = color
   except:
      x = 0
   try:
      coinvallabel["foreground"] = color
   except:
      x = 0
   try:
      daylabel["foreground"] = color
   except:
      x = 0
   try:
      daycolonlabel["foreground"] = color
   except:
      x = 0
   try:
      dayvallabel["foreground"] = color
   except:
      x = 0
   try:
      hourlabel["foreground"] = color
   except:
      x = 0
   try:
      hourcolonlabel["foreground"] = color
   except:
      x = 0
   try:
      hourvallabel["foreground"] = color
   except:
      x = 0
   try:
      bagstashlabel["foreground"] = color
   except:
      x = 0
   try:
      savegamebutton["foreground"] = color
   except:
      x = 0
   try:
      loadgamebutton["foreground"] = color
   except:
      x = 0
   try:
      newgamebutton["foreground"] = color
   except:
      x = 0
   try:
      quitbutton["foreground"] = color
   except:
      x = 0
   try:
      resetbutton["foreground"] = color
   except:
      x = 0
   try:
      refreshbutton["foreground"] = color
   except:
      x = 0
   try:
      button1["foreground"] = color
   except:
      x = 0
   try:
      button2["foreground"] = color
   except:
      x = 0
   try:
      button3["foreground"] = color
   except:
      x = 0
   try:
      button4["foreground"] = color
   except:
      x = 0
   try:
      button5["foreground"] = color
   except:
      x = 0
   try:
      button6["foreground"] = color
   except:
      x = 0
   try:
      button7["foreground"] = color
   except:
      x = 0
   try:
      button8["foreground"] = color
   except:
      x = 0
   try:
      button9["foreground"] = color
   except:
      x = 0
   try:
      button10["foreground"] = color
   except:
      x = 0
   try:
      button11["foreground"] = color
   except:
      x = 0
   try:
      button12["foreground"] = color
   except:
      x = 0
   try:
      looksbutton["foreground"] = color
   except:
      x = 0
   try:
      statsbutton["foreground"] = color
   except:
      x = 0
   try:
      effectsbutton["foreground"] = color
   except:
      x = 0
   try:
      helpbutton["foreground"] = color
   except:
      x = 0
   try:
      levelsbutton["foreground"] = color
   except:
      x = 0
   try:
      gearbutton["foreground"] = color
   except:
      x = 0
   try:
      titlesbutton["foreground"] = color
   except:
      x = 0
   try:
      creditsbutton["foreground"] = color
   except:
      x = 0
   try:
      appearancebutton["foreground"] = color
   except:
      x = 0
   try:
      themebutton["foreground"] = color
   except:
      x = 0
   try:
      textsizedownbutton["foreground"] = color
   except:
      x = 0
   try:
      textsizeresetbutton["foreground"] = color
   except:
      x = 0
   try:
      textsizeupbutton["foreground"] = color
   except:
      x = 0
   try:
      textboldbutton["foreground"] = color
   except:
      x = 0
   try:
      textcolorbutton["foreground"] = color
   except:
      x = 0
   try:
      themebutton7["foreground"] = color
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
      a = ", 'bold'"
      return a
   else:
      return ""

def UpdateText():
   global fontMain, textMain, textSide
   a = UTCheckBold()
   #fontMain = "(" + "Times New Roman" + ", " + str(fontSize) + a + ")"
   fontMain = ("Times New Roman", fontSize, a)
   textmain.configure(state="normal")
   textside.configure(state="normal")
   textmain["font"] = fontMain
   textside["font"] = fontMain
   textmain.configure(state="disabled")
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
quitimg = tkinter.PhotoImage(file="./images/0.png")
resetimg = tkinter.PhotoImage(file="./images/0.1.png")
refreshimg = tkinter.PhotoImage(file="./images/0.2.png")
valupimg = tkinter.PhotoImage(file="./images/1.png")
valdownimg = tkinter.PhotoImage(file="./images/2.png")


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
textmain = ScrolledText(mainframe, cursor="arrow", wrap="word")
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
textside = ScrolledText(sidebar, cursor="arrow", wrap="word")
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

OutputMainText("Nimin: Fetish Fantasy" + "\n" + "    v" + versionNumber + "\n" + "\n" + "Click 'New Game' to begin a new game." + "\n" + "\n" + "Created by:    --Xadera" + "\n" + "    www.furaffinity.net/user/xadera/" + "\n" + "\n" + "Original concept by:     --Fenoxo" + "\n" + "    fenoxo.com" + "\n" + "\n" + "Currently maintained by:    ajdelguidice" + "\n" + "    github.com/ajdelguidice" + "\n" + "For tutorial/guide, questions, or bug reports, visit github.com/ajdelguidice/pymin/", True)
root.mainloop()