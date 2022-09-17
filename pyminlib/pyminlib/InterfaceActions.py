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
        global button1
    def Show():
        button1 = tkinter.Button(buttonpanel, text="Button 1")
        button1.place(anchor=NW, height=46, width=140, x=0, y=0)
    def Hide():
        button1.destroy()
class PanelButton2:
    def __init__():
        global button2
    def Show():
        button2 = tkinter.Button(buttonpanel, text="Button 2")
        button2.place(anchor=NW, height=46, width=140, x=160, y=0)
    def Hide():
        button2.destroy()
class PanelButton3:
    def __init__():
        global button3
    def Show():
        button3 = tkinter.Button(buttonpanel, text="Button 3")
        button3.place(anchor=NW, height=46, width=140, x=320, y=0)
    def Hide():
        button3.destroy()
class PanelButton4:
    def __init__():
        global button4
    def Show():
        button4 = tkinter.Button(buttonpanel, text="Button 4")
        button4.place(anchor=NW, height=46, width=140, x=480, y=0)
    def Hide():
        button4.destroy()
class PanelButton5:
    def __init__():
        global button5
    def Show():
        button5 = tkinter.Button(buttonpanel, text="Button 5")
        button5.place(anchor=NW, height=46, width=140, x=0, y=66)
    def Hide():
        button5.destroy()
class PanelButton6:
    def __init__():
        global button6
    def Show():
        button6 = tkinter.Button(buttonpanel, text="Button 6")
        button6.place(anchor=NW, height=46, width=140, x=160, y=66)
    def Hide():
        button6.destroy()
class PanelButton7:
    def __init__():
        global button7
    def Show():
        button7 = tkinter.Button(buttonpanel, text="Button 7")
        button7.place(anchor=NW, height=46, width=140, x=320, y=66)
    def Hide():
        button7.destroy()
class PanelButton8:
    def __init__():
        global button8
    def Show():
        button8 = tkinter.Button(buttonpanel, text="Button 8")
        button8.place(anchor=NW, height=46, width=140, x=480, y=66)
    def Hide():
        button8.destroy()
class PanelButton9:
    def __init__():
        global button9
    def Show():
        button9 = tkinter.Button(buttonpanel, text="Button 9")
        button9.place(anchor=NW, height=46, width=140, x=0, y=132)
    def Hide():
        button9.destroy()
class PanelButton10:
    def __init__():
        global button10
    def Show():
        button10 = tkinter.Button(buttonpanel, text="Button 10")
        button10.place(anchor=NW, height=46, width=140, x=160, y=132)
    def Hide():
        button10.destroy()
class PanelButton11:
    def __init__():
        global button11
    def Show():
        button11 = tkinter.Button(buttonpanel, text="Button 11")
        button11.place(anchor=NW, height=46, width=140, x=320, y=132)
    def Hide():
        button11.destroy()
class PanelButton12:
    def __init__():
        global button12
    def Show():
        button12 = tkinter.Button(buttonpanel, text="Button 12")
        button12.place(anchor=NW, height=46, width=140, x=480, y=132)
    def Hide():
        button12.destroy()
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