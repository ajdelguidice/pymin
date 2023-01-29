import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
tkScrolledText = tkinter.scrolledtext.ScrolledText
"""
to set text of ScrolledText, first use textmain.configure(state="normal")
to enable text input, then use <Name>.delete(0,"end") and <Name>.insert(0,<Text>)
to write text, finally use textmain.configure(state="disabled") to disable input
again.
"""

theme = 0
fontColor = "#000000"
fontSize = 12
fontBold = False

def FontSizeDown():
     global fontSize
     if fontSize > 4:
          fontSize -= 2
     UpdateText()
     #SavePreferences()

def FontSizeReset():
     global fontSize
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

def UTCheckBold():
    global fontBold
    if fontBold == True:
        a = 'bold'
        return a
    else:
        return ""

def UpdateText():
     global fontSize, fontBold, fontMain
     a = UTCheckBold()
     #fontMain = "(" + "Times New Roman" + ", " + str(fontSize) + a + ")"
     fontMain = ("Times New Roman", fontSize, a)
     textmain["font"] = fontMain
     textside["font"] = fontMain

def ToggleTheme():
     global theme
     theme += 1
     if theme == 6:
          theme = 0
     UpdateTheme()
     #SavePreferences()

def UpdateTheme():
     global theme
     if theme == 0:
          ChangeTKBColor("#FFFFFF")
     elif theme == 1:
          ChangeTKBColor("#000000")
     elif theme == 2:
          ChangeTKBColor("#EF7DB6")
     elif theme == 3:
          ChangeTKBColor("#29705C")
     elif theme == 4:
          ChangeTKBColor("#4248A6")
     elif theme == 5:
          ChangeTKBColor("#721717")
     else:
          ChangeTKBColor("#FFFFFF")
          theme = 0

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
     ChangeTKFColor(fontColor)
     #SavePreferences()

def ChangeTKBColor(color):
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
        textcolourbutton["background"] = color
    except:
        x = 0
    try:
        themebutton7["background"] = color
    except:
        x = 0


def ChangeTKFColor(color):
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
        textcolourbutton["foreground"] = color
    except:
        x = 0
    try:
        themebutton7["foreground"] = color
    except:
        x = 0

def imgchange():
    global _str_, ment, lib, sen, HP, lust
    if "?str2?" > "?str1?":
        strimglabel["image"] = valupimg
    elif "?str2?" < "?str1?":
        strimglabel["image"] = valdownimg
    else:
        strimglabel["image"] = ""

    if "?ment2?" > "?ment1?":
        mentimglabel["image"] = valupimg
    elif "?ment2?" < "?ment1?":
        mentimglabel["image"] = valdownimg
    else:
        mentimglabel["image"] = ""

    if "?lib2?" > "?lib1?":
        libimglabel["image"] = valupimg
    elif "?lib2?" < "?lib1?":
        libimglabel["image"] = valdownimg
    else:
        libimglabel["image"] = ""

    if "?sen2?" > "?sen1?":
        senimglabel["image"] = valupimg
    elif "?sen2?" < "?sen1?":
        senimglabel["image"] = valdownimg
    else:
        senimglabel["image"] = ""

    if "?hp2?" > "?hp1?":
        hpimglabel["image"] = valupimg
    elif "?hp2?" < "?hp1?":
        hpimglabel["image"] = valdownimg
    else:
        hpimglabel["image"] = ""

    if "?lust2?" > "?lust1?":
        lustimglabel["image"] = valupimg
    elif "?lust2?" < "?lust1?":
        lustimglabel["image"] = valdownimg
    else:
        lustimglabel["image"] = ""

def OutputMainText(text):
    textmain.configure(state="normal")
    textmain.delete(1.0,"end")
    textmain.insert(1.0, text)
    textmain.configure(state="disabled")

def OutputSideText(text):
    textside.configure(state="normal")
    textside.delete(1.0,"end")
    textside.insert(1.0, text)
    textside.configure(state="disabled")


#window
root = Tk()
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
quitimg = PhotoImage(file="./images/0.png")
resetimg = PhotoImage(file="./images/0.1.png")
refreshimg = PhotoImage(file="./images/0.2.png")
valupimg = PhotoImage(file="./images/1.png")
valdownimg = PhotoImage(file="./images/2.png")


#main
mainframe = ttk.Frame(root)
mainframe.place(anchor=NW, height=662, width=1176)
mainframe['padding'] = (20,30,0,0)

bccolorlabel1 = ttk.Label(mainframe)
bccolorlabel1.place(anchor=NW, height=662, width=1176, x=-20, y=-30)

#statframe
statframe = ttk.Frame(mainframe)
statframe.place(anchor=NW, height=611, width=180, x=0, y=0)

bccolorlabel2 = ttk.Label(statframe)
bccolorlabel2.place(anchor=NW, height=611, width=180)

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
loadgamebutton = tkinter.Button(statframe, text="Load Game")
loadgamebutton.place(anchor=N, height=30, width=100, x=90, y=515)
newgamebutton = tkinter.Button(statframe, text="New Game")
newgamebutton.place(anchor=N, height=30, width=100, x=90, y=550)

quitbutton = tkinter.Button(statframe, image=quitimg,command=root.destroy)
quitbutton.place(anchor=NW, height=20, width=20, x=0, y=591)
resetbutton = tkinter.Button(statframe, image=resetimg,command="reset()")
resetbutton.place(anchor=NW, height=20, width=20, x=25, y=591)
refreshbutton = tkinter.Button(statframe, image=refreshimg,command="refreshall()")
refreshbutton.place(anchor=NW, height=20, width=20, x=50, y=591)


buttonpanel = ttk.Frame(mainframe)
buttonpanel.place(anchor=NW, height=179, width=662, x=180, y=0)

bccolorlabel3 = ttk.Label(buttonpanel)
bccolorlabel3.place(anchor=NW, height=179, width=662)

button1 = tkinter.Button(buttonpanel, text="Button 1")
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
button12.place(anchor=NW, height=46, width=140, x=480, y=132)

amountlabel1 = ttk.Label(buttonpanel, text="000")
amountlabel1.place(anchor=NW, height=15, width=30, x=110, y=33)
amountlabel2 = ttk.Label(buttonpanel, text="000")
amountlabel2.place(anchor=NW, height=15, width=30, x=270, y=33)
amountlabel3 = ttk.Label(buttonpanel, text="000")
amountlabel3.place(anchor=NW, height=15, width=30, x=430, y=33)
amountlabel4 = ttk.Label(buttonpanel, text="000")
amountlabel4.place(anchor=NW, height=15, width=30, x=590, y=33)
amountlabel5 = ttk.Label(buttonpanel, text="000")
amountlabel5.place(anchor=NW, height=15, width=30, x=110, y=99)
amountlabel6 = ttk.Label(buttonpanel, text="000")
amountlabel6.place(anchor=NW, height=15, width=30, x=270, y=99)
amountlabel7 = ttk.Label(buttonpanel, text="000")
amountlabel7.place(anchor=NW, height=15, width=30, x=430, y=99)
amountlabel8 = ttk.Label(buttonpanel, text="000")
amountlabel8.place(anchor=NW, height=15, width=30, x=590, y=99)
amountlabel9 = ttk.Label(buttonpanel, text="000")
amountlabel9.place(anchor=NW, height=15, width=30, x=110, y=165)
amountlabel10 = ttk.Label(buttonpanel, text="000")
amountlabel10.place(anchor=NW, height=15, width=30, x=270, y=165)
amountlabel11 = ttk.Label(buttonpanel, text="000")
amountlabel11.place(anchor=NW, height=15, width=30, x=430, y=165)
amountlabel12 = ttk.Label(buttonpanel, text="000")
amountlabel12.place(anchor=NW, height=15, width=30, x=590, y=165)

#textmain
textmain = tkScrolledText(mainframe, cursor="arrow", wrap="word")
textmain.place(anchor=NW, height=430, width=622, x=180, y=180)
textmain.delete(1.0,"end")
textmain.insert(1.0, "yeet")
textmain.configure(state="disabled")


#frame
frame2 = ttk.Frame(mainframe)
frame2.place(anchor=NW, height=179, width=334, x=802, y=0)

bccolorlabel4 = ttk.Label(frame2)
bccolorlabel4.place(anchor=NW, height=179, width=334)

bagstashlabel = ttk.Label(frame2, text="BAG 1")
bagstashlabel.place(anchor=NW, height=30, width=80, x=20, y=0)
"""
moveitembutton = tkinter.Button(frame2, text="Move Item")
moveitembutton.place(anchor=CENTER, height=46, width=140, x=167, y=90)
"""

#sidebar
sidebar = ttk.Frame(mainframe)
sidebar.place(anchor=NW, height=432, width=334, x=803, y=180)

bccolorlabel5 = ttk.Label(sidebar)
bccolorlabel5.place(anchor=NW, height=432, width=334)

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

appearancebutton = tkinter.Button(sidebar, text="Appearance")
appearancebutton.place(anchor=CENTER, height=50, width=150, x=167, y=216)

themebutton = tkinter.Button(sidebar, text="Theme", command=ToggleTheme)
themebutton.place(anchor=NW, height=30, width=60, x=0, y=385)
textsizedownbutton = tkinter.Button(sidebar, text="A", command=FontSizeDown)
textsizedownbutton.place(anchor=NW, height=30, width=30, x=83, y=385)
textsizedownbutton["font"] = ("Times New Roman", 10)
textsizeresetbutton = tkinter.Button(sidebar, text="A", command=FontSizeReset)
textsizeresetbutton.place(anchor=NW, height=30, width=30, x=118, y=385)
textsizeresetbutton["font"] = ("Times New Roman", 12)
textsizeupbutton = tkinter.Button(sidebar, text="A", command=FontSizeUp)
textsizeupbutton.place(anchor=NW, height=30, width=30, x=153, y=385)
textsizeupbutton["font"] = ("Times New Roman", 14)
textboldbutton = tkinter.Button(sidebar, text="B", command=ToggleBold)
textboldbutton.place(anchor=NW, height=30, width=30, x=200, y=385)
textcolourbutton = tkinter.Button(sidebar, text="C", command=ToggleColor)
textcolourbutton.place(anchor=NW, height=30, width=30, x=245, y=385)
themebutton7 = tkinter.Button(sidebar, text="O")
themebutton7.place(anchor=NW, height=30, width=30, x=301, y=385)

appearancebutton.destroy()
ChangeTKBColor("#FFFFFF")
ChangeTKFColor("#000000")

UpdateText()
textmain.delete(1.0,"end")
textmain.insert(1.0, "'\033[1m', '\x1B[4m', test, '\x1B[0m', '\033[0m'")


root.mainloop()