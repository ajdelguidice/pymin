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
    bccolorlabel1["background"] = color
    bccolorlabel2["background"] = color
    bccolorlabel3["background"] = color
    bccolorlabel4["background"] = color
    bccolorlabel5["background"] = color
    textmain["background"] = color
    textside["background"] = color
    label1["background"] = color
    strlabel["background"] = color
    strcolonlabel["background"] = color
    strvallabel["background"] = color
    strimglabel["background"] = color
    mentlabel["background"] = color
    mentcolonlabel["background"] = color
    mentvallabel["background"] = color
    mentimglabel["background"] = color
    liblabel["background"] = color
    libcolonlabel["background"] = color
    libvallabel["background"] = color
    libimglabel["background"] = color
    senlabel["background"] = color
    sencolonlabel["background"] = color
    senvallabel["background"] = color
    senimglabel["background"] = color
    label6["background"] = color
    hplabel["background"] = color
    hpcolonlabel["background"] = color
    hpvallabel["background"] = color
    hpimglabel["background"] = color
    lustlabel["background"] = color
    lustcolonlabel["background"] = color
    lustvallabel["background"] = color
    lustimglabel["background"] = color
    hungerlabel["background"] = color
    hungercolonlabel["background"] = color
    hungervallabel["background"] = color
    label10["background"] = color
    currentregionlabel["background"] = color
    levellabel["background"] = color
    levelcolonlabel["background"] = color
    levelvallabel["background"] = color
    sexplabel["background"] = color
    sexpcolonlabel["background"] = color
    sexpvallabel["background"] = color
    coinlabel["background"] = color
    coincolonlabel["background"] = color
    coinvallabel["background"] = color
    daylabel["background"] = color
    daycolonlabel["background"] = color
    dayvallabel["background"] = color
    hourlabel["background"] = color
    hourcolonlabel["background"] = color
    hourvallabel["background"] = color
    bagstashlabel["background"] = color

    savegamebutton["background"] = color
    savegamebutton["background"] = color
    loadgamebutton["background"] = color
    newgamebutton["background"] = color
    quitbutton["background"] = color
    resetbutton["background"] = color
    refreshbutton["background"] = color
    button1["background"] = color
    button2["background"] = color
    button3["background"] = color
    button4["background"] = color
    button5["background"] = color
    button6["background"] = color
    button7["background"] = color
    button8["background"] = color
    button9["background"] = color
    button10["background"] = color
    button11["background"] = color
    button12["background"] = color
    looksbutton["background"] = color
    statsbutton["background"] = color
    effectsbutton["background"] = color
    helpbutton["background"] = color
    levelsbutton["background"] = color
    gearbutton["background"] = color
    titlesbutton["background"] = color
    creditsbutton["background"] = color
    appearancebutton["background"] = color
    themebutton["background"] = color
    textsizedownbutton["background"] = color
    textsizeresetbutton["background"] = color
    textsizeupbutton["background"] = color
    textboldbutton["background"] = color
    textcolourbutton["background"] = color
    themebutton7["background"] = color


def ChangeTKFColor(color):
    bccolorlabel1["foreground"] = color
    bccolorlabel2["foreground"] = color
    bccolorlabel3["foreground"] = color
    bccolorlabel4["foreground"] = color
    bccolorlabel5["foreground"] = color
    textmain["foreground"] = color
    textside["foreground"] = color
    label1["foreground"] = color
    strlabel["foreground"] = color
    strcolonlabel["foreground"] = color
    strvallabel["foreground"] = color
    strimglabel["foreground"] = color
    mentlabel["foreground"] = color
    mentcolonlabel["foreground"] = color
    mentvallabel["foreground"] = color
    mentimglabel["foreground"] = color
    liblabel["foreground"] = color
    libcolonlabel["foreground"] = color
    libvallabel["foreground"] = color
    libimglabel["foreground"] = color
    senlabel["foreground"] = color
    sencolonlabel["foreground"] = color
    senvallabel["foreground"] = color
    senimglabel["foreground"] = color
    label6["foreground"] = color
    hplabel["foreground"] = color
    hpcolonlabel["foreground"] = color
    hpvallabel["foreground"] = color
    hpimglabel["foreground"] = color
    lustlabel["foreground"] = color
    lustcolonlabel["foreground"] = color
    lustvallabel["foreground"] = color
    lustimglabel["foreground"] = color
    hungerlabel["foreground"] = color
    hungercolonlabel["foreground"] = color
    hungervallabel["foreground"] = color
    label10["foreground"] = color
    currentregionlabel["foreground"] = color
    levellabel["foreground"] = color
    levelcolonlabel["foreground"] = color
    levelvallabel["foreground"] = color
    sexplabel["foreground"] = color
    sexpcolonlabel["foreground"] = color
    sexpvallabel["foreground"] = color
    coinlabel["foreground"] = color
    coincolonlabel["foreground"] = color
    coinvallabel["foreground"] = color
    daylabel["foreground"] = color
    daycolonlabel["foreground"] = color
    dayvallabel["foreground"] = color
    hourlabel["foreground"] = color
    hourcolonlabel["foreground"] = color
    hourvallabel["foreground"] = color
    bagstashlabel["foreground"] = color

    savegamebutton["foreground"] = color
    savegamebutton["foreground"] = color
    loadgamebutton["foreground"] = color
    newgamebutton["foreground"] = color
    quitbutton["foreground"] = color
    resetbutton["foreground"] = color
    refreshbutton["foreground"] = color
    button1["foreground"] = color
    button2["foreground"] = color
    button3["foreground"] = color
    button4["foreground"] = color
    button5["foreground"] = color
    button6["foreground"] = color
    button7["foreground"] = color
    button8["foreground"] = color
    button9["foreground"] = color
    button10["foreground"] = color
    button11["foreground"] = color
    button12["foreground"] = color
    looksbutton["foreground"] = color
    statsbutton["foreground"] = color
    effectsbutton["foreground"] = color
    helpbutton["foreground"] = color
    levelsbutton["foreground"] = color
    gearbutton["foreground"] = color
    titlesbutton["foreground"] = color
    creditsbutton["foreground"] = color
    appearancebutton["foreground"] = color
    themebutton["foreground"] = color
    textsizedownbutton["foreground"] = color
    textsizeresetbutton["foreground"] = color
    textsizeupbutton["foreground"] = color
    textboldbutton["foreground"] = color
    textcolourbutton["foreground"] = color
    themebutton7["foreground"] = color

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
textsizedownbutton = tkinter.Button(sidebar, text="A")
textsizedownbutton.place(anchor=NW, height=30, width=30, x=83, y=385)
textsizedownbutton["font"] = ("Times New Roman", 10)
textsizeresetbutton = tkinter.Button(sidebar, text="A")
textsizeresetbutton.place(anchor=NW, height=30, width=30, x=118, y=385)
textsizeresetbutton["font"] = ("Times New Roman", 12)
textsizeupbutton = tkinter.Button(sidebar, text="A")
textsizeupbutton.place(anchor=NW, height=30, width=30, x=153, y=385)
textsizeupbutton["font"] = ("Times New Roman", 14)
textboldbutton = tkinter.Button(sidebar, text="B")
textboldbutton.place(anchor=NW, height=30, width=30, x=200, y=385)
textcolourbutton = tkinter.Button(sidebar, text="C", command=ToggleColor)
textcolourbutton.place(anchor=NW, height=30, width=30, x=245, y=385)
themebutton7 = tkinter.Button(sidebar, text="O")
themebutton7.place(anchor=NW, height=30, width=30, x=301, y=385)

ChangeTKBColor("#FFFFFF")
ChangeTKFColor("#000000")

root.mainloop()