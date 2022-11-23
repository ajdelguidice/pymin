import math
import random
import tkinter
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
#import pyminlib.InterfaceActions as PIA
import pyminlib.FunctionExtensions as FE
#import pyminlib.Items.MainItems as MainItems
#import pyminlib.Items.General as General
#import pyminlib.Items.Dye as DyeItems
#import pyminlib.Items.Appoticary as AppothItems
#import pyminlib.Items.Salon as SalonItems
from os.path import exists

#acheivements = list(())
#FindMalon, MalonRepMax, FindSil, SilRepMax, MistressRepMax, FindJamie, JamieRepMax, DefeatMinotaur, DefeatFreakyGirl, DefeatSuccubus, HaveAtleast25Aff5Races, HaveAffAllRaces, OneYear, Over9000Coins(Over9000 Joke), BugRaceFull, CowRaceFull, SkunkRaceFull, RabbitRaceFull, BirdRaceFull, PigRaceFull
fontMain = ("Times New Roman", 12) #Array
Option3 #TextField
Side2 #TextField
lustDown #downArrow
Amount1 #TextField
Amount11 #TextField
AmountOutline2 #MovieClip
Choice3 #TextField
Choice2Outline #MovieClip
Option4 #TextField
Side3 #TextField
scrollBar1 #UIScrollBar
Amount2 #TextField
Amount12 #TextField
AmountOutline1 #MovieClip
AmountOutline10 #MovieClip
Choice4 #TextField
Choice10 #TextField
Choice1Outline #MovieClip
Option5 #TextField
Side4 #TextField
scrollBar2 #UIScrollBar
strDown #downArrow
DayPane #TextField
Amount3 #TextField
AmountOutline11 #MovieClip
Choice5 #TextField
Choice11 #TextField
Option6 #TextField
Option4Outline #MovieClip
Side5 #TextField
Amount4 #TextField
AmountOutline12 #MovieClip
Choice12 #TextField
Choice6 #TextField
Choice7Outline #MovieClip
newGame #TextField
newGameOutline #MovieClip
Option7 #TextField
Option5Outline #MovieClip
Side6 #TextField
Side3Outline #MovieClip
senUp #upArrow
currentRegion #TextField
Amount5 #TextField
Choice7 #TextField
Choice6Outline #MovieClip
Option6Outline #MovieClip
Side7 #TextField
Side2Outline #MovieClip
statPane #TextField
Amount6 #TextField
Choice8 #TextField
Choice5Outline #MovieClip
loadGameOutline #MovieClip
Option7Outline #MovieClip
Side8 #TextField
Side1Outline #MovieClip
Amount7 #TextField
Choice9 #TextField
Choice4Outline #MovieClip
saveGameOutline #MovieClip
senDown #downArrow
Amount8 #TextField
loadGame #TextField
appearanceBox #MovieClip
Option1Outline #MovieClip
Side7Outline #MovieClip
region #TextField
moveItemAmount #TextField
Amount9 #TextField
Option2Outline #MovieClip
Side6Outline #MovieClip
lustUp #upArrow
levelPane #TextField
Option3Outline #MovieClip
Side5Outline #MovieClip
AmountOutline9 #MovieClip
Choice9Outline #MovieClip
pageNum #TextField
Side4Outline #MovieClip
hpUp #upArrow
libUp #upArrow
mentaUp #upArrow
AmountOutline8 #MovieClip
moveItem #TextField
Choice8Outline #MovieClip
AmountOutline7 #MovieClip
Choice12Outline #MovieClip
outputWindow #TextField
AmountOutline6 #MovieClip
Choice11Outline #MovieClip
sideWindow #TextField
hpDown #downArrow
libDown #downArrow
AmountOutline5 #MovieClip
MoveOutline #MovieClip
Choice10Outline #MovieClip
Option1 #TextField
AmountOutline4 #MovieClip
Choice1 #TextField
appearanceText #TextField
Option2 #TextField
Side1 #TextField
Side8Outline #MovieClip
strUp #upArrow
mentaDown #downArrow
Amount10 #TextField
MoveAmountOutline #MovieClip
AmountOutline3 #MovieClip
Choice2 #TextField
Choice3Outline #MovieClip
saveGame #TextField
doListen #Function
versionNumber #str
theme = 0 #int
fontSize = 12 #int
fontBold = False #bool
fontColor = "#000000" #str
showSide = True #bool
i = 0 #int
buttonChoice = 0 #int
currentText = "" #str
sideText = "" #str
sideFocus = 1 #int
pregTempInt = 0 #int
pregTempBool = False #bool
lustArray = list(()) #Array
loadFile #FileReference
fileLoader #URLLoader
bg #Sprite
rndResult = 0 #int
rndArray = list(()) #Array
textCheckArray = list(()) #Array
choiceListArray = list(()) #Array
choiceListResult = list(()) #Array
choicePage = 0 #int
moveItemID = 0 #int
moveItemStack = 0 #int
skipExhaustion = False #bool
shiftHeld = False #bool
currentState = 0 #int
inBag = False #bool
inShop = False #bool
currentZone = 0 #int
day = 0 #int
hour = 0 #int
inDungeon = False #bool
currentDungeon = 0 #int
_str_ = 0 #int
ment = 0 #int
lib = 0 #int
sen = 0 #int
HP = 0 #int
lust = 0 #int
coin = 0 #int
strMod = 0 #int
mentMod = 0 #int
libMod = 0 #int
senMod = 0 #int
strength = 0 #int
mentality = 0 #int
libido = 0 #int
sensitivity = 0 #int
hunger = 0 #int
hrs = 0 #int
itemGainArray = list(()) #Array
human = 0 #int
horse = 0 #int
wolf = 0 #int
cat = 0 #int
cow = 0 #int
lizard = 0 #int
rabbit = 0 #int
mouse = 0 #int
bird = 0 #int
pig = 0 #int
skunk = 0 #int
bug = 0 #int
SexP = 0 #int
levelUP = 0 #int
level = 0 #int
runMod = 0 #int
rapeMod = 0 #int
cumMod = 1 #Number
cockSizeMod = 1 #Number
vagSizeMod = 1 #Number
vagElastic = 1 #Number
milkMod = 0 #int
carryMod = 0 #int
vagBellyMod = 0 #int
pregChanceMod = 0 #int
extraPregChance = 0 #int
pregTimeMod = 0 #int
enticeMod = 0 #int
milkHPMod = 0 #int
changeMod = 1 #Number
HPMod = 0 #int
SexPMod = 0 #Number
minLust = 0 #int
milkCap = 0 #int
coinMod = 0 #int
hipMod = 1 #int
buttMod = 1 #int
bellyMod = 0 #int
cockMoistMod = 0 #int
vagMoistMod = 0 #int
lockTail = 0 #int
lockFace = 0 #int
lockSkin = 0 #int
lockBreasts = 0 #int
lockEars = 0 #int
lockLegs = 0 #int
lockNipples = 0 #int
lockCock = 0 #int
enemyID = 0 #int
eHP = 0 #int
eMaxHP = 0 #int
eStr = 0 #int
eMenta = 0 #int
eSen = 0 #int
eLib = 0 #int
eLust = 0 #int
eGen = 0 #int
ePref = 0 #int
eCoin = 0 #int
eSexP = 0 #int
eItem = 0 #int
gender = 0 #int
race = 0 #int
body = 0 #int
dominant = 0 #int
hips = 0 #int
butt = 0 #int
tallness = 0 #int
skinType = 0 #int
tail = 0 #int
ears = 0 #int
hair = 0 #int
hairLength = 0 #int
hairColor = 0 #int
legType = 0 #int
wings = 0 #int
faceType = 0 #int
skinColor = 0 #int
cockTotal = 0 #int
humanCocks = 0 #int
horseCocks = 0 #int
wolfCocks = 0 #int
catCocks = 0 #int
lizardCocks = 0 #int
rabbitCocks = 0 #int
cockSize = 0 #int
cockMoist = 0 #int
balls = 0 #int
ballSize = 0 #int
showBalls = True #bool
knot = False #bool
bugCocks = 0 #int
breastSize = 0 #int
boobTotal = 0 #int
nippleSize = 1 #int
udders = False #bool
udderSize = 0 #int
teatSize = 0 #int
clitSize = 0 #int
vagTotal = 0 #int
vagSize = 0 #int
vagMoist = 0 #int
vulvaSize = 0 #int
nipType = 0 #int
attireTop = 0 #int
attireBot = 0 #int
weapon = 10 #Number
pregArray = list(()) #Array
pregStatus = 0 #int
pregnancyTime = 0 #int
pregRate = 1 #Number
eggLaying = 0 #int
eggMaxTime = 0 #int
eggTime = 0 #int
eggRate = 0 #int
exhaustion = 0 #int
exhaustionPenalty = 0 #int
milkEngorgement = 0 #int
milkEngorgementLevel = 0 #int
udderEngorgement = 0 #int
udderEngorgementLevel = 0 #int
heat = 0 #int
heatTime = 0 #int
heatMaxTime = 0 #int
lactation = 0 #int
udderLactation = 0 #int
nipplePlay = 0 #Number
udderPlay = 0 #Number
blueBalls = 0 #int
teatPump = 0 #int
nipPump = 0 #int
cockPump = 0 #int
clitPump = 0 #int
vulvaPump = 0 #int
masoPot = 0 #int
sMasoPot = 0 #int
babyFree = 0 #int
charmTime = 0 #int
pheromone = 0 #int
eggceleratorTime = 0 #int
eggceleratorDose = 0 #int
bodyOil = 0 #int
lustPenalty = 0 #int
snuggleBall = False #bool
fertileGel = 0 #int
eggType = 0 #int
milkSuppressant = 0 #int
milkSuppressantLact = 0 #int
milkSuppressantUdder = 0 #int
suppHarness = False #bool
fertilityStatueCurse = 0 #int
plumpQuats = 0 #int
lilaWetStatus = 0 #int
cockSnakePreg = 0 #int
milkCPoisonNip = 0 #int
milkCPoisonUdd = 0 #int
cockSnakeVenom = 0 #int
humanAffinity = 0 #int
horseAffinity = 0 #int
wolfAffinity = 0 #int
catAffinity = 0 #int
cowAffinity = 0 #int
lizardAffinity = 0 #int
rabbitAffinity = 0 #int
fourBoobAffinity = 0 #int
mouseAffinity = 0 #int
birdAffinity = 0 #int
pigAffinity = 0 #int
twoBoobAffinity = 0 #int
sixBoobAffinity = 0 #int
eightBoobAffinity = 0 #int
tenBoobAffinity = 0 #int
cowTaurAffinity = 0 #int
humanTaurAffinity = 0 #int
skunkAffinity = 0 #int
bugAffinity = 0 #int
lilaRep = 0 #int
lilaVulva = 0 #int
lilaMilk = 0 #int
lilaPreg = -2 #int
malonRep = 0 #int
malonPreg = 0 #int
malonChildren = 0 #int
mistressRep = 0 #int
jamieRep = 0 #int
jamieSize = 4 #int
jamieChildren = 0 #int
silRep = 0 #int
silPreg = 0 #int
silRate = 0 #int
silLay = 10 #int
silTied = False #bool
silGrowthTime = 0 #int
lilaUB = False #bool
dairyFarmBrand = False #bool
jamieRep1 = 0 #int
jamieRep2 = 0 #int
jamieRep3 = 0 #int
lilaWetness = 0 #int
jamieButt = False #bool
jamieBreasts = False #bool
jamieHair = False #bool
travArray = list(())#Array
foundSoftlik = False #bool
foundFirmshaft = False #bool
foundTieden = False #bool
foundSizCalit = False #bool
foundOviasis = False #bool
foundValley = False #bool
foundSanctuary = False #bool
defeatedMinotaur = False #bool
defeatedFreakyGirl = False #bool
defeatedSuccubus = False #bool
firstExplore = False #bool
knowLustDraft = False #bool
knowRejuvPot = False #bool
knowExpPreg = False #bool
knowBallSwell = False #bool
knowMaleEnhance = False #bool
knowSLustDraft = False #bool
knowSRejuvPot = False #bool
knowSExpPreg = False #bool
knowSBallSwell = False #bool
knowBabyFree = False #bool
knowPotPot = False #bool
knowGenSwap = False #bool
knowMasoPot = False #bool
knowMilkSuppress = False #bool
knowSGenSwap = False #bool
knowSMasoPot = False #bool
knowSBabyFree = False #bool
knowSPotPot = False #bool
knowPussJuice = False #bool
knowPheromone = False #bool
knowBazoomba = False #bool
babyFactLevel = 0 #int
bodyBuildLevel = 0 #int
hyperHappyLevel = 0 #int
alchemistLevel = 0 #int
fetishMasterLevel = 0 #int
milkMaidLevel = 0 #int
shapeshiftyLevel = 0 #int
shapeshiftyFirst = "" #str
shapeshiftySecond = "" #str
maleFetish = 1 #Number
femaleFetish = 1 #Number
hermFetish = 1 #Number
narcissistFetish = 1 #Number
dependentFetish = 1 #Number
dominantFetish = 1 #Number
submissiveFetish = 1 #Number
lboobFetish = 1 #Number
sboobFetish = 1 #Number
furryFetish = 1 #Number
scalyFetish = 1 #Number
smoothyFetish = 1 #Number
pregnancyFetish = 1 #Number
bestialityFetish = 1 #Number
milkFetish = 1 #Number
sizeFetish = 1 #Number
unbirthingFetish = 1 #Number
ovipositionFetish = 1 #Number
toyFetish = 1 #Number
hyperFetish = 1 #Number
currentDayCare = 0 #int
humanChildren = 0 #int
equanChildren = 0 #int
lupanChildren = 0 #int
felinChildren = 0 #int
cowChildren = 0 #int
lizanEggs = 0 #int
lizanChildren = 0 #int
bunnionChildren = 0 #int
wolfPupChildren = 0 #int
miceChildren = 0 #int
birdEggs = 0 #int
birdChildren = 0 #int
pigChildren = 0 #int
calfChildren = 0 #int
bugEggs = 0 #int
bugChildren = 0 #int
skunkChildren = 0 #int
minotaurChildren = 0 #int
freakyGirlChildren = 0 #int
bagPage = 1 #int
bagArray = list(()) #Array
bagStackArray = list(()) #Array
stashArray = list(()) #Array
stashStackArray = list(()) #Array
button1visible = False
button2visible = False
button3visible = False
button4visible = False
button5visible = False
button6visible = False
button7visible = False
button8visible = False
button9visible = False
button10visible = False
button11visible = False
button12visible = False

#def MainTimeline():
#   super()
#   addFrameScript(0,this.frame1)
#   __setProp_scrollBar2_Scene1_TextFields_0()
#   __setProp_scrollBar1_Scene1_TextFields_0()

def ButtonEvent1():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(1)
   else:
      buttonChoice = 1
      UpDown.HideAll()

def ButtonEvent2():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(2)
   else:
      buttonChoice = 2
      UpDown.HideAll()

def ButtonEvent3():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(3)
   else:
      buttonChoice = 3
      UpDown.HideAll()

def ButtonEvent4():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      x = 0
   else:
      buttonChoice = 4
      UpDown.HideAll()

def ButtonEvent5():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(5)
   else:
      buttonChoice = 5
      UpDown.HideAll()

def ButtonEvent6():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(6)
   else:
      buttonChoice = 6
      UpDown.HideAll()

def ButtonEvent7():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(7)
   else:
      buttonChoice = 7
      UpDown.HideAll()

def ButtonEvent8():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      x = 0
   else:
      buttonChoice = 8
      UpDown.HideAll()

def ButtonEvent9():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(9)
   else:
      buttonChoice = 9
      UpDown.HideAll()

def ButtonEvent10():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(10)
   else:
      buttonChoice = 10
      UpDown.HideAll()

def ButtonEvent11():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      ItemMove(11)
   else:
      buttonChoice = 11
      UpDown.HideAll()

def ButtonEvent12():
   global shiftHeld, inBag, buttonChoice
   if (shiftHeld == True) and (inBag == True):
      x = 0
   else:
      buttonChoice = 12
      UpDown.HideAll()

def Side1Event():
   SideEvent(1)

def Side2Event():
   SideEvent(2)

def Side3Event():
   SideEvent(3)

def Side4Event():
   SideEvent(4)

def Side5Event():
   SideEvent(5)

def Side6Event():
   SideEvent(6)

def Side7Event():
   SideEvent(7)

def Side8Event():
   SideEvent(8)

def SideEvent(which:int):
   global sideFocus
   sideFocus = which
   if which == 1:
      AppearanceGo()
   if which == 2:
      DetailedStats()
   if which == 3:
      DetailedStatuses()
   if which == 4:
      DetailedHelp()
   if which == 5:
      DetailedLevels()
   if which == 6:
      DetailedGear()
   if which == 7:
      DetailedTitles()
   if which == 8:
      DetailedCredits()

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

"""
def KeysUp():      {
         if(!e.shiftKey)
         {
            this.shiftHeld = False
         }
      }
"""
"""
def HotKeys():
     if shiftHeld == False
          if((e.keyCode == 103 || e.keyCode == 81) && this.Choice1.visible == True)
               this.buttonChoice = 1;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 104 || e.keyCode == 87) && this.Choice2.visible == True)
               this.buttonChoice = 2;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 105 || e.keyCode == 69) && this.Choice3.visible == True)
               this.buttonChoice = 3;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 109 || e.keyCode == 82) && this.Choice4.visible == True)
               this.buttonChoice = 4;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 100 || e.keyCode == 65) && this.Choice5.visible == True)
            {
               this.buttonChoice = 5;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 101 || e.keyCode == 83) && this.Choice6.visible == True)
            {
               this.buttonChoice = 6;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 102 || e.keyCode == 68) && this.Choice7.visible == True)
            {
               this.buttonChoice = 7;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 107 || e.keyCode == 70) && this.Choice8.visible == True)
            {
               this.buttonChoice = 8;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 97 || e.keyCode == 90) && this.Choice9.visible == True)
            {
               this.buttonChoice = 9;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 98 || e.keyCode == 88) && this.Choice10.visible == True)
            {
               this.buttonChoice = 10;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 99 || e.keyCode == 67) && this.Choice11.visible == True)
            {
               this.buttonChoice = 11;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 13 || e.keyCode == 86) && this.Choice12.visible == True)
            {
               this.buttonChoice = 12;
               this.hideUpDown();
               this.doListen();
            }
         }
         if(e.keyCode == 85 && this.showSide == True)
         {
            this.sideEvent(1);
         }
         else if(e.keyCode == 85 && this.showSide == False && this.appearanceText.visible == True)
         {
            this.appearanceGo();
         }
         if(e.keyCode == 73 && this.showSide == True)
         {
            this.sideEvent(2);
         }
         if(e.keyCode == 79 && this.showSide == True)
         {
            this.sideEvent(3);
         }
         if(e.keyCode == 80 && this.showSide == True)
         {
            this.sideEvent(4);
         }
         if(e.keyCode == 72 && this.showSide == True)
         {
            this.sideEvent(5);
         }
         if(e.keyCode == 74 && this.showSide == True)
         {
            this.sideEvent(6);
         }
         if(e.keyCode == 75 && this.showSide == True)
         {
            this.sideEvent(7);
         }
         if(e.keyCode == 76 && this.showSide == True)
         {
            this.sideEvent(8);
         }
         if(e.keyCode == 37)
         {
            this.toggleTheme();
         }
         if(e.keyCode == 38)
         {
            this.fontSizeUp();
         }
         if(e.keyCode == 39)
         {
            this.toggleColor();
         }
         if(e.keyCode == 40)
         {
            this.fontSizeDown();
         }
         if(e.keyCode == 17)
         {
            this.fontSizeReset();
         }
         if(e.keyCode == 190 && this.Option7.visible == True)
         {
            this.toggleSide();
         }
         if(e.keyCode == 191)
         {
            this.toggleBold();
         }
         if(e.keyCode == 113 && this.saveGame.visible == True)
         {
            this.saveGo();
         }
         if(e.keyCode == 115 && this.loadGame.visible == True)
         {
            this.loadGo();
         }
         if(e.keyCode == 8 && this.newGame.visible == True)
         {
            this.newGameGo();
         }
         if(e.shiftKey)
         {
            this.shiftHeld = True
         }
         if(this.inBag == True)
         {
            if(this.shiftHeld)
            {
               if((e.keyCode == 103 || e.keyCode == 81) && this.Choice1.visible == True)
               {
                  this.itemMove(1);
               }
               if((e.keyCode == 104 || e.keyCode == 87) && this.Choice2.visible == True)
               {
                  this.itemMove(2);
               }
               if((e.keyCode == 105 || e.keyCode == 69) && this.Choice3.visible == True)
               {
                  this.itemMove(3);
               }
               if((e.keyCode == 100 || e.keyCode == 65) && this.Choice5.visible == True)
               {
                  this.itemMove(5);
               }
               if((e.keyCode == 101 || e.keyCode == 83) && this.Choice6.visible == True)
               {
                  this.itemMove(6);
               }
               if((e.keyCode == 102 || e.keyCode == 68) && this.Choice7.visible == True)
               {
                  this.itemMove(7);
               }
               if((e.keyCode == 97 || e.keyCode == 90) && this.Choice9.visible == True)
               {
                  this.itemMove(9);
               }
               if((e.keyCode == 98 || e.keyCode == 88) && this.Choice10.visible == True)
               {
                  this.itemMove(10);
               }
               if((e.keyCode == 99 || e.keyCode == 67) && this.Choice11.visible == True)
               {
                  this.itemMove(11);
               }
            }
         }
      }
"""

def Appearance():
   AppearanceGo()

def SaveG():
   SaveGo()

def LoadG():
   LoadGo()

def NewGameStart():
   NewGameGo()

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
      textcolourbutton["foreground"] = color
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

"""
def SideHide():
   this.sideWindow.visible = False
      this.scrollBar2.visible = False
      this.Side1.visible = False
      this.Side1Outline.visible = False
      this.Side2.visible = False
      this.Side2Outline.visible = False
      this.Side3.visible = False
      this.Side3Outline.visible = False
      this.Side4.visible = False
      this.Side4Outline.visible = False
      this.Side5.visible = False
      this.Side5Outline.visible = False
      this.Side6.visible = False
      this.Side6Outline.visible = False
      this.Side7.visible = False
      this.Side7Outline.visible = False
      this.Side8.visible = False
      this.Side8Outline.visible = False
      if(this.saveGame.visible == True)
      {
         this.appearanceText.visible = True
         this.appearanceBox.visible = True
      }
def SideShow():
   this.sideWindow.visible = True
      this.scrollBar2.visible = True
      this.Side1.visible = True
      this.Side1Outline.visible = True
      this.Side2.visible = True
      this.Side2Outline.visible = True
      this.Side3.visible = True
      this.Side3Outline.visible = True
      this.Side4.visible = True
      this.Side4Outline.visible = True
      this.Side5.visible = True
      this.Side5Outline.visible = True
      this.Side6.visible = True
      this.Side6Outline.visible = True
      this.Side7.visible = True
      this.Side7Outline.visible = True
      this.Side8.visible = True
      this.Side8Outline.visible = True
      this.appearanceText.visible = False
      this.appearanceBox.visible = False
      this.updateSide();
"""

!def SavePreferences():
   global theme, fontSize, fontBold, fontColor, showSide
   if exists("pyminprefs.txt") == True:
      f = open("pyminprefs.txt", "w")
      prefSave = list(())
      prefSave[0] = theme
      prefSave[1] = fontSize
      prefSave[2] = fontBold
      prefSave[3] = fontColor
      prefSave[4] = showSide
      f.write(prefSave)
      f.close()
   
!def LoadPreferences():
   global theme, fontSize, fontBold, fontColor, showSide
   if exists("pyminprefs.txt") == True:
      f = open("pyminprefs.txt", "r")
      pref = f.read()
      theme = prefLoad[0]
      fontSize = prefLoad[1]
      fontBold = prefLoad[2]
      fontColor = prefLoad[3]
      showSide = prefLoad[4]
      UpdateText()
      ChangeBackgroundColor(theme)
      ChangeTextColor(fontColor)
      f.close()
   else:
      theme = 0
      fontSize = 14
      fontBold = false
      fontColor = "#000000"
      showSide = True
      UpdateText()
      ChangeBackgroundColor(theme)
      ChangeTextColor(fontColor)

!def OutputMainText(texts:str, reset:bool):
   if reset == False:
        TextBoxes.AddMain(texts)
   if reset == True:
        TextBoxes.ClearAddMain(texts)

"""
   global textCheckArray
   if reset == False:
        if (textCheckArray.indexOf(textCheck[0]) == -1)
           currentText += texts
           textCheckArray = textCheckArray.concat(textCheck)
   else:
        currentText = texts
        textCheckArray = list(())
   tempStr = currentText
   if fontBold == True:
        tempStr = "<b>" + tempStr + "</b>"
   #tempStr = "<font size = \'" + this.fontSize + "\' color = \'#" + this.fontColor + "\'>" + tempStr + "</font>";
   this.outputWindow.htmlText = tempStr
   this.outputWindow.scrollV = 0
   this.scrollBar1.update()
"""
!def OutputSideText(texts:str, reset:bool):
   if reset == False:
        TextBoxes.AddSide(texts)
   if reset == True:
        TextBoxes.ClearAddSide(texts)

"""
   if reset == False:
        sideText += texts
   else:
        sideText = texts
   tempStr = sideText
   if(this.fontBold == True)
        tempStr = "<b>" + tempStr + "</b>";
   tempStr = "<font size = \'" + this.fontSize + "\' color = \'#" + this.fontColor + "\'>" + tempStr + "</font>";
   this.sideWindow.htmlText = tempStr;
   this.sideWindow.scrollV = 0;
   this.scrollBar2.update();
"""
def UpdateSide():
   global sideFocus
   if sideFocus == 1:
      AppearanceGo()
   if sideFocus == 2:
      DetailedStats()
   if sideFocus == 3:
      DetailedStatuses()
   if sideFocus == 5:
      DetailedLevels()
   if sideFocus == 6:
      DetailedGear()
   if sideFocus == 7:
      DetailedTitles()
   if sideFocus == 8:
      DetailedCredits()
"""
def HideUpDown():
   this.strUp.visible = False
   this.strDown.visible = False
   this.mentaUp.visible = False
   this.mentaDown.visible = False
   this.libUp.visible = False
   this.libDown.visible = False
   this.senDown.visible = False
   this.senUp.visible = False
   this.lustUp.visible = False
   this.lustDown.visible = False
   this.hpUp.visible = False
   this.hpDown.visible = False
"""
"""
def ButtonWrite(buttonNumber:int, buttonText:str):
   if buttonNumber == 1:
      this.Choice1.htmlText = buttonText
   if buttonNumber == 2:
      this.Choice2.htmlText = buttonText
   if buttonNumber == 3:
      this.Choice3.htmlText = buttonText
   if buttonNumber == 4:
      this.Choice4.htmlText = buttonText
   if buttonNumber == 5:
      this.Choice5.htmlText = buttonText
   if buttonNumber == 6:
      this.Choice6.htmlText = buttonText
   if buttonNumber == 7:
      this.Choice7.htmlText = buttonText
   if buttonNumber == 8:
      this.Choice8.htmlText = buttonText
   if buttonNumber == 9:
      this.Choice9.htmlText = buttonText
   if buttonNumber == 10:
      this.Choice10.htmlText = buttonText
   if buttonNumber == 11:
      this.Choice11.htmlText = buttonText
   if buttonNumber == 12:
      this.Choice12.htmlText = buttonText
"""
!def ViewButtonText():
!def ViewButtonOutline():
!def AmountWrite():
!def ViewAmount():
!def HideAmount():
!def ChoiceListButtons():
!def ChoiceListBlanks():
!def ChoiceListSelect():
!def ChoiceListCheck():
!def ShowPage():
def CheckZero():
   global bagArray, bagStackArray, stashArray, stashStackArray, cockSize, cockTotal, ball, blueBalls, ballSize, cockMoist, breastSize, boobTotal, nippleSize, udderSize, teatSize, clitSize, vagSize, vagTotal, vagMoist, vulvaSize, exhaustion, exhaustionPenalty, hips, butt, body, tallness, cockSizeMod, vagSizeMod, vagBellyMod, pregChance, lactation, MilkMod, MilkCap, coin, hipMod, buttMod, bellyMod, pregArray
   for i in range(0, 26):
      if bagStackArray[i] == 0:
         bagArray[i] = ""
         bagStackArray[i] = ""
   for i in range(0, 26):
      if stashStackArray[i] == 0:
         stashArray[i] = ""
         stashStackArray[i] = ""
   if cockSize < 0:
      cockSize = 0
   if cockTotal < 0:
      cockTotal = 0
   if balls < 0:
      balls = 0
   if balls == 0 & blueBalls > 0:
      blueBalls = 0
   if ballSize < 1:
      ballSize = 1
   if cockMoist < 0:
      cockMoist = 0
   if cockMoist > 12:
      cockMoist = 12
   if breastSize < 0:
      breastSize = 0
   if boobTotal < 0:
      boobTotal = 0
   if nippleSize < 1:
      nippleSize = 1
   if udderSize < 1:
      udderSize = 1
   if teatSize < 2:
      teatSize = 2
   if clitSize < 1:
      clitSize = 1
   if vagSize < 0:
      vagsize = 0
   if vagTotal < 0:
      vagTotal = 0
   if vagMoist < 0:
      vagMoist = 0
   if vagMoist > 12:
      vagMoist = 12
   if vulvaSize < 0:
      vulvaSize = 0
   if exhaustion < 0:
      exhaustion = 0
   if exhaustionPenalty < 0:
      exhaustionPenalty = 0
   if hips < 1:
      hips = 1
   if butt < 1:
      butt = 1
   if body < 5:
      body = 5
   if tallness < 3:
      tallness = 3
   if cockSizeMod < 0.1:
      cockSizeMod = 0.1
   if vagSizeMod < 0.1:
      vagSizeMod = 0.1
   if vagBellyMod < 0:
      vagBellyMod = 0
   if pregChanceMod < -100:
      pregChanceMod = -100
   if lactation < 0:
      lactation = 0
   if milkMod < 0:
      milkMod = 0
   if milkCap < 0:
      milkCap = 0
   if coin < 0:
      coin = 0
   if hipMod < 1:
      hipMod = 1
   if buttMod < 1:
      buttMod = 1
   if bellyMod < 0:
      bellyMod = 0
   if len(pregArray) < vagTotal * 5:
      while len(pregArray) < vagTotal * 5:
         pregArray.push(False,0,0,0,0)

def CheckDecimal():
   cumMod = round(cumMod * 10) / 10
   cockSizeMod = round(cockSizeMod * 100) / 100
   vagSizeMod = round(vagSizeMod * 100) / 100
   vagElastic = round(vagElastic * 10) / 10
   changeMod = round(changeMod * 10) / 10
   SexPMod = round(SexPMod * 10) / 10
   pregRate = round(pregRate * 100) / 100
   maleFetish = round(maleFetish * 10) / 10
   femaleFetish = round(femaleFetish * 10) / 10
   hermFetish = round(hermFetish * 10) / 10
   narcissistFetish = round(narcissistFetish * 10) / 10
   dependentFetish = round(dependentFetish * 10) / 10
   dominantFetish = round(dominantFetish * 10) / 10
   submissiveFetish = round(submissiveFetish * 10) / 10
   lboobFetish = round(lboobFetish * 10) / 10
   sboobFetish = round(sboobFetish * 10) / 10
   furryFetish = round(furryFetish * 10) / 10
   scalyFetish = round(scalyFetish * 10) / 10
   smoothyFetish = round(smoothyFetish * 10) / 10
   pregnancyFetish = round(pregnancyFetish * 10) / 10
   bestialityFetish = round(bestialityFetish * 10) / 10
   milkFetish = round(milkFetish * 10) / 10
   sizeFetish = round(sizeFetish * 10) / 10
   unbirthingFetish = round(unbirthingFetish * 10) / 10
   ovipositionFetish = round(ovipositionFetish * 10) / 10
   toyFetish = round(toyFetish * 10) / 10
   hyperFetish = round(hyperFetish * 10) / 10

def BC():
   global buttonChoice
   buttonChoice = 0

def ButtonConfirm():
   BC()
   ButtonFunctions.Visible(0,0,0,0,0,1,1,0,0,0,0,0)
   ButtonFunctions.WriteText(6,"Yes")
   ButtonFunctions.WriteText(7,"No")
   while (buttonChoice != 6) and (buttonChoice != 7):
      sleep()

def DoNext():
   global buttonChoice
   BC()
   ButtonFunctions.Visible(0,0,0,0,0,1,0,0,0,0,0,0)
   ButtonFunctions.WriteText(6,"Next")
   while buttonChoice != 6:
      sleep()

def DoEnd():
   global choicePage, inBag, lust, currentState, buttonChoice
   choicePage = 1
   ShowPage(False,"")
   StatDisplay()
   if inBag == True and lust > 99 and currentState == 2:
      inBag = False
      HideAmount()
      DoLustForcedMasturbate()
   else:
      DoNext()
      if buttonChoice == 6:
         DoProcess()

def DoButtonChoices(buttonlist:list):
   global buttonChoice
   BC()
   templist = list(())
   while i < (len(buttonlist) / 2):
      ButtonFunctions.WriteText(buttonlist[(2 * i) - 1], buttonlist[2 * i])
      templist.append(buttonlist[(2 * i) - 1])
      i += 1
   while any(buttonChoices == a for a in templist) == False:
      sleep()

def DoProcess():
   global choicePage, moveItemID, moveItemStack, itemGainArray, human, horse, wolf, cat, cow, hrs
   choicePage = 1
   if inBag == False and moveItemID != 0:
      OutputMainText("You seem to have not placed your " + ItemName(moveItemID) + "",True)
      if moveItemStack > 1:
         OutputMainText(" x" + moveItemStack,False)
      OutputMainText(" in your bag. Do you want to discard the item?",False)
      ButtonConfirm()
      if buttonChoice == 6:
         PassiveItemRemove(moveItemID)
      else:
         for i in range(0, 26):
            if i <= moveItemStack: 
               ItemAdd(moveItemID)
         moveItemID = 0
         moveItemStack = 0
         ShowMoveItem(False)
      if len(itemGainArray) != 0:
         itemGainArray.sort()
         GainItem(itemGainArray.pop())
      elif human != 0 or horse != 0 or wolf != 0 or cat != 0 or cow != 0:
         AffinityChange()
      elif hrs != 0:
         DayTime(hrs)
      else:
         DoReturn()

def DoReturn():
   global choicePage, showSide, inBag, inShop, currentState, inDungeon
   choicePage = 1
   CheckZero()
   CheckDecimal()
   if showSide == True:
      UpdateSide()
   if inBag == False:
      ShowPage(False,"")
      HideAmount()
   if inBag == True:
      DoBag()
   elif inShop == True:
      DoShop()
   elif currentState == 2:
      DoBattle()
   elif currentState == 3:
      DoMasturbate()
   elif inDungeon == True:
      DoDungeon()
   elif currentState == 1:
      DoGeneral()

def MoistCalc(which:int):
   tempNum = 0
   if which == 1:
      tempNum = cockMoist + cockMoistMod
   if which == 2:
      tempNum = vagMoist + vagMoistMod
   if b < 0:
      tempNum = 0
   if lust >= 75:
      tempNum = math.ceil(tempNum * 1.5)
   elif lust >= 50:
      tempNum = math.ceil(tempNum * 1)
   elif lust >= 25:
      tempNum = math.ceil(tempNum * 0.75)
   else:
      tempNum = math.ceil(tempNum * 0.25)
   return tempNum

def VagLimit():
   global vagSize, vagSizeMod, vagElastic
   a = vagSize * (vagSizeMod + vagElastic) + vagSize * vagSizeMod * MoistCalc(2) / 10
   return a

def eVagLimit(limit:int):
   a = limit + limit * MoistCalc(1) / 10
   return a

!def DecGet(number, places:int):
   tempStr = str(number)
   tempStr2 = ""
   tempInt = 0
   tempInt = tempStr.index(".", 0)
   if tempInt > 0:
      tempStr2 = tempStr[0: tempInt + places + 1]
   else:
      tempStr2 = tempStr
   return tempStr2

!def DoWeight():
   global cockSize, cockSizeMod, body, _str_, carryMod, tallness, breastSize, boobTotal, ballSize, showBalls, udderSize, udders, pregnancyTime, bellyMod
   tempBool = False
   if (cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60)):
      OutputMainText("\n" + "\n" + "The weight of your " + CockDesc() + " cock" + Plural(1) + " is too much to carry, making it impossible to walk. You're stuck in this town until either you get stronger or the bulge in your " + ClothesBottom() + " gets smaller...",False)
      tempBool = True
   elif (cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6):
      OutputMainText("\n" + "\n" + "The weight of your " + CockDesc() + " cock" + Plural(1) + " is almost constantly on your mind... Your walk has a noticeable sway in its step just trying to hold it off the ground while you move. You're cautious when moving, or else you will lose control and slam it into something or someone.",False)
   elif (cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3):
      OutputMainText("\n" + "\n" + "The weight of your " + CockDesc() + " cock" + Plural(1) + " is becoming a bit of a nuisance. Whenever you move around, you're subconsciously afraid your bulge will accidentally gain more momentum than intended and potentially hurt someone or break something.",False)
   elif (cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2):
      OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + CockDesc() + " cock" + Plural(1) + ". You often find yourself slipping a hand into your " + ClothesBottom() + " to readjust your bulge in an attempt to be a little less mindful about it.",False)
   if (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60))) or ((boobTotal == 4) and (breastSize > (0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60)))) or ((boobTotal == 6) and (breastSize > (0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60)))) or ((boobTotal == 8) and (breastSize > (0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60)))) or ((boobTotal == 10) and (breastSize > (0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60)))):
      OutputMainText("\n" + "\n" + "The weight of your " + BoobDesc() + " tits is too much to really carry, making even standing a chore. You're stuck in this town until either you get stronger or they get smaller...",False)
      tempBool = True
   elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6)) or ((boobTotal == 4) and (breastSize > (0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6))) or ((boobTotal == 6) and (breastSize > (0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6))) or ((boobTotal == 8) and (breastSize > (0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6))) or ((boobTotal == 10) and (breastSize > (0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6))):
      OutputMainText("\n" + "\n" + "The weight of your " + BoobDesc() + " tits is rather troubling. Not only does your back ache from trying to keep them aloft, but you're also afraid you won't be able to get back up when you lay down.",False)
   elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3)) or ((boobTotal == 4) and (breastSize > (0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3))) or ((boobTotal == 6) and (breastSize > (0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3))) or ((boobTotal == 8) and (breastSize > (0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3))) or ((boobTotal == 10) and (breastSize > (0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3))):
      OutputMainText("\n" + "\n" + "The weight of your " + BoobDesc() + " tits is becoming worrisome. Your back aches a little from holding them up and you often find yourself resting them on tables whenever you sit down, to keep the load off yourself.",False)
   elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2)) or ((boobTotal == 4) and (breastSize > (0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2))) or ((boobTotal == 6) and (breastSize > (0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2))) or ((boobTotal == 8) and (breastSize > (0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2))) or ((boobTotal == 10) and (breastSize > (0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2))):
      OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + BoobDesc() + " tits. Your hands are frequently beneath your " + ClothesTop() + ", trying to readjust the things. They\'re so heavy, you're subconsciouly drawing more attention to them with the way you keep swinging them around and absent-mindedly handling them.",False)
   if (ballSize * balls / 2) > ((body * 2 + _str_ + carryMod) * (tallness / 60)) and (showBalls == True):
      OutputMainText("\n" + "\n" + "The weight of your " + BallDesc() + " nuts is too much to carry, anchoring you to the ground. You're stuck here until you get strong or your balls get smaller...",False)
      tempBool = True
   elif (ballSize * balls / 2) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6) and (showBalls == True):
      OutputMainText("\n" + "\n" + "The weight of your " + BallDesc() + " nuts is troublesome. Your " + LegDesc(6) + " bend" + LegPlural(1) + " with the heaviness and you have difficulty standing up whenever you sit down. And you're afraid of running because once those things start swaying, they\'re quite difficult to stop.",False)
   elif (ballSize * balls / 2) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3) and (showBalls == True):
      OutputMainText("\n" + "\n" + "The weight of your " + BallDesc() + " nuts is becoming annoying. You're walking with your crotch sagging quite often and frequently consider buying a bra for them...",False)
   elif (ballSize * balls / 2) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2) and (showBalls == True):
      OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + BallDesc() + " nuts. Even in public, a hand is dipping into your " + ClothesBottom() + " to readjust them and massaging your stretched scrotum is quickly becoming a hobby of yours.",False)
   if (udderSize > ((body * 2 + _str_ + carryMod) * (tallness / 60))) and (udders == True):
      OutputMainText("\n" + "\n" + "The weight of your " + UdderDesc() + " udder is too much to carry, sitting heavily in front of you. You're stuck in this town until either you get stronger or it gets smaller...",False)
      tempBool = True
   elif (udderSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6)) and (udders == True):
      OutputMainText("\n" + "\n" + "The weight of your " + UdderDesc() + " udder makes you uneasy. The momentum it gains when you walk makes you fear falling on your face and every now and then your " + LegDesc(2) + " go numb while you're sitting or laying down.",False)
   elif (udderSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3)) and (udders == True):
      OutputMainText("\n" + "\n" + "The weight of your " + UdderDesc() + " udder is becoming an inconvenience. Whenever you turn from side to side, it lifts off slightly and acts like a fleshy wrecking ball that you're unable to stop.",False)
   elif (udderSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2)) and (udders == True):
      OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + UdderDesc() + " udder. You often find yourself fondling it in an attempt to make it settle more appropriately, wondering if they make bras for this sort of thing...",False)
   if ((pregnancyTime + bellyMod * 2) / 5) > ((body * 2 + _str_ + carryMod) * (tallness / 60)):
      OutputMainText("\n" + "\n" + "The weight of your " + BellyDesc() + " belly is too much carry, putting your weight more on it than you can yourself. You're stuck in this town until either you get stronger or you lose some of the girth...",False)
      tempBool = True
   elif ((pregnancyTime + bellyMod * 2) / 5) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6):
      OutputMainText("\n" + "\n" + "The weight of your " + BellyDesc() + " belly is rather alarming... You're almost constantly trying to cradle it, subconsciously fearing it will drag you down to the ground if you don't. Whenever you sit down, you always prop it up against a table simply so you don't roll forward.",False)
   elif ((pregnancyTime + bellyMod * 2) / 5) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3):
      OutputMainText("\n" + "\n" + "The weight of your " + BellyDesc() + " belly is becoming irksome. You take a bit more time to come to a halt whenever you move as it retains much of your momentum. And whenever you bend over, it's difficult to rise back up.",False)
   elif ((pregnancyTime + bellyMod * 2) / 5) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2):
      OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + BellyDesc() + " belly. You often subconsciously center your weight more by resting your hands on top of it rather than let them hang at your sides.",False)
   return tempBool

!def CheckItem(ID:int):
   global bagArray
   tempBool = False
   if (bagArray.index(ID) != -1):
      tempBool = True
   return tempBool

def CheckMagicItem():
   tempBool = False
   if (CheckItem(101) == True):
      tempBool = True
   elif (CheckItem(102) == True):
      tempBool = True
   elif (CheckItem(200) == True):
      tempBool = True
   elif (CheckItem(215) == True):
      tempBool = True
   elif (CheckItem(231) == True):
      tempBool = True
   elif (CheckItem(233) == True):
      tempBool = True
   elif (CheckItem(234) == True):
      tempBool = True
   elif (CheckItem(235) == True):
      tempBool = True
   elif (CheckItem(236) == True):
      tempBool = True
   elif (CheckItem(237) == True):
      tempBool = True
   elif (CheckItem(252) == True):
      tempBool = True
   return tempBool

!def CheckStash():
   global stashArray
   tempBool = False
   if (stashArray.index(ID) != -1):
      tempBool = True
   return tempBool

!def CountItem():
   global bagArray, bagStackArray
   tempInt = 0
   for i in range(0,26):
      if(bagArray[i] == ID):
         tempInt += bagStackArray[i]
   return tempInt
    
def Percent():
   a = math.floor(random.random() * (1 + 100 - 1)) + 1
   return a

def ChooseFrom():
   global rndArray, hour
   tempInt = 0
   rndResult = 0
   if len(rndArray) < 1:
      OutputMainText("\n" + "\n" + "An ERROR has occured in the choice array. Please report this bug and where you saw it (" + rndArray[0] + " at " + hour + "hour), or else you'll get the hose.",False)
      rndArray = list(())
   else:
      tempInt = round(random.random() * (len(rndArray) - 1))
      rndResult = rndArray[tempInt]
      rndArray = list(())
   return rndResult

!def Stats(stre:int, menta:int, libi:int, sens:int):
   global strength, mentality, libido, sensitivity, lust
   PIA.UpDown.HideAll()
   strength += stre
   mentality += menta
   libido += libi
   sensitivity += sens
   if strength > 1000:
      strength = 1000
   if strength < 1:
      strength = 1
   if mentality > 1000:
      mentality = 1000
   if mentality < 1:
      mentality = 1
   if libido > 1000:
      libido = 1000
   if libido < 1:
      libido = 1
   if sensitivity > 1000:
      sensitivity = 1000
   if sensitivity < 1:
      sensitivity = 1
   if lust > 100:
      lust = 100
   if lust < 0:
      lust = 0
   if stre > 0:
      UpDown.StrImg("./images/1.png")
   if stre < 0:
      UpDown.StrImg("./images/2.png")
   if menta > 0:
      UpDown.MentImg("./images/1.png")
   if menta < 0:
      UpDown.MentImg("./images/2.png")
   if libi > 0:
      UpDown.LibImg("./images/1.png")
   if libi < 0:
      UpDown.LibImg("./images/2.png")
   if sens > 0:
      UpDown.SenImg("./images/1.png")
   if sens < 0:
      UpDown.SenImg("./images/2.png")
   StatDisplay()

!def StatsMod(stre:int, menta:int, libi:int, sens:int):
   global strMod, mentMod, libMod, senMod
   PIA.UpDown.HideAll()
   strMod += stre
   mentMod += menta
   libMod += libi
   senMod += sens
   if stre > 0:
      PIA.UpDown.StrImg("./images/1.png")
   if stre < 0:
      PIA.UpDown.StrImg("./images/2.png")
   if menta > 0:
      PIA.UpDown.MentImg("./images/1.png")
   if menta < 0:
      PIA.UpDown.MentImg("./images/2.png")
   if libi > 0:
      PIA.UpDown.LibImg("./images/1.png")
   if libi < 0:
      PIA.UpDown.LibImg("./images/2.png")
   if sens > 0:
      PIA.UpDown.SenImg("./images/1.png")
   if sens < 0:
      PIA.UpDown.SenImg("./images/2.png")
   StatDisplay()

!def StatsDisplay():
   _str_ = strength + strMod
   ment = mentality + mentMod
   lib = libido + libMod
   sen = sensitivity + senMod
   PIA.StatPane.SetCStats()

!def DoSexP(changes:int):
   global SexP, SexPMod, level, levelUP
   if (SexP + changes * SexPMod) >= 100:
      changes -= math.ceil((100 - SexP) / SexPMod)
      SexP = 0
      level += 1
      levelUP += 1
      DoSexP(changes)
   else:
      SexP += changes * SexPMod
      PIA.StatPane.SetSCStats()

!def RegionChange(changes:int):
   if (inDungeon == False):
      currentZone = changes
      if (changes == 1):
         region.text = "Softlik"
      if (changes == 2):
         region.text = "Firmshaft"
      if (changes == 3):
         region.text = "Tieden"
      if (changes == 4):
         region.text = "Siz'Calit"
      if (changes == 6):
         region.text = "Oviasis"
      if (changes == 12):
         region.text = "Sanctuary"
   if (inDungeon == True):
      currentDungeon = changes
      if (changes > 1000) and (changes < 1010):
         region.text = "Cave Descent"

!def DayTime(Time):
   global hour, day
   addTime = Time
   while ((hour + addTime) >= 24):
      addTime -= 24 - hour
      hour = 0
      day += 1
   hour += addTime
   PIA.StatPane.SetDHStats()
   DoStatus(Time)

def DoCoin(changes:int):
   global coin, coinMod
   if ((coin + changes) < 0):
      coin = 0
      changes = 0
   if (changes > 0):
      changes += coinMod
   coin += changes
   DoSexP(0)

!def DoHP(changes:int):
   global masoPot, sMasoPot, lust, HP, _str_, HPMod
   if (masoPot > 0) and (sMasoPot <= 0) and (changes < 0):
      DoLust(math.floor(-changes / 2),0)
      changes -= math.ceil(changes / 2)
   if (sMasoPot > 0) and (lust < 100) and (changes < 0):
      DoLust(-changes,0)
      changes = 0
   if (sMasoPot > 0) and (lust >= 100) and (changes < 0):
      OutputMainText("\n" + "\n" + "It seems that no matter how much fun you had getting beaten like that, there's just some things your body wasn't meant to withstand.",False)
   if changes < 0:
      PIA.UpDown.hpImg["image"] = "./images/2.png"
   if changes > 0:
      PIA.UpDown.hpImg["image"] = "./images/1.png"
   if (HP + changes) <= 0:
      HP = 1
      changes = 0
      DoPassOut()
   if (HP + changes) > (30 + math.floor(_str_ / 2) + HPMod):
      HP = 30 + math.floor(_str_ / 2) + HPMod
   else:
      HP += changes
   PIA.StatPane.SetHPStat()
   StatDisplay()

!def DoPassOut():
   global level, coin, currentState, inDungeon, exhaustion, skipExhaustion, hrs
   tempNum = math.floor(Percent() / 10 * level + level * Percent() / 10)
   if (coin - tempNum) < 0:
      tempNum = coin
   SpecialKOLose()
   OutputMainText("\n" + "\n" + "You pass out from all the pain. When you wake back up, you manage to stumble back to town. However, it seems as though your pockets are a bit lighter for some reason or another." + "\n" + "\n" + "You have lost " + tempNum + " coins.",False)
   if currentState == 2:
      currentState = 1
   if inDungeon == True:
      inDungeon = False
   DoCoin(-tempNum)
   exhaustion -= math.floor(Percent() / 20)
   skipExhaustion = True
   hrs = 2 + math.floor(Percent() / 20)
   DoEnd()

!def DoLust(changes:int, source:int, triggers):
   global ment, fertilityStatueCurse, cockSnakeVenom, cockTotal, vagTotal, clitSize, milkCPoisonNip, nipplePlay, milkCPoisonUdd, level, lust, _str_, nipType, inBag, minLust, heat, heatTime
   if source == 1:
      if changes > 0:
         changes -= math.floor(changes * ment / 125)
         if changes < 0:
            changes = 0
   if source == 2:
      if changes <= 0:
         changes += math.floor(changes * ment / 125)
   if (changes <= 0) and (source == 2):
      changes -= 6
      if fertilityStatueCurse > 0:
         OutputMainText("\n" + "\n" + "With your orgasm, you feel strange as wispy fumes escape from your crotch, just like those that descended from the statue you encountered...",False)
         VagChange(0,1)
      if (cockSnakeVenom > 0) and (triggers.index(1) != -1) and (cockTotal > 0):
         OutputMainText("\n" + "\n" + "However, after you have finished, you realize there's a bit more meat to your meat... The venom from the cock-snake fed off of your orgasm, causing your appendage" + Plural(1) + " to flop a bit lower down your " + LegDesc(3) + " as " + Plural(11) + " shrink" + Plural(3) + " back down...",False)
         CockChange(2,0)
      if (cockSnakeVenom > 0) and (triggers.indexOf(2) != -1) and (vagTotal > 0):
         OutputMainText("\n" + "\n" + "However, after you have finished, you realize your clit" + Plural(2) + " " + Plural(14) + " a bit more prominent... The venom from the cock-snake fed off of your orgasm, causing the button" + Plural(2) + " swell larger than before, and aren't shrinking all the way back down...",False)
         clitSize += 3
      if (milkCPoisonNip > 0) and (triggers.indexOf(3) != -1):
         OutputMainText("\n" + "\n" + "However, now that you've calmed down, you notice a bit more weight at your chest... The warmth from the milk creeper poison in your bosom intensified with your pleasure, causing your flesh to grow larger while you were distracted by the climax. A hefty reminder.",False)
         BoobChange(1)
         nipplePlay += 15
      if (milkCPoisonUdd > 0) and (triggers.indexOf(4) != -1):
         OutputMainText("\n" + "\n" + "However, now that you've calmed down, you notice a bit more weight at your belly... The warmth from the milk creeper poison in your udder intensified with your pleasure, causing your flesh to grow larger while you were distracted by the climax. A hefty reminder.",False)
         BoobChange(1)
         nipplePlay += 15
      if level < 50:
         if ((lust + changes) >= 0) and (-changes > (level + 6 + _str_ / 3)):
            DoSexP(math.floor(-changes - (level + 6 + _str_ / 3)))
         elif ((lust + changes) < 0) and (lust > (level + 6 + _str_ / 3)):
            DoSexP(math.floor(lust - (level + 6 + _str_ / 3)))
      elif ((lust + changes) >= 0) and (-changes > (50 + 6 + _str_ / 3)):
         DoSexP(math.floor(-changes - (50 + 6 + _str_ / 3)))
      elif((lust + changes) < 0) and (lust > (50 + 6 + _str_ / 3)):
         DoSexP(math.floor(lust - (50 + 6 + _str_ / 3)))
   if changes < 0:
      PIA.UpDown.LustImg("./images/2.png")
   if changes > 0:
      PIA.UpDown.LustImg("./images/1.png")
   if ((lust + changes) >= 75) and (lust < 75):
      if cockTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + CockDesc() + " cock" + Plural(1) + " squirm" + Plural(3) + " in your " + ClothesBottom() + ", throbbing and wanting desperately to come.",False)
         if (MoistCalc(1) > 0) and (MoistCalc(1) <= 3):
            OutputMainText(" A small amount of pre leaks out, making a moist blotch on your " + ClothesBottom() + ".",False)
         if (MoistCalc(1) > 3) and (MoistCalc(1) <= 7):
            OutputMainText(" Steady drops of pre leak out, blotching your " + ClothesBottom() + " with small patches of slime.",False)
         if (MoistCalc(1) > 7) and (MoistCalc(1) <= 11):
            OutputMainText(" You feel your cock" + Plural(1) + " slimed from tip to belly with " + Plural(5) + " own pre, a steady dribble down your thigh and your " + ClothesBottom() + " looking more like you peed yourself.",False)
         if (MoistCalc(1) > 11):
            OutputMainText(" You feel your cock" + Plural(1) + " swimming in " + Plural(5) + " own pre, as long strands of slime seep through your " + ClothesBottom() + " and stretch down to the ground. With each step, you fling the stuff around you like a whip, smacking across whatever is nearby",False)
      if vagTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + VulvaDesc() + " lips feel swollen and hot in your " + ClothesBottom() + ", making your " + LegDesc(2) + " feel weak. Your " + ClitDesc() + " clit" + Plural(2) + " seem" + Plural(4) + " on the verge of exploding without any attention soon, stiffly rubbing against your " + ClothesBottom() + " with each move.",False)
         if (MoistCalc(2) > 0) and (MoistCalc(2) <= 3):
            OutputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",False)
         if (MoistCalc(2) > 3) and (MoistCalc(2) <= 7):
            OutputMainText(" You can feel webs of slime smear across the inside of your " + ClothesBottom() + ", your honey dribbling lightly within.",False)
         if (MoistCalc(2) > 7) and (MoistCalc(2) <= 11):
            OutputMainText(" You swear you can hear yourself squish with each step as your " + ClothesBottom() + " is completely soaked through with your honey. Your thighs feel like they've been completely oiled down by the warm, sensuous fluid.",False)
         if MoistCalc(2) > 11:
            OutputMainText(" There must be a waterfall in your " + ClothesBottom() + " as a steady flow of clear honey drools from " + LegWhere(1) + " your " + LegDesc(2) + ". You have to be extra careful of slipping in your own slime...",False)
      OutputMainText("\n" + "\n" + "Your " + NipDesc() + "nipples threaten to pierce through your " + ClothesTop() + ". They feel as hard as diamonds with all your arousal, making you shiver whenever something brushes them.",False)
   elif ((lust + changes) >= 50) and (lust < 50):
      if cockTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + CockDesc() + " cock" + Plural(1) + " feel" + Plural(3) + " stiff and engorged with blood. Oh how nice it would be to take care of that problem... ",False)
         if (MoistCalc(1) > 0) and (MoistCalc(1) <= 3):
            OutputMainText(" A small amount of pre leaks out, making a moist blotch on your " + ClothesBottom() + ".",False)
         if (MoistCalc(1) > 3) and (MoistCalc(1) <= 7):
            OutputMainText(" Steady drops of pre leak out, blotching your " + ClothesBottom() + " with small patches of slime.",False)
         if MoistCalc(1) > 7:
            OutputMainText(" You feel your cock" + Plural(1) + " slimed from tip to belly with its own pre, a steady dribble down your thigh and your " + ClothesBottom() + " looking more like you peed yourself.",False)
      if vagTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + VulvaDesc() + " vulva feels puffy with engorgement, making you walk a little awkwardly so as to not squeeze them so much. Your " + ClitDesc() + " clit" + Plural(2) + " stir" + Plural(4) + " in your " + ClothesBottom() + ", throbbing gently in anticipation.",False)
         if (MoistCalc(2) > 0) and (MoistCalc(2) <= 3):
            OutputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",False)
         if (MoistCalc(2) > 3) and (MoistCalc(2) <= 7):
            OutputMainText(" You can feel webs of slime smear across the inside of your " + ClothesBottom() + ", your honey dribbling lightly within.",False)
         if MoistCalc(2) > 7:
            OutputMainText(" You swear you can hear yourself squish with each step as your " + ClothesBottom() + " is completely soaked through with your honey. Your thighs feel like they've been completely oiled down by the warm, sensuous fluid.",False)
      if nipType == 2:
         OutputMainText("\n" + "\n" + "Your sunken nipples rise out of your " + BoobDesc() + " mounds, standing to attention in your " + ClothesTop() + ". They tingle slightly with your arousal.",False)
      else:
         OutputMainText("\n" + "\n" + "Your " + NipDesc() + "nipples stand at attention in your " + ClothesTop() + ". They tingle slightly with your arousal.",False)
   elif ((lust + changes) >= 25) and (lust < 25):
      if cockTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + CockDesc() + " cock" + Plural(1) + " wiggle" + Plural(3) + " in your " + ClothesBottom() + ", stirring awake and growing erect. Bulging against the fabric, you silently wonder if anybody else will notice...",False)
         if (MoistCalc(1) > 0) and (MoistCalc(1) <= 3):
            OutputMainText(" A small amount of pre leaks out, making a moist blotch on your " + ClothesBottom() + ".",False)
         if MoistCalc(1) > 3:
            OutputMainText(" Steady drops of pre leak out, blotching your " + ClothesBottom() + " with small patches of slime.",False)
      if vagTotal > 0:
         OutputMainText("\n" + "\n" + "Your " + VulvaDesc() + " slit tingles and sparks. You feel a little giggly and warm with the sensation, delighting in the pleasantness of it all. Your " + ClitDesc() + " clit" + Plural(2) + " tug" + Plural(4) + " at the hood" + Plural(4) + ", pulsing awake in your " + ClothesBottom() + ".",False)
         if (MoistCalc(2) > 0) and (MoistCalc(2) <= 3):
            OutputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",False)
         if MoistCalc(2) > 3:
            OutputMainText(" You can feel webs of slime smear across the inside of your " + ClothesBottom() + ", your honey dribbling lightly within.",False)
   if ((lust + changes) >= 30) and (lustPenalty == 0):
      OutputMainText("\n" + "\n" + "The distraction weighs on your mind constantly, making it hard to focus on normal tasks.",False)
      StatsMod(0,-4,0,0)
      lustPenalty = 1
   if ((lust + changes) >= 60) and (lustPenalty == 1):
      OutputMainText("\n" + "\n" + "Your muscles are twitchy and feeling weak from the strong tingle of arousal.",False)
      StatsMod(-5,0,0,0)
      lustPenalty = 2
   if ((lust + changes) >= 90) and (lustPenalty == 2):
      OutputMainText("\n" + "\n" + "The intense lust has overwhelmed your body, leaving your " + SkinDesc() + " hypersensitive.",False)
      StatsMod(0,0,0,10)
      lustPenalty = 3
   if ((lust + changes) >= 100):
      lust = 100
      changes = 0
      if inBag == False:
         DoLustForcedMasturbate()
   if ((lust + changes) < (minLust + 20)) and (heat > 0) and (heatTime < 0) and (PregCheck(0) != True):
      lust = minLust + 20
      changes = 0
   elif (lust + changes) < minLust:
      lust = minLust
      changes = 0
   lust += changes
   StatDisplay()

!def DoLustForcedMasturbate():
   global currentState, ePref, gender, button6
   if currentState == 2:
      OutputMainText("\n" + "\n" + "Amidst the heat of battle, your " + LegDesc(2) + " buckle" + LegPlural(1) + " from your intense arousal, preventing you from fighting any further.",False)
      if inBag == False:
         currentState = 1
      #DoNext()
      #BC()
      #ViewButtonOutline(0,0,0,0,0,1,0,0,0,0,0,0)
      #ViewButtonText(0,0,0,0,0,1,0,0,0,0,0,0)
      #ButtonWrite(6,"Next")
      PIA.PanelButton1.Hide()
      PIA.PanelButton2.Hide()
      PIA.PanelButton3.Hide()
      PIA.PanelButton4.Hide()
      PIA.PanelButton5.Hide()
      PIA.PanelButton7.Hide()
      PIA.PanelButton8.Hide()
      PIA.PanelButton9.Hide()
      PIA.PanelButton10.Hide()
      PIA.PanelButton11.Hide()
      PIA.PanelButton12.Hide()
      button6["text"] = "Next"
      button6["command"] = "DoLustForcedMasturbatePt2"

!def DoLustForcedMasturbatePt2():
   global ePref, gender
   if ((ePref == 0) or ((ePref == 1) and (gender == 2)) or ((ePref == 2) and (gender == 1)) or (gender == 0)):
      OutputMainText("Unfortunately, the " + EnemyName() + " has no interest in taking advantage of your state and lands a heavy blow, knocking you out.",True)
      DoHP(-100000)
   else:
      DoGetRaped()

!def NewGameGo():
   global button6, button7, currentState
   appearanceText.visible = False
   appearanceBox.visible = False
   SGButton.Hide()
#   saveGameOutline.visible = False
   if (currentState == 0):
      this.Choice7.visible = False
   OutputMainText("Are you sure you would like to start a new game?", True)
   ButtonConfirm()
   #BC()
   #ViewButtonText(0,0,0,0,0,1,1,0,0,0,0,0)
   #ViewButtonOutline(0,0,0,0,0,1,1,0,0,0,0,0)
   #ButtonWrite(6,"Yes")
   #ButtonWrite(7,"No")
   PanelButton1.Hide()
   PanelButton2.Hide()
   PanelButton3.Hide()
   PanelButton4.Hide()
   PanelButton5.Hide()
   PanelButton8.Hide()
   PanelButton9.Hide()
   PanelButton10.Hide()
   PanelButton11.Hide()
   PanelButton12.Hide()
   button6["text"] = "Yes"
   button6["command"] = "NewGameGoPt2"
   button7["text"] = "No"
   button7["command"] = "DoReturn"

!def NewGameGoPt2():
   global currentState, currentZone,
   UpDown.HideAll()
   statPane.visible = True
   DayPane.visible = True
   levelPane.visible = True
   Option7.visible = False
   SideHide()
   currentState = 0
   currentZone = 0
   inBag = False
   inShop = False
   inDungeon = False
   currentDungeon = 0
   _str_ = 0
   ment = 0
   lib = 0
   sen = 0
   HP = 0
   lust = 0
   coin = 0
   strMod = 0
   mentMod = 0
   libMod = 0
   senMod = 0
   hunger = 0
   day = 0
   hour = 8
   SexP = 0
   levelUP = 0
   level = 0
   runMod = 0
   rapeMod = 0
   cumMod = 1
   cockSizeMod = 1
   vagSizeMod = 1
   vagElastic = 1
   milkMod = 0
   carryMod = 0
   vagBellyMod = 0
   pregChanceMod = 0
   extraPregChance = 0
   pregTimeMod = 0
   enticeMod = 0
   milkHPMod = 0
   changeMod = 1
   HPMod = 0
   SexPMod = 1
   minLust = 0
   milkCap = 0
   coinMod = 0
   hipMod = 1
   buttMod = 1
   bellyMod = 0
   cockMoistMod = 0
   vagMoistMod = 0
   lockTail = 0
   lockFace = 0
   lockSkin = 0
   lockBreasts = 0
   lockEars = 0
   lockLegs = 0
   lockNipples = 0
   lockCock = 0
   gender = 0
   race = 0
   body = 0
   dominant = 0
   hips = 0
   butt = 0
   tallness = 0
   skinType = 0
   tail = 0
   ears = 0
   hair = 0
   hairLength = 0
   hairColor = 0
   legType = 0
   wings = 0
   faceType = 0
   skinColor = 0
   cockTotal = 0
   humanCocks = 0
   horseCocks = 0
   wolfCocks = 0
   catCocks = 0
   lizardCocks = 0
   rabbitCocks = 0
   cockSize = 0
   cockMoist = 0
   balls = 0
   ballSize = 0
   showBalls = True
   knot = False
   bugCocks = 0
   breastSize = 0
   boobTotal = 0
   nippleSize = 1
   udders = False
   udderSize = 0
   teatSize = 0
   clitSize = 0
   vagTotal = 0
   vagSize = 0
   vagMoist = 0
   vulvaSize = 0
   nipType = 0
   attireTop = 1
   attireBot = 2
   weapon = 10
   pregArray = list(())
   pregStatus = 0
   pregnancyTime = 0
   pregRate = 1
   eggLaying = 0
   eggMaxTime = 0
   eggTime = 0
   eggRate = 0
   exhaustion = 0
   exhaustionPenalty = 0
   milkEngorgement = 0
   milkEngorgementLevel = 0
   udderEngorgement = 0
   udderEngorgementLevel = 0
   heat = 0
   heatTime = 0
   heatMaxTime = 0
   lactation = 0
   udderLactation = 0
   nipplePlay = 0
   udderPlay = 0
   blueBalls = 0
   teatPump = 0
   nipPump = 0
   cockPump = 0
   clitPump = 0
   vulvaPump = 0
   masoPot = 0
   sMasoPot = 0
   babyFree = 0
   charmTime = 0
   pheromone = 0
   eggceleratorTime = 0
   eggceleratorDose = 0
   bodyOil = 0
   lustPenalty = 0
   snuggleBall = False
   fertileGel = 0
   eggType = 0
   milkSuppressant = 0
   milkSuppressantLact = 0
   milkSuppressantUdder = 0
   suppHarness = False
   fertilityStatueCurse = 0
   plumpQuats = 0
   lilaWetStatus = 0
   cockSnakePreg = 0
   milkCPoisonNip = 0
   milkCPoisonUdd = 0
   cockSnakeVenom = 0
   humanAffinity = 0
   horseAffinity = 0
   wolfAffinity = 0
   catAffinity = 0
   cowAffinity = 0
   lizardAffinity = 0
   rabbitAffinity = 0
   fourBoobAffinity = 0
   mouseAffinity = 0
   birdAffinity = 0
   pigAffinity = 0
   twoBoobAffinity = 0
   sixBoobAffinity = 0
   eightBoobAffinity = 0
   tenBoobAffinity = 0
   cowTaurAffinity = 0
   humanTaurAffinity = 0
   skunkAffinity = 0
   bugAffinity = 0
   lilaRep = 0
   lilaVulva = 0
   lilaMilk = 0
   lilaPreg = -2
   malonRep = 0
   malonPreg = 0
   malonChildren = 0
   mistressRep = 0
   jamieRep = 0
   jamieSize = 4
   jamieChildren = 0
   silRep = 0
   silPreg = 0
   silRate = 0
   silLay = 10
   silTied = False
   silGrowthTime = 0
   lilaUB = False
   dairyFarmBrand = False
   jamieRep1 = 0
   jamieRep2 = 0
   jamieRep3 = 0
   lilaWetness = 0
   foundSoftlik = False
   foundFirmshaft = False
   foundTieden = False
   foundSizCalit = False
   foundOviasis = False
   foundValley = False
   foundSanctuary = False
   defeatedMinotaur = False
   defeatedFreakyGirl = False
   defeatedSuccubus = False
   firstExplore = False
   knowLustDraft = False
   knowRejuvPot = False
   knowExpPreg = False
   knowBallSwell = False
   knowMaleEnhance = False
   knowSLustDraft = False
   knowSRejuvPot = False
   knowSExpPreg = False
   knowSBallSwell = False
   knowGenSwap = False
   knowMasoPot = False
   knowBabyFree = False
   knowPotPot = False
   knowMilkSuppress = False
   knowSGenSwap = False
   knowSMasoPot = False
   knowSBabyFree = False
   knowSPotPot = False
   knowPussJuice = False
   knowPheromone = False
   knowBazoomba = False
   babyFactLevel = 0
   bodyBuildLevel = 0
   hyperHappyLevel = 0
   alchemistLevel = 0
   fetishMasterLevel = 0
   milkMaidLevel = 0
   shapeshiftyLevel = 0
   shapeshiftyFirst = ""
   shapeshiftySecond = ""
   maleFetish = 1
   femaleFetish = 1
   hermFetish = 1
   narcissistFetish = 1
   dependentFetish = 1
   dominantFetish = 1
   submissiveFetish = 1
   lboobFetish = 1
   sboobFetish = 1
   furryFetish = 1
   scalyFetish = 1
   smoothyFetish = 1
   pregnancyFetish = 1
   bestialityFetish = 1
   milkFetish = 1
   sizeFetish = 1
   unbirthingFetish = 1
   ovipositionFetish = 1
   toyFetish = 1
   hyperFetish = 1
   currentDayCare = 0
   humanChildren = 0
   equanChildren = 0
   lupanChildren = 0
   felinChildren = 0
   cowChildren = 0
   lizanEggs = 0
   lizanChildren = 0
   bunnionChildren = 0
   miceChildren = 0
   birdEggs = 0
   birdChildren = 0
   pigChildren = 0
   bugEggs = 0
   bugChildren = 0
   skunkChildren = 0
   minotaurChildren = 0
   freakyGirlChildren = 0
   wolfPupChildren = 0
   calfChildren = 0
   bagPage = 1
   bagArray = list(())
   bagStackArray = list(())
   BagSlotAdd(27)
   stashArray = list(())
   stashStackArray = list(())
   StashSlotAdd(27)
   DoRace()

!def AppearanceGo():
   global tallness, hair, tail, skunkAffinity, skinType, dominant, legType, attireTop, attireBot, snuggleBall, weapon, lilaWetStatus, pregnancyTime, vagBellyMod, bellyMod, wings, dairyFarmBrand, breastSize, boobTotal, lust, nipType, lactation, milkEngourgement, milkEngourgementLevel, milkSuppressantLact, udders, udderEngourgement, udderEngourgementLevel, cowAffinity, teatSize, udderLactation, cockTotal, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, bugCocks, rabbitCocks, cockSize, cockSizeMod, showBalls, balls, ballSize, ballSizeMod, blueBalls, vagTotal, vagSize, vagSizeMod, clitSize, vulvaSize, heat, heatTime, showSide, button1, button2, button3, button5, button6, button7, button11, button12
   tempStr = ""
   tempStr += "You began your journey as a " + RaceName() + "." + "\n" + "\n" + math.floor(tallness / 12) + " feet and " + (tallness - math.floor(tallness / 12) * 12) + " inches tall, you wield " + HipDesc() + " hips and a " + ButtDesc() + " butt on an overall " + BodyDesc() + " figure."
   if hair > 0:
      tempStr += " With " + HairC() + "" + HairDesc() + ""
   if HairstyleLength(hair):
      tempStr += " " + HairL() + ""
   if hair > 0:
      tempStr += ", you look much like a" + GenName() + " " + DomName() + ""
   else:
      tempStr += " You look much like a" + GenName() + " " + DomName() + ""
   tempStr += "" + FaceDesc() + ""
   if tail > 1:
      tempStr += ", and a " + TailDesc() + " tail swishing upon your backside"
   if skunkAffinity >= 40:
      tempStr += ". A rather alluring scent constant lingers from your rump, sweet and pleasant, but with the potential for something far worse"
      if skinType == 2:
         tempStr += ". Your fur also sports two stripes that connect at your brow and runs over your head down to the scented area"
         if tail == 11:
            tempStr += " where they connect to the stripes on your tail"
   tempStr += ". " + EarDesc() + "."
   if CheckItem(234):
      tempStr += " Large, multi-pointed, slightly fuzzy antlers grow out from atop your head, feeling slightly heavy but perfectly melded to your skull so you can easily lift them."
   if CheckItem(101):
      tempStr += " Soft padding protects the palms of your hands, making them look much like paws, your nails being sharp claws."
   elif dominant == 9:
      tempStr += " Pointy talons grow from the tips of your fingers, more menacing than normal nails but not useful enough to be a threat."
   if legType >= 1000:
      tempStr += " From your waist down extends an almost second body, complete with a second belly and set of legs, standing on four " + LegDesc(10) + ". 'Taur' tends to be the term for such a being, with your crotch and rump far back at the end of the continued body."
      if legType == 1001:
         tempStr += " This second body is covered in white fur with large black patches, and your ass is squared off a bit from the bulky back hips."
      if legType == 1002:
         tempStr += " This second body matches the " + SkinDesc() + " of your upper half, with a thin and lithe torso, looking somewhat like a humans and not exactly made for riding but makes up for the frailness with plantigrade feet that easily support yourself, even though they aren't the speediest."
   if CheckItem(102) and legType == 1001:
      tempStr += " Keratin extends from your combined toes like hooves, your ankle angled upward and high up like a second backwards knee, making you walk on the tips of your hooved toes with a clap against the ground every step."
   elif legType == 1:
      tempStr += " Your ankles elongated and lithe, the front of your feet are large wide paws that help balance you as you walk digitigrade, your steps nothing but a soft and gentle patter against the ground."
   elif skinType == 5 and LegDesc(10) == "feet":
      tempStr += " Chitin extends further past your heels, making you stand higher and balancing more on your toes."
   if CheckItem(234):
      tempStr += " Your " + ButtDesc() + " butt also looks a bit tighter for its size with the " + SkinDesc() + " around it a lighter color than the rest, acting like a bullseye to your nethers. Below, the bone structure of your " + LegDesc(2) + " is also fairly lithe, causing you to step with a graceful swagger and wave your " + HipDesc() + " hips erotically with every footfall."
      tempStr += "\n" + "\n" + "You are currently wearing a "
   if attireTop != attireBot:
      tempStr += "" + ClothesTop() + " and " + ClothesBottom() + " that cover"
   else:
      tempStr += ClothesTop() + " that covers"
   if snuggleBall == True:
      tempStr += " the thick and soft layer of plushy snuggliness which coats"
   tempStr += " your " + SkinDesc() + " "
   if weapon == 10:
      tempStr += "while you defend yourself unarmed."
   else:
      tempStr += "while you defend yourself with a " + ItemName(weapon) + " as your weapon."
   if lilaWetStatus > 0 and (attireBot == 10 or attireBot == 11):
      tempStr += " Although, your " + ClothesBottom() + " doesn't do much to stem your squishy flow of slick fluids, just like a certain little felin girl."
   if legType >= 1000:
      tempStr += " Your tauric waist measures " + DecGet(tallness * 0.75 + pregnancyTime / 10 + vagBellyMod / 8 + bellyMod / 10,1) + " inches around, your " + BellyDesc() + " belly swinging underneath."
   else:
      tempStr += " Your waist measures " + DecGet(tallness / 2 + pregnancyTime / 10 + vagBellyMod / 8 + bellyMod / 10,1) + " inches around, sporting a " + BellyDesc() + " belly beneath your " + ClothesTop() + "."
   if dominant == 10:
      tempStr += " There's also a bit of extra pudge around your waist, some chubbiness to add to your pig-like nature."
   if wings > 0:
      tempStr += " Holes over your shoulders help your "
      if wings == 9:
         tempStr += "feathery"
      tempStr += " wings stretch freely, even though they're not of much use beyond hopping around and fly out of battle."
   if dairyFarmBrand == True:
      tempStr += " Beneath your " + ClothesBottom() + ", the shape of a bucket with milk splashing out over the edges is forever imprinted upon your " + ButtDesc() + " hind, marking you as property of the Softlik Dairy Farm."
   if breastSize > 0:
      if boobTotal == 2:
         tempStr += "\n" + "\n" + "Upon your chest heaves " + boobTotal + " " + BoobDesc() + " breasts. Your bust measures " + DecGet(breastSize * 0.5,1) + " inches in circumference beyond that of your chest, with " + NipDesc()
      if boobTotal == 4:
         tempStr += "\n" + "\n" + "Upon your chest heaves " + boobTotal + " " + BoobDesc() + " breasts; two pairs of equal size, one close below the other. Your dual busts each measure " + DecGet(breastSize * 0.5,1) + " inches in circumference beyond that of your chest, with " + NipDesc()
      if boobTotal == 6:
         tempStr += "\n" + "\n" + "Upon your chest and down to your belly heaves " + boobTotal + " " + BoobDesc() + " breasts; three pairs diminishing in size the lower they go. Your bust measures " + DecGet(breastSize * 0.5,1) + " inches in circumference beyond that of your chest, the next pair measuring " + DecGet(breastSize * 0.25,2) + " inches and the next measuring " + DecGet(breastSize * 0.15,2) + " inches; each with " + NipDesc()
      if boobTotal == 8:
         tempStr += "\n" + "\n" + "Upon your chest and down to your lower belly heaves " + boobTotal + " " + BoobDesc() + " breasts; four pairs all the same size and practically stacked on top of each other. Your bust measures " + DecGet(breastSize * 0.38,1) + " inches in circumference beyond that of your chest, the lower pairs just as large; each with " + NipDesc()
      if boobTotal == 10:
         tempStr += "\n" + "\n" + "Upon your chest and down to just above your crotch heaves " + boobTotal + " " + BoobDesc() + " breasts; five pairs all the same size and practically stacked on top of each other. Your bust measures " + DecGet(breastSize * 0.4,1) + " inches in circumference beyond that of your chest, the lower pairs just as large; each with " + NipDesc()
      if dominant == 5:
         tempStr += "teats"
      if dominant != 5:
         tempStr += "nipples"
      if nipType == 2:
         tempStr += " hidden within slits in your areola."
      elif lust < 50:
         tempStr += " softly bulging " + DecGet(nippleSize * 0.1,1) + " inches beyond that."
      elif lust < 75:
         tempStr += " stiffly standing " + DecGet(nippleSize * 0.2,1) + " inches beyond that."
      else:
         tempStr += " achingly hard and reaching " + DecGet(nippleSize * 0.25,1) + " inches beyond that."
      if nipType == 1:
         tempStr += " With four nubs each, your breasts look quite similar to cows' udders."
      if lactation > 0:
         if milkEngorgementLevel == 2:
            tempStr += " A few drops of milk dangle from each nipple as you pull your " + ClothesTop() + " from your engorged breasts to inspect yourself."
         if milkEngorgementLevel == 3:
            tempStr += " Milk sprays from each of your nipples as you pull your " + ClothesTop() + " from your heavily engorged breasts to inspect yourself, and continue to dribble down your belly and soaking into your " + ClothesBottom() + "."
      if milkSuppressantLact > 0:
         if milkEngorgementLevel == 2:
            tempStr += " The mounds beneath your nipples feel a bit swollen and sensitive, holding back all their milk."
         if milkEngorgementLevel == 3:
            tempStr += " The mounds beneath your nipples stand more perk than ever, despite feeling so heavy; so stuffed with milk that they're fairly hard."
   if udders == True:
      if legType == 1001:
         tempStr += "\n" + "\n" + "Just behind your tauric belly, squishing between your rear legs, hangs a " + UdderDesc() + " udder "
      elif cowAffinity >= 55:
         tempStr += "\n" + "\n" + "Just below your belly hangs a " + UdderDesc() + " udder "
      tempStr += "with 4 " + TeatDesc() + " teats, each " + DecGet(teatSize * 0.2,1) + " inches long"
      if udderLactation > 0:
         if udderEngorgementLevel == 2:
            tempStr += " and dribbling milk from your engorgement"
         if udderEngorgementLevel == 3:
            tempStr += " and practically spraying milk onto the ground before you from your excessive engorgment"
      if milkSuppressantUdder > 0:
         if milkEngorgementLevel == 2:
            tempStr += " feeling stiff as the bag beneath them is swollen with milk"
         if milkEngorgementLevel == 3:
            tempStr += " feeling quite hard and almost pointing straight out from the very swollen bag beneath them"
      tempStr += "."
   if cockTotal > 0:
      tempStr += "\n" + "\n" + "Above your groin rests " + cockTotal + " " + CockDesc() + " wang" + Plural(1) + "."
      if lust <= 30:
         if humanCocks > 0:
            tempStr += " " + humanCocks + " dangle" + Plural(3) + " flaccidly from your groin, reaching " + DecGet(cockSize * cockSizeMod * 0.25,2) + " inches down, with smooth skin and a mushroom-like glans, just like a human's."
         if horseCocks > 0:
            tempStr += " " + horseCocks + " hide" + Plural(3) + " within a fuzzy sheath that protrudes from your groin, around " + DecGet(cockSize * cockSizeMod / 12,1) + " inches in thickness."
         if wolfCocks > 0 or this.catCocks > 0 or this.rabbitCocks > 0:
            tempStr += " " + (wolfCocks + catCocks + rabbitCocks) + " hide" + Plural(3) + " within a fuzzy sheath that protrudes from your groin, around " + DecGet(cockSize * cockSizeMod / 16,1) + " inches in thickness."
         if lizardCocks > 0:
            tempStr += " " + lizardCocks + " hide" + Plural(3) + " in a slit, flush against your body."
         if bugCocks > 0:
            tempStr += " " + bugCocks + " dangle" + Plural(3) + " flaccidly from your groin, reaching " + DecGet(cockSize * cockSizeMod * 0.25,2) + " inches down, its four spikes around glans soft and blunt at the moment, the bumpy ridge underneath soft, almost like a bug's."
         if MoistCalc(1) > 2:
            tempStr += " Drops of pre slowly bead at the tip of your cock" + Plural(1) + ", "
            if horseCocks > 0 or wolfCocks > 0 or catCocks > 0 or rabbitCocks > 0:
               tempStr += " pooling within your sheath" + Plural(1) + ","
            tempStr += " running down your thighs as it continually blotches your " + ClothesBottom() + ", even though you're barely aroused at all. The slime is enough to slip yourself into a pussy smaller than you are long, at least."
      if lust > 30 and lust <= 70:
         if humanCocks > 0:
            tempStr += " " + humanCocks + " stand" + Plural(3) + " erect, reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches up, with smooth skin and a mushroom-like glans, just like a human's."
         if horseCocks > 0:
            tempStr += " " + horseCocks + " droop" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 12,1) + "-inch thick smooth sheath, reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches down your thigh with a ring of prepuce halfway down its length and a flat head at the end, just like a horse's."
         if wolfCocks > 0:
            tempStr += " " + wolfCocks + " poke" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, red and hard, smooth and covered in veins with a narrowing tip" + Plural(1) + ", standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a wolf's."
         if catCocks > 0:
            tempStr += " " + catCocks + " poke" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, pink and soft, with tender barbs near the narrowing tip" + Plural(1) + ", standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a cat's."
         if lizardCocks > 0:
            tempStr += " " + lizardCocks + " poke" + Plural(3) + " through the slit, stretching it wide as the purple flesh pulses with the ribbing along the top slightly stiff and the bulbous head feeling squishy to the touch, the narrow tip reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, probably like a reptile's."
         if rabbitCocks > 0:
            tempStr += " " + rabbitCocks + " poke" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, red and pointy, gently narrowing to their tip" + Plural(1) + ", somewhat like a carrot, standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a rabbit's."
         if bugCocks > 0:
            tempStr += " " + bugCocks + " stand" + Plural(3) + " erect, reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches up, with four fleshy spikes poking out from the rim of the glans and a sturdy bumpy ridge lining the underside, almost like a bug's."
         if knot == True:
            tempStr += " Your cock" + Plural(1) + " swell" + Plural(3) + " a little near the base, preparing for a chance for the knot" + Plural(1) + " to expand."
         if MoistCalc(1) > 2 and MoistCalc(1) <= 5:
            tempStr += " Drops of pre slowly bead at the tip of your cock" + Plural(1) + ", "
            tempStr += " running down your thighs as it blotches your " + ClothesBottom() + ". The slime is enough to slip yourself into a pussy smaller than you are long, at least."
         if MoistCalc(1) > 5:
            tempStr += " Pre steadily drips from your groin, making a large wet spot on your " + ClothesBottom() + ", looking more like you had peed yourself from all the seminal fluid.  Fortunately, you could probably slip " + OneYour(1) + " cock" + Plural(1) + " into a pussy smaller than you are, thanks to all the lubrication."
      if lust > 70:
         if humanCocks > 0:
            tempStr += " " + humanCocks + " stand" + Plural(3) + " erect, reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches up, throbbing strongly with smooth skin and a mushroom-like glans that is nearly purple in color, just like a human's."
         if horseCocks > 0:
            tempStr += " " + horseCocks + " twitches out of a " + DecGet(cockSize * cockSizeMod / 12,1) + "-inch thick smooth sheath, trying to stand " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches from your body with a ring of prepuce halfway down its length and a flaring flat head at the end, just like a horse's."
         if wolfCocks > 0:
            tempStr += " " + wolfCocks + " throb" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, red and hard, smooth and covered in veins that almost look purple, they're so full of blood, with a narrowing tip" + Plural(1) + ", standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a wolf's."
         if catCocks > 0:
            tempStr += " " + catCocks + " stiffly stand" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, pink and nearly hard, with tender barbs bristling out near the narrowing tip" + Plural(1) + ", standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a cat's."
         if lizardCocks > 0:
            tempStr += " " + lizardCocks + " harden" + Plural(3) + " through the slit, stretching it wide as the purple flesh throbs with the ribbing along the top nearly like actual bone and the bulbous head feeling quite swollen, the narrow tip reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, probably like a reptile's."
         if rabbitCocks > 0:
            tempStr += " " + rabbitCocks + " stiffly stand" + Plural(3) + " out of a " + DecGet(cockSize * cockSizeMod / 16,1) + "-inch thick fuzzy sheath, red and throbbing, almost breaking the conical shape with the pulsing, and standing " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches high, just like a rabbit's."
         if bugCocks > 0:
            tempStr += " " + bugCocks + " stand" + Plural(3) + " erect, reaching " + DecGet(cockSize * cockSizeMod * 0.5,1) + " inches up, throbbing strongly with four spikes jutting out around the glans, hard and pointy, and a bumpy ridge lining the underside that presses outward, almost like a bug's."
         if knot == True:
            tempStr += " Your cock" + Plural(1) + " bulge" + Plural(3) + " tremendously at " + Plural(5) + " base" + Plural(1) + ", the knot" + Plural(1) + " completely expecting to come at any moment and nearly " + DecGet(cockSize * cockSizeMod / 4,1) + " inches thick."
         if MoistCalc(1) > 2 and MoistCalc(1) <= 5:
            tempStr += " Drops of pre slowly bead at the tip of your cock" + Plural(1) + ", "
            tempStr += " running down your thighs as it blotches your " + ClothesBottom() + ". The slime is enough to slip yourself into a pussy smaller than you are long, at least."
         if MoistCalc(1) > 5 and MoistCalc(1) <= 10:
            tempStr += " Pre steadily drips from your groin, making a large wet spot on your " + ClothesBottom() + ", looking more like you had peed yourself from all the seminal fluid. Fortunately, you could probably slip " + OneYour(1) + " cock" + Plural(1) + " into a pussy smaller than you are, thanks to all the lubrication."
         if MoistCalc(1) > 10:
            tempStr += " Your " + ClothesBottom() + " feels completely swamped as pre flies from your lower half as you move about. Standing still for too long, you quickly form a small puddle of the slick stuff. You could probably stuff " + OneYour(1) + " cock" + Plural(1) + " into a pussy half your size without any difficulty, you're so slimy!"
   if showBalls == True and this.balls > 0:
      tempStr += "\n" + "\n" + "Beneath your cock" + Plural(1) + " swing" + Plural(3) + " a scrotum filled with " + balls + " " + BallDesc() + " testicles."
      if blueBalls > 36 and blueBalls <= 84:
         tempStr += " They groan and squirm, full of hot cum just waiting to blow."
      if blueBalls > 84:
         tempStr += " They groan so strongly you shudder slightly. They're so full of cum that they ache a bit, desperately wanting to come."
   if vagTotal > 0:
      tempStr += "\n" + "\n" + "Also, " + LegWhere(1) + " your " + LegDesc(2) + " nestles " + vagTotal + " " + VulvaDesc() + " pair" + Plural(2) + " of feminine nether-lips, about " + DecGet(vagSize * vagSizeMod * 0.5,1) + " inches deep, when aroused."
      if (vagSize * vagSizeMod * vagTotal) > (tallness / 2):
         tempStr += " So deep, in fact, that your belly bulges more because of the excess vaginal flesh."
      if lust <= 30:
         if clitSize >  vulvaSize * 3:
            tempStr += " Although you're hardly aroused, your " + ClitDesc() + " clit" + Plural(2) + " dangle" + Plural(4) + " softly from the front of your slit" + Plural(2) + ", measuring nearly " + DecGet(clitSize * 0.1,1) + " inches in length."
         if MoistCalc(2) > 2:
            tempStr += " Lubrication makes your cunt" + Plural(2) + " slick, the lips slipping past each other as you walk, while the slime continually blotches the crotch of your " + ClothesBottom() + ", whether you're horny or not. Fortunately, you could take a cock slightly bigger than you are deep, thanks to the slickness."
      if lust > 30 and lust <= 70:
         tempStr += " Your " + ClitDesc() + " clit" + Plural(2) + " swell" + Plural(4) + " from the hood" + Plural(2) + " at the front of your slit" + Plural(2) + ", reaching " + DecGet(clitSize * 0.2,1) + " inches in length and making you walk awkwardly as the sensitive button" + Plural(2) + " rub" + Plural(4) + " between your thighs."
         if MoistCalc(2) > 2 and MoistCalc(2) <= 5:
            tempStr += " Lubrication makes your cunt" + Plural(2) + " slick, the lips slipping past each other as you walk, while the slime continually blotches the crotch of your " + ClothesBottom() + ", whether you're horny or not. Fortunately, you could take a cock slightly bigger than you are deep, thanks to the slickness."
         if MoistCalc(2) > 5:
            tempStr += " So much feminine honey drips from your cunt" + Plural(2) + " that it looks like you have peed in your " + ClothesBottom() + " and webs of slime form sheets " + LegWhere(2) + " your " + LegDesc(2) + ". But, with all that lubrication you could take a cock around one and a half times long as you are deep."
      if lust > 70:
         tempStr += " Your " + ClitDesc() + " clit" + Plural(2) + " swell" + Plural(4) + " tremendously from the hood" + Plural(2) + " at the front of your slit" + Plural(2) + ", reaching " + DecGet(clitSize * 0.25,2) + " inches in length. You walk awkwardly half the time as squeezing the clit" + Plural(2) + " and swollen lips between your thighs is often too much, making you hunger to hump something."
         if MoistCalc(2) > 2 and MoistCalc(2) <= 5:
            tempStr += " Lubrication makes your cunt" + Plural(2) + " slick, the lips slipping past each other as you walk, while the slime continually blotches the crotch of your " + ClothesBottom() + ", whether you're horny or not. Fortunately, you could take a cock slightly bigger than you are deep, thanks to the slickness."
         if MoistCalc(2) > 5 and MoistCalc(2) <= 10:
            tempStr += " So much feminine honey drips from your cunt" + Plural(2) + " that it looks like you have peed in your " + ClothesBottom() + " and webs of slime form sheets " + LegWhere(2) + " your " + LegDesc(2) + ". But, with all that lubrication you could take a cock around one and a half times long as you are deep."
         if MoistCalc(2) > 10:
            tempStr += " A slow waterfall of feminine honey drips from your crotch, your " + ClothesBottom() + " completely soaked. If you stand for too long, you worry your " + LegDesc(10) + " will slip in the puddle you quickly make beneath you. It's so much that you could probably take a cock twice as large as you are deep!"
      if heat > 0 and heatTime < 0:
         tempStr += " Your nether-lips are also puffier and redder than usual, heat emanating from your loins, an oven just waiting to cook something..."
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      ButtonFunctions.Visible(1,1,1,0,1,1,1,0,1,0,1,1)
      #ButtonWrite(1,"More Stats")
      #ButtonWrite(2,"Titles")
      #ButtonWrite(3,"Statuses")
      #ButtonWrite(5,"Levels")
      #ButtonWrite(6,"Gear")
      #ButtonWrite(7,"Help")
      #ButtonWrite(11,"Credits")
      #ButtonWrite(12,"Return")
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedStats():
   global strMod, mentMod, libMod, senMod, SexPMod, changeMod, carryMod, HPMod, coinMod, cockSizeMod, vagSizeMod, cumMod, buttMod, babyFree, pregChanceMod, extraPregChance, pregTimeMod, pregRate, lactation, udders, udderLactation, milkMod, milkCap, rapeMod, enticeMod, runMod, showSide
   tempStr = ""
   tempStr += "These are the modifiers and multipliers for more detailed stats beyond your base stats:" + "\n"
   tempStr += "\n" + "Strength Modifier:" + "\t" + "\t" + "\t" + strMod
   tempStr += "\n" + "Mentality Modifier:" + "\t" + "\t" + "\t" + mentMod
   tempStr += "\n" + "Libidio Modifier:" + "\t" + "\t" + "\t" + libMod
   tempStr += "\n" + "Sensitivity Modifier:" + "\t" + "\t" + "\t" + senMod
   tempStr += "\n"
   tempStr += "\n" + "SexP Multiplier:" + "\t" + "\t" + "\t" + "\t" + SexPMod + ""
   tempStr += "\n" + "Adapting Multiplier:" + "\t" + "\t" + "\t" + changeMod + ""
   tempStr += "\n" + "Carry Capacity Modifier:\t" + carryMod + ""
   tempStr += "\n" + "Hit Point Modifier:" + "\t" + "\t" + "\t" + "+" + HPMod + ""
   tempStr += "\n" + "Bonus Coin Gain:" + "\t" + "\t" + "\t" + "+" + coinMod + ""
   tempStr += "\n"
   tempStr += "\n" + "Penis Size Multiplier:" + "\t" + "\t" + cockSizeMod + ""
   tempStr += "\n" + "Vagina Size Multiplier:" + "\t" + "\t" + vagSizeMod + ""
   tempStr += "\n" + "Semen Multiplier:" + "\t" + "\t" + "\t" + cumMod + ""
   tempStr += "\n" + "Butt Size Multiplier:" + "\t" + "\t" + "\t" + buttMod + ""
   tempStr += "\n" + "Hip Size Multiplier:" + "\t" + "\t" + "\t" + buttMod + ""
   tempPregMod = 0
   if babyFree > 0:
      tempPregMod -= 50
   tempStr += "\n" + "Pregnancy Chance:" + "\t" + "\t" + "\t" + (10 + pregChanceMod + tempPregMod) + "%"
   tempStr += "\n" + "Extra Baby Chance Mod:" + "\t" + "+" + extraPregChance + "%"
   tempStr += "\n" + "Pregnancy Time Mod:" + "\t" + "\t" + pregTimeMod + "hrs"
   tempStr += "\n" + "Pregnancy Time Rate:" + "\t" + "\t" + pregRate + "x"
   tempStr += "\n" + "Boob Lactation Rate:" + "\t" + "\t" + lactation + "ml/hr"
   if udders == True:
      tempStr += "\n" + "Udder Lactation Rate:" + "\t" + "\t" + udderLactation + "ml/hr"
   tempStr += "\n" + "Milk Modifier:" + "\t" + "\t" + "\t" + "\t" + "+" + milkMod + "ml/hr"
   tempStr += "\n" + "Bonus Milk Capacity:" + "\t" + "\t" + milkCap + "ml"
   tempStr += "\n"
   tempStr += "\n" + "Rape Modifier:" + "\t" + "\t" + "\t" + "\t" + "+" + rapeMod + ""
   tempStr += "\n" + "Enticement Modifier:" + "\t" + "\t" + "+" + enticeMod + ""
   tempStr += "\n" + "Run Chance:" + "\t" + "\t" + "\t" + "\t" + (20 + runMod) + "%"
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = ""
      button1["command"] = ""
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedTitles():
   global enticeMod, ment, lib, cockSize, cockSizeMod, tallness, breastSize, cockTotal, vulvaSize, clitSize, vagTotal, ballSize, balls, lactation, milkMod, udderLactation, pregnancyTime, vagBellyMod, dominant, currentZone, cowAffinity, malonRep, malonChildren, lilaRep, silRep, silPreg, showSide
   tempStr = ""
   tempStr += "Around town, you are thought of as being:\n"
   if enticeMod >= 10 and (ment + 40 < lib) and lib > 75:
      tempStr += "\n" + "A Sex Monster"
   elif (ment + 40 < lib) and lib > 60:
      tempStr += "\n" + "A Sex Fiend"
   elif enticeMod >= 10 and lib > 60:
      tempStr += "\n" + "A Slut"
   elif enticeMod >= 10:
      tempStr += "\n" + "A Whore"
   if (cockSize * cockSizeMod) > tallness and breastSize > (tallness * 3) and cockTotal > 0 and (vulvaSize > 50 or (clitSize * 3) > tallness) and vagTotal > 0:
      tempStr += "\n" + "A Mobile Pile of Naughtiness"
   elif (cockSize * cockSizeMod) > tallness and (cockSize * cockSizeMod) > 300 and cockTotal > 0:
      tempStr += "\n" + "Cock Mountain"
   elif (vulvaSize * tallness) > 300 and vulvaSize > 50 and vagTotal > 0:
      tempStr += "\n" + "The Mobile Fuckable Hill"
   elif (cockSize * cockSizeMod * 2) > tallness and (cockSize * cockSizeMod) > 100 and cockTotal > 0:
      tempStr += "\n" + "A Massive Dick"
   elif (vulvaSize * tallness) > 100 and vulvaSize > 50 and vagTotal > 0:
      tempStr += "\n" + "A Giant Pussy"
   if cockTotal > 10:
      tempStr += "\n" + "A Cock-Forest"
   elif cockTotal > 4:
      tempStr += "\n" + "A Cock-Tree"
   if vagTotal > 10:
      tempStr += "\n" + "Pussy Galore"
   elif vagTotal > 4:
      tempStr += "\n" + "Great for Orgies"
   if (ballSize * (ballSize / 2) * balls * cumMod * 2) > 20000:
      tempStr += "\n" + "The 'Cum Flooder'"
   elif (ballSize * (ballSize / 2) * balls * cumMod * 2) > 5000:
      tempStr += "\n" + "Dangerous When You Come"
   elif (ballSize * (ballSize / 2) * balls * cumMod * 2) > 1000:
      tempStr += "\n" + "Overflowing With Seed"
   if breastSize > (tallness * 3):
      tempStr += "\rMissus Tits"
   elif breastSize > (tallness * 2):
      tempStr += "\n" + "Wildly Top-Heavy"
   elif breastSize > tallness:
      tempStr += "\n" + "Blessed by the Boob Goddess"
   elif (breastSize * 2) > tallness:
      tempStr += "\rSurprisingly Stacked"
   elif (breastSize * 4) > tallness:
      tempStr += "\n" + "The Beautiful Bouncy Boobs that Everyone Stares At"
   if (lactation + milkMod) > 15000 and (lactation > 0 or (udderLactation + milkMod) > 30000) and udderLactation > 0:
      tempStr += "\rThe Milk Cannon"
   elif (lactation + milkMod) > 5000 and (lactation > 0 or (udderLactation + milkMod) > 10000) and udderLactation > 0:
      tempStr += "\rA Walking Milk Tank"
   elif (lactation + milkMod) > 500 and (lactation > 0 or (udderLactation + milkMod) > 1000) and udderLactation > 0:
      tempStr += "\rA Dairy Cow"
   if (pregnancyTime + vagBellyMod) > 500 and vagTotal > 0:
      tempStr += "\n" + "The 'Extraordinary Enormous Pregnant Belly'"
   elif (pregnancyTime + vagBellyMod) > 300 and vagTotal > 0:
      tempStr += "\n" + "A Fertility Goddess"
   tempStr += "\n" + "\n" + "Within " + RegionName(currentZone) + " specifically, you are considered to be:" + "\n"
   if (dominant == currentZone):
      tempStr += "\n" + "A Fellow Native"
   else:
      tempStr += "\n" + "A Strange Outsider"
   if (currentZone == 1):
      if cowAffinity > 50:
         tempStr += "\n" + "From the Dairy Farm"
      if malonRep == 2:
         tempStr += "\n" + "Malon's Personal Milker"
      if malonRep == 3:
         tempStr += "\n" + "Malon's Lover"
      if malonRep > 3:
         tempStr += "\n" + "Malon's Loving Partner"
      if malonChildren > 4:
         tempStr += "\n" + "The Progenitor of a New Race"
   if currentZone == 2:
      x = 0
   if currentZone == 3:
      x = 0
   if currentZone == 4:
      if lilaRep == 2:
         tempStr += "\n" + "Lila's Friend"
      if lilaRep == 3:
         tempStr += "\n" + "Lila's 'Playmate'"
      if lilaRep == 4:
         tempStr += "\n" + "Lila's Close Friend"
      if lilaRep == 5:
         tempStr += "\n" + "Lila's Kinky Mate"
   if currentZone == 6:
      if silRep == 1:
         tempStr += "\n" + "A Friend of the Strange Woman"
      if silRep > 1 and silRep < 4:
         tempStr += "\n" + "Silandrias' Virile Companion"
      if silRep > 3 and silRep < 6:
         tempStr += "\n" + "Silandrias' Excessively Fertile Companion"
      if silRep == 6:
         tempStr += "\n" + "Silandrias' Trusted Lover and Mate"
      if silRep == 6 and silPreg > 5000:
         tempStr += "\n" + "The Progenitor of an Extinct Race"
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = ""
      button2["command"] = ""
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedStatuses():
   global masoPot, sMasoPot, babyFree, charmTime, pheromone, eggceleratorTime, bodyOil, fertileGel, milkSuppressant, exhaustionPenalty, lustPenalty, heatTime, milkEngorgementLevel, udderEngorgementLevel, blueBalls, pregnancyTime, lockTail, lockFace, lockSkin, lockBreasts, lockEars, lockLegs, lockNipples, lockCock, showSide
   tempStr = ""
   tempStr += "The following status effects are currently active on you that you are aware of: (Name - Hours Left)" + "\n"
   if masoPot > 0:
      tempStr += "\n" + "Masochism Potion" + "\t" + "\t" + masoPot + ""
   if sMasoPot > 0:
      tempStr += "\n" + "Supererior Maso. Pot." + "\t" + "\t" + sMasoPot + ""
   if babyFree > 0:
      tempStr += "\n" + "Baby Free" + "\t" + "\t" + "\t" + "\t" + babyFree + ""
   if charmTime > 0:
      tempStr += "\rCharmed\t\t\t\t" + charmTime + ""
   if pheromone > 0:
      tempStr += "\n" + "Pheromones" + "\t" + "\t" + "\t" + pheromone + ""
   if eggceleratorTime > 0:
      tempStr += "\n" + "Eggcelerator" + "\t" + "\t" + "\t" + eggceleratorTime + ""
   if bodyOil > 0:
      tempStr += "\n" + "Body Oil" + "\t" + "\t" + "\t" + "\t" + bodyOil + ""
   if fertileGel > 0:
      tempStr += "\n" + "Fertile Gel" + "\t" + "\t" + "\t" + fertileGel + ""
   if milkSuppressant > 0:
      tempStr += "\n" + "Milk Suppressant" + "\t" + milkSuppressant + ""
   tempStr += "\n"
   if exhaustionPenalty == 2:
      tempStr += "\n" + "Exhausted"
   if exhaustionPenalty == 1:
      tempStr += "\n" + "Tired"
   if lustPenalty > 0:
      tempStr += "\n" + "Horny"
   if heatTime < 0:
      tempStr += "\n" + "In Heat"
   if milkEngorgementLevel > 0:
      tempStr += "\n" + "Engorged Breasts"
   if udderEngorgementLevel > 0:
      tempStr += "\n" + "Engorged Udder"
   if blueBalls > 84:
      tempStr += "\n" + "Blue Balls"
   if pregnancyTime > 36:
      tempStr += "\n" + "Pregnant"
   tempStr += "\r"
   if lockTail > 0:
      tempStr += "\n" + "Racial-locked Tail"
   if lockFace > 0:
      tempStr += "\n" + "Racial-locked Face"
   if lockSkin > 0:
      tempStr += "\n" + "Racial-locked Skin"
   if lockBreasts > 0:
      tempStr += "\n" + "Racial-locked Breasts"
   if lockEars > 0:
      tempStr += "\n" + "Racial-locked Ears"
   if lockLegs > 0:
      tempStr += "\n" + "Racial-locked Legs"
   if lockNipples > 0:
      tempStr += "\n" + "Racial-locked Nipples"
   if lockCock > 0:
      tempStr += "\n" + "Racial-locked Cocks"
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = ""
      button3["command"] = ""
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedLevels():
   global babyFactLevel, bodyBuildLevel, hyperHappyLevel, alchemistLevel, milkMaidLevel, shapeshiftyLevel, level, showSide
   tempStr = ""
   tempStr += "You have the following perks and their respective ranks:" + "\n"
   if babyFactLevel > 0:
      tempStr += "\n" + "Baby Factory" + "\t" + "\t" + babyFactLevel + ""
   if bodyBuildLevel > 0:
      tempStr += "\n" + "Body Builder" + "\t" + "\t" + bodyBuildLevel + ""
   if hyperHappyLevel > 0:
      tempStr += "\n" + "Hyper Happy" + "\t" + "\t" + hyperHappyLevel + ""
   if alchemistLevel > 0:
      tempStr += "\n" + "Alchemist" + "\t" + "\t" + alchemistLevel + ""
   if milkMaidLevel > 0:
      tempStr += "\n" + "Milk Maid" + "\t" + "\t" + milkMaidLevel + ""
   if shapeshiftyLevel > 0:
      tempStr += "\n" + "Shapeshifty" + "\t" + "\t" + shapeshiftyLevel + ""
   tempStr += "\n" + "\n" + "For a total of " + level + " levels."
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = ""
      button5["command"] = ""
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedGear():
   global bagArray, bagStackArray, showSide
   tempStr = ""
   tempStr += "You have the following items in your Bag:" + "\n"
   for i in range(0, 26):
   #(this.i = 0; this.i <= this.bagArray.length; ++this.i)
      if bagArray[i] != 0:
         tempStr += "\n" + ItemName(bagArray[i])
      if bagStackArray[i] > 1:
         tempStr += " x" + bagStackArray[i]
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,true)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = ""
      button6["command"] = ""
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedFetishes():
   global maleFetish, femaleFetish, hermFetish, narcissistFetish, dependentFetish, dominantFetish, submissiveFetish, lboobFetish, sboobFetish, furryFetish, scalyFetish, smoothyFetish, pregnancyFetish, bestialityFetish, milkFetish, sizeFetish, unbirthingFetish, ovipositionFetish, toyFetish, hyperFetish, showSide
   tempStr = ""
   tempStr += "You have the following interests in kinks (0 being no interest, 1 being average interest, etc):" + "\n"
   tempStr += "\n" + "Major kinks (affects most situations):" + "\n"
   tempStr += "\n" + "Men" + "\t" + "\t" + "\t" + maleFetish + ""
   tempStr += "\n" + "Women" + "\t" + "\t" + "\t" + femaleFetish + ""
   tempStr += "\n" + "Herms" + "\t" + "\t" + "\t" + hermFetish + ""
   tempStr += "\n" + "Yourself" + "\t" + "\t" + narcissistFetish + ""
   tempStr += "\n" + "Others" + "\t" + "\t" + "\t" + dependentFetish + ""
   tempStr += "\n" + "\n" + "Moderate kinks (affects many situations):" + "\n"
   tempStr += "\n" + "Dominant" + "\t" + "\t" + dominantFetish + ""
   tempStr += "\n" + "Submissive" + "\t" + "\t" + submissiveFetish + ""
   tempStr += "\n" + "Large Boobs" + "\t" + lboobFetish + ""
   tempStr += "\n" + "Small Boobs" + "\t" + sboobFetish + ""
   tempStr += "\n" + "Furries" + "\t" + "\t" + "\t" + furryFetish + ""
   tempStr += "\n" + "Scalies" + "\t" + "\t" + "\t" + scalyFetish + ""
   tempStr += "\n" + "Smoothies" + "\t" + "\t" + smoothyFetish + ""
   tempStr += "\n" + "\n" + "Minor kinks (affects few situations):" + "\n"
   tempStr += "\n" + "Pregnancy" + "\t" + "\t" + pregnancyFetish + ""
   tempStr += "\n" + "Bestiality" + "\t" + "\t" + bestialityFetish + ""
   tempStr += "\n" + "Milk" + "\t" + "\t" + "\t" + milkFetish + ""
   tempStr += "\n" + "Size" + "\t" + "\t" + "\t" + sizeFetish + ""
   tempStr += "\n" + "Unbirthing" + "\t" + "\t" + unbirthingFetish + ""
   tempStr += "\n" + "Oviposition" + "\t" + "\t" + ovipositionFetish + ""
   tempStr += "\n" + "Toys" + "\t" + "\t" + "\t" + toyFetish + ""
   tempStr += "\n" + "Hyper" + "\t" + "\t" + "\t" + hyperFetish + ""
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedHelp():
   global showSide
   tempStr = ""
   tempStr += "<b><u>Stats</u></b>\r"
   tempStr += "\r-Strength - Adds to damage, rape chance, carry capacity, and HP. Reduces SexP gain from sex and masturbation."
   tempStr += "\r-Mentality - Fights hostile lust gain, improves helpful lust loss."
   tempStr += "\r-Libido - Increases lust gain, can hinder mentality in events."
   tempStr += "\r-Sensitivity - Increases damage taken and increases lust loss."
   tempStr += "\r-HP - Your Hit Points. Lose too much and you\'ll pass out."
   tempStr += "\r-Lust - Can overwhelm your actions, resulting in getting raped in battle, but large pleasant losses of lust grant SexP."
   tempStr += "\r\r<b><u>Actions</u></b>\r"
   tempStr += "\r-Stash - Extra inventory space that you cannot carry, but moves with you from town to town."
   tempStr += "\r-Prostitute - When desparate for money, you can resort to prostitution. Remember, beggars can\'t be choosers and you may not like the company."
   tempStr += "\r-Alchemy - Mix items together to get other items. Learn recipes around the world."
   tempStr += "\r-Bag - Where you hold all your items. Shift+Click will allow you to select an item to move, Shift+Click a slot to move it to."
   tempStr += "\r-Rape - A combat action to attempt to overpower your opponent and sex their brains out. An aroused opponent is easier to rape."
   tempStr += "\r-Entice - A combat action to raise opponent\'s lust (if they find you attractive)."
   tempStr += "\r-Run - A combat action to flee from battle. Running in a dungeon will leave the dungeon."
   tempStr += "\r-Submit - Because some people can\'t wait to be king- I mean raped."
   tempStr += "\r\r<b><u>Tips</u></b>\r"
   tempStr += "\r-Carry Capacity - Determined by strength, height, body type, and modifiers. Determines how much of yourself you can carry."
   tempStr += "\r-Shops - Each town has unique wares in many of their shops, so it\'s good to look around."
   tempStr += "\r-Race - Some racial features are based on whatever blood is most dominant. Some features can be shared."
   tempStr += "\r-Bust Size - 1 inch of bust circumference = 1 cup in real life. 1 inch = A-cup, 4 inches = D-cup, 4.5 inches = DD-cup, 26 inches = Z-cup."
   tempStr += "\r-Breasts - Everybody has breasts. Yes, even males. How many is determined by your race."
   tempStr += "\r-Empty Button - Outside of inventories, these mean you have access to something, but do not currently have the correct item/requirements."
   tempStr += "\r\r<b><u>Hotkeys</u></b>\r"
   tempStr += "\rOnly function when they show."
   tempStr += "\r-Save = F2, Load = F4, New Game = Backspace, Appearance = U"
   tempStr += "\r-Font Size+ = Up, Font Size- = Down, Theme = Left, Font Color = Right"
   tempStr += "\r-Reset Font Size = Ctrl, Font Bold = /?, Toggle Side Window = ."
   tempStr += "\r-Side window buttons (in order):"
   tempStr += "\r\tUIOP"
   tempStr += "\r\tHJKL"
   tempStr += "\r-Main choice buttons (both keyboard and NumPad in order):"
   tempStr += "\r\tQWER\t789-"
   tempStr += "\r\tASDF\t456+"
   tempStr += "\r\tZXCV\t123Enter"
   if showSide == true:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = ""
      button7["command"] = ""
      button11["text"] = "Credits"
      button11["command"] = "DetailedCredits"
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def DetailedCredits():
   global versionNumber, showSide
   tempStr = ""
   tempStr += "Nimin v" + versionNumber + "\n" + "Created by:" + "\t" + "--Xadera" + "\n" + "\t" + "www.furaffinity.net/user/xadera/" + "\n" + "\n" + "Original concept by:" + "\t" + "--Fenoxo" + "\n" + "\t" + "fenoxo.com"
   tempStr += "\n" + "\n" + "Special thanks to SumigakiFox (owner of Silandrias) and Arlyurl (made the Nimin image) on FA."
   tempStr += "\n" + "\n" + "Prostitution scene editors (thanks for the work!): Torakazu, Bahamad, and omegaokami on FA."
   tempStr += "\n" + "\n" + "Prostitution scene writers:" + "\n" + "\t" + "--Buncubus, BantinNysam, TheAbyssalWatcher, mike12345, V, grottokraft, Ludoergosum, perrothetraveler, reikonova, shockblock99, Kidou, bunnybunbun, supernaut, shaesullivan, m3chawolf, Kizzneth, barkbarkboom, Torakazu"
   if showSide == True:
      OutputSideText(tempStr,True)
   else:
      OutputMainText(tempStr,True)
      button1["text"] = "More Stats"
      button1["command"] = "DetailedStats"
      button2["text"] = "Titles"
      button2["command"] = "DetailedTitles"
      button3["text"] = "Statuses"
      button3["command"] = "DetailedStatuses"
      button5["text"] = "Levels"
      button5["command"] = "DetailedLevels"
      button6["text"] = "Gear"
      button6["command"] = "DetailedGear"
      button7["text"] = "Help"
      button7["command"] = "DetailedHelp"
      button11["text"] = ""
      button11["command"] = ""
      button12["text"] = "Return"
      button12["command"] = "DoProcess"

!def SaveGo():
!def LoadGo():
!def DoSave():
!def DoLoad():
def CheckUpdate():
     void
!def LoadFromFile():
!def FileSelected():
!def LoadError():
!def DataLoaded():
def DoRace():
   global boobTotal, race, foundFirmshaft, currentZone, horseAffinity, cockSizeMod, vagSizeMod, dominant, tail, ears, skinType, faceType, strength, mentality, libido, sensitivity, tallness, foundTieden, wolfAffinity, knot, changeMod, foundSoftlik, humanAffinity, foundSizCalit, catAffinity, heat, heatMaxTime, heatTime, foundOviasis, lizardAffinity, eggLaying, eggTime, eggMaxTime
   #trace("race");
   #trace(this.tallness);
   BC()
   ButtonFunctions.Visible(1,0,1,0,0,1,0,0,1,0,1,0)
   OutputMainText("Choose which race you want to be:",True)
   OutputMainText("\n" + "\n" + "Human - A race supposedly descendant of apes, their curious minds are more open to change and their skin is slightly more sensitive.",False)
   OutputMainText("\n" + "\n" + "Equan - A race supposedly descendant of horses, their large genitals make them slightly more sexual and their muscles are more powerful.",False)
   OutputMainText("\n" + "\n" + "Lupan - A race supposedly descendant of wolves, their lean bodies are stronger and their minds more quick-witted.",False)
   OutputMainText("\n" + "\n" + "Felin - A race supposedly descendant of cats, their lust-driven society makes them a bit more sexual and sensitive.",False)
   OutputMainText("\n" + "\n" + "Lizan - A race supposedly descendant of some kind of reptile, their desert-adapted bodies have made them stronger, but they're still careful as their scales make them somewhat sensitive.",False)
   templist = [1, "Equan", 3, "Lupan", 6, "Human", 9, "Felin", 11, "Lizan"]
   DoButtonChoices(templist)
   #this.doListen = function():void
   boobTotal = 2
   if (buttonChoice == 1):
      race = 2
      foundFirmshaft = True
      currentZone = 2
      horseAffinity = 50
      cockSizeMod += 1
      vagSizeMod += 1
      dominant = 2
      tail = 2
      ears = 2
      skinType = 2
      faceType = 20
      strength = 17
      mentality = 15
      libido = 17
      sensitivity = 15
      tallness += 4
      DoGender()
   elif (buttonChoice == 3):
      race = 3
      foundTieden = True
      currentZone = 3
      wolfAffinity = 50
      knot = true
      boobTotal = 6
      dominant = 3
      tail = 3
      ears = 3
      skinType = 2
      faceType = 30
      strength = 17
      mentality = 17
      libido = 15
      sensitivity = 15
      tallness += -2
      DoGender()
   elif (buttonChoice == 6):
      race = 1
      changeMod += 0.5
      currentZone = 1
      foundSoftlik = True
      humanAffinity = 50
      dominant = 1
      ears = 1
      skinType = 1
      faceType = 10
      strength = 15
      mentality = 17
      libido = 15
      sensitivity = 17
      DoGender()
   elif (buttonChoice == 9):
      race = 4
      foundSizCalit = True
      currentZone = 4
      catAffinity = 50
      dominant = 4
      heat += 1
      heatMaxTime = 96
      heatTime = 96
      boobTotal = 6
      tail = 4
      ears = 4
      skinType = 2
      faceType = 40
      strength = 15
      mentality = 15
      libido = 17
      sensitivity = 17
      tallness += -3
      DoGender()
   elif (buttonChoice == 11):
      race = 6
      foundOviasis = True
      currentZone = 6
      lizardAffinity = 50
      dominant = 6
      eggLaying = 1
      eggTime = 36
      eggMaxTime = 36
      tail = 6
      ears = 6
      skinType = 3
      faceType = 60
      strength = 17
      mentality = 16
      libido = 15
      sensitivity = 16
      tallness += 2
      DoGender()

def DoGender():
   global currentDayCare, dominant, buttonChoice, gender, cockSize, ballSize, balls, cockTotal, cockMoist, strength, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, vagSize, vulvaSize, pregArray, vagTotal, vagMoist, clitSize, mentality,
   currentDayCare = dominant
   StatDisplay()
   OutputMainText("Choose which gender you want to be:" + "\n" + "\n" + "Male - You has painus!" + "\n" + "\n" + "Female - You has vagoo!" + "\n" + "\n" + "Herm - You has painus and vagoo!",True)
   ButtonFunctions.Visible(0,0,0,0,1,1,1,0,0,0,0,0)
   DoButtonChoices(5, "Male", 6, "Female", 7, "Herm")
   #this.doListen = function():void
   if (buttonChoice == 5):
      gender = 1
   elif (buttonChoice == 6):
      gender = 2
   elif (buttonChoice == 7):
      gender = 3
   if (gender == 1):
      cockSize = 12
      ballSize = 3
      balls = 2
      cockTotal = 1
      cockMoist = 1
      strength += 1
      if (dominant == 1):
         humanCocks = 1
      elif (dominant == 2):
         horseCocks = 1
      elif (dominant == 3):
         wolfCocks = 1
      elif (dominant == 4):
         catCocks = 1
      elif (dominant == 6):
         lizardCocks = 2
         cockTotal += 1
   elif (gender == 2):
      vagSize = 12
      vulvaSize = 5
      pregArray = [False,0,0,0,0]
      vagTotal = 1
      vagMoist = 1
      clitSize = 2
      mentality += 1
   if (gender == 3):
      cockSize = 8
      ballSize = 2
      balls = 2
      cockTotal = 1
      cockMoist = 1
      pregArray = [False,0,0,0,0]
      vagTotal = 1
      vagMoist = 1
      vagSize = 8
      vulvaSize = 3
      if (dominant == 1):
         humanCocks = 1
      elif (dominant == 2):
         horseCocks = 1
      elif (dominant == 3):
         wolfCocks = 1
      elif (dominant == 4):
         catCocks = 1
      elif (dominant == 6):
         lizardCocks = 2
         cockTotal += 1
      libido += 1
   BodyType()

def BodyType():
   global gender, buttonChoice body, hips, butt, tallness, strength, libido, cockSize, ballSize, balls, cockTotal, cockMoist, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, vagSize, vulvaSize, pregArray, vagTotal, vagMoist, clitSize, breastSize, nippleSize, sensitivity, mentality
   StatDisplay()
   OutputMainText("Choose your body type. Types determine height and a few beginning characteristics. Their names describe what they look like and may potentially alter your true gender.",True)
   if (gender == 1):
      ButtonFunctions.Visible(1,0,1,0,1,0,1,0,0,1,0,0)
      templist = [1, "Bodybuilder", 3, "Average", 5, "Cunt Boy", 7, "Femme Boy", 10, "Childlike"]
      DoButtonChoices(templist)
      if (buttonChoice == 1):
         body = 29
         hips = 4
         butt = 4
         tallness += 70 + math.floor(Percent() / 10)
         strength += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 3):
         body = 20
         hips = 3
         butt = 3
         tallness += 68 + math.floor(Percent() / 10)
         libido += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 5):
         body = 20
         hips = 3
         butt = 3
         tallness += 68 + math.floor(Percent() / 10)
         libido += 1
         Stats(0,0,0,0)
         cockSize = 0
         ballSize = 0
         balls = 0
         cockTotal = 0
         cockMoist = 0
         humanCocks = 0
         horseCocks = 0
         wolfCocks = 0
         catCocks = 0
         lizardCocks = 0
         vagSize = 8
         vulvaSize = 3
         pregArray = [False,0,0,0,0]
         gender = 2
         vagTotal = 1
         vagMoist = 1
         clitSize = 2
         DoStartingDescription()
      elif (buttonChoice == 7):
         body = 15
         hips = 7
         butt = 6
         breastSize = 2
         nippleSize = 2
         tallness += 60 + math.floor(Percent() / 10)
         sensitivity += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 10):
         body = 7
         hips = 1
         butt = 2
         tallness += 42 + math.floor(Percent() / 10)
         sensitivity += 2
         mentality -= 2
         strength -= 4
         libido += 2
         cockSize = 6
         cockMoist = 1
         ballSize = 1
         Stats(0,0,0,0)
         DoStartingDescription()
   elif (gender == 2):
      ButtonFunctions.Visible(0,1,1,0,1,0,0,0,0,1,0,0)
      templist = [2, "Bodybuilder", 3, "Voluptuous", 5, "Average", 10, "Childlike"]
      DoButtonChoices(templist)
      if (buttonChoice == 2):
         body = 29
         hips = 5
         butt = 4
         tallness += 68 + math.floor(Percent() / 10)
         breastSize = 4
         nippleSize = 4
         strength += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 3):
         body = 16
         hips = 9
         butt = 6
         tallness += 60 + math.floor(Percent() / 10)
         breastSize = 10
         nippleSize = 10
         libido += 2
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 5):
         body = 13
         hips = 6
         butt = 5
         tallness += 60 + math.floor(Percent() / 10)
         breastSize = 6
         nippleSize = 6
         mentality += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      if (buttonChoice == 10):
         body = 7
         hips = 2
         butt = 2
         tallness += 41 + math.floor(Percent() / 10)
         sensitivity += 2
         mentality -= 2
         strength -= 4
         libido += 2
         vagSize = 6
         breastSize = 2
         nippleSize = 2
         vulvaSize = 2
         clitSize = 1
         vagMoist = 1
         Stats(0,0,0,0)
         DoStartingDescription()
   if (gender == 3):
      ButtonFunctions.Visible(0,1,0,0,1,1,0,0,0,1,0,0)
      templist = [2, "Bodybuilder", 5, "Masculine", 6, "Feminine", 10, "Childlike"]
      DoButtonChoices(templist)
      if (buttonChoice == 2):
         body = 29
         hips = 4
         butt = 4
         tallness += 68 + math.floor(Percent() / 10)
         breastSize = 6
         nippleSize = 6
         strength += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      elif (buttonChoice == 5):
         body = 19
         hips = 3
         butt = 3
         tallness += 62 + math.floor(Percent() / 10)
         breastSize = 2
         nippleSize = 2
         libido += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      if (buttonChoice == 6):
         body = 14
         hips = 5
         butt = 4
         tallness += 58 + math.floor(Percent() / 10)
         breastSize = 6
         nippleSize = 6
         mentality += 1
         Stats(0,0,0,0)
         DoStartingDescription()
      if (buttonChoice == 10):
         body = 7
         hips = 2
         butt = 2
         tallness += 42 + math.floor(Percent() / 10)
         sensitivity += 2
         mentality -= 2
         strength -= 4
         libido += 2
         cockSize = 4
         cockMoist = 1
         ballSize = 1
         vagSize = 4
         clitSize = 1
         vagMoist = 1
         vulvaSize = 1
         breastSize = 2
         nippleSize = 2
         Stats(0,0,0,0)
         DoStartingDescription()

def DoStartingDescription():
   global currentZone, race
   RegionChange(currentZone)
   DayTime(0)
   currentRegion.visible = True
   region.visible = True
   DoHP(10000)
   DoSexP(0)
   OutputMainText("\n" + "\"...Hello?\"",True)
   DoNext()
   #this.doListen = function():void
   OutputMainText("\n" + "\n" + "\"...Can anybody hear me?\"",True)
   DoNext()
   #doListen = function():void
   OutputMainText("\n" + "\n" + "\n" + "\"Please... I know you are still young... You still do not know the world... But... It is almost ready again...\"",True)
   DoNext()
   #doListen = function():void
   OutputMainText("\n" + "\n" + "\n" + "\n" + "\"I am so tired...\"\n" + "\n" + "\"...Please...\"",True)
   DoNext()
   #doListen = function():void
   OutputMainText("\n" + "\n" + "\n" + "\n" + "\n" + "\"S⌠æ☼m±¥§ me...\"",True)
   DoNext()
   #doListen = function():void
   OutputMainText("Ugh... You awaken from that dream for the fifth time this month. That soft, gentle voice echoes around your mind. A numbing dream with nothing to keep your attention. Something about a tower... Not a dream about flying or fleeing, nor school nor sex. Just this bland dream that you can remember better than all the rest. And yet you can never recall those last words..." + "\n" + "\n" + "It's been a few months since you started having that dream and it's been growing in frequency. Just so... annoying. Makes you feel anxious and antsy, like there is something missing in your life." + "\n" + "\n" + "Life isn't bad in ",True)
   if (race == 1):
      OutputMainText("Softlik, though. The houses of wood and stone are comfortable, safe, and stable. The rolling hills around the city are quite beautiful. Lots of people in town are coming up with new potions or inventions, and with humans being so prone to being changed by the outside world of Nimin, there's rarely a dull moment.",False)
   if (race == 2):
      OutputMainText("Firmshaft, though. The large canvas tents provide plenty of room for harems filled with the large genitals equans are most notable for, with plenty of airflow to keep things from getting too hot. The broad plains allow for lots of trotting and races. Between the warmth and the plentiful activity, there's always great sex and comfort around here, with little need to venture into the outside world of Nimin.",False)
   if (race == 3):
      OutputMainText("Tieden, though. The wooden buildings and surrounding walls provide plenty of security from the outside world of Nimin, all the forest and jungle around filled with dangers. Not that there's any reason to be afraid; with the training and constant vigil, lupans are great at handling their foes. Especially when it comes to \"handling\" them. Plus letting off steam around here tends to be rather enjoyable.",False)
   if (race == 4):
      OutputMainText("Siz'Calit, though. The tree-borne huts and bridges admist the canopy of the jungle allows for plenty of breezes and pleasant napping spots in the hot and humid area. And with so many felin females going into heat and craving sex, it's difficult to tell if the humidity is from the jungle itself or the kinky activity within. It's hard to imagine a sex-crazed felin surviving long in the outside world on Nimin.",False)
   if (race == 6):
      OutputMainText("Oviasis, though. The rock-hewn homes built into the sides of the surrounding cliffs provide plenty of insulation against the warm days and cool nights of the desert. This small oasis of paradise in the middle of nowhere provides plenty of ways to lounge, allowing the lizan people to soak in the sun and the women to casually lay their eggs. This near-resort is usually much more pleasant than the outside world of Nimin.",False)
   OutputMainText("\n" + "\n" + "But that dream...",False)
   DoNext()
   #doListen = function():void
   OutputMainText("It isn't unheard of to go venturing out. In fact, you know there are other civilizations around, separated by the strange wilderness. Explorers of other races have come and visited from time to time. A rarity and always so interesting in how they look and act, so diverse from your own people." + "\n" + "\n" + "Although, they do make you wonder... Why don't you see them more often? They seem to enjoy visiting, after all. There's no history of hate or trouble between the peoples. Although, the recorded history only goes back a few generations, so who knows what could have happened centuries ago..." + "\n" + "\n" + "Oh well.",True)
   DoNext()
   #doListen = function():void
   OutputMainText("You finally get out of bed and start your day. And after that dream, you just can't seem to shake the feeling that there's more to this life, this world... The dangerously odd world of Nimin.",True)
   DoNext()
   #doListen = function():void
   toggleSide()
   toggleSide()
   Option7.visible = true
   currentState = 1
   DoGeneral()

!def DoGeneral():
!def DoJizzPants():
!def DoBag():
def UseItem(ID:int):
   global bagStackArray, choiceListResult
   if ID == 0:
      OutputMainText("This slot is empty.",True)
      DoBag()
   else:
      OutputMainText(ItemDescription(ID),True)
      if UsableItem(ID) == True or ConItem(ID) == True:
         OutputMainText("\n" + "\n" + "Are you sure you want to use this item?",False)
         if ConItem(ID) == True:
            OutputMainText("\n" + "\n" + "Warning: Using this item will consume it.",False)
         ButtonConfirm()
         if (buttonChoice == 6):
            if ConItem(ID) == True:
               if bagStackArray[choiceListResult[1]] <= 1:
                  BagSlotClear(choiceListResult[1])
               else:
                  bagStackArray[choiceListResult[1]] = bagStackArray[choiceListResult[1]] - 1
            FoodItem(ID)
            DoItemUse(ID)
            StatDisplay()
         else:
            DoBag()
      else:
         DoBag()

!def ItemAdd(ID:int):
   global itemGainArray
   itemGainArray.push(ID)

!def GainItem(ID:int):
   global openSlot, bagArray, bagStackArray, itemGainArray
   tempNum = 0
   openSlot = CheckOpenSlot(ID)
   if openSlot >= 0:
      if bagArray[openSlot] == 0:
         bagArray[openSlot] = ID
         bagStackArray[openSlot] = 1
         PassiveItemAdd(ID)
         tempNum += 1
         while bagStackArray[openSlot] < ItemStackMax(ID) and itemGainArray.indexOf(ID) != -1:
            this.itemGainArray.pop()
            bagStackArray[openSlot] += 1
            tempNum += 1
      else:
         tempNum += 1
         bagStackArray[openSlot] += 1
         while bagStackArray[openSlot] < ItemStackMax(ID) and itemGainArray.index(ID) != -1:
            this.itemGainArray.pop()
            bagStackArray[openSlot] += 1
            tempNum += 1
      if tempNum < 2:
         OutputMainText("You have obtained a " + ItemName(ID) + "!",True)
      else:
         OutputMainText("You have obtained " + tempNum + "x " + ItemName(ID) + "!",True)
      DoEnd()
   else:
      OutputMainText("You have obtained a " + ItemName(ID) + "!\n" + "\n" + "However, you do not have enough room in your bag. Click on an item in your bag to replace it with the new one or click a non-item button to ignore the new item.",True)
      DoDiscard(ID)

def CheckOpenSlots(ID:int):
   global bagArray
   slot = -1
   for i in range(0, 26):
      if (bagArray[i] == 0):
         slot = i
   for i in range(0, 26):
      if (bagStackArray[i] < ItemStackMax(ID)) and (bagArray[i] == ID):
         slot = i
   return slot

!def BagSlotAdd(amount:int):
   for i in ??:
   #for (this.i = 1; this.i <= amount; ++this.i)
      this.bagArray.push(0)
      this.bagStackArray.push(0)

!def BagSlotRemove(param1:int):
   _loc2_ = 0
   _loc3_ = 0
   _loc4_ = 0
   for i in ??:
   #for (this.i = 1; this.i <= param1; ++this.i)
      _loc2_ = this.bagArray.pop()
      _loc3_ = this.bagStackArray.pop()
      if (_loc2_ != 0) and (_loc3_ != 0):
         for ?? in ??:
         #for(_loc4_ = 1; _loc4_ <= _loc3_; this.itemAdd(_loc2_),_loc4_++)
         {
         }

def BagSlotClear(slot:int):
   global bagArray, bagStackArray
   PassiveItemRemove(bagArray[slot])
   bagArray[slot] = 0
   bagStackArray[slot] = 0

!def DoDiscard(ID:int):
{
   this.choiceListButtons("Bag");
   this.doListen = function():void
   {
      choiceListSelect("Bag");
      if(buttonChoice == 12)
      {
         while(itemGainArray.indexOf(ID) != -1)
         {
            itemGainArray.pop();
         }
         doProcess();
      }
      else if(buttonChoice == 4 || buttonChoice == 8)
      {
         choiceListButtons("Bag");
      }
      else if(canLose(choiceListResult[0]))
      {
         outputMainText(itemDescription(choiceListResult[0]) + "\r\r" + itemDescription(ID) + "\r\rDo you want to replace " + itemName(choiceListResult[0]) + " with " + itemName(ID) + "?",true);
         if(bagStackArray[choiceListResult[1]] > 1)
         {
            outputMainText("\r\rYou will lose all " + bagStackArray[choiceListResult[1]] + " of " + itemName(choiceListResult[0]) + " if you do.",false);
         }
         buttonConfirm();
         doListen = function():void
         {
            if(buttonChoice == 6)
            {
               bagSlotClear(choiceListResult[1]);
               gainItem(ID);
            }
            if(buttonChoice == 7)
            {
               doDiscard(ID);
            }
         };
      }
      else if(!canLose(choiceListResult[0]))
      {
         outputMainText("Something is preventing you from removing the " + itemName(choiceListResult[0]) + ". You may have to unequip it first or it could be cursed!\r\rPlease choose something else.",true);
         doDiscard(ID);
      }
   };
}
!def ItemMove(slot:int):
   global moveItemID, moveItemStack, choicePage, bagArray, bagStackArray
   tempInt = moveItemID
   tempInt2 = moveItemStack
   tempI = slot + choicePage * 9 - 9
   if (slot < 4):
      tempI -= 1
   elif (slot < 8):
      tempI -= 2
   elif (slot < 12):
      tempI -= 3
   if (moveItemID == bagArray[tempI]) and (bagStackArray[tempI] < ItemStackMax(bagArray[tempI])):
      if ((moveItemStack + bagStackArray[tempI]) <= ItemStackMax(bagArray[tempI])):
         bagStackArray[tempI] += moveItemStack
         moveItemID = 0
         moveItemStack = 0
      else:
         moveItemStack -= ItemStackMax(bagArray[tempI]) - bagStackArray[tempI]
         bagStackArray[tempI] = ItemStackMax(bagArray[tempI])
   else:
      moveItemID = bagArray[tempI]
      moveItemStack = bagStackArray[tempI]
      bagArray[tempI] = tempInt
      bagStackArray[tempI] = tempInt2
      trace(tempI)
      trace(bagArray)
      trace(bagStackArray)
   if (moveItemID == 0):
      this.moveItem.visible = False
      this.moveItemAmount.visible = False
      this.MoveOutline.visible = False
      this.MoveAmountOutline.visible = False
   else:
      this.moveItem.visible = True
      this.MoveOutline.visible = True
      this.moveItem.htmlText = ItemName(moveItemID)
      if (moveItemStack > 1):
         this.moveItemAmount.visible = true
         this.moveItemAmount.htmlText = "" + moveItemStack + ""
         this.MoveAmountOutline.visible = true
   HideAmount()
   DoBag()

!def ShowMoveItem(which:Boolean):
{
   if(which == true)
   {
      if(this.moveItemID != 0)
      {
         this.moveItem.visible = true;
         this.MoveOutline.visible = true;
         if(this.moveItemStack > 1)
         {
            this.moveItemAmount.visible = true;
            this.MoveAmountOutline.visible = true;
         }
      }
   }
   else
   {
      this.moveItem.visible = false;
      this.moveItemAmount.visible = false;
      this.MoveOutline.visible = false;
      this.MoveAmountOutline.visible = false;
   }
}
def ItemName(ID:int):
   tempStr = "ITEM NAME ERROR " + ID
   if (ID == 0):
      tempStr = " "
   if (ID == 1):
      tempStr = "Test"
   if (ID == 101):
      tempStr = "Anc Claws"
   if (ID == 102):
      tempStr = "Imb Shoes"
   if (ID == 103):
      tempStr = "Dry Sand"
   if (ID == 104):
      tempStr = "Milker"
   if (ID == 105):
      tempStr = "Cat's Meow"
   if (ID == 106):
      tempStr = "Penis Pump"
   if (ID == 108):
      tempStr = "Blood Gge"
   if (ID == 109):
      tempStr = "Edu Egg"
   if (ID == 110):
      tempStr = "Reduction"
   if (ID == 111):
      tempStr = "Skin Balm"
   if (ID == 112):
      tempStr = "Bol Juice"
   if (ID == 113):
      tempStr = "Taint Leaf"
   if (ID == 114):
      tempStr = "Sweet Sap"
   if (ID == 115):
      tempStr = "Poultice"
   if (ID == 116):
      tempStr = "Dagger"
   if (ID == 117):
      tempStr = "Hammer"
   if (ID == 118):
      tempStr = "Saber"
   if (ID == 119):
      tempStr = "Whip"
   if (ID == 120):
      tempStr = "Neuter"
   if (ID == 121):
      tempStr = "TS Soft"
   if (ID == 122):
      tempStr = "TS Firm"
   if (ID == 123):
      tempStr = "TS Tied"
   if (ID == 124):
      tempStr = "TS Siz"
   if (ID == 125):
      tempStr = "TS Ovi"
   if (ID == 126):
      tempStr = "Oas Water"
   if (ID == 127):
      tempStr = "Tail Spike"
   if (ID == 128):
      tempStr = "TS Sanct"
   if (ID == 200):
      tempStr = "Lila's Gift"
   if (ID == 201):
      tempStr = "Milk C Pois"
   if (ID == 202):
      tempStr = "Co-Snak Ven"
   if (ID == 203):
      tempStr = "Wolf Fur"
   if (ID == 204):
      tempStr = "Sm Pouch"
   if (ID == 205):
      tempStr = "Sm Pouch"
   if (ID == 206):
      tempStr = "Trinket"
   if (ID == 207):
      tempStr = "Cock Carv"
   if (ID == 208):
      tempStr = "Blo Berry"
   if (ID == 209):
      tempStr = "Grain"
   if (ID == 210):
      tempStr = "Puss Fruit"
   if (ID == 211):
      tempStr = "DairE Pill"
   if (ID == 212):
      tempStr = "Red Mush"
   if (ID == 213):
      tempStr = "Wet Cloth"
   if (ID == 214):
      tempStr = "Lon Milk"
   if (ID == 215):
      tempStr = "Lon Pendant"
   if (ID == 216):
      tempStr = "Pink Ink"
   if (ID == 217):
      tempStr = "Egg Jelly"
   if (ID == 218):
      tempStr = "Bul Berry"
   if (ID == 219):
      tempStr = "Fresh Egg"
   if (ID == 220):
      tempStr = "Blondie"
   if (ID == 221):
      tempStr = "Puss Juice"
   if (ID == 222):
      tempStr = "Kinky Carr"
   if (ID == 223):
      tempStr = "Eq Snack"
   if (ID == 224):
      tempStr = "Lila's Milk"
   if (ID == 225):
      tempStr = "Body Wash"
   if (ID == 226):
      tempStr = "Felin Tea"
   if (ID == 227):
      tempStr = "Oral Wash"
   if (ID == 228):
      tempStr = "Body Oil"
   if (ID == 229):
      tempStr = "Leath Strap"
   if (ID == 230):
      tempStr = "Eggcelerator"
   if (ID == 231):
      tempStr = "Desi Sand"
   if (ID == 232):
      tempStr = "Flying Carp"
   if (ID == 233):
      tempStr = "A-Grav Rock"
   if (ID == 234):
      tempStr = "Rein Charm"
   if (ID == 235):
      tempStr = "Fell Rod"
   if (ID == 236):
      tempStr = "Recept Bell"
   if (ID == 237):
      tempStr = "Dewy Gift"
   if (ID == 238):
      tempStr = "Squ Cheese"
   if (ID == 239):
      tempStr = "Shiny Rock"
   if (ID == 240):
      tempStr = "Auburn Dye"
   if (ID == 241):
      tempStr = "Brown Dye"
   if (ID == 242):
      tempStr = "Grey Dye"
   if (ID == 243):
      tempStr = "White Dye"
   if (ID == 244):
      tempStr = "Snuggle Ball"
   if (ID == 245):
      tempStr = "Facial Mud"
   if (ID == 246):
      tempStr = "Fertile Gel"
   if (ID == 247):
      tempStr = "Supp Harness"
   if (ID == 248):
      tempStr = "Breeder Pot"
   if (ID == 249):
      tempStr = "Treant's Tear"
   if (ID == 250):
      tempStr = "Foomp Bomb"
   if (ID == 251):
      tempStr = "Plump Quat"
   if (ID == 252):
      tempStr = "Milky Pend"
   if (ID == 253):
      tempStr = "Bug Egg"
   if (ID == 254):
      tempStr = "Lantern"
   if (ID == 255):
      tempStr = "Frag Flower"
   if (ID == 256):
      tempStr = "Nectar Candy"
   if (ID == 257):
      tempStr = "Too Human"
   if (ID == 258):
      tempStr = "Tainted Pot"
   if (ID == 259):
      tempStr = "Sweet&Sour"
   if (ID == 260):
      tempStr = "Succ Draft"
   if (ID == 500):
      tempStr = "Milk Bottle"
   if (ID == 501):
      tempStr = "Milk Jug"
   if (ID == 502):
      tempStr = "Milk Barrel"
   if (ID == 503):
      tempStr = "Lust Draft"
   if (ID == 504):
      tempStr = "Rejuv Pot"
   if (ID == 505):
      tempStr = "Bad Exper"
   if (ID == 506):
      tempStr = "Exp Preg"
   if (ID == 507):
      tempStr = "Ball Sweller"
   if (ID == 508):
      tempStr = "S Lust Draft"
   if (ID == 509):
      tempStr = "S Rejuv Pot"
   if (ID == 510):
      tempStr = "S Bad Exper"
   if (ID == 511):
      tempStr = "S Exp Preg"
   if (ID == 512):
      tempStr = "S Ball Sweller"
   if (ID == 513):
      tempStr = "Gen Swap"
   if (ID == 514):
      tempStr = "Maso Pot"
   if (ID == 515):
      tempStr = "Black Dye"
   if (ID == 516):
      tempStr = "Baby Free"
   if (ID == 517):
      tempStr = "Pot Pot"
   if (ID == 518):
      tempStr = "S Gen Swap"
   if (ID == 519):
      tempStr = "S Maso Pot"
   if (ID == 520):
      tempStr = "Red Dye"
   if (ID == 521):
      tempStr = "S Baby Free"
   if (ID == 522):
      tempStr = "S Pot Pot"
   if (ID == 523):
      tempStr = "Cum Vial"
   if (ID == 524):
      tempStr = "Cum Bottle"
   if (ID == 525):
      tempStr = "Cum Jug"
   if (ID == 526):
      tempStr = "Cum Barrel"
   if (ID == 527):
      tempStr = "Good Egg"
   if (ID == 528):
      tempStr = "Bad Egg"
   if (ID == 529):
      tempStr = "Strange Egg"
   if (ID == 530):
      tempStr = "Charmed Egg"
   if (ID == 531):
      tempStr = "Divine Egg"
   if (ID == 532):
      tempStr = "Pheromone"
   if (ID == 533):
      tempStr = "Reduc Reduc"
   if (ID == 534):
      tempStr = "Male Enhance"
   if (ID == 535):
      tempStr = "Milk Suppress"
   if (ID == 536):
      tempStr = "Bazoomba!"
   if (ID == 537):
      tempStr = "Queen Egg"
   if (ID == 538):
      tempStr = "Soldier Egg"
   if (ID == 539):
      tempStr = "Drone Egg"
   if (ID == 540):
      tempStr = "Worker Egg"
   return tempStr

def ItemDescription(ID:int):
   global snuggleBall, suppHarness, tail
   tempStr = "ITEM DESCRIPTION ERROR " + ID
   if (ID == 101):
      tempStr = "Claws of the Lupine Ancestors" + "\n" + "\n" + "Harkening back to supposed Lupan ancestry, as long as this item remains in your bag, your hands will change into clawed paws that will help hold down your foes, just like the wolves of the forest." + "\n" + "\n" + "Although, in your case, it just gives you a bonus to Rape attempts..."
   if (ID == 102):
      tempStr = "Imbued Horseshoes" + "\n" + "\n" + "Crafted by the Equans of Firmshaft, these horseshoes help improve your running capabilities as long as they're in your bag. And they'll turn your feet into hooves."
   if (ID == 103):
      tempStr = "Magical Sands of the Dry Dunes" + "\n" + "\n" + "Applying this special sand to your genitalia will permanently make it a bit less moist than usual. Often used by the women of Siz'Calit when their heat makes them a little too moist. Or when they're producing a bit too much milk (though that's rarely the case in Siz'Calit)."
   if (ID == 104):
      tempStr = "Milking Machine" + "\n" + "\n" + "A compact device that produces enough suction to pump any breasts/udder you wish to collect the lactation of. Doing so will allow you to store the milk to be used or sold later, if you can produce enough. Comes with 2 hoses and multiple cups to work on almost any nipple/teat." + "\n" + "\n" + "Warning: Excessive use may result in permanent nipple/teat growth." + "\n" + "\n" + "Can only be used during Masturbation."
   if (ID == 105):
      tempStr = "'Cat's Meow' Potion" + "\n" + "\n" + "Favored by the Felins of Siz'Calit, this potion helps increase the production of breastmilk. Just try not to show off in Siz'Calit, or you may draw a crowd."
   if (ID == 106):
      tempStr = "Penis Pump" + "\n" + "\n" + "A simple device with an elastic cylinder that's intended to slip over a penis and pump it until it climaxes. Doing so will allow you to store the semen to be used or sold later, if you can produce enough." + "\n" + "\n" + "Can only be used during Masturbation."
   if (ID == 108):
      tempStr = "Blood Gauge" + "\n" + "\n" + "Due to their propensity to be swayed by outside blood, humans developed this nifty little gadget. Pressing it against your pulse, the magic of the device can detect the levels of racial influence in your body."
   if (ID == 109):
      tempStr = "Educated Eggdicator" + "\n" + "\n" + "With so many unfertilized eggs around the oasis, Lizan developed this to be able to tell a good egg from a bad egg. Even though an egg is just an egg beforehand, once put through this eggdicator its wave function collapses into a more determinable state." + "\n" + "\n" + "Warning: Using this item requires 1 Fresh Egg to operate."
   if (ID == 110):
      tempStr = "A Reduction of Reducer Agents" + "\n" + "\n" + "This is a powerful - yet often necessary in Nimin - elixer that, when rubbed on a part of your body, will permanently shrink that part to half its original size. Be careful!" + "\n" + "\n" + "Warning: This item is not useful against your enemies."
   if (ID == 111):
      tempStr = "Skin Balm" + "\n" + "\n" + "Used and created by the Humans of Softlik, this balm helps increase their skin's supplesness and other human attributes, as well as decrease those of other races."
   if (ID == 112):
      tempStr = "Bolstering Juice" + "\n" + "\n" + "This white 'juice' is often used and created by the Equans of Firmshaft. It helps strengthen their equan attributes and  decrease those of other races."
   if (ID == 113):
      tempStr = "Tainted Leaf" + "\n" + "\n" + "This paw-shaped leaf is farmed and used by the Lupans of Tieden to fend off the attributes of other races, usually the more violent ones, and increase their lupan strengths."
   if (ID == 114):
      tempStr = "Sweet Sap" + "\n" + "\n" + "Used and created by the Felins of Siz'Calit, this vial of clear liquid helps increase their felin sensitivities as well as ward off outside influences."
   if (ID == 115):
      tempStr = "Poultice" + "\n" + "\n" + "A generic swathe of cloth soaked in soothing balms, this poultice will heal 20 HP. It'll also make you a little aroused from rubbing it all over yourself..."
   if (ID == 116):
      tempStr = "Dagger" + "\n" + "\n" + "A relatively cheap weapon, the dagger is a nice way to defend oneself in Nimin." + "\n" + "\n" + "Base damage: 5-12"
   if (ID == 117):
      tempStr = "Warhammer" + "\n" + "\n" + "A rather blunt weapon, it's a bit unwieldy but gets the job done." + "\n" + "\n" + "Base damage: 2-20"
   if (ID == 118):
      tempStr = "Saber" + "\n" + "\n" + "A well-designed blade, the saber can deal significant damage to foes." + "\n" + "\n" + "Base damage: 10-25"
   if (ID == 119):
      tempStr = "Whip" + "\n" + "\n" + "A somewhat kinky weapon, the whip can leave some rather nasty welts." + "\n" + "\n" + "Base damage: 12-18"
   if (ID == 120):
      tempStr = "Neuterizer" + "\n" + "\n" + "Developed by the Lupans of Tieden, this isn't actually intended to be used on most of their inhabitants. Instead, it was created as a post-defensive measure against the... oddities of Nimin."
   if (ID == 121):
      tempStr = "Teleport Scroll: Softlik" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Softlik." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 122):
      tempStr = "Teleport Scroll: Firmshaft" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Firmshaft." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 123):
      tempStr = "Teleport Scroll: Tieden" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Tieden." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 124):
      tempStr = "Teleport Scroll: Siz'Calit" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Siz'Calit." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 125):
      tempStr = "Teleport Scroll: Oviasis" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Oviasis." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 126):
      tempStr = "Oasis Water" + "\n" + "\n" + "A vial of the fresh water from the oasis in the lizan city of Oviasis, it helps the residents cool off and moisten their scales so they can hunt and sunbathe more, as well as ward off the influences of other races."
   if (ID == 127):
      tempStr = "Tail Spike" + "\n" + "\n" + "This large spike is held firm upon leather straps. When attached to a tail, it can be used as a rather effective weapon." + "\n" + "\n" + "Base damage: 10-20" + "\n" + "\n" + "Requirement: Must have a muscular/skeletal tail to equip (tails of hair or excessively fluffy tails will not work)."
   if (ID == 128):
      tempStr = "Teleport Scroll: Sanctuary" + "\n" + "\n" + "Created for an easy return, this scroll of teleportation will instantly return the user to the city of Sanctuary." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
   if (ID == 200):
      tempStr = "Lila's Gift" + "\n" + "\n" + "A small charm given to you by the young felin girl in Siz'Calit, it seems to be pretty decoration made from flowers and leaves and some other cute little things. However, as you hold it, you notice it makes you wetter down under... This might have been the reason the girl was so wet to begin with, or maybe her extreme wetness for such a young age rubbed off onto her charm? Either way, as long as you carry it, you'll be wetter than usual. And you seem much more sensitive than usual..." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
   if (ID == 201):
      tempStr = "Milk Creeper Poison" + "\n" + "\n" + "Obtained from a passed out Milk Creeper, this poison is a bit diluted from her ingestion from so much of your milk. It is unlikely that it will affect your lactation rate directly like the pure poison does, but rubbing it into your mammary glands will cause them to swell slightly larger."
   if (ID == 202):
      tempStr = "Cock-Snake Venom" + "\n" + "\n" + "Obtained from the fangs of a passed out cock-snake, this venom is a potent male enhancement. And if you aren't male when you use it, you will be, if at least partially..."
   if (ID == 203):
      tempStr = "Tuft of Wolf Fur" + "\n" + "\n" + "Obtained from an encounter with a feral wolf, a tuft of their fur has been known to decrease sensitivity, and thus increase your toughness against attacks, when rubbed onto your " + SkinDesc() + "."
   if (ID == 204):
      tempStr = "Small Pouch" + "\n" + "\n" + "This is a small pouch you have obtained somewhere. Use it to see what it contains!"
   if (ID == 205):
      tempStr = "Small Pouch" + "\n" + "\n" + "This is a small pouch you have obtained somewhere. Use it to see what it contains!"
   if (ID == 206):
      tempStr = "Shiny Trinket" + "\n" + "\n" + "Other than being a pretty decoration, this thing isn't much use to you. However, it probably sells fairly well."
   if (ID == 207):
      tempStr = "Wooden Cock Carving" + "\n" + "\n" + "This thing looks like a dildo made of wood, with decorated carvings all around. It sounds hollow, so maybe you could break it open and see if anything is inside?"
   if (ID == 208):
      tempStr = "Bloated Berry" + "\n" + "\n" + "A berry from across the ocean, it looks oddly bloated, nearly two berries in one. It seems edible though."
   if (ID == 209):
      tempStr = "Handful of Grain" + "\n" + "\n" + "A handful of fresh grain, it smells slightly sweet in your hands. Eating it will provide you some energy from the carbs!"
   if (ID == 210):
      tempStr = "Pussy Fruit" + "\n" + "\n" + "It is unknown whether the name derives from the cat-like felin people that enjoy this fruit or from the fruit's rather... lewd shape. Either way, it is a very sweet and juicy fruit that felin females love."
   if (ID == 211):
      tempStr = "DairE Pill" + "\n" + "\n" + "Produced by the farmers of the Dairy Farm outside of Softlik, this pill supposedly helps increase the lactation rate of dairy cows. It is not suggested to be ingested by anything other than cows, though that's just a suggestion."
   if (ID == 212):
      tempStr = "Red Mushroom" + "\n" + "\n" + "An odd looking mushroom with a red cap with a few white dots found on the walls of the Old Cave. You're not really sure what it does, but you think you'll get bigger so you can smash some blocks... or something."
   if (ID == 213):
      tempStr = "Wet, Slimy Cloth" + "\n" + "\n" + "This piece of white cloth seems to be perpetually wet and slimy, no matter how long you keep it in your bag. You have no idea what it can do, however."
   if (ID == 214):
      tempStr = "Malon's Milk" + "\n" + "\n" + "Unlike the other bottles of milk that come from the Dairy Farm, this wasn't from a cow. From Malon's own supply, you're unsure exactly how it's different from the rest, though it does taste better."
   if (ID == 215):
      tempStr = "Malon's Pendant" + "\n" + "\n" + "Given to you by Malon from the Dairy Farm, this gift of admiration seems to have been a keepsake of hers since she was a child and has imbued by her long-time love of animals and rather bovine qualities. As long as you hold onto it, everything is a bit more consensual towards being 'raped', be a bit more lenient to you running away, and all milk products heal you slightly more than usual." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
   if (ID == 216):
      tempStr = "Pink Ink" + "\n" + "\n" + "Octopus ink gained from a rather pink octopus girl, this ink serves as a very rare and valuable hair dye. Should you use it, your hair will turn a coral pink color, if you have hair."
   if (ID == 217):
      tempStr = "Octopus Egg Jelly" + "\n" + "\n" + "The jelly from the eggs of the octopus girls you gave birth to, it seems like it'd make you very aroused if you rubbed it on your genitals. Although, you're not quite sure what it would do beyond that..."
   if (ID == 218):
      tempStr = "Bulging Berry" + "\n" + "\n" + "A cousin of the bloated berry, this fruit splits into multiple spheres from the same stem, somewhat like cherries but can often have three of four from the same stem. It is quite edible, though it is highly suggested to not eat many."
   if (ID == 219):
      tempStr = "Fresh Egg" + "\n" + "\n" + "An unfertilized egg from a lizan female (or herm), eggs like this are common in the lizan diet. High in protein, they're good for your health."
   if (ID == 220):
      tempStr = "Blonde Dye" + "\n" + "\n" + "A dye made from mashed grain, this will turn your hair blonde in color when used, if you have hair, or it can be sold for a decent sum."
   if (ID == 221):
      tempStr = "Concentrated Pussy Fruit Juice" + "\n" + "\n" + "Created by a notable mistress in Siz'calit, this vial contains some rather concentrated juice from the Pussy Fruit. It is likely to have a notable effect on a woman's loins, more potent than its source."
   if (ID == 222):
      tempStr = "Kinky Carrot" + "\n" + "\n" + "Used in lewd fashions by a small rabbit-like people, you're sure to clean this off as soon as you got it. Although you're not entirely certain what would happen if you ate it, besides being in better health for keeping veggies in your diet."
   if (ID == 223):
      tempStr = "Equan Snack" + "\n" + "\n" + "A common snack amongst the equan people, this sweet little thing has the kind of carbs that will help you get through the day, no matter what life may put on your shoulders. And it seems to be the cause of some bellies of some equan women..."
   if (ID == 224):
      tempStr = "Lila's Milk" + "\n" + "\n" + "From the ample supply of a certain little felin girl, this milk seems to be a tad sweeter than normal milk and also slightly tainted by the poor girl's constant heat."
   if (ID == 225):
      tempStr = "Body Wash" + "\n" + "\n" + "This nice body wash is scented like a meadow of flowers. It can help clean up some dirty thoughts and make your body feel much fresher."
   if (ID == 226):
      tempStr = "Felin Tea Mix" + "\n" + "\n" + "A common brew amongst felins, this tea helps calm the body and mind. Especially the body, which is often necessary for Felins..."
   if (ID == 227):
      tempStr = "Felin Oral Wash" + "\n" + "\n" + "With bath by licking being commonplace amongst felins, this wash is to aid in such endeavors. Delightfully tingly, this stuff will leave both your breath and your fur feeling fresh."
   if (ID == 228):
      tempStr = "Body Oil" + "\n" + "\n" + "Nice and slick, this stuff is great for your skin or scales and makes you look quite shiny and alluring for the next 5 hours."
   if (ID == 229):
      tempStr = "Leather Strap" + "\n" + "\n" + "Found somewhere in Silandrias' den, this leather strap seems to be fitted to tie tightly around the base of her tail. Otherwise, you have no idea what it could be for."
   if (ID == 230):
      tempStr = "Eggcelerator" + "\n" + "\n" + "Meant to temporarily increase the rate of egg production in Lizan females, this pill looks to be a little egg-shaped itself, with more of a torpedo-like tip. This pill also seems to be too large to be ingested orally by the average person, which you deduct means it's meant as a suppository... Though, considering its nature, it's safe to say it's not meant to be administered anally, at least." + "\n" + "\n" + "Its effect stacks."
   if (ID == 231):
      tempStr = "Desiccating Sand" + "\n" + "\n" + "Obtained from a sentient dust devil, this sand is specially imbued with the ability to suck moisture from a body. Though the Dust Devil only uses it to feed, in this quantity it can be rather damaging if thrown at an enemy all at once. Be wary of blow-back, though." + "\n" + "\n" + "This item can only be used during battle."
   if (ID == 232):
      tempStr = "Flying Carpet" + "\n" + "\n" + "Borrowed from Silandrias, this flying carpet can take you on a magical ride to see a whole new world. However, it can only take you to towns you have already found, since you wouldn't know how to guide it someplace you haven't been, so the whole 'new' aspect is rather moot. But it is still quite convenient!" + "\n" + "\n" + "You cannot activate the flying carpet in amidst the heat of battle or amidst the heat of masturbation."
   if (ID == 233):
      tempStr = "Anti-Gravity Rock" + "\n" + "\n" + "Borrowed from Silandrias, this small rock, more of a pebble really, just kind of floats there and defies gravity. Yet, as you carry it, even you seem to defy gravity to a degree. You feel much lighter on your " + LegDesc(10) + " and your carry capacity increases by a whole 75! '75 what', you have no idea, but it's a big number so it's got to be good, right?"
   if (ID == 234):
      tempStr = "Reindeer Charm" + "\n" + "\n" + "Borrowed from Silandrias, this sapphire charm is carved into the shape of a reindeer's head, with large antlers. Carrying it imbues you with the essence of a reindeer mother, providing you with a nice set of antlers and a matching deer-butt, as well as speeding up your pregnancies and increasing your minimum lust, urging you to give birth to plenty of children."
   if (ID == 235):
      tempStr = "Fellatio Rod" + "\n" + "\n" + "Borrowed from Silandrias, this rather phallic rod is actually a weapon. When the base is pointed at the target, you can siphon out some of their life force by placing your lips around the bulbous end of the rod and gently sucking. If you're very skilled, you can make the weapon perform even stronger. It even ignores their natural resistance to physical attacks."
   if (ID == 236):
      tempStr = "Reception Bell" + "\n" + "\n" + "Borrowed from Silandrias, this small cowbell is worn around the neck and makes one more receptive to outside influences. In other words, the wearer gains 50% more SexP than usual *ding*. They also tend to be 30% more susceptible to blood-changes though... *dong*"
   if (ID == 237):
      tempStr = "Lila's Dewy Gift" + "\n" + "\n" + "Originally given to you by Lila, dew drops have started forming on and falling from the leaves and flowers constantly, ever since it became more 'infused' with your relationship with Lila. As long as you hold it, you're sexual lubrication flows much more and makes you quite sensitive. It even feels warm to the touch, a warmth that sometimes may spread to you..." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
   if (ID == 238):
      tempStr = "Squeaky Cheese" + "\n" + "\n" + "Some cheese found in an alley that kinda squeaks when you rub it, it smells quite delicious and would help restore your energy if you're hurt. Other than that, though, well... you did find it in an alley, after all."
   if (ID == 239):
      tempStr = "Shiny Rock" + "\n" + "\n" + "A rather shiny rock you found, you're almost intent at staring at it. If anything, it at least improves your focus."
   if (ID == 240):
      tempStr = "Auburn Dye" + "\n" + "\n" + "A dark reddish color, this dye will turn your hair auburn when used, if you have hair"
   if (ID == 241):
      tempStr = "Brown Dye" + "\n" + "\n" + "A simple brownish, this dye will turn your hair brown when used, if you have hair"
   if (ID == 242):
      tempStr = "Grey Dye" + "\n" + "\n" + "A shade, this dye will turn your hair grey when used, if you have hair"
   if (ID == 243):
      tempStr = "White Dye" + "\n" + "\n" + "Lacking any color, this dye will turn your hair pure white when used, if you have hair"
   if (ID == 244) and (snuggleBall == False):
      tempStr = "Snuggle Ball" + "\n" + "\n" + "Squishy and plush, this odd ball is made out of seemingly unnatural materials. Almost like a living liquid, it wobbles around in your hand and is slightly pliable. It feels so pleasant, you kinda want to snuggle with it."
   elif (ID == 244):
      tempStr = "Snuggle Ball" + "\n" + "\n" + "Not really a 'ball' at the moment, this squishy thing is currently coating your body with a thick plush layer of shiny snuggliness. You can attempt to take it off, though it does make you look kinda cute, like a cuddly toy."
   if (ID == 245):
      tempStr = "Facial Mud" + "\n" + "\n" + "Some mud you found at a secluded mudhole in the savanna, this particular mud is quite clean and rich in minerals and would really help your complexion."
   if (ID == 246):
      tempStr = "Fertile Gel" + "\n" + "\n" + "A soft gel that gives off a pleasant warmth, it helps increase the fertility of women who want to be mothers or want a nice big swollen belly." + "\n" + "\n" + "Extra doses extend the duration of the gel."
   if (ID == 247):
      tempStr = "Support Harness" + "\n" + "\n" + "This contraption of straps and slings can be equipped to help support all those sizable appendages. Like a bra, except for the whole body!"
   if (ID == 247) and (suppHarness == True):
      tempStr += "\n" + "\n" + "You currently have a harness equipped. Using it will unequip the harness."
   if (ID == 248):
      tempStr = "Breeder Potion" + "\n" + "\n" + "This potion is normally used by animal breeders to increase the litter sizes of their animals and make their animals more frequently fertily receptive."
   if (ID == 249):
      tempStr = "Treant's Tear" + "\n" + "\n" + "This small tear-shaped piece of wood looks almost like a seed. However, across its surface are etched images of tree-like beings losing their limbs as they dance around the tear, progressively larger and larger with the more limbs they have lost. It's like some sort of ancient ritual, one you have never heard of..."
   if (ID == 250):
      tempStr = "Foomp Bomb" + "\n" + "\n" + "Much like a smoke bomb, this small ball can be tossed at an enemy to provide you an immediate escape from battle." + "\n" + "\n" + "This item can only be used during battle. This item will automatically successfully run from battle."
   if (ID == 251):
      tempStr = "Plump Quat" + "\n" + "\n" + "The quats is a very delicious fruit, so plump and ripe and full of mmm-mmm-goodness."
   if (ID == 252):
      tempStr = "Malon's Milky Pendant" + "\n" + "\n" + "This is the pendant Malon had given you, except now infused with a sort of milky complexion that ensures you'll always share her milky tendancies as long as you hold it, supporting your relationship as a couple of drippy cows~ It still seems to retain all the properties it had before as well."
   if (ID == 253):
      tempStr = "Bug Egg" + "\n" + "\n" + "Relatively small, this squishy unfertilized egg seems rather gooey. You could eat it, but the thought of doing so is somewhat nasty."
   if (ID == 253) and (tail == 12):
      tempStr += "\n" + "\n" + "However, you do notice that the egg is just about the right size for the ovipositor hanging off your backside."
   if (ID == 254):
      tempStr = "Lantern" + "\n" + "\n" + "This is a fairly basic lantern that you found at the hidden entrance below the ground in the valley. And though it might be basic and have no other function, the light it gives off can help you access areas that are otherwise too dark."
   if (ID == 255):
      tempStr = "Fragrant Flower" + "\n" + "\n" + "A very pleasant smelling flower whose petals are black with white stripes. If you took a good whiff, it would likely help hone your senses a bit."
   if (ID == 256):
      tempStr = "Nectar Candy" + "\n" + "\n" + "A sweet treat that bugs seem to swarm if not stored properly. It bolsters your muscles and helps egg laying."
   if (ID == 257):
      tempStr = "Too Human Potion" + "\n" + "\n" + "This potion was made to help the humans of Softlik regain some of their human attributes. However, this batch was apparently a failure for being too effective, somehow?"
   if (ID == 258):
      tempStr = "Tainted Potion" + "\n" + "\n" + "This potion was tainted by your DairE Pill, so you don't really know what it will do until you ingest it."
   if (ID == 259):
      tempStr = "Sweet & Sour Candy" + "\n" + "\n" + "This rare little treat is a favorite among many, if you can find it. It's that the sweetness is so sweet that you'll drop from the bliss and that the sourness is so sour that you'll suck yourself in."
   if (ID == 260):
      tempStr = "Succubus Draft" + "\n" + "\n" + "One of the glowing vials from the succubus, this is some concentrated masculinity that has been drained from various people, quite possibly even yourself. For her, it's a source of food and power, for you... the effects are probably different."
   if (ID == 500):
      tempStr = "Bottle of Milk" + "\n" + "\n" + "A bottle of delicious milk that, when drunk, will heal 10 HP and help you stay awake a little longer."
   if (ID == 501):
      tempStr = "Jug of Milk" + "\n" + "\n" + "A large jug of delicious milk that, when drunk, will heal 40 HP and help you stay awake a while longer. When you're done peeing, of course."
   if (ID == 502):
      tempStr = "Barrel of Milk" + "\n" + "\n" + "A barrel full of delicious milk, this is mostly meant to be used for easy handling by merchants. However, if you use it, you will gain 4 Jugs of Milk instantly."
   if (ID == 503):
      tempStr = "Lust Draft" + "\n" + "\n" + "A potion that will increase your lust by 20 instantly when used."
   if (ID == 504):
      tempStr = "Rejuvenating Potion" + "\n" + "\n" + "A potion that will heal 30 HP and reduce your lust by 15 instantly when used."
   if (ID == 505):
      tempStr = "Bad Experiment" + "\n" + "\n" + "This combustable concoction will deal 10-20 damage to your enemy before they can react!" + "\n" + "\n" + "This item can only be used during battle."
   if (ID == 506):
      tempStr = "Express Pregnancy Potion" + "\n" + "\n" + "When that baby is taking a while to gestate, this potion up the pregnancy as though 50 hours had passed."
   if (ID == 507):
      tempStr = "Ball Sweller" + "\n" + "\n" + "Imbibing this will make your balls feel as though you hadn't ejaculated in 30 hours."
   if (ID == 508):
      tempStr = "Superior Lust Draft" + "\n" + "\n" + "A potion that will increase your lust by 50 instantly when used."
   if (ID == 509):
      tempStr = "Superior Rejuvenating Potion" + "\n" + "\n" + "A potion that will heal 70 HP and reduce your lust by 40 instantly when used."
   if (ID == 510):
      tempStr = "Super Bad Experiment" + "\n" + "\n" + "This extremely combustable concoction will deal 20-40 damage to your enemy before they can react!" + "\n" + "\n" + "This item can only be used during battle."
   if (ID == 511):
      tempStr = "Superior Express Pregnancy Potion" + "\n" + "\n" + "When that baby is taking a while to gestate, this potion up the pregnancy as though 120 hours had passed."
   if (ID == 512):
      tempStr = "Superior Ball Sweller" + "\n" + "\n" + "Imbibing this will make your balls feel as though you hadn't ejaculated in 70 hours."
   if (ID == 513):
      tempStr = "Gender Swap Potion" + "\n" + "\n" + "If you want to try out the opposite sex, this potion will revert your genitals back to infancy, allowing them to reform as their opposite counterparts. If a hermaphrodite takes this, it reverts all genitals to their smallest value. If a genderless person takes this, the resulting gender is random."
   if (ID == 514):
      tempStr = "Masochism Potion" + "\n" + "\n" + "After this potion is imbibed, your nervous system confuses half of all damage as pleasure for a whole day."
   if (ID == 515):
      tempStr = "Black Dye" + "\n" + "\n" + "This will turn your hair black in color when used, if you have hair."
   if (ID == 516):
      tempStr = "Baby Free Potion" + "\n" + "\n" + "Sipping this potion will reduce your chance of becoming pregnancy by 50% fr the next 3 days. This contraceptive is not gauranteed to prevent pregnancy, especially if you're especially fertile. It will work whether you have the appropriate plumbing or not. Multiple instances of Baby Free Potion will only extend the time of its duration, not increase the reduction in chance."
   if (ID == 517):
      tempStr = "Potency Potion" + "\n" + "\n" + "Kicking your balls into gear, they will permanently produce 20% more cum, despite their size."
   if (ID == 518):
      tempStr = "Superior Gender Swap Potion" + "\n" + "\n" + "If you want to try out the opposite sex, this potion will transform your genitals into their opposite counterparts, retaining the relative size. If a hermaphrodite takes this, the genitals swap sizes. If a genderless person takes this, the resulting gender is random, along with the sizes of their genitals (up to a certain amount)."
   if (ID == 519):
      tempStr = "Superior Masochism Potion" + "\n" + "\n" + "After this potion is imbibed, your nervous system confuses all damage as pleasure for a whole day."
   if (ID == 520):
      tempStr = "Red Dye" + "\n" + "\n" + "This will turn your hair red in color when used, if you have hair."
   if (ID == 521):
      tempStr = "Superior Baby Free Potion" + "\n" + "\n" + "Sipping this potion will reduce your chance of becoming pregnancy by 50% for the next 9 days. This contraceptive is not gauranteed to prevent pregnancy, especially if you're especially fertile. It will work whether you have the appropriate plumbing or not. Multiple instances of Superior Baby Free Potion will only extend the time of its duration, not increase the reduction in chance."
   if (ID == 522):
      tempStr = "Superior Potency Potion" + "\n" + "\n" + "Drop-kicking your balls into gear, they will permanently produce 50% more cum, despite their size."
   if (ID == 523):
      tempStr = "Vial of Cum" + "\n" + "\n" + "Still kinda warm, this vial of goop will arouse you slightly when imbibed, plus heal a bit."
   if (ID == 524):
      tempStr = "Bottle of Cum" + "\n" + "\n" + "A bottle of warm cum that will arouse you and heal you slightly when imbibed. If you can get it all down."
   if (ID == 525):
      tempStr = "Jug of Cum" + "\n" + "\n" + "A jug full of hot cum, this is mostly meant to be used for easy handling by the merchants that might be able to find a use for it. However, if you use it, you will gain 3 Bottles of Cum instantly."
   if (ID == 526):
      tempStr = "Barrel of Cum" + "\n" + "\n" + "There's... not really much you can do with a barrel full of hot cum. The merchants will still buy it, but at a very low price, since there's not much they can do with it either..."
   if (ID == 527):
      tempStr = "Good Egg" + "\n" + "\n" + "An unfertilized fresh egg that is especially good for your health and body."
   if (ID == 528):
      tempStr = "Bad Egg" + "\n" + "\n" + "An unfertilized fresh egg that should never be eaten... Instead it can be thrown at your enemy for a quick 10-20 damage." + "\n" + "\n" + "This item can only be used during battle."
   if (ID == 529):
      tempStr = "Strange Egg" + "\n" + "\n" + "An unfertilized fresh egg that can do... odd things to your body."
   if (ID == 530):
      tempStr = "Charmed Egg" + "\n" + "\n" + "An unfertilized fresh egg that will make you quite alluring for 20 hours."
   if (ID == 531):
      tempStr = "Divine Egg" + "\n" + "\n" + "A very rare unfertilized fresh egg, eating it will make you closer to a diety of fertility."
   if (ID == 532):
      tempStr = "Strong Pheromone" + "\n" + "\n" + "Originally meant to be fishing bait, this concoction is much more potent than originally intended and attracts far more than fish for 30 hours..."
   if (ID == 533):
      tempStr = "Reduced Reduction" + "\n" + "\n" + "A weaker form of a Reduction, this will shrink the desired body part by a regular amount instead of halving its size."
   if (ID == 534):
      tempStr = "Male Enhancement Drug" + "\n" + "\n" + "A simple pill that, when ingested, will increase the size of you male genitals." + "\n" + "\n" + "Caution: females taking this pill may have similar side-effects."
   if (ID == 535):
      tempStr = "Milk Suppressant" + "\n" + "\n" + "This drug will prevent any milk from leaking from your body. It does not prevent your mammary glands from producing milk, but it does prevent the milk from escaping for its duration, avoiding most unsightly leaks."
   if (ID == 536):
      tempStr = "Bazoomba!" + "\n" + "\n" + "This glowing squishy orb is a secret recipe that creates more of one of the best things in life when ingested...!" + "\n" + "\n" + "Warning - Be wary of overload."
   if (ID == 537):
      tempStr = "Queen Egg" + "\n" + "\n" + "Not the egg of a queen, but rather an unfertilized egg fit for a queen! This wonderful egg would make any queen's abdomen larger and sexier. Though, if you're not an insect, this mostly translates to things below the waist. It will also help shorten the gestation period for quicker offspring and help your breasts hold more milk for all those births."
   if (ID == 538):
      tempStr = "Soldier Egg" + "\n" + "\n" + "Not the egg of a soldier, but rather an unfertilized egg suitable for a soldier. This powerful egg will make you taller, stronger, and more physically fit just by eating it!"
   if (ID == 539):
      tempStr = "Drone Egg" + "\n" + "\n" + "Not the egg of a drone, but rather an unfertilized egg better fed to the sex-craving drones, those mindless males that are only useful for impregnating a queen. This will make them even better at that singular duty."
   if (ID == 540):
      tempStr = "Worker Egg" + "\n" + "\n" + "Not the egg of a worker, but rather an unfertilized egg that would help any worker. Munching down this little thing will help anybody feel less exhausted and thus allow them to work even more!"
   return tempStr

def UsableItem(ID:int):
   tempBool = False
   if (ID == 104):
      tempBool = True
   if (ID == 106):
      tempBool = True
   if (ID == 108):
      tempBool = True
   if (ID == 109):
      tempBool = True
   if (ID == 116):
      tempBool = True
   if (ID == 117):
      tempBool = True
   if (ID == 118):
      tempBool = True
   if (ID == 119):
      tempBool = True
   if (ID == 127):
      tempBool = True
   if (ID == 232):
      tempBool = true
   if (ID == 235):
      tempBool = True
   if (ID == 244):
      tempBool = True
   if (ID == 247):
      tempBool = True
   return tempBool

def CanLose(ID:int):
   global snuggleBall, suppHarness
   tempBool = True
   if (ID == 244) and (CountItem(244) == 1) and (snuggleBall == True):
      tempBool = False
   if (ID == 247) and (CountItem(247) == 1) and (suppHarness == True):
      tempBool = False
   return tempBool

def ConItem(ID:int):
   tempBool = False
   if (ID == 103):
      tempBool = True
   if (ID == 105):
      tempBool = True
   if (ID == 110):
      tempBool = True
   if (ID == 111):
      tempBool = True
   if (ID == 112):
      tempBool = True
   if (ID == 113):
      tempBool = True
   if (ID == 114):
      tempBool = True
   if (ID == 115):
      tempBool = True
   if (ID == 120):
      tempBool = True
   if (ID == 121):
      tempBool = True
   if (ID == 122):
      tempBool = True
   if (ID == 123):
      tempBool = True
   if (ID == 124):
      tempBool = True
   if (ID == 125):
      tempBool = True
   if (ID == 126):
      tempBool = True
   if (ID == 128):
      tempBool = True
   if (ID == 201):
      tempBool = True
   if (ID == 202):
      tempBool = True
   if (ID == 203):
      tempBool = True
   if (ID == 204):
      tempBool = True
   if (ID == 205):
      tempBool = True
   if (ID == 207):
      tempBool = True
   if (ID == 208):
      tempBool = True
   if (ID == 209):
      tempBool = True
   if (ID == 210):
      tempBool = True
   if (ID == 211):
      tempBool = True
   if (ID == 212):
      tempBool = True
   if (ID == 213):
      tempBool = True
   if (ID == 214):
      tempBool = True
   if (ID == 216):
      tempBool = True
   if (ID == 217):
      tempBool = True
   if (ID == 218):
      tempBool = True
   if (ID == 219):
      tempBool = True
   if (ID == 220):
      tempBool = True
   if (ID == 221):
      tempBool = True
   if (ID == 222):
      tempBool = True
   if (ID == 223):
      tempBool = True
   if (ID == 224):
      tempBool = True
   if (ID == 225):
      tempBool = True
   if (ID == 226):
      tempBool = True
   if (ID == 227):
      tempBool = True
   if (ID == 228):
      tempBool = True
   if (ID == 230):
      tempBool = True
   if (ID == 231):
      tempBool = True
   if (ID == 238):
      tempBool = True
   if (ID == 239):
      tempBool = True
   if (ID == 240):
      tempBool = True
   if (ID == 241):
      tempBool = True
   if (ID == 242):
      tempBool = True
   if (ID == 243):
      tempBool = True
   if (ID == 245):
      tempBool = True
   if (ID == 246):
      tempBool = True
   if (ID == 248):
      tempBool = True
   if (ID == 249):
      tempBool = True
   if (ID == 250):
      tempBool = True
   if (ID == 251):
      tempBool = True
   if (ID == 253):
      tempBool = True
   if (ID == 255):
      tempBool = True
   if (ID == 256):
      tempBool = True
   if (ID == 257):
      tempBool = True
   if (ID == 258):
      tempBool = True
   if (ID == 259):
      tempBool = True
   if (ID == 260):
      tempBool = True
   if (ID == 500):
      tempBool = True
   if (ID == 501):
      tempBool = True
   if (ID == 502):
      tempBool = True
   if (ID == 503):
      tempBool = True
   if (ID == 504):
      tempBool = True
   if (ID == 505):
      tempBool = True
   if (ID == 506):
      tempBool = True
   if (ID == 507):
      tempBool = True
   if (ID == 508):
      tempBool = True
   if (ID == 509):
      tempBool = True
   if (ID == 510):
      tempBool = True
   if (ID == 511):
      tempBool = True
   if (ID == 512):
      tempBool = True
   if (ID == 513):
      tempBool = True
   if (ID == 514):
      tempBool = True
   if (ID == 515):
      tempBool = True
   if (ID == 516):
      tempBool = True
   if (ID == 517):
      tempBool = True
   if (ID == 518):
      tempBool = True
   if (ID == 519):
      tempBool = True
   if (ID == 520):
      tempBool = True
   if (ID == 521):
      tempBool = True
   if (ID == 522):
      tempBool = True
   if (ID == 523):
      tempBool = True
   if (ID == 524):
      tempBool = True
   if (ID == 525):
      tempBool = True
   if (ID == 526):
      tempBool = True
   if (ID == 527):
      tempBool = True
   if (ID == 528):
      tempBool = True
   if (ID == 529):
      tempBool = True
   if (ID == 530):
      tempBool = True
   if (ID == 531):
      tempBool = True
   if (ID == 532):
      tempBool = True
   if (ID == 533):
      tempBool = True
   if (ID == 534):
      tempBool = True
   if (ID == 535):
      tempBool = True
   if (ID == 536):
      tempBool = True
   if (ID == 537):
      tempBool = True
   if (ID == 538):
      tempBool = True
   if (ID == 539):
      tempBool = True
   if (ID == 540):
      tempBool = True
   return tempBool

def PassiveItemAdd(ID:int):
   global rapeMod, runMod, vagMoistMod, cockMoistMod, milkHPMod, carryMod, pregRate, minLust, hips, sexPMod, changeMod, heatMaxTime, heatTimeMod, heatMod, milkCap
   if (ID == 101):
      rapeMod += 10
   if (ID == 102):
      runMod += 20
   if (ID == 200):
      vagMoistMod += 4
      cockMoistMod += 4
      StatsMod(0,0,0,10)
   if (ID == 215):
      rapeMod += 5
      runMod += 5
      milkHPMod += 5
   if (ID == 233):
      carryMod += 75
   if (ID == 234):
      pregRate += 0.5
      minLust += 10
      hips += 10
      doLust(0,0)
   if (ID == 236):
      SexPMod += 0.5
      changeMod += 0.3
   if (ID == 237):
      vagMoistMod += 8
      cockMoistMod += 8
      StatsMod(0,0,0,10)
      if (heat < 1):
         heatMaxTime = 96
         heatTime = 96
         heat += 1
      elif (heat >= 1):
         heatMaxTime -= 12
         heat += 1
   if (ID == 252):
      rapeMod += 5
      runMod += 5
      milkHPMod += 5
      carryMod += 10
      milkCap += 3000

def PassiveItemRemove(ID:int):
   global rapeMod, runMod, vagMoistMod, cockMoistMod, milkHPMod, carryMod, pregRate, minLust, hips, sexPMod, changeMod, heatMaxTime, heat, milkCap, weapon
   if (ID == 101):
      rapeMod -= 10
   if (ID == 102):
      runMod -= 20
   if (ID == 200):
      vagMoistMod -= 4
      cockMoistMod -= 4
      StatsMod(0,0,0,-10)
   if (ID == 215):
      rapeMod -= 5
      runMod -= 5
      milkHPMod -= 5
   if (ID == 233):
      carryMod -= 75
   if (ID == 234):
      pregRate -= 0.5
      minLust -= 10
      hips -= 10
   if (ID == 236):
      SexPMod -= 0.5
      changeMod -= 0.3
   if (ID == 237):
      vagMoistMod -= 8
      cockMoistMod -= 8
      StatsMod(0,0,0,-10)
      if (heat >= 2):
         heatMaxTime += 12
      heat -= 1
   if (ID == 252):
      rapeMod -= 5
      runMod -= 5
      milkHPMod -= 5
      carryMod -= 10
      milkCap -= 3000
   if (ID == 116) and (weapon == 116):
      weapon = 10
   if (ID == 117) and (weapon == 117):
      weapon = 10
   if (ID == 118) and (weapon == 118):
      weapon = 10
   if (ID == 119) and (weapon == 119):
      weapon = 10
   if (ID == 127) and (weapon == 127):
      weapon = 10
   if (ID == 235) and (weapon == 235):
      weapon = 10

def LoseManyItem(ID:int, amount:int):
   global bagArray, bagStackArray
   for i in (0, 26):
   #for(this.i = this.bagArray.length; this.i >= 0; --this.i)
      if bagArray[i] == ID and amount > 0:
         if amount >= bagStackArray[i]:
            PassiveItemRemove(bagArray[i])
            bagArray[i] = 0
            amount -= bagStackArray[i]
            bagStackArray[i] = 0
         else:
            bagStackArray[i] -= amount
            amount = 0

def ItemValue(ID:int):
   tempNum = 0
   if (ID == 1):
      tempNum = 13
   if (ID == 101):
      tempNum = 50
   if (ID == 102):
      tempNum = 50
   if (ID == 103):
      tempNum = 20
   if (ID == 104):
      tempNum = 100
   if (ID == 105):
      tempNum = 30
   if (ID == 106):
      tempNum = 75
   if (ID == 108):
      tempNum = 50
   if (ID == 109):
      tempNum = 125
   if (ID == 110):
      tempNum = 20
   if (ID == 111):
      tempNum = 15
   if (ID == 112):
      tempNum = 15
   if (ID == 113):
      tempNum = 15
   if (ID == 114):
      tempNum = 15
   if (ID == 115):
      tempNum = 5
   if (ID == 116):
      tempNum = 20
   if (ID == 117):
      tempNum = 30
   if (ID == 118):
      tempNum = 55
   if (ID == 119):
      tempNum = 40
   if (ID == 120):
      tempNum = 30
   if (ID == 121):
      tempNum = 15
   if (ID == 122):
      tempNum = 15
   if (ID == 123):
      tempNum = 15
   if (ID == 124):
      tempNum = 15
   if (ID == 125):
      tempNum = 15
   if (ID == 126):
      tempNum = 15
   if (ID == 127):
      tempNum = 35
   if (ID == 128):
      tempNum = 25
   if (ID == 200):
      tempNum = 0
   if (ID == 201):
      tempNum = 15
   if (ID == 202):
      tempNum = 15
   if (ID == 203):
      tempNum = 5
   if (ID == 204):
      tempNum = 1
   if (ID == 205):
      tempNum = 1
   if (ID == 206):
      tempNum = 30
   if (ID == 207):
      tempNum = 20
   if (ID == 208):
      tempNum = 15
   if (ID == 209):
      tempNum = 3
   if (ID == 210):
      tempNum = 17
   if (ID == 211):
      tempNum = 10
   if (ID == 212):
      tempNum = 14
   if (ID == 213):
      tempNum = 5
   if (ID == 214):
      tempNum = 5
   if (ID == 215):
      tempNum = 0
   if (ID == 216):
      tempNum = 150
   if (ID == 217):
      tempNum = 40
   if (ID == 218):
      tempNum = 20
   if (ID == 219):
      tempNum = 5
   if (ID == 220):
      tempNum = 50
   if (ID == 221):
      tempNum = 30
   if (ID == 222):
      tempNum = 15
   if (ID == 223):
      tempNum = 15
   if (ID == 224):
      tempNum = 10
   if (ID == 225):
      tempNum = 10
   if (ID == 226):
      tempNum = 5
   if (ID == 227):
      tempNum = 10
   if (ID == 228):
      tempNum = 10
   if (ID == 229):
      tempNum = 0
   if (ID == 230):
      tempNum = 25
   if (ID == 231):
      tempNum = 15
   if (ID == 232):
      tempNum = 0
   if (ID == 233):
      tempNum = 0
   if (ID == 234):
      tempNum = 0
   if (ID == 235):
      tempNum = 0
   if (ID == 236):
      tempNum = 0
   if (ID == 237):
      tempNum = 0
   if (ID == 238):
      tempNum = 10
   if (ID == 239):
      tempNum = 3
   if (ID == 240):
      tempNum = 75
   if (ID == 241):
      tempNum = 30
   if (ID == 242):
      tempNum = 45
   if (ID == 243):
      tempNum = 100
   if (ID == 244):
      tempNum = 35
   if (ID == 245):
      tempNum = 15
   if (ID == 246):
      tempNum = 20
   if (ID == 247):
      tempNum = 80
   if (ID == 248):
      tempNum = 25
   if (ID == 249):
      tempNum = 45
   if (ID == 250):
      tempNum = 45
   if (ID == 251):
      tempNum = 10
   if (ID == 252):
      tempNum = 0
   if (ID == 253):
      tempNum = 3
   if (ID == 254):
      tempNum = 0
   if (ID == 255):
      tempNum = 15
   if (ID == 256):
      tempNum = 20
   if (ID == 257):
      tempNum = 30
   if (ID == 258):
      tempNum = 30
   if (ID == 259):
      tempNum = 50
   if (ID == 260):
      tempNum = 45
   if (ID == 500):
      tempNum = 5
   if (ID == 501):
      tempNum = 15
   if (ID == 502):
      tempNum = 70
   if (ID == 503):
      tempNum = 10
   if (ID == 504):
      tempNum = 10
   if (ID == 505):
      tempNum = 10
   if (ID == 506):
      tempNum = 10
   if (ID == 507):
      tempNum = 10
   if (ID == 508):
      tempNum = 25
   if (ID == 509):
      tempNum = 25
   if (ID == 510):
      tempNum = 25
   if (ID == 511):
      tempNum = 25
   if (ID == 512):
      tempNum = 25
   if (ID == 513):
      tempNum = 20
   if (ID == 514):
      tempNum = 20
   if (ID == 515):
      tempNum = 20
   if (ID == 516):
      tempNum = 20
   if (ID == 517):
      tempNum = 20
   if (ID == 518):
      tempNum = 50
   if (ID == 519):
      tempNum = 50
   if (ID == 520):
      tempNum = 150
   if (ID == 521):
      tempNum = 50
   if (ID == 522):
      tempNum = 50
   if (ID == 523):
      tempNum = 2
   if (ID == 524):
      tempNum = 7
   if (ID == 525):
      tempNum = 25
   if (ID == 526):
      tempNum = 5
   if (ID == 527):
      tempNum = 10
   if (ID == 528):
      tempNum = 2
   if (ID == 529):
      tempNum = 30
   if (ID == 530):
      tempNum = 40
   if (ID == 531):
      tempNum = 69
   if (ID == 532):
      tempNum = 75
   if (ID == 533):
      tempNum = 5
   if (ID == 534):
      tempNum = 10
   if (ID == 535):
      tempNum = 20
   if (ID == 536):
      tempNum = 20
   if (ID == 537):
      tempNum = 30
   if (ID == 538):
      tempNum = 20
   if (ID == 539):
      tempNum = 10
   if (ID == 540):
      tempNum = 5
   return tempNum

def ItemStackMax(ID:int):
   tempNum = 0
   if (ID == 1):
      tempNum = 1 
   if (ID == 101):
      tempNum = 1 
   if (ID == 102):
      tempNum = 1 
   if (ID == 103):
      tempNum = 15 
   if (ID == 104):
      tempNum = 1 
   if (ID == 105):
      tempNum = 5 
   if (ID == 106):
      tempNum = 1 
   if (ID == 108):
      tempNum = 1 
   if (ID == 109):
      tempNum = 1 
   if (ID == 110):
      tempNum = 5 
   if (ID == 111):
      tempNum = 5 
   if (ID == 112):
      tempNum = 5 
   if (ID == 113):
      tempNum = 5 
   if (ID == 114):
      tempNum = 5 
   if (ID == 115):
      tempNum = 10 
   if (ID == 116):
      tempNum = 1 
   if (ID == 117):
      tempNum = 1 
   if (ID == 118):
      tempNum = 1 
   if (ID == 119):
      tempNum = 1 
   if (ID == 120):
      tempNum = 5 
   if (ID == 121):
      tempNum = 10 
   if (ID == 122):
      tempNum = 10 
   if (ID == 123):
      tempNum = 10 
   if (ID == 124):
      tempNum = 10 
   if (ID == 125):
      tempNum = 10 
   if (ID == 126):
      tempNum = 5 
   if (ID == 127):
      tempNum = 1 
   if (ID == 128):
      tempNum = 10 
   if (ID == 200):
      tempNum = 1 
   if (ID == 201):
      tempNum = 5 
   if (ID == 202):
      tempNum = 5 
   if (ID == 203):
      tempNum = 15 
   if (ID == 204):
      tempNum = 5 
   if (ID == 205):
      tempNum = 5 
   if (ID == 206):
      tempNum = 10 
   if (ID == 207):
      tempNum = 5 
   if (ID == 208):
      tempNum = 10 
   if (ID == 209):
      tempNum = 15 
   if (ID == 210):
      tempNum = 5 
   if (ID == 211):
      tempNum = 15 
   if (ID == 212):
      tempNum = 10 
   if (ID == 213):
      tempNum = 10 
   if (ID == 214):
      tempNum = 10 
   if (ID == 215):
      tempNum = 1 
   if (ID == 216):
      tempNum = 5 
   if (ID == 217):
      tempNum = 5 
   if (ID == 218):
      tempNum = 10 
   if (ID == 219):
      tempNum = 5 
   if (ID == 220):
      tempNum = 5 
   if (ID == 221):
      tempNum = 10 
   if (ID == 222):
      tempNum = 5 
   if (ID == 223):
      tempNum = 10 
   if (ID == 224):
      tempNum = 10 
   if (ID == 225):
      tempNum = 10 
   if (ID == 226):
      tempNum = 15 
   if (ID == 227):
      tempNum = 10 
   if (ID == 228):
      tempNum = 10 
   if (ID == 229):
      tempNum = 1 
   if (ID == 230):
      tempNum = 5 
   if (ID == 231):
      tempNum = 10 
   if (ID == 232):
      tempNum = 1 
   if (ID == 233):
      tempNum = 1 
   if (ID == 234):
      tempNum = 1 
   if (ID == 235):
      tempNum = 1 
   if (ID == 236):
      tempNum = 1 
   if (ID == 237):
      tempNum = 1 
   if (ID == 238):
      tempNum = 15 
   if (ID == 239):
      tempNum = 15 
   if (ID == 240):
      tempNum = 5 
   if (ID == 241):
      tempNum = 5 
   if (ID == 242):
      tempNum = 5 
   if (ID == 243):
      tempNum = 5 
   if (ID == 244):
      tempNum = 1 
   if (ID == 245):
      tempNum = 15 
   if (ID == 246):
      tempNum = 10 
   if (ID == 247):
      tempNum = 1 
   if (ID == 248):
      tempNum = 10 
   if (ID == 249):
      tempNum = 5 
   if (ID == 250):
      tempNum = 5 
   if (ID == 251):
      tempNum = 15 
   if (ID == 252):
      tempNum = 1 
   if (ID == 253):
      tempNum = 15 
   if (ID == 254):
      tempNum = 1 
   if (ID == 255):
      tempNum = 15 
   if (ID == 256):
      tempNum = 15 
   if (ID == 257):
      tempNum = 5 
   if (ID == 258):
      tempNum = 5 
   if (ID == 259):
      tempNum = 10 
   if (ID == 260):
      tempNum = 10 
   if (ID == 500):
      tempNum = 10 
   if (ID == 501):
      tempNum = 5 
   if (ID == 502):
      tempNum = 1 
   if (ID == 503):
      tempNum = 10 
   if (ID == 504):
      tempNum = 10 
   if (ID == 505):
      tempNum = 5 
   if (ID == 506):
      tempNum = 10 
   if (ID == 507):
      tempNum = 10 
   if (ID == 508):
      tempNum = 10 
   if (ID == 509):
      tempNum = 10 
   if (ID == 510):
      tempNum = 10 
   if (ID == 511):
      tempNum = 10 
   if (ID == 512):
      tempNum = 10 
   if (ID == 513):
      tempNum = 5 
   if (ID == 514):
      tempNum = 5 
   if (ID == 515):
      tempNum = 5 
   if (ID == 516):
      tempNum = 5 
   if (ID == 517):
      tempNum = 5 
   if (ID == 518):
      tempNum = 5 
   if (ID == 519):
      tempNum = 5 
   if (ID == 520):
      tempNum = 5 
   if (ID == 521):
      tempNum = 5 
   if (ID == 522):
      tempNum = 5 
   if (ID == 523):
      tempNum = 15 
   if (ID == 524):
      tempNum = 10 
   if (ID == 525):
      tempNum = 5 
   if (ID == 526):
      tempNum = 1 
   if (ID == 527):
      tempNum = 10 
   if (ID == 528):
      tempNum = 10 
   if (ID == 529):
      tempNum = 5 
   if (ID == 530):
      tempNum = 5 
   if (ID == 531):
      tempNum = 1 
   if (ID == 532):
      tempNum = 5 
   if (ID == 533):
      tempNum = 15 
   if (ID == 534):
      tempNum = 10 
   if (ID == 535):
      tempNum = 10 
   if (ID == 536):
      tempNum = 5 
   if (ID == 537):
      tempNum = 5 
   if (ID == 538):
      tempNum = 10 
   if (ID == 539):
      tempNum = 10 
   if (ID == 540):
      tempNum = 15
   return tempNum

def FoodItem(ID:int):
   global hunger
   tempNum = 0
   if (ID == 114):
      tempNum = 5
   if (ID == 208):
      tempNum = 8
   if (ID == 209):
      tempNum = 10
   if (ID == 210):
      tempNum = 20
   if (ID == 211):
      tempNum = 5
   if (ID == 212):
      tempNum = 15
   if (ID == 214):
      tempNum = 30
   if (ID == 218):
      tempNum = 10
   if (ID == 219):
      tempNum = 15
   if (ID == 221):
      tempNum = 15
   if (ID == 222):
      tempNum = 10
   if (ID == 223):
      tempNum = 25
   if (ID == 224):
      tempNum = 20
   if (ID == 226):
      tempNum = 10
   if (ID == 238):
      tempNum = 20
   if (ID == 251):
      tempNum = 40
   if (ID == 253):
      tempNum = 4
   if (ID == 256):
      tempNum = 15
   if (ID == 259):
      tempNum = 25
   if (ID == 500):
      tempNum = 30
   if (ID == 501):
      tempNum = 70
   if (ID == 503):
      tempNum = 3
   if (ID == 504):
      tempNum = 5
   if (ID == 506):
      tempNum = 5
   if (ID == 507):
      tempNum = 7
   if (ID == 508):
      tempNum = 7
   if (ID == 509):
      tempNum = 8
   if (ID == 511):
      tempNum = 10
   if (ID == 512):
      tempNum = 10
   if (ID == 513):
      tempNum = 4
   if (ID == 514):
      tempNum = 4
   if (ID == 516):
      tempNum = 15
   if (ID == 517):
      tempNum = 15
   if (ID == 518):
      tempNum = 8
   if (ID == 519):
      tempNum = 8
   if (ID == 521):
      tempNum = 20
   if (ID == 522):
      tempNum = 20
   if (ID == 523):
      tempNum = 10
   if (ID == 524):
      tempNum = 30
   if (ID == 527):
      tempNum = 15
   if (ID == 529):
      tempNum = 1
   if (ID == 530):
      tempNum = 20
   if (ID == 531):
      tempNum = 50
   if (ID == 534):
      tempNum = 5
   if (ID == 535):
      tempNum = 10
   if (ID == 536):
      tempNum = 15
   if (ID == 537):
      tempNum = 25
   if (ID == 538):
      tempNum = 20
   if (ID == 539):
      tempNum = 15
   if (ID == 540):
      tempNum = 10
   hunger += 2 * tempNum

!def DoItemUse(ID:int):
   global cockTotal
   tempNum = 0
   chance = 0
   dmg = 0
   tempCockSize = 0
   tempBallSize = 0
   if (ID == 103):
      bc()
      this.viewButtonText(0,0,0,0,1,0,1,0,1,0,0,1);
      this.viewButtonOutline(0,0,0,0,1,0,1,0,1,0,1,1);
      this.buttonWrite(5,"Penis");
      if (cockTotal < 1):
         this.Choice5.visible = False
      this.buttonWrite(7,"Pussy")
      if(this.vagTotal < 1)
      {
         this.Choice7.visible = false;
      }
      this.buttonWrite(9,"Breasts");
      this.buttonWrite(11,"Udder");
      this.buttonWrite(12,"Cancel");
      if(this.udders == true)
      {
         this.Choice11.visible = true;
      }
      this.outputMainText("Which genitalia would you like to make a bit dryer?",true);
      this.doListen = function():void
      {
         if(buttonChoice == 5)
         {
            outputMainText("You dab the sand onto your cock-head" + plural(1) + ". It feels odd at first, but as you rub yourself to arousal a bit, you notice a decrease in pre.",true);
            cockMoist -= 4;
            doEnd();
         }
         if(buttonChoice == 7)
         {
            outputMainText("You dab the sand onto your cunt" + plural(2) + ". It feels odd at first, but as you rub yourself to arousal a bit, you notice a decrease in lubrications.",true);
            vagMoist -= 4;
            doEnd();
         }
         if(buttonChoice == 9)
         {
            outputMainText("You dab the sand onto your nipples. It feels odd at first, but as you rub them until they are stiff, you notice a decrease in lactation.",true);
            if(lactation - 75 < 0)
            {
               milkMod += lactation - 75;
            }
            lactChange(1,-75);
            doEnd();
         }
         if(buttonChoice == 11)
         {
            outputMainText("You dab the sand onto your teats. It feels odd at first, but as you rub them until they are stiff, you notice a decrease in lactation.",true);
            lactChange(2,-75);
            doEnd();
         }
         if(buttonChoice == 12)
         {
            itemAdd(103);
            doProcess();
         }
      };
   }
   if(ID == 104)
   {
      if(this.currentState != 3)
      {
         this.outputMainText("You can only use a milker while masturbating.",true);
         this.doEnd();
      }
      else
      {
         tempNum = 0;
         this.bc();
         this.viewButtonText(0,0,0,0,1,0,0,0,0,0,0,0);
         this.viewButtonOutline(0,0,0,0,1,0,1,0,0,0,0,0);
         this.buttonWrite(5,"Breasts");
         this.buttonWrite(7,"Udder");
         if(this.udders == true)
         {
            this.Choice7.visible = true;
         }
         this.outputMainText("What would you like to pump?",true);
         this.doListen = function():void
         {
            var getMilk:int = 0;
            if(buttonChoice == 5)
            {
               tempNum = 1;
            }
            if(buttonChoice == 7)
            {
               tempNum = 2;
            }
            getMilk = 0;
            outputMainText("You uncoil the tubes of your milker, stretching them out and starting up the pump. Attaching the appropriate cups, you slip them onto your ",true);
            if(tempNum == 1)
            {
               outputMainText(nipDesc() + " nipples, until the rims press up and seal onto your " + boobDesc() + " breasts with the gentle suction.",false);
            }
            if(tempNum == 2)
            {
               outputMainText(teatDesc() + " teats, until the rims press up and seal onto your " + udderDesc() + " udder with the gentle suction.",false);
            }
            outputMainText("\r\rYou shudder a little as the stuttered pumping vibrates through your body. Warmth begins to envelop your ",false);
            if(tempNum == 1)
            {
               outputMainText("chest",false);
            }
            if(tempNum == 2)
            {
               outputMainText("belly",false);
            }
            outputMainText(" feeling all tingly.",false);
            if(tempNum == 1 && lactation > 0 || tempNum == 2 && udderLactation > 0)
            {
               ++hrs;
               getMilk = milkAmount(tempNum);
               outputMainText(" Droplets of milk begin to trickle around your ",false);
               if(tempNum == 1)
               {
                  outputMainText("nipples",false);
               }
               if(tempNum == 2)
               {
                  outputMainText("teats",false);
               }
               outputMainText(" and slurps through the tubes. Within moments, your ",false);
               if(tempNum == 1)
               {
                  outputMainText("nipples",false);
               }
               if(tempNum == 2)
               {
                  outputMainText("teats",false);
               }
               outputMainText(" throb along with the pulse, ",false);
               if(getMilk <= 500)
               {
                  outputMainText("small dribbles",false);
               }
               if(getMilk > 500 && getMilk <= 1000)
               {
                  outputMainText("spurts",false);
               }
               if(getMilk > 1000 && getMilk <= 2000)
               {
                  outputMainText("sprays",false);
               }
               if(getMilk > 2000 && getMilk <= 8000)
               {
                  outputMainText("jets",false);
               }
               if(getMilk > 8000 && getMilk <= 19000)
               {
                  outputMainText("steady streams",false);
               }
               if(getMilk > 19000)
               {
                  outputMainText("small floods",false);
               }
               outputMainText(" of milk swishing through the tubes and collecting at the machine.",false);
            }
            outputMainText(" The pleasurable sensation lingers constantly, bringing you to a small orgasm",false);
            if(getMilk > 0)
            {
               outputMainText(" while your flow of milk slows to a stop",false);
            }
            outputMainText(".\r\rYou flip the machine off, the cups making a loud kissing sound as the vacuum is released. As they fall to the floor, you rub your aroused ",false);
            if(tempNum == 1)
            {
               outputMainText(nipDesc() + " nipples",false);
            }
            if(tempNum == 2)
            {
               outputMainText(teatDesc() + " teats",false);
            }
            outputMainText(", shivering from their shortly increased sensitivity, slightly engorged and inflated.",false);
            if(boobTotal > 2 || tempNum == 2)
            {
               outputMainText(" Then you move onto the next pair...",false);
            }
            outputMainText(" Eventually you clean yourself up and put the machine away.",false);
            if(tempNum == 1)
            {
               nipPump += 10;
               if(nipPump > 40)
               {
                  nipPump = 0;
                  ++nippleSize;
                  outputMainText("\r\rHowever, this time your nipples don\'t seem to relax back to their original state, permanently swollen larger...",false);
               }
            }
            if(tempNum == 2)
            {
               teatPump += 10;
               if(teatPump > 40)
               {
                  teatPump = 0;
                  ++teatSize;
                  outputMainText("\r\rHowever, this time your teats don\'t seem to relax back to their original state, permanently swollen larger...",false);
               }
            }
            doNext();
            doListen = function():void
            {
               if(getMilk < 1000)
               {
                  outputMainText("You have produced " + getMilk + " ml of milk!",true);
               }
               else if(getMilk >= 1000)
               {
                  outputMainText("You have produced " + decGet(getMilk / 1000,1) + " liters of milk!",true);
               }
               if(breastSize > 14 && tempNum == 1)
               {
                  doLust(-Math.floor(sen / 4),2,3);
               }
               if(breastSize < 4 && tempNum == 1)
               {
                  doLust(-Math.floor(sen / 4),2,3);
               }
               if(tempNum == 2)
               {
                  doLust(-Math.floor(sen / 4),2,4);
               }
               if(tempNum == 1)
               {
                  nipplePlay += 10;
               }
               if(tempNum == 2)
               {
                  udderPlay += 10;
               }
               if(getMilk < 1000)
               {
                  outputMainText("\r\rUnfortunately, you haven\'t produced enough milk to fill a full bottle yet.",false);
               }
               if(getMilk >= 1000 && getMilk < 3000)
               {
                  itemAdd(500);
               }
               if(getMilk >= 3000 && getMilk < 6000)
               {
                  itemAdd(501);
               }
               if(getMilk >= 6000 && getMilk < 17000)
               {
                  itemAdd(501);
                  itemAdd(501);
               }
               if(getMilk >= 17000 && getMilk < 25000)
               {
                  itemAdd(502);
               }
               if(getMilk >= 25000)
               {
                  itemAdd(502);
                  outputMainText("\r\rHowever, you produced so much milk that the container in the milker couldn\'t hold it all and everything beyond a barrel-full splashed out around the edges, making a mess everywhere!",false);
               }
               ++hrs;
               doEnd();
            };
         };
      }
   }
   if(ID == 106)
   {
      if(this.currentState != 3)
      {
         this.outputMainText("You can only use the a penis pump while masturbating.",true);
         this.doEnd();
      }
      else
      {
         tempNum = 0;
         this.bc();
         this.viewButtonText(0,0,0,0,0,0,0,0,0,1,0,0);
         this.viewButtonOutline(0,0,0,0,1,0,1,0,0,1,0,0);
         this.buttonWrite(5,"Penis");
         if(this.cockTotal > 0)
         {
            this.Choice5.visible = true;
         }
         this.buttonWrite(7,"Clit");
         if(this.vagTotal > 0)
         {
            this.Choice7.visible = true;
         }
         this.buttonWrite(10,"None");
         this.outputMainText("What would you like to pump?",true);
         this.doListen = function():void
         {
            var tempInt:int = 0;
            var whichCock:String = null;
            var getCum:int = 0;
            if(buttonChoice == 5)
            {
               rndArray = [];
               if(humanCocks > 0)
               {
                  rndArray.push(1);
               }
               if(horseCocks > 0)
               {
                  rndArray.push(2);
               }
               if(wolfCocks > 0)
               {
                  rndArray.push(3);
               }
               if(catCocks > 0)
               {
                  rndArray.push(4);
               }
               if(lizardCocks > 0)
               {
                  rndArray.push(6);
               }
               if(rabbitCocks > 0)
               {
                  rndArray.push(7);
               }
               if(bugCocks > 0)
               {
                  rndArray.push(12);
               }
               tempInt = chooseFrom();
               whichCock = "WHICH COCK ERROR";
               if(tempInt == 1)
               {
                  whichCock = "hard human rod";
               }
               if(tempInt == 2)
               {
                  whichCock = "long equine flesh";
               }
               if(tempInt == 3)
               {
                  whichCock = "pointy wolf meat";
               }
               if(tempInt == 4)
               {
                  whichCock = "pink thorny cat prick";
               }
               if(tempInt == 6)
               {
                  whichCock = "purple ribbed reptile rod";
               }
               if(tempInt == 7)
               {
                  whichCock = "throbbing bunny carrot";
               }
               if(tempInt == 12)
               {
                  whichCock = "bumpy-ridged spiked bug wang";
               }
               outputMainText("You pick out the appropriate cylinder size for " + oneYour(1) + " cock" + plural(1) + ". You slip it over your " + whichCock + " and attach the tube at the other end. Whether you were hard or not already, as soon as you flip on the pump\'s switch, your " + hipDesc() + " hips jerk as blood flushes through the " + cockDesc() + " member. The vacuum pressure makes it swell, growing stiffer and larger than before!\r\rThe pump then gently relaxes before giving you another nice suck, followed by another release, eventually building into a slow rhythm.",true);
               if(lust < 20)
               {
                  outputMainText(" Yet, despite the pleasurable sensation, you\'re not really horny enough to climax, the pump merely sucking away at your engorgement for a while before you finally give up and put it away.",false);
                  cockPump += 10;
                  if(cockPump > 40)
                  {
                     cockPump = 0;
                     ++cockSize;
                     outputMainText("\r\rAlthough, the swelling from the suction doesn\'t seem to go down all the way, your cock" + plural(1) + " permanently slightly larger.",false);
                  }
                  hrs = 1;
                  doEnd();
               }
               else
               {
                  getCum = cumAmount();
                  if(moistCalc(1) <= 3)
                  {
                     outputMainText(" The bottle within the machine fills a little with your pre as it seeps out, but it\'s hardly much.\r\r",false);
                  }
                  if(moistCalc(1) > 3 && moistCalc(1) <= 7)
                  {
                     outputMainText(" The bottle within the machine fills nearly halfway with your pre as it dribbles out, so you quickly spill it out before you climax.\r\r",false);
                  }
                  if(moistCalc(1) > 7 && moistCalc(1) <= 11)
                  {
                     outputMainText(" The bottle within the machine fills to the brim with your pre as it spurts from your cock, forcing you to quickly replace it with a fresh bottle before you climax.\r\r",false);
                  }
                  if(moistCalc(1) > 11)
                  {
                     outputMainText(" The bottle within the machine fills to the brim with your pre as it gushes from your cock, spilling over the rim. You pull the bottle out and let your slime spew across the floor until you\'re about to climax and replace it with a fresh one.\r\r",false);
                  }
                  if(showBalls == true)
                  {
                     outputMainText("Eventually, your " + ballDesc() + " balls groan as the sensation gets the best of them. ",false);
                  }
                  outputMainText("You begin to buck as the machine does its job, your cum spurting from the tip of your " + whichCock + " and flowing through the tubes, despositing into the bottle. Spurt after spurt gets sucked out, milking your cock until it\'s dry.",false);
                  if(getCum < 1000)
                  {
                     outputMainText("\r\rYou have produced " + getCum + " ml of spooge!",false);
                  }
                  else if(getCum >= 1000)
                  {
                     outputMainText("\r\rYou have produced " + decGet(getCum / 1000,1) + " liters of spooge!",false);
                  }
                  if(getCum <= 400)
                  {
                     outputMainText(" Although, the resulting amount is so small that you can\'t really do anything with it...",false);
                  }
                  if(getCum > 400 && getCum <= 600)
                  {
                     outputMainText(" The resulting amount of spunk is just enough to fill a vial!",false);
                     itemAdd(523);
                  }
                  if(getCum > 600 && getCum <= 1200)
                  {
                     outputMainText(" The resulting amount of spunk is more than enough to fill a vial, with a quite a bit left to spill over the edge.",false);
                     itemAdd(523);
                  }
                  if(getCum > 1200 && getCum <= 2000)
                  {
                     outputMainText(" You come so much that you fill the whole bottle, great for resale!",false);
                     itemAdd(524);
                  }
                  if(getCum > 2000 && getCum <= 4500)
                  {
                     outputMainText(" You come so much that you fill the whole bottle, and more continues to gush out over the edge, making quite the mess.",false);
                     itemAdd(524);
                  }
                  if(getCum > 4500 && getCum <= 5500)
                  {
                     outputMainText(" Well prepared, you quickly swap out the bottle with a jug. Your cum floods inside, filling it up to the brim!",false);
                     itemAdd(525);
                  }
                  if(getCum > 5500 && getCum <= 21000)
                  {
                     outputMainText(" Prepared, you quickly swap out the bottle with a jug. Your cum floods inside, filling it up to the brim. However, you continue to gush, overfilling it until cum spills over the edge and floods around you, making quite the mess...",false);
                     itemAdd(525);
                  }
                  if(getCum > 21000)
                  {
                     outputMainText(" Worried about drowing in your own cum, you quickly pull the bottle out and attach a hose to the item you came prepared with... a barrel. Though you still manage to overfill it, you haven\'t created quite the natural disaster. And since you can\'t quite get much for a whole barrel of cum, you top off a jug as well...",false);
                     itemAdd(525);
                     itemAdd(526);
                  }
                  cockPump += 10;
                  if(cockPump > 40)
                  {
                     cockPump = 0;
                     ++cockSize;
                     outputMainText("\r\rAlthough, after cleaning up, the swelling from the suction doesn\'t seem to go down, your cock" + plural(1) + " permanently slightly larger...",false);
                  }
                  if(cockSize * cockSizeMod * 4 > tallness && gender == 3)
                  {
                     doLust(-Math.floor(sen / 4),2,58,3,57,4);
                  }
                  else if(cockSize * cockSizeMod * 4 > tallness)
                  {
                     doLust(-Math.floor(sen / 4),2,58,1,57,4);
                  }
                  else if(gender == 3)
                  {
                     doLust(-Math.floor(sen / 4),2,3,57,4);
                  }
                  else
                  {
                     doLust(-Math.floor(sen / 4),2,1,57,4);
                  }
                  hrs = 2;
                  doEnd();
               }
            }
            if(buttonChoice == 7)
            {
               if(lust < 20)
               {
                  outputMainText("You\'re not really in the mood to do it at the moment, opting to put the pump back in your bag for now...",true);
                  doEnd();
               }
               else
               {
                  if(clitSize <= 20)
                  {
                     outputMainText("Feeling a little kinky, you take the smallest available cylinder and push it over " + oneYour(2) + " clit" + plural(2) + ". Turning on the machine, you quickly notice you\'re still too small, having to manually seal the cylinder against your skin with your fingers. However, that isn\'t a problem, as you soon begin to enjoy the sucking on your clit, the button swelling from the vacuum while your fingers sliding through your " + vulvaDesc() + " lips and dipping into your hole" + plural(2) + ", moving in rhythm to the pumping.",true);
                  }
                  if(clitSize > 20)
                  {
                     outputMainText("Feeling a little kinky, you take some cylinders to slide over " + oneYour(2) + " clit" + plural(2) + ". Its so big that it easily fits into one of them, just like it were a cock. Turning on the machine, your " + hipDesc() + " hips squirm as the suction forces your button to swell, becoming even larger. Your fingers slide through your " + vulvaDesc() + " lips and dip into your hole" + plural(2) + ", moving in rhythm to the pumping.",true);
                  }
                  if(moistCalc(2) > 0 && moistCalc(2) <= 3)
                  {
                     outputMainText(" The pump manages to suck up a few drops of your feminine honey as you masturbate, misting the tubes slightly.",false);
                  }
                  if(moistCalc(2) > 3 && moistCalc(2) <= 7)
                  {
                     outputMainText(" The pump manages to suck up some of your dribbling feminine honey, letting it drip lazily from into a bottle that was meant for spunk.",false);
                  }
                  if(moistCalc(2) > 7 && moistCalc(2) <= 11)
                  {
                     outputMainText(" The pump manages to suck up a bit of your flowing feminine honey, spurting it into a bottle meant for spunk instead.",false);
                  }
                  if(moistCalc(2) > 11)
                  {
                     outputMainText(" The pump manages to suck up a good deal of your gushing feminine honey, filling a bottle in the machine that was meant for spunk instead. It\'s not something you can sell, but it amuses you nonetheless.",false);
                  }
                  outputMainText(" You soon quiver and moan as you come to climax, sighing gently as you turn the pump off to enjoy your swollen clit by hand for a while.",false);
                  clitPump += 10;
                  if(clitPump > 40)
                  {
                     clitPump = 0;
                     ++clitSize;
                     outputMainText("\r\rAlthough, after cleaning up, the swelling from the suction doesn\'t seem to go down, your clit" + plural(1) + " permanently slightly larger...",false);
                  }
                  if(clitSize * 24 > tallness && gender == 3)
                  {
                     doLust(-Math.floor(sen / 4),2,1);
                  }
                  else if(clitSize * 24 > tallness)
                  {
                     doLust(-Math.floor(sen / 4),2,1);
                  }
                  else if(gender == 3)
                  {
                     doLust(-Math.floor(sen / 4),2,1);
                  }
                  else
                  {
                     doLust(-Math.floor(sen / 4),2,1);
                  }
                  hrs = 2;
                  doEnd();
               }
            }
            if(buttonChoice == 10)
            {
               outputMainText("You realize you didn\'t actually want to use the pump and put it back in your bag. You fickle bastard.",true);
               doEnd();
            }
         };
      }
   }
   if(ID == 105)
   {
      this.outputMainText("Bringing the vial filled with white liquid to your lips, you soon taste the sweet, milky stuff within. Downing it, your " + this.boobDesc() + " breasts feel warm. Small blotches of milk form through your " + this.clothesTop() + ", around your nipples. The tingling heat then permeates your body, making you feel slightly more aroused as well.",true);
      this.stats(0,0,1,0);
      this.doLust(5,0);
      if(this.udders == true)
      {
         this.outputMainText(" Even your udder begins to dribble a little, feeling slightly fuller.",false);
         this.lactChange(2,20);
      }
      this.lactChange(1,15);
      this.doEnd();
   }
   if(ID == 108)
   {
      this.outputMainText("You push the gauge against your pulse. It grows warm for a moment before a vague display shows up on the other side.",true);
      if(this.humanAffinity > 0)
      {
         this.outputMainText("\r\rHuman:\r",false);
       #  for(this.i = 1; this.i <= this.humanAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.horseAffinity > 0)
      {
         this.outputMainText("\r\rHorse:\r",false);
      #   for(this.i = 1; this.i <= this.horseAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.wolfAffinity > 0)
      {
         this.outputMainText("\r\rWolf:\r",false);
      #   for(this.i = 1; this.i <= this.wolfAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.catAffinity > 0)
      {
         this.outputMainText("\r\rCat:\r",false);
      #   for(this.i = 1; this.i <= this.catAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.cowAffinity > 0)
      {
         this.outputMainText("\r\rCow:\r",false);
      #   for(this.i = 1; this.i <= this.cowAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.lizardAffinity > 0)
      {
         this.outputMainText("\r\rLizard:\r",false);
      #   for(this.i = 1; this.i <= this.lizardAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.rabbitAffinity > 0)
      {
         this.outputMainText("\r\rRabbit:\r",false);
      #   for(this.i = 1; this.i <= this.rabbitAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.mouseAffinity > 0)
      {
         this.outputMainText("\r\rMouse:\r",false);
      #   for(this.i = 1; this.i <= this.mouseAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.birdAffinity > 0)
      {
         this.outputMainText("\r\rBird:\r",false);
      #   for(this.i = 1; this.i <= this.birdAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.pigAffinity > 0)
      {
         this.outputMainText("\r\rPig:\r",false);
      #   for(this.i = 1; this.i <= this.pigAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.skunkAffinity > 0)
      {
         this.outputMainText("\r\rSkunk:\r",false);
      #   for(this.i = 1; this.i <= this.skunkAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      if(this.bugAffinity > 0)
      {
         this.outputMainText("\r\rBug:\r",false);
      #   for(this.i = 1; this.i <= this.bugAffinity; this.outputMainText("|",false),++this.i)
         {
         }
      }
      this.doEnd();
   }
   if(ID == 109)
   {
      if(this.checkItem(219))
      {
         if(this.knowPheromone == true && this.silRep < 1 && !this.checkItem(530) && !this.checkStash(530) && !this.checkItem(532) && !this.checkStash(532) && this.pheromone < 1)
         {
            this.outputMainText("You slip a Fresh Egg into the eggdicator and listen to it whir as it studies the egg. Within moments, you hear a *DING*.\r\r",true);
            this.loseManyItem(219,1);
            this.outputMainText("Into the reception bin rolls a white-shelled egg with pretty red hearts all over.",false);
            this.itemAdd(530);
            this.doEnd();
         }
         else
         {
            chance = this.percent();
            this.outputMainText("You slip a Fresh Egg into the eggdicator and listen to it whir as it studies the egg. Within moments, you hear a *DING*.\r\r",true);
            this.loseManyItem(219,1);
            if(chance <= 45)
            {
               this.outputMainText("Into the reception bin rolls a blue-shelled egg.",false);
               this.itemAdd(527);
            }
            else if(chance <= 85)
            {
               this.outputMainText("Into the reception bin rolls a red-shelled egg.",false);
               this.itemAdd(528);
            }
            else if(chance <= 92)
            {
               this.outputMainText("Into the reception bin rolls a pink-shelled egg with teal polka-dots.",false);
               this.itemAdd(529);
            }
            else if(chance <= 97)
            {
               this.outputMainText("Into the reception bin rolls a white-shelled egg with pretty red hearts all over.",false);
               this.itemAdd(530);
            }
            else if(chance <= 100)
            {
               this.outputMainText("Into the reception bin rolls a golden-shelled glowing egg.",false);
               this.itemAdd(531);
            }
            this.doEnd();
         }
      }
      else
      {
         this.outputMainText("The well-educated eggdicator indicates a deficiency in your ovoid protein supply and thus cannot adequately correspond to your commands.\r\rI.e. - You need a Fresh Egg to use this.",true);
         this.doEnd();
      }
   }
   if(ID == 110)
   {
      this.choiceListArray = [];
      if(this.breastSize > 0)
      {
         this.choiceListArray.push("Breasts");
      }
      if(this.nippleSize > 1)
      {
         this.choiceListArray.push("Nipples");
      }
      if(this.butt > 1)
      {
         this.choiceListArray.push("Butt");
      }
      if(this.hips > 1)
      {
         this.choiceListArray.push("Hips");
      }
      if(this.vagTotal > 0)
      {
         this.choiceListArray.push("Pussy");
         if(this.vulvaSize > 0)
         {
            this.choiceListArray.push("Vulva");
         }
         if(this.clitSize > 1)
         {
            this.choiceListArray.push("Clit");
         }
      }
      if(this.cockTotal > 0)
      {
         this.choiceListArray.push("Cock");
         if(this.showBalls == true && this.ballSize > 1)
         {
            this.choiceListArray.push("Balls");
         }
      }
      if(this.udders == true)
      {
         if(this.udderSize > 1)
         {
            this.choiceListArray.push("Udder");
         }
         if(this.teatSize > 2)
         {
            this.choiceListArray.push("Teats");
         }
      }
      if(this.bellyMod > 0)
      {
         this.choiceListArray.push("Belly");
      }
      this.choiceListButtons("Reduction");
      this.outputMainText("Select which body part you would like to halve in size. If you don\'t have that part, this elixer will do nothing but will still be consumed.",true);
      this.doListen = function():void
      {
         choiceListSelect("Reduction");
         outputMainText("You splash the elixir out onto your ",true);
         if(choiceListResult[0] == "Cock")
         {
            outputMainText(cockDesc() + " cock" + plural(1),false);
            outputMainText(" and watch with a shiver as the flesh receeds.",false);
            cockChange(-Math.ceil(cockSize / 2),0);
         }
         if(choiceListResult[0] == "Balls")
         {
            outputMainText(ballDesc() + " balls",false);
            ballSize -= Math.floor(ballSize / 2);
            outputMainText(" and watch with a shiver as the orbs shrink, becoming " + ballDesc() + ".",false);
         }
         if(choiceListResult[0] == "Pussy")
         {
            outputMainText("vagina" + plural(2),false);
            outputMainText(" and quiver as the fleshy walls within your body shrink.",false);
            vagChange(Math.floor(-vagSize / 2),0);
         }
         if(choiceListResult[0] == "Vulva")
         {
            outputMainText(vulvaDesc() + " vulva",false);
            vulvaSize -= Math.floor(vulvaSize / 2);
            outputMainText(" and watch with a quiver as nether-lips shrink, becoming " + vulvaDesc() + ".",false);
         }
         if(choiceListResult[0] == "Clit")
         {
            outputMainText(clitDesc() + " clit" + plural(2),false);
            clitSize -= Math.floor(clitSize / 2);
            outputMainText(" and watch with a quiver as the button" + plural(2) + " shrink" + plural(4) + ", becoming " + clitDesc() + ".",false);
         }
         if(choiceListResult[0] == "Breasts")
         {
            outputMainText(boobDesc() + " breasts",false);
            breastSize -= Math.floor(breastSize / 2);
            outputMainText(" and shudder as they shrink.",false);
         }
         if(choiceListResult[0] == "Nipples")
         {
            outputMainText(nipDesc() + " nipples",false);
            nippleSize -= Math.floor(nippleSize / 2);
            outputMainText(" and shudder as they receed into your breasts.",false);
         }
         if(choiceListResult[0] == "Udder")
         {
            outputMainText(udderDesc() + " udder",false);
            udderSize -= Math.floor(udderSize / 2);
            outputMainText(" and watch as it shrivels, becoming " + udderDesc() + ".",false);
         }
         if(choiceListResult[0] == "Teats")
         {
            outputMainText(teatDesc() + " teats",false);
            teatSize -= Math.floor(teatSize / 2);
            outputMainText(" and watch as they recede, becoming " + teatDesc() + ".",false);
         }
         if(choiceListResult[0] == "Butt")
         {
            outputMainText(buttDesc() + " butt",false);
            butt -= Math.floor(butt / 2);
            outputMainText(" and squirm as it shrinks, becoming " + buttDesc() + ".",false);
         }
         if(choiceListResult[0] == "Hips")
         {
            outputMainText(hipDesc() + " hips",false);
            hips -= Math.floor(hips / 2);
            outputMainText(" and squirm as they narrow, becoming " + hipDesc() + ".",false);
         }
         if(choiceListResult[0] == "Belly")
         {
            outputMainText(bellyDesc() + " belly",false);
            bellyMod -= Math.floor(bellyMod / 2);
            outputMainText(" and feel lighter as the chubbiness burns off, becoming " + bellyDesc() + ".",false);
         }
         if(buttonChoice == 4 || buttonChoice == 8)
         {
            choiceListButtons("Reduction");
         }
         else if(buttonChoice == 12)
         {
            itemAdd(110);
            doProcess();
         }
         else
         {
            doEnd();
         }
      };
   }
   if(ID == 111)
   {
      this.outputMainText("Smearing the balm around your body, you feel slightly more sensitive and your curiousity is slightly piquied.",true);
      this.stats(0,1,0,1);
      this.aff(1,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 112)
   {
      this.outputMainText("Downing the \'juice\', you realize it\'s a lot thicker and stickier than you expected, and quite heady. Your heart beats a bit stronger and you shudder a bit.",true);
      this.stats(1,0,1,0);
      this.aff(2,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 113)
   {
      this.outputMainText("Biting into the leaf, it feels oddly sour. However, afterward your mind feels a bit clearer and your body more prepared for whatever may come.",true);
      this.stats(1,1,0,0);
      this.aff(3,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 114)
   {
      this.outputMainText("Drinking the slick, slimey, slightly sweet sap, you realize it probably isn\'t sap... The thought makes you tingle with arousal, your whole body slightly more sensitive.",true);
      this.stats(0,0,1,1);
      this.aff(4,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 115)
   {
      this.outputMainText("You rub the soothing poultice all over your wounds, quickly making them heal. Rubbing yourself down with the wet rag, you rub a little too much in some areas and become slightly more aroused.",true);
      this.doHP(20);
      this.doLust(5,0);
      this.doEnd();
   }
   if(ID == 116)
   {
      this.outputMainText("You have equipped the dagger.",true);
      this.weapon = 116;
      this.doEnd();
   }
   if(ID == 117)
   {
      this.outputMainText("You have equipped the warhammer.",true);
      this.weapon = 117;
      this.doEnd();
   }
   if(ID == 118)
   {
      this.outputMainText("You have equipped the saber.",true);
      this.weapon = 118;
      this.doEnd();
   }
   if(ID == 119)
   {
      this.outputMainText("You have equipped the whip.",true);
      this.weapon = 119;
      this.doEnd();
   }
   if(ID == 120)
   {
      this.bc();
      this.viewButtonText(0,1,0,0,1,0,1,0,0,0,0,1);
      this.viewButtonOutline(0,1,0,0,1,0,1,0,0,1,0,1);
      this.buttonWrite(2,"None");
      this.buttonWrite(5,"Cock");
      if(this.cockTotal < 1)
      {
         this.Choice5.visible = false;
         this.Choice10.visible = false;
      }
      this.buttonWrite(7,"Cunt");
      if(this.vagTotal < 1)
      {
         this.Choice7.visible = false;
      }
      this.buttonWrite(10,"Balls");
      this.buttonWrite(12,"Cancel");
      if(this.showBalls == true && this.balls > 0)
      {
         this.Choice10.visible = true;
      }
      this.outputMainText("What would you like to remove?\r\rNote that removing balls removes one at a time. If try to remove them when you only have two left, neuterizer simply hides them, as it would severely damage your plumbing without them.",true);
      this.doListen = function():void
      {
         if(buttonChoice == 2)
         {
            outputMainText("You decide you\'d rather keep what you got, for the moment, and put the neuterizer back in your bag.",true);
            itemAdd(120);
            doEnd();
         }
         if(buttonChoice == 5)
         {
            outputMainText("You rub the neuterizer into " + oneYour(1) + " " + cockDesc() + " cock" + plural(1) + "...",true);
            cockChange(0,-1);
            doEnd();
         }
         if(buttonChoice == 7)
         {
            outputMainText("You rub the neuterizer into " + oneYour(2) + " " + vulvaDesc() + " cunt" + plural(1) + "...",true);
            vagChange(0,-1);
            doEnd();
         }
         if(buttonChoice == 10)
         {
            if(balls > 2)
            {
               outputMainText("You rub the neuterizer into your scrotum. You squirm a bit as one of your testicles wrenches a bit, shrinking down. Once it disappears into nothing, you feel perfectly fine again.",true);
               --balls;
               doEnd();
            }
            else
            {
               outputMainText("Unfortunately, the neuterizer cannot simply make your testicles disappear while you still have any cocks. It would be... too dangerous. But, rubbing it onto your scrotum, your balls disappear up into your body, hidden from view.",true);
               showBalls = false;
               doEnd();
            }
         }
         if(buttonChoice == 12)
         {
            itemAdd(120);
            doProcess();
         }
      };
   }
   if(ID == 121)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a whoosh, they quickly disappear and you find yourself back in the human city of Softlik!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(1);
      this.doEnd();
   }
   if(ID == 122)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a whistle, they quickly disappear and you find yourself back in the equan city of Firmshaft!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(2);
      this.doEnd();
   }
   if(ID == 123)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a howl, they quickly disappear and you find yourself back in the lupan city of Tieden!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(3);
      this.doEnd();
   }
   if(ID == 124)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a swish, they quickly disappear and you find yourself back in the felin city of Siz\'Calit!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(4);
      this.doEnd();
   }
   if(ID == 125)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a splash, they quickly disappear and you find yourself back in the lizan city of Oviasis!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(6);
      this.doEnd();
   }
   if(ID == 126)
   {
      this.outputMainText("Sipping the refreshing water, you notice a slight aftertaste of something funny, like people have been bathing and doing... things in the water. It\'s kinda kinky when you think about it, but also feels nice inside of you.",true);
      if(this.percent() <= 50)
      {
         this.stats(1,0,1,0);
      }
      else
      {
         this.stats(0,0,1,1);
      }
      this.aff(6,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 127)
   {
      if(this.tail == 4 || this.tail == 5 || this.tail == 6 || this.tail == 8)
      {
         this.outputMainText("You strap the tail spike to your tail, equipping it as your weapon.",true);
         this.weapon = 127;
      }
      else
      {
         this.outputMainText("You do not have an appropriate tail to strap this onto and thus cannot equip it.",true);
      }
      this.doEnd();
   }
   if(ID == 128)
   {
      this.outputMainText("You read the scroll and soft, sparkling lights between to shine and fly around you, faster and faster until you can\'t see beyond them.\r\rWith a thump, they quickly disappear and you find yourself back in the city of Sanctuary!",true);
      this.currentState = 1;
      this.inBag = false;
      this.inDungeon = false;
      this.regionChange(12);
      this.doEnd();
   }
   if(ID == 201)
   {
      this.bc();
      this.viewButtonText(0,0,0,0,1,0,0,0,0,0,0,1);
      this.viewButtonOutline(0,0,0,0,1,0,1,0,0,0,0,1);
      this.buttonWrite(5,"Breasts");
      if(this.udders == true)
      {
         this.buttonWrite(7,"Udder");
         this.Choice7.visible = true;
      }
      this.buttonWrite(12,"Cancel");
      this.outputMainText("What would you like to rub the Milk Creeper Poison into?",true);
      this.doListen = function():void
      {
         if(buttonChoice == 5)
         {
            outputMainText("You pour out the vial of poison and rub the pearlescant fluid all over your " + boobDesc() + " breasts. You shiver a little as they tingle, a subtle warmth permeating your bosom as the poison sets in and remains.",true);
            milkCPoisonNip += 5;
            doLust(percent() / 10,0);
            doEnd();
         }
         if(buttonChoice == 7)
         {
            outputMainText("You pour out the vial of poison and rub the pearlescant fluid all over your " + udderDesc() + " udder. Your hips twitch a little as the fleshy bag tingles, a subtle warmth permeating your udder as the poison sets in and remains.",true);
            milkCPoisonUdd += 5;
            doLust(percent() / 10,0);
            doEnd();
         }
      };
      if(this.buttonChoice == 12)
      {
         this.itemAdd(201);
         this.doProcess();
      }
   }
   if(ID == 202)
   {
      if(this.cockTotal > 0)
      {
         this.outputMainText("You pull your " + this.clothesBottom() + " " + this.pullUD(2) + " and rub the venom into your cock" + this.plural(1) + ". Within seconds, you begin to shudder erotically as warmth fills your cock" + this.plural(1) + ", becoming erect. After waiting a few moments, the erection settles somewhat, but the warmth of the venom within persists, as though lying in wait...",true);
         this.doLust(4 * this.cockTotal,0);
         this.cockSnakeVenom += 5;
         this.doEnd();
      }
      else if(this.cockTotal < 1 && this.vagTotal > 0)
      {
         this.outputMainText("You pull your " + this.clothesBottom() + " " + this.pullUD(2) + " and rub the venom into your groin. Within seconds, you begin to shudder...",true);
         if(this.clitSize > 20 && this.percent() <= 5)
         {
            this.outputMainText(" You feel " + this.oneYour(2) + " " + this.clitDesc() + " clit" + this.plural(2) + " swell and shift within your " + this.clothesBottom() + ", your lips starting to grow quite oddly as well...",false);
            this.vagChange(0,-1);
            this.cockChange(Math.ceil(this.clitSize * 5 / 2),1);
            this.doLust(4,0);
         }
         else
         {
            this.outputMainText(" You feel your " + this.clitDesc() + " clit" + this.plural(2) + " grow warm. Within seconds, you begin to shudder erotically as you clit" + this.plural(2) + " grow hot and erect. After waiting a few moments, the initial intensity passes, but the warmth of the venom within persists, as though lying in wait...",false);
            this.cockSnakeVenom += 5;
            this.doLust(4 * this.vagTotal,0);
         }
         this.doEnd();
      }
      else
      {
         this.outputMainText("You pull your " + this.clothesBottom() + " " + this.pullUD(2) + " and rub the venom into your groin. You wait for several seconds and... nothing seems to happen. What a waste.",true);
         this.doEnd();
      }
   }
   if(ID == 203)
   {
      this.outputMainText("You rub the tuft of coarse wolf fur into your " + this.skinDesc() + ". The roughness desensitizes you a bit.",true);
      this.stats(0,0,0,-3);
      this.doEnd();
   }
   if(ID == 204)
   {
      chance = this.percent();
      if(chance <= 30)
      {
         this.outputMainText("You find some coins inside!",true);
         this.doCoin(Math.floor(this.percent() / 5));
      }
      else if(chance <= 40)
      {
         this.itemAdd(246);
      }
      else if(chance > 40 && chance <= 55)
      {
         this.itemAdd(105);
      }
      else if(chance > 55 && chance <= 75)
      {
         this.itemAdd(103);
      }
      else if(chance > 75 && chance <= 90)
      {
         this.itemAdd(114);
      }
      else
      {
         this.outputMainText("Daww, turns out the pouch was empty...",true);
      }
      this.doEnd();
   }
   if(ID == 205)
   {
      chance = this.percent();
      if(chance <= 50)
      {
         this.outputMainText("You find some coins inside!",true);
         this.doCoin(Math.floor(this.percent() / 5 + 5));
      }
      else if(chance > 50 && chance <= 65)
      {
         this.itemAdd(112);
      }
      else if(chance > 65 && chance <= 85)
      {
         this.itemAdd(115);
      }
      else if(chance > 85)
      {
         this.outputMainText("Daww, turns out the pouch was empty...",true);
      }
      this.doEnd();
   }
   if(ID == 207)
   {
      chance = this.percent();
      this.outputMainText("You crack open the wooden cock. ",true);
      if(chance <= 15)
      {
         this.outputMainText(" Sparkling lights erupt from the crack, swirling around in the air until they come together to form the outline of a disembodied glowing cock, looking much like the carving. Before you react, it flips around and dives down, before driving back up " + this.legWhere(1) + " your " + this.legDesc(2) + " and disappearing into the crotch of your " + this.clothesBottom() + ".",false);
         this.vagChange(0,1);
         this.doLust(this.percent() / 5,0);
      }
      else if(chance <= 30)
      {
         this.outputMainText(" Sparkling lights erupt from the crack, swirling around in the air until they come together to form the outline of a disembodied glowing cock, looking much like the carving. Before you react, it flips around and charges at your groin, ramming right above your crotch and disappearing into the front of your " + this.clothesBottom() + ".",false);
         this.cockChange(0,1);
         this.doLust(this.percent() / 5,0);
      }
      else
      {
         this.outputMainText(" There\'s nothing inside... Either this thing was just some kinky woman\'s play-toy, or it was a dud.",false);
      }
      this.doEnd();
   }
   if(ID == 208)
   {
      this.outputMainText("You pop the berry into your mouth. As it pops and gushes with juice within your mouth, your face cringes at how un-sweet it is. Tasting more salty with a thick texture, you swallow it as fast as possible.",true);
      if(this.balls > 0 && this.ballSize > 0 && this.showBalls == true && this.hunger >= 60)
      {
         this.outputMainText(" Moments later, you feel a warmth in your groin as the food digests. You squirm as you feel your testicles swell within their scrotum, growing hot with seed... Seems as though this berry has increased the size of your balls, somehow, and now you feel a little hungry again.",false);
         this.ballSize += Math.floor(this.percent() / 33);
         this.hunger -= 20;
      }
      else if(this.balls > 0 && this.ballSize > 0 && this.showBalls == false && this.hunger >= 60)
      {
         this.outputMainText(" Moments later, you feel a warmth in your groin as the food digests. You squirm as you feel your cum churning within your body, something swelling within... Seems as though this berry has increased the size of your non-visible balls, somehow, and now you feel a little hungry again.",false);
         this.ballSize += Math.floor(this.percent() / 33);
         this.doLust(this.percent() / 10,0);
         this.hunger -= 20;
      }
      else
      {
         this.outputMainText(" Moments later, you feel a bit of warmth in your groin, but it quickly passes. Now all you\'re left with is the aftertaste...",false);
      }
      this.doEnd();
   }
   if(ID == 209)
   {
      this.outputMainText("You pop the handful into your mouth and munch on them. Doesn\'t taste too bad. Although, the thought of mixing them in a bowl with some milk for breakfast does cross your mind, but passes shortly as you feel like you can get through the day better anyways.",true);
      this.exhaustion -= 4;
      if(this.hunger >= 80)
      {
         this.outputMainText("\r\rUnfortunately, it seems the food you have been eating has gone straight to your " + this.buttDesc() + " ass, making your " + this.clothesBottom() + " feel slightly tight around it as it swells.",false);
         this.butt += Math.floor(this.percent() / 33);
         this.hunger -= 20;
      }
      this.doEnd();
   }
   if(ID == 210)
   {
      chance = this.percent();
      this.outputMainText("You bite into the fold-like cleft of the pussy fruit, sweet juices spilling out around your face and drooling from your chin in long, slimy strands. You devour it shortly and feel great!",true);
      this.doHP(15);
      if(this.hunger >= 70 && this.vagTotal > 0 && chance <= 50)
      {
         this.outputMainText("\r\rHowever, it feels as though the food energy has run straight to your crotch as a warmth spreads around your cunt" + this.plural(2) + ". You squeeze your " + this.vulvaDesc() + " groin through your " + this.clothesBottom() + ", feeling it swell larger...\r\rYou walk a bit awkwardly afterward, getting used to your now extra-swollen lips and feeling slightly hungry again...",false);
         this.vulvaSize += Math.floor(this.percent() / 20);
         this.doLust(this.percent() / 10,0);
         this.hunger -= 20;
      }
      else if(this.hunger >= 70 && this.vagTotal > 0)
      {
         this.outputMainText("\r\rHowever, it feels as though the juices have run straight to your crotch as a warmth spreads around your cunt" + this.plural(2) + ". You double over as your stomach cramps a little. It feels like your insides are being compressed, your cunt" + this.plural(2) + " feeling larger within...\r\rThe cramping shortly passes, but the increased size is real and you feel slightly hungry again...",false);
         this.vagChange(Math.floor(this.percent() / 20),0);
         this.doLust(this.percent() / 10,0);
         this.hunger -= 20;
      }
      else if(this.hunger >= 90 && this.vagTotal > 0)
      {
         this.outputMainText("\r\rHowever, it feels as though the juices have run straight to your crotch as a warmth spreads around your cunt" + this.plural(2) + ". You double over as your stomach cramps a little. It feels like your insides are being compressed, your cunt" + this.plural(2) + " feeling larger within. You squeeze your " + this.vulvaDesc() + " groin through your " + this.clothesBottom() + ", feeling it swell larger...\r\rThe cramping shortly passes, but you walk awkwardly afterward, getting used to your now extra-swollen lips and feeling slightly hungry again...",false);
         this.vulvaSize += Math.floor(this.percent() / 20);
         this.vagChange(Math.floor(this.percent() / 20),0);
         this.doLust(this.percent() / 5,0);
         this.hunger -= 30;
      }
      this.doLust(this.percent() / 10,0);
      this.doEnd();
   }
   if(ID == 211)
   {
      this.outputMainText("Considering you don\'t have any cows to give it to, you pop the pill into your mouth and gulp it down. Within some moments your " + this.boobDesc() + " chest feels rather warm...",true);
      if(this.udders == true)
      {
         this.outputMainText(" And so does your udder.",false);
         if(this.udderPlay >= 60)
         {
            this.lactChange(2,35);
         }
         else
         {
            this.udderPlay += 20;
         }
      }
      if(this.nipplePlay >= 60)
      {
         this.lactChange(1,25);
      }
      else
      {
         this.nipplePlay += 20;
      }
      this.doLust(this.percent() / 10,0);
      this.aff(5,Math.floor(this.percent() / 20 + 2),-1);
      this.doEnd();
   }
   if(ID == 212)
   {
      this.outputMainText("You munch on the red mushroom. It doesn\'t taste terribly good or bad, but a blush quickly heats up your face as your chest turns intensely warm.",true);
      if(this.hunger >= 80)
      {
         this.outputMainText(" Your " + this.clothesTop() + " feels unexpectedly tight, thanks to all the food you\'ve been eating.\r\rAs you look down, you let out a gasp as your " + this.boobDesc() + " chest swells beneath your " + this.clothesTop() + ", your " + this.nipDesc() + "nipples pushing against the fabric. You grab the mounds and feel them grow larger, heavier, and more wobbly...\r\rThe warmth soon passes, leaving you bent over slightly as you adjust to the increased weight. You don\'t feel quite as full anymore though, much of your excess energy used up by this sudden growth.",false);
         this.boobChange(Math.ceil(this.percent() / 33));
         this.hunger -= 20;
      }
      else
      {
         this.outputMainText(" Then the warmth subsides and your stomach grumbles from the strange food. You do feel less hungry though.",false);
      }
      this.doEnd();
   }
   if(ID == 213)
   {
      this.bc();
      this.viewButtonText(0,0,0,0,0,0,0,0,0,1,0,0);
      this.viewButtonOutline(0,0,0,0,1,0,1,0,0,1,0,0);
      this.buttonWrite(5,"Cock" + this.plural(1));
      this.buttonWrite(7,"Cunt" + this.plural(2));
      this.buttonWrite(10,"Breasts");
      this.buttonWrite(12,"Cancel");
      if(this.cockTotal > 0)
      {
         this.Choice5.visible = true;
      }
      if(this.vagTotal > 0)
      {
         this.Choice7.visible = true;
      }
      this.outputMainText("What would you like to rub the wet, slimy cloth on?",true);
      this.doListen = function():void
      {
         if(buttonChoice == 5)
         {
            outputMainText("You rub the slimy cloth around the head" + plural(1) + " of your " + cockDesc() + " cock" + plural(1) + ", polishing until there\'s a nice sheen. You feel a bit aroused from doing so, yet the cloth seems to have finally dried off.\r\rHowever, your cock" + plural(1) + " begin" + plural(3) + " dripping with the slime of the cloth instead...",true);
            ++cockMoist;
            if(cockMoist > 12)
            {
               outputMainText("\r\rHowever, that\'s not really any different than normal, leaving you fairly unaffected.",false);
            }
            doLust(percent() / 10,0);
            doEnd();
         }
         if(buttonChoice == 7)
         {
            outputMainText("You rub the slimy cloth through the lips of your " + vulvaDesc() + " cunt" + plural(2) + " until your thighs are completely wet. You feel a bit aroused from doing so, yet the cloth seems to have finally dried off.\r\rHowever, your cunt" + plural(2) + " begin" + plural(4) + " dripping with the slime of the cloth instead...",true);
            ++vagMoist;
            if(vagMoist > 12)
            {
               outputMainText("\r\rHowever, that\'s not really any different than normal, leaving you fairly unaffected.",false);
            }
            doLust(percent() / 10,0);
            doEnd();
         }
         if(buttonChoice == 10)
         {
            outputMainText("You rub the slimy cloth over your " + boobDesc() + " breasts and " + nipDesc() + "nipples until they\'re all completely wet. You feel a bit aroused from doing so, yet the cloth seems to have finally dried off.\r\rHowever, other than make your chest shine erotically, it doesn\'t really do much.",true);
            doLust(percent() / 10,0);
            doEnd();
         }
         if(buttonChoice == 12)
         {
            itemAdd(213);
            doProcess();
         }
      };
   }
   if(ID == 214)
   {
      this.outputMainText("You down the bottle of milk and feel refreshed!",true);
      this.doHP(15 + this.milkHPMod);
      this.aff(5,Math.floor(this.percent() / 10),0);
      this.exhaustion -= 3;
      this.doEnd();
   }
   if(ID == 216)
   {
      this.dyeThing(ID,5);
   }
   if(ID == 217)
   {
      this.outputMainText("You smear the jelly around your genitals. It\'s so slick and hot, you can\'t help but feel immensely aroused.",true);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" And as you rub it into your nether-lips, you feel it absorb into the walls of your vagina" + this.plural(2) + ". Slipping a finger in, it doesn\'t feel much different, until you actually prod a wall. It bends much more easily, as though it were more elastic than before. You could probably shove even larger things in there without feeling pain...",false);
         this.vagElastic += 0.1;
      }
      this.doLust(50,0);
      this.doEnd();
   }
   if(ID == 218)
   {
      this.outputMainText("You pop the berry into your mouth. As it pops and gushes with juice within your mouth, your face cringes at how un-sweet it is. Tasting more salty with a thick texture, you swallow it as fast as possible.",true);
      if(this.balls > 0 && this.ballSize > 0 && this.showBalls == true)
      {
         this.outputMainText(" Moments later, you feel a warmth in your groin. You squirm as your testicles feel crowded, your scrotum growing tight. You look to see and find an extra testicle in your sack!",false);
         ++this.balls;
         this.doLust(this.percent() / 10,0);
      }
      else if(this.balls > 0 && this.ballSize > 0 && this.showBalls == false)
      {
         this.outputMainText(" Moments later, you feel a warmth in your groin. You squirm as you feel your cum churning within your body, something extra growing within... Seems as though this berry caused you to grow an extra internal testicle, somehow.",false);
         ++this.balls;
         this.doLust(this.percent() / 10,0);
      }
      else
      {
         this.outputMainText(" Moments later, you feel a bit of warmth in your groin, but it quickly passes. Now all you\'re left with is the aftertaste...",false);
      }
      this.doEnd();
   }
   if(ID == 219)
   {
      this.outputMainText("You crack the egg open and swallow its contents, your belly thanking you for the food.",true);
      this.doHP(5);
      if(this.hunger >= 70)
      {
         this.outputMainText("\r\rHowever, the fertile nature of the egg (and lots of protein) seem to go straight to your hips, making them grow wider.",false);
         this.hips += Math.floor(this.percent() / 50);
         this.hunger -= 25;
      }
      this.doEnd();
   }
   if(ID == 220)
   {
      this.dyeThing(ID,2);
   }
   if(ID == 221)
   {
      this.outputMainText("You down the vial. It\'s so sweet that your face puckers a bit, the concentrated syrup slowly dripping down your throat.",true);
      if(this.vagTotal < 1)
      {
         this.outputMainText("\r\rYour loins feel quite warm for a moment, but the sensation quickly passes. It does nothing for you other than overwhelm your sweet-tooth.",false);
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour loins begin to grow hot. Your hand jerks down to your crotch, rubbing yourself feverishly through your " + this.clothesBottom() + ". The garment quickly grows moist, your arousal spreading " + this.legWhere(1) + " your " + this.legDesc(2) + ". You can feel your labia swell beneath your grip, your lips bulging out of your grasp, while your belly aches slightly with a bloating sensation. Your clit" + this.plural(2) + " squeeze" + this.plural(4) + " between your fingers.\r\rThe change soon passes, but the changing in the size of your nethers is easily noticeable, making you walk awkwardly at first as you become accustomed.",false);
         this.vagChange(Math.floor(this.percent() / 20) + 2,0);
         this.vulvaSize += Math.floor(this.percent() / 20) + 2;
         this.clitSize += Math.floor(this.percent() / 20) + 2;
         ++this.vagMoist;
      }
      this.doEnd();
   }
   if(ID == 222)
   {
      this.outputMainText("Happy with how clean you\'ve gotten it, you munch on the tasty vegetable. It makes you feel healthier to the point where you\'re nearly hopping with energy.",true);
      this.aff(7,Math.floor(this.percent() / 15 + 2),-2);
      this.doHP(4);
      this.doEnd();
   }
   if(ID == 223)
   {
      this.outputMainText("The tasty morsel crumbles delightfully in your mouth.",true);
      this.doHP(5);
      if(this.vagTotal > 0 && this.hunger >= 90)
      {
         this.outputMainText(" Though it settles in your stomach rather oddly, as you feel some squirming slightly below that, the snack quickly digesting into something else...",false);
         this.vagChange(1,0);
         this.hunger -= 25;
      }
      if(this.percent() <= 25)
      {
         this.outputMainText("\r\rAnd you don\'t quite feel stronger, you feel as though you could hold up more weight.",false);
         ++this.carryMod;
      }
      this.doEnd();
   }
   if(ID == 224)
   {
      this.outputMainText("Lila\'s breastmilk tastes quite sweet, with a slight aftertaste of her other fluids. It makes you feel a bit... tender, so to speak.",true);
      if(this.percent() <= 25 && this.vagMoist < 12 && this.vagTotal > 0)
      {
         this.outputMainText(" You feel some extra moistness in your loins as well, the liquid seeming to imprint some of the girl\'s wetness upon you.",false);
         ++this.vagMoist;
      }
      if(this.heat > 0)
      {
         if(this.heatTime > 0)
         {
            this.outputMainText(" There\'s also a slight sensation of coming closer to your fertile period...",false);
            if(this.heatTime > 5)
            {
               this.heatTime -= 5;
            }
            if(this.heatTime < 6)
            {
               this.heatTime = 1;
            }
         }
         if(this.heatTime < 0)
         {
            this.outputMainText(" There\'s also a slight tinge of heat that flows through your body, strengthening your estrus for a little longer...",false);
            this.heatTime -= 5;
         }
      }
      this.doEnd();
   }
   if(ID == 225)
   {
      this.outputMainText("You quickly scrub yourself down with the body wash, feeling so fresh and so clean. Which is kinda odd, considering that you\'re currently playing a porn game.",true);
      this.exhaustion -= 8;
      this.stats(0,1,0,2);
      this.doLust(-10,0);
      this.doEnd();
   }
   if(ID == 226)
   {
      this.outputMainText("You mix the tea with a nice cup of hot water, producing a nice calming aroma. You sip it down and quite quickly feel much more relaxed.",true);
      this.exhaustion -= 6;
      this.doLust(-10,0);
      if(this.heat > 0)
      {
         if(this.heatTime > 0)
         {
            this.heatTime += 3;
         }
         if(this.heatTime < 0)
         {
            if(this.heatTime < -3)
            {
               this.heatTime += 3;
            }
            if(this.heatTime > -4)
            {
               this.heatTime = -1;
            }
         }
      }
      this.doEnd();
   }
   if(ID == 227)
   {
      this.outputMainText("Taking a swig of the sweet-smelling stuff, you feel it tingle all the way down your throat and spread throughout your body from the inside.",true);
      this.doLust(10,0);
      this.stats(0,0,1,0);
      if(this.skinType == 2)
      {
         this.outputMainText(" You then proceed to lick as much of your fur as possible, making it look sleek and shiny",false);
         this.stats(0,0,0,1);
      }
      this.doEnd();
   }
   if(ID == 228)
   {
      this.outputMainText("You rub the oil all over your " + this.skinDesc() + ", making yourself look shiny and attractive, bringing attention to all the contours of your body.",true);
      if(this.bodyOil > 0)
      {
         this.bodyOil = 5;
      }
      else
      {
         this.enticeMod += 5;
         this.bodyOil = 5;
      }
      if(this.skinType == 1 || this.skinType == 3)
      {
         this.outputMainText(" It also makes your " + this.skinDesc() + " feel so good to the touch~",false);
         this.stats(0,0,0,1);
      }
      this.doEnd();
   }
   if(ID == 230)
   {
      if(this.vagTotal < 1)
      {
         this.outputMainText("You take out the eggcelerator, realize you don\'t have an appropriate orifice, and put it back away...",true);
         this.itemAdd(230);
         this.doEnd();
      }
      else
      {
         this.outputMainText("You pull " + this.pullUD(2) + " your " + this.clothesBottom() + " and squat down to help spread your " + this.vulvaDesc() + " lips. Grabbing the eggcelerator with your fingertips, you slip it into " + this.oneYour(2) + " slit" + this.plural(2) + ", pointy end first. It doesn\'t take much before physics takes over and the suppository slips up into your deeper spaces where you can feel a slight tingle as it dissolves.",true);
         if(this.eggLaying > 0)
         {
            if(this.eggceleratorDose > 6 + Math.ceil(this.percent() / 20))
            {
               this.outputMainText("\r\rYou can feel your next egg starting to come along more quickly than before... but it continues to build. Your " + this.bellyDesc() + " belly lets out a groan as you feel the fresh egg already press against your lips, demanding its way out. You fall back onto your hands, your " + this.legDesc(6) + " in the air as you lay it with such expediency that your thighs quiver and your pussy gasps in surprise. Yet, the sensation doesn\'t end, as more eggs begin to develop almost instantly inside your womb, one by one forcing their way through your passageway. Your " + this.hipDesc() + " hips jerk and your " + this.clitDesc() + " clit" + this.plural(2) + " stand" + this.plural(4) + " tall with a strange arousal as you thrust into the air again and again to plop out egg after egg. Part of you wants to furiously rub yourself as the eggs nearly launch from your spread cunt, but the rapid pace of the laying makes your body a twitching, seizing mess as you cry out in desparation. So many eggs fly out of you into a pile that you can hardly save them all; quite a few crack and ooze over the others. The round, smooth, slick object having their way with your sensitive flesh eventually makes you quake with an odd orgasm, somewhat powerful but not quite fulfilling, making you collapse back onto the ground as your womb pops out the rest...\r\rOver half an hour passes after your egg-laying extravaganza before you can collect yourself. You sit up to wipe the slime from your pussy, gazing upon the pile of eggs you have laid until you finally go through and pull out the good ones. You also notice that your womb seems to have completely calmed down afterwards, the eggcelerator having been purged from your system. It seems you had taken so many doses that your body could no longer handle it...",false);
               this.i = 0;
               while(this.i < this.eggceleratorDose)
               {
                  this.itemAdd(219);
                  ++this.i;
               }
               this.doLust(Math.floor(-this.sen / 3),2,2);
               this.eggceleratorTime = 0;
               this.eggRate -= this.eggceleratorDose;
               this.eggceleratorDose = 0;
               this.hrs = 1;
            }
            else
            {
               this.outputMainText("\r\rAlready you can somewhat feel that the next egg will be coming along more quickly than before and hope you\'ll be prepared for it.",false);
               ++this.eggRate;
               this.eggceleratorTime = 30;
               ++this.eggceleratorDose;
            }
         }
         else
         {
            this.outputMainText("\r\rOther than the tingling, it doesn\'t seem to do much... It would probably be more useful if you could actually lay eggs.",false);
         }
         this.doEnd();
      }
   }
   if(ID == 231)
   {
      if(this.currentState != 2)
      {
         this.outputMainText("You can only use this dangerous sand in battle. You put the sand back into your bag.",true);
         this.itemAdd(231);
         this.doEnd();
      }
      else
      {
         dmg = Math.floor(Math.random() * (1 + 40 - 20)) + 20;
         this.outputMainText("You throw the pile of sand at the " + this.enemyName() + ". It cringes and winces as the sand sucks the moisture from its body, dealing " + dmg + " damage!",true);
         this.doeHP(-dmg);
         if(this.percent() <= 25)
         {
            this.outputMainText("\r\rHowever, the wind catches some of the sand and it blow back at you! ",false);
            this.rndArray = ["Desi Sand"];
            if(this.cockSizeMod > 0.5 && this.cockTotal > 0)
            {
               this.rndArray.push(1);
            }
            if(this.vagSizeMod > 0.5 && this.vagTotal > 0)
            {
               this.rndArray.push(2);
            }
            if(this.cumMod > 0.5 && this.showBalls == true && this.cockTotal > 0)
            {
               this.rndArray.push(3);
            }
            if(this.milkMod > 0)
            {
               this.rndArray.push(4);
            }
            if(this.pregnancyTime > 200)
            {
               this.rndArray.push(5);
            }
            this.rndArray.push(6);
            this.chooseFrom();
            if(this.rndResult == 1)
            {
               this.outputMainText("The stuff rushes across your " + this.cockDesc() + " cock" + this.plural(1) + ", seeping in deep and causing some permanent shrinkage.",false);
               this.cockSizeMod -= 0.05;
            }
            else if(this.rndResult == 2)
            {
               this.outputMainText("The stuff rushes between your legs and you can feel some slip up into your passage" + this.plural(2) + ", seeping in deep and resulting in some permanent shriveling.",false);
               this.vagSizeMod -= 0.05;
            }
            else if(this.rndResult == 3)
            {
               this.outputMainText("The stuff rushes across your " + this.ballDesc() + " balls, sinking through the scrotum and causing them to lose some of their efficiency.",false);
               this.cumMod -= 0.1;
            }
            else if(this.rndResult == 4)
            {
               this.outputMainText("The stuff rushes across your " + this.boobDesc() + " breasts, sinking into your mammary glands and reducing their power.",false);
               this.milkMod -= 5;
            }
            else if(this.rndResult == 5)
            {
               this.outputMainText("The stuff rushes across your " + this.bellyDesc() + " belly. It doesn\'t affect the life within, but you can feel your womb wane as it loses some of its future fertility.",false);
               this.pregRate -= 0.05;
               this.pregChanceMod = this.pregChanceMod - 1;
               this.extraPregChance = this.extraPregChance - 1;
            }
            else
            {
               this.outputMainText("Thankfully, it barely touches you and you\'re left unaffected.",false);
            }
         }
         if(this.currentState == 2)
         {
            this.doEnd();
         }
      }
   }
   if(ID == 232)
   {
      if(this.currentState != 1)
      {
         this.outputMainText("You cannot activate the flying carpet during battle or while attempting to masturbate. It takes too long to set up during battle and it is not the kind of \'carpet-munching\' you should be doing while masturbating.",true);
         this.doEnd();
      }
      else
      {
         this.viewButtonText(0,0,0,0,0,1,0,0,0,0,0,0);
         this.viewButtonOutline(0,0,0,0,0,1,0,0,0,0,0,0);
         this.buttonWrite(6,"Stay Here");
         this.outputMainText("Where would you like to go?",true);
         if(this.currentZone == 1)
         {
            if(this.foundTieden == true)
            {
               this.Choice1.visible = true;
               this.Choice1Outline.visible = true;
               this.buttonWrite(1,"Tieden");
            }
            if(this.foundFirmshaft == true)
            {
               this.Choice10.visible = true;
               this.Choice10Outline.visible = true;
               this.buttonWrite(10,"Firmshaft");
            }
         }
         if(this.currentZone == 2)
         {
            if(this.foundSoftlik == true)
            {
               this.Choice3.visible = true;
               this.Choice3Outline.visible = true;
               this.buttonWrite(3,"Softlik");
            }
            if(this.foundSizCalit == true)
            {
               this.Choice5.visible = true;
               this.Choice5Outline.visible = true;
               this.buttonWrite(5,"Siz\'Calit");
            }
            if(this.foundOviasis == true)
            {
               this.Choice10.visible = true;
               this.Choice10Outline.visible = true;
               this.buttonWrite(10,"Oviasis");
            }
            if(this.foundSanctuary == true)
            {
               this.Choice11.visible = true;
               this.Choice11Outline.visible = true;
               this.buttonWrite(11,"Sanctuary");
            }
         }
         if(this.currentZone == 3)
         {
            if(this.foundSoftlik == true)
            {
               this.Choice7.visible = true;
               this.Choice7Outline.visible = true;
               this.buttonWrite(7,"Softlik");
            }
            if(this.foundSizCalit == true)
            {
               this.Choice9.visible = true;
               this.Choice9Outline.visible = true;
               this.buttonWrite(9,"Siz\'Calit");
            }
         }
         if(this.currentZone == 4)
         {
            if(this.foundTieden == true)
            {
               this.Choice2.visible = true;
               this.Choice2Outline.visible = true;
               this.buttonWrite(2,"Tieden");
            }
            if(this.foundFirmshaft == true)
            {
               this.Choice7.visible = true;
               this.Choice7Outline.visible = true;
               this.buttonWrite(7,"Firmshaft");
            }
            if(this.foundOviasis == true)
            {
               this.Choice11.visible = true;
               this.Choice11Outline.visible = true;
               this.buttonWrite(11,"Oviasis");
            }
         }
         if(this.currentZone == 6)
         {
            if(this.foundSizCalit == true)
            {
               this.Choice1.visible = true;
               this.Choice1Outline.visible = true;
               this.buttonWrite(1,"Siz\'Calit");
            }
            if(this.foundFirmshaft == true)
            {
               this.Choice2.visible = true;
               this.Choice2Outline.visible = true;
               this.buttonWrite(2,"Firmshaft");
            }
         }
         this.doListen = function():void
         {
            inDungeon = false;
            if(currentZone == 1)
            {
               if(buttonChoice == 1)
               {
                  regionChange(3);
               }
               if(buttonChoice == 10)
               {
                  regionChange(2);
               }
            }
            else if(currentZone == 2)
            {
               if(buttonChoice == 3)
               {
                  regionChange(1);
               }
               if(buttonChoice == 5)
               {
                  regionChange(4);
               }
               if(buttonChoice == 10)
               {
                  regionChange(6);
               }
               if(buttonChoice == 11)
               {
                  regionChange(12);
               }
            }
            else if(currentZone == 3)
            {
               if(buttonChoice == 7)
               {
                  regionChange(1);
               }
               if(buttonChoice == 9)
               {
                  regionChange(4);
               }
            }
            else if(currentZone == 4)
            {
               if(buttonChoice == 2)
               {
                  regionChange(3);
               }
               if(buttonChoice == 7)
               {
                  regionChange(2);
               }
               if(buttonChoice == 11)
               {
                  regionChange(6);
               }
            }
            else if(currentZone == 6)
            {
               if(buttonChoice == 1)
               {
                  regionChange(4);
               }
               if(buttonChoice == 2)
               {
                  regionChange(2);
               }
            }
            if(buttonChoice == 6)
            {
               doProcess();
            }
            else
            {
               outputMainText("You step onto the carpet and with a gentle woosh, it lifts into the air and darts off in the direction of your desired location. Within just a couple of hours, you land in " + regionName(currentZone) + ", just like you wanted.",true);
               hrs = 2;
               doEnd();
            }
         };
      }
   }
   if(ID == 235)
   {
      this.outputMainText("You have equipped the fellatio rod.",true);
      this.weapon = 235;
      this.doEnd();
   }
   if(ID == 238)
   {
      this.outputMainText("Nibbling the cheese, the delicious flavor melts in your mouth and feels so good going down. It feels good just eating it, like you could go hunting for lots more. Though... Hey, did your clothes get looser, or is it just your imagination?",true);
      this.tallness = this.tallness - 1;
      this.aff(8,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 239)
   {
      this.outputMainText("You take out the rock and stare at it, intently focused on how shiny it is. Your mind grows sharper, allowing you to focus even harder and... Wait, what? One last glint of shininess and the rock suddenly became dull. Maybe you stared too hard? Either way, you toss the now dull rock, no longer interested in it.",true);
      this.stats(0,1,0,0);
      this.aff(9,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 240)
   {
      this.dyeThing(ID,6);
   }
   if(ID == 241)
   {
      this.dyeThing(ID,7);
   }
   if(ID == 242)
   {
      this.dyeThing(ID,8);
   }
   if(ID == 243)
   {
      this.dyeThing(ID,9);
   }
   if(ID == 244)
   {
      if(this.snuggleBall == false)
      {
         this.outputMainText("You take out the snuggle ball and squeeze it against your chest, hugging it gleefully. So squishy and soft, the pleasant sensation of it forming around your body as you compress it is oh so nice~ Though it doesn\'t stop forming around your body...\r\rLiquidy tendrils lash out from the ball, sticking to your face and arms, belly and " + this.legDesc(2) + ". You don\'t have time to resist as it wraps around your body, seeping past your " + this.currentClothes() + " and coating your " + this.skinDesc() + ".\r\rOver within moments, you stand there and gradually try to move. A plush and soft layer, slightly shiny and malleable just like the ball, covers all your " + this.skinDesc() + ". It doesn\'t impede your movement or actions, almost like it was an extra layer of skin, and doesn\'t do much but make you... snuggly.",true);
         this.snuggleBall = true;
         this.doEnd();
      }
      else
      {
         this.outputMainText("Would you like to try and remove the plush shiny layer of cuddliness that covers your " + this.skinDesc() + "?",true);
         this.buttonConfirm();
         this.doListen = function():void
         {
            if(buttonChoice == 6)
            {
               if(percent() / 2 > str)
               {
                  outputMainText("You pull and tug at the extra layer of \'skin\'. It stretches from your body, but yanks itself out of your grip and snaps back in place. The little bugger just doesn\'t want to let go!",true);
               }
               else
               {
                  outputMainText("You pull and tug at the extra layer of \'skin\'. It stretches from your body and with a bit more exertion it snaps off, coalescing back down into a little ball in your hand. Your " + skinDesc() + " now free of the little bugger, you put it back in your bag to deal with later.",true);
                  snuggleBall = false;
               }
               doEnd();
            }
            else
            {
               doProcess();
            }
         };
      }
   }
   if(ID == 245)
   {
      this.outputMainText("You pour the mud out into your hands and slather it all over your face. You let it sit there for a few moments, enjoying the warm sensation and feeling it creep into your pores and make your " + this.skinDesc() + " feel nice.\r\rYou soon wipe it off once it has had its effect, but tickle your nose a little in the process and make you laugh until you oink- err... snort.",true);
      this.stats(0,0,0,1);
      this.aff(10,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 246)
   {
      this.outputMainText("You pour out the gel into your hand and rub it into your loins, making sure it gets in niiice and deeeep.",true);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" Your womb seems to soak up the warmth of the gel, feeling more receptive to semen~",false);
         if(this.fertileGel == 0)
         {
            this.pregChanceMod += 10;
         }
         this.fertileGel += 24;
      }
      else
      {
         this.outputMainText(" However, you\'re not sure why you did that, since you don\'t exactly have a womb to make more fertile... Oh well, you\'re a pervert anyways.",false);
      }
      this.doEnd();
   }
   if(ID == 247)
   {
      if(this.suppHarness == false)
      {
         this.outputMainText("You wrap the harness around your back with the latches in front of you so you can see what you\'re doing. You gauge how tight they should be for your chest, crotch, and other various anatomy to fit before twisting it around. Then you stuff your chest into the appropriate sling, and continue on down until the multiple slings hold up your various weighty bits snugly, giving you a good deal more support. You can\'t exactly carry the world on your shoulders, but you can at least carry a bit more of yourself now.",true);
         this.carryMod += 50;
         this.suppHarness = true;
      }
      else
      {
         this.carryMod -= 50;
         if(this.doWeight())
         {
            this.outputMainText("You reach around behind back and fiddle with the latches of the harness, forcing them open. Your anatomy immediately falls out of the slings, taken you with it as you crash to the ground, completely anchored by your own body. You at least manage to finish unequipping the harness and put it in your bag, but now you\'ve got some issues...",true);
            this.doWeight();
         }
         else
         {
            this.outputMainText("You reach around behind back and fiddle with the latches of the harness, forcing them open. Your bits bounce out as they\'re set free, making you jerk as the weight falls back upon your body. You then stuff the harness back into your bag, no longer equipped, and prepare yourself to continue on with the unsupported weight.",false);
         }
         this.suppHarness = false;
      }
      this.doEnd();
   }
   if(ID == 248)
   {
      this.outputMainText("You gulp down the potion yourself, rather than giving it to some animal that it was intended for.",true);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" Your womb immediately begins to warm up a little, your ovaries \'feeling\' like they\'re working harder. It\'s strange to describe, but your body quickly adapts and the warmth settles down.",false);
         this.extraPregChance += 3;
      }
      else
      {
         this.outputMainText(" However, you don\'t really notice any effect when it comes to having a larger litter... You kinda can\'t have litters without a womb to birth them from, come to think of it.",false);
      }
      if(this.heat > 0)
      {
         this.outputMainText(" Whereas your loins seem to feel flushed. Not exactly going into heat just from the potion, but more feeling like they will do so more readily now...",false);
         this.heatMaxTime -= Math.floor(this.heatMaxTime * 0.1);
      }
      this.doEnd();
   }
   if(ID == 249)
   {
      this.outputMainText("You drop the small tear into your mouth, swallowing it easily with a quick gulp. You don\'t even feel it in your stomach; it doesn\'t seem to do anything at first.\r\rHowever, a sensation of wilting envelopes your appendages, like they\'re growing weaker.",true);
      if(this.cockTotal > 0 || this.vagTotal > 0)
      {
         this.outputMainText(" The sensation coalesces into your crotch, focusing within your extra genitalia.",false);
         if(this.cockTotal > 0)
         {
            this.tallness += Math.ceil(this.cockTotal / 4) * 2;
            this.cockChange(0,-Math.ceil(this.cockTotal / 4));
         }
         if(this.balls > 2)
         {
            this.tallness += Math.ceil(this.balls / 4);
            if(this.showBalls == true)
            {
               this.outputMainText("\r\r" + Math.ceil(this.balls / 4) + " of your testicles also shrivel up inside your scrotum, being absorbed back into your body.",false);
            }
            this.balls -= Math.ceil(this.balls / 4);
         }
         if(this.vagTotal > 0)
         {
            this.tallness += Math.ceil(this.vagTotal / 4) * 2;
            this.vagChange(0,-Math.ceil(this.vagTotal / 4));
         }
         this.outputMainText("\r\rThen, once you have lost the extra genitals, the ground below you falls away! Or, more accurately, your heads shoots upward as your body rapidly begins to grow, taller and taller to compensate for the genitals you have lost! You have shed your extra \'limbs\' and grown towards the sky.",false);
      }
      else
      {
         this.outputMainText(" The sensation coalesces into your crotch for an instance, but quickly dissolves. Then... that\'s it.\r\rSeems whatever the tear was supposed to do didn\'t affect you. So much for that.",false);
      }
      this.doEnd();
   }
   if(ID == 250)
   {
      if(this.currentState != 2)
      {
         this.outputMainText("You can only use this escape bomb in battle, it\'s not really useful otherwise. You put the foomp bomb back into your bag.",true);
         this.itemAdd(250);
         this.doEnd();
      }
      else
      {
         this.outputMainText("Needing a quick escape, you throw the foomp bomb at the enemy. It explodes on contact with a cloud of magical dust and, just as its name implies, there\'s a sort of \"foomp!\" sound. As the dust clears, you can\'t help but giggle at the results. The " + this.enemyName() + "\'s whole body has ballooned to amusing proportions; inflated by the bomb.",true);
         if(this.eGen == 1 || this.eGen == 3)
         {
            this.outputMainText(" The " + this.enemyName() + "\'s cock propels forward with the growth, flopping down onto the ground many times larger than it was, anchoring itself do the ground and preventing its owner from moving.",false);
         }
         if(this.eGen == 2 || this.eGen == 3)
         {
            this.outputMainText(" The " + this.enemyName() + "\'s breasts swell to obscene sizes, making her fall forward and be cushioned by the pillowy masses, unable to stand.",false);
         }
         if(this.eGen == 4)
         {
            this.outputMainText(" The " + this.enemyName() + "\'s midsection grows so large and round that it is unable to move at all.",false);
         }
         this.outputMainText("\r\rHowever, the bomb\'s effects are already beginning to wear off as you stare at its results. Taking advantage of this short opportunity, you turn and dash away before the " + this.enemyName() + " can shrink back down to a manageable size and continue the fight.",false);
         this.currentState = 1;
         this.hrs += 1;
         this.doEnd();
      }
   }
   if(ID == 251)
   {
      this.outputMainText("Biting into the plump fruit, the sweet flesh melts delightfully in your mouth with a nice citrusy sour tinge. Gulping it down and feeling it splash into your stomach and warm your insides makes you crave even more. Your mouth immediately bites off another chunk of the fruit, then another, insatiably devouring the delicious thing. The flesh slips down your throat and sinks into your stomach, filling you up so delightfully~\r\rBut before you know it, you\'ve already eaten the whole thing. You glutton. Though there\'s no more left, you can still feel it digesting inside, which in itself is rather pleasant...",true);
      this.bellyMod += 10;
      this.plumpQuats += 6;
      this.doEnd();
   }
   if(ID == 253)
   {
      if(this.tail == 12)
      {
         this.viewButtonText(0,0,0,0,1,0,1,0,0,0,0,0);
         this.viewButtonOutline(0,0,0,0,1,0,1,0,0,0,0,0);
         this.buttonWrite(5,"Eat");
         this.buttonWrite(7,"Ovipositor");
         this.outputMainText("Considering the egg is just about the right size for the hole in your large ovipositor tail, what would you like to do with it?",true);
         this.doListen = function():void
         {
            var chance:int = 0;
            if(buttonChoice == 5)
            {
               outputMainText("You pop the egg into your mouth and bite down. The gooey stuff splorts about your mouth and... isn\'t exactly tasty. Even swallowing it makes your belly want to rebel. The act kills off some of your arousal, at least.",true);
               doLust(-3,0);
               doEnd();
            }
            if(buttonChoice == 7)
            {
               outputMainText("Taking the chance, you bend around yourself and press the squishy egg up against the hole at the end of your blunted tail. You wince and shudder as you push it in, the passage inside sensitive as it quickly engulfs the sphere, arousing you slightly. Then it\'s gone.\r\rYou jiggle your " + buttDesc() + " butt, feeling the wide fleshy tail flop up and down on it, and wait a few moments as you hear and sense some groaning within, similar to the sounds of digestion. Eventually you feel a pressure against the inside of the hole and you press down, your hand ready at the tip to catch the slimy thing as it pops back out.\r\r",true);
               chance = percent();
               if(chance <= 8)
               {
                  outputMainText("The egg now glows with a sort of regal luster, slightly larger than before with a heavier weight.",false);
                  itemAdd(537);
               }
               else if(chance <= 25)
               {
                  outputMainText("The egg now feels tougher, less squishy in your hand than before.",false);
                  itemAdd(538);
               }
               else if(chance <= 55)
               {
                  outputMainText("The egg now looks somewhat dimmer, but also has some more warmth to it than before.",false);
                  itemAdd(539);
               }
               else
               {
                  outputMainText("The egg now seems rather bland, not as gooey and more starchy than before.",false);
                  itemAdd(540);
               }
               doEnd();
            }
         };
      }
      else
      {
         this.outputMainText("You pop the egg into your mouth and bite down. The gooey stuff splorts about your mouth and... isn\'t exactly tasty. Even swallowing it makes your belly want to rebel. The act kills off some of your arousal, at least.",true);
         this.doLust(-3,0);
         this.doEnd();
      }
   }
   if(ID == 255)
   {
      this.outputMainText("You bring the flower to your nose and inhale deeply. It smells so good, the delightful scent filling your nostils and your lungs and leaving you feeling quite tingly all over.\r\rHowever, once you look back down afterwards, the flower has wilted and no longer has any scent at all...",true);
      this.stats(0,0,0,2);
      this.aff(11,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 256)
   {
      this.outputMainText("You suck on the hard candy, the nutrient-rich ingredients making you feel stronger as the sweet flavors fill your belly.",true);
      if(this.eggLaying > 0)
      {
         this.outputMainText(" And your womb gets a good workout, the pro-something bacteria or whatever helping with its functions. Or something.",false);
         this.eggTime -= 4;
      }
      this.stats(1,0,0,0);
      this.aff(12,Math.floor(this.percent() / 15 + 2),-2);
      this.doEnd();
   }
   if(ID == 257)
   {
      this.outputMainText("You drink down the potion. You immediately begin to feel very odd...",true);
      if(this.legType != 1002)
      {
         this.humanTaurAffinity = 100;
         this.legChange(1002);
         this.outputMainText("\r\rFor a normal human, having a second body would -technically- be more human than a human. Though you can see why it was a failure...",false);
      }
      else
      {
         this.outputMainText("\r\rBut the feeling passes as nothing happens.",false);
      }
      this.doEnd();
   }
   if(ID == 258)
   {
      this.outputMainText("You drink down the potion. You immediately begin to feel very odd...",true);
      if(this.legType != 1001)
      {
         this.cowTaurAffinity = 100;
         this.legChange(1001);
         this.outputMainText("\r\rIt\'s probably best that alchemist didn\'t sell it to others...",false);
      }
      else
      {
         this.outputMainText("\r\rBut the feeling passes as nothing happens.",false);
      }
      this.doEnd();
   }
   if(ID == 259)
   {
      this.outputMainText("You pop the candy into your mouth and let it slowly dissolve. You immediately realize that the \'sour\' comes before the \'sweet\', despite the name, and your face puckers up with the intensity, your pain subsiding in relation.",true);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" You pucker so hard that you can feel your cunt" + this.plural(2) + " stretch further into your body from the force, permanently slightly larger...",false);
         this.vagSizeMod += 0.05;
      }
      this.outputMainText("\r\rThen the sweetness comes along, your body relaxing and tingling from the blissful flavor.",false);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" You relax your body so much that your cock" + this.plural(1) + " droop out even further than usual, so far that they\'re permanently slightly longer...",false);
         this.cockSizeMod += 0.05;
      }
      this.doHP(5);
      this.doLust(5,0);
      this.doEnd();
   }
   if(ID == 260)
   {
      this.outputMainText("You gulp down the draft. The stuff is very thick and heady, nearly burning your throat on the way down. The warmth spreads from your belly, your mind becoming more focused while your body grows stronger, more mature, and taller.",true);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" Your " + this.cockDesc() + " cock" + this.plural(1) + " also grow" + this.plural(3) + " from the concentrated masculinity, bulging in your " + this.clothesBottom() + ".",false);
         this.cockChange(2,0);
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText(" However, unexpectedly, the concentrated masculinity causes your " + this.clitDesc() + " clit" + this.plural(2) + " to grow as well, pushing out your " + this.clothesBottom() + " further...",false);
         this.clitSize += 2;
      }
      this.body += 1;
      this.tallness += 1;
      this.stats(2,1,0,0);
      this.doEnd();
   }
   if(ID == 500)
   {
      this.outputMainText("You down the bottle of milk and feel refreshed!",true);
      this.doHP(10 + this.milkHPMod);
      this.exhaustion -= 2;
      this.doEnd();
   }
   if(ID == 501)
   {
      this.outputMainText("You guzzle down the jug of milk and feel very refreshed! And you feel like you have a rather full bladder...",true);
      this.doHP(40 + this.milkHPMod);
      this.exhaustion -= 6;
      this.doEnd();
   }
   if(ID == 502)
   {
      this.outputMainText("You pour the milk out of the barrel into 4 jugs...",true);
      this.itemAdd(501);
      this.itemAdd(501);
      this.itemAdd(501);
      this.itemAdd(501);
      this.doEnd();
   }
   if(ID == 503)
   {
      this.outputMainText("You take a swig of the draft, your loins warming within seconds.",true);
      this.doLust(20,0);
      this.doEnd();
   }
   if(ID == 504)
   {
      this.outputMainText("You down the potion, your body feeling much better than before.",true);
      this.doHP(30);
      this.doLust(-15,0);
      this.doEnd();
   }
   if(ID == 505)
   {
      if(this.currentState != 2)
      {
         this.outputMainText("You can only use this explosive potion in battle. You put the bad experiment back into your bag.",true);
         this.itemAdd(505);
         this.doEnd();
      }
      else
      {
         dmg = Math.floor(Math.random() * (1 + 20 - 10)) + 10;
         this.outputMainText("You pull the bad experiment from your bag and toss it at the " + this.enemyName() + ". The crude stuff explodes, far enough away to not harm you, dealing " + dmg + " damage!",true);
         this.doeHP(-dmg);
         this.doBattle();
      }
   }
   if(ID == 506)
   {
      if(this.pregCheck(0))
      {
         this.outputMainText("Drinking this potion, you can feel your " + this.bellyDesc() + " belly quiver, the offspring inside moving about. With a groan, you double over for a moment, your belly stretching beneath your hands. You can almost hear the " + this.skinDesc() + " creak, growing taut!",true);
         this.i = 0;
         while(this.i < this.pregArray.length)
         {
            if(this.pregArray[this.i] == true)
            {
               this.pregArray[this.i + 3] += 50;
            }
            this.i += 5;
         }
         this.outputMainText("\r\rA few moments pass before you gather yourself, standing upright once more. You are slightly more swollen now, wielding a " + this.bellyDesc() + " gut instead. Fortunately, both you and your offspring are uninjured, though it\'ll take a bit to get used to the sudden increase in size.",false);
         this.doEnd();
      }
      else
      {
         this.outputMainText("For some reason, you thought it necessary to drink this potion. It... doesn\'t seem to have any effect. Though you do strangely feel like you have to go to the bathroom all of a sudden...",true);
         this.doEnd();
      }
   }
   if(ID == 507)
   {
      if(this.balls > 0 && this.showBalls == true)
      {
         this.outputMainText("Downing the potion, you quickly begin to feel a slight ache in your " + this.ballDesc() + " testicles, like you haven\'t had an orgasm in a while...",true);
         this.blueBalls += 30;
         this.doEnd();
      }
      else if(this.balls > 0 && this.showBalls == false)
      {
         this.outputMainText("Downing the potion, you quickly begin to feel a slight ache in your abdomen, like you haven\'t had an orgasm in a while...",true);
         this.blueBalls += 30;
         this.doEnd();
      }
      else
      {
         this.outputMainText("Despite not having any balls to speak of, you drink this potion anyways. It does nothing. I hope you\'re happy.",true);
         this.doEnd();
      }
   }
   if(ID == 508)
   {
      this.outputMainText("You take a swig of the draft, your loins burning hot within seconds.",true);
      this.doLust(50,0);
      this.doEnd();
   }
   if(ID == 509)
   {
      this.outputMainText("You down the potion, your body feeling immensely better than before.",true);
      this.doHP(70);
      this.doLust(-40,0);
      this.doEnd();
   }
   if(ID == 510)
   {
      if(this.currentState != 2)
      {
         this.outputMainText("You can only use this explosive potion in battle. You put the bad experiment back into your bag.",true);
         this.itemAdd(510);
         this.doEnd();
      }
      else
      {
         dmg = Math.floor(Math.random() * (1 + 40 - 20)) + 20;
         this.outputMainText("You pull the super bad experiment from your bag and toss it at the " + this.enemyName() + ". The super crude stuff explodes superbly, far enough away to not harm you, dealing a super " + dmg + " damage!",true);
         this.doeHP(-dmg);
         this.doBattle();
      }
   }
   if(ID == 511)
   {
      if(this.pregCheck(0))
      {
         this.outputMainText("Drinking this potion, you can feel your " + this.bellyDesc() + " belly shake, the offspring inside moving about. With a groan, you double over for a moment, your belly stretching beneath your hands. You\'re pretty sure you can hear the " + this.skinDesc() + " creak, growing taut, to the point where you fear it will tear!",true);
         this.i = 0;
         while(this.i < this.pregArray.length)
         {
            if(this.pregArray[this.i] == true)
            {
               this.pregArray[this.i + 3] += 120;
            }
            this.i += 5;
         }
         this.outputMainText("\r\rA few moments pass before you gather yourself, standing upright once more, having a bit of difficulty doing so. You are much more swollen now, wielding a " + this.bellyDesc() + " gut instead. Fortunately, both you and your offspring are uninjured, though you\'re unsure if you\'ll be able to get used to this sudden increase in size...",false);
         this.doEnd();
      }
      else
      {
         this.outputMainText("For some reason, you thought it necessary to drink this potion. It... doesn\'t seem to have any effect. Though you do strangely wish there was a bathroom here all of a sudden...",true);
         this.doEnd();
      }
   }
   if(ID == 512)
   {
      if(this.balls > 0 && this.showBalls == true)
      {
         this.outputMainText("Downing the potion, you quickly begin to feel a great ache in your " + this.ballDesc() + " testicles, like you haven\'t had an orgasm in sooo long!",true);
         this.blueBalls += 70;
         this.doEnd();
      }
      else if(this.balls > 0 && this.showBalls == false)
      {
         this.outputMainText("Downing the potion, you quickly begin to feel a great ache in your abdomen, like you haven\'t had an orgasm in sooo long!",true);
         this.blueBalls += 70;
         this.doEnd();
      }
      else
      {
         this.outputMainText("Despite not having any balls to speak of, you drink this potion anyways. It does nothing. I hope you\'re happy.",true);
         this.doEnd();
      }
   }
   if(ID == 513)
   {
      if(this.gender == 1)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You pull " + this.pullUD(2) + " your " + this.clothesBottom() + " and watch as your " + this.cockDesc() + " cock" + this.plural(1) + " shrink more and more before eventually disappearing into your groin. Then, you hug your belly as you feel your insides wrench, making room for a small amount of vaginal flesh inside.",true);
         if(this.showBalls == true)
         {
            this.outputMainText(" Your " + this.ballDesc() + " balls squeeze up " + this.legWhere(1) + " your " + this.legDesc(2) + " before eventually melding into your " + this.skinDesc() + ", leaving behind 1 tiny pair of feminine lips.",false);
         }
         if(this.showBalls == false)
         {
            this.outputMainText(" The skin " + this.legWhere(1) + " your " + this.legDesc(2) + " swells slightly, forming two tiny mounds, 1 pair of new feminine lips.",false);
         }
         this.outputMainText(" The lips part, the fresh air making you shiver as it passes across the moist flesh within. Your hand passes over your clitoris, making you shiver slightly, before you dip your finger into your new cunny, amazed at the sensation of being penetrated like that. For all intents and purposes, you are now a girl.",false);
         this.balls = 0;
         this.ballSize = 0;
         this.cockSize = 0;
         this.stats(0,0,-(2 * (this.cockTotal - 1)),0);
         this.cockTotal = 0;
         this.humanCocks = 0;
         this.horseCocks = 0;
         this.wolfCocks = 0;
         this.catCocks = 0;
         this.lizardCocks = 0;
         this.rabbitCocks = 0;
         this.bugCocks = 0;
         this.vagBellyChange(1,1);
         this.vagTotal = 1;
         this.pregArray = [false,0,0,0,0];
         this.vagSize = 1;
         this.vulvaSize = 1;
         this.clitSize = 1;
         this.gender = 2;
      }
      else if(this.gender == 2)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You hug your belly as you feel your insides wrench, your vaginal flesh shrinking within.",true);
         this.cockChange(1,1);
         this.outputMainText("\r\rHowever, it doesn\'t last long as the last of your vagina" + this.plural(2) + " shrink" + this.plural(4) + " to nothing, your " + this.vulvaDesc() + " lips disintegrating back against your groin before finally vanishing, making you a boy for all intents and purposes.",false);
         this.vagChange(-1,0);
         this.vagBellyChange(-this.vagSize,-this.vagTotal);
         this.stats(0,0,-(2 * (this.vagTotal - 1)),0);
         this.vagSize = 0;
         this.vagTotal = 0;
         this.i = 0;
         while(this.i < this.pregArray.length)
         {
            if(this.pregArray[this.i] == false)
            {
               this.pregArray.splice(this.i,5);
               this.i = -5;
            }
            this.i += 5;
         }
         this.vulvaSize = 0;
         this.clitSize = 0;
         this.gender = 1;
      }
      else if(this.gender == 3)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You hug your belly as you feel your insides wrench, your vaginal flesh shrinking within. Your " + this.clothesBottom() + " feels loser as your " + this.cockDesc() + " bulges dwindle as well.",true);
         if(this.showBalls == true)
         {
            this.outputMainText(" Even your testicles shrivel up, growing smaller and smaller.",false);
         }
         this.outputMainText("\r\rBy the time you finally pull " + this.pullUD(2) + " your " + this.clothesBottom() + ", all your attributes are like that of a childs...",false);
         this.vagChange(-1,0);
         this.vagBellyChange(-(this.vagSize - 1),0);
         this.ballSize = 1;
         this.cockSize = 1;
         this.vagSize = 1;
         this.vulvaSize = 1;
         this.clitSize = 1;
      }
      else if(this.gender == 0)
      {
         chance = this.percent();
         this.outputMainText("You ingest the potion and quickly begin to feel its effects.",true);
         if(chance <= 40)
         {
            this.cockChange(1,1);
         }
         if(chance > 40 && chance <= 80)
         {
            this.vagChange(1,1);
         }
         if(chance > 80)
         {
            this.cockChange(1,1);
            this.vagChange(1,1);
         }
      }
      this.doEnd();
   }
   if(ID == 514)
   {
      this.outputMainText("After drinking the potion, your body feels tingly all over. You have the odd feeling like it would be fun to be whipped right about now...",true);
      this.masoPot += 24;
      this.doEnd();
   }
   if(ID == 515)
   {
      this.dyeThing(ID,1);
   }
   if(ID == 516)
   {
      this.outputMainText("Taking the potion, you sudden feel less... fertile than before. You might still be a little fertile, but you suspect you can go out \'clubbing\' for the next few days and not have to worry so much about a little extra weight in a few more. If you knew what any of that even meant.",true);
      this.babyFree += 72;
      this.doEnd();
   }
   if(ID == 517)
   {
      if(this.showBalls == true && this.balls > 0)
      {
         this.outputMainText("Within seconds of drinking this potion, you can feel your balls grow slightly warmer. You can almost hear them hum as they work harder to produce more fun goop for your cock" + this.plural(1) + ".",true);
      }
      else if(this.showBalls == true && this.balls > 0)
      {
         this.outputMainText("Within seconds of drinking this potion, you can feel your abdomen grow slightly warmer. You can almost hear something inside hum as it works harder to produce more fun goop for your cock" + this.plural(1) + ".",true);
      }
      else
      {
         this.outputMainText("If you had balls to be kicked in, they\'d probably be feeling more active right now. Not that you would know, you ball-less freak.",true);
      }
      this.cumMod += 0.2;
      this.doEnd();
   }
   if(ID == 518)
   {
      if(this.gender == 1)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You pull " + this.pullUD(2) + " your " + this.clothesBottom() + " and watch as your " + this.cockDesc() + " cock" + this.plural(1) + " shrink more and more before eventually disappearing into your groin. Then, you hug your belly as you feel your insides wrench, making room for an equal amount of vaginal flesh inside.",true);
         if(this.showBalls == true)
         {
            this.outputMainText(" Your " + this.ballDesc() + " balls squeeze up " + this.legWhere(1) + " your " + this.legDesc(2) + " before eventually melding into your " + this.skinDesc() + ", forming mounds of equal size until you have " + this.cockTotal + " pair" + this.plural(1) + " of feminine lips.",false);
         }
         if(this.showBalls == false)
         {
            this.outputMainText(" The skin " + this.legWhere(1) + " your " + this.legDesc(2) + " swells slightly, forming mounds of plush flesh, " + this.cockTotal + " pair" + this.plural(1) + " of new feminine lips.",false);
         }
         this.outputMainText(" The lips part, the fresh air making you shiver as it passes across the moist flesh within. Your hand passes over your new clit" + this.plural(1) + ", making you shiver slightly, before you dip your finger into " + this.oneYour(1) + " new cunt" + this.plural(1) + ", amazed at the sensation of being penetrated like that. For all intents and purposes, you are now a girl.",false);
         this.vagBellyChange(this.cockSize,this.cockTotal);
         this.vagTotal = this.cockTotal;
         this.i = 1;
         while(this.i <= this.vagTotal)
         {
            if(this.pregArray.length / 5 < 1)
            {
               this.pregArray = [false,0,0,0,0];
               ++this.i;
            }
            else if(this.pregArray.length / 5 < this.vagTotal)
            {
               this.pregArray.push(false,0,0,0,0);
               ++this.i;
            }
            else
            {
               ++this.i;
            }
         }
         this.vagSize = this.cockSize;
         this.vulvaSize = this.ballSize;
         this.clitSize = this.ballSize;
         this.balls = 0;
         this.ballSize = 0;
         this.cockSize = 0;
         this.cockTotal = 0;
         this.humanCocks = 0;
         this.horseCocks = 0;
         this.wolfCocks = 0;
         this.catCocks = 0;
         this.lizardCocks = 0;
         this.rabbitCocks = 0;
         this.bugCocks = 0;
         this.gender = 2;
      }
      else if(this.gender == 2)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You hug your belly as you feel your insides wrench, your vaginal flesh shrinking within.",true);
         this.cockChange(this.vagSize,this.vagTotal);
         this.outputMainText("\r\rHowever, it doesn\'t last long as the last of your vagina" + this.plural(2) + " shrink" + this.plural(4) + " to nothing, your " + this.vulvaDesc() + " lips disintegrating into your new scrotum, your testicles growing larger and larger before your lips finally vanish, making you a boy for all intents and purposes.",false);
         this.ballSize = this.vulvaSize;
         this.vagBellyChange(-this.vagSize,-this.vagTotal);
         this.vagSize = 0;
         this.vagTotal = 0;
         this.i = 0;
         while(this.i < this.pregArray.length)
         {
            if(this.pregArray[this.i] == false)
            {
               this.pregArray.splice(this.i,5);
               this.i = -5;
            }
            this.i += 5;
         }
         this.vulvaSize = 0;
         this.clitSize = 0;
         this.gender = 1;
      }
      else if(this.gender == 3)
      {
         this.outputMainText("You ingest the potion and quickly begin to feel its effects. You hug your belly as you feel your insides wrench, your vaginal flesh attempting to match the size of your male anatomy. Your " + this.clothesBottom() + " shakes as your " + this.cockDesc() + " bulges try to mimic your female anatomy as well.",true);
         if(this.showBalls == true)
         {
            this.outputMainText(" Even your testicles shift, growing to match your pussy lips, while those lips do the same. Your clit" + this.plural(2) + " also change" + this.plural(4) + " to more closely match the size of your different vulva.",false);
         }
         else
         {
            this.outputMainText("Even your pussy lips shift, trying to match the size of what\'s in your abdomen. Your clit" + this.plural(2) + " also change" + this.plural(4) + " to more closely match the size of your different vulva.",false);
         }
         this.outputMainText(" In the end, your whole body feels a little off balanced, having to adjust to the backwards genitals...",false);
         tempCockSize = this.cockSize;
         tempBallSize = this.ballSize;
         this.cockSize = this.vagSize;
         this.ballSize = this.vulvaSize;
         this.vagBellyChange(tempCockSize - this.vagSize,0);
         this.vagChange(-1,0);
         this.vagSize = tempCockSize;
         this.vulvaSize = tempBallSize;
         this.clitSize = tempBallSize;
      }
      else if(this.gender == 0)
      {
         chance = this.percent();
         this.outputMainText("You ingest the potion and quickly begin to feel its effects.",true);
         if(chance <= 40)
         {
            this.cockChange(Math.ceil(this.percent() / 5),1);
            this.ballSize = Math.ceil(this.percent() / 5);
         }
         if(chance > 40 && chance <= 80)
         {
            this.vagChange(Math.ceil(this.percent() / 5),1);
            this.vulvaSize = Math.ceil(this.percent() / 5);
            this.clitSize = Math.ceil(this.percent() / 5);
         }
         if(chance > 80)
         {
            this.cockChange(Math.ceil(this.percent() / 5),1);
            this.vagChange(Math.ceil(this.percent() / 5),1);
            this.ballSize = Math.ceil(this.percent() / 5);
            this.vulvaSize = Math.ceil(this.percent() / 5);
            this.clitSize = Math.ceil(this.percent() / 5);
         }
      }
      this.doEnd();
   }
   if(ID == 519)
   {
      this.outputMainText("After drinking the potion, your body feels like electricity is sparking all over. You have the odd feeling like it would be fun to be beaten to a pulp right about now...",true);
      this.sMasoPot += 24;
      this.doEnd();
   }
   if(ID == 520)
   {
      this.dyeThing(ID,3);
   }
   if(ID == 521)
   {
      this.outputMainText("Taking the potion, you sudden feel less... fertile than before. You might still be a little fertile, but you suspect you can go out \'clubbing\' for the next several days and not have to worry so much about a little extra weight afterwards. If you knew what any of that even meant.",true);
      this.babyFree += 216;
      this.doEnd();
   }
   if(ID == 522)
   {
      if(this.showBalls == true && this.balls > 0)
      {
         this.outputMainText("Within seconds of drinking this potion, you can feel your balls grow slightly hotter. You can almost hear them whir as they work harder to produce more fun goop for your cock" + this.plural(1) + ".",true);
      }
      else if(this.showBalls == true && this.balls > 0)
      {
         this.outputMainText("Within seconds of drinking this potion, you can feel your abdomen grow slightly hotter. You can almost hear something inside whir as it works harder to produce more fun goop for your cock" + this.plural(1) + ".",true);
      }
      else
      {
         this.outputMainText("If you had balls to be kicked in, they\'d probably be feeling much more active right now. Not that you would know, you ball-less freak.",true);
      }
      this.cumMod += 0.5;
      this.doEnd();
   }
   if(ID == 523)
   {
      this.outputMainText("You pop open the vial of cum and let it ooze down your throat, shivering a bit from the heady taste.",true);
      this.doHP(2);
      this.doLust(5,0);
      this.doEnd();
   }
   if(ID == 524)
   {
      this.outputMainText("You gulp down the thick, creamy, sticky cum, having difficulty getting down the large amount of hot spunk with its heady taste.",true);
      this.doHP(5);
      this.doLust(15,0);
      this.doEnd();
   }
   if(ID == 525)
   {
      this.outputMainText("You pour the jug of cum out into 3 bottles...",true);
      this.itemAdd(524);
      this.itemAdd(524);
      this.itemAdd(524);
      this.doEnd();
   }
   if(ID == 526)
   {
      if(this.currentState == 2)
      {
         this.outputMainText("You have no use for a barrel full of cum in the midst of battle, so you... tuck it away somewhere in your bag?",true);
         this.itemAdd(526);
         this.doEnd();
      }
      else
      {
         this.outputMainText("Without much of a use for it otherwise, you decide to... strip down naked and jump in!\r\rThe cum is nice and warm and feels so good on your " + this.skinDesc() + ". You scrub yourself nice and thoroughly, making sure to get all the nooks and crannies. And with the slimy goop, you really focus on those crannies~\r\rAfter cleaning yourself up a bit, you sit back and relax, pulling out a toy to play with.\r\r\r\'Oh rubber ducky, you\'re the one. You make bath-time lots of fun~\'",true);
         this.stats(0,0,1,1);
         ++this.hrs;
         this.doEnd();
      }
   }
   if(ID == 527)
   {
      this.outputMainText("You crack open the good egg and down its contents, feeling healthier and stronger already.",true);
      this.doHP(15);
      this.stats(1,0,0,0);
      this.doEnd();
   }
   if(ID == 528)
   {
      if(this.currentState != 2)
      {
         this.outputMainText("You can only use this dangerous egg in battle. You put the bad egg back into your bag.",true);
         this.itemAdd(528);
         this.doEnd();
      }
      else
      {
         dmg = Math.floor(Math.random() * (1 + 20 - 10)) + 10;
         this.outputMainText("You pull the bad egg from your bag and toss it at the " + this.enemyName() + ". It explodes in a burst of fire, somehow, dealing " + dmg + " damage!",true);
         this.doeHP(-dmg);
         if(this.currentState == 2)
         {
            this.doEnd();
         }
      }
   }
   if(ID == 529)
   {
      this.outputMainText("You crack open the strange egg and down its contents, feeling odd...",true);
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYou grow an inch taller.",false);
         ++this.tallness;
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYou shrink by an inch.",false);
         --this.tallness;
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYour chest springs out, swelling in size.",false);
         this.breastSize += Math.ceil(this.percent() / 10);
      }
      if(this.percent() <= 10 && this.breastSize > 1)
      {
         this.outputMainText("\r\rYour breasts recoil back, deflating.",false);
         this.breastSize -= Math.ceil(this.percent() / 10);
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYour crotch feels strange as some feminine bits begin to appear...",false);
         this.vagChange(Math.ceil(this.percent() / 10),Math.ceil(this.percent() / 20));
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYour crotch feels strange as some masculine bits begin to appear...",false);
         this.cockChange(Math.ceil(this.percent() / 10),Math.ceil(this.percent() / 20));
      }
      if(this.percent() <= 10 && this.cockTotal > 0)
      {
         this.outputMainText("\r\rYour cock" + this.plural(1) + " grow" + this.plural(3) + " sporadically.",false);
         this.cockChange(Math.ceil(this.percent() / 10),0);
      }
      if(this.percent() <= 10 && this.cockTotal > 0)
      {
         this.outputMainText("\r\rYour cock" + this.plural(1) + " shrink" + this.plural(3) + " sporadically.",false);
         this.cockChange(-Math.ceil(this.percent() / 10),0);
      }
      if(this.percent() <= 10 && this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour vulva" + this.plural(2) + " grow" + this.plural(4) + " sporadically.",false);
         this.vagChange(Math.ceil(this.percent() / 10),0);
         this.vulvaSize += Math.ceil(this.percent() / 10);
         this.clitSize += Math.ceil(this.percent() / 10);
      }
      if(this.percent() <= 10 && this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour vulva" + this.plural(2) + " shrink" + this.plural(4) + " sporadically.",false);
         this.vagChange(-Math.ceil(this.percent() / 10),0);
         this.vulvaSize -= Math.ceil(this.percent() / 10);
         this.clitSize -= Math.ceil(this.percent() / 10);
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rIt feels as though your blood has thinned out a bit.",false);
         this.aff(0,0,-10);
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYou suddenly feel very aroused.",false);
         this.doLust(50,0);
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\rYour arousal suddenly dies down.",false);
         this.doLust(-50,0);
      }
      if(this.percent() <= 10)
      {
         this.outputMainText("\r\r10 coins pop out of your ears.",false);
         this.doCoin(10);
      }
      if(this.percent() <= 10 && this.vagTotal > 0)
      {
         this.outputMainText("\r\rYou grunt and squat, " + this.legVerb(1) + " your " + this.legDesc(2) + " and pulling " + this.pullUD(2) + " your " + this.clothesBottom() + " in time for more fresh eggs to come sliding out of your slit" + this.plural(2) + " from nowhere!",false);
         this.itemAdd(219);
         this.itemAdd(219);
         this.itemAdd(219);
      }
      this.outputMainText("\r\rQuite strange indeed...",false);
      this.doEnd();
   }
   if(ID == 530)
   {
      this.outputMainText("You crack the charmed egg open and gulp its contents. You suddenly feel charming, oh so charming, it\'s alarming how charming you feeeeel~",true);
      if(this.charmTime <= 0)
      {
         this.enticeMod += 13;
         this.charmTime = 20;
      }
      else
      {
         this.charmTime += 20;
      }
      this.stats(0,1,0,0);
      this.doEnd();
   }
   if(ID == 531)
   {
      this.outputMainText("You can nearly hear the sounds of an angelic chorus as you crack the divine egg open, its gooey contents slipping down your throat.",true);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" Your " + this.cockDesc() + " cock" + this.plural(1) + " pulse" + this.plural(3) + " and bulge" + this.plural(3) + " in your " + this.clothesBottom() + ", swelling in size.",false);
         if(this.showBalls == true)
         {
            this.outputMainText(" Your balls groan to match the amount of growth, expanding in their confines.",false);
         }
         this.outputMainText(" You can feel the cum churn within your body, trying to make room for more.",false);
         this.cockChange(5,0);
         this.ballSize += 5;
         this.cumMod += 0.5;
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText(" Your loins ache as your nether-lips grow between your thighs, your pelvis literally spreading to make more room as your " + this.hipDesc() + " hips press outward. Your ovaries tickle a little as they spill their eggs for easier fertilization. Even your " + this.boobDesc() + " breasts feel heavier, your " + this.nipDesc() + "nipples growing longer for greater mouthfuls.",false);
         this.vagChange(5,0);
         this.hips += 5;
         this.vulvaSize += 5;
         this.pregChanceMod += 5;
         this.extraPregChance += 10;
         this.boobChange(5);
      }
      this.doEnd();
   }
   if(ID == 532)
   {
      this.outputMainText("You rub the strong-scented pheromones all over your body. It\'s so... powerful that even you feel a little rambunctious just wearing it. Others would probably find it much more enticing as well, strengthening their attraction to you.",true);
      if(this.pheromone <= 0)
      {
         this.pheromone = 30;
         this.enticeMod += 25;
         this.statsMod(0,0,3,0);
      }
      else
      {
         this.pheromone += 30;
      }
      this.doEnd();
   }
   if(ID == 533)
   {
      this.choiceListArray = [];
      if(this.breastSize > 0)
      {
         this.choiceListArray.push("Breasts");
      }
      if(this.nippleSize > 1)
      {
         this.choiceListArray.push("Nipples");
      }
      if(this.butt > 1)
      {
         this.choiceListArray.push("Butt");
      }
      if(this.hips > 1)
      {
         this.choiceListArray.push("Hips");
      }
      if(this.vagTotal > 0)
      {
         this.choiceListArray.push("Pussy");
         if(this.vulvaSize > 0)
         {
            this.choiceListArray.push("Vulva");
         }
         if(this.clitSize > 1)
         {
            this.choiceListArray.push("Clit");
         }
      }
      if(this.cockTotal > 0)
      {
         this.choiceListArray.push("Cock");
         if(this.showBalls == true && this.ballSize > 1)
         {
            this.choiceListArray.push("Balls");
         }
      }
      if(this.udders == true)
      {
         if(this.udderSize > 1)
         {
            this.choiceListArray.push("Udder");
         }
         if(this.teatSize > 2)
         {
            this.choiceListArray.push("Teats");
         }
      }
      if(this.bellyMod > 0)
      {
         this.choiceListArray.push("Belly");
      }
      this.choiceListButtons("Reduc Reduc");
      this.outputMainText("Select which body part you would like to shrink a bit. If you don\'t have that part, this elixir will do nothing but will still be consumed.",true);
      this.doListen = function():void
      {
         choiceListSelect("Reduc Reduc");
         outputMainText("You splash the elixir out onto your ",true);
         if(choiceListResult[0] == "Cock")
         {
            outputMainText(cockDesc() + " cock" + plural(1),false);
            outputMainText(" and watch the appendage" + plural(1) + " quiver and shrivel down by " + 2 * cockSizeMod + " inches.",false);
            cockChange(-4,0);
         }
         if(choiceListResult[0] == "Balls")
         {
            outputMainText(ballDesc() + " balls",false);
            ballSize -= 4;
            outputMainText(" and watch with a shiver as the orbs shrink.",false);
         }
         if(choiceListResult[0] == "Pussy")
         {
            outputMainText("vagina" + plural(2),false);
            outputMainText(" and quiver as the fleshy walls within your body shrink.",false);
            vagChange(-4,0);
         }
         if(choiceListResult[0] == "Vulva")
         {
            outputMainText(vulvaDesc() + " vulva",false);
            vulvaSize -= 4;
            outputMainText(" and watch with a quiver as nether-lips shrink, becoming " + vulvaDesc() + ".",false);
         }
         if(choiceListResult[0] == "Clit")
         {
            outputMainText(clitDesc() + " clit" + plural(2),false);
            clitSize -= 4;
            outputMainText(" and watch with a quiver as the button" + plural(2) + " shrink" + plural(4) + ", becoming " + clitDesc() + ".",false);
         }
         if(choiceListResult[0] == "Breasts")
         {
            outputMainText(boobDesc() + " breasts",false);
            breastSize -= 4;
            outputMainText(" and shudder as they shrink by about 2 inches.",false);
         }
         if(choiceListResult[0] == "Nipples")
         {
            outputMainText(nipDesc() + " nipples",false);
            nippleSize -= 4;
            outputMainText(" and shudder as they receed into your breasts nearly an inch.",false);
         }
         if(choiceListResult[0] == "Udder")
         {
            outputMainText(udderDesc() + " udder",false);
            udderSize -= 4;
            outputMainText(" and watch as it shrivels, becoming " + udderDesc() + ".",false);
         }
         if(choiceListResult[0] == "Teats")
         {
            outputMainText(teatDesc() + " teats",false);
            teatSize -= 4;
            outputMainText(" and watch as they recede, becoming " + teatDesc() + ".",false);
         }
         if(choiceListResult[0] == "Butt")
         {
            outputMainText(buttDesc() + " butt",false);
            butt -= 4;
            outputMainText(" and squirm as it shrinks, becoming " + buttDesc() + ".",false);
         }
         if(choiceListResult[0] == "Hips")
         {
            outputMainText(hipDesc() + " hips",false);
            hips -= 4;
            outputMainText(" and squirm as they narrow, becoming " + hipDesc() + ".",false);
         }
         if(choiceListResult[0] == "Belly")
         {
            outputMainText(bellyDesc() + " belly",false);
            bellyMod -= 4;
            outputMainText(" and watch as some of the fat burns off, becoming " + bellyDesc() + ".",false);
         }
         if(buttonChoice == 4 || buttonChoice == 8)
         {
            choiceListButtons("Reduc Reduc");
         }
         else if(buttonChoice == 12)
         {
            itemAdd(533);
            doProcess();
         }
         else
         {
            doEnd();
         }
      };
   }
   if(ID == 534)
   {
      this.outputMainText("You pop the pill into your mouth, feeling a bit of warmth emanating from your groin.",true);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" You pull " + this.pullUD(2) + " your " + this.clothesBottom() + " and watch with awe as your shlong" + this.plural(1) + " grow longer",false);
         if(this.showBalls == true)
         {
            this.outputMainText(" and the testicles beneath swell within your scrotum",false);
         }
         this.outputMainText(".\r\rIt really does work!",false);
         this.cockSize += 4;
         this.ballSize += 2;
      }
      else if(this.gender == 2)
      {
         this.outputMainText(" Yet, despite not having any male genitals to speak of, you feel something growing longer. Pulling " + this.pullUD(2) + " your " + this.clothesBottom() + ", you watch with awe as your clit" + this.plural(2) + " extends further from " + this.plural(6) + " hood" + this.plural(2) + "! You also feel more... horny than usual...\r\rThough the pill was meant for males, females have quite a bit in common.",false);
         this.clitSize += 3;
         this.stats(0,0,1,0);
      }
      else
      {
         this.outputMainText("\r\rYou don\'t have any genitals for it to enhance though, so it was kind of a waste.",false);
      }
      this.doEnd();
   }
   if(ID == 535)
   {
      this.outputMainText("You gulp down the vial of Milk Suppressant. You don\'t notice much of a difference, except that your " + this.nipDesc() + " nipples",true);
      if(this.udders == true)
      {
         this.outputMainText(" and " + this.teatDesc() + " teats",false);
      }
      this.outputMainText(" stiffen to such a point that they feel almost rock-hard. They don\'t really settle down either, like they\'re trying to hold something back.",false);
      this.milkSuppressant += 48;
      this.milkSuppressantLact = this.lactation;
      this.milkSuppressantUdder = this.udderLactation;
      this.lactation = 0;
      this.udderLactation = 0;
      this.doEnd();
   }
   if(ID == 536)
   {
      this.outputMainText("You pop the little growing orb into your mouth and quickly gulp it down past your gag reflex. It doesn\'t take long before your chest begins to feel warm...",true);
      if(this.boobTotal == 2)
      {
         this.outputMainText("\r\rYour chest, close beneath your nipples, begins to tickle. A new pair of sensitive areolas form amongst your " + this.skinDesc() + ", creating an extra row of breasts beneath the originals.",false);
         if(this.breastSize > 4)
         {
            this.outputMainText(" The new nipples protrude as fleshy mounds form from beneath them. The new boobs wobble as they grow to the same size of your original pair, lifting the originals slightly with their girth.\tWhen you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",false);
         }
         this.boobTotal = 4;
         this.fourBoobAffinity = 100;
         this.twoBoobAffinity = 0;
      }
      else if(this.boobTotal == 4)
      {
         this.outputMainText("\r\rYour chest and belly tickle. Two new nipples form amongst your " + this.skinDesc() + ", right below your second pair above your belly, leaving you with three rows of two breasts.",false);
         if(this.breastSize > 4)
         {
            this.outputMainText(" The nipples protrude as fleshy mounds form beneath them, while your second pair seems to shrink in turn. Breast-flesh wobbles, each row a fraction in size of the one above it. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",false);
         }
         this.boobTotal = 6;
         this.sixBoobAffinity = 100;
         this.fourBoobAffinity = 0;
      }
      else if(this.boobTotal == 6)
      {
         this.outputMainText("\r\rYour chest and belly tickle. Two new nipples form amongst your " + this.skinDesc() + ", right below your second pair above your belly, leaving you with four rows of two breasts, from chest to your lower belly.",false);
         if(this.breastSize > 4)
         {
            this.outputMainText(" The lower pairs continue to grow while your top pair shrinks a little, all equalizing in size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",false);
         }
         this.boobTotal = 8;
         this.eightBoobAffinity = 100;
         this.sixBoobAffinity = 0;
      }
      else if(this.boobTotal == 8)
      {
         this.outputMainText("\r\rThe area above your crotch tickles. Two new nipples form amongst your " + this.skinDesc() + ", right below your fourth pair below your belly, leaving you with five rows of two breasts, from your chest to your crotch.",false);
         if(this.breastSize > 4)
         {
            this.outputMainText(" The lower pairs continue to grow while your top pair shrinks a little, all equalizing in size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",false);
         }
         this.boobTotal = 10;
         this.tenBoobAffinity = 100;
         this.eightBoobAffinity = 0;
      }
      else if(this.boobTotal == 10)
      {
         this.outputMainText("\r\rYour chest down to your crotch starts to tickle. Checking, you see dozens of nipples beginning to appear amongst your breasts, going down to your groin and some even on your back. Mound of flesh begin growing everywhere until you\'re surrounded by tits!\r\rThen, a popping whir begins to fill the air. In a puff of pink smoke, all your breasts disappear at once, save the single primary pair upon your chest. It seems you have gone a bit overboard with the boobage...",false);
         this.boobTotal = 2;
         this.twoBoobAffinity = 100;
         this.tenBoobAffinity = 0;
      }
      this.doEnd();
   }
   if(ID == 537)
   {
      this.outputMainText("You munch on the egg, the wonderful flavors flowing over your tongue. It\'s sweet and buttery, quickly sliding down your gullet with delight until you\'re sucking the leftovers from your fingers. And as you ruminate over the delicious snack, you feel your " + this.clothesBottom() + " grow tighter. Your hips grow wider and your rump larger,",true);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" the lips of your sex swelling as well, while your womb becomes more efficient,",false);
         this.pregRate += 0.05;
         this.vulvaSize += 1;
      }
      this.outputMainText(" and your " + this.boobDesc() + " chest feels slightly bigger on the inside than on the outside. Growing more suitable for a breeding queen.",false);
      this.hips += 1;
      this.butt += 1;
      this.milkCap += 4;
      this.doEnd();
   }
   if(ID == 538)
   {
      this.outputMainText("You bite down into the egg, getting through the tougher rind and giving it a good chew before you swallow. It takes a bit to get through the whole thing and by the time you\'re done the ground looks further away than usual. You\'ve grown slightly taller and feel more lean and strong.",true);
      this.tallness += 1;
      this.body += 1;
      this.stats(1,0,0,0);
      this.doEnd();
   }
   if(ID == 539)
   {
      this.outputMainText("You gobble down the egg, your mind quickly drifting more towards lustful thoughts.",true);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" Your cock" + this.plural(1) + " grow" + this.plural(3) + " slightly larger, more able to ensure a deeper injection of your seed.",false);
         this.cockSize += 1;
         if(this.showBalls == true)
         {
            this.outputMainText(" Your balls also feel more ready to spurt, as though you\'ve gone many more hours without ejaculation than you actually have.",false);
         }
         this.blueBalls += 10;
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText(" And though " + this.plural(8) + " not actually something that can impregnate, your clit" + this.plural(2) + " swell" + this.plural(4) + " slightly larger.",false);
         this.clitSize += 1;
      }
      this.stats(0,-1,1,0);
      this.doEnd();
   }
   if(ID == 540)
   {
      this.outputMainText("You quickly chomp down the egg. It doesn\'t exactly taste good or bad, but that doesn\'t really matter. You just feel like you\'ve got more energy to keep working!",true);
      this.exhaustion -= 6;
      this.doEnd();
   }
}
!def DoStash():
   this.hideAmount();
   this.viewButtonOutline(0,0,0,1,0,0,0,1,0,0,0,1);
   this.viewButtonText(0,0,0,1,0,0,0,1,0,0,0,1);
   this.buttonWrite(4,"Store");
   this.buttonWrite(8,"Remove");
   this.buttonWrite(12,"Return");
   this.outputMainText("Click \'Store\' to store an item from your bag in the stash.\r\rClick \'Remove\' to remove an item from your stash and put it into your bag.\r\rClick \'Return\' to leave your stash.",true);
   this.doListen = function():void
   {
      if(buttonChoice == 4)
      {
         doStoreStash();
      }
      if(buttonChoice == 8)
      {
         doRemoveStash();
      }
      if(buttonChoice == 12)
      {
         doReturn();
      }
   };
}
!def DoStoreStash():
!def DoRemoveStash():
!def StashStore(storeItem:int):
!def StashRemove(storeItem:int):
!def StashSlotAdd():
!def StashSlotRemove():
!def DoShops():
!def DoShop():
!def DoSell():
def GoodsID(goodsSlot:int):
   global currentZone
   goodNum = 0
   if (currentZone == 1):
      if (goodsSlot == 1):
         goodNum = 104
      if (goodsSlot == 2):
         goodNum = 111
      if (goodsSlot == 3):
         goodNum = 116
      if (goodsSlot == 5):
         goodNum = 500
      if (goodsSlot == 6):
         goodNum = 501
      if (goodsSlot == 7):
         goodNum = 108
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 121
   if (currentZone == 2):
      if (goodsSlot == 1):
         goodNum = 102
      if (goodsSlot == 2):
         goodNum = 112
      if (goodsSlot == 3):
         goodNum = 117
      if (goodsSlot == 5):
         goodNum = 106
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 122
   if (currentZone == 3):
      if (goodsSlot == 1):
         goodNum = 101
      if (goodsSlot == 2):
         goodNum = 113
      if (goodsSlot == 3):
         goodNum = 118
      if (goodsSlot == 5):
         goodNum = 120
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 123
   if (currentZone == 4):
      if (goodsSlot == 2):
         goodNum = 114
      if (goodsSlot == 3):
         goodNum = 119
      if (goodsSlot == 5):
         goodNum = 103
      if (goodsSlot == 6):
         goodNum = 105
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 124
   if (currentZone == 6):
      if (goodsSlot == 1):
         goodNum = 109
      if (goodsSlot == 2):
         goodNum = 126
      if (goodsSlot == 3):
         goodNum = 127
      if (goodsSlot == 5):
         goodNum = 103
      if (goodsSlot == 6):
         goodNum = 230
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 125
   if (currentZone == 12):
      if (goodsSlot == 1):
         goodNum = 247
      if (goodsSlot == 2):
         goodNum = 250
      if (goodsSlot == 3):
         goodNum = 256
      if (goodsSlot == 5):
         goodNum = 120
      if (goodsSlot == 9):
         goodNum = 110
      if (goodsSlot == 10):
         goodNum = 115
      if (goodsSlot == 11):
         goodNum = 128
   return goodNum

!def DoDyeShop():
def DyeID(goodsSlot:int):
   goodNum = 0
   if (goodsSlot == 1):
      goodNum = 240
   if (goodsSlot == 2):
      goodNum = 241
   if (goodsSlot == 5):
      goodNum = 242
   if (goodsSlot == 6):
      goodNum = 243
   return goodNum

!def DyeThing():
!def DoApothecary():
def ApothID(goodsSlot:int):
   global currentZone, knowLustDraft, knowSRejuvPot, knowMasoPot, knowBabyFree, knowRejuvPot, knowSLustDraft, knowSMasoPot, knowBallSwell, knowPotPot, knowSGenSwap, knowExpPreg, knowGenSwap, knowSBabyFree, knowSExpPreg, knowSBallSwell, knowSPotPot, knowMilkSuppress
   goodNum = 0
   if (currentZone == 1):
      if (goodsSlot == 1):
         goodNum = 203
      if (goodsSlot == 2):
         goodNum = 209
      if (goodsSlot == 3):
         goodNum = 523
      if (goodsSlot == 7):
         if (knowLustDraft == False):
            goodNum = 1
      if (goodsSlot == 9):
         if (knowSRejuvPot == False):
            goodNum = 6
      if (goodsSlot == 10):
         if (knowMasoPot == False):
            goodNum = 10
      if (goodsSlot == 11):
         if (knowBabyFree == False):
            goodNum = 11
   if (currentZone == 2):
      if (goodsSlot == 1):
         goodNum = 209
      if (goodsSlot == 2):
         goodNum = 202
      if (goodsSlot == 3):
         goodNum = 206
      if (goodsSlot == 5):
         goodNum = 212
      if (goodsSlot == 6):
         goodNum = 524
      if (goodsSlot == 9):
         if (knowRejuvPot == False):
            goodNum = 2
      if (goodsSlot == 10):
         if (knowSLustDraft == False):
            goodNum = 5
      if (goodsSlot == 11):
         if (knowSMasoPot == False):
            goodNum = 14
   if (currentZone == 3):
      if (goodsSlot == 1):
         goodNum = 201
      if (goodsSlot == 2):
         goodNum = 202
      if (goodsSlot == 3):
         goodNum = 213
      if (goodsSlot == 3):
         goodNum = 203
      if (goodsSlot == 9):
         if (knowBallSwell == False):
            goodNum = 4
      if (goodsSlot == 10):
         if (knowPotPot == False):
            goodNum = 12
      if (goodsSlot == 11):
         if (knowSGenSwap == False):
            goodNum = 13
   if (currentZone == 4):
      if (goodsSlot == 1):
         goodNum = 210
      if (goodsSlot == 2):
         goodNum = 201
      if (goodsSlot == 3):
         goodNum = 218
      if (goodsSlot == 9):
         if (knowExpPreg == False):
            goodNum = 3
      if (goodsSlot == 10):
         if (knowGenSwap == False):
            goodNum = 9
      if (goodsSlot == 11):
         if (knowSBabyFree == False):
            goodNum = 15
   if (currentZone == 6):
      if (goodsSlot == 1):
         goodNum = 207
      if (goodsSlot == 2):
         goodNum = 213
      if (goodsSlot == 3):
         goodNum = 208
      if (goodsSlot == 5):
         goodNum = 228
      if (goodsSlot == 9):
         if (knowSExpPreg == False):
            goodNum = 7
      if (goodsSlot == 10):
         if (knowSBallSwell == False):
            goodNum = 8
      if (goodsSlot == 11):
         if (knowSPotPot == False):
            goodNum = 16
   if (currentZone == 12):
      if (goodsSlot == 9):
         if (knowMilkSuppress == False):
            goodNum = 17
   return goodNum

def ApothLearn(ID:int):
   global knowLustDraft, knowRejuvPot, knowExpPreg, knowBallSwell, knowSLustDraft, knowSRejuvPot,knowSExpPreg, knowSBallSwell, knowGenSwap, knowMasoPot, knowBabyFree, knowPotPot, knowSGenSwap, knowSMasoPot, knowSBabyFree, knowSPotPot, knowMilkSuppress
   if (ID == 1):
      knowLustDraft = True
   if (ID == 2):
      knowRejuvPot = True
   if (ID == 3):
      knowExpPreg = True
   if (ID == 4):
      knowBallSwell = True
   if (ID == 5):
      knowSLustDraft = True
   if (ID == 6):
      knowSRejuvPot = True
   if (ID == 7):
      knowSExpPreg = True
   if (ID == 8):
      knowSBallSwell = True
   if (ID == 9):
      knowGenSwap = True
   if (ID == 10):
      knowMasoPot = True
   if (ID == 11):
      knowBabyFree = True
   if (ID == 12):
      knowPotPot = True
   if (ID == 13):
      knowSGenSwap = True
   if (ID == 14):
      knowSMasoPot = True
   if (ID == 15):
      knowSBabyFree = True
   if (ID == 16):
      knowSPotPot = True
   if (ID == 17):
      knowMilkSuppress = True

def ApothName(ID:int):
   if (ID >= 200):
      return ItemName(ID)
   tempStr = ""
   if (ID == 1):
      tempStr = "R: LustDraft"
   if (ID == 2):
      tempStr = "R: RejuvPot"
   if (ID == 3):
      tempStr = "R: ExpPreg"
   if (ID == 4):
      tempStr = "R: BallSwell"
   if (ID == 5):
      tempStr = "R: SLustDraft"
   if (ID == 6):
      tempStr = "R: SRejuvPot"
   if (ID == 7):
      tempStr = "R: SExpPreg"
   if (ID == 8):
      tempStr = "R: SBallSwell"
   if (ID == 9):
      tempStr = "R: GenSwap"
   if (ID == 10):
      tempStr = "R: MasoPot"
   if (ID == 11):
      tempStr = "R: BabyFree"
   if (ID == 12):
      tempStr = "R: PotPot"
   if (ID == 13):
      tempStr = "R: SGenSwap"
   if (ID == 14):
      tempStr = "R: SMasoPot"
   if (ID == 15):
      tempStr = "R: SBabyFree"
   if (ID == 16):
      tempStr = "R: SPotPot"
   if (ID == 17):
      tempStr = "R: MilkSuppress"
   return tempStr

def ApothDescription(ID:int):
   if (ID >= 200):
      return ItemDescription(ID)
   tempStr = ""
   if (ID == 1):
      tempStr = "Recipe: Lust Draft" + "\n" + "\n" + "For those who need a boost in the bedroom." + "\n" + "\n" + "Alchemy difficulty: Simple"
   if (ID == 2):
      tempStr = "Recipe: Rejuvenation Potion" + "\n" + "\n" + "Useful for soothing what ailes you." + "\n" + "\n" + "Alchemy difficulty: Simple"
   if (ID == 3):
      tempStr = "Recipe: Express Pregnancy Potion" + "\n" + "\n" + "Helps quicken the gestation period." + "\n" + "\n" + "Alchemy difficulty: Simple"
   if (ID == 4):
      tempStr = "Recipe: Ball Sweller" + "\n" + "\n" + "Gives your nuts a jump in their production." + "\n" + "\n" + "Alchemy difficulty: Simple"
   if (ID == 5):
      tempStr = "Recipe: Superior Lust Draft" + "\n" + "\n" + "For when you've got a long night ahead with your spouse." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 6):
      tempStr = "Recipe: Superior Rejuvenation Potion" + "\n" + "\n" + "Greatly soothes your ailments." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 7):
      tempStr = "Recipe: Superior Express Pregnancy Potion" + "\n" + "\n" + "Because that baby just needs to get out." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 8):
      tempStr = "Recipe: Superior Ball Sweller" + "\n" + "\n" + "If you like that swollen, achy, full of seed feeling, this is what you want." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 9):
      tempStr = "Recipe: Gender Swap Potion" + "\n" + "\n" + "Don't like your current path in life? This will help start you off from a new perspective." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 10):
      tempStr = "Recipe: Masochism Potion" + "\n" + "\n" + "Makes some the pain feel pleasurable instead." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 11):
      tempStr = "Recipe: Baby Free Potion" + "\n" + "\n" + "A good contraceptive." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 12):
      tempStr = "Recipe: Potency Potion" + "\n" + "\n" + "Makes your testicles more efficient in their duties." + "\n" + "\n" + "Alchemy difficulty: Complex"
   if (ID == 13):
      tempStr = "Recipe: Superior Gender Swap Potion" + "\n" + "\n" + "For when you're bored and wanna try out something new." + "\n" + "\n" + "Alchemy difficulty: Advanced"
   if (ID == 14):
      tempStr = "Recipe: Superior Masochism Potion" + "\n" + "\n" + "Really helps take on the big fellas; all that soreness will be delightful instead." + "\n" + "\n" + "Alchemy difficulty: Advanced"
   if (ID == 15):
      tempStr = "Recipe: Superior Baby Free Potion" + "\n" + "\n" + "Necessary in Siz'Calit." + "\n" + "\n" + "Alchemy difficulty: Advanced"
   if (ID == 16):
      tempStr = "Recipe: Superior Potency Potion" + "\n" + "\n" + "Helps make sure you absolutely fertilize all those eggs with a good coating." + "\n" + "\n" + "Alchemy difficulty: Advanced"
   if (ID == 17):
      tempStr = "Recipe: Milk Suppressant" + "\n" + "\n" + "Sometimes all that leaking can be a bit of a nuisance... So, they came up with this!" + "\n" + "\n" + "Alchemy difficulty: Complex"
   return tempStr

def ApothValue(ID:int):
   tempNum = 0
   if (ID >= 200):
      return ItemValue(ID)
   if (ID == 1):
      tempNum = 20
   if (ID == 2):
      tempNum = 25
   if (ID == 3):
      tempNum = 25
   if (ID == 4):
      tempNum = 20
   if (ID == 5):
      tempNum = 35
   if (ID == 6):
      tempNum = 40
   if (ID == 7):
      tempNum = 35
   if (ID == 8):
      tempNum = 30
   if (ID == 9):
      tempNum = 45
   if (ID == 10):
      tempNum = 45
   if (ID == 11):
      tempNum = 40
   if (ID == 12):
      tempNum = 45
   if (ID == 13):
      tempNum = 60
   if (ID == 14):
      tempNum = 70
   if (ID == 15):
      tempNum = 55
   if (ID == 16):
      tempNum = 65
   if (ID == 17):
      tempNum = 35
   return tempNum

!def DoSalon():
def HairstyleName(ID:int):
   global hair
   tempStr = "HAIRSTYLE NAME ERROR " + hair
   if (ID == 0):
      tempStr = "None"
   if (ID == 1):
      tempStr = "Wavy"
   if (ID == 2):
      tempStr = "Pigtail"
   if (ID == 3):
      tempStr = "Ponytail"
   if (ID == 4):
      tempStr = "Straight"
   if (ID == 5):
      tempStr = "Buzzcut"
   if (ID == 6):
      tempStr = "Mohawk"
   if (ID == 7):
      tempStr = "Bun"
   if (ID == 8):
      tempStr = "Curly"
   if (ID == 9):
      tempStr = "B Pigtail"
   if (ID == 10):
      tempStr = "B Ponytail"
   if (ID == 11):
      tempStr = "Braided"
   if (ID == 12):
      tempStr = "Spiky"
   if (ID == 13):
      tempStr = "Emo"
   if (ID == 14):
      tempStr = "Afro"
   return tempStr

def HairDesc():
   global hair
   tempStr = "HAIR DESC ERROR " + hair
   if (hair == 1):
      tempStr = "wavy hair"
   if (hair == 2):
      tempStr = "hair pulled to the sides of your head in pigtails"
   if (hair == 3):
      tempStr = "hair pulled back into a ponytail"
   if (hair == 4):
      tempStr = "straight hair"
   if (hair == 5):
      tempStr = "really short hair"
   if (hair == 6):
      tempStr = "hair styled up into a mohawk"
   if (hair == 7):
      tempStr = "hair curled up into a bun"
   if (hair == 8):
      tempStr = "curly hair"
   if (hair == 9):
      tempStr = "hair pulled to the sides of your head in braided pigtails"
   if (hair == 10):
      tempStr = "hair pulled back into a braided ponytail"
   if (hair == 11):
      tempStr = "braided hair"
   if (hair == 12):
      tempStr = "spiky hair"
   if (hair == 13):
      tempStr = "straight, stiff hair covering an eye"
   if (hair == 14):
      tempStr = "giant poofball of hair"
   return tempStr

def HairC():
   global hairColor
   tempStr = "HAIR COLOR ERROR " + hairColor
   if (hairColor == 0):
      tempStr = ""
   if (hairColor == 1):
      tempStr = "black "
   if (hairColor == 2):
      tempStr = "blonde "
   if (hairColor == 3):
      tempStr = "red "
   if (hairColor == 4):
      tempStr = "blue "
   if (hairColor == 5):
      tempStr = "coral pink "
   if (hairColor == 6):
      tempStr = "auburn "
   if (hairColor == 7):
      tempStr = "brown "
   if (hairColor == 8):
      tempStr = "grey "
   if (hairColor == 9):
      tempStr = "white "
   return tempStr

def HairL():
   global hairLength
   tempStr = "HAIR LENGTH ERROR " + hairLength
   if (hairLength == 2):
      tempStr = "that is short enough to not dangle past your head"
   if (hairLength == 4):
      tempStr = "that reaches down to your shoulders"
   if (hairLength == 6):
      tempStr = "that reaches down your back"
   if (hairLength == 8):
      tempStr = "that reaches down to your butt"
   if (hairLength == 10):
      tempStr = "that reaches down to the ground"
   return tempStr

def HairstyleID(choice:int):
   global currentZone
   tempNum = 0
   if (currentZone == 1):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 4
      if (choice == 3):
         tempNum = 8
      if (choice == 5):
         tempNum = 2
      if (choice == 6):
         tempNum = 3
      if (choice == 7):
         tempNum = 12
      if (choice == 9):
         tempNum = 14
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   if (currentZone == 2):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 4
      if (choice == 3):
         tempNum = 8
      if (choice == 5):
         tempNum = 3
      if (choice == 6):
         tempNum = 10
      if (choice == 7):
         tempNum = 5
      if (choice == 9):
         tempNum = 6
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   if (currentZone == 3):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 4
      if (choice == 3):
         tempNum = 8
      if (choice == 5):
         tempNum = 6
      if (choice == 6):
         tempNum = 11
      if (choice == 7):
         tempNum = 12
      if (choice == 9):
         tempNum = 13
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   if (currentZone == 4):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 4
      if (choice == 3):
         tempNum = 8
      if (choice == 5):
         tempNum = 2
      if (choice == 6):
         tempNum = 9
      if (choice == 7):
         tempNum = 7
      if (choice == 9):
         tempNum = 13
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   if (currentZone == 6):
      if (choice == 1):
         tempNum = 2
      if (choice == 2):
         tempNum = 3
      if (choice == 3):
         tempNum = 4
      if (choice == 5):
         tempNum = 9
      if (choice == 6):
         tempNum = 10
      if (choice == 7):
         tempNum = 11
      if (choice == 9):
         tempNum = 12
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   if (currentZone == 12):
      if (choice == 1):
         tempNum = 2
      if (choice == 2):
         tempNum = 9
      if (choice == 3):
         tempNum = 6
      if (choice == 5):
         tempNum = 12
      if (choice == 6):
         tempNum = 13
      if (choice == 7):
         tempNum = 1
      if (choice == 9):
         tempNum = 4
      if (choice == 10):
         PIA.PanelButton10.Hide()
      if (choice == 11):
         tempNum = 0
   return tempNum

def HairstyleValue(ID:int):
   tempNum = 0
   if (ID == 0):
      tempNum = 0
   if (ID == 1):
      tempNum = 5
   if (ID == 2):
      tempNum = 8
   if (ID == 3):
      tempNum = 8
   if (ID == 4):
      tempNum = 5
   if (ID == 5):
      tempNum = 7
   if (ID == 6):
      tempNum = 20
   if (ID == 7):
      tempNum = 10
   if (ID == 8):
      tempNum = 5
   if (ID == 9):
      tempNum = 15
   if (ID == 10):
      tempNum = 15
   if (ID == 11):
      tempNum = 23
   if (ID == 12):
      tempNum = 18
   if (ID == 13):
      tempNum = 18
   if (ID == 14):
      tempNum = 20
   return tempNum

def HairstyleLength(ID:int):
   tempBool = False
   if (ID == 1):
      tempBool = True
   if (ID == 2):
      tempBool = True
   if (ID == 3):
      tempBool = True
   if (ID == 4):
      tempBool = True
   if (ID == 8):
      tempBool = True
   if (ID == 9):
      tempBool = True
   if (ID == 10):
      tempBool = True
   if (ID == 11):
      tempBool = True
   if (ID == 13):
      tempBool = True
   return tempBool

def HairstyleDescription(ID:int):
   tempStr = "CLOTHES NAME ERROR " + ID
   if (ID == 0):
      tempStr = "No hairstyle whatsoever. Choosing this option removes any mention of hair from your appearance description."
   if (ID == 1):
      tempStr = "Wavy hair has subtle curves that make it seem more flowing.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 2):
      tempStr = "Pigtails are straight/wavy/curvy hair pulled away from the face and gathered towards the sides of your head, where it is bundled and tied at the base, allowing it to hang freely over your shoulders.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 3):
      tempStr = "A Ponytail is straight/wavy/curvy hair pulled away from the face and gathered at the back of your head, where it is bundled and tied at the base, allowing it to hang freely over your back.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 4):
      tempStr = "Straight hair has been combed out to be nice and straight.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 5):
      tempStr = "A Buzzcut is hair cut quite short, less than a quarter inch from your head."
   if (ID == 6):
      tempStr = "A Mohawk leaves only the hair along the center, from front to back, left, shaving the rest. It\'s usually a couple inches long."
   if (ID == 7):
      tempStr = "A Bun is straight or wavy hair pulled up into a bun-like shape on top of the back of your head."
   if (ID == 8):
      tempStr = "Curly hair has been treated to make it nice and curly with a bit of spring.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 9):
      tempStr = "Braided Pigtails are pigtails that have been braided, keeping the dangling hair in a nice tight formation.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 10):
      tempStr = "A Braided Ponytail is a ponytail that has been braided, keeping the dangling hair in a nice tight formation.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 11):
      tempStr = "Braided hair involves tying all your hair into many braids, keeping it all in multiple tight formations.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 12):
      tempStr = "Spiky hair is hair that has been treated to stand away from your head, defying gravity. Due to limitations, it can only reach a few inches in length."
   if (ID == 13):
      tempStr = "Emo hair is hair that has been treated to sit straight at all times, with bangs often hanging over one eye.\r\rThis hairstyle has additional length options available after purchasing."
   if (ID == 14):
      tempStr = "An Afro is a giant poofball of curly hair. Due to limitations, it only reaches about half a foot from your head."
   return tempStr

!def DoTailor():
def ClothesName(ID:int):
   tempStr = "CLOTHES NAME ERROR"
   if (ID == 1):
      tempStr = "Shirt"
   if (ID == 2):
      tempStr = "Pants"
   if (ID == 3):
      tempStr = "Bikini Top"
   if (ID == 4):
      tempStr = "Bikini Bottom"
   if (ID == 5):
      tempStr = "Elegant Dress"
   if (ID == 6):
      tempStr = "Latex Suit"
   if (ID == 7):
      tempStr = "Skirt"
   if (ID == 8):
      tempStr = "Shorts"
   if (ID == 9):
      tempStr = "Blouse"
   if (ID == 10):
      tempStr = "Diaper"
   if (ID == 11):
      tempStr = "Poofy Diaper"
   if (ID == 12):
      tempStr = "Sundress"
   if (ID == 13):
      tempStr = "Skimpy Dress"
   if (ID == 14):
      tempStr = "Short Skirt"
   if (ID == 15):
      tempStr = "Short Shorts"
   if (ID == 16):
      tempStr = "Loin Cloth"
   if (ID == 17):
      tempStr = "Bathing Suit"
   if (ID == 18):
      tempStr = "Muscle Shirt"
   if (ID == 19):
      tempStr = "Corset"
   if (ID == 20):
      tempStr = "Silk Panties"
   if (ID == 21):
      tempStr = "Slingkini"
   if (ID == 22):
      tempStr = "Thong"
   if (ID == 23):
      tempStr = "Bloomers"
   if (ID == 24):
      tempStr = "Tights"
   if (ID == 25):
      tempStr = "Gothic Dress"
   if (ID == 26):
      tempStr = "Tube Top"
   if (ID == 27):
      tempStr = "Nipple Pasties"
   if (ID == 28):
      tempStr = "Camisole"
   if (ID == 29):
      tempStr = "Training Suit"
   if (ID == 30):
      tempStr = "Bouncy Bra"
   return tempStr

def ClothesID(choice:int):
   global currentZone
   tempNum = 0
   if (currentZone == 1):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 6
      if (choice == 6):
         tempNum = 9
      if (choice == 7):
         tempNum = 10
      if (choice == 9):
         tempNum = 13
      if (choice == 10):
         tempNum = 22
      if (choice == 11):
         tempNum = 27
   if (currentZone == 2):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 8
      if (choice == 6):
         tempNum = 9
      if (choice == 7):
         tempNum = 15
      if (choice == 9):
         tempNum = 18
      if (choice == 10):
         tempNum = 24
      if (choice == 11):
         tempNum = 26
   if (currentZone == 3):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 5
      if (choice == 6):
         tempNum = 13
      if (choice == 7):
         tempNum = 19
      if (choice == 9):
         tempNum = 22
      if (choice == 10):
         tempNum = 23
      if (choice == 11):
         tempNum = 25
   if (currentZone == 4):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 3
      if (choice == 6):
         tempNum = 4
      if (choice == 7):
         tempNum = 11
      if (choice == 9):
         tempNum = 12
      if (choice == 10):
         tempNum = 20
      if (choice == 11):
         tempNum = 28
   if (currentZone == 6):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 7
      if (choice == 6):
         tempNum = 14
      if (choice == 7):
         tempNum = 16
      if (choice == 9):
         tempNum = 17
      if (choice == 10):
         tempNum = 19
      if (choice == 11):
         tempNum = 21
   if (currentZone == 12):
      if (choice == 1):
         tempNum = 1
      if (choice == 2):
         tempNum = 2
      if (choice == 3):
         tempNum = 29
      if (choice == 5):
         tempNum = 28
      if (choice == 6):
         tempNum = 30
      if (choice == 7):
         tempNum = 25
      if (choice == 9):
         tempNum = 23
      if (choice == 10):
         tempNum = 22
      if (choice == 11):
         tempNum = 19
   return tempNum

def ClothesValue(ID:int):
   tempNum = 0
   if (ID == 1):
      tempNum = 5
   if (ID == 2):
      tempNum = 5
   if (ID == 3):
      tempNum = 25
   if (ID == 4):
      tempNum = 25
   if (ID == 5):
      tempNum = 45
   if (ID == 6):
      tempNum = 60
   if (ID == 7):
      tempNum = 25
   if (ID == 8):
      tempNum = 25
   if (ID == 9):
      tempNum = 25
   if (ID == 10):
      tempNum = 30
   if (ID == 11):
      tempNum = 40
   if (ID == 12):
      tempNum = 40
   if (ID == 13):
      tempNum = 50
   if (ID == 14):
      tempNum = 35
   if (ID == 15):
      tempNum = 35
   if (ID == 16):
      tempNum = 40
   if (ID == 17):
      tempNum = 55
   if (ID == 18):
      tempNum = 15
   if (ID == 19):
      tempNum = 50
   if (ID == 20):
      tempNum = 35
   if (ID == 21):
      tempNum = 65
   if (ID == 22):
      tempNum = 40
   if (ID == 23):
      tempNum = 30
   if (ID == 24):
      tempNum = 35
   if (ID == 25):
      tempNum = 60
   if (ID == 26):
      tempNum = 20
   if (ID == 27):
      tempNum = 45
   if (ID == 28):
      tempNum = 40
   if (ID == 29):
      tempNum = 35
   if (ID == 30):
      tempNum = 45
   return tempNum

def ClothesDescription(ID:int):
   tempStr = "CLOTHES NAME ERROR"
   if (ID == 1):
      tempStr = "A generic shirt with no special attributes." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 2):
      tempStr = "A generic pair of pants with no special attributes." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 3):
      tempStr = "A rather revealing bikini top/s, covering all your breasts, looking good and hugging tightly to improve enticement and sensitivity, but reduces your mentality and milk production." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 4):
      tempStr = "A rather revealing bikini bottom, covering your groin, looking good and hugging tightly to improve enticement and sensitivity, but reduces your mentality and cum production." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 5):
      tempStr = "A courtly dress that's more about giving a good impression than a slutty one, improving mentality, but the caution to prevent ripping reduces strength. It also increases the speed of your pregnancies slightly, in the attempt to not look slutty, or something." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 6):
      tempStr = "A suit made of a thin, very tight material that covers most of your body and greatly improves enticement and sensitivity, but also reduces mentality, run chance, cum and milk production." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 7):
      tempStr = "A modest skirt, very helpful in terms of function. Improves run chance, strength, and cum production, but reduces mentality and increases pregnancy chance with its 'ease of access'." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 8):
      tempStr = "A pair of shorts, very helpful in terms of function. Improves run chance and strength, but reduces libido with its lackluster appearance." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 9):
      tempStr = "A buttoned shirt that allows your breasts to produce more milk while looking good to increase mentality, but reduces sensitivity and strength." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 10):
      tempStr = "A diaper that helps soak up some of your moistness and makes your hips look bigger, but reduces mentality." + "\n" + "\n" + "Warning: Removing the diaper after wearing it could potentially make you even wetter than before you put it on, your body depending too much on it." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 11):
      tempStr = "A poofy diaper that helps soak up a lot of your moistness and makes both your hips and butt look bigger, but reduces mentality and libido." + "\n" + "\n" + "Warning: Removing the poofy diaper after wearing it could potentially make you even wetter than before you put it on, your body depending too much on it." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 12):
      tempStr = "A casual dress that gives your body a lot of exposure, improving sensitivity, cum production, and libido, but reduces run chance, strength, and increases pregnancy chance." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 13):
      tempStr = "A skimpy dress that really hugs your curves, improving sensitivity, enticement, and libido, but reduces strength and mentality with its slutty appearance, and increases pregnancy chance with its ease of access." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 14):
      tempStr = "A short skirt that's more attractive than modest, improving cum production, sensitivity, and enticement, but reduces mentality and increases pregnancy chance with its ease of access." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 15):
      tempStr = "A pair of short shorts that are more skimpy than functional, hugging tightly to improve sensitivity, enticement, and run chance, but reduces cum production, mentality, and strength." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 16):
      tempStr = "A loin cloth that is more suited for the simplicity of the wild, but also a bit uncivilized, improving cum production, run chance, strength, and sensitivity, but reduces mentality and increases pregnancy chance." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 17):
      tempStr = "A one-piece bathing suit that covers both chest and groin and is great for swimming, it acts as a barrier to liquids. The suit prevents your sexual lubrication from drying away as easily, thus increasing your moistness, as well as increasing strength and sensitivity while reducing mentality and pregnancy chance." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 18):
      tempStr = "A simple muscle shirt that is more functional than civilized. Increases strength but reduces mentality, and makes your chest look slightly bigger." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 19):
      tempStr = "A corset that ties tightly around your waist, greatly magnifying your bust and hips, increasing your mentality and libido, but is also quite restrictive and hard to breath in, reducing strength and your maximum HP." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 20):
      tempStr = "A pair of silken panties, this underwear looks and feels good, amplifying your vulva size, increasing your enticement, libido, and sensitivity, but also reduces mentality, cum production, and run chance as you're afraid of tearing them." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 21):
      tempStr = "A very scant bathing suit that consists of thin fabric that barely covers your crotch and forks to sling around your body and just barely cover your nipples. Largely increases enticement, as well as increasing libido and sensitivity. However, it largely reduces your mentality, reduces your strength, keeps you constantly slightly aroused, and is rather difficult to run in as it easily rides up your rear." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 22):
      tempStr = "A quite small piece of underwear that shows off much of your posterior, the thong is quite enticing and raises your libido, but reduces strength, mentality, and sensitivity, and is slightly difficult to run in as it rides up your rear." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 23):
      tempStr = "A pair of form-fitting athletic bloomers, they are very nice to run in and increases strength and libido, but also reduces mentality and is slightly difficult to rape others while wearing them." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 24):
      tempStr = "A pair of form-fitting, stretchy, agile tights, they are easy to run in and increase your sensitivity, but their tightness reduces cum production and ability to get pregnant." + "\n" + "\n" + "Takes bottom clothes slot."
   if (ID == 25):
      tempStr = "A dark and decorated frilly dress of the gothic variety, it increases your mentality and the intimidation helps you rape others, but it also makes vaginal passages more stretchy for some strange reason." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 26):
      tempStr = "A single piece of stretchy fabric that wraps around the chest, the tube top is slightly enticing and slightly increases milk production. However, it tends to outline nipples so well that it seems to make them bigger and also lowers mentality." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 27):
      tempStr = "A simple bunch of adhesive stickers that paste to the nipples to cover them and only them. Extremely lewd, it lowers your mentality significantly, but also raises enticement, libido, and sensitivity, and increases the amount of milk your breasts can hold by literally capping your nipples." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 28):
      tempStr = "A soft and loose piece of lingerie, this camisole is an attractive and smart way to cover your breasts, increasing enticement, mentality, and sensitivity. The soft fabric constantly teasing your nipples also reduces the rate at which your breasts dry up, should they be lactating." + "\n" + "\n" + "Takes top clothes slot."
   if (ID == 29):
      tempStr = "A yellow tracksuit with black stripes up the sides, this training suit makes you feel much stronger and heartier while wearing it, perfect for fighting. However, it looks fairly silly, basically the opposite of attractive, and reduces your mentality, libido, and sensitivity." + "\n" + "\n" + "Takes both top and bottom clothes slots."
   if (ID == 30):
      tempStr = "A bra that allows for a little more bounce to your step by allowing you to withstand a bit more weight. And it's so wonderful that it helps you carry -any- extra weight, even beyond your breasts!" + "\n" + "\n" + "Takes top clothes slot."
   return tempStr

def ClothesTop():
   global attireTop, boobTotal
   tempStr = "CLOTHES TOP ERROR " + attireTop
   if (attireTop == -1):
      tempStr = "tattered shreds"
   if (attireTop == 0):
      tempStr = "invisible underwear"
   if (attireTop == 1):
      tempStr = "shirt"
   if (attireTop == 3):
      if (boobTotal == 2):
         tempStr = "bikini top"
      if (boobTotal >= 4):
         tempStr = "bikini tops"
   if (attireTop == 5):
      tempStr = "elegant dress"
   if (attireTop == 6):
      tempStr = "latex suit"
   if (attireTop == 9):
      tempStr = "blouse"
   if (attireTop == 12):
      tempStr = "sundress"
   if (attireTop == 13):
      tempStr = "skimpy dress"
   if (attireTop == 17):
      tempStr = "bathing suit"
   if (attireTop == 18):
      tempStr = "muscle shirt"
   if (attireTop == 19):
      tempStr = "corset"
   if (attireTop == 21):
      tempStr = "slingkini"
   if (attireTop == 25):
      tempStr = "gothic dress"
   if (attireTop == 26):
      tempStr = "tube top"
   if (attireTop == 27):
      tempStr = "nipple pasties"
   if (attireTop == 28):
      tempStr = "camisole"
   if (attireTop == 29):
      tempStr = "training suit"
   if (attireTop == 30):
      tempStr = "bouncy bra"
   return tempStr

def ClothesBottom():
   global attireBot
   tempStr = "CLOTHES BOTTOM ERROR " + attireBot
   if (attireBot == -1):
      tempStr = "tattered shreds"
   if (attireBot == 0):
      tempStr = "invisible underwear"
   if (attireBot == 2):
      tempStr = "pants"
   if (attireBot == 4):
      tempStr = "bikini bottom"
   if (attireBot == 5):
      tempStr = "elegant dress"
   if (attireBot == 6):
      tempStr = "latex suit"
   if (attireBot == 7):
      tempStr = "skirt"
   if (attireBot == 8):
      tempStr = "shorts"
   if (attireBot == 10):
      tempStr = "diaper"
   if (attireBot == 11):
      tempStr = "poofy diaper"
   if (attireBot == 12):
      tempStr = "sundress"
   if (attireBot == 13):
      tempStr = "skimpy dress"
   if (attireBot == 14):
      tempStr = "short skirt"
   if (attireBot == 15):
      tempStr = "short shorts"
   if (attireBot == 16):
      tempStr = "loincloth"
   if (attireBot == 17):
      tempStr = "bathing suit"
   if (attireBot == 20):
      tempStr = "silken panties"
   if (attireBot == 21):
      tempStr = "slingkini"
   if (attireBot == 22):
      tempStr = "thong"
   if (attireBot == 23):
      tempStr = "bloomer"
   if (attireBot == 24):
      tempStr = "tights"
   if (attireBot == 25):
      tempStr = "gothic dress"
   if (attireBot == 29):
      tempStr = "training suit"
   return tempStr

def CurrentClothes():
   global attireTop, attireBot
   tempStr = "CURRENT CLOTHES ERROR"
   if (attireTop == attireBot):
      tempStr = "" + ClothesTop() + ""
   else:
      tempStr = "" + ClothesTop() + " and " + ClothesBottom() + ""
   return tempStr

def PullUD(source:int):
   global attireTop, attireBot
   tempStr = "PULL UP/DOWN ERROR " + attireTop + " " + attireBot
   if (source == 1):
      if (attireTop == -1):
         tempStr = "open"
      if (attireTop == 0):
         tempStr = "up"
      if (attireTop == 1):
         tempStr = "up"
      if (attireTop == 3):
         tempStr = "down"
      if (attireTop == 5):
         tempStr = "down"
      if (attireTop == 6):
         tempStr = "open"
      if (attireTop == 9):
         tempStr = "open"
      if (attireTop == 12):
         tempStr = "down"
      if (attireTop == 13):
         tempStr = "down"
      if (attireTop == 17):
         tempStr = "down"
      if (attireTop == 18):
         tempStr = "up"
      if(attireTop == 19):
         tempStr = "down"
      if (attireTop == 21):
         tempStr = "open"
      if (attireTop == 25):
         tempStr = "down"
      if (attireTop == 26):
         tempStr = "down"
      if (attireTop == 27):
         tempStr = "off"
      if (attireTop == 28):
         tempStr = "up"
      if (attireTop == 29):
         tempStr = "open"
      if (attireTop == 30):
         tempStr = "down"
   if (source == 2):
      if (attireBot == -1):
         tempStr = "open"
      if (attireBot == 0):
         tempStr = "down"
      if (attireBot == 2):
         tempStr = "down"
      if (attireBot == 4):
         tempStr = "down"
      if (attireBot == 5):
         tempStr = "up"
      if (attireBot == 6):
         tempStr = "open"
      if (attireBot == 7):
         tempStr = "up"
      if (attireBot == 8):
         tempStr = "down"
      if (attireBot == 10):
         tempStr = "down"
      if (attireBot == 11):
         tempStr = "down"
      if (attireBot == 12):
         tempStr = "up"
      if (attireBot == 13):
         tempStr = "up"
      if (attireBot == 14):
         tempStr = "up"
      if (attireBot == 15):
         tempStr = "down"
      if (attireBot == 16):
         tempStr = "up"
      if (attireBot == 17):
         tempStr = "aside"
      if (attireBot == 20):
         tempStr = "down"
      if (attireBot == 21):
         tempStr = "aside"
      if (attireBot == 22):
         tempStr = "down"
      if (attireBot == 23):
         tempStr = "down"
      if (attireBot == 24):
         tempStr = "down"
      if (attireBot == 25):
         tempStr = "up"
      if (attireBot == 29):
         tempStr = "open"
   return tempStr

def ClothesChange(ID:int):
   if (ID == 1):
      ChangeTop(1)
   if (ID == 2):
      ChangeBot(2)
   if (ID == 3):
      ChangeTop(3)
   if (ID == 4):
      ChangeBot(4)
   if (ID == 5):
      ChangeTop(5)
      ChangeBot(5)
   if (ID == 6):
      ChangeTop(6)
      ChangeBot(6)
   if (ID == 7):
      ChangeBot(7)
   if (ID == 8):
      ChangeBot(8)
   if (ID == 9):
      ChangeTop(9)
   if (ID == 10):
      ChangeBot(10)
   if (ID == 11):
      ChangeBot(11)
   if (ID == 12):
      ChangeTop(12)
      ChangeBot(12)
   if (ID == 13):
      ChangeTop(13)
      ChangeBot(13)
   if (ID == 14):
      ChangeBot(14)
   if (ID == 15):
      ChangeBot(15)
   if (ID == 16):
      ChangeBot(16)
   if (ID == 17):
      ChangeTop(17)
      ChangeBot(17)
   if (ID == 18):
      ChangeTop(18)
   if (ID == 19):
      ChangeTop(19)
   if (ID == 20):
      ChangeBot(20)
   if (ID == 21):
      ChangeTop(21)
      ChangeBot(21)
   if (ID == 22):
      ChangeBot(22)
   if (ID == 23):
      ChangeBot(23)
   if (ID == 24):
      ChangeBot(24)
   if (ID == 25):
      ChangeTop(25)
      ChangeBot(25)
   if (ID == 26):
      ChangeTop(26)
   if (ID == 27):
      ChangeTop(27)
   if (ID == 28):
      ChangeTop(28)
   if (ID == 29):
      ChangeTop(29)
      ChangeBot(29)
   if (ID == 30):
      ChangeTop(30)

def ChangeTop(ID:int):
   global attireTop, enticeMod, milkMod, pregRate, cumMod, runMod, pregChanceMod, vagMoistMod, cockMoistMod, breastSize, hips, HPMod, minLust, rapeMod, vagElastic, nippleSizem milkCap, carryMod, attireBot
   if (ID != attireTop):
      if (attireTop == -1):
         StatsMod(2,2,0,0)
      if (attireTop == 0):
         StatsMod(0,4,0,0)
      if (attireTop == 1):
         x = 0
      if (attireTop == 3):
         enticeMod -= 6
         StatsMod(0,2,0,-2)
         milkMod += 15
      if (attireTop == 5):
         StatsMod(2,-4,0,0)
         pregRate -= 0.2
      if (attireTop == 6):
         enticeMod -= 8
         StatsMod(0,2,0,-8)
         cumMod += 0.2
         milkMod += 10
         runMod += 5
      if (attireTop == 9):
         StatsMod(2,-2,0,1)
         milkMod -= 20
      if (attireTop == 12):
         StatsMod(2,0,-2,-2)
         cumMod -= 0.2
         runMod += 5
         pregChanceMod -= 5
      if (attireTop == 13):
         StatsMod(2,3,-2,-3)
         enticeMod -= 14
         pregChanceMod -= 5
      if (attireTop == 17):
         StatsMod(-2,2,0,-2)
         vagMoistMod -= 2
         cockMoistMod -= 2
         pregChanceMod += 5
      if (attireTop == 18):
         StatsMod(-2,2,0,0)
         breastSize = breastSize - 1
      if (attireTop == 19):
         StatsMod(2,-2,-2,0)
         breastSize -= 4
         hips -= 2
         HPMod += 5
      if (attireTop == 21):
         enticeMod -= 18
         StatsMod(2,6,-4,-4)
         runMod += 10
         minLust -= 5
      if (attireTop == 25):
         StatsMod(0,-4,0,0)
         rapeMod -= 3
         vagElastic -= 0.2
      if (attireTop == 26):
         enticeMod -= 2
         StatsMod(0,2,0,0)
         milkMod -= 5
         nippleSize -= 2
      if (attireTop == 27):
         StatsMod(0,6,-2,-4)
         milkCap -= 250
         enticeMod -= 6
      if (attireTop == 28):
         StatsMod(0,-2,0,-4)
         enticeMod -= 4
      if (attireTop == 29):
         StatsMod(-10,2,2,2)
         enticeMod += 10
         HPMod -= 10
      if (attireTop == 30):
         carryMod -= 15
      if (ID == -1):
         if (attireTop == attireBot) and (attireBot != -1):
            attireTop = ID
            ChangeBot(-1)
         StatsMod(-2,-2,0,0)
      if (ID == 0):
         StatsMod(0,-4,0,0)
      if (ID == 1):
         x = 0
      if (ID == 3):
         enticeMod += 6
         StatsMod(0,-2,0,2)
         milkMod -= 15
      if (ID == 5):
         StatsMod(-2,4,0,0)
         pregRate += 0.2
      if (ID == 6):
         enticeMod += 8
         StatsMod(0,-2,0,8)
         cumMod -= 0.2
         milkMod -= 10
         runMod -= 5
      if (ID == 9):
         StatsMod(-2,2,0,-1)
         milkMod += 20
      if (ID == 12):
         StatsMod(-2,0,2,2)
         cumMod += 0.2
         runMod -= 5
         pregChanceMod += 5
      if (ID == 13):
         StatsMod(-2,-3,2,3)
         enticeMod += 14
         pregChanceMod += 5
      if (ID == 17):
         StatsMod(2,-2,0,2)
         vagMoistMod += 2
         cockMoistMod += 2
         pregChanceMod -= 5
      if (ID == 18):
         StatsMod(2,-2,0,0)
         breastSize += 1
      if (ID == 19):
         statsMod(-2,2,2,0)
         breastSize += 4
         hips += 2
         HPMod -= 5
      if (ID == 21):
         enticeMod += 18
         StatsMod(-2,-6,4,4)
         runMod -= 10
         minLust += 5
      if (ID == 25):
         StatsMod(0,4,0,0)
         rapeMod += 3
         vagElastic += 0.2
      if (ID == 26):
         enticeMod += 2
         StatsMod(0,-2,0,0)
         milkMod += 5
         nippleSize += 2
      if (ID == 27):
         StatsMod(0,-6,2,4)
         milkCap += 250
         enticeMod += 6
      if (ID == 28):
         StatsMod(0,2,0,4)
         enticeMod += 4
      if (ID == 29):
         StatsMod(10,-2,-2,-2)
         enticeMod -= 10
         HPMod += 10
      if (ID == 30):
         carryMod += 15
      if (attireTop == attireBot) and (ID != 0) and (ID != -1):
         attireTop = ID
         changeBot(2)
      else:
         attireTop = ID

def ChangeBot(ID:int):
   global attireBot, enticeMod, cumMod, runMod, pregChanceMod, vagMoistMod, cockMoistMod, hips, butt, vulvaSize, attireTop
   if (ID != attireBot):
      if (attireBot == -1):
         StatsMod(2,2,0,0)
      if (attireBot == 0):
         StatsMod(0,4,0,0)
      if (attireBot == 2):
         x = 0
      if (attireBot == 4):
         enticeMod -= 6
         StatsMod(0,2,0,-2)
         cumMod += 0.2
      if (attireBot == 7):
         runMod -= 3
         cumMod -= 0.2
         StatsMod(-2,2,0,0)
         pregChanceMod -= 4
      if (attireBot == 8):
         runMod -= 3
         StatsMod(-2,0,3,0)
      if (attireBot == 10):
         vagMoistMod += 2
         cockMoistMod += 2
         hips = this.hips - 1
         StatsMod(0,4,0,0)
      if (attireBot == 11):
         vagMoistMod += 5
         cockMoistMod += 5
         hips = hips - 1
         butt -= 2
         StatsMod(0,4,4,0)
      if (attireBot == 14):
         cumMod -= 0.2
         enticeMod -= 7
         StatsMod(0,4,0,-2)
         pregChanceMod -= 6
      if (attireBot == 15):
         cumMod += 0.2
         runMod -= 5
         enticeMod -= 4
         StatsMod(2,3,0,-2)
      if (attireBot == 16):
         cumMod -= 0.2
         runMod -= 4
         pregChanceMod -= 5
         StatsMod(-2,4,0,-2)
      if (attireBot == 20):
         cumMod += 0.3
         runMod += 3
         vulvaSize = vulvaSize - 1
         enticeMod -= 7
         StatsMod(0,2,-2,-2)
      if (attireBot == 22):
         runMod += 5
         enticeMod -= 9
         StatsMod(2,2,-4,2)
      if (attireBot == 23):
         runMod -= 6
         rapeMod += 4
         StatsMod(-2,2,-2,0)
      if (attireBot == 24):
         runMod -= 4
         cumMod += 0.2
         pregChanceMod += 3
         StatsMod(0,0,0,-2)
      if (ID == -1):
         if (attireTop == attireBot) and (attireTop != -1):
            attireBot = ID
            ChangeTop(-1)
         StatsMod(-2,-2,0,0)
      if (ID == 0):
         StatsMod(0,-4,0,0)
      if(ID == 2):
         x = 0
      if (ID == 4):
         enticeMod += 6
         StatsMod(0,-2,0,2)
         cumMod -= 0.2
      if (ID == 7):
         runMod += 3
         cumMod += 0.2
         StatsMod(2,-2,0,0)
         pregChanceMod += 4
      if(ID == 8):
         runMod += 3
         StatsMod(2,0,-3,0)
      if (ID == 10):
         vagMoistMod -= 2
         cockMoistMod -= 2
         hips += 1
         StatsMod(0,-4,0,0)
      if (ID == 11):
         vagMoistMod -= 5
         cockMoistMod -= 5
         hips += 1
         butt += 2
         StatsMod(0,-4,-4,0)
      if (ID == 14):
         cumMod += 0.2
         enticeMod += 7
         StatsMod(0,-4,0,2)
         pregChanceMod += 6
      if (ID == 15):
         cumMod -= 0.2
         runMod += 5
         enticeMod += 4
         StatsMod(-2,-3,0,2)
      if (ID == 16):
         cumMod += 0.2
         runMod += 4
         pregChanceMod += 5
         StatsMod(2,-4,0,2)
      if (ID == 20):
         cumMod -= 0.3
         runMod -= 3
         vulvaSize += 1
         enticeMod += 7
         StatsMod(0,-2,2,2)
      if (ID == 22):
         runMod -= 5
         enticeMod += 9
         StatsMod(-2,-2,4,-2)
      if (ID == 23):
         runMod += 6
         rapeMod -= 4
         StatsMod(2,-2,2,0)
      if (ID == 24):
         runMod += 4
         cumMod -= 0.2
         pregChanceMod -= 3
         StatsMod(0,0,0,2)
      if (attireTop == attireBot) and (ID != 0) and (ID != -1):
         attireBot = ID
         ChangeTop(1)
      else:
         attireBot = ID

!def DoDayCare():
!def DoProstitute():
!def DoSleep():
   global exhaustion, skipExhaustion, exhaustionPenalty, lust, heatTime, heat, cockTotal, vagTotal, milkEngorgementLevel, udderEngorgementLevel, pregnancyTime, body, _str_, carryMod, firstExplore, hrs
   this.bc()
   OutputMainText("You head into town to sleep for the night...",True)
   exhaustion = 0
   skipExhaustion = True
   if (exhaustionPenalty == 1):
      exhaustionPenalty = 0
      StatsMod(3,3,0,0)
   if (exhaustionPenalty == 2):
      exhaustionPenalty = 0
      StatsMod(11,11,0,0)
   DoHP(20)
   if (lust <= 30):
      OutputMainText("\n" + "\n" + "Despite everything, your body is calm and sleeps rather soundly.",False)
      if (((MoistCalc(1) > 9) and (cockTotal > 0)) or ((MoistCalc(2) > 9) and (vagTotal > 0))):
         OutputMainText(" Although your bed is slightly moist from your constant production of lubricant from your loins.",False)
   if (lust > 30) and (lust <= 70):
      OutputMainText("\n" + "\n" + "Your sleep is somewhat disrupted by tossing and turning throughout the night, your arousal making certain attributes swell with blood and desiring attention...",False)
      exhaustion += 3
      if (((MoistCalc(1) > 3) and (MoistCalc(1) <= 9) and (cockTotal > 0)) or ((MoistCalc(2) > 3) and (MoistCalc(2) <= 9) and (vagTotal > 0))):
         OutputMainText(" Plus your bed is slightly moist from your constant production of lubricant from your loins.",False)
      if (((MoistCalc(1) > 9) and (cockTotal > 0)) or ((MoistCalc(2) > 9) and (vagTotal > 0))):
         OutputMainText(" It also seems as though you had wet the bed throughout the night, however the slick slime that pulls away in long strands as you touch it indicates a different fluid...",False)
   if (lust > 70):
      OutputMainText("\n" + "\n" + "You spend most of the night tossing and turning, your mind having difficulty sleeping with the lust that envelops it. Although you do manage to eventually get some, it's not nearly as good.",False)
      exhaustion += 8
      if (((MoistCalc(1) > 0) and (MoistCalc(1) <= 3) and (cockTotal > 0)) or ((MoistCalc(2) > 0) and (MoistCalc(2) <= 3) and (vagTotal > 0))):
         OutputMainText(" Plus your bed is slightly moist from your constant production of lubricant from your loins.",False)
      if (((MoistCalc(1) > 3) and (MoistCalc(1) <= 9) and (cockTotal > 0)) or ((MoistCalc(2) > 3) and (MoistCalc(2) <= 9) and (vagTotal > 0))):
         OutputMainText(" It also seems as though you had wet the bed throughout the night, however the slick slime that pulls away in long strands as you touch it indicates a different fluid...",False)
      if (((MoistCalc(1) > 9) and (cockTotal > 0)) or ((MoistCalc(2) > 9) and (vagTotal > 0))):
         OutputMainText(" You also wake up in a pool of your own sexual lubricant, the slick stuff sloshing off the sheets as you attempt to get out. You remain cautious as your " + LegDesc(10) + " touch the floor, as you have to avoid slipping in the large puddle around the bed.",False)
   if ((heatTime < 0) and (heat > 0) and (vagTotal > 0)):
      OutputMainText("\n" + "\n" + "Dreams of being fucked by over a dozen cocks, each filling you to the brim with hot spunk, filled your sleep. When you eventually woke up in a hot sweat, your hand reflexively inspects your belly and you find yourself slightly disappointed to find it empty.",False)
   if (milkEngorgementLevel == 2):
      OutputMainText("\n" + "\n" + "Your sheets smell somewhat sweet, slightly wet and white, as you wake up. Milk still dribbles from your breasts, having formed a small puddle throughout the night.",False)
   if (milkEngorgementLevel > 2):
      OutputMainText("\n" + "\n" + "Your sheets smell somewhat sweet and feel very wet as you wake up. Milk spills in streams from your breasts, as you sit up, a pool of the stuff all around you.",False)
   if (udderEngorgementLevel == 2):
      OutputMainText("\n" + "\n" + "Your sheets smell somewhat sweet, slightly wet and white, as you wake up. Milk still dribbles from your udder, having formed a small puddle throughout the night.",False)
   if (udderEngorgementLevel > 2):
      OutputMainText("\n" + "\n" + "Your sheets smell somewhat sweet and feel very wet as you wake up. Milk spills in streams from your udder, as you sit up, a pool of the stuff all around you.",False)
   if (pregCheck(0) == True):
      if (pregnancyTime > 18) and (pregnancyTime <= 36):
         OutputMainText("\n" + "\n" + "After waking, you feel oddly sick and strangely bloated. You should probably watch what you eat more closely.",False)
      elif (pregnancyTime > 36) and (pregnancyTime <= 72):
         OutputMainText("\n" + "\n" + "You seem to be getting a bit chubbier in your midsection, might be because you've been hungrier and eating more lately. Plus you've been feeling a bit more randy than usual...",False)
      elif (pregnancyTime > 72) and (pregnancyTime <= 108):
         OutputMainText("\n" + "\n" + "Your belly is obviously bulging now, more than it would if it were just fat. You should probably accept the fact that you're pregnant...",False)
      elif (pregnancyTime > 108) and (pregnancyTime <= 144):
         OutputMainText("\n" + "\n" + "You can easily hug your belly as it protrudes from your torso, looking like you were trying to smuggle a melon in your womb. But it feels so good to rub and caress it, making you easily get horny.",False)
      elif (pregnancyTime > 144) and (pregnancyTime <= 180):
         OutputMainText("\n" + "\n" + "Your belly is so large your belly button has turned into an outie. You play with it as you head to sleep, the baby inside kicking back in turn.",False)
      elif (pregnancyTime > 180) and (pregnancyTime <= 216):
         OutputMainText("\n" + "\n" + "For most races, you would be giving birth any time now. You actually have to be cautious about people bumping into you as you walk through the town, it protrudes so far.",False)
      elif (pregnancyTime > 216) and (pregnancyTime <= 252):
         OutputMainText("\n" + "\n" + "The " + SkinDesc() + " around your giant belly is so taut that you can audibly drum it with your fingers. Which the baby inside does with its feet frequently from inside.",False)
      elif (pregnancyTime > 252) and (pregnancyTime <= 288):
         OutputMainText("\n" + "\n" + "You're beginning to draw the eyes of the crowd as you move through town, your belly is so enormous. People are wondering if you've actually got a baby in there and not a small child.",False)
      elif (pregnancyTime > 288) and (pregnancyTime <= 324):
         OutputMainText("\n" + "\n" + "This is getting ridiculous... People are starting to come up to you as you move through the street on your way to bed and actually ask if you've got a small person in your belly! Although, you aren't quite sure, but as your hands try to wrap around it, unable to fully embrace it, you begin to wonder yourself.",False)
      elif (pregnancyTime > 324) and (pregnancyTime <= 360):
         OutputMainText("\n" + "\n" + "Your giant belly is becoming a bit of a nuisance... As you walk through buildings, people back up against a wall to let you pass by. You can feel your belly scrape against the frames of narrow doorways as you pass through, and it's been a while since you've last seen your belly-button...",False)
      elif (pregnancyTime > 360) and (pregnancyTime <= 396):
         OutputMainText("\n" + "\n" + "Now you're actually starting to get a little worried... Your " + LegDesc(6) + " are knocking against the underside of your belly when you try to walk. People are clearing the way when you move down the streets to make room for your belly and you have to skillfully wedge yourself through narrow doorways!",False)
      elif (pregnancyTime > 396) and (pregnancyTime <= 432):
         OutputMainText("\n" + "\n" + "As you lay down to go to sleep, you have to curl forward to fit your belly in your bed, leaving your backside hanging off the mattress. The sheets aren't even wide enough to cover you completely, making you feel a draft on some of your exposed belly. The chill makes you shiver, not from the cold, but from your nerves sparking from the super-taut, extra-sensitive " + SkinDesc() + ".",False)
      elif (pregnancyTime > 432):
         OutputMainText("\n" + "\n" + "You don't even bother to head to your bed. Borrowing a bunch of blankets, you've made do with sleeping outside. Your belly is too big to go indoors, even having to handle shop business from the streets. Your hand reaches out as far as it can and hardly wraps around any of your girth. The warmth it emanates and sensations it echoes through your body help you sleep quite soundly and pleasantly, though, so you'll be fine until you give birth.",False)
      if ((body + (_str_ / 2) + carryMod) < math.floor(pregnancyTime / 10)):
         OutputMainText(" However, none of that really matters as you can no longer carry the weight of your hefty belly. You're stuck in this town, dragging your belly across the ground, with padding beneath to protect it. There's going to be no more exploring until you either get stronger or give birth to this massive nuisance...",False)
      elif (((body + (_str_ / 2) + carryMod) * 2) < math.floor(pregnancyTime / 10)):
         OutputMainText(" Your " + SkinDesc() + " is pulled so taut around your belly that you're afraid it might tear, though it never does. But it's so sensitive... Caressing it as you try to sleep is so nice~ Although, it does have the slight drawback of looking rather silly while you walk with a hunch and attempt to cradle it wherever you go; it's gotten so heavy.",False)
      elif (((body + (_str_ / 2) + carryMod) * 3) < math.floor(pregnancyTime / 10)):
         OutputMainText(" The mound feels so heavy... When walking around town, you even had to keep a hand on your back for support.",False)
      elif (((body + (_str_ / 2) + carryMod) * 4) < math.floor(pregnancyTime / 10)):
         OutputMainText(" The weight of your belly makes you feel more exhausted than you really are by the end of the day, making you glad for the night's rest.",False)
      elif (((body + (_str_ / 2) + carryMod) * 5) < math.floor(pregnancyTime / 10)):
         OutputMainText(" You can noticeably feel the weight of your belly.",False)
   if (firstExplore == False) and (Percent() < 10):
      OutputMainText("\n" + "\n" + "\"Please... Anybody?\" Despite everything, your mind focuses on that echoing dream for another night now...",False)
   hrs = 8
   DoEnd()

!def DoMasturbate():
   this.bc()
   currentState = 3
   ViewButtonOutline(1,0,1,1,0,0,1,0,0,1,0,1)
   ViewButtonText(0,0,0,1,0,0,1,0,0,0,0,1)
   this.buttonWrite(1,"Penis")
   this.buttonWrite(2,"Both")
   this.buttonWrite(3,"Vagina")
   this.buttonWrite(4,"Bag")
   this.buttonWrite(7,"Breasts")
   this.buttonWrite(10,"Udder")
   this.buttonWrite(12,"Return")
   if(this.cockTotal > 0)
      this.Choice1.visible = true
   if(this.vagTotal > 0)
   {
      this.Choice3.visible = true;
   }
   if(this.udders == true)
   {
      this.Choice10.visible = true;
   }
   this.outputMainText("How would you like to masturbate?",true);
   this.doListen = function():void
   {
      if(buttonChoice == 1)
      {
         doCockMasturbate();
      }
      if(buttonChoice == 3)
      {
         doVagMasturbate();
      }
      if(buttonChoice == 2)
      {
         doBothMasturbate();
      }
      if(buttonChoice == 4)
      {
         doBag();
      }
      if(buttonChoice == 7)
      {
         doBoobMasturbate();
      }
      if(buttonChoice == 10)
      {
         doUdderMasturbate();
      }
      if(buttonChoice == 12)
      {
         doGeneral();
      }
   };
}
def DoCockMasturbate():
   global rndArray, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, rabbitCocks, bugCocks, lust, ment, lib, currentZone, cockSize, cockSizeMod, tallness, breastSize, boobTotal, showBalls, balls, knot, cockTotal, sen, hrs, exhaustion, attireBot
   _loc1_ = 0
   _loc2_ = null
   _loc3_ = 0
   _loc4_ = 0
   rndArray = list(())
   if (humanCocks > 0):
      rndArray.push(1)
   if (horseCocks > 0):
      rndArray.push(2)
   if (wolfCocks > 0):
      rndArray.push(3)
   if (catCocks > 0):
      rndArray.push(4)
   if (lizardCocks > 0):
      rndArray.push(6)
   if (rabbitCocks > 0):
      rndArray.push(7)
   if (bugCocks > 0):
      rndArray.push(12)
   _loc1_ = ChooseFrom()
   _loc2_ = "WHICH COCK ERROR"
   if (_loc1_ == 1):
      _loc2_ = "hard human rod"
   if (_loc1_ == 2):
      _loc2_ = "long equine flesh"
   if (_loc1_ == 3):
      _loc2_ = "pointy wolf meat"
   if (_loc1_ == 4):
      _loc2_ = "pink thorny cat prick"
   if (_loc1_ == 6):
      _loc2_ = "purple ribbed reptile rod"
   if (_loc1_ == 7):
      _loc2_ = "throbbing bunny carrot"
   if (_loc1_ == 12):
      _loc2_ = "bumpy-ridged spiked bug wang"
   if (lust < 20):
      OutputMainText("You're hardly aroused enough to get your cock" + Plural(1) + " standing, let alone masturbate. You'll just have to settle for something else.",True)
      DoEnd()
   else:
      _loc1_ = math.floor((Percent() / 20) + (ment / 5) + (lib / 5))
      _loc3_ = CumAmount()
      i = 0
      while (i == 0):
         _loc4_ = math.floor(random.random() * (1 + 7 - 1)) + 1
         if (_loc4_ == 1):
            if (ment >= (lib - 10)):
               OutputMainText("You sneak off to the private place where you sleep in " + RegionName(currentZone) + " with a bunch of towels in hand. Carefully, so as to not let anybody hear, you pull " + PullUD(2) + " your " + ClothesBottom() + ", your " + CockDesc() + " erection" + Plural(1) + " bobbing out." + "\n" + "\n" + "You wrap your ",True)
            if (ment < (lib - 10)) and (ment >= (lib - 25)):
               OutputMainText("You quickly head off to the private place where you sleep with your intentions clear as those around " + RegionName(currentZone) + " can easily see your " + CockDesc() + " bulge growing in your " + ClothesBottom() + ". Before you even reach your destination, you're already pulling the " + ClothesBottom() + " " + PullUD(2) + ", your cock" + Plural(1) + " flopping out." + "\n" + "\n" + "You're not too sure if anybody saw it before you disappeared into solitude, but that doesn't matter as you wrap your ",True)
            if (ment < (lib - 25)) and (ment >= (lib - 50)):
               OutputMainText("Your chest heaving with your heavy breathing, you don't think you can reach the private place where you sleep without blowing your load, the thought of coming hanging so heavily on your mind." + "\n" + "\n" + "Instead, you duck into one of the more hidden corners of " + RegionName(currentZone) + " as you pull " + PullUD(2) + " your " + ClothesBottom() + " and let your " + CockDesc() + " cock" + Plural(1) + " spring out. You hear somebody pass nearby, but you don't care as you wrap your ",True)
            if (ment < (lib - 50)):
               OutputMainText("Without a second thought, right in the middle of " + RegionName(currentZone) + " you pull " + PullUD(2) + " your " + ClothesBottom() + " and whip out your " + CockDesc() + " wang" + Plural(1) + "." + "\n" + "\n" + "People gasp and stare as you wrap your ",True)
            if ((cockSize * cockSizeMod) <= (tallness / 3.75)):
               OutputMainText("hand around your " + _loc2_ + " and slowly pump it, building stronger and stronger.",False)
            if ((cockSize * cockSizeMod) > (tallness / 3.75)) and ((cockSize * cockSizeMod) <= (tallness * 1.2)):
               OutputMainText("hands around your " + _loc2_ + " , ",False)
               if ((cockSize * cockSizeMod) > (tallness / 1.5)):
                  if (breastSize > 4):
                     OutputMainText("hugging it between your " + boobTotal + " breasts, ",False)
                  else:
                     OutputMainText("hugging it to your chest, ",False)
               OutputMainText("pounding your fists up and down its length.",False)
            if ((cockSize * cockSizeMod) > (tallness * 1.2)):
               OutputMainText("arms around your " + _loc2_ + ", hugging it close and trying to jerk yourself the best you can.",False)
            if (MoistCalc(1) > 0) and (MoistCalc(1) <= 3):
               OutputMainText(" Drops of pre help aid your efforts, though it's still a little rough.",False)
            if (MoistCalc(1) > 3) and (moistCalc(1) <= 7):
               OutputMainText(" A dribble of pre leaks out, sufficiently coating your " + CockDesc() + " cock and making your efforts so much easier.",False)
            if (MoistCalc(1) > 7) and (MoistCalc(1) <= 11):
               OutputMainText(" Pre squeezes out of your cock and more than coat your " + CockDesc() + " cock, with plenty extra drooling down across your " + SkinDesc() + ".",False)
            if (MoistCalc(1) > 11):
               OutputMainText(" A flood of pre gushes out from the tip, sufficiently coating yourself, your " + CockDesc() + " cock and then some in slick lubrication.",False)
            if (showBalls == True):
               OutputMainText(" One of your hands reaches down to knead your " + BallDesc() + " scrotum, letting your " + balls + " cum-factories know it's time.",False)
            if (lust <= 30):
               OutputMainText("\n" + "\n" + "Slowly,",False)
            if (lust > 30) and (lust <= 70):
               OutputMainText("\n" + "\n" + "Quickly,",False)
            if (lust > 70):
               OutputMainText("\n" + "\n" + "Almost instantly,",False)
            OutputMainText(" your " + _loc2_ + " throbs, a pressure building at the base of your spine",False)
            if (knot == True):
               OutputMainText(", the base of your cock swelling into a thick knot that you begin to tug",False)
            OutputMainText(".",False)
            if (cockTotal > 1):
               OutputMainText(" Your other cocks do the same, your hands dashing back and forth between them, attempting to not leave them completely ignored.",False)
            OutputMainText("Your " + HipDesc() + " hips soon jerk as thick strands of hot spunk launch from your cock-tip" + Plural(1) + ",",False)
            if (_loc3_ <= 24):
               OutputMainText(" with a bit more drooling down to the floor.",False)
            if (_loc3_ > 24) and (_loc3_ <= 72):
               OutputMainText(" spitting small wads again and again until it's done.",False)
            if (_loc3_ > 72) and (_loc3_ <= 1000):
               OutputMainText(" spewing large gobs again and again until you've made a heck of a mess.",False)
            if (_loc3_ > 1000) and (_loc3_ <= 2200):
               OutputMainText(" coming more and more, like it can't stop, until you've made so much cum that you could feed a person with it for a day...",False)
            if (_loc3_ > 2200) and (_loc3_ <= 4500):
               OutputMainText(" the stuff gushing like a fire-hose. Somewhere between half and a full gallon, you're not sure what to do with it all!",False)
            if (_loc3_ > 4500) and (_loc3_ <= 20000):
               OutputMainText(" gallons upon gallons of it spewing and spraying out, nearly nonstop. If you had a tub with you, you could have taken a bath in it all!",False)
            if (_loc3_ > 20000):
               OutputMainText(" so much, so strong, it keeps on spewing out! Gallons and gallons, your body is wracked by the long ejaculation. After a while, your mind can't take any more and you pass out, only to wake up in a pool of cum and no way to take care of it all... You sneak away.",False)
               DoLust(-math.floor(sen / 2),2,1)
               hrs = 5
               exhaustion -= 2
               i += 1
            else:
               if (ment >= (lib - 10)):
                  OutputMainText("\n" + "\n" + "You quietly heave as you attempt to clean up your mess with the towels you have brought along, hiding them until you can safely clean them without being caught. Except for the smell that permeates the area, you don't think anybody will catch on to your lewd actions, and you continue on with your day.",False)
               if (ment < (lib - 10)) and (ment >= (lib - 25)):
                  OutputMainText("\n" + "\n" + "Coming down from your high, you clean up your mess the best you can, though its likely some cum was left behind. At least, it smells like some was. And as you leave the place, one of your neighbors eyes you with a surprised look. You were probably a bit loud... Or maybe you have a wad of cum in your hair?",False)
               if (ment < (lib - 25)) and (ment >= (lib - 50)):
                  OutputMainText("\n" + "\n" + "You realize your hiding place is a mess as you come to your senses. Before you're caught, you quickly don your " + ClothesBottom() + " again, even though your cock is still drooling and leaving quite the blotch. As you attempt to casually walk away, some nearby strangers blink at you curiously, not quite sure what they just heard. You then dash off before anybody tries to check out what you left behind.",False)
               if (ment < (lib - 50)):
                  OutputMainText("\n" + "\n" + "Gasping, you blink and look around you. You've gathered quite the crowd, especially some women, and they all gaze out you in amazement. A few tug at their own groins, ducking away from the rest, while others don't look so happy at what you have done, especially the ones with children beside them. You pull " + PullUD(2) + " your " + ClothesBottom() + ", cum dripping down the front and smearing about within, and you slink away, trying to avoid any more stares. Although, your heart pounds within your chest at the thought of what you had just done...",False)
               if (_loc3_ < 1000):
                  OutputMainText("\n" + "\n" + "\n" + "You have produced " + _loc3_ + " ml of spooge!",False)
               elif (_loc3_ >= 1000):
                  OutputMainText("\n" + "\n" + "\n" + "You have produced " + DecGet(_loc3_ / 1000,1) + " liters of spooge!",False)
               DoLust(-math.floor(sen / 2),2,1)
               hrs = 1
               i += 1
         if (_loc4_ == 2) and ((cockSize * cockSizeMod * 6) > tallness) and ((cockSize * cockSizeMod * 8) < (tallness * 3)):
         {
         }
         if (_loc4_ == 3) and (_loc3_ > 2000):
         {
         }
         if (_loc4_ == 4) and (ment < (lib - 50)):
         {
         }
         if ((_loc4_ == 5) and ((attireBot == 6) or (attireBot == 17)) and (lust > 80)):
         {
         }
         if (_loc4_ == 6 and ((attireBot == 5) or (attireBot == 7) or (attireBot == 12) or (attireBot == 13) or (attireBot == 14) or (attireBot == 16)) and (lust > 45)):
            OutputMainText("Already half hard from your lingering lust, just the thought of masturbating makes your " + CockDesc() + " erection" + Plural(1) + " stiffen to full length. Which produces a slight problem... Your arousal is fairly evident through your " + ClothesBottom() + " as your rod" + Plural(1) + " lift" + Plural(3) + " the fabric forward. You do your best to press it back down in an attempt to hide " + Plural(9) + ", but ",True)
            if ((cockSize * cockSizeMod) > 10):
               OutputMainText("" + Plural(11) + " wind up popping out beneath, accidentally flashing a random passerby who quickly pick up their pace to get away before you can try to catch your long thing" + Plural(1) + " back within the cloth.",False)
            else:
               OutputMainText("" + Plural(11) + " inevitably slide back up anyways, making your efforts futile.",False)
            OutputMainText("\n" + "\n" + "Looking for a quick escape, you slink behind the closest structure you can find. Glancing left and right to ensure nobody can see you, you pant as you look down at your tented " + ClothesBottom() + ".",False)
            if (MoistCalc(1) > 8):
               OutputMainText(" Pre seeping through the fabric and drizzling down in a steady strand over the edge",False)
            elif (MoistCalc(1) > 4):
               OutputMainText(" Pre soaking through the fabric and glistening with a large drop on the outside",False)
            else:
               OutputMainText(" Pre blotching the fabric with a large moist spot",False)
            OutputMainText(", you have no choice but to pull the clothing up, letting your wang" + Plural(1) + " bounce out. Grabbing " + Plural(9) + " the best you can in your impetuous state, you stroke strongly and swiftly. You lean back against the structure, with people openly walking and talking just on the other side, as you masturbate fervently." + "\n" + "\n" + "The fear of being caught only makes your heart beat faster, quickly producing results in your loins. You hardly hold back for a second to let the pressure build, before you release it in a spurting torrent of white fluid. You continue to pet yourself, squeezing out the leftover cum, while your mind savors the dwindling orgasm." + "\n" + "\n" + "Half-aware of what you had just done, your mind still in a fuzz, you simply catch your cock" + Plural(1) + " within your " + ClothesBottom() + " once more, staining it slightly with the gobs of seed at your tip" + Plural(1) + ", and leave your secluded area to head back into the public, leaving behind your puddle of lewd mess for someone else to stumble across...",False)
            DoLust(-math.floor(sen / 2),2,1)
            i += 1
         if ((_loc4_ == 7) and ((attireBot == 4) or (attireBot == 15) or (attireBot == 20))):
            OutputMainText("With the thought of masturbating on your mind, you can feel your cock" + Plural(1) + " begin to swell in anticipation. The tight confines of your " + ClothesBottom() + " rapidly growing tighter, you hurry on home." + "\n" + "\n" + "Just as you step through the doorway to your private abode, the waistband of your " + ClothesBottom() + " can no longer contain the " + CockDesc() + " bulge. Your length" + Plural(1) + " leap" + Plural(3) + " out, flinging ",True)
            if (MoistCalc(1) > 8):
               OutputMainText("ropes",False)
            elif (MoistCalc(1) > 4):
               OutputMainText("strands",False)
            else:
               OutputMainText("drops",False)
            OutputMainText(" of pre out across the floor while the shaft" + Plural(1) + " droop" + Plural(3) + " half-flaccidly over the edge. You slump against the nearest wall, gripping yourself as you eagerly start the stroking process. Free of " + Plural(5) + " small prison, the blood-flow picks up, quickly allowing " + Plural(9) + " to stiffen to full size while your hands stroke the sensitive skin. Your stroking turns to rhythmic pumps and your back presses against the wall, your hips bucking back in turn.",False)
            if (showBalls == True):
               OutputMainText(" You can wholly feel the pressure in your " + BallDesc() + " balls building, especially as the " + ClothesBottom() + " continues to grip and squeeze them as it hugs your bottom to stay on amidst your efforts.",False)
            OutputMainText("\n" + "\n" + "Before long, you wince as you try to hold back a little, one last moment of restraint until you let the fluids spray freely, escaping from your body with enough force to shoot across your room. So strong an orgasm, your " + LegDesc(2) + " grow" + LegPlural(1) + " weak and you slide down the wall, until you're sitting on the floor while the last spurts of cum shoot out between your " + LegDesc(6) + "." + "\n" + "\n" + "A bit tired, you sit there for a little while longer as the stuff drools from your tip" + Plural(1) + ".",False)
            if (knot == True):
               OutputMainText(" Despite being done, your swollen knot" + Plural(1) + " refuse to allow your member" + Plural(1) + " to slip back into the " + ClothesBottom() + ", standing defiantly against the waistband. The most you can do for now is stuff the knot" + Plural(1) + " into the crotch of the piece and hope you soften up later as you proceed to clean up your mess.",False)
            else:
               OutputMainText(" Your softening member" + Plural(1) + " slowly recede back into the " + ClothesBottom() + ", leaving a slight slimy trail in the process, but at least allows you to tuck " + Plural(9) + " away for now as you proceed to clean up the mess you made.",False)
            DoLust(-math.floor(sen / 2),2,1)
            i += 1
         if((_loc4_ == 8) and ((attireBot == 10) or (attireBot == 11)) and (lust > 60)):
         {
         }
      DoEnd()

def DoVagMasturbate():
   global lust, ment, lib, currentZone, vagTotal, tallness, sen, hrs, cockSize, cockSizeMod, vulvaSize, clitSize, cockTotal
   tempInt = 0
   chance = 0
   if (lust < 20):
      OutputMainText("You're not really in the mood to play with yourself. You'll just have to settle for something else.",True)
      DoEnd()
   else:
      tempInt = math.floor((Percent() / 20) + (ment / 5) + (lib / 5))
      i = 0
      while (i == 0):
         chance = math.floor(random.random() * (1 + 6 - 1)) + 1
         if (chance == 1):
            if (ment >= (lib - 10)):
               OutputMainText("You sneak off to the private place where you sleep in " + RegionName(currentZone) + " with a bunch of towels in hand. Carefully, so as to not let anybody hear, you pull " + PullUD(2) + " your " + ClothesBottom() + ", and gently squeeze your " + VulvaDesc() + " nether-lips." + "\n" + "\n" + "You lay down on your back and slide your fingers through the front of the cleft" + Plural(2) + " at your crotch, you tease your " + ClitDesc() + " button" + Plural(2) + ". Stiff and erect, you rub ",True)
            if (ment < (lib - 10)) and (ment >= (lib - 25)):
               OutputMainText("You quickly head off to the private place where you sleep with your intentions clear as those around " + RegionName(currentZone) + " can easily see you rub your " + VulvaDesc() + " groin through your " + ClothesBottom() + ". Before you even reach your destination, you're already pulling the " + ClothesBottom() + " " + PullUD(2) + ", accidentally flashing someone your " + ButtDesc() + " bum." + "\n" + "\n" + "Nevertheless, you squeeze your nether-lips, rubbing your hands down through your " + VulvaDesc() + " crotch, grinding your " + ClitDesc() + " button" + Plural(2) + " and kneading ",True)
            if (ment < (lib - 25)) and (ment >= (lib - 50)):
               OutputMainText("Your chest heaving with your heavy breathing, you don't think you can reach the private place where you sleep without crouching and " + LegVerb(2) + " your " + LegDesc(2) + " erotically, the thought of coming hanging so heavily on your mind." + "\n" + "\n" + "Instead, you duck into one of the more hidden corners of " + RegionName(currentZone) + " as you pull " + PullUD(2) + " your " + ClothesBottom() + ", squeezing your " + VulvaDesc() + " nether-lips with anticipation and tug at your " + ClitDesc() + " clit" + Plural(2) + " grinding ",True)
            if (ment < (lib - 50)):
               OutputMainText("Without a second thought, right in the middle of " + RegionName(currentZone) + " you pull " + PullUD(2) + " your " + ClothesBottom() + ", rubbing a hand across your " + VulvaDesc() + " cunt and pinching your " + ClitDesc() + " clit" + Plural(2) + "." + "\n" + "\n" + "People gasp as you continue to grind ",True)
            if (vagTotal > 1):
               OutputMainText("them ",False)
            if (vagTotal == 1):
               OutputMainText("it ",False)
            OutputMainText("vigorously, making ",False)
            if (vagTotal > 1):
               OutputMainText("them ",False)
            if (vagTotal == 1):
               OutputMainText("it ",False)
            OutputMainText("stiff. Faster and faster you go, until your " + VulvaDesc() + " vulva swells with blood.",False)
            if (MoistCalc(2) > 0) and (MoistCalc(2) <= 3):
               OutputMainText(" A bit of sweet feminine honey slips out from " + LegWhere(1) + " your " + LegDesc(2) + ", your hand taking as much as possible to meagerly lubricate your sex.",False)
            if (MoistCalc(2) > 3) and (MoistCalc(2) <= 7):
               OutputMainText(" Some sweet feminine honey dribbles from " + LegWhere(1) + " your " + LegDesc(2) + ", slipping back across your " + ButtDesc() + " tush and smearing across your thighs, plenty to take care of business.",False)
            if (MoistCalc(2) > 7) and (MoistCalc(2) <= 11):
               OutputMainText(" Lubricant spills from your slit" + Plural(2) + ", running down your " + LegDesc(2) + " and smearing across your " + ButtDesc() + " backside, dribbling off your body, more than enough to frig yourself silly.",False)
            if (MoistCalc(2) > 11):
               OutputMainText(" Fem-cum floods your crotch, loudly slurping as your hands, all the way up to your elbows, become slick with the stuff. Your " + ButtDesc() + " ass is practically sopping with it and more flings across your " + LegDesc(2) + " and down below you as you go.",False)
            if (lust <= 30):
               OutputMainText("\n" + "\n" + "Slowly,",False)
            if (lust > 30) and (lust <= 70):
               OutputMainText("\n" + "\n" + "Quickly,",False)
            if (lust > 70):
               OutputMainText("\n" + "\n" + "Almost instantly,",False)
            OutputMainText(" your cunt" + Plural(2) + " begin" + Plural(4) + " to quake and shiver, your whole body tingling. So eager, you ram ",False)
            if (VagLimit() <= (tallness / 5)):
               OutputMainText("a finger",False)
            if (vagLimit() > (tallness / 5)) and (VagLimit() <= (tallness / 2.2)):
               OutputMainText("your fingers",False)
            if (VagLimit() > (tallness / 2.2)) and (VagLimit() <= (tallness / 1.25)):
               OutputMainText("your hand",False)
            if (VagLimit() > (tallness / 1.25)) and (VagLimit() <= (tallness * 1.2)):
               OutputMainText("both hands",False)
            if (VagLimit() > (tallness * 1.2)) and (VagLimit() <= (tallness * 1.7)):
               OutputMainText("your forearm",False)
            if (VagLimit() > (tallness * 1.7)):
               OutputMainText("as much of one arm as possible",False)
            this.outputMainText(" into " + this.oneYour(2) + " hungry hole" + this.plural(2) + ", pounding away at yourself. Your body twitches and jerks as you come again and again.",false);
            if (ment >= lib - 10):
               OutputMainText("\n" + "\n" + "You quietly heave as you attempt to clean up your mess with the towels you have brought along, hiding them until you can safely clean them without being caught. Except for the smell that permeates the area and the bit of slurping that echoed, you don't think anybody will catch on to your lewd actions, and you continue on with your day.",False)
            if (ment < (lib - 10)) and (ment >= (lib - 25)):
               OutputMainText("\n" + "\n" + "Coming down from your high, you clean up your mess the best you can, though its likely some of your slick lubricant has seeped in somewhere. At least, you're cautious of your step, in case of slipping and falling back on your " + ButtDesc() + " ass... And as you leave the place, one of your neighbors eyes you with a surprised look. You were probably a bit loud... Well... you were definitely loud, actually.",False)
            if (ment < (lib - 25)) and (ment >= (lib - 50)):
               OutputMainText("\n" + "\n" + "You realize your hiding place probably echoed your moans as you come to your senses. Before you're caught, you quickly don your " + ClothesBottom() + " again, even though fem-cum is still slathered about and making your " + ClothesBottom() + " blotch. As you attempt to casually walk away, some nearby strangers blink at you curiously, not quite sure what they just heard. With an awkward flutter in your step, you dash off, your body still slightly in mid-orgasm.",False)
            if (ment < (lib - 50)):
               OutputMainText("\n" + "\n" + "Gasping, you blink and look around you. You've gathered quite the crowd, especially some men, and they all gaze out you in amazement. A few tug at their own groins, ducking away from the rest, while others don't look so happy at what you have done, especially the ones with children beside them. You pull " + PullUD(2) + " your " + ClothesBottom() + ", slick slime dripping down your " + LegDesc(2) + " and smearing about within, and you slink away, trying to avoid any more stares. Although, your heart pounds within your chest at the thought of what you had just done...",False)
            DoLust(-math.floor(sen / 2),2,1)
            hrs = 1
            i += 1
         if (chance == 2) and ((cockSize * cockSizeMod * 6) > tallness) and ((cockSize * cockSizeMod * 8) < (tallness * 3)):
         {
         }
         if (chance == 3):
         {
         }
         if (chance == 4) and (ment < (lib - 50)):
         {
         }
         if ((chance == 5) and ((attireBot == 6) or (attireBot == 17) or (attireBot == 20)) and (lust > 60)):
         {
         }
         if (chance == 6 and ((attireBot == 13) or (attireBot == 14)) and (lust > 80)):
            OutputMainText("With the cooler air easily breezing underneath your " + ClothesBottom() + " and over your moistened nethers, the thought of masturbating just makes your " + LegDesc(2) + " weak and buckle. Even if your place was only ten feet away, it would be an eternity to get there in this state. You don't think you could ever make it... So you manage to convince yourself you have no other choice." + "\n" + "\n" + "You manuever your bag to your front, feigning an attempt to look through it for something. Adjusting it slightly, it very easily manages to cover the high edge of your " + ClothesBottom() + ". While one hand holds up the bag, the other slinks behind, sneaking underneath your scant outfit. Right out in the middle of " + RegionName(currentZone) + ", with people walking by just a few feet away, your fingers touch your intimate region." + "\n" + "\n",True)
            if (vulvaSize < 30):
               OutputMainText("Swiftly slipping through your fingers through the tender folds, your " + HipDesc() + " hips start to rock gently as you stand there. Soft slurps slip out from your thighs as you cautiously masturbate in public, with the rustling of the bag in front of you thankfully drowning it out.",False)
            else:
               OutputMainText("Sloshing your entire hand through the quite obvious folds, you actually wonder if the " + VulvaDesc() + " lips normally poke out from under the cloth... The thought of modesty is quickly pushed aside, however, as your hips rock against your fist, making you gasp in pleasure. The lewd slurping is quite obvious over the heavy rustling of your bag, drawing some eyes to your direction, but you're too lost with pushing through your meaty lips to care.",False)
            if (clitSize > 20):
               OutputMainText(" You can feel your clit" + Plural(2) + " tent the " + ClothesBottom() + " and gently scrape against the back of the bag whenever your thumb wraps around and rubs " + Plural(10) + " with each pass of your hand.",False)
            else:
               OutputMainText(" Your thumb wraps around and rubs across your clit" + Plural(2) + " with each pass of your hand, making you buck against the back of the bag.",False)
            if (cockTotal > 0):
               OutputMainText(" Along with your movements, your cock" + Plural(1) + " also knock" + Plural(3) + " upon your bag from behind, completely neglected as any more stroking would be far to obvious in this state.",False)
            OutputMainText(" With the heated slick-friction in your loins and the anxiety of doing this amidst complete strangers, your heart beats so powerfully that it doesn't take long for your whole body to begin burning with orgasm." + "\n" + "\n",False)
            if (MoistCalc(2) > 8):
               OutputMainText("Managing to muffle the moans building in your throat as you peak, your stealthy pleasuring is betrayed by the waterfall of juices that descend " + LegWhere(1) + " your " + LegDesc(2) + ". Splashing loudly across the ground, your fem-cum draws the attention of several others, their eyes turning to stare at the drooling strands of thick slime that slowly falls post-orgasm. Webs of the stuff stretch over the gap " + LegWhere(1) + " your " + LegDesc(2) + ", with large gobs of the lubricant forming puddles about your " + LegDesc(10) + "." + "\n" + "\n" + "In the seconds it takes to catch your breath and realize you've been caught, a heavy blush fills your cheeks. You lower your head and lift your bag back up, more slime trailing from the guilty hand, and proceed to run off, a slight limp and squish in your step as the excess fluids allow your thighs to slip erotically over your sensitive bits...",False)
            elif(MoistCalc(2) > 4):
               OutputMainText("Muffling most of the moan that builds with your climax, you can feel your fluids spill down to your " + LegDesc(6) + ". The audible squishing and slurping of the spilling lubrication quickly cut your orgasm short, bringing your attention to the few eyes that have turned toward you. Blush warming your face and the tinges of climax still lingering, you do your best to act as casually as possible." + "\n" + "\n" + "Lowering the bag even further to disguise the fem-cum that drizzles lightly down your " + LegDesc(2) + ", you turn and rush away, hoping nobody notices the shimmering strands that reach back to your sensitive bits as the drops slowly spill to the ground beneath you...",False)
            else:
               OutputMainText("Muffling your moans as you come, you're able to take a few breaths of relief and relaxation as you relish the sensations. Not a soul knows what you have done, allowing you to fully enjoy your orgasm. And when you slip your hand back out from behind the bag, you take a moment to quickly lick off the moistness upon them, your pleasured flavor quite tasty." + "\n" + "\n" + "As if nothing had happened at all, you're able to pick up your bag and strut off, your thighs sqeezing the sensitive lips slightly with each step.",False)
            DoLust(-math.floor(sen / 2),2,1)
            hrs = 1
            i += 1
         if ((chance == 7) and ((attireBot == 4) or (attireBot == 15))):
         {
         }
         if ((chance == 8) and ((attireBot == 10) or (attireBot == 11)) and (lust > 60)):
         {
         }
      DoEnd()

def DoBothMasturbate():
   global ment, lib, lust
   if (ment >= (lib - 10)):
      OutputMainText("",True)
   if (ment < (lib - 10)) and (ment >= (lib - 25)):
      OutputMainText("",True)
   if (ment < (lib - 25)) and (ment >= (lib - 50)):
      OutputMainText("",True)
   if (ment < (lib - 50)):
      OutputMainText("",True)
   if (lust > 20):
      DoSexP(10)

def DoBoobMasturbate():
   global lustArray, breastSize, lactation, ment, lib, currentZone, nippleSize, boobTotal, sen, lust, dominant, nipplePlay, nipType, milkHPMod, hrs
   _loc1_ = 0
   _loc2_ = 0
   lustArray = [4]
   if (breastSize > 16):
      lustArray.push(23)
   elif (breastSize < 5):
      lustArray.push(24)
   i = 0
   while (i == 0):
      _loc1_ = math.floor(random.random() * (1 + 6 - 1)) + 1
      if (_loc1_ == 1):
         if (lactation > 0):
            lustArray.push(53)
         if (ment >= (lib - 10)):
            OutputMainText("You sneak off to the private place where you sleep in " + RegionName(currentZone) + ". Carefully, so as to not let anybody hear, you pull " + PullUD(1) + " your " + ClothesTop() + " and gently knead your " + BoobDesc() + " breasts." + "\n" + "\n" + "Hunching over at the side of the bed, you massage your " + NipDesc() + "nipples, tugging and squeezing them each with",True)
         if (ment < (lib - 10)) and (ment >= (lib - 25)):
            OutputMainText("You quickly head off to the private place where you sleep with your intentions clear as those around " + RegionName(currentZone) + " can easily see you rub your " + BoobDesc() + " chest through your " + ClothesTop() + ". Before you even reach your destination, your hands are already reaching under your " + ClothesTop() + " to play with your " + NipDesc() + "nipples, giving someone a good view of your under-boob." + "\n" + "\n" + "By the time you're hidden inside, both hands are fondling your chest, kneading and massaging your nipples with",True)
         if (ment < (lib - 25)) and (ment >= (lib - 50)):
            OutputMainText("Your " + BoobDesc() + " breasts heave with your heavy breathing as you think about playing with them. You don't think you can reach the private place where you sleep without your hands diving underneath your " + ClothesTop() + " and massaging them roughly." + "\n" + "\n" + "Instead, you duck into one of the more hidden corners of " + RegionName(currentZone) + " and without even taking off your " + ClothesTop() + ", you grope your chest through the fabric before reaching underneath, kneading and massaging your " + NipDesc() + "nipples with",True)
         if (ment < (lib - 50)):
            OutputMainText("Without a second thought, right in the middle of " + RegionName(currentZone) + " you pull " + PullUD(1) + " your " + ClothesTop() + ", rubbing a hand across your " + BoobDesc() + " breasts and making them jiggle obscenely." + "\n" + "\n" + "People gasp and stare as you knead and massage your " + BipDesc() + "nipples with",True)
         if (nippleSize <= 25):
            OutputMainText(" your fingers",False)
         elif (nippleSize > 25) and (nippleSize <= 60):
            OutputMainText(" your hands",False)
         elif (nippleSize > 60) and (nippleSize <= 180):
            OutputMainText(" both hands",False)
         elif (nippleSize > 180):
            OutputMainText(" the nearby wall",False)
         OutputMainText(" until they begin to feel warm and tingly.",False)
         if (boobTotal == 4):
            OutputMainText(" Your hands even double their work as they fondle your second set of breasts as well, molding and massaging them just as much as the first pair, feeling twice as much pleasure.",False)
         if (boobTotal == 6):
            OutputMainText(" Your hands have their work cut out for them as they attempt to give all 6 of your breasts attention, running up and down, from chest to belly, caressing them restlessly as you heave to control yourself just a little longer.",False)
         if (boobTotal == 8):
            OutputMainText(" From chest to lower belly, your hands continue to rove to fondle all four sets of tits, fervently groping them all with great pleasure.",False)
         if (sen <= 30):
            OutputMainText(" Unfortunately, you can't really come as your breasts simply aren't sensitive enough. But, it does feel nice as you continue to play with your nipples.",False)
            DoLust(-math.floor(sen / 5),2,3)
         else:
            if (lust <= 30):
               OutputMainText("\n" + "\n" + "Slowly,",False)
            if (lust > 30) and (lust <= 70):
               OutputMainText("\n" + "\n" + "Quickly,",False)
            if (lust > 70):
               OutputMainText("\n" + "\n" + "Almost instantly,",False)
            OutputMainText(" your whole body begins to quiver,",False)
            if ((MoistCalc(1) > 0) and ((MoistCalc(1) <= 3) or (MoistCalc(2) > 0)) and (MoistCalc(2) <= 3)):
               OutputMainText(" your " + ClothesBottom() + " growing a tad moist,",False)
            if ((MoistCalc(1) > 3) and ((MoistCalc(1) <= 7) or (MoistCalc(2) > 3)) and (MoistCalc(2) <= 7)):
               OutputMainText(" your " + ClothesBottom() + " growing wet,",False)
            if((MoistCalc(1) > 7) and ((MoistCalc(1) <= 11) or (MoistCalc(2) > 7)) and (MoistCalc(2) <= 11)):
               OutputMainText(" your " + ClothesBottom() + " becoming soaked through,",False)
            if ((MoistCalc(1) > 11) or (MoistCalc(2) > 11)):
               OutputMainText(" your " + ClothesBottom() + " becoming drenched, your " + ButtDesc() + " bum absolutely swamped,",False)
            OutputMainText(" being wracked by a boobgasm.",False)
            DoLust(-math.floor(sen / 2),2,3)
         if (lactation > 0):
            hrs += 1
            _loc2_ = MilkAmount(1)
            OutputMainText("\n" + "\n" + "Milk ",False)
            if (_loc2_ <= 500):
               OutputMainText("spits",False)
            if (_loc2_ > 500) and (_loc2_ <= 1000):
               OutputMainText("squirts",False)
            if (_loc2_ > 1000) and (_loc2_ <= 2000):
               OutputMainText("spews",False)
            if (_loc2_ > 2000) and (_loc2_ <= 8000):
               OutputMainText("gushes",False)
            if(_loc2_ > 8000) and (_loc2_ <= 19000):
               OutputMainText("erupts",False)
            if (_loc2_ > 19000):
               OutputMainText("explodes",False)
            OutputMainText(" from your nipples and dribbles down your front as you begin to lactate. You continue to pump it out in ",False)
            if (_loc2_ <= 500):
               OutputMainText("small dribbles",False)
            if (_loc2_ > 500) and (_loc2_ <= 1000):
               OutputMainText("spurts",False)
            if (_loc2_ > 1000) and (_loc2_ <= 2000):
               OutputMainText("sprays",False)
            if (_loc2_ > 2000) and (_loc2_ <= 8000):
               OutputMainText("jets",False)
            if (_loc2_ > 8000) and (_loc2_ <= 19000):
               OutputMainText("steady streams",False)
            if (_loc2_ > 19000):
               OutputMainText("small floods",False)
            OutputMainText(", relieving your " + BoobDesc() + " breasts of their supply",False)
            if (dominant == 5):
               OutputMainText(" as you let out a contented 'mooo~'",False)
            OutputMainText(".",False)
         if (ment >= (lib - 10)):
            OutputMainText("\n" + "\n" + "You quietly heave as you attempt to clean up any mess you have made, hoping the bedsheets will dry quickly. Except for some stains, you don't think anybody will catch on to your lewd actions, and you continue on with your day.",False)
         if (ment < (lib - 10)) and (ment >= (lib - 25)):
            OutputMainText("\n" + "\n" + "Coming down from your high, you clean up your mess the best you can, though its likely some of your fluids have seeped in somewhere. At least, you're cautious of cleaning any mess up with your sheets. And as you leave the place, one of your neighbors eyes you with a surprised look. You probably left a blotch or few on your clothes somewhere...",False)
         if (ment < (lib - 25)) and (ment >= (lib - 50)):
            OutputMainText("\n" + "\n" + "You realize your hiding place probably echoed your moans as you come to your senses. You also have the slight problem of milk blotching your " + ClothesTop() + "... As you attempt to casually walk away, some nearby strangers blink at you curiously, not quite sure what they just heard. Rubbing your chest through the fabric once more, you dash away hoping it will dry.",False)
         if (ment < (lib - 50)):
            OutputMainText("\n" + "\n" + "Gasping, you blink and look around you. You've gathered quite the crowd, especially some men, and they all gaze out you in amazement, having given them quite the show. A few tug at their own groins, ducking away from the rest, while others don't look so happy at what you have done, especially the ones with children beside them. You pull back your " + ClothesTop() + ", milk splashing everywhere and slink away, trying to avoid any more stares. Although, your heart pounds within your chest at the thought of what you had just done...",False)
         if (_loc2_ > 0) and (_loc2_ < 1000):
            OutputMainText("\n" + "\n" + "\n" + "You produced " + _loc2_ + " ml of milk!",False)
         elif (_loc2_ > 0) and (_loc2_ >= 1000):
            OutputMainText("\n" + "\n" + "\n" + "You produced " + DecGet(_loc2_ / 1000,1) + " liters of milk!",False)
         nipplePlay += 8
         i += 1
      if (_loc1_ == 2) and (((breastSize * 2) + (nippleSize * 5)) > (tallness / 5)) and (lactation > 0):
         lustArray.push(53)
         OutputMainText("Relaxing in your room, you sneak your breasts out of your " + ClothesTop() + ", palming their undersides and gently kneading them. Hanging from your chest, so soft and squishy, your anticipation over playing with them already begins to make drops of milk form around your nipples. The white nurturing fluid drips warmly from the tips, splashing upon your " + ClothesBottom() + ". It looks so delicious that you can't help but..." + "\n" + "\n" + "You reach under a boob and hoist it up, craning your neck down to meet ",True)
         if (nipType == 0):
            this.outputMainText("the " + NipDesc() + " nipple",False)
         elif (nipType == 1):
            OutputMainText("one of the four " + NipDesc() + " nipples",False)
         OutputMainText(" with your mouth. You lick around it at first, but quickly suck it into your mouth, letting out an unintended \"Mmm~\" as the erect peak readily compresses over your tongue, rewarding you with a mouthful of squirting sustenance. Sweet and rich, the stuff is better than it looked. And with your mouth fellating the stiffened nipple, the sensations and flavor only make you try to gulp down more, nomming and sucking with delight.",False)
         _loc2_ = MilkAmount(1)
         if (_loc2_ < 300):
            OutputMainText("\n" + "\n" + "Thin sprays occassionally spurt and spit about your mouth, with a gentle trickle dribbling down your throat. Though you may only produce a few mouthfuls before you run dry, you savor every swallow while your other ",False)
         elif (_loc2_ < 1500):
            OutputMainText("\n" + "\n" + "The flow picks up a little, with constant spurting about your mouth and down your throat. You steadily gulp again and again as your mouth refills, serving you a nice meal of milk while your other ",False)
         elif (_loc2_ < 3000):
            OutputMainText("\n" + "\n" + "The flow quickly increases with wide streams of milk spraying within your mouth and down your throat. You hastily gulp again and again to keep up with the outpour of milk, barely able to keep up with the supply and a little dribbling out the corners of your mouth while your other ",False)
         else:
            OutputMainText("\n" + "\n" + "Caught slightly off gaurd, the flow of milk rapidly increases to a powerful gushing. Like a geyser erupting in your mouth, you do all you can to drink down as much as possible, but plenty more floods out of your mouth in a pale waterfall over your body while your other ",False)
         if (nipType != 1) and (boobTotal == 2):
            OutputMainText(" breast ",False)
         else:
            OutputMainText(" tits ",False)
         OutputMainText(" do the same as you grope about with your other hand. Fluids splatter about, carelessly falling where they may with the warmth of climax casting over your mind." + "\n" + "\n" + "A sudden spike in the flow accompanies a shudder through your body, nearly biting down on your own nipple in ecstasy. You open wide and gasp as the nipple washes your mouth, with saliva and milk spilling out as you moan blissfully." + "\n" + "\n" + "You then collapse back into your bed, continuing to suckle from yourself slowly and express what is left in your breasts.",False)
         if (_loc2_ < 300):
            OutputMainText(" With the nice drink ",False)
            DoHP(2 + math.floor(milkHPMod / 2))
         elif (_loc2_ < 1500):
            OutputMainText(" With the small meal ",False)
            DoHP(8 + math.floor(milkHPMod / 2))
         elif (_loc2_ < 3000):
            OutputMainText(" With the abundant nourishment and slight bloating of your belly ",False)
            DoHP(10 + milkHPMod)
         else:
            OutputMainText(" With the grand feast leaving you with a hefty swelling of your abdomen and impromptu bath ",False)
            DoHP(math.ceil((30 + math.floor(_str_ / 2) + HPMod) / 4) + milkHPMod)
         OutputMainText(", you settle in for a short nap to help with the digestion, feeling quite pleased with yourself~",False)
         DoLust(-math.floor(sen / 2),2,3)
         hrs += 2
         i += 1
   hrs += 1
   DoEnd()

def DoUdderMasturbate():
   global udderLactation, lustArray, ment, lib, currentZone, teatSize, sen, lust, hrs, dominant, udderPlay, milkHPMod, _str_, HPMod
   _loc1_ = 0
   _loc2_ = 0
   lustArray = [4]
   i = 0
   while (i == 0):
      _loc1_ = math.floor(random.random() * (1 + 2 - 1)) + 1
      if (_loc1_ == 1):
         if (udderLactation > 0):
            lustArray.push(53)
         if (ment >= (lib - 10)):
            OutputMainText("You sneak off to the private place where you sleep in " + RegionName(currentZone) + " with a bunch of towels in hand. Carefully, so as to not let anybody hear, you pull " + PullUD(1) + " your " + ClothesTop() + " and gently knead your " + UdderDesc() + " udder." + "\n" + "\n" + "Hunching over at the side of the bed, you massage your " + TeatDesc() + " teats, tugging and squeezing them each with",True)
         if (ment < (lib - 10)) and (ment >= (lib - 25)):
            OutputMainText("You quickly head off to the private place where you sleep with your intentions clear as those around " + RegionName(currentZone) + " can easily see you rub your " + UdderDesc() + " bulge through your " + ClothesTop() + ". Before you even reach your destination, your hands are already reaching " + PullUD(1) + " under your " + ClothesTop() + " to play with your " + TeatDesc() + " teats, giving someone a good view of your fleshy bag." + "\n" + "\n" + "By the time you're hidden inside, both hands are fondling your udder, kneading and massaging your teats with",True)
         if (ment < (lib - 25)) and (ment >= (lib - 50)):
            OutputMainText("Your " + UdderDesc() + " udder heaves with your heavy breathing as you think about playing with it. You don't think you can reach the private place where you sleep without your hands diving underneath your " + ClothesTop() + " and massaging it roughly." + "\n" + "\n" + "Instead, you duck into one of the more hidden corners of " + RegionName(currentZone) + " and without even taking off your " + ClothesTop() + ", you grope your udder through the fabric before your reaching underneath, kneading and massaging your " + TeatDesc() + " teats with",True)
         if (ment < (lib - 50)):
            OutputMainText("Without a second thought, right in the middle of " + RegionName(currentZone) + " you pull " + PullUD(1) + " your " + ClothesTop() + ", rubbing a hand across your " + UdderDesc() + " udder and making it jiggle obscenely." + "\n" + "\n" + "People gasp and stare as you knead and massage your " + TeatDesc() + " teats with",True)
         if (teatSize <= 25):
            OutputMainText(" your fingers",False)
         elif (teatSize > 25) and (teatSize <= 60):
            OutputMainText(" your hands",False)
         elif (teatSize > 60) and (teatSize <= 180):
            OutputMainText(" both hands",False)
         elif (teatSize > 180):
            OutputMainText(" the nearby wall",False)
         OutputMainText(" until they begin to feel warm and tingly.",False)
         if (sen <= 30):
            OutputMainText(" Unfortunately, you can't really come as your udder simply isn't sensitive enough. But, it does feel nice as you continue to play with your teats.",False)
            DoLust(-math.floor(sen / 5),2,4)
         else:
            if (lust <= 30):
               OutputMainText("\n" + "\n" + "Slowly,",False)
            if (lust > 30) and (lust <= 70):
               OutputMainText("\n" + "\n" + "Quickly,",False)
            if (lust > 70):
               OutputMainText("\n" + "\n" + "Almost instantly,",False)
            OutputMainText(" your whole body begins to quiver,",False)
            if ((MoistCalc(1) > 0) and ((MoistCalc(1) <= 3) or (MoistCalc(2) > 0)) and (MoistCalc(2) <= 3)):
               OutputMainText(" your " + ClothesBottom() + " growing a tad moist,",False)
            if ((MoistCalc(1) > 3) and ((MoistCalc(1) <= 7) or (MoistCalc(2) > 3)) and (MoistCalc(2) <= 7)):
               OutputMainText(" your " + ClothesBottom() + " growing wet,",False)
            if ((MoistCalc(1) > 7) and ((MoistCalc(1) <= 11) or (MoistCalc(2) > 7)) and (MoistCalc(2) <= 11)):
               OutputMainText(" your " + ClothesBottom() + " becoming soaked through,",False)
            if ((MoistCalc(1) > 11) or (MoistCalc(2) > 11)):
               OutputMainText(" your " + ClothesBottom() + " becoming drenched, your " + ButtDesc() + " bum absolutely swamped,",False)
            OutputMainText(" being wracked by an udder orgasm.",False)
            DoLust(-math.floor(sen / 2),2,4)
         if (udderLactation > 0):
            hrs += 1
            _loc2_ = MilkAmount(2)
            OutputMainText("\n" + "\n" + "Milk ",False)
            if (_loc2_ <= 500):
               OutputMainText("spits",False)
            if (_loc2_ > 500) and (_loc2_ <= 1000):
               OutputMainText("squirts",False)
            if (_loc2_ > 1000) and (_loc2_ <= 2000):
               OutputMainText("spews",False)
            if (_loc2_ > 2000) and (_loc2_ <= 8000):
               OutputMainText("gushes",False)
            if (_loc2_ > 8000) and (_loc2_ <= 19000):
               OutputMainText("erupts",False)
            if (_loc2_ > 19000):
               OutputMainText("explodes",False)
            OutputMainText(" from your teats and dribbles down your front as you begin to lactate. You continue to pump it out in ",False)
            if (_loc2_ <= 500):
               OutputMainText("small dribbles",False)
            if (_loc2_ > 500) and (_loc2_ <= 1000):
               OutputMainText("spurts",False)
            if (_loc2_ > 1000) and (_loc2_ <= 2000):
               OutputMainText("sprays",False)
            if (_loc2_ > 2000) and (_loc2_ <= 8000):
               OutputMainText("jets",False)
            if (_loc2_ > 8000) and (_loc2_ <= 19000):
               OutputMainText("steady streams",False)
            if (_loc2_ > 19000):
               OutputMainText("small floods",False)
            OutputMainText(", relieving your " + UdderDesc() + " udder of its supply",False)
            if (dominant == 5):
               OutputMainText(" as you let out a contented 'mooo~'",False)
            OutputMainText(".",False)
         if (ment >= (lib - 10)):
            OutputMainText("\n" + "\n" + "You quietly heave as you attempt to clean up any mess you have made, hoping the bedsheets will dry quickly. Except for some stains, you don't think anybody will catch on to your lewd actions, and you continue on with your day.",False)
         if (ment < (lib - 10)) and (ment >= (lib - 25)):
            OutputMainText("\n" + "\n" + "Coming down from your high, you clean up your mess the best you can, though its likely some of your fluids have seeped in somewhere. At least, you're cautious of cleaning any mess up with your sheets. And as you leave the place, one of your neighbors eyes you with a surprised look. You probably left a blotch or few on your clothes somewhere...",False)
         if (ment < (lib - 25)) and (ment >= (lib - 50)):
            OutputMainText("\n" + "\n" + "You realize your hiding place probably echoed your moans as you come to your senses. You also have the slight problem of milk blotching your " + ClothesTop() + "... As you attempt to casually walk away, some nearby strangers blink at you curiously, not quite sure what they just heard. Rubbing your chest through the fabric once more, you dash away hoping it will dry.",False)
         if (ment < (lib - 50)):
            OutputMainText("\n" + "\n" + "Gasping, you blink and look around you. You've gathered quite the crowd, especially some men, and they all gaze out you in amazement, having given them quite the show. A few tug at their own groins, ducking away from the rest, while others don't look so happy at what you have done, especially the ones with children beside them. You pull " + PullUD(1) + " your " + ClothesTop() + ", milk splashing everywhere and slink away, trying to avoid any more stares. Although, your heart pounds within your chest at the thought of what you had just done...",False)
         if (_loc2_ > 0) and (_loc2_ < 1000):
            OutputMainText("\n" + "\n" + "\n" + "You produced " + _loc2_ + " ml of milk!",False)
         elif (_loc2_ > 0) and (_loc2_ >= 1000):
            OutputMainText("\n" + "\n" + "\n" + "You produced " + DecGet(_loc2_ / 1000,1) + " liters of milk!",False)
         udderPlay += 8
         i += 1
      if (_loc1_ == 2) and ((udderSize + teatSize * 5) > (tallness / 2)) and (udderLactation > 0):
         lustArray.push(53)
         OutputMainText("Relaxing in your room, you pull your udder out of your " + ClothesBottom() + ", lifting the underside and gently kneading the supple bag. Hanging from below your belly, so soft and squishy, your anticipation over playing with it already begins to make drops of milk form around your teats. The white nurturing fluid drips warmly from the tips, splashing over your " + LegDesc(2) + " and the floor. It looks so delicious that you can't help but..." + "\n" + "\n" + "You hug around the udder and hoist it up, craning your neck down to meet a " + TeatDesc() + " teat",True)
         OutputMainText(" with your mouth, guiding it with a hand. You lick around it at first, but quickly suck it into your mouth, letting out an unintended \"Mmm~\" as the erect peak readily compresses over your tongue, rewarding you with a mouthful of squirting sustenance. Sweet and rich, the stuff is better than it looked. And with your mouth fellating the semi-firm teat, the sensations and flavor only make you try to gulp down more, nomming and sucking with delight.",False)
         _loc2_ = MilkAmount(2)
         if (_loc2_ < 300):
            OutputMainText("\n" + "\n" + "Thin sprays occassionally spurt and spit about your mouth, with a gentle trickle dribbling down your throat. Though you may only produce a few mouthfuls before you run dry, you savor every swallow while your other ",False)
         elif (_loc2_ < 1500):
            OutputMainText("\n" + "\n" + "The flow picks up a little, with constant spurting about your mouth and down your throat. You steadily gulp again and again as your mouth refills, serving you a nice meal of milk while your other ",False)
         elif (_loc2_ < 3000):
            OutputMainText("\n" + "\n" + "The flow quickly increases with wide streams of milk spraying within your mouth and down your throat. You hastily gulp again and again to keep up with the outpour of milk, barely able to keep up with the supply and a little dribbling out the corners of your mouth while your other ",False)
         else:
            OutputMainText("\n" + "\n" + "Caught slightly off gaurd, the flow of milk rapidly increases to a powerful gushing. Like a geyser erupting in your mouth, you do all you can to drink down as much as possible, but plenty more floods out of your mouth in a pale waterfall over your body while your other ",False)
         OutputMainText(" teats do the same as you grope about with your other hand, your arm bending around to keep the udder elevated. Fluids splatter about, carelessly falling where they may with the warmth of climax casting over your mind." + "\n" + "\n" + "A sudden spike in the flow accompanies a shudder through your body, nearly biting down on your own teat in ecstasy. You open wide and gasp as the " + TeatDesc() + " teat washes your mouth, with saliva and milk spilling out as you moan blissfully." + "\n" + "\n" + "You then collapse back into your bed, curled around and continuing to suckle from yourself slowly, gently milking what is left in your udder.",False)
         if (_loc2_ < 300):
            OutputMainText(" With the nice drink ",False)
            DoHP(2 + math.floor(milkHPMod / 2))
         elif (_loc2_ < 1500):
            OutputMainText(" With the small meal ",False)
            DoHP(8 + math.floor(milkHPMod / 2))
         elif (_loc2_ < 3000):
            OutputMainText(" With the abundant nourishment and slight bloating of your belly ",False)
            DoHP(10 + milkHPMod)
         else:
            OutputMainText(" With the grand feast leaving you with a hefty swelling of your abdomen and impromptu bath ",False)
            DoHP(math.ceil((30 + math.floor(_str_ / 2) + HPMod) / 4) + milkHPMod)
         OutputMainText(", you settle in for a short nap to help with the digestion, feeling quite pleased with yourself~",False)
         DoLust(-math.floor(sen / 2),2,4)
         hrs += 2
         i += 1
   hrs += 1
   DoEnd()

!def DoAlchemy():
!def SimpleAlchemy():
!def ComplexAlchemy():
!def AdvancedAlchemy():
!def MakeAlchemy():
!def DoLevelUp():
!def DoExplore():
!def EventSelect():
!def DoSoftlik():
!def DoFirmshaft():
!def DoTieden():
!def DoSizCalit():
!def DoOviasis():
!def DoSanctuary():
!def DoForest():
!def DoJungle():
!def DoPlains():
!def DoSavanna():
!def DoDesert():
!def DoBeach():
!def DoDairyFarm():
!def DoOldCave():
!def DoDen():
!def DoValley():
def DoDungeon():
   global currentDungeon
   if (currentDungeon > 1000) and (currentDungeon <= 1010):
      DoOldCaveDescent()

!def DoOldCaveDescent():
   global currentDungeon, defeatedMinotaur, defeatedFreakyGirl, defeatedSuccubus
   if currentDungeon == 1001 or currentDungeon == 1002 or currentDungeon == 1003:
      if defeatedMinotaur == False:
         OutputMainText("With the lantern allowing you to actually see where you're going, you're able to venture much deeper into the old cave. It is surpisingly long for a cave that doesn't open up into a large cavern and there's not terribly much of note either, nothing you could have accidentally bumped into. The only thing particularly interesting are holes that line the bottom of the walls that angle downward, as a sort of natural drainage system for fluids. Otherwise, things are just rather... humid and slimy. It's not something you think too much about, however, as your light eventually begins to glisten off of the back wall of the cave, finally having reached the end. Or so you think it's the end." + "\n" + "\n" + "As you reach the back wall, you notice another cave branching off. Yet, it's not exactly another cave. From the way the stone is hewn and the entrance is elevated from the normal floor of the original cave, this appears to have been carved out. You step up inside and immediately notice... There's stairs going down. Since ventured this far in, you continue on, walking down the spiraling staircase." + "\n" + "\n" + "This passage appears to be ancient, with many of the steps rather worn from all the footsteps. The walls are slightly warped and scratched, but otherwise in good condition for their age. And they just keep going down and down and down... You quickly lose count of how many steps you've descended and it just becomes a relentless trek downward until... you find a room!" + "\n" + "\n" + "Although, it's not much of a room... Rectangular, somewhat large, lighted by a couple torches and relatively boring, with another stairwell against the opposite wall. This is just a sort of waypoint along the stairwell... But it's not empty either.",True)
         DoNext()
         doListen = function():void
            outputMainText("\"Who go there?!\" A loud grunting voice bellows in your direction." + "\n" + "\n" + "You blink at first, the hot and smelly breath catching you off guard, but you quickly grow aware of the large figure towering before you. Large horns nearly scraping the ceiling, the bulky muscular man before you stands in your way. The head of a bull, the body of a human, and the crotch... bulging massively beneath a simple loin cloth, this monster does not look pleased." + "\n" + "\n" + "\"I am Minotaur!,\" You're not entirely sure if he's stating his name or his ancestry... \"I no know you! I guardian! You no pass!\"" + "\n" + "\n" + "You don't exactly have time for a diplomatic solution as the creature charges towards you, his massive hands balling up into hard-looking fists as he makes his intentions clear.",True)
            enemyID = 307
            currentState = 2
            enemyBaseStats()
            eMaxHP = eHP
            doBattle()
      else:
         if currentDungeon == 1001:
            OutputMainText("You make your way back to the first 'checkpoint' along the large staircase in the old cave. The Minotaur you had bested is currently facing the wall, grunting and sweating, but quickly jerks to attention as he hears you enter. He quickly spins around to face you, acting like he had been busy guarding attentively the whole time. However, his big fat cock still throbs beneath his lazily drooped loin cloth, the aroused head poking out the side with a gob of pre drooling down. He pretends not to notice so he can tend to his duties, but exhales with a grunt as he sees you." + "\n" + "\n" + "\"Oh, just you. You can go, I know you now. Unless you want to try Minotaur again?\"",True)
         if currentDungeon == 1002:
            OutputMainText("With the Minotaur sitting in a corner sulking over his loss, you're free to either go up to the surface or venture further down the stairs.",True)
         if currentDungeon == 1003:
            OutputMainText("With the Minotaur laying on the ground, continuing to pleasure himself, you're free to either go up to the surface or venture further down the stairs.",True)
         ViewButtonOutline(1,1,0,1,0,0,0,0,0,0,0,0)
         ViewButtonText(1,1,0,1,0,0,0,0,0,0,0,0)
         ButtonWrite(4,"Firmshaft")
         ButtonWrite(1,"Fight")
         ButtonWrite(2,"Down")
         if currentDungeon != 1001:
            this.Choice1.visible = False
         doListen = function():void
            if buttonChoice == 2:
               if currentDungeon == 1001:
                  OutputMainText("The beast-man gives you a grunt. \"Fine.\"" + "\n" + "\n" + "Before you're even gone, he's already turning back to the wall and slipping a hand under his loin cloth... You head down the next set of stairs.",True)
               else:
                  outputMainText("You leave the beast-man to himself and head towards the stairs.",True)
               DoNext()
               doListen = function():void
                  currentDungeon = 1004
                  DoOldCaveDescent()
            if buttonChoice == 4:
               if currentDungeon == 1001:
                  OutputMainText("The beast-man gives you a grunt. \"Fine.\"" + "\n" + "\n" + "Before you're even gone, he's already turning back to the wall and slipping a hand under his loin cloth... You head back out to Firmshaft.",True)
               else:
                  OutputMainText("You leave the beast-man to himself and head towards the stairs.",True)
               DoNext()
               doListen = function():void
                  inDungeon = False
                  RegionChange(2)
                  DoEnd()
            if buttonChoice == 1:
               OutputMainText("\"Ahh, goody. Me need something to do!\" The beast-man begins to charge after you once more.",True)
               DoNext()
               doListen = function():void
                  enemyID = 307
                  currentState = 2
                  EnemyBaseStats()
                  eMaxHP = eHP
                  DoBattle()
   if currentDungeon == 1004 or currentDungeon == 1005 or currentDungeon == 1006:
      if defeatedFreakyGirl == False:
         OutputMainText("Even more stairs than before, you keep going and going, deeper below the surface. You don't know how long it takes, but you do know it's a while before you find the end and step into another room. Just like before, it's nothing too grandoise, just a rectangular room hewn in the ancient stone. And at the far and, you see even more stairs descending down... However, something far more interesting grabs your attention." + "\n" + "\n" + "\"Ooo, look Mr. Snuggles, someone to pway with!\" The cute little girly voice cuts through the boredom of stairs like a sweet delicate knife." + "\n" + "\n" + "Only as the girl gets up from sitting cross-legged do you notice a flash of her white panties. With the short frilly skirt that curls outward and shows off much of her supple legs, she must have been exposing her undergarments to you much longer as she sat on the floor. Although, you quickly try to dash that thought as you realize how young she seems to be. Barely over four feet tall, she hardly has any curves to speak of; a rather flat chest that hardly pushes out her soft shirt just by the slightly puffy nipples beneath and her hips more emphasized by the short bouncy skirt then their own girth. Her hair is bound on either side by big ribbons, pulled into two pigtails the dangle down past her shoulders, brushing across the puffed short sleeves of the otherwise tight-fitting shirt and exposing her large long ears that look almost goofy on her small form." + "\n" + "\n" + "And as she stands, her immaturity is further amplified by the large plushy doll she lifts with her. Nearly as large as herself, it looks like the minotaur you defeated in the previous room, except small and adorable. The thing seems to have seen a fair deal of use, however, as it's completely covered in patches of leather. You can't really tell how old it is, considering much of the leather looks brand new whereas other places look quite worn and faded, with quite a few gashes from some kind of scratches that should probably be patched up as well soon. Nevertheless, the girl hugs it close as she begins to skip around in a circle, her skirt bouncing with small glimpses of her undies as she frolics. \"We're gonna pla-ay~ We're gonna pla-ay~ We're gonna pla-ay~\"" + "\n" + "\n" + "She seems just so adorable that you almost feel obligated to play. That is... until she stops dead in her tracks and turns to you with a ferocious stare, her eyes looking far darker and her pigtails looking almost like wings as the hair curls outward sinisterly. Her nails dig into the leather of Mr. Snuggles, scratching it like all the other gashes you noticed, and she speaks in a much louder, much more snarling voice. \"IT'S BEEN YEARS SINCE I'VE HAD A GOOD TOY~\"" + "\n" + "\n" + "Uh oh...",True)
         DoNext()
         doListen = function():void
            enemyID = 308
            currentState = 2
            EnemyBaseStats()
            eMaxHP = eHP
            DoBattle()
      else:
         if currentDungeon == 1004:
            OutputMainText("Returning to the second floor of the cave descent, the strange little girl sits on the floor playing with Mr. Snuggles in her lap. As she spots you, she lifts the plushy leather minotaur up to her eyes and turns it toward you, using it as a puppet as she speaks in a fake menacing voice. \"Grr, did you come back to play some more~?\"",True)
         if currentDungeon == 1005:
            OutputMainText("The girl hides behind Mr. Snuggles, grumbling about how you're a \"Big fat meanie face\" and how she's \"GOING TO FEAST ON YOUR BONES\" for having defeated her, but she allows you to go as you please.",True)
         if currentDungeon == 1006:
            OutputMainText("The girl cuddles up with Mr. Snuggles, her hips still twitching and thrusting her enlarged clit into the doll, allowing you to go as you please.",True)
         ViewButtonOutline(0,1,0,1,0,1,1,0,0,0,0,0)
         ViewButtonText(0,1,0,1,0,1,1,0,0,0,0,0)
         ButtonWrite(2,"Up")
         ButtonWrite(4,"Firmshaft")
         ButtonWrite(6,"'Play'")
         ButtonWrite(7,"Down")
         if currentDungeon != 1004:
            this.Choice11.visible = False
         doListen = function():void
            if buttonChoice == 2:
               if currentDungeon == 1004:
                  OutputMainText("\"Maww, fine. Looks like it's just you and me again, Mr. Snuggles.\" The girl returns to her playing, orienting the big minotaur back into her lap with her hand slipping beneath her skirt as you head up to the above floor.",True)
               else:
                  OutputMainText("She continues on with her doll and you take to the stairs.",True)
               DoNext()
               doListen = function():void
                  currentDungeon = 1001
                  DoOldCaveDescent()
            if buttonChoice == 4:
               if currentDungeon == 1004:
                  OutputMainText("\"Maww, fine. Looks like it's just you and me again, Mr. Snuggles.\" The girl returns to her playing, orienting the big minotaur back into her lap with her hand slipping beneath her skirt as you head up the stairs and out of the cave to Firmshaft.",True)
               else:
                  OutputMainText("She continues on with her doll and you take to the stairs.",True)
               DoNext()
               doListen = function():void
                  inDungeon = False
                  RegionChange(2)
                  DoEnd()
            if buttonChoice == 6:
               OutputMainText("\"Ooo, really?! Yay~!\" The girl hops up to her feet, her skirt flipping up a little to flash you her panties. With Mr. Snuggles in hand, the excitement gets the best of her and she bellows out with her fiercer side. \"I'LL TRY NOT TO TEAR YOU TO SHREDS~\"",True)
               DoNext()
               doListen = function():void
                  enemyID = 308
                  currentState = 2
                  EnemyBaseStats()
                  eMaxHP = eHP
                  DoBattle()
            if buttonChoice == 7:
               if currentDungeon == 1004:
                  OutputMainText("\"Maww, fine. Looks like it's just you and me again, Mr. Snuggles.\" The girl returns to her playing, orienting the big minotaur back into her lap with her hand slipping beneath her skirt as you venture down the next set of stairs.",True)
               else:
                  OutputMainText("She continues on with her doll and you take to the stairs.",True)
               DoNext()
               doListen = function():void
                  currentDungeon = 1007
                  DoOldCaveDescent()
   if currentDungeon == 1007 or currentDungeon == 1008 or currentDungeon == 1009:
      if defeatedSuccubus == False:
         OutputMainText("The spiraling stairs just keep going down further and further... You don't know how far down below the surface you've traveled, there's no signs of being any deeper. The rock walls look the same, the steps look the same, even the air isn't as stale as you would expect such a deep cavern to be. Even as you muse over these thoughts, the fact that you have reach yet another room almost eludes you until your feet attempt to continue down non-existant steps and slam into the floor abruptly. You've reached another room, just like the others, except your eyes widen in hope as you see a door on the far wall, no more stairs! Yet, your attention is turned as a sweet feminine voice tantalizes your ears and blocks your exit." + "\n" + "\n" + "\"Well, well. Looks like I've finally got a visitor. So you managed to get past the other two guardians? That's quite the feat. To be honest, that little girl creeps the hell out of me.\"" + "\n" + "\n" + "The figure steps into your view of the door as she shudders at the thought. Her chest wobbles with two grandoise mounds, the things barely held back by an overburdened red leather bikini top. They look even larger when compared to her surprisingly thin waist that widens back out to some very ample hips, the cheeks of her rump jiggling erotically in the matching red leather panties and her long thin tail tipped with a fleshy spade waves behind her to accentuate the movement further. Garters descend down to help hold up her thigh-high high-heeled boots from a belt that lazily hangs around her waist, adorned with glowing vials and a long beatiful whip. To top the whole image off, her milky white skin, long black hair, short little horns, short bat-like wings, and eyes as red as her outfit, all amount to a single idea. A succubus. A creature popular in legends passed down from earlier generations. A creature that, according to the myths, is known for being extremely attractive and for sucking out the essence of men." + "\n" + "\n" + "Sure you've encountered a lot of strange things, but this is something you already knew about and is something that supposedly did NOT exist. However, you don't have time to contemplate such things further as she proceeds to take her whip in hand and lash it against the floor." + "\n" + "\n" + "\"On the other hand, if you were able to beat those two, then you must be quite a treat for me. Don't worry, I won't hurt you... much. I doubt you'll be able to pass, but if you do it would be worth it. I'd probably like to try my hand at you again sometime.\" She gives you a wink before lunging in to fight.",True)
         DoNext()
         doListen = function():void
            enemyID = 309
            currentState = 2
            EnemyBaseStats()
            eMaxHP = eHP
            DoBattle()
      else:
         if currentDungeon == 1007:
            OutputMainText("On the last floor before Sanctuary, the succubus toys around with her vials filled with the masculinity of various victims. She perks up at your presence, something to cut into the boredom. \"Hello again~ Don't worry. Now that you've defeated all of us, you're free to come and go as you please since you've shown you can handle yourself and won't be dead weight, so I won't fight you. Unless you want to go another round~\" She gives you a wink.",True)
         if currentDungeon == 1008:
            OutputMainText("The succubus smiles at you as she leans up against the wall, trying to pretend like you didn't actually hurt her at all and waiting for you to leave so she can rub the achy bits.",True)
         if currentDungeon == 1008:
            OutputMainText("The succubus smiles at you as she leans up against the wall, trying to pretend like you didn't actually best her in the art of sex and waiting for you to leave so she can rub her tingly bits.",True)
         ViewButtonOutline(0,0,0,1,0,0,1,0,0,0,1,1)
         ViewButtonText(0,0,0,1,0,0,1,0,0,0,1,1)
         ButtonWrite(4,"Firmshaft")
         ButtonWrite(7,"Up")
         ButtonWrite(11,"Fight")
         ButtonWrite(12,"Sanctuary")
         if defeatedSuccubus == True:
            this.Choice11Outline.visible = True
         doListen = function():void
            if buttonChoice == 7:
               if currentDungeon == 1007:
                  OutputMainText("\"Alright, enjoy yourself~\" She returns her focus to her vials.",True)
               else:
                  OutputMainText("\"Take care~\" She seems relieved as you leave.",True)
               DoNext()
               doListen = function():void
                  currentDungeon = 1004
                  DoOldCaveDescent()
            if buttonChoice == 4:
               if currentDungeon == 1007:
                  outputMainText("\"Alright, enjoy yourself~\" She returns her focus to her vials while you head up out to Firmshaft.",True)
               else:
                  outputMainText("\"Take care~\" She seems relieved as you leave.",True)
               DoNext()
               doListen = function():void
                  inDungeon = False
                  RegionChange(2)
                  DoEnd()
            if buttonChoice == 11:
               OutputMainText("\"Oh, so you want to have another go at little ole me? Don't mind if I do; I could go for a nice snack~\" Her breasts bounce as she steps to attention, grabbing for her whip in anticipation of some excitement.",True)
               DoNext()
               doListen = function():void
                  enemyID = 309
                  currentState = 2
                  EnemyBaseStats()
                  eMaxHP = eHP
                  DoBattle()
            if buttonChoice == 12)
               if currentDungeon == 1007:
                  OutputMainText("\"Alright, try not to do anything I'd want to do~\" She returns her focus to her vials.",True)
               else:
                  OutputMainText("\"Take care~\" She seems relieved as you leave.",True)
               DoNext()
               doListen = function():void
                  inDungeon = False
                  RegionChange(12)
                  DoEnd()
   if currentDungeon == 1010:
      OutputMainText("The succubus shakes off her defeat and congratulates you. \"Gosh, it's been a while since an outsider has made it through. I suppose you'll be fine then.\" She steps back to the door at the end of the room, grunting slightly as she uses a good deal of force to push it open." + "\n" + "\n" + "Gazing through, you mouth goes agape. After all those stairs, this is faaaar more interesting." + "\n" + "\n" + "A massive cavern stretches out before you, carved and chipped down to provide room for a sizeable city. The door is high up on a wall, giving you a grand view of all the wonder, with wide steps leading down. There's buildings made from all sorts of materials - from wood to stone to mud to things you can't even identify - littering the expansive floor with some stretching up to the high ceiling. All sorts of alien-looking beings walk the streets, faces and races and bodies you never thought imagineable. They peddle their wares, peddle their bodies, play games, play with each other, they... do all sorts of things to entertain their wide variety of cultures. All of this deep, deep underground." + "\n" + "\n" + "\"Welcome to Sanctuary! This place has been down here a very long time and has become a haven for those who survived the Change. Err... you probably don't know what the 'Change' is, since you're the newest generation and haven't witnessed it... Well... nor have I... or has anybody down here.... If we had witnessed it, we wouldn't be here to tell about it.\" She gives a dry chuckle." + "\n" + "\n" + "\"Basically, every several decades, the world just... changes. The terrain... the wildlife... the people... And some of us manage to dodge it somehow, either being caught up in some magical mishap or being in the right place at the right time or whatever. We survive while the rest... disappear. And without anybody else, we venture around and many of us wind up gathering here. Sanctuary seems to be one of the places that remains unaffected by the Change. Some of the people down there have even survived multiple Changes!\"" + "\n" + "\n" + "\"That's why us 'guardians' are up here. We aren't here to guard Sanctuary from 'evildoers' or whatever. We're just here to make sure unwary wanderers from the newest generations don't find their way down here and... get a bit more than they bargained for. Except for those rabbits, but they're a different story that I don't know; they supply us with semen in exchange for something, it's not a matter I pay much attention to.\"" + "\n" + "\n" + "\"Anyways, since you've 'defeated' all of us, you're free to come and go as you please, since you won't be a liability. Other than that, I... can't really explain it much more. I'm just from the last generation, so I don't know everything. This job just lets me get a good amount of essence from stronger travelers, like yourself,\" the succubus snickers as she jiggles her vials, \"and they needed someone a bit more eloquent than the other guardians to explain all I've just said. Sooo... yeah. You can go down there and have fun on your own, I'm not paid to babysit. I'll be here if you ever want to go another round, though.\"" + "\n" + "\n" + "The succubus gives you a wink and gives you a nudge down the steps, allowing you to explore this hidden world on your own.",True)
      inDungeon = False
      RegionChange(12)
      if foundSanctuary == False:
         foundSanctuary = True

def LilaDesc():
   global lilaMilk, lilaVulva, lilaPreg
   if (lilaMilk == 0):
      OutputMainText("\n" + "\n" + "Her small breasts leak only a few drops of milk as she stands there, but her nipples are quite erect and peek through her fur as she blushes at you staring at her.",False)
   elif (lilaMilk <= 2):
      OutputMainText("\n" + "\n" + "Thin trails of white milk travel through her fur from her many erect nipples, slowly dripping onto the floor as she stands there and waits for you, a slight blush crossing her cheeks as the air chills her wet areolas and makes her shiver.",False)
   elif (lilaMilk <= 5):
      OutputMainText("\n" + "\n" + "Her nipples push out from her fur, drops almost continually forming around them and drizzling down her naked body. Shyly, she brings a hand up to squeeze one that's especially stiff and sensitive, making her cheeks red as a squirt of milk launches across the floor of your room.",False)
   elif (lilaMilk <= 8):
      OutputMainText("\n" + "\n" + "Thick streams of white milk dribble down her body, her puffy nipples bulging from their retained milk. Her arms cross over a few of them in embarrassment at how obvious they are, but milk squirts out around them and runs down over her pussy, mixing with the fluids there, and pooling on the floor.",False)
   elif (lilaMilk <= 12):
      OutputMainText("\n" + "\n" + "Though not completely engorged thanks to her 'sharing', her nipples are still quite puffy. A hand reaches up to massage one of the breasts as it feels a bit full to her and it spews several thin spurts in different directions from the slight touch, making her blush furiously.",False)
   elif (lilaMilk <= 18):
      OutputMainText("\n" + "\n" + "Despite having just fed some of her friends, her breasts are still swollen, her nipples puffing out further than ever before. Stiff and long, she can't help but play with them with her fingers, milk spilling profusely down her hand and body, and making her moan before you even get to her. With her eager actions, her face grows red with embarrassment.",False)
   elif (lilaMilk <= 19):
      OutputMainText("\n" + "\n" + "She stands there, short and happy as her breasts squirt thin sprays of milk simply by moving a little. Her hands often pass over them, squeezing her thick stiff nipples and moaning as thick streams gush from them, spilling down her body. Rather used to them by now, she hardly blushes at all, and is quite eager for you to get back to her.",False)
   if (lilaVulva == 0):
      OutputMainText(" Her dainty little vulva also dribbles onto her thighs, her pink lips panting with lubrication in excitement.",False)
   elif (lilaVulva <= 2):
      OutputMainText(" She also twists her hips back and forth while she waits, still trying to figure out how to stand with her thick developed labia filling much the gap between her thighs, making slick webs spread back and forth between them.",False)
   elif (lilaVulva <= 5):
      OutputMainText(" Her nose seems somewhat red from a different kind of blush, a heat filling her face as her thighs tense and relax, squeezing the thick vulva between her legs again and again. You can see her clit peek out from its hood through the cleft, aroused and urging on the slimy coating about her thighs.",False)
   elif (lilaVulva <= 8):
      OutputMainText(" She still holds onto her swollen vulva, with much of the flesh bulging out from between her fingers. Standing with her legs slightly spread so as to not squeeze it, she still manages to cause long strands of thick lubricant to spill from her fingers as she kneads the mass about, afraid to stop or it'll drop from body.",False)
   elif (lilaVulva <= 12):
      OutputMainText(" She also stands with her legs spread, her thighs unable to touch due to the thick lips between them. Each outer labia is as big as her fist, with the inner labia dangling down and nearly red with arousal, drizzling thick strands of clear honey down to the floor without her even touching it. Which she puts a great deal of effort into doing, afraid that she won't stop rubbing the thick clit that sticks out slightly.",False)
   elif (lilaVulva <= 18):
      OutputMainText(" And between her knees hangs her overgrown lips, making her stand slightly bow-legged. Her legs almost constantly twist about, using her knees to squish the flesh again and again since her hands can hardly hold it all if she tried. Her clitoris can hardly be called a button, stroked like a small penis as it pushes out from the massive folds. Her inner lips are so pink with arousal that they seem to be growing longer, due to the the amount of slickness flowing down them that creates the illusion and forms a puddle around her feet.",False)
   elif (lilaVulva <= 19):
      OutputMainText(" And she hardly seems like she's standing at all. With how much her legs bend around and squeeze the large squishy labia that fills the space between them, it seems like she's nearly sitting on her own pussy. However, it barely hovers over the floor, the inner labia dangling down and brushing across it when she presses down slightly to push her clit against the floor to please it a bit. If she curled up and actually wrapped her whole hand around the sensitive thing, there would have still been some more length to cover. Which only makes her original 'wetness' problem worse, the overall size of her genitals causing a flood about her feet and leaving them almost constantly slick and wet with a trail of more following her wherever she goes. However, thanks to her size, when she slips from her moisture she simply lets out an erotic mewl as she falls down onto her soft flesh.",False)
   if (lilaPreg <= 35) and (lilaVulva >= 11):
      OutputMainText(" Her belly seems to be sporting some extra cushioning as well. Not exactly chubby, her excess vaginal flesh from all the growth causes it to protrude, her lower breasts pushing out even more.",False)
   elif (lilaPreg <= 70) and (lilaPreg > 35):
        OutputMainText(" Her hands have a tendancy to cup her growing belly as well, imagining how big she will get. Already protruding quite a bit, her belly button just beginning to stick out, she giggles a little to herself at the thoughts of what's to come.",False)
   elif (lilaPreg <= 100) and (lilaPreg > 70):
      OutputMainText("Yet, despite all of that, her focus mostly remains on her large belly. Nearly as large as herself if she were to curl up, the thing hangs forward to the point where she can't see her messy arousal below. Her hands often roam over the taut fur, taking her naked opportunity to caress it and pleasure in it, cradling it gently.",False)

def Gibberish():
   tempStr = "GIBBERISH ERROR"
   chance = Percent()
   if (chance <= 33):
      tempStr = "¤çÑ-| ÇôG+¦æ| EÆáÜaß pOƒ§· +îdvwqe 5dfÑ¯» º¤äÜ¦) ¼ÿæ¤h ·ƒ."
   if (chance > 33) and (chance <= 66):
      tempStr = "Gs¿ fdfƒæ d§ew ¤-ÿö fs¤£· ÖÅ¢¥¬ ¼«¦ds?"
   if (chance > 66):
      tempStr = "Tas ªÜhf¤ ÄäÑse çåÅû¿ ÑÜñ?Äsd Ü¥¦»¦ƒ ¦ÜÆ+¿æ£ we¤ rgdA-d»¦± Ü+#A¤$¤-ò. Fi?¤çÑK)^¤2 ges nec ¤?+ÿ• ºñ¡as frtr."
   return tempStr

def GibButt():
   tempStr = "GIB BUTTON ERROR"
   chance = Percent()
   if (chance <= 20):
      tempStr = "Pk¿ºs"
   if (chance > 20) and (chance <= 40):
      tempStr = "Ju£¥)"
   if (chance > 40) and (chance <= 60):
      tempStr = "§hdsa"
   if (chance > 60) and (chance <= 80):
        tempStr = "Ö¦¤ÄT¦+"
   if (chance > 80):
      tempStr = "Pancakes"
   return tempStr

!def KnotholeMain():
   global hrs, entering, ment, lust, exhaustion
   ViewButtonOutline(1,0,0,0,0,1,1,0,0,0,0,1)
   ViewButtonText(1,0,0,0,0,1,1,0,0,0,0,1)
   ButtonWrite(1,"Upstairs")
   ButtonWrite(6,"Drum")
   ButtonWrite(7,"Dance")
   ButtonWrite(12,"Leave")
   hrs += 1
   if entering == True:
      OutputMainText("Inside The Knothole, you come across an almost primal sight." + "\n" + "\n",True)
   else:
      OutputMainText("You return to the main floor of the Knothole, looking around to see what else you would like to do." + "\n" + "\n",True)
   OutputMainText("Many Lupans are gathered in the drum-house, beating on sturdy, yet beautifully crafted drums built into the very foundation, the source of the deep, hard thumps that got your heart racing in the first place now pounding at your ears.",False)
   if ment <= 20 and entering == True:
      OutputMainText("The few who look like they are done for the night that you can see look like they've either just ran a marathon, or have just released after being pent up for a month or five. And to you right now, those vacant drums are looking very inviting.",False)
   OutputMainText("To the right, you see more Lupans dancing to the beating rhythm. Pheromones and mixed scents fill the Knothole, making your heart race harder. As you start feeling the blood pump through your veins, almost in sync with the beat of the drums, you find your body bouncing slightly with the rhythm.",False)
   if lust >= 50 and entering == True:
      OutputMainText("As if there was a subtle draft, the scents coming from the dancers start to entice you to join them, the movement of bodies a welcome sight right now. Watching the movement of bodies and tails dancing to the beat, you find your body starting to sway with the flow of the dances, as if the very essence of the drum-house was moving it for you.",False)
      DoLust(10,0)
   OutputMainText("On the left, you spot a wide staircase leading up, and another leading down. A good portion of Lupans are going to the other floors, some holding others on leashes linked to collars wrapped and locked around the necks of the ones being walked. Those on leashes heading up seemed to be more high-spirited than those heading down, which half seemed to be 'zoned out' or in a trance, following their Masters and Mistresses.",False)
   this.doListen = function():void
      if buttonChoice == 1:
         KnotholeUpstairs()
      if buttonChoice == 6:
         OutputMainText("Stepping up to one of the many drums, you feel the beat seeping into your veins. Each thrum of the rhythm resounding through the structure can be felt through the floor. Your fists rise up above your head, not entirely of your will, before swinging down upon the drum. Your fists bounce off the head of the instrument, and both swing down on their own, your rhythm matching that of the one booming throughout the room." + "\n" + "\n" + "You decide to add a few quirks to the beat, your hands dancing and slamming into the drum, adding a bit of a different style lead to the rhythmic percussion. Meeting your ear is the sound of more and more of the others around you start going with your new style, soon, the whole house thrums with the rhythm." + "\n" + "\n" + "After quite a while of beating your heart out almost literally, you slowly bring your drumming to a halt, feeling like you just ran a marathon. Yet, there's also a sensation as having just got out of a soothing, relaxing bath and massage." + "\n" + "\n" + "Feeling no more need to be here, you leave the Knothole and return to Tieden.",True)
         Stats(1,0,-1,0)
         DoLust(-20,0)
         hrs += 2
         DoEnd()
      if buttonChoice == 7:
         if Percent() <= 50:
            OutputMainText("The beat of the drums and movement of the dancers pull you to the crowd, your heartbeat racing hard as your body starts moving." + "\n" + "\n" + "At the edge of the crowd, your " + LegDesc(10) + " hit the floor with the rhythm, your " + LegDesc(2) + " pulsing with each beat of your thumping heart. Your arms bent at your sides, bouncing with your body, the flow of the dancers taking you in, your dance becomes one with the heat and movement of those around you." + "\n" + "\n" + "As the drums start thrumming in a more graceful cadence, the dance of everyone around you, and yourself, takes on a smoother, gliding turn. A long stride, harsh stomp, left twist, right glide double stomp. Your " + LegDesc(10) + " slam the ground with the drumbeat, the floor vibrating as everyone does so as well." + "\n" + "\n" + "A good long time of dancing harshly and calmly leads you to the edge of the group again, the dance eventually driven from your body, leaving you feeling exhausted, yet incredibly invigorated." + "\n" + "\n" + "Finding your time done for now, you leave the Knothole, wiping off the sweat collected on your body.",True)
            DoLust(-15,0)
            exhaustion += 3
         else:
            OutputMainText("The draw of the dancers pulls you to them, your body already starting to move with the enticing way they dance to the beat of the drums." + "\n" + "\n" + "Reaching the edge of the group, your motions start to match theirs, your heartbeat already racing and pulsing throughout your body. Moving with the others around you, you find yourself being drawn further in, surrounded by bodies shifting to the rhythm. You also slowly come to realize that you feel those same bodies softly rubbing and grinding on yours…" + "\n" + "\n" + "Undaunted, you continue dancing, matching the beat of those around you, until you come across a particularly inviting gesture of a fluffy Lupan tail brushing over your face, with the rump connected to said tail grinding against your hips. Another thing you quickly notice: not everyone is fully clothed, but not naked either, and the scent of pheromones comes to your nose." + "\n" + "\n" + "Your new dance partner continues to dance circles around you, almost always keeping contact with your body, be it with their tail, hands, or hips. Your hands and hips return the favor by matching their moves, grinding back into them, along with your rump." + "\n" + "\n" + "Your hands explore their body, finding a bare chest and a skirt over their legs and hips. Both bodies soon dance in sync, theirs pressing back into yours. You could have sworn you could hear them moan, but it's drowned out by the drums, and your hands explore the soft fur regardless. Your right hand moves down and slips under the skirt, finding a soaked pussy between a firm, soft pair of thighs." + "\n" + "\n" + "Your fingers stroke the soft lips, hips swaying back and forth to the rhythm, and the unoccupied hand keeping itself occupied with the soft mounds on her chest. Her hips grind harder into you, laying her head back on you in need. Your fingers stop stroking her cunny’s labia and start to wriggle in. Your tongue slides out of your mouth and licks her exposed neck, and you can hear her whimpers and moans with her mouth next to your ear." + "\n" + "\n" + "In a burst of primal urge out of nowhere, you find yourself bearing your teeth and biting her neck through her fur, causing her to howl as her pussy clamps down over your fingers in ecstasy. Her howl rings out, with other Lupans in the area, a chorus of howls resounding throughout the drum-house. Once her pussy lets go of your fingers and your teeth no longer hold her neck, she slips away into the crowd, dancing with renewed energy." + "\n" + "\n" + "Before you know it, you're back outside of the dancing group, with a pair of soaked fingers, and feeling exhausted from the dancing and surprisingly refreshed even though you know you haven't actually 'released'." + "\n" + "\n" + "With nothing more to do save smell the woman's scent on your fingers, you leave the Knothole.",True)
            DoLust(-200,0)
            exhaustion += 4
            Stats(0,0,1,0)
         hrs += 2
         doEnd()
      if buttonChoice == 12:
         KnotholeLeave()

!def KnotholeLeave():
   OutputMainText("Finished with your time in the Knothole, you return to the fresh air of Tieden.",True)
   DoEnd()
!def KnotholeUpstairs():
   global breastSize, hips, body, lib, hrs
   ViewButtonOutline(1,0,1,0,0,0,0,0,1,0,0,1)
   ViewButtonText(1,0,1,0,0,0,0,0,1,0,0,1)
   ButtonWrite(1,"Relax")
   ButtonWrite(3,"Exhibition")
   ButtonWrite(9,"Downstairs")
   ButtonWrite(12,"Leave")
   OutputMainText("The staircase going up is wide, accommodating as many as five people side by side. With enough space, you make it up without bumping into anyone, though you're sure you felt some eyes on your rear as you climbed the stairs. Looking back, you don’t see anyone staring at you but you still sense eyes admiring your " + BodyDesc() + " figure." + "\n" + "\n" + "Dismissing the odd paranoia, you look around the area, deciding to get accustomed to the environment. The room looks like it covers the whole area above the first floor. Pillars here and there support the roof, standing above pillars and supporting walls you saw below, though these ones have four iron rings midway up their height. Many of these rings sport Lupans, both male and female, chained to the pillars, mostly nude or wearing exotic clothing, and exposing themselves in erotic displays, looking like they are enjoying themselves in front of their audience." + "\n" + "\n" + "A large area of the room is taken up by rigs. X-crosses, suspension rigs, stockades, padded sawhorses, and cushioning on the walls with more iron rings and padded metal restraints. Aside the pillars and walls with the rings, there are several wooden posts standing in various spots around the room, half of those also linked to what looks to be more personal 'displays' of Lupans acting as pets." + "\n" + "\n" + "In the area filled with rigs, there stands a small gathering as submissive Lupans toy, tease, get teased, beg, seduce, and outright presenting themselves for their audience. The apparent Dominants either stand or seat themselves on lavish sofas and chairs; a group of voyeurs enjoying the exhibitions.",True)
   this.doListen = function():void
      if buttonChoice == 1:
         if breastSize > 2 and hips > 2 and body < 20:
            OutputMainText("Feeling the need to relax, you find an empty seat in the corner of the room that looks like you would be alone." + "\n" + "\n" + "The moment you take a seat on the soft comfortable cushions, a dark gray collared Lupan takes notice of you and makes their way over to you. Slowly approaching you (and crawling on all fours), you notice that they are male, and he is avoiding eye contact with you, focusing more on your " + LegDesc(10) + " and " + LegDesc(2) + "." + "\n" + "\n" + "Reaching your corner of the room, the collared male kneels at your " + LegDesc(10) + ", keeping his eyes low and bows his head. “Would you like me to dance for you?” he asks almost indirectly, his voice sounding timid." + "\n" + "\n" + "You consider for a moment, looking over the dark fur of the male's slender, nude frame before you.",True)
         else:
            OutputMainText("Feeling the need to relax, you find an empty seat in the corner of the room that looks like you would be alone." + "\n" + "\n" + "The moment you take a seat on the soft, comfortable cushions, a collared Lupan takes notice of you and makes their way over to you. Getting closer to you (and crawling on all fours), you notice that they are female, and she avoids eye contact despite you almost getting lost in her beautiful deep emerald green eyes." + "\n" + "\n" + "Reaching your corner of the room, she kneels before you, pressing her bare chest out to display her ample breasts, showing her Lupan qualities to you. Her legs spread to expose her snatch between her legs, her hands on her legs with palms up. “Would you like me to dance for you?” she asks, still avoiding eye contact and keeping her head down, her tone of voice very timid." + "\n" + "\n" + "You consider for a moment, looking over the dark fur of the female's slender, nude frame before you.",True)
         ButtonConfirm()
         doListen = function():void
            if buttonChoice == 6:
               if breastSize > 2 and hips > 2 and body < 20:
                  outputMainText("The male Lupan with a collar before you nods and slowly comes to a stand, keeping his head down. With the stand, you have full view of his endowment, an already fully erect deep-red canine cock, with knot and all at attention out of his sheath." + "\n" + "\n" + "The beat of the drums below rumbles softly through the floor, being felt through your " + LegDesc(10) + ". Tapping a toe to the rhythm, the slender Lupan male before you counts himself down, then starts with a spin, and slide, giving you a very nice view of his furred ass." + "\n" + "\n" + "The dance quickly turns erotic, his hands sliding over his body as his torso weaves in concert, putting on a rather arousing display for his audience. His tail sways with his motions, in rhythm to the drumbeat." + "\n" + "\n" + "The collar he wears has a slight jingle of an oval, golden tag bearing his name. With how he moves, you don't get a good view of it, but you don't believe he is available for an owner anyway. Instead, you enjoy his display, watching the slender figure move and twist, showing off his supple ass and throbbing knotted canine shaft." + "\n" + "\n" + "After a couple hours of watching him dance almost nonstop to the ever-changing rhythm of the drum-house below, he is called by a female Lupan wearing a deep red corset and short skirt holding a couple of leashes. This woman you assume to be his owner and you watch as he obediently heeds her call, bowing to you before crawling back to her on all fours and letting her hook a leash to his collar." + "\n" + "\n" + "Seeing as you became rather aroused by his performance, you decide to leave the Knothole for now, leaving the male Lupan to his Mistress.",True)
                  DoLust(math.floor(lib / 4),0)
               else:
                  OutputMainText("The female Lupan with a collar before you nods and slowly comes to a stand, keeping her head down. With the stand, you have a wondrous view of her supple bosom and damp pussy." + "\n" + "\n" + "The beat of the drums below rumbles softly through the floor, being felt through your " + LegDesc(10) + ". Tapping a toe to the rhythm, the slender Lupan female before you counts herself down, then starts with a spin, and slide, giving you a very nice view of her soft and firm furred ass." + "\n" + "\n" + "The dance quickly turns erotic, her hands sliding over her breasts and slender belly as her torso weaves in concert, putting on a rather arousing display for her audience. Her fluffy tail sways with her motions, in rhythm to the drumbeat." + "\n" + "\n" + "The collar she wears has a slight jingle of an oval, golden tag bearing her name. With how she moves, you don't get a good view of it, but you don't believe she is available for an owner anyway. Instead, you enjoy her erotic display, watching the slender figure move and twist, showing off her firm slim ass and damp cunny." + "\n" + "\n" + "After a couple hours of watching her dance almost nonstop to the ever-changing rhythm of the drum-house below, she is called by another female Lupan wearing a deep red corset and short skirt holding a couple of leashes. This woman you assume to be her owner and you watch as she obediently heeds her call, bowing to you before crawling back to her on all fours and letting her hook a leash to her collar." + "\n" + "\n" + "Seeing as you became rather aroused by her performance, you decide to leave the Knothole for now, leaving the female Lupan to her Mistress.",True)
                  DoLust(math.floor(lib / 4),0)
               hrs += 3
               DoEnd()
            else:
               OutputMainText("Dismissing the submissive Lupan before you, you lay your head back and relax, listening to the dulled beat of the drum-house below and the mixed sounds of pleasure, conversation, and ecstasy around the large room." + "\n" + "\n" + "Sometime later, you don't know how long, you take a heavy yawn and stretch, having your rest filled with wet dreams and imaginings of the events around you. Seeing not much else to do, you take your leave of the Knothole.",True)
               hrs += 1
               DoLust(10,0)
               DoEnd()
      if buttonChoice == 3:
         OutputMainText("Feeling like showing off, you walk to an open area of the room, swaying your hips a bit." + "\n" + "\n" + "Almost right away, you notice you've already caught someone's eye, relaxing on a bench. A smirk crosses your lips as your motions, now directed in their general direction, make your body sway and twist." + "\n" + "\n" + "While turned away from your observer, you slowly strip off your " + CurrentClothes() + ", letting the outfit drop to the floor. The patron you are entertaining, now standing and a bit closer to watch, a Lupan male, nude, with a full erection and deep-red throbbing knot, raises his brow to your naked backside, intrigued by what he sees." + "\n" + "\n" + "Without breaking stride, feeling the beat of the drum-house through the floor, and your " + LegDesc(10) + ", you swirl your hips and twirl, giving him a round-view of your naked body. This gets both his brows raised, and leaving him licking his lips as he watches." + "\n" + "\n" + "Your now-exposed rump has his attention now, his eyes following it whenever you spin and twist as you dance before him. Having a bit more fun, you inch closer to the Lupan, teasing with your ass as you wiggle it, only to pull it away.",True)
         DoNext()
         doListen = function():void
            if gender == 2:
               OutputMainText("Bending over and leaning up against a pillar, your hand slides down your body to your lower lips. You wiggle your ass teasingly and spread your pussy lips wide, giving him a nice view of your nethers. With his almost-full attention (almost because he is now stroking his throbbing, pre-leaking canine dick while watching), you wriggle a finger into your lips with a moan, starting to please yourself in front of the Lupan male." + "\n" + "\n" + "One finger not enough, you push in another, pulling out a loud moan as you finger yourself, getting lost in the pleasure." + "\n" + "\n" + "Wet, moaning, and so lost in yourself, you don't notice the male now behind you. He grabs your hips, making you gasp in surprise, your fingers pulling out of your soaking wet cunn" + Plural(16) + ". The next thing you feel, is a thick, canine shaft thrusting into " + OneYour(2) + " puss" + Plural(16) + ", a very loud moan of mixed surprise and pleasure escaping you as you feel the throbbing rod slide in all the way to its knot, the inflation pressing up against your quivering lips." + "\n" + "\n" + "The manhood thrust into you gets pulled, almost leaving your body before thrusting back in, and out, and in, getting into a pace. You brace yourself against the pillar, not fighting against his assertion." + "\n" + "\n" + "Feeling his girth fill your cunny drives you up towards your climax, not quite reaching it. Feeling him grip your waist and breathe against your neck, you bite your lip to stifle a loud moan. His thrusts get harder, and harder, then -POP- your cunny stretches hard as his knot finally enters your body. You try to stifle a scream of ecstasy, but your own climax, and feeling him bite down on your neck, it is let loose for all to hear." + "\n" + "\n" + "The following moments slowly dim into darkness as you faint, your pussy feeling nice and full, of both his knotted cock, and his thick, warm cream.",True)
            if gender == 1:
               OutputMainText("Bending over and leaning up against a pillar, your hand slides down your body to your stiffened shaft. You wiggle your ass teasingly and spread your legs wide, giving him a nice view of your tailhole. With his almost-full attention (almost because he is now stroking his throbbing, pre-leaking canine dick while watching), you start to tease your cock, lightly stroking it with a few fingers, starting to please yourself in front of the Lupan male." + "\n" + "\n" + "The teasing not enough, you grip your rod tighter, stroking faster, pulling out a loud moan as you finger yourself, getting lost in the pleasure." + "\n" + "\n" + "Hard, moaning, and so lost in yourself, you don't notice the male now behind you. The next thing you feel, is a thick, canine shaft thrusting into your ass, a very loud moan of mixed surprise and pleasure escaping you as you feel the throbbing rod slide in all the way to its knot, the inflation pressing up against your tight hole." + "\n" + "\n" + "The manhood thrust into you gets pulled, almost leaving your body before thrusting back in, and out, and in, getting into a pace. You brace yourself against the pillar, not fighting against his assertion." + "\n" + "\n" + "Feeling his girth fill your ass drives you up towards your climax, not quite reaching it. Feeling him grip your waist, and breathe against your neck, you bite your lip to stifle a loud moan. His thrusts get harder, and harder, then -POP- your tailhole stretches hard as his knot finally enters your body. You try to stifle a scream of ecstasy, but your own climax, and feeling him bite down on your neck, it is let loose for all to hear." + "\n" + "\n" + "The following moments slowly dim into darkness as you faint, your rump feeling nice and full, of both his knotted cock, and his thick, warm cream.",True)
            if gender == 3:
               outputMainText("Bending over and leaning up against a pillar, your hand slides down your body to your lower lips. You wiggle your ass teasingly and spread pussy lips wide and pressing " + OneYour(1) + " shaft" + Plural(1) + " down " + LegWhere(1) + " your " + LegDesc(2) + ", giving him a nice view of your nethers. With his almost-full attention (almost because he is now stroking his throbbing, pre-leaking canine dick while watching), you wriggle a finger into your lips with a moan, your other hand stroking and playing with your throbbing cock, starting to please yourself in front of the Lupan male." + "\n" + "\n" + "One finger not enough, you push in another, pulling out a loud moan as you finger yourself, getting lost in the pleasure, stroking your shaft harder and faster." + "\n" + "\n" + "Wet, moaning, and so lost in yourself, you don't notice the male now behind you. He grabs your hips, making you gasp in surprise, your fingers pulling out of your soaking wet cunt" + Plural(16) + ". The next thing you feel, is a thick, canine shaft thrusting into " + OneYour(2) + " puss" + Plural(16) + ", a very loud moan of mixed surprise and pleasure escaping you as you feel the throbbing rod slide in all the way to its knot, the inflation pressing up against your quivering lips." + "\n" + "\n" + "The manhood thrust into you gets pulled, almost leaving your body before thrusting back in, and out, and in, getting into a pace. You brace yourself against the pillar, not fighting against his assertion." + "\n" + "\n" + "Feeling his girth fill your cunny drives you up towards your climax, not quite reaching it. Feeling him grip your waist, and breathe against your neck, you bite your lip to stifle a loud moan. His thrusts get harder, and harder, then -POP- your cunny stretches hard as his knot finally enters your body. You try to stifle a scream of ecstasy, but your own climax, your cock spraying your load all over the ground and pillar in front of you, and feeling him bite down on your neck, it is let loose for all to hear." + "\n" + "\n" + "The following moments slowly dim into darkness as you faint, your pussy feeling nice and full, of both his knotted cock, and his thick, warm cream.",True)
            DoNext()
            doListen = function():void
               OutputMainText("A couple hours later, you wake up and find yourself laying on a bench, clothes stacked next to you, and feeling very relieved from the experience." + "\n" + "\n" + "Gathering your clothes, and trying to stand, you wobble a bit, still feeling the fuck you had not long ago, your ",True)
               if vagTotal > 0:
                  OutputMainText("pussy",False)
                  DoImpregnate(3)
               else:
                  OutputMainText("ass",False)
               OutputMainText(" dripping a bit from the cum still filling it as you -slowly- take your leave of the knothole.",False)
               DoLust(-math.floor(sen / 2),2,2,5)
               hrs += 2
               DoEnd()
      if buttonChoice == 9:
         KnotholeMain(False)
      if buttonChoice == 12:
         KnotholeLeave()

!def DoBattle():
   global lust, buttonChoice, inDungeon, currentZone, currentState, hrs, gender, eGen, _str_, rapeMod, eStr, eLust, ePref, enemyID, eSen, eMenta
   BC()
   ViewButtonOutline(1,1,0,0,1,0,1,0,1,1,0,1)
   ViewButtonText(1,1,0,0,1,0,1,0,1,1,0,1)
   ButtonWrite(1,"Bag")
   ButtonWrite(2,"Run")
   ButtonWrite(5,"Attack")
   ButtonWrite(7,"Special")
   ButtonWrite(9,"Rape")
   ButtonWrite(10,"Entice")
   ButtonWrite(12,"Submit")
   if lust < 15:
      this.Choice12.visible = False
   this.doListen = function():void
      dmg = 0
      eLustChange = 0
      if buttonChoice == 1:
         doBag()
      if buttonChoice == 2:
         if Percent() <= 20 + runMod:
            OutputMainText("You successfully run away!",True)
            if inDungeon == True:
               RegionChange(currentZone)
               inDungeon = False
               OutputMainText("\n" + "\n" + "To escape, you run all the way back to " + regionName(currentZone) + ".",False)
            currentState = 1
            hrs = 1
            doEnd()
         else:
            OutputMainText("You fail to run away...",True)
            if currentState == 2:
               EnemyAttack()
            if currentState == 2:
               doBattle()
      if buttonChoice == 5:
         WeaponAttack()
         if currentState == 2:
            enemyAttack()
         if currentState == 2:
            doBattle()
      if buttonChoice == 7:
         DoSpecialAbility(1)
      if buttonChoice == 9:
         if gender == 0 or eGen == 0:
            OutputMainText("What are you going to rape it with? Good intentions?" + "\n" + "\n" + "Choose another option.",True)
            if currentState == 2:
               doBattle()
         else:
            OutputMainText("You attempt to toss the " + EnemyName() + " to the ground and fuck it wildly!",True)
            if lust < 15:
               OutputMainText("\n" + "\n" + "However, you aren't nearly aroused enough to even think about penetration, leaving your efforts futile.",False)
               if currentState == 2:
                  eEemyAttack()
            elif (Percent() / 5 + _str_ + rapeMod) <= (Percent() / 5 + eStr - eLust / 2):
               OutputMainText("\n" + "\n" + "However, the " + EnemyName() + " overpowers you and tosses you off!",False)
               if currentState == 2:
                  EnemyAttack()
            elif (ePref != gender and ePref != 4 and gender != 3 or ePref == 0):
               dmg = math.floor(Percent() / 10 + lust / 10)
               OutputMainText("\n" + "\n" + "However, the " + EnemyName() + " is sorely turned off by your rough pounding on its sensitive area, merely hurting its genitals and its pride." + "\n" + "\n" + "But you do deal " + dmg + " damage and satisfy yourself a bit.",False)
               DoeHP(-dmg)
               if enemyID < 300:
                  DoLust(-math.floor(Percent() / 20 + sen / 10),2,1,2)
               else:
                  DoLust(-math.floor(Percent() / 20 + sen / 10),2,1,2)
            else:
               DoRape()
               eLustChange = math.floor(Percent() / 10 + eSen / 5)
               if (eLust - eLustChange) <= 0:
                  eLust = 0
               if (eMenta - eLustChange) < 0:
                  SpecialRapeWin()
                  OutputMainText("\n" + "\n" + "You win!",False);
                  currentState = 1
                  DoNext()
                  doListen = function():void
                     battleWin()
               else:
                  OutputMainText("\n" + "\n" + "The " + EnemyName() + " picks itself up after you had your way with it, a little distraught but not yet defeated.",False)
                  eLust -= eLustChange
               eMenta -= eLustChange
            if currentState == 2:
               doBattle()
      if buttonChoice == 10:
         DoEntice()
         if currentState == 2:
            EnemyAttack()
         if currentState == 2:
            DoBattle()
      if buttonChoice == 12:
         OutputMainText("No longer wishing to fight, you attempt to submit yourself to the " + EnemyName() + "'s whims in hopes of leaving the battle with a little fun.",True)
         if (ePref == 0) or (ePref == 1 and gender == 2) or (ePref == 2 and gender == 1) or (gender == 0):
            OutputMainText("\n" + "\n" + "However, it is quickly apparent that the enemy has no interest in you, in that fashion.",False)
            if currentState == 2:
               EnemyAttack()
         elif eLust < eMenta:
            OutputMainText("\n" + "\n" + "However, the " + EnemyName() + " isn't nearly aroused enough, a bit too cautious at the moment to assault you in such a way.",False)
            if currentState == 2:
               enemyAttack()
         else:
            currentState = 1
            DoNext()
            doListen = function():void
               doGetRaped()
         if currentState == 2:
            doBattle()

def WeaponAttack():
   global weapon, _str_, eSen, ment
   dmg = 0
   if (weapon == 10):
      dmg = math.floor(random.random() * (1 + 10 - 1)) + 1 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You punch the " + EnemyName() + " with your fists, dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 116):
      dmg = math.floor(random.random() * (1 + 12 - 5)) + 5 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You lunge at the " + EnemyName() + " and stab it with your dagger, dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 117):
      dmg = math.floor(random.random() * (1 + 20 - 2)) + 2 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You swing your hammer at the " + EnemyName() + ", dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 118):
      dmg = math.floor(random.random() * (1 + 25 - 10)) + 10 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You slash at the " + EnemyName() + " with your saber, dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 119):
      dmg = math.floor(random.random() * (1 + 18 - 12)) + 12 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You lash at the " + EnemyName() + " with your whip, dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 127):
      dmg = math.floor(random.random() * (1 + 20 - 10)) + 10 + math.floor(_str_ / 2 - (100 - eSen) / 20)
      OutputMainText("You whip around your tail and smack the " + EnemyName() + " with the spike at the end, dealing " + dmg + " damage!",True)
      DoeHP(-dmg)
   if (weapon == 235):
      dmg = math.floor(random.random() * (1 + 5 - 1)) + 1 + math.ceil(ment / 10)
      if (ment < 30):
         OutputMainText("You awkwardly stuff the wide-rimmed head of the rod into your mouth, sucking as hard as you can even though you only manage drain " + dmg + " HP from the " + EnemyName() + ".",True)
      elif (ment < 70):
         OutputMainText("You gently lick around the wide-rimmed head of the rod before sliding it into your mouth and gently sucking from the tip, draining a whole " + dmg + " HP from the " + EnemyName() + ".",True)
      else:
         OutputMainText("You lick up the shaft of the rod before swirling your tongue around the wide-rimmed head, coaxing it into your mouth as you continue to drag your tastebuds over and around it while pumping it in and out gently, draining " + dmg + " HP from the " + EnemyName() + "!",True)
      DoeHP(-dmg)
      DoHP(dmg)

!def DoSpecialAbility(more:int):
   var specialAbilityArray:Array = null
   this.viewButtonOutline(0,0,0,0,0,0,0,0,0,0,0,1)
   this.viewButtonText(0,0,0,0,0,0,0,0,0,0,0,1)
   this.choicePage = more
   this.showPage(True,"Spc Abilities")
   this.buttonWrite(4,"&#60;&#60;")
   this.buttonWrite(8,">>")
   this.buttonWrite(12,"Return")
   specialAbilityArray = []
   if (skunkAffinity >= 40):
      specialAbilityArray.push(1)
   if (len(specialAbilityArray) < 1):
      OutputMainText("Your do not currently have any special abilities that you can use.",True)
   else:
      OutputMainText("Which special ability would you like to use?",True)
   if (len(specialAbilityArray) > 9):
      this.Choice4Outline.visible = True
      this.Choice4.visible = True
      this.Choice8Outline.visible = True
      this.Choice8.visible = True
   if (specialAbilityArray[0 + (more * 9 - 9)]):
      this.buttonWrite(1,this.specialAbilityName(specialAbilityArray[0 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[0 + (more * 9 - 9)])
      this.Choice1Outline.visible = True
      this.Choice1.visible = True
   if (specialAbilityArray[1 + (more * 9 - 9)]):
      this.buttonWrite(2,this.specialAbilityName(specialAbilityArray[1 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[1 + (more * 9 - 9)])
      this.Choice2Outline.visible = True
      this.Choice2.visible = True
   if (specialAbilityArray[2 + (more * 9 - 9)]):
      this.buttonWrite(3,this.specialAbilityName(specialAbilityArray[2 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[2 + (more * 9 - 9)])
      this.Choice3Outline.visible = True
      this.Choice3.visible = True
   if (specialAbilityArray[3 + (more * 9 - 9)]):
      this.buttonWrite(5,this.specialAbilityName(specialAbilityArray[3 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[3 + (more * 9 - 9)])
      this.Choice5Outline.visible = True
      this.Choice5.visible = True
   if (specialAbilityArray[4 + (more * 9 - 9)]):
      this.buttonWrite(6,this.specialAbilityName(specialAbilityArray[4 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[4 + (more * 9 - 9)])
      this.Choice6Outline.visible = True
      this.Choice6.visible = True
   if (specialAbilityArray[5 + (more * 9 - 9)]):
      this.buttonWrite(7,this.specialAbilityName(specialAbilityArray[5 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[5 + (more * 9 - 9)])
      this.Choice7Outline.visible = True
      this.Choice7.visible = True
   if (specialAbilityArray[6 + (more * 9 - 9)]):
      this.buttonWrite(9,this.specialAbilityName(specialAbilityArray[6 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[6 + (more * 9 - 9)])
      this.Choice9Outline.visible = True
      this.Choice9.visible = True
   if (specialAbilityArray[7 + (more * 9 - 9)]):
      this.buttonWrite(10,this.specialAbilityName(specialAbilityArray[7 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[7 + (more * 9 - 9)])
      this.Choice10Outline.visible = True
      this.Choice10.visible = True
   if (specialAbilityArray[8 + (more * 9 - 9)]):
      this.buttonWrite(11,this.specialAbilityName(specialAbilityArray[8 + (more * 9 - 9)]))
      SpecialAbilityDescription(specialAbilityArray[8 + (more * 9 - 9)])
      this.Choice11Outline.visible = True
      this.Choice11.visible = True
   this.doListen = function():void
      if (buttonChoice == 1):
         SpecialAbilityUse(specialAbilityArray[0 + (more * 9 - 9)])
      if (buttonChoice == 2):
         SpecialAbilityUse(specialAbilityArray[1 + (more * 9 - 9)])
      if (buttonChoice == 3):
         SpecialAbilityUse(specialAbilityArray[2 + (more * 9 - 9)])
      if (buttonChoice == 5):
         SpecialAbilityUse(specialAbilityArray[3 + (more * 9 - 9)])
      if (buttonChoice == 6):
         SpecialAbilityUse(specialAbilityArray[4 + (more * 9 - 9)])
      if (buttonChoice == 7):
         SpecialAbilityUse(specialAbilityArray[5 + (more * 9 - 9)])
      if (buttonChoice == 9):
         SpecialAbilityUse(specialAbilityArray[6 + (more * 9 - 9)])
      if (buttonChoice == 10):
         SpecialAbilityUse(specialAbilityArray[7 + (more * 9 - 9)])
      if (buttonChoice == 11):
         SpecialAbilityUse(specialAbilityArray[8 + (more * 9 - 9)]);
      if (buttonChoice == 4):
         if (len(specialAbilityArray) / 9 < more):
            DoSpecialAbility(1)
         else:
            DoSpecialAbility(more + 1)
      if (buttonChoice == 8):
         if (more == 1):
            DoSpecialAbility(math.floor(len(specialAbilityArray) / 9))
         else:
            DoSpecialAbility(more - 1)
      if (buttonChoice == 12):
         ShowPage(False,"")
         DoReturn()

def SpecialAbilityName(ID:int):
   tempStr = "SPECIAL ABILITY NAME ERROR " + ID + ""
   if (ID == 1):
      tempStr = "Skunk Spray;
   return tempStr

def SpecialAbilityDescription(ID:int):
   tempStr = "SPECIAL ABILITY DESC ERROR " + ID + ""
   if (ID == 1):
      tempStr = "\n" + "\n" + "Skunk Spray - Using your scent glands in your rump, you can unleash this terrible stench upon your enemy, causing damage and potentially making them miss their next turn."
   return tempStr

def SpecialAbilityUse(ID:int):
   global currentState
   dmg = 0
   if (ID == 1):
      dmg = math.floor(10 + Percent() / 10)
      OutputMainText("\n" + "\n" + "You turn around and aim your " + ButtDesc() + " butt at the " + EnemyName() + " and spray out a foul odor. The " + EnemyName() + " snorts and shakes, taking " + dmg + " damage.",False)
      DoeHP(-dmg)
      if (Percent() < 35) and (currentState == 2):
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " flinches so badly from the stench that it misses its chance to counter.",False)
      elif (currentState == 2):
         EnemyAttack()
   if (currentState == 2):
      DoBattle()

def DoEntice():
   global eGen, gender, ePref, tail, eLib, enticeMod, lust, nippleSize
   chance = Percent()
   if (eGen == 1) and (gender == 1) and (ePref != 2) and (ePref != 0):
      if (chance <= 50):
         OutputMainText("You turn around and bend over before the " + EnemyName() + " stroking the " + CockDesc() + " bulge in your " + ClothesBottom() + " and patting your " + ButtDesc() + " rump while you wave your " + HipDesc() + " hips",True)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail dancing above",False)
         OutputMainText(" tantalizingly.",False)
      if (chance > 50):
         OutputMainText("You flex your muscles, trying to show off your masculinity, while you thrust your " + HipDesc() + " hips in an attempt to show off your " + CockDesc() + " bulge.",True)
      if (ePref == 1 or ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5) + (enticeMod / 2)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10) + (enticeMod / 2)))
   elif (eGen == 1) and (gender == 2) and (ePref != 1) and (ePref != 0):
      if (chance <= 50):
         OutputMainText("You turn around and bend over before the " + EnemyName() + ", stroking your " + VulvaDesc() + " vulva through your " + ClothesBottom(),True)
         if (lust > 20) and (MoistCalc(2) > 3):
            OutputMainText(" until your feminine arousal seeps through",False)
         OutputMainText(". Your " + HipDesc() + " hips wiggle erotically",False)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail dancing above",False)
         OutputMainText(".",False)
      if (chance > 50):
         OutputMainText("You lick your finger before sliding it into your mouth, sucking and pulling it out slowly with a small drop of saliva dangling upon your supple lips while you rub a " + NipDesc() + "nipple through your " + ClothesTop() + " with your other hand.",True)
      if (ePref == 2) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5) + (enticeMod / 2)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10) + (enticeMod / 2)))
   elif (eGen == 2) and (gender == 1) and (ePref != 2) and (ePref != 0):
      if (chance <= 50):
         OutputMainText("You pull " + PullUD(2) + " your " + ClothesBottom() + " a little, revealing the base of your cock-flesh",True)
         if (lust > 20):
            OutputMainText(", the " + CockDesc() + " erection pulsing strongly beneath your " + ClothesBottom(),False)
         OutputMainText(", rubbing it to show off what you can offer",False)
         if (MoistCalc(1) > 3):
            OutputMainText(", a blotch of pre beginning to seep across the fabric",False)
         OutputMainText(".",False)
      if (chance > 50):
         OutputMainText("You flex your muscles as you groan with sexual desire, trying to turn you opponent on with the possibilities of what might come.",True)
      if (ePref == 1) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5) + (enticeMod / 2)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10) + (enticeMod / 2)))
   elif (eGen == 2) and (gender == 2) and (ePref != 1) and (ePref != 0):
      if (chance <= 50):
         OutputMainText("You spread your " + LegDesc(6) + ", crouching down as both hands grind into your " + VulvaDesc() + " pussy",True)
         if (lust > 20) and (MoistCalc(2) > 3):
            OutputMainText(", your honey spreading from the crotch of your " + ClothesBottom() + ",",False)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail swishing across the ground,",False)
         OutputMainText(" luring the " + EnemyName() + " to come grind instead.",False)
      if (chance > 50):
         OutputMainText("Your arms hug beneath your " + BoobDesc() + " chest, squeezing the mounds and making them look even bigger",True)
         if (lust > 20) and ((nippleSize > 1) or (nippleSize > 6)):
            OutputMainText(", your " + NipDesc() + "nipples clearly visible through your " + ClothesTop(),False)
         OutputMainText(".",False)
      if (ePref == 2) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5) + (enticeMod / 2)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10) + (enticeMod / 2)))
   elif (eGen == 3) and (gender == 1) and (ePref != 2) and (ePref != 0):
      if (chance <= 25):
         OutputMainText("You turn around and bend over before the " + EnemyName() + " stroking the " + CockDesc() + " bulge in your " + ClothesBottom() + " and patting your " + ButtDesc() + " rump while you wave your " + HipDesc() + " hips",True)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail dancing above",False)
         OutputMainText(" tantalizingly.",False)
      if (chance > 25) and (chance <= 50):
         OutputMainText("You flex your muscles, trying to show off your masculinity, while you thrust your " + HipDesc() + " hips in an attempt to show off your " + CockDesc() + " bulge.",True)
      if (chance > 50) and (chance <= 75):
         OutputMainText("You pull " + PullUD(2) + " your " + ClothesBottom() + " a little, revealing the base of your cock-flesh",True)
         if (lust > 20):
            OutputMainText(", the " + CockDesc() + " erection pulsing strongly beneath your " + ClothesBottom(),False)
         OutputMainText(", rubbing it to show off what you can offer",False)
         if (MoistCalc(1) > 3):
            OutputMainText(", a blotch of pre begining to seep across the fabric",False)
         OutputMainText(".",False)
      if (chance > 75):
         OutputMainText("You flex your muscles as you groan with sexual desire, trying to turn you opponent on with the possibilities of what might come.",True)
      if (ePref == 1) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5) + (enticeMod / 2)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10) + (enticeMod / 2)))
   elif (eGen == 3) and (gender == 2) and (ePref != 1) and (ePref != 0):
      if (chance <= 25):
         OutputMainText("You spread your " + LegDesc(6) + ", crouching down as both hands grinding into your " + VulvaDesc() + " pussy",True)
         if (lust > 20) and (MoistCalc(2) > 3):
            OutputMainText(", your honey spreading from the crotch of your " + ClothesBottom() + ",",False)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail swishing across the ground,",False)
         OutputMainText(" luring the " + EnemyName() + " to come grind instead.",False)
      if (chance > 25) and (chance <= 50):
         OutputMainText("Your arms hug beneath your " + BoobDesc() + " chest, squeezing the mounds and making them look even bigger",True)
         if (lust > 20) and ((nippleSize > 1) or (nippleSize > 6)):
            OutputMainText(", your " + NipDesc() + "nipples clearly visible through your " + ClothesTop() + ".",False)
         OutputMainText(".",False)
      if (chance > 50) and (chance <= 75):
         OutputMainText("You turn around and bend over before the " + EnemyName() + ", stroking your " + VulvaDesc() + " vulva through your " + ClothesBottom(),True)
         if (lust > 20) and (MoistCalc(2) > 3):
            OutputMainText(" until your feminine arousal seeps through",False)
         OutputMainText(". Your " + HipDesc() + " hips waggle erotically",False)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail dancing above",False)
         OutputMainText(".",False)
      if (chance > 75):
         OutputMainText("You lick your finger before sliding it into your mouth, sucking and pulling it out slowly with a small drop of saliva dangling upon your supple lips while you rub a " + NipDesc() + "nipple through your " + ClothesTop() + " with your other hand.",True)
      if (ePref == 2) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5)))
      elif (ePref == 3):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10)))
   elif (gender == 3) and (ePref != 0) and (eGen != 0):
      if (chance <= 25):
         OutputMainText("You turn around and bend over before the " + EnemyName() + ", patting your " + ButtDesc() + " ass and " + VulvaDesc() + " pussy. You waggle your " + HipDesc() + " hips, the " + CockDesc() + " bulge in your " + ClothesBottom() + " swaying",True)
         if (tail != 0):
            OutputMainText(", your " + TailDesc() + " tail dancing above",False)
         OutputMainText(" deliciously.",False)
      if (chance > 25) and (chance <= 50):
         OutputMainText("Your arms hug beneath your " + BoobDesc() + " chest, squeezing the mounds and making them look even bigger while you flex, thrusting at the air with your " + CockDesc() + " package bobbing.",True)
      if (chance > 50) and (chance <= 75):
         OutputMainText("You pull " + PullUD(2) + " your " + ClothesBottom() + " a little, revealing the base of your male anatomy while you spread your " + LegDesc(6) + ", crouching down as both hands grind across the bulge and into your female portions",True)
         if (lust > 20) and ((MoistCalc(2) > 3) or (MoistCalc(1) > 3)):
            OutputMainText(", the fabric quickly growing damp",False)
         OutputMainText(".",False)
         if (tail != 0):
            OutputMainText("Your " + TailDesc() + " tail swishes across the ground in anticipation.",False)
      if (chance > 75):
         OutputMainText("You lick your finger before sliding it into your mouth, sucking and pulling it out slowly with a small drop of saliva dangling upon your supple lips while you rub the " + CockDesc() + " phallic outline in your " + ClothesBottom() + " with your other hand.",True)
      if (ePref == 3) or (ePref == 4):
         DoeLust(math.floor((Percent() / 10) + (eLib / 5)))
      elif (ePref == 1) or (ePref == 2):
         DoeLust(math.floor((Percent() / 10) + (eLib / 10)))
   elif (gender == 0) and (ePref != 0) and (eGen != 0):
      OutputMainText("Your " + HipDesc() + " hips dance provocatively while you lick and suckle your fingers, trying to show off what you can do with what you've still got.",True)
      DoeLust(math.floor((Percent() / 10) + (eLib / 10)))
   else:
      OutputMainText("Your attempt at an erotic display only seems to turn the " + EnemyName() + " off further.",True)
      eLust -= 5

def BattleWin():
   global eCoin, eItem, eSexP, hrs
   OutputMainText("You walk away from the battle the victor and to the victor goes the spoils.",True)
   if (eCoin != 0):
      OutputMainText("\n" + "\n" + "Somewhere on the passed out body (you probably don't want to know where) you find " + eCoin + " coins.",False)
      DoCoin(eCoin)
   if (eItem != 0):
      OutputMainText("\n" + "\n" + "You manage to obtain " + ItemName(eItem) + " from your opponent.",False)
   if (eSexP != 0):
      OutputMainText("\n" + "\n" + "For your efforts, you grow in experience, gaining " + eSexP + " SexP!",False)
      DoSexP(eSexP)
   if (eItem != 0):
      ItemAdd(eItem)
   hrs = 2
   DoEnd()

def SpecialRapeWin():
   global enemyID, defeatedMinotaur, currentDungeon, defeatedFreakyGirl, defeatedSuccubus
   if (enemyID == 303):
      OutputMainText("\n" + "\n" + "The octopus shudders as her belly quakes, the orgasm having wracked her a little too strongly. She huffs as she begins to crawl back towards the ocean. Just as she touches the water, she lets out a loud groan. Her tentacles quiver and part, exposing her vaginal-beak. The thing yawns wide as a spherical object pushes through." + "\n" + "\n" + "Clear with a solid pink center, the egg falls from her dripping pussy-beak, and into the sand. Barely 4 inches in diameter, it doesn't come close to the size of her belly. She quickly catches her breath, her pink face red with embarrassment, before she pushes herself into the water, a tentacle grabbing the egg and pulling it with her before any more can escape..." + "\n" + "\n" + "However, she seems to have left behind a big gob of pink goop.",False)
   elif (enemyID == 304) or (enemyID == 305):
      OutputMainText("\n" + "\n" + "As the " + enemyName() + " collapses to the ground, wracked by orgasms and thoroughly distracted by the lewd fun, you find yourself beginning to grow. The effects of the bottle seems to wear off as you return to your normal height. Donning your outfit once again, however, it feels a little loose. It seems as though you're still missing a couple inches in height... On the other hand, however, inspecting the " + enemyName() + "'s body, you find something wedged in a rather lewd location.",False)
   elif (enemyID == 306):
      OutputMainText("\n" + "\n" + "The naga collapses to the ground, tail still squirming in delighted orgasm and no longer wishing to battle. You take a moment to brush off some of the sparkly colorful dust from her wings for potential use later. Not quite sparkly of colorful when in your hands, you can at least ball it up into a nice suppository.",False)
   elif (enemyID == 307):
      OutputMainText("\n" + "\n" + "He succombs to the pleasant sensations and doesn't seem to want to stop. \"You win, take this, go do stuff.\"" + "\n" + "\n" + "The Minotaur slides a jug across the floor to you and then ignores you.",False)
      if (defeatedMinotaur == False):
         defeatedMinotaur = True
         currentDungeon = 1003
      else:
         currentDungeon = 1003
   elif (enemyID == 308):
      OutputMainText("\n" + "\n" + "A little too much for her, the girl can't seem to get back up. \"Y-You win... \" She proceeds to pull off Mr. Snuggles head, a feature the doll seems to naturally have, and she reaches down his neck to pull out an object which she tosses to you." + "\n" + "\n" + "\"Please go now, I want some time alone...\"",False)
      if (defeatedFreakyGirl == False):
         defeatedFreakyGirl = True
         currentDungeon = 1006
      else:
         currentDungeon = 1006
   elif (enemyID == 309):
      OutputMainText("\n" + "\n" + "However, her hips can stop twitching and she has difficulty zipping back up, nearly coming again just from trying. \"O-Okay... You win. I... I can't take any more than that... Here, you can have one of these for besting me. Should give you back some of what I took.\"" + "\n" + "\n" + "She detaches one of the glowing vials from her belt and tosses it to you.",False)
      if (defeatedSuccubus == False):
         defeatedSuccubus = True
         currentDungeon = 1010
      else:
         currentDungeon = 1009
   else:
      OutputMainText("\n" + "\n" + "The " + EnemyName() + " collapses to the ground, quivering body wracked by orgasms. Having broken its mental state into a puddle of sex, it no longer wishes to battle.",False)

def SpecialKOWin():
   global enemyID, defeatedMinotaur, currentDungeon, defeatedFreakyGirl, defeatedSuccubus
   if (enemyID == 303):
      OutputMainText("\n" + "\n" + "Saddened with your rough treatment, you don't seem to want to play like she does. A bit hurt, she jumps back into the ocean, leaving nothing but a gob of pink goop behind.",False)
   elif (enemyID == 304) or (enemyID == 305):
      OutputMainText("\n" + "\n" + "As the " + EnemyName() + " passes out from all the pain, you find yourself beginning to grow. The effects of the bottle seems to wear off as you return to your normal height. Donning your outfit once again, however, it feels a little loose. It seems as though you're still missing a couple inches in height... On the other hand, however, inspecting the " + EnemyName() + "'s body, you find something wedged in a rather lewd location.",False)
   elif (enemyID == 102):
      OutputMainText("\n" + "\n" + "Feeling itself about to dissipate from your attacks, the desiccating dust devil feebly spins away, leaving behind some of the sand it can no longer support.",False)
   elif (enemyID == 306):
      OutputMainText("\n" + "\n" + "The naga passes out from your attacks, allowing you take a moment to brush off some of the sparkly colorful dust from her wings for potential use later. Not quite sparkly of colorful when in your hands, you can at least ball it up into a nice suppository.",False)
   elif (enemyID == 307):
      OutputMainText("\n" + "\n" + "\"No, stop! No more! It hurts!\" He slinks away from you, sullen. \"You win, take this, go do stuff." + "\n" + "\n" + "The Minotaur slides a jug across the floor to you and then starts grumbling to himself in a corner.",False)
      if (defeatedMinotaur == False):
         defeatedMinotaur = True
         currentDungeon = 1002
      else:
         currentDungeon = 1002
   elif (enemyID == 308):
      OutputMainText("\n" + "\n" + "She growls and curses obsceneties while nursing her pain. \"GAH, NO MORE! TAKE YOUR DAMNED WINNINGS AND GO!\"" + "\n" + "\n" + "She proceeds to rip off Mr. Snuggles head, a feature the doll seems to naturally have, and she reaches down his neck to pull out an object which she throws at you.",False)
      if (defeatedFreakyGirl == False):
         defeatedFreakyGirl = True
         currentDungeon = 1004
      else:
         currentDungeon = 1004
   elif (enemyID == 309):
      OutputMainText("\n" + "\n" + "Ow, ow, ow, ow. Okay, okay, you win! Here, you can have one of these for besting me. Should give you back some of what I took.\"" + "\n" + "\n" + "She detaches one of the glowing vials from her belt and tosses it to you.",False)
      if (defeatedSuccubus == False):
         defeatedSuccubus = True
         currentDungeon = 1010
      else:
         currentDungeon = 1008
   else:
      OutputMainText("\n" + "\n" + "You have made the " + EnemyName() + " pass out from all the pain.",False)

def SpecailKOLose():
   global currentState, enemyID
   if (currentState == 2):
      if (enemyID == 303):
         OutputMainText("\n" + "\n" + "Just as you're about to pass out, you see the octopus girl lean over your body. She wears a disappointed expression, finding you weren't strong enough for what she was looking for. Shrugging, she jumps back into the ocean, leaving you to yourself.",False)
      elif (enemyID == 304) or (enemyID == 305):
         OutputMainText("\n" + "\n" + "Just as you're about to pass out, you feel yourself beginning to grow. The effects of the bottle seems to wear off as you return to your normal height. Though not quite all the way...",False)
      elif (enemyID == 30):
         OutputMainText("\n" + "\n" + "The succubus seems a bit surprised as you pass out. \"Oops... I thought you could take more than that. Sorry~\"",False)
   
def DoRape():
   global enemyID, gender, sen, showBalls, cockSize, cockSizeMod, cockTotal, vagTotal, tallness, knot, clitSize, body
   chance = 0
   if (enemyID == 1):
      if (gender == 1):
         OutputMainText("You stick your cock in the test enemy's butt and cum.",True)
      if (gender == 2):
         OutputMainText("You sit on the test enemy's cock until you cum.",True)
      if (gender == 3):
         OutputMainText("You stuff your cock in the test enemy's butt, then sit on its cock and cum.",True)
   if (enemyID == 201):
      OutputMainText("You easily roll the wolf onto his back. Pulling " + PullUD(2) + " your " + ClothesBottom() + ", you squat your " + VulvaDesc() + " cunt over his sheath, wedging it between your folds while you grind against it. Once his bright red prick twitches as it stretches from its sheath, reaching long and hard while dribbling with pre, you slip it into " + OneYour(2) + " hungry hole" + Plural(2) + ". You bounce on top of his belly,",True)
      if (MoistCalc(2) > 7):
         OutputMainText(" your honey splashing about everywhere,",False)
      OutputMainText(" his hard doggy dick scraping against your inner walls. The lone wolf howls and drools, his tongue lolling out the side of his muzzle, as hot spurts of fresh cum gush within you. You shudder at the raw sensation, squeezing his coarse fur between your thighs. Then, you shiver as you feel the base of his cock swell, knotting within you. You collapse beside him, your pussy throbbing with orgasm, as you gasp and moan with his howls...",False)
      OutputMainText("\n" + "\n" + "\n" + "Eventually, his knot deflates. You rub your ",False)
      if (VagLimit() < 8):
         OutputMainText("sore little pussy, a bit stretched from the size of the thing,",False)
         VagChange(1,0)
      else:
         OutputMainText("satiated cunt,",False)
      OutputMainText(" the cock sliding out with cum dripping down " + LegWhere(1) + " your " + LegDesc(2) + ".",False)
      DoImpregnate(EnemyBaby())
      DoLust(-math.floor(sen / 2),2,2)
   if (enemyID == 202):
      OutputMainText("You easily roll the wolf onto his back. Pulling " + PullUD(2) + " your " + ClothesBottom() + ", you squat your " + ButtDesc() + " ass over the pointy prick. You grab the hard, meaty rod and gently squeeze out some of the pre, slipping it about between your cheeks to make things nice and slick. Slowly sitting down, you wince as the narrow tip kisses your tight hole and moan as it slides in, easily stretching your ass around its curvy girth.",True)
      if (showBalls == True):
         OutputMainText(" Your " + BallDesc() + " testicles eventually come to a rest upon the wolf's belly, with your own " + CockDesc() + " cock" + Plural(1) + " bobbing above.",False)
      else:
         OutputMainText(" Your own " + CockDesc() + " cock" + Plural(1) + " eventually come to a rest upon the wolf's belly, slightly tickled by his course fur.",False)
      OutputMainText("\n" + "\n" + "After a couple breaths from taking in the warm intruder, you begin to bounce your hips upon the animal. It howls back up at you in pleasure, your own gasps matching as your erection" + Plural(1) + " drum" + Plural(3) + " the fur. The wolf's tongue lolls out of the side of its mouth, allowing you to do all the work as its hind legs twitch in the air and its tail swishes over the ground. It seems to be quite happy with the result of this ordeal, so much so that it begins to spurt into your rectum rather quickly, coating your insides with hot sticky spunk." + "\n" + "\n" + "However, you're not left out of the fun as you feel something swell within the entrance to your ass. The wolf's knot expanding, the prick grinds against your inner walls more and more as it sprays about. You can't last any longer and explode above the wolf, drenching its fur in strand after strand of fresh steamy semen. More soon begins to spew back out your ass as the pent-up wolf overflows your cavity, forming sticky webs about the cheeks of your rump." + "\n" + "\n" + "Fur is eventually completely matted, dripping with wads of white, while your own " + SkinDesc() + " is sufficiently gunked up around your bottom and thighs. The wolf pants below you, tired and elated. With an attempt to stand, you lift the hind legs with you, still tied to your backside. But, with all the mess that has been made, the cock slips out with a wet pop and sends the animal back into the puddle below with a splash.",False)
      DoLust(-math.floor(sen / 2),2,5)
   if (enemyID == 301):
      chance = Percent()
      if (gender == 1) or ((Percent() <= 50) and (gender == 3)):
         if (chance <= 100):
            OutputMainText("The felin woman is easily bent forward by your efforts. Her loincloth droops out of the way, giving you a perfect view of the swollen, supple lips that pucker around the crotch of her bikini bottom. Pulling " + PullUD(2) + " your " + ClothesBottom() + ", you slide " + OneYour(1) + " " + CockDesc() + " prick" + Plural(1) + " out and through the cheeks of her ample rump, making her quiver with anticipation. Not wanting to leave her waiting for too long, the head of your cock pushes into the bikini bottom, pushing through to kiss the waiting hole within.",True)
            if ((cockSize * cockSizeMod) > eVagLimit(40)):
               OutputMainText("\n" + "\n" + "However, she cries out in pain and disappointment, your " + CockDesc() + " cock far to big to fit inside without tearing her apart. So, instead, you slip it between her legs, rubbing it across her stiff clit and through her loincloth and over her belly as you ",False)
            if ((cockSize * cockSizeMod) <= eVagLimit(40)) and ((cockSize * cockSizeMod) > eVagLimit(24)):
               OutputMainText("\n" + "\n" + "She cries out in pain and pleasure as your " + CockDesc() + " cock stretches her thirsting cunt wide, pushing her bikini in until it tears from your path. She pushes her rump back towards you, trying her best to devour the hot rod all the way to its hilt as you ",False)
            if ((cockSize * cockSizeMod) <= eVagLimit(24)):
               OutputMainText("\n" + "\n" + "She cries out in ecstacy as her hungry cunt devours your " + CockDesc() + " cock, along with her own bikini until it tears from your path. She takes it all the way in to your hilt as you ",False)
            OutputMainText("lean forward and hug her from behind, your hands groping about her many breasts. You pump hard, again and again, until the unavoidable pressure begins to build. Soon, you blow your load ",False)
            if ((cockSize * cockSizeMod) > eVagLimit(40)):
               OutputMainText("across her chest while she tries to lap up the spray with her tongue. You pull back, leaving her a mess.",False)
            if ((cockSize * cockSizeMod) <= eVagLimit(40)):
               OutputMainText("into her womb, making her let out a long and joyful mewl. Before she can become too content, you pull out of her with a slurp, your cum still dribbling from her used sex.",False)
            CumAmount()
      elif (gender == 2) or (gender == 3):
         OutputMainText("You knock the felin woman backwards onto her ample ass, her legs spreading wide. She cries out as you duck beneath her loincloth and lick her stiff clit through her bikini. Juices flood within your mouth as she instantly reacts, her swollen cunt-lips gnawing at the crotch of the messy bottom. You pull it aside, diving in and getting a good mouthful of her supple flavor. You devour her folds until she twitches uncontrollably, so desparate to come. But, before she does, you consider your own needs and draw your head out before repaclacing it with your own crotch.",True)
         OutputMainText("\n" + "\n" + "You grind against her stiff clit as it pokes through her loin cloth, your own " + ClitDesc() + " button" + Plural(2) + " throbbing through your " + ClothesBottom() + ".",False)
         if (cockTotal > 0) and (CumAmount() > 0):
            OutputMainText(" You pull your " + CockDesc() + " cock" + Plural(1) + ", letting the engorged length" + Plural(1) + " bounce against her belly and hump through her many breasts.",False)
         OutputMainText(" You grind, cunt to cunt" + Plural(2) + ", until you both let out a yowl as you climax together." + "\n" + "\n" + "You're quick to gather your wits and clean yourself up, standing before her pussy even stops gushing with honey.",False)
      DoLust(-math.floor(sen / 2),2,1)
   if (enemyID == 302):
      if (gender == 2) or ((Percent() <= 50) and (gender == 3)):
         OutputMainText("The drunken equan falls to his ass, his huge cock bouncing out of his loose pants. It throbs in the air, a large gob of pre spilling out. With a smirk, you step over him, pulling " + PullUD(2) + " your " + ClothesBottom() + " and showing him your own hungry flesh. You " + LegVerb(1) + " your " + LegDesc(2) + " over his twitchy rod, kissing the flat head of the horsy member with your " + VulvaDesc() + " lips.",True)
         if (VagLimit() < 32):
            OutputMainText("\n" + "\n" + "His man-meat is far too large for your cunt" + Plural(2) + " however, so you do the next best thing and sit down in his lap. Grinding your hips forward, your " + ClitDesc() + " clit" + Plural(2) + " hump" + Plural(4) + " into his length. The long prick squeezes between your " + BoobDesc() + " tits as you press against him, making him tense even more.",False)
         else:
            OutputMainText("\n" + "\n" + "You plunge down onto his giant man-meat with " + OneYour(2) + " " + VulvaDesc() + " cunt" + Plural(2) + ". It fills you up so much you grin with a drool. You hug him close, your " + BoobDesc() + " tits pressing against his firm chest, making the thing inside you even harder.",False)
         OutputMainText(" Your hips jerk up and down again and again as you rub along his length. Tingling sparks between the two of you as you feel his softball-sized testicles tighten up beneath your " + ButtDesc() + " butt. Within seconds, the two of you echo in ecstacy, his whinnying quickly over-taking your moans,",False)
         if (VagLimit() < 32):
            OutputMainText(" his cock erupting like a volcano between the two of you",False)
            if (cockTotal > 0) and (CumAmount() > 0):
               OutputMainText(", with yours joining in the volley,",False)
            OutputMainText(" and the hot spunk spills back down all over your bodies." + "\n" + "\n" + "You don't give him much time to recover as you pull away, leaving a bit of after-cum to gush out over his belly.",False)
         else:
            OutputMainText(" his cock erupting within you like a powerful volcano, the molten spunk making your belly swell slightly before spilling back out onto the ground",False)
            if (cockTotal > 0) and (CumAmount() > 0):
               OutputMainText(", while yours sprays across his chest and face",False)
            OutputMainText("." + "\n" + "\n" + "You don't give him much time to recover as you pull him out, a bit of after-cum gushing across your clit" + Plural(2) + ".",False)
            DoImpregnate(EnemyBaby())
      elif (gender == 1) or (gender == 3):
         OutputMainText("The drunken equan falls to his ass, his huge cock bouncing out of his loose pants. It throbs in the air, a large gob of pre spilling out. With a smirk, you step over him, pulling " + PullUD(2) + " your " + ClothesBottom() + " and brandishing " + OneYour(1) + " own " + CockDesc() + " cock" + Plural(1) + ". You roll him over onto all fours, his pants quickly slipping from his tight rump as you give it a slap.",True)
         OutputMainText("\n" + "\n" + "He whinnies loudly as you plunge your " + CockDesc() + " erection into his backside. Again and again, you pump away at his hole, until he lets out a loud whinny. His eyes going wide, his giant rod explodes across the ground until its massive length is swimming in a puddle of his own stuff,",False)
         if (CumAmount() > 0):
            OutputMainText(" while yours erupts into his ass, churning his insides,",False)
         OutputMainText(" until you've both had a heady orgasm. You pull out quickly, fluids still dripping from your cock, while he heaves upon the ground.",False)
      DoLust(-math.floor(sen / 2),2,1,5)
   if (enemyID == 303):
      if (gender == 1) or (gender == 3):
         OutputMainText("Able to wrestle through the octopus girl's eight powerful tentacles and knock her onto her squishy bottom, you pin her onto her back. Her tentacles spread wide before you, you're able to see the underside of her fleshy webbing. Her hands cover her face in a futile attempt to hide her blush while you inspect her. In the center of all the tentacles, right beneath her hips, gasps a gaping hole." + "\n" + "\n" + "A sort of 'beak', like octopuses normally have, encompasses the hole. It looks tougher than the surrounding flesh, able to maintain its shape, but as you stick your finger into the maw and it bites down upon you, you realize it's still quite soft, merely molding around your finger. Beyond the beak itself is a deep hallway of supple folds that ripple as it tries to swallow your finger, and supremely lubricated as your finger comes out with a long strand of translucent slime trailing behind it. With your own smirk, you pull " + PullUD(2) + " your " + ClothesBottom() + " and let your " + CockDesc() + " erection" + Plural(2) + " wobble out. Aligning yourself, you thrust ",True)
         if (cockTotal == 1):
            OutputMainText("it",False)
         else:
            OutputMainText("all of them",False)
         OutputMainText(" into her juicy hole.",False)
         if ((cockTotal * cockSize * cockSizeMod) > 40):
            OutputMainText("\n" + "\n" + "Surprisingly, she's able to take in all of your length" + Plural(1) + ", although you hear a dulcet, yet quite high pitched, cry as her face escapes her hands and lurches forward with her mouth wide in a strange combination of pain and confusion. She settles down quickly, however, and idly grips at the sand beneath her and her tentacles wrap around you to hang on for dear life. Her body literally stretches to form around your " + CockDesc() + " cock" + Plural(1) + ", with lubrication spitting out from her beak, her skin becoming more translucent the more taut she becomes, until you can make out your throbbing erection" + Plural(1) + " within. Fortunately, her belly isn't affected by the stretching, her pregnancy perfectly fine.",False)
         else:
            OutputMainText("\n" + "\n" + "She seems to be able to take your length" + Plural(1) + " easily, her passage large and excessively lubricated. Her hands leave her face as she grins wryly, not having expected you to take her on as such. Her tentacles wrap around your body, pulling you in deeper as she gropes her large belly.",False)
         OutputMainText("\n" + "\n" + "The hungry maw seems to constantly swallow your dick" + Plural(1) + " as you plunge into her again and again. The slick folds do a number on you, bringing you to orgasm within a minute. You gush inside of her,",False)
         if (CumAmount() > 2000):
            OutputMainText(" your massive amount of cum causing her to swell further, her soft skin growing lighter as it stretches,",False)
         OutputMainText(" until you're fully spent." + "\n" + "\n" + "Just as you're about to pull out, you see her squirm, her belly jiggling and growing slightly larger, deforming slightly as the offspring inside her shifts.",False)
      elif (gender == 2):
         OutputMainText("Able to wrestle through the octopus girl's eight powerful tentacles and knock her onto her squishy bottom, pinning her onto her back. Her tentacles spread wide before you, you're able to see the underside of her fleshy webbing. Her hands cover her face in a futile attempt to hide her blush while you inspect her. In the center of all the tentacles, right beneath her hips, gasps a gaping hole." + "\n" + "\n" + "A sort of 'beak', like octopuses normally have, encompasses it. The beak looks tougher than the surrounding flesh, able to maintain its shape, but as you stick your finger into the maw and it bites down upon you, you realize it's still quite soft, merely molding around your finger. Beyond the beak itself is a deep hallway of supple folds that ripple as it tries to swallow your finger, and supremely lubricated as your finger comes out with a long strand of translucent slime trailing behind it. With your own smirk, you pull " + PullUD(2) + " your " + ClothesBottom() + " and begin to grind your " + VulvaDesc() + " cunt" + Plural(2) + " against it." + "\n" + "\n" + "She lets out a warbling moan. Her hands leave her face, showing the blush and lustful expression she now wears. The beak nips at your " + ClitDesc() + " clit" + Plural(2) + " whenever the stiff thing" + Plural(2) + " rub against it, making you buck in turn. Her tentacles quickly begin to grope around your body, making you slick as the move towards your crotch.",True)
         if (vagTotal > 1) and (vagTotal < 9):
            OutputMainText("\n" + "\n" + "One tentacle for each of your pussies, they softly dive in, as far as they can go before they feel you begin to stretch. They slip in and out as you hump the girl, quickly driving you towards climax.",False)
         elif (vagTotal == 1):
            OutputMainText("\n" + "\n" + "A tentacle softly slips into your pussy, diving in as far as it can go before it feels you begin to stretch. It slips in and out as you hump the girl, quickly driving you towards climax.",False)
         elif (vagTotal > 8):
            OutputMainText("\n" + "\n" + "Taking turns at each of your pussies, the tentacles softly dive in, as far as they can go before they feel you begin to stretch. They slip in and out as you hump the girl, quickly driving you towards climax.",False)
         OutputMainText(" You can soon feel her shudder " + LegWhere(1) + " your " + LegDesc(2) + ", her large belly jiggling as milk drizzles past the feeding starfish and down her large breasts. The tentacles leave your slit" + Plural(2) + " as you finish with your own orgasm...",False)
      DoLust(-math.floor(sen / 2),2,1,2)
   if (enemyID == 304):
      if (vagTotal > 0) and (VagLimit() > 80):
         OutputMainText("Somehow managing to push the little big bunny-man onto his tail, you pull " + PullUD(2) + " your " + ClothesBottom() + ", climb up through his thighs, and plant your " + LegDesc(10) + " on his relatively large scrotum. His conical cock stands high before you, red and wet with arousal. With it's sloped shape, you easily manage to climb up it as well, " + LegVerb(5) + " it at the top with your " + LegDesc(2) + ". The narrow tip easily fits between your thighs and slips into " + OneYour(2) + " " + VulvaDesc() + " vagina" + Plural(4) + " as you descend upon it." + "\n" + "\n" + "His eyes roll up into his head as you slip down his length, the prick stretching your hole open wider and wider as it slides in.",True)
         if (tallness < 180):
            OutputMainText(" Your belly begins to stretch as the tip burrows through your inner flesh, the giant cock filling you tremendously. By the time your " + ButtDesc() + " rump lands upon his balls, your " + LegDesc(2) + " wedge" + LegPlural(1) + " into his sheath, the " + SkinDesc() + " of your belly reaches past your head. You stand again to fuck his massive prick, though... you quickly find it's difficult to manage such a thing with his body so much larger that yours." + "\n" + "\n" + "To your surprise, you find a white hand wrapping around your body, hugging you against the cock. Before you know it, you're being lifted into the air, slipping up the shaft, only to come back down once more. Difficult to tell who's raping who at the point, but he overtaken bunny-man masturbates with you as his toy. Fast and faster he pumps you up and down his length, quickly bringing you both to orgasm. His seed gushes into your belly, causing it to visibly ripple and distend from outside. It splashes back down the cock and spills around his sheath, quickly soaking through the fur of his balls. The warmth sends you to climax as well, slowly slipping off his shlong as it receeds into his sheath...",False)
         else:
            OutputMainText(" Taking in his entire length, you bounce again and again, letting it penetrate you thoroughly. His long foot beats against the ground in ecstasy while the whiskers around his nose twitch. It doesn't take long for him to freeze, his hips bucking into you, as your cunt fills with his seed, spilling back down around his sheath and soaking into the fur on his balls.",False)
         DoImpregnate(EnemyBaby())
      else:
         OutputMainText("Rather intimidated by his size, you still manage to pull his head down until he's on all fours. You pull " + PullUD(2) + " your " + ClothesBottom() + " and shove his face into your naked groin. He quickly notices your scent and lustfully opens his mouth. You debate whether this is actually rape or not as he seems eager to lap at your",True)
         if (gender == 1):
            OutputMainText(" " + CockDesc() + " cock" + Plural(1) + "",False)
         if (gender == 2):
            OutputMainText(" " + VulvaDesc() + " cunt" + Plural(2) + "",False)
         if (gender == 3):
            OutputMainText(" " + CockDesc() + " cock" + Plural(1) + " and " + VulvaDesc() + " cunt" + Plural(2) + "",False)
         OutputMainText(", expertly sucking and nibbling at your genitals. One of his hands reaches to his underside and begins to audibly slurp across his growing erection. He quickly drives you to orgasm and as his mouth fills with your fluids, you soon find his spraying about your " + LegDesc(10) + " as well." + "\n" + "\n" + "You both soon back away from each other, spent from the connection.",False)
      DoLust(-math.floor(sen / 2),2,1,2)
   if (enemyID == 305):
      if((cockSize * cockSizeMod) > 140) or ((cockTotal * cockSize * cockSizeMod) > 280):
         OutputMainText("Somehow managing to push the little big bunny-girl onto her tail, you pull " + PullUD(2) + " your " + ClothesBottom() + " and step in between her thighs. Her pussy is already aroused and gaping, drooling with her feminine lubrication and forming webs from her large clit down through her inner labia. Hefting up your " + CockDesc() + " erection" + Plural(1) + ", you aim for the sweet spot, spreading her even wider as you push yourself in, feeling her folds hug around you.",True)
         if (tallness < 180):
            OutputMainText("\n" + "\n" + "However, you quickly realize it's going to be quite... difficult to plow through someone so much larger than you... And much to your surprise, you find a white hand beginning to hug around you, lifting you up and pulling you back from her cunt. Then you find yourself being rammed back in, the clear fluids splashing about your " + SkinDesc() + ". Slightly confused as to who is raping who at this point, the bunny-girl proceeds to use you like a living dildo, ramming your cock" + Plural(1) + " in and out of her folds again and again.",False)
            if (knot == True):
               OutputMainText(" Your swelling knot" + Plural(1) + " pop in and out of her relatively tight cun again and again, causing her to let out an ecstatic shriek as she's stretched obscenely.",False)
            OutputMainText("\n" + "\n" + "Faster and faster she thrusts you through until you begin to feel her pussy squeeze about your length" + Plural(1) + ", pulsating rapidly with her large orgasm. You find yourself coming in second as your " + CockDesc() + " shlong" + Plural(1) + " burst" + Plural(3) + " inside of her",False)
            if (CumAmount() > 2000):
               OutputMainText(", the stuff spraying back out at you as it overflows her womb",False)
            OutputMainText("." + "\n" + "\n" + "Eventually she releases you back to the ground, allowing you to stumble backwards, her thighs heaving on either side with her breath.",False)
         else:
            OutputMainText(" Your hips quickly begin to thrust, holding her body down as you plow her again and again. She squirms erotically beneath you, her eyes rolled up into her head and her breasts jiggling back and forth in happiness. Soon her button nose and whiskers begin to twitch, followed by a shuddering from the rest of her body, as her pussy clamps down around your shaft" + Plural(1) + " in orgasm. You grunt as well as your cock" + Plural(1) + " fire" + Plural(3) + " back, filling her womb with your seed",False)
            if (CumAmount() > 2000):
               OutputMainText(" until it overflows and spews back out across your thighs",False)
            OutputMainText("." + "\n" + "\n" + "You pause for a moment, heaving over her, until you begin to pull your softening erection" + Plural(1) + " back out",False)
            if (knot == True):
               OutputMainText(", your knot" + Plural(1) + " making a lewd popping sound as it ejects from her stretched pussy, eliciting one last yelp of ecstasy",False)
            OutputMainText(".",False)
      else:
         OutputMainText("Rather intimidated by her size, you still manage to pull her head down until she's on all fours. You pull " + PullUD(2) + " your " + ClothesBottom() + " and shove her face into your naked groin. She quickly notices your scent and lustfully opens her mouth. You debate whether this is actually rape or not as she seems to eager lap at your",True)
         if (gender == 1):
            OutputMainText(" " + CockDesc() + " cock" + Plural(1) + "",False)
         if (gender == 2):
            OutputMainText(" " + VulvaDesc() + " cunt" + Plural(2) + "",False)
         if (gender == 3):
            OutputMainText(" " + CockDesc() + " cock" + Plural(1) + " and " + VulvaDesc() + " cunt" + Plural(2) + "",False)
         OutputMainText(", expertly sucking and nibbling at your genitals. Her hands reach to her underside and begins to audibly slurp in her crotch and rub at her bosom. She quickly drives you to orgasm and as her mouth fills with your fluids, you soon find a puddle of clear slime oozing its way about your " + LegDesc(10) + " as well." + "\n" + "\n" + "You both soon back away from each other, spent from the connection.",False)
         if (cockTotal > 0):
            CumAmount()
      DoLust(-math.floor(sen / 2),2,1,2)
   if (enemyID == 306):
      OutputMainText("Conceding to your assault rather willingly, she actually bends back over her tail and pulls up her sash, exposing herself to you. A supple slit amidst her belly-scales, the green of her scales part with a delicious and moist pink tunnel. Her fingers even roam down to part herself for you, waiting for you to please yourself with her.",True)
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "You prepare " + OneYour(1) + " " + CockDesc() + " cock" + Plural(1) + " as you remove it from your " + ClothesBottom() + ". You slide it over the scales of her tail as you approach her hips, making her shiver expectantly.",False)
         if ((cockSize * cockSizeMod) > eVagLimit(80)):
            outputMainText(" Your tip soon bumps into the valley between the mounds of her bulbous vulva and fused thighs, pressing against her sex. She gasps as it touches the sensitive pink flesh and her eyes go wide as you begin to press in. Your member far greater than her large yet tight entrance, her hips seem to unhinge, her lower maw stretching wider and wider to take in your full girth. The belly-scales distend with the thick rod driving deeper within, filling her so much that she wraps the tip of her tail around her chest and over her face, squeezing and biting it in ecstasy.",False)
         else:
            OutputMainText(" Your tip soon bumps into the valley between the mounds of her bulbous vulva and fused thighs, pressing against her sex. She gasps as it touches the sensitive pink flesh and croons as it pushes inside.",False)
         OutputMainText("\n" + "\n" + "The muscular flesh gnaws around your cock once you're fully devoured, making you collapse into the soft-scaled body. Your face presses into her chest, sneaking beneath the silken shawl and nibbling at the hills therein, making her writhe beneath you. Your hips quickly find a rhythm with hers, though her inner walls seem to be doing most of the work. Twisting and tenderly gnashing upon the meat you've fed her, the velvety flesh makes you both moan and shudder. For a creature that seemed so vicious before, she has become quite the docile and sexually charged. It doesn't take long before you're spraying your seed inside and she's clawing at her own scales in orgasm." + "\n" + "\n" + "After blowing your load, it takes another several minutes before her muscles release your softening member, allowing you to slip out and stumble back.",False)
         CumAmount()
      else:
         OutputMainText("\r\rYou pull " + PullUD(2) + " your own " + ClothesBottom() + " to expose yourself similarly. Climbing up her tail and straddling the humanoid half of her serpentine body, you press your " + VulvaDesc() + " lips against her own bulbous vulva, the slits kissing each other as they touch and making the naga let out a gasp. Despite your somewhat unstable position on top of her, she adjusts to keep you balanced, ensuring your continous mashing of feminine flesh." + "\n" + "\n" + "You grind into her, grabbing at her scales and groping beneath the silken shawl for her breasts. So enjoying your ministrations upon her, that you don't see the tip of her tail sneaking up behind you. It's not until you pleasantly find the thick thing pressing itself into " + OneYour(2) + " hole" + Plural(2) + " that you notice her own attack, though you can hardly object. You collapse upon her large body and embrace her, continuing your grinding into her sex as the agile tail swirls about your insides. For a creature that seemed so vicious before, she has become quite the docile and sexually charged. It doesn't take long before you're bucking your hips and she's bucking back in orgasm." + "\n" + "\n" + "After an extended period of moans from the two of you, it takes a few more before you can gather your strength and slide off, stumbling back.",False)
      DoLust(-math.floor(sen / 2),2,1,2)
   if (enemyID == 307):
      OutputMainText("You pull " + PullUD(2) + " your " + ClothesBottom() + " and push the Minotaur down onto his ",True)
      if (vagTotal > 0):
         OutputMainText(" ass and his hefty cock bounces out from under his loin cloth, already half erect.",False)
         if (VagLimit() < 72):
            OutputMainText(" Way too big for you, the most you can do is sit your " + ButtDesc() + " ass down on his head-sized testicles and hug yourself around his rod, grinding against it. He doesn't seem to mind though and rather eagerly snorts in excitement, taking your efforts as a rather physical lap dance. He grunts and groans as you grind your " + ClitDesc() + " clit" + Plural(2) + " against his shaft, especially when you begin to lick and knead his thick head." + "\n" + "\n" + "Rather abruptly, steam blows out his bovine nostrils as spunk blows out his cock. The stuff sprays hard, making you lean back to dodge direct contact with the geyser. You focus more on getting yourself off as you're showered with semen from above, until your hips are twitching and bucking against his meat." + "\n" + "\n" + "He was probably more pleasured by the performance than you were, but you manage.",False)
         else:
            OutputMainText(" You climb up his bulky body and he doesn't make any effort to stop you. He even flops his cock around so you can more easily squat over it, pushing the thick head into " + OneYour(2) + " " + VulvaDesc() + " cunt" + Plural(2) + ". The bull-man seems rather excited, snorting eagerly as you slide down his erection while it causes your belly to bulge more and more. Your " + ButtDesc() + " ass plops down into his lap, onto his head-sized balls and he leans back to let you do all the work." + "\n" + "\n" + "It's a bit difficult going up and down the whole length, but you crawl over his chest and manage to do well enough to make his cock throb throughout your passage. He's a little too eager, though, and quickly begins to start spraying stupid amounts of seed inside of you..." + "\n" + "\n" + "You continue to fuck him as you fill with his spunk, with plenty more squirting out with each pump, and eventually you manage to come yourself. Not exactly the most gratifying rape, but it works well enough...",False)
            DoImpregnate(EnemyBaby())
      else:
         OutputMainText("face and flip up his loin cloth to expose his large ass. The thing looks rather used already, though, and it doesn't take much to push in " + OneYour(1) + " " + CockDesc() + " cock" + Plural(1) + ". The bull-man even snorts across the floor like he was enjoying it and his large meaty cock rises to attention below him. Nevertheless, you continue to pump in and out grand rump, slapping the hard muscular buttocks",False)
         if (showBalls == True):
            OutputMainText(" while your " + BallDesc() + " balls slap against his head-sized testicles",False)
         OutputMainText(" and you're both quick to start spraying your loads. Yours gurgles down deeper into his body while his nearly knocks himself out with the blast, plenty of semen volleying into his face and pooling below him." + "\n" + "\n" + "Once you're satisfied, you have this nagging feeling like he might have enjoyed it more. Whatever the case may be, you got what you wanted.",False)
         CumAmount()
      DoLust(-math.floor(sen / 2),2,2,5)
   if (enemyID == 308):
      OutputMainText("The freaky little girl melts into your embrace rather readily, suddenly becoming more frail and acting more like she appears, holding Mr. Snuggles tight across her chest. \"Be gentle, please?\"" + "\n" + "\n" + "Catching you slightly off guard, you comply and proceed a little less roughly. You take her from behind, sitting down to the ground and pulling her into your lap with you. You kiss her cheek and nibble on her long elven ears, making her squirm in your arms as your hand reaches down beneath her skirt. Her panties are rather moist, slick with her honey, and the tender region twitches as you start to massage it. However, you soon feel something bumping against your palm." + "\n" + "\n" + "Pulling her undergarments down further, you can see her pink flesh protruding out past her crotch slightly. A clitoris as big as her thumb pokes out from her folds, stiff and twitching with arousal. Not quite as little as the rest of her..." + "\n" + "\n" + "Seeing as though she's rather aroused, you take the liberty of pushing things a step further. ",True)
      if ((cockTotal > 0) and ((cockSize * cockSizeMod) < eVagLimit(24))) or ((vagTotal > 0) and (clitSize < 60)):
         OutputMainText("Pulling " + PullUD(2) + " your " + ClothesBottom() + ", you angle ",False)
         if (cockTotal > 0) and ((cockSize * cockSizeMod) < eVagLimit(24))
            OutputMainText("" + OneYour(1) + " " + CockDesc() + " cock" + Plural(1) + "",False)
         else:
            OutputMainText("" + OneYour(2) + " " + ClitDesc() + " clit" + Plural(2) + "",False)
         OutputMainText(" towards her tight dainty folds, sinking it in as you push her down upon it as she lets out a slightly pained yet quite erotic squeal. By the time you're completely hilted inside of her, the protruding clit in front bucks up and down, jerking just from being penetrated. Such sensitivity only makes you want to thrill her more, making up for the pain she's given to you. You lift her slightly and slam her back down, thrusting with your hips in rhythm." + "\n" + "\n" + "\"Eeek!\" She cries out from the rough treatment, but the immediate cooing thereafter and the warmth you feel coming from her only shows that she enjoys it more. So the more you give to her..." + "\n" + "\n" + "Pounding again and again, you plow the small body in your lap, making her bounce up and down with your thrusting alone. The pigtails flail about, her mouth yawning wide and Mr. Snuggles riding on top of her tiny erection. She practically burns in your embrace, wildly reaching moaning and gasping orgasms while your own climax goes off",False)
         if (cockTotal > 0) and ((cockSize * cockSizeMod) < eVagLimit(24)):
            OutputMainText(", your spunk spraying into her womb",False)
            CumAmount()
         OutputMainText("." + "\n" + "\n" + "After a few minutes of tight connection, the girl crawls out of your lap, her naked ass shaking as she pulls you out before pulling her panties back up...",False)
      elif (cockTotal > 0):
         OutputMainText("Pulling " + PullUD(2) + " your " + ClothesBottom() + ", you realize your " + CockDesc() + " cock" + Plural(1) + " " + Plural(13) + " far too large for the small girl. Not wanting to tear her apart, despite the wounds she's given, you instead slip your stiff thing" + Plural(1) + " up through her lap and over her own twitching erection, sinking between the doll and her chest. She accepts this predicament and proceeds to hug your sensitive flesh along with Mr. Snuggles while she begins to grind against your cock" + Plural(1) + ". Her large button drags across you while her hands play with your shaft" + Plural(1) + ", rubbing you and trying to pleasure you as well." + "\n" + "\n" + "Her efforts succeed on both ends, sending the two of you into gasping orgasms. Your cum sprays over her chest and face, drenching the doll and her outfit. She shivers and shakes, her hips pressing down against yours as she tries to anchor the quaking clitoris.",False)
         OutputMainText("." + "\n" + "\n" + "After a few minutes of tight connection, the girl crawls out of your lap, her naked ass shaking as she pulls her panties back up...",False)
         CumAmount()
      else:
         OutputMainText("Turning the girl around, you land her back upon the floor. She looks up at you over the head of the doll, fearful of your menace as you press your " + HipDesc() + " hips down against her. Your " + VulvaDesc() + " nether-lips engulf her standing erection. Not enough to actually penetrate, you merely use the stiff button as a grinding post, slipping it through your labia again and again, banging it against your own " + ClitDesc() + " clit" + Plural(2) + "." + "\n" + "\n" + "The sensation sends the girl into a tizzy, her rump wiggling against the floor as her hips squirm from your succulent flesh. She bites down on one of Mr. Snuggle's horn, muffling her moans as she approaches orgasm. You make up for her with your own cries of climax, shivering and spilling your honey across her dainty sex while her own pools beneath her." + "\n" + "\n" + "A few more moments of the blissful high passes before the girl inches her way out from under you, spreading her legs to air out her heated crotch while she pulls up her panties, the undergarments becoming wet with her honey and outlining her sex, especially the button that continues to poke out...",False)
      DoLust(-math.floor(sen / 2),2,1,2)
   if (enemyID == 309):
      OutputMainText("\"Mmm, so you want to take the lead, huh?\" The succubus concedes to your advances, bending over and putting her hands up against the wall, even going so far as to unzip her panties down the middle, exposing her engorged plump lips. The meaty things are plush and look like they're made for being fucked hard, luring you in more as you press in behind her.",True)
      if (cockTotal > 0) or ((vagTotal > 0) and (clitSize > 20)):
         OutputMainText("\n" + "\n" + "You plunge ",False)
         if (cockTotal > 0):
            OutputMainText("" + OneYour(1) + " " + CockDesc() + " cock" + Plural(1) + "",False)
         else:
            OutputMainText("" + OneYour(2) + " " + ClitDesc() + " clit" + Plural(2) + "",False)
         OutputMainText(" into her awaiting entrance, pushing in deep.",False)
         if (cockTotal > 0) and ((cockSize * cockSizeMod) > 48):
            OutputMainText(" Amazingly, her sensual lips stretch wider and wider, taking in your whole length until your cock pushes back out against her belly below, her body easily taking you in and hugging you tightly with her warmth.",False)
         elif (cockTotal < 1) and (clitSize > 120):
            OutputMainText(" Amazingly, her sensual lips stretch wider and wider, taking in your whole length until your clitoris pushes back out against her belly below, her body easily taking you in and hugging you tightly with her warmth.",False)
         OutputMainText(" The swollen labia presses against your crotch as you sink your hilt inside. The whole tunnel slurps around your shaft, kneading and squeezing you gently with her well-trained muscles. She was definitely made for this sort of thing... You begin to thrust again and again, the divine pussy sucking you in and out with such fantastic intensity." + "\n" + "\n" + "And while your attention is diverted, you fail to notice the serpentine tail creeping around to your " + ButtDesc() + " tush. The spaded tip foldsin on itself, narrowing for a quick entrance into your ass. You buck harder into the she-devil as you feel yourself fill with the tail while it sensually slips in and out, pinning you from behind and urging you on further. Which you oblige." + "\n" + "\n" + "The succubus' wings spread as she lets out an ecstatic shrill, climaxing from your stimulated efforts. The grinding around your rod from her clenching passage also sends you along as well",False)
         if (cockTotal > 0):
            CumAmount()
            OutputMainText(", spraying your seed inside of her until it's pouring back out against your combined thighs",False)
         OutputMainText(".",False)
      else:
         OutputMainText("\n" + "\n" + "You fall to your knees and push your face into her nethers. You bite into the swollen labia and lick up through the crevice, devouring her sex until you can feel her quiver. The plush flesh around your face feels pleasant, encouraging you to dive in more, slipping your tongue in and out of her hole while her ass shakes in delight." + "\n" + "\n" + "And while you're busy eating out the oversexual pussy, the serpentine tail creeps down to " + OneYour(2) + " own. The spade at the tip of the tail folds in on itself, narrowing for a quick entrance into your tunnel. You buck as you're caught off guard, but with your face planted in her round ass you quickly sit back down, driving her tail deeper into you." + "\n" + "\n" + "The succubus seems pleased with the way things are, content with bringing you to orgasm as you do so for her. She lets out an ecstatic shrill, her wings spreading wide as she climaxes, a flood of honey pouring down around your mouth. The tail inside of you unfurls and drags across your inner walls, making your hips twitch with a writhing high in turn.",False)
      OutputMainText(" Yet, the climax feels a bit more draining than you might have expected. You feel slightly weaker, your body seemingly slimming down a bit, as the vials around the woman's belt glow slightly." + "\n" + "\n" + "\"Mmmm~\" She moans in concert with the glow. \"Tastes sooo good~\"" + "\n" + "\n" + "Just as you thought you had been the one in charge the whole time, the succubus pulls away from you and comes to a stand while zipping herself up. \"That was a nice snack~\"",False)
      Stats(-1,0,0,0)
      body = body - 1
      DoLust(-math.floor(sen / 2),2,1,2)

!def DoGetRaped():
   global enemyID, gender, cockTotal, sen, vagTotal, pregArray, cockSnakePreg
   if (enemyID == 1):
      if (gender == 1):
         OutputMainText("The test enemy pokes its cock in your butt and cums.",True)
      if (gender == 2):
         OutputMainText("The test enemy pokes its cock in your vagina and cums.",True)
      if (gender == 3):
         OutputMainText("The test enemy pokes its cock in your vagina and cums while stroking you off.",True)
   if (enemyID == 101):
      if (cockTotal > 0):
         OutputMainText("As your growing erection" + Plural(1) + " spill" + Plural(3) + " from your " + ClothesBottom() + ", the cock-snake's mouth grows wide. It slithers forward, engulfing " + OneYour(1) + " cock" + Plural(1) + ", its mouth stretching wider and wider to fully engulf it, its body so elastic it could take on any length." + "\n" + "\n" + "In an instant, your body begins to writhe and shudder as the cock-snake's gullet strongly massages along your length, quickly building you to orgasm. You clench at the ground beneath you as the cum is sucked right from your body, your hips jerking while you pump it out. The cock-snake guzzles it down, drinking it until you're completely finished, some of the spunk splashing back out across your thighs..." + "\n" + "\n" + "Hunger sated, the cock-snake slithers away",True)
         if (CumAmount() > 2300):
            OutputMainText(", its belly obviously distended from your massive load",False)
         OutputMainText(".",False)
         DoLust(-math.floor(sen / 2),2,1)
      elif (vagTotal > 0):
         OutputMainText("Feeling the warmth emanating from beneath your " + ClothesBottom() + ", the cock-snake slithers in " + LegWhere(1) + " your " + LegDesc(2) + ". The phallic head nuzzles up against your " + VulvaDesc() + " lips, smearing around some of your lubricant. Its nose bumps against your " + ClitDesc() + " clit" + Plural(2) + ", testing your arousal until you quiver beneath.",True)
         if (PregCheck(1)):
            OutputMainText("\n" + "\n" + "Satisfied with what it sees, the wide-rimmed head pushes its way into your folds. You can feel it stretch your walls and move around inside of you, exploring your warm and soft inner-depths. The rest of its tail wraps around your " + LegDesc(1) + ", holding tightly and anchoring itself. Then, its muscles begin to flex and coil, yanking the head back through your passage. The head barely emerges for a second to make sure everything is fine, before thrusting itself back in. Again and again, pushing and pulling itself through your tunnel. The snake is fucking you!" + "\n" + "\n" + "And it's quite good at its job as well. The strong muscular body flexes and pulses within, matching your warmth and testing the limits of your pussy. In your state, you can't help but gasp and moan, quickly coming to climax. You shout in ecstasy as the sensations flow through you, orgasm wracking your body." + "\n" + "\n" + "In that moment of peak pleasure, the snake lets go of your " + LegDesc(1) + " and slips through your cervix as the doorway opens with your high, completely disappearing into your womb." + "\n" + "\n" + "In the few moments of bliss, your hands press down onto your bloated belly, feeling the phallic lube-covered snake squirm around and make itself comfortable inside of you...",False)
            i = 0
            while (i < len(pregArray)):
               if (pregArray[i] == False):
                  pregArray[i] = True
                  pregArray[i + 1] = 503
                  pregArray[i + 2] = 240
                  pregArray[this.i + 3] = 150
                  i = len(pregArray)
               i += 5
            cockSnakePreg += 50
            DoLust(-math.floor(sen / 2),2,2)
         else:
            OutputMainText("\n" + "\n" + "However, it seems to not be satisfied with what it has found. Barely sating any of your desire, the snake turns around and slithers off, completely losing interest...",False)
            DoLust(-5,0)
   if (enemyID == 201):
      OutputMainText("The lone wolf rolls you onto all fours with its nose. Obliging, you duck forward, raising your " + ButtDesc() + " rump into the air. He sniffs your cunt" + Plural(2) + ", lapping at the wetness that soaks through your " + ClothesBottom() + ". He jumps up, clawing your " + ClothesBottom() + " to shreds until your " + VulvaDesc() + " hot crotch is put on display. Scratching your back, he mounts you from behind." + "\n" + "\n" + "His rock-hard rod pokes and prods around your sex until it finds " + OneYour(2) + " gaping hole" + Plural(2) + " and plunges it in. You gasp as the steaming meaty flesh pounds into you, the wolf roughly humping away, the inner fur of his thighs rubbing back and forth along your " + ButtDesc() + " naked bum. He hugs you with his paws, his muzzle panting beside your ear while drool drips down from his lolling tongue and down your cheek. It only takes a minute before he howls loudly, cum spurting into your pussy at an astonishing rate. You shout as it floods your insides, a thick knot growing at your entrance and spreading you open further...",True)
      ChangeBot(-1)
      DoNext()
      OutputMainText("You gasp as you're about to pass out, feeling the wolf tug at your violated cunt in an attempt to get away. Still tied by his knot, his cock squirting away within, ",False)
      if (VagLimit() < 32):
         OutputMainText("you wince with each pull, the knot stretching you wider,",False)
         VagChange(1,0)
      elif (VagLimit() < 8):
         OutputMainText("you yelp with each pull, the knot far too large for your little pussy and stretches you much wider and wider while causing you some pain,",False)
         VagChange(2,0)
         DoHP(-5)
      else:
         OutputMainText("but your gaping cunt is more than enough to handle it,",False)
      OutputMainText(" until it finally pulls free and he runs back off into the forest.",False)
      DoImpregnate(EnemyBaby())
      DoLust(-math.floor(sen / 2),2,1)
   if (EnemyID == 202):
      OutputMainText("The lone wolf rolls you onto all fours with its nose. Obliging, you duck forward, raising your " + ButtDesc() + " rump into the air. He sniffs the thing you have presented him, burrowing his wet nose into your cheeks slightly and blowing in acceptance of your offer. He jumps up, clawing your " + ClothesBottom() + " to shreds until your " + ButtDesc() + " ass is ready for the taking. Scratching your back, he mounts you from behind." + "\n" + "\n" + "You can feel his pointed rod poke about the cushioning of your bum, swiftly finding its way into the crevice therein. Slick pre slips around the hole of your ass as the tips circles around, lubricating it lavishly for a smooth injection. A short gasp escapes your lips as the narrow tip kisses the hole, stretching it wide as it then rapidly rams in with a lewd schlick. The wolf's muzzle rests upon your shoulder, the long tongue lolling and panting hot humid air across your cheek. His hips bounce up and down, slipping in and out of your ass with slurping pops, growing more and more stiff." + "\n" + "\n" + "It doesn't take long before you feel hot spurts coat the inside of your rectum, splashing against the inner wall again and again. So much semen inside that you can feel yourself begin to bloat. The pressure quickly makes your own " + CockDesc() + " erection" + Plural(1) + " burst with white strands below, pumping out in tune to the throbbing of the growing girth in your ass. You can feel yourself stretch, the wolf's knot swelling to anchor itself within, overflowing cum spraying out as the hole tightens...",True)
      ChangeBot(-1)
      DoNext()
      OutputMainText("You gasp as you're about to pass out, feeling the wolf tug at your violated ass in an attempt to get away, gush after gush of spent spunk blowing out each time. Still tied by his knot, his cock now slowly squirting away within, you can't help but get yanked backwards several feet as he drags you over the ground by your sensitive hole. Eventually, you manage to grab at the ground and hold yourself firm, allowing the knot to pop out from your ass, the member spraying across your cheeks with more rushing out about your thighs. Freed of your ass, the wolf takes off into the forest, satisfied, leaving you to lay in the white mess below. ",False)
      DoLust(-math.floor(sen / 2),2,5)
   if (this.enemyID == 301)
   {
      this.outputMainText("Finally having someone as horny as she is, she pounces onto you. She presses your face against her exposed nipples, forcing you to lick the soreness that had been caused by her own rubbing. She grinds up and down your belly, tearing your " + this.clothesTop() + " to tattered shreds with her claws while biting and suckling from your own " + this.nipDesc() + "nipples",True);
      this.changeTop(-1);
      if(this.lactation > 0)
      {
         this.outputMainText(", delighting in the taste of your milk",False);
      }
      this.outputMainText(". However, it doesn\'t take long until she reaches beneath her loin cloth and pulls her bikini bottom to the side before she goes diving into your " + this.clothesBottom() + ",",False);
      if(this.gender == 1 || this.gender == 3)
      {
         this.outputMainText(" digging out " + this.oneYour(1) + " " + this.cockDesc() + " cock" + this.plural(1) + ".",False);
         if(this.cockSize * this.cockSizeMod > this.eVagLimit(40))
         {
            this.outputMainText(" She attempts to stand and squat down upon it, but, to her dismay, she can\'t seem to push it into her hungry pussy, even though she tried until tears welled up in her eyes from the painful stretching. Instead, she settles for hugging and humping the " + this.cockDesc() + " thing, grinding her own stiff little erection into it, her feminine juices spilling down its length and over your body.",False);
         }
         else if(this.cockSize * this.cockSizeMod > this.eVagLimit(20))
         {
            this.outputMainText(" She mewls and mrowls in pain as she stands up and squats down upon it. It spreads her so wide that it hurts her so much, yet she doesn\'t care, so desperate to fuck. Tears roll down her cheeks, but her mouth yawns wide with erotic joy, being filled so much.",False);
         }
         else
         {
            this.outputMainText(" She rises up, only to squat back down on your erection, your cock slipping into her supple folds. So absolutely overjoyed to finally have a cock in her, she scratches at your chest with her claws and bites down upon your neck.",False);
         }
         this.outputMainText(" Her hips speed up faster and faster, wildly working her pussy so much that the slick liquids spilling from her gurgle and churn into a bubbly mess. You too find her efforts to be extremely effective, your body quaking along with her.",False);
         if(this.cumAmount() > 550 && this.cockSize * this.cockSizeMod <= this.eVagLimit(40))
         {
            this.outputMainText(" She purrs loudly as she feels your cum explode within her, utterly pleased as it fills her so much that it squirts back out of her pussy with a loud lewd noise.",False);
         }
         else if(this.cockSize * this.cockSizeMod > this.eVagLimit(40))
         {
            this.outputMainText(" She purrs hungrily as she laps at you cum as it sprays about the both of you, her face absolutely delighted in having her fur matted with the stuff.",False);
         }
         else
         {
            this.outputMainText(" She purrs pleasantly as she feels your cum spurt within her, gyrating her hips around your rod to drink in every drop.",False);
         }
         this.outputMainText("\r\r",False);
         if(this.knot == True && this.cockSize * this.cockSizeMod <= this.eVagLimit(40))
         {
            this.outputMainText("With a high-pitched squeak, she pulls off of your knot without thinking. She rubs her poor cunny from the pain, only to roll her eyes up into her head with the pleasant masturbation. ",False);
         }
      }
      if(this.gender == 2)
      {
         this.outputMainText(" lapping at your " + this.vulvaDesc() + " crotch and rouchly licking your " + this.clitDesc() + " clit" + this.plural(2) + ".",False);
         if(this.clitSize > 25)
         {
            this.outputMainText(" With a wicked grin, she eyes your " + this.clitDesc() + " clit" + this.plural(2) + " hungrily.",False);
            if(this.clitSize > 100)
            {
               this.outputMainText(" She attempts to stand and squat down upon " + this.oneYour(2) + " erect button" + this.plural(2) + ", but, to her dismay, she can\'t seem to push it into her hungry pussy, even though she tried until tears welled up in her eyes from the painful stretching. Instead, she settles for hugging and humping the " + this.clitDesc() + " thing, grinding her own stiff little erection into it, her feminine juices spilling down its length and over your body.",False);
            }
            else if(this.clitSize > 50)
            {
               this.outputMainText(" She mewls and mrowls in pain as she stands up and squats down upon " + this.oneYour(2) + " erect button" + this.plural(2) + ". It spreads her so wide that it hurts her so much, yet she doesn\'t care, so desperate to fuck. Tears roll down her cheeks, but her mouth yawns wide with erotic joy, being filled so much.",False);
            }
            else
            {
               this.outputMainText(" She rises up, only to squat back down upon " + this.oneYour(2) + " erect button" + this.plural(2) + ", your clit slipping into her supple folds. So absolutely overjoyed to finally have a hard phallic object in her, she scratches at your chest with her claws and bites down upon your neck.",False);
            }
         }
         else
         {
            this.outputMainText(" She glides back up your chest and presses her sloppy cunt to yours, grinding the two together.",False);
         }
         this.outputMainText(" Her hips speed up faster and faster, wildly working her pussy so much that the slick liquids spilling from her gurgle and churn into a bubbly mess. You too find her efforts to be extremely effective, your body quaking along with her.",False);
      }
      this.outputMainText("Dazed and high with her climax, having finally overcome her heat a little, she stumbles away, her loin cloth pushed so far to the side that her lips shine between her legs for all to see.",False);
      if(this.percent() < 40 && this.ballSize > 1 && this.cockSize * this.cockSizeMod <= this.eVagLimit(40))
      {
         this.outputMainText(" And she seems oddly content, as though her heat had passed with that romp for some reason...",False);
      }
      this.doLust(-Math.floor(this.sen / 2),2,1,2);
   }
   if(this.enemyID == 302)
   {
      this.outputMainText("Seeing you laying defenseless and utterly aroused before him, the drunken equan falls to the ground. With a grunt and a grope, he pulls his huge cock from his pants, his erection barely 2/3 its full potential. Considering how drunk he is, it probably won\'t get much larger.",True);
      if(this.gender == 1 || this.gender == 3 && this.percent() <= 50)
      {
         this.outputMainText(" Nevertheless, not caring whether you\'re male or female, he turns you over to find the hole everybody has. Giving your " + this.buttDesc() + " ass a slap with his mug, he leans forward and plunges his erection deep inside.",False);
      }
      else if(this.gender == 2 || this.gender == 3)
      {
         this.outputMainText(" Nevertheless, he slips his arms behind your " + this.legDesc(6) + ", pushing them up and foward as his cock plows into " + this.oneYour(2) + " cunt" + this.plural(2) + ".",False);
         if(this.vagLimit() < 12)
         {
            this.outputMainText(" You cry out in pain as the cock slams against your entrance, completely unable to fit. So, instead, the the horny equan turns you over, plunging his erection deep into your " + this.buttDesc() + " ass until you can see it bulge through your belly.",False);
            this.doHP(-5);
         }
         else if(this.vagLimit() < 28)
         {
            this.outputMainText(" With a cry, the large horse-cock proves too big for your relatively small pussy, stretching it dramatically and causing you some pain.",False);
            this.vagChange(3,0);
            this.doHP(-Math.floor(this.eStr / 2));
            this.doImpregnate(this.enemyBaby());
         }
         else if(this.vagLimit() < 52)
         {
            this.outputMainText(" You wince as it pushes in too far, pounding your cervix further and further into your belly, permanently stretching you a bit.",False);
            this.vagChange(1,0);
            this.doImpregnate(this.enemyBaby());
         }
         else
         {
            this.outputMainText(" You feel it push against your belly from within, the mound slightly protruding through your " + this.skinDesc() + ", taking his entire length inside of you.",False);
            this.doImpregnate(this.enemyBaby());
         }
      }
      this.outputMainText(" Again and again, he has his way with your hole, until he lets out a loud whinny. Eyes going wide, you feel a flood of his hot stuff flush into your body, making you lose all thoughts of everything else...",False);
      if(this.cumAmount() > 0)
      {
         this.outputMainText(" Your cock" + this.plural(1) + " explode" + this.plural(3) + " across the ground just before you collapse, forming a nice puddle to splash in.",False);
      }
      this.outputMainText("\r\rAs drunk as he is, the large equan doesn\'t take long to pull out, cum dribbling in long strands from his huge cock and splattering across his pants, as he sways back towards Firmshaft.",False);
      this.doLust(-Math.floor(this.sen / 2),2,2,5);
   }
   if(this.enemyID == 303)
   {
      if(this.gender == 1)
      {
         this.outputMainText("With a giggle at your vulnerable state, her tentacles wrap about your " + this.buttDesc() + " butt, weaving into your " + this.clothesBottom() + " and pulling out your " + this.cockDesc() + " erection" + this.plural(1) + ". She takes " + this.oneYour(1) + " cock" + this.plural(1) + " and fondles it with the slimy appendages, making sure it\'s nice and hard.",True);
         if(this.cockSize * this.cockSizeMod > 50)
         {
            this.outputMainText(" Not wanting to stretch herself to engulf your " + this.cockDesc() + " thing, she instead wraps her tentacles around it, drawing it towards the center of her webbing, just beneath her hips.\r\rYou can\'t tell what is going on, but you quickly jerk as something nips at your urethra. Nothing painful, just a soft yet rigid fleshy thing, like cartilage, that gently pinches you. Then your eyes go wide as whatever it is begins to dig into your urethra, spreading the last couple of inches wider as it slips inside, holding your cock-tip open like a gaping hole.\r\rAgain, she is gentle, but any pain you might have noticed quickly disappears as all eight of her tentacles work together in harmony, writhing about your cock and making you twitch sporadically on the ground from the intense pleasure. She wrings your cock powerfully, quickly bringing you to a gushing orgasm, spraying your cum through your gaping urethra and filling her body.",False);
         }
         else
         {
            this.outputMainText(" Her whole body moves over yours, your groin being lost to her webbing.\r\rYou can\'t tell what is going on, but you quickly jerk as something nips at the tip of your rod. Nothing painful, just a soft yet rigid fleshy thing, like cartilage, that gently pinches you. Then your eyes go wide as whatever it is engulfs your length, sucking you inside. Supple folds squish and writhe around your cock, as though it were a pussy with a throat that was trying desperately to swallow you. Within moments, you find your " + this.hipDesc() + " hips jerking as you blow your load, filling her.",False);
         }
         if(this.cumAmount() > 2300)
         {
            this.outputMainText(" You come so much that her belly begins to swell larger, stretching to engulf as much of your seed as she can, before gushing back out and down your cock.",False);
         }
         this.outputMainText("\r\rHer belly shivers a little as it absorbs your cum. It grows slightly larger as her offspring wiggle inside, maturing. With a grin, she slides off of you and back into the ocean, her tentacles twitching excitedly as she disappears...",False);
      }
      if(this.gender == 2)
      {
         this.outputMainText("She grins at you, particularly happy to see you submit before her. She leans in for a wet kiss, licking your cheek with her long tongue, as her tentacles wrap around your " + this.buttDesc() + " butt. They weave into your " + this.clothesBottom() + " and pull it " + this.pullUD(2) + ", exposing your swollen and hungry " + this.vulvaDesc() + " cunt" + this.plural(2) + ". She then swings back, her tentacles flying wide for a moment and giving you a view of what\'s behind her webbing.\r\rIn the center of all the tentacles, right beneath her hips, gasps a gaping hole. A sort of \'beak\', like octopuses normally have, encompasses it. The beak looks tougher than the surrounding flesh, able to maintain its shape. However, as she rams it against your groin, you notice it\'s softer than you expected, more like cartilage. Yet, you don\'t have much time to reflect about what it is as it begins to nip at your nether-lips, prying them open and burying itself within, a few inches deep.\r\rIt doesn\'t hurt much, but any pain quickly dissipates as her tentacles wrap around your groin. The suction cups underneath stick to your " + this.skinDesc() + ", giving her a good grip, while some in particular latch onto your clit" + this.plural(2) + " and lips, tugging and sliming at your arousal. Your hips quickly begin to buck on the ground as she brings you to orgasm after orgasm, your button" + this.plural(2) + " and vulva swelling larger as fluids from the cups seep into them.",True);
         if(!this.pregCheck(1))
         {
            this.outputMainText("\r\rHowever, she seems to quickly notice that you already have something growing inside of you without room for more. With a smile, she removes her tentacles and draws up your body. She leans in yet again for another kiss, this time on your forehead, her breasts surrounding your face. Then she turns and leaps back into the water with a splash, leaving you wracked with ecstasy and larger genitals...",False);
            this.clitSize += 4;
            this.vulvaSize += 2;
         }
         else
         {
            this.outputMainText("\r\rWhile your mind is distracted by the multiple climaxes, you hardly notice as she begins to wince and groan, her arms hugging her belly. Then, amidst your ecstatic moans, you let out a gasp as something breaches your " + this.vulvaDesc() + " pussy, round and large.",False);
            if(this.vagSize < 20)
            {
               this.outputMainText(" The object is so big that it stretches your poor cunt" + this.plural(2) + " even larger, making sure there\'s enough room.",False);
               this.vagSize += 2;
            }
            this.outputMainText("\r\rAnd that was just the first...\r\rAgain and again, you can feel something slip into your womb. Yet, as her tentacles work at your " + this.clitDesc() + " clit" + this.plural(2) + ", you can do nothing but cry out in pleasure with each pass. Soon, you find yourself groping your own belly as it swells beneath your hands, while hers deflates, emptying its contents into you. Eventually, you look as pregnant as she did, the things inside shivering slightly at the warmth of their new home...\r\rHappy with her spawning season, the octopus girl gathers her own wits, relinquishing you from her tentacles and kissing your enormous belly. Then, she turns towards the ocean and dives back into it, disappearing until the next time she needs a surrogate...",False);
            this.i = 0;
            while(this.i < len(pregArray))
            {
               if(this.pregArray[this.i] == False)
               {
                  this.pregArray[this.i] = True
                  this.pregArray[this.i + 1] = 200;
                  this.pregArray[this.i + 2] = 216;
                  this.pregArray[this.i + 3] = 180;
                  this.i = len(pregArray);
               }
               this.i += 5;
            }
         }
      }
      if(this.gender == 3)
      {
         this.outputMainText("With a giggle at your vulnerable state, her tentacles wrap about your " + this.buttDesc() + " butt, weaving into you " + this.clothesBottom() + " and pulling out your " + this.cockDesc() + " erection" + this.plural(1) + ". She takes " + this.oneYour(1) + " cock" + this.plural(1) + " and fondles it with the slimy appendages, making sure it\'s nice and hard.",True);
         if(this.cockSize * this.cockSizeMod > 50)
         {
            this.outputMainText(" Not wanting to stretch herself to engulf your " + this.cockDesc() + " thing, she instead wraps her tentacles around it, drawing it towards the center of her webbing, just beneath her hips.\r\rYou can\'t tell what is going on, but you quickly jerk as something nips at your urethra. Nothing painful, just a soft yet rigid fleshy thing, like cartilage, that gently pinches you. Then your eyes go wide as whatever it is begins to dig into your urethra, spreading the last couple of inches wider as it slips inside, holding your cock-tip open like a gaping hole.\r\rAgain, she is gentle, but any pain you might have noticed quickly disappears as all eight of her tentacles work together in harmony, writhing about your cock and making you twitch sporadically on the ground from the intense pleasure. She wrings your cock powerfully, quickly bringing you to a gushing orgasm, spraying your cum through your gaping urethra and filling her body.",False);
         }
         else
         {
            this.outputMainText(" Her whole body moves over yours, your groin being lost to her webbing.\r\rYou can\'t tell what is going on, but you quickly jerk as something nips at the tip of your rod. Nothing painful, just a soft yet rigid fleshy thing, like cartilage, that gently pinches you. Then your eyes go wide as whatever it is engulfs your length, sucking you inside. Supple folds squish and writhe around your cock, as though it were a pussy with a throat that was trying desperately to swallow you. Within moments, you find your " + this.hipDesc() + " hips jerking as you blowing your load, filling her.",False);
         }
         if(this.cumAmount() > 2300)
         {
            this.outputMainText(" You come so much that her belly begins to swell larger, stretching to engulf as much of your seed as she can, before gushing back out and down your cock.",False);
         }
         this.outputMainText("\r\rHer belly shivers a little as it absorbs your cum. It grows slightly larger as her offspring wiggle inside, maturing.",False);
         this.outputMainText("With a grin, she seems particularly happy to have found such a suitable partner. She leans in for a wet kiss, licking your cheek with her long tongue, as her tentacles wrap around your " + this.buttDesc() + " butt once more. They squirm around your exposed swollen and hungry " + this.vulvaDesc() + " cunt" + this.plural(2) + ", making sure you\'re still aroused. She then swings back, her tentacles flying wide for a moment and giving you a view of what\'s behind her webbing.\r\rIn the center of all the tentacles, right beneath her hips, gasps a gaping hole. A sort of \'beak\', like octopuses normally have, encompasses it. The beak looks tougher than the surrounding flesh, able to maintain its shape. However, as she rams it against your groin, you notice it\'s softer than you expected, more like cartilage. Its the thing you had noticed before... Yet, you don\'t have much time to reflect about what it is as it begins to nip at your nether-lips, prying them open and burying itself within, a few inches deep.\r\rIt doesn\'t hurt much, but any pain quickly dissipates as her tentacles wrap around your groin. The suction cups underneath stick to your " + this.skinDesc() + ", giving her a good grip, while some in particular latch onto your clit" + this.plural(2) + " and lips, tugging and sliming at your arousal. Your hips quickly begin to buck on the ground as she brings you to orgasm after orgasm, your button" + this.plural(2) + " and vulva swelling larger as fluids from the cups seep into them.",False);
         if(!this.pregCheck(1))
         {
            this.outputMainText("\r\rHowever, she seems to quickly notice that you already have something growing inside of you without room for more. With a smile, she removes her tentacles and draws up your body. She leans in yet again for another kiss, this time on your forehead, her breasts surrounding your face. Then she turns and leaps back into the water with a splash, leaving you wracked with ecstasy and larger genitals...",False);
            this.clitSize += 4;
            this.vulvaSize += 2;
         }
         else
         {
            this.outputMainText("\r\rWhile your mind is distracted by the multiple climaxes, you hardly notice as she begins to wince and groan, her arms hugging her belly. Then, amidst your ecstatic moans, you let out a gasp as something breaches your " + this.vulvaDesc() + " pussy, round and large.",False);
            if(this.vagSize < 20)
            {
               this.outputMainText(" The object is so big that it stretches your poor cunt" + this.plural(2) + " even larger, making sure there\'s enough room.",False);
               this.vagSize += 3;
            }
            this.outputMainText("\r\rAnd that was just the first...\r\rAgain and again, you can feel something slip into your womb. Yet, as her tentacles work at your " + this.clitDesc() + " clit" + this.plural(2) + ", you can nothing but cry out in pleasure with each pass. Soon, you find yourself groping your own belly as it swells beneath your hands, while hers deflates, emptying its contents into you. Eventually, you look as pregnant as she did, even the extra bit she gained from after you filled her with your cum, the things inside shivering slightly at the warmth of their new home...\r\rEspecially happy with how well her spawning season went this week, the octopus girl gathers her own wits, relinquishing you from her tentacles and kissing your enormous belly. Then, she turns towards the ocean and dives back into it, disappearing until the next time she needs a surrogate...",False);
            this.i = 0;
            while(this.i < len(pregArray))
            {
               if(this.pregArray[this.i] == False)
               {
                  this.pregArray[this.i] = True
                  this.pregArray[this.i + 1] = 200;
                  this.pregArray[this.i + 2] = 252;
                  this.pregArray[this.i + 3] = 216;
                  this.i = len(pregArray);
               }
               this.i += 5;
            }
         }
      }
      if((this.gender == 2 || this.gender == 3) && this.pregCheck(1))
      {
         this.doLust(-Math.floor(this.sen / 2),2,2);
      }
      else
      {
         this.doLust(-Math.floor(this.sen / 2),2,1);
      }
   }
   if(this.enemyID == 304)
   {
      if(this.vagTotal > 0 && this.vagLimit() > 80)
      {
         this.outputMainText("A smirk crosses the bunny-man\'s face as you fall before him, your cunt" + this.plural(2) + " dripping with arousal. His own conical prick twitches in his sheath at the size of you gaping maw, even in your reduced state, eager to hop in and make you his new bunny-hole. He falls to his knees and wraps his arms around your body, his hips quickly closing the gap between your heights. You can hardly tell at first that " + this.oneYour(2) + " slit" + this.plural(2) + " is being penetrated, the narrow tip relatively small. But as he quickly plows the rest of his length in, your eyes nearly cross from the rapid change in girth.",True);
         if(this.tallness < 160)
         {
            this.outputMainText(" You can feel your belly distend, your vaginal flesh stretching out within to match the shape of his cock.",False);
         }
         if(this.tallness < 80)
         {
            this.outputMainText(" So much so that your vision becomes blocked by your own " + this.skinDesc() + ", the massive erection squeezing between your face and his body.",False);
         }
         this.outputMainText("\r\rWith tremendous fervor, he rams his hips into you again and again. So fast that your mind can hardly distinguish between being empty and relaxed versus stuff and stretched, it\'s all a blur. Long before you\'re even able to start to come to your own climax, you hear him clench his teeth above you. In an instant, your crotch feels hot and sticky as spunk floods your tunnel, splashing about as the bunny-man continues to hump away. His fuzzy balls smack against your thighs with lewd noises from the sticky mess, with no signs of slowing down.\r\rAgain and again he comes inside of you, your pussy almost numb from all the thrusting. So lost in the speedy sex, your mind can hardly register that you have reached orgasm",False);
         if(this.cockTotal > 0)
         {
            this.outputMainText(", barely noticing the extra stickiness upon his fur that rubs against your belly as your own erection" + this.plural(1) + " explode" + this.plural(3) + "",False);
         }
         this.outputMainText(".\r\rAll you seem to remember is the fact that he doesn\'t stop until you feel yourself begin to grow. He comes to an abrupt halt, yanking out while his spunk still spits between your thighs, and soon backs off as you begin to return to your normal state, though not quite...",False);
         this.doImpregnate(this.enemyBaby());
      }
      else
      {
         this.outputMainText("A smirk crosses the bunny-man\'s face as you fall to your " + this.legDesc(6) + ". He lunges forward to hold you up, his conical prick bobbing before your face. So lost in lust, your mouth subconsciously opens as you feel a supple tip press against it, sucking it in until you quickly find your jaw wedged open by the increasing girth. Just the tip of his penis is all that manages to fit inside, but he doesn\'t seem to care. He twirls what little there is around the inside of your mouth, pressing it down against your tongue. Your tongue lashes back, your throat sucking it in as it tries to gulp down the pre that leaks.\r\rThough he can\'t face-fuck you too well, he seems perfectly happy pleasuring the rest of his shaft with a hand. With each stroke of his length, your whole body bobs to keep up with the stiffness that holds your mouth agape. Until he comes to an abrupt halt...\r\rYour throat goes numb as hot seed gushes down it. You don\'t even have time to swallow, it\'s so forceful and so plentiful. Some sprays back out from your nose and even your eyes feel wet and slightly sticky from something that isn\'t tears. Your stomach quickly fills and you feel oh so full... For a moment, your hands can wrap around your belly as it distends to obscene sizes.\r\rHowever, oddly, you soon find yourself sucking in more and more of his length. Your extended belly shrinks as it\'s able to contain more of the stuff, your throat regaining composure. As your body grows out from his hands, he suddenly pulls out from you, spraying the last bit from your face. He quickly hops away as you begin to nearly grow to your normal size, though your head is still oversexed.",True);
      }
      this.doLust(-Math.floor(this.sen / 2),2,1,5);
   }
   if(this.enemyID == 305)
   {
      if((this.gender == 1 || this.gender == 3 && this.percent() > 50) && (this.cockSize * this.cockSizeMod > 140 || this.cockTotal * this.cockSize * this.cockSizeMod > 280))
      {
         this.outputMainText("A smile crosses the bunny-girl\'s face as you fall before her, your cock" + this.plural(1) + " pushing at your " + this.clothesBottom() + ". She ducks down and releases your member" + this.plural(1) + " with one hand while her other disappears between her legs. It quickly reappears as she stands up and hovers over you, her fingers spreading her large snatch wide. Her honey drizzles down around your cock" + this.plural(1) + " with the rest of her swiftly bearing down after it. She lets out a loud sweet moan as she engulfs your length" + this.plural(1) + ". Her velvety puffy folds soon hug the rest of your body, covering you like warm wet blankets, and your face is buried by her clit. It\'s a rather comforting position, somewhat relaxing, that only lasts for a few seconds...\r\rHer strong legs quickly kick up, sending her skyward, before plunging back down upon you again. Her movements are so swift and powerful, your cock" + this.plural(1) + " can\'t tell if " + this.plural(7) + " inside or not, only feeling a constant rubbing against " + this.plural(5) + " sensitive skin. And despite the fervent efforts on your manhood, the bunny-girl still manages to climax first, as she lets out a succulent shout of ecstasy. Her walls clamp around your appendage" + this.plural(1) + ", sucking " + this.plural(9) + " in and tugging " + this.plural(9) + " along with her as her bouncing only grows more enthused.\r\rIt doesn\'t take long until your own arousal begins to build pressure, though you find that pressure to grow much greater than you would have expected. The bunny-girl\'s pussy seems to only be growing tighter and tighter, lifting her from your body as your cock" + this.plural(1) + " push her away. When you finally reach orgasm, she groans loudly as her belly fills and swells. Opening your eyes, you realize you\'re growing larger, almost your full size! She flies off your erection" + this.plural(1) + " with a slick pop before she is really harmed and hops away, leaving you to finish gushing outside of the cave...",True);
      }
      else if(this.udderSize / 2 > 300)
      {
         this.outputMainText("A smile crosses the bunny-girl\'s face as you fall before her. Eyeing your " + this.udderDesc() + " udder through your " + this.clothesTop() + ", an idea seems to dawn upon her and she ducks down to releas your relatively massive mammaries. Then she stands and hovers over you, her fingers spreading her large snatch wide. Her honey drizzles down around your udder with the rest of her swiftly bearing down after it. She lets out a loud sweet moan as she engulfs your " + this.udderDesc() + " bag, letting the fleshy balloon fill her. Her velvety puffy folds soon hug the rest of your body, covering you like warm wet blankets, and your face is buried by her clit. It\'s a rather comforting position, somewhat relaxing, that only lasts for a few seconds...\r\rHer strong legs quickly kick up, sending her skyward, before plunging back down upon you again. Her movements are so swift and powerful, your whole body is lifted by your stretching udder before being slammed back into the ground with the giant little bunny bum crashing back down upon you.",True);
         if(this.udderLactation > 0)
         {
            this.outputMainText(" The supple massage upon your milky mound causes your " + this.teatDesc() + " teats to spray warm milk profusely into her belly.",False);
            this.milkAmount(2);
         }
         this.outputMainText(" Her hands grope about herself in ecstasy at the sensation within, letting out a succulent shout as she climaxes. Her walls clamp around your milk-bag, sucking it in and tugging it along with her as her bouncing only grows more enthused.\r\rYou begin to enjoy the sensation yourself, an outlet for your lust, but quickly realize something is odd as the bunny-girl\'s pussy seems to only be growing tighter and tighter. She slowly lifts from your body as your udder pushes her away, growing larger and larger within her until she\'s hardly straddling your teats! When you finally manage to reach orgasm, her large feet smack against the bag as she realizes how large you\'ve become, propelling herself away. While you come close to returning to your full size with your body still tingling, she dashes away, a hand still jerking at her clit as she goes.",False);
      }
      else if(this.breastSize > 300)
      {
         this.outputMainText("A smile crosses the bunny-girl\'s face as you fall before her. Eyeing your " + this.boobDesc() + " tits through your " + this.clothesTop() + ", an idea seems to dawn upon her and she ducks down to releas your relatively massive mammaries. Then she stands and hovers over you, her fingers spreading her large snatch wide. Her honey drizzles down around your breasts with the rest of her swiftly bearing down after it. She lets out a loud sweet moan as she engulfs your " + this.boobDesc() + " mounds, letting the fleshy balloons fill her. Her velvety puffy folds soon hug the rest of your body, covering you like warm wet blankets, and your face is buried by her clit. It\'s a rather comforting position, somewhat relaxing, that only lasts for a few seconds...\r\rHer strong legs quickly kick up, sending her skyward, before plunging back down upon you again. Her movements are so swift and powerful, your whole body is lifted by your stretching breasts before being slammed back into the ground with the giant little bunny bum crashing back down upon you.",True);
         if(this.lactation > 0)
         {
            this.outputMainText(" The supple massage upon your milky mounds causes your " + this.nipDesc() + "nipples to spray warm milk profusely into her belly.",False);
            this.milkAmount(1);
         }
         this.outputMainText(" Her hands grope about herself in ecstasy at the sensation within, letting out a succulent shout as she climaxes. Her walls clamp around your tits, sucking them in and tugging them along with her as her bouncing only grows more enthused.\r\rYou begin to enjoy the sensation yourself, an outlet for your lust, but quickly realize something is odd as the bunny-girl\'s pussy seems to only be growing tighter and tighter. She slowly lifts from your body as your boobs push her away, growing larger and larger within her until she\'s hardly straddling your nipples! When you finally manage to reach orgasm, her large feet smack against your chest as she realizes how large you\'ve become, propelling herself away. While you come close to returning to your full size with your body still tingling, she dashes away, a hand still jerking at her clit as she goes.",False);
      }
      else
      {
         this.outputMainText("A smile crosses the bunny-girl\'s face as you fall before her. Though a little disappointed at the lack of anything to really have fun with, she still seems to know what to do with you. Your vision is soon obscured as she steps over you, her pussy hovering high above with thick strands of arousal drizzling over your body. Her hips then quickly bear down upon you, wedging you into her supple puffy folds. Her clit pushes into your chest and grinds up towards your face as her legs push her forward. Within moments, her powerful thighs have her running up and down your body with great fervor, nearly pasting you to the ground with all of the slickness.",True);
         if(this.tallness < 80)
         {
            this.outputMainText("\r\rHer speed and lack of cautiousness don\'t quite account for your especially small size and in one swift passing, your " + this.legDesc(10) + " get" + this.legPlural(1) + " caught by the rim of her vaginal entrance... In one pass, you\'re sucked up into her pussy, surrounded by wet warm fleshy walls.\r\rShe seems to be completely unphased, however, and actually increases her pace now that she has something inside of her. Humping at the ground, her fingers wrap around her clit and furiously stroke her. Her palm presses into her belly, squishing you between the tight walls. They rapidly begin to shudder as she approaches her first orgasm, squishing and pressing about your body erotically in the meantime. You soon find yourself coming to and orgasm, your genitals mashed by supple flesh, but also find your confines growing tighter and tighter... You can feel her belly distend as you grow within her, forcing her to come to an abrupt halt. She lifts from the ground, grabbing her clit tightly with a sweet shout, a strong orgasm pushing you out from her loins\r\rWhile you continue to grow to nearly your full height in the midst of your climax, she dashes away.",False);
         }
         else
         {
            this.outputMainText(" She humps you furiously, her speed and strength quickly bringing herself to her first orgasm. Yet, that doesn\'t stop her as she continues to jerk across your body, with even more enthusiasm than before. All the rubbing of soft supple flesh against your genitals every pass makes you begin to feel a little tingly as well.\r\rHowever, just as you\'re coming close to orgasm, you can feel her legs spread more and more, her efforts no longer making it across your entire body. Nearly growing to your full size as you climax, the bunny-girl comes to a halt and dashes away while continuing to jerk her erect clit, her advantage over you lost.",False);
         }
         if(this.cockTotal > 0)
         {
            this.cumAmount();
         }
      }
      this.doLust(-Math.floor(this.sen / 2),2,1,3,4);
   }
   if(this.enemyID == 306)
   {
      this.outputMainText("Pleased with your less-threatening state, she takes her time to tower over your prone body and wraps her tail around your " + this.hipDesc() + " hips and " + this.legDesc(2) + ", holding you still with her strength and leans in to taste her prey...\r\rPulling " + this.pullUD(1) + " your " + this.clothesTop() + ", she licks over the " + this.skinDesc() + " of your belly with her long serpentine tongue. She glides down, constricting her tail in an oscillating fashion to help pull your " + this.clothesBottom() + " " + this.pullUD(2) + " enough to access your",True);
      if(this.cockTotal > 0)
      {
         this.outputMainText(" " + this.cockDesc() + " erection" + this.plural(1) + ". Pleased with what she finds, she caresses " + this.plural(9) + " with her fingers and lavishes the tip" + this.plural(1) + " with her tongue, darting in and out of the urethra" + this.plural(1) + " pleasantly.\r\rQuite satisfied with your flavor, she drags her silk-covered breasts over the rod" + this.plural(1) + ", grinding her body up yours until the sash dangles over your glans. Lifting the cloth, her own awaiting sex spills a clear drop from the pink flesh that runs down through the valley of her fused thighs. Holding you tightly with her tail, she lifts " + this.oneYour(1) + " member" + this.plural(1) + " up and drives herself down to devour it.",False);
         if(this.cockSize * this.cockSizeMod > this.eVagLimit(80))
         {
            this.outputMainText("\r\rMuch larger than the entrance you\'re being forced into, the naga lets out a loud moan. The maw stretches to widen over your girth and you think even her hips unhinge to gobble you whole. The belly-scales bulge as you fill her up and she doesn\'t stop until you\'re completely sheathed inside of her. Her claws dig into your skin and she hisses in delight, her tail \'hugging\' you tighter.",False);
         }
         else
         {
            this.outputMainText("\r\rHer entrance easily takes you all the way to the hilt, yet surprisingly tight despite her size. She hisses happily, her tail pushing your rear up further to engulf more of you, even if it is a slight amount.",False);
         }
         this.outputMainText(" Fully engulfed, the muscular flesh within gnaws around your cock. Then she begins to bounce and grind on top of you, her tail holding you firm, and with your member being tugged and sucked by the velvety maw like a phallic lolipop. In fact, her hungry slit seems to be doing most of the work, as her muscles twist and tenderly gnash the hard toy with such force that you\'re both quickly moaning in ecstasy.\r\rHer plush vulva presses down to your crotch as the first spurts of cum shoot inside of her. Her hands crush your shoulders, her wings spreading out while her back arches in climax. The vigorous pussy helps to suck the spunk right out of you, drinking it into her womb. When your gushing loses its power, her tail slowly begins to unravel around you, flexing from side to side as she tries to rein in her own orgasm.\r\rQuite satisfied with the sexual experience, her slit finally relaxes, dropping you to the ground. Having been the only thing keeping you tied to her, she gropes the sated vulva, dropping her sash over it and slithers away over the dunes.",False);
         this.cumAmount();
      }
      else
      {
         this.outputMainText(" " + this.vulvaDesc() + " cunt" + this.plural(2) + ". Happy with what she finds, she slips a few fingers through your lips, followed by the long tongue.\r\rSatisfied with how swollen and aroused you are, she lifts the sash around her waist to expose her own bulbous vulva. A hungry pink amidst the green scales, she promptly thrusts it against your crotch, mashing your sexes together. Holding you tightly with her tail, she grinds against you, pushing you up from underneath to force you against her even more. Her arms wrap around your neck as she leans down, surrounding your face with her silk-covered bosom and pressing your " + this.skinDesc() + " to her scales.\r\rWith a whole tail of muscle the help her move, her hips gyrate so powerfully against you that it doesn\'t take long before you both reach climax. A concerted moan fills the air while her claws dig into you, her tail \'hugging\' you even more.\r\rHowever, after a few moments of bliss, you\'re allowed to breath. The naga\'s tail unwinds, stretching out as she relishes in the last few moments of orgasm, her wings fanning out and back arching high. Then, she drops her sash with a pleased smile and slithers away over the dunes.",False);
      }
      this.doLust(-Math.floor(this.sen / 2),2,1,2);
   }
   if(this.enemyID == 307)
   {
      this.outputMainText("The Minotaur grunts. \"Good. Could use a fuck!\"\r\rNot exactly a romantic, he lifts you by your " + this.legDesc(8) + " and pulls off your " + this.clothesBottom() + " so it\'s out of the way. He continues to " + this.legVerb(3) + " your " + this.legDesc(2) + ", inspecting what you have before he goes further. Shrugging at what he finds, he waggles his hips so that his big fat bulky cock flops out from behind his loin cloth. Already stiff and willing to go, pre dribbles down from the tip and lubes up your entire crotch, running into all your cracks and crevices.",True);
      if(this.vagTotal > 0 && this.vagLimit() > 72)
      {
         this.outputMainText(" He proceeds to stuff his massive schlong into " + this.oneYour(2) + " cunt" + this.plural(2) + " with a loud slurp, pushing in until he can see his own cock bulge out from your belly.",False);
      }
      else if(this.vagTotal > 0)
      {
         this.outputMainText(" With your cunt" + this.plural(2) + " obviously too small, he proceeds to stuff his massive schlong into your ass with a loud slurping squish.",False);
      }
      else
      {
         this.outputMainText(" With no obvious vagina, he proceeds to stuff his massive schlong into your ass with a loud slurping squish.",False);
      }
      this.outputMainText(" You gasp from the sudden intrusion and gurgle slightly when he begins to pull you up and down his length, plowing through your hole again and again with little regard to what\'s at the other end. The big dork is so selfish with his actions that he quickly begins to blow steam through his bovine nostrils as he snorts, wads of spunk blasting away inside of you. He continues to go on and on until you yourself are eventually climaxing",False);
      if(this.cockTotal > 0)
      {
         this.outputMainText(", your cock" + this.plural(1) + " launching ribbons over yourself while " + this.plural(11) + " bounce" + this.plural(3) + " against you",False);
         this.cumAmount();
      }
      this.outputMainText(".\r\rWith all the flurry of the abrupt orgasm, the Minotaur then lets go of you, making you shiver as you slide down his shaft and plop onto the floor, seed pooling out of your orifice...",False);
      if(this.vagTotal > 0 && this.vagLimit() > 72)
      {
         this.doImpregnate(this.enemyBaby());
      }
      this.doLust(-Math.floor(this.sen / 2),2,2);
   }
   if(this.enemyID == 308)
   {
      this.outputMainText("Seeing you in your helpless state, the girl growls in delight. \"MMM... PREY~,\" Mr. Snuggles drops to the floor as her attention grows more focused upon you. Only then do you notice the large hole between the doll\'s legs, looking a bit moist as though it had been used many times and never able to dry. The reason for its existence also begins to grow quite clear while the freaky little girl paws at her own crotch.\r\rEach time she lifts her skirt with her fondling, you can see a bulge growing and pressing at her small panties. At first it looks like a rather large clitoris, but it continues to sweel rapidly. It bows outward, a meaty length of flesh bunching up within. Eventually, the waistband of the panties gives way, letting the phallic monster loose and lifting her skirt altogether. It coninues to grow all the way up to the little girl\'s chest, thick and throbbing and eager for a good meal. The cock is large and seems even larger compared to the rest of her small body, growing upward from her dripping feminine sex that is exposed from the fallen undies.\r\rShe rubs herself a bit, pleased to have it big and horny again, perfect for impaling you~ She bends down to the floor, scratching at the ground with her nails. Walking on all fours like and animal, her cock thumps up and down against her chest as she creeps toward you, sniffing at you to make sure you\'re ready. She crawls up between your legs, nipping here and there at your " + this.currentClothes() + ", until she finally reaches your chest. She pulls " + this.pullUD(1) + " your " + this.clothesTop() + " with her teeth, exposing your " + this.nipDesc() + " nipples which she promptly bites down upon. Hearing you gasp in slight pain and pleasure, ",True);
      if(this.lactation > 0)
      {
         this.outputMainText("a few drops of your milk rewarding her, ",False);
      }
      this.outputMainText("she finds you to be ready and she rams her large thing into",False);
      if(this.vagTotal > 0)
      {
         this.outputMainText(" " + this.oneYour(2) + " cunt" + this.plural(2) + "",False);
         if(this.vagLimit() < 16)
         {
            this.outputMainText(", stretching you terribly wide and making you yelp in pain",False);
            this.vagChange(4,0);
         }
         else if(this.vagLimit() < 36)
         {
            this.outputMainText(", stretching you much wider to the point that you grunt slightly from the pain",False);
            this.vagChange(2,0);
         }
         else if(this.vagLimit() < 60)
         {
            this.outputMainText(", stretching you to make more room for itself",False);
            this.vagChange(1,0);
         }
         else
         {
            this.outputMainText(", slipping in without much trouble",False);
         }
      }
      else
      {
         this.outputMainText(" your ass, stirring up your insides as she forces her way through",False);
      }
      this.outputMainText(".\r\rThe little girl quickly begins to thrust her small hips, powerfully drilling into you again and again as she keeps her jaw clamped around your nipple, not letting go as she fucks your brains out. Each thrust makes your whole body jerk, her strength far more formidable than her figure might let on. It doesn\'t take long before you feel her spraying her seed inside of you, but that doesn\'t stop her. She continues on and on, bringing you to your own high from the rough treatment, and she doesn\'t stop there...",False);
      if(this.vagTotal > 0)
      {
         this.doImpregnate(this.enemyBaby());
         this.doImpregnate(this.enemyBaby());
      }
      this.doLust(-Math.floor(this.sen / 2),2,2);
   }
   if(this.enemyID == 309)
   {
      this.outputMainText("The succubus grins as you give yourself to her. \"That\'s right, you know what\'s best for you~\"\r\rHigh-heels click on either side of you as the she-devil positions herself over you. She zips her red panties right down the center, making them part to expose her engorged large feminine lips. The things look plump and practically made for intense fucking, which only leads you to be even more anxious for her to take you. However, before you can attempt to lunge at her, she squats down and sits upon your " + this.bellyDesc() + " belly and leans forward to grab your arms up above your head. Pinning you to the floor, her ample bosom engulfs your face, burrowing you inside her cleavage while her hips grind against you, her plush pussy slickening up your " + this.skinDesc() + ".",True);
      if(this.cockTotal > 0 || this.vagTotal > 0 && this.clitSize > 20)
      {
         this.outputMainText("\r\rHer tail wraps around ",False);
         if(this.cockTotal > 0)
         {
            this.outputMainText("" + this.oneYour(1) + " " + this.cockDesc() + " cock" + this.plural(1) + "",False);
         }
         else
         {
            this.outputMainText("" + this.oneYour(2) + " " + this.clitDesc() + " clit" + this.plural(1) + "",False);
         }
         this.outputMainText(" and pulls it up to her awaiting hole. She teases you for a bit, sliding your tip through her thick folds, letting the supple flesh tempt you until your hips are eager to thrust all the way in. Once you\'re groaning and begging for her cunt, she lets your erection slip, plunging her rump back onto your shaft and impaling herself upon you.",False);
         if(this.cockTotal > 0 && this.cockSize * this.cockSizeMod > 48)
         {
            this.outputMainText(" Amazingly, her sensual lips stretch wider and wider, taking in your whole length until you can see your own cock pushing back out against her belly, her body easily taking you in and hugging you tightly with her warmth.",False);
         }
         else if(this.cockTotal < 1 && this.clitSize > 120)
         {
            this.outputMainText(" Amazingly, her sensual lips stretch wider and wider, taking in your whole length until you can see your own clitoris pushing back out against her belly, her body easily taking you in and hugging you tightly with her warmth.",False);
         }
         this.outputMainText(" Her insides feel divine, slurping around you and gently squeezing you in soft perfection. She was definitely made for this...\r\rThe succubus\' round rump begins to bounce upon you, sucking you in and out, nearly lifting you off each time as her tunnel squeezes strongly around you. Totally in control, she proceeds to further show her dominance over you by dancing her tail beneath your " + this.buttDesc() + " tush. The spade at the end folds in upon itself, growing narrow just before driving itself in. You wince at first, her tail burrowing deep into your ass, and you relax as more pleasure overwhelms you from behind. The tail fucks your rear \'pussy\' while the succubus takes care of your rod. Completely restrained and dominated by her, you\'re rapidly growing tingly and eventually going numb as you climax.",False);
         if(this.cockTotal > 0)
         {
            this.cumAmount();
            this.outputMainText(" Your spunk blows within her, filling her insides and drooling back out to your crotch. She doesn\'t seem to retain much of your cum, though.",False);
         }
      }
      else
      {
         this.outputMainText("\r\rShe seems perfectly content with fucking your belly, the stiffening clitoris rumbling against you, while she keeps you planted within her bosom. Completely restrained, you\'re unable to resist as her tail dances between your legs. The spade at the tip folds in upon itself, growing narrow just before it drives into " + this.oneYour(2) + " " + this.vulvaDesc() + " cunt" + this.plural(2) + " and burrowing deep inside to fill you the best it can. You can feel it unfurl within, anchoring itself within your tunnel and spreading you apart. It pumps in and out, making you twitch and squirm beneath you. The woman keeps you pinned, however, and continues to grind against you as she fucks you with her tail. Completely dominated and at her mercy, you\'re rapidly growing tingly and eventually going numb as you climax.",False);
      }
      this.outputMainText("\r\rAs you orgasm, you can feel yourself being drained by more than just the sensual high. You become weaker, smaller, as though any sense of strength is being drained from you while your craving for sex grows stronger, making you more of a slutty bitch that is only good for being fucked. And all the while the vials around the succubus\' belt glow as they fill themselves with what you\'re drained of, sending the she-devil to her own sort of orgasm.\r\r\"Oh god, yes! Give it to me~!\" She siezes upon you, letting your essence flow throughout her and her vials until she\'s full. Then she slowly rises, removing her tail and sliding her fingers through her naked and now rather drippy sex before bringing them to her mouth for a taste. \"Mmm... You were definitely full of \'spunk\' to have gotten this far. I\'m glad I could dine on it~\"",False);
      this.stats(-2,-1,2,0);
      this.submissiveFetish += 0.05;
      this.dominantFetish -= 0.05;
      this.tallness -= 2;
      this.body -= 2;
      this.doLust(-Math.floor(this.sen / 2),2,1,2);
   }
   this.outputMainText("\r\rYou pass out in a puddle of mixed sensual fluids...",False);
   if(this.inDungeon == True)
   {
      this.inDungeon = False
   }
   this.currentState = 1;
   this.hrs = 2 + Math.floor(this.percent() / 20);
   this.exhaustion -= Math.floor(this.percent() / 20);
   this.skipExhaustion = True
   this.doEnd();
}
def SetEnemyStats(enemyHP:int, enemyStr:int, enemyMenta:int, enemySen:int, enemyLib:int, enemyLust:int, enemyGen:int, enemyPref:int, enemyCoin:int, enemySexP:int, enemyItem:int):
   global eHP, eStr, eMent, eSen, eLib, eLust, eGen, ePref, eCoin, eSexP, eItem
   eHP = enemyHP
   eStr = enemyStr
   eMenta = enemyMenta
   eSen = enemySen
   eLib = enemyLib
   eLust = enemyLust
   eGen = enemyGen
   ePref = enemyPref
   eCoin = enemyCoin
   eSexP = enemySexP
   eItem = enemyItem

!def DoeHP(changes:int):
   global eHP, inBag, currentState, eMaxHP
   if ((eHP + changes) <= 0):
      SpecialKOWin()
      OutputMainText("\n" + "\n" + " You win the battle!",False)
      if (inBag == True):
         inBag = False
      currentState = 1
      DoNext()
        this.doListen = function():void
            {
               battleWin();
            }
          eHP += changes
          if (eHP > 0):
               OutputMainText("\n" + "\n" + "Your enemy now seems to be under " + math.ceil(eHP / eMaxHP * 10) * 10 + "% HP.",False)

def DoeLust(changes:int):
   global eGen, eLust, 
   if (eGen == 1):
      if (eLust + changes) > 65 and eLust <= 65:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " smears the pre across its rod, stroking it gently while fighting, majorly distracted.",False)
      elif (eLust + changes) > 40 and eLust <= 40:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " squirms, pre dripping from the tip of its stiffness.",False)
      elif (eLust + changes) > 20 and eLust <= 20:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " shifts a little, an erection clearly beginning to grow.",False)
   if (eGen == 2):
      if (eLust + changes) > 65 and eLust <= 65:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " smears the honey all over as it rubs itself constantly while fighting, majorly distracted.",False)
      elif (eLust + changes) > 40 and eLust <= 40:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " squirms, honey dribbling from its naughty hole.",False)
      elif (eLust + changes) > 20 and eLust <= 20:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " shifts a little, caressing its pussy here and there when it can.",False)
   if (eGen == 3):
      if (eLust + changes) > 65 and eLust <= 65:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " smears the lubricant all over as it rubs and strokes itself constantly while fighting, majorly distracted.",False)
      elif (eLust + changes) > 40 and eLust <= 40:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " squirms, honey dribbling and pre dripping from its aroused genitals.",False)
      elif (eLust + changes) > 20 and eLust <= 20:
         OutputMainText("\n" + "\n" + "The " + EnemyName() + " shifts a little, caressing its pussy here and there when it can while its erection clearly grows.",False)
   eLust += changes

def eDmg(eweapon):
   global sen, eStr, level
   dmgRed = 0
   dmg = 0
   if (sen > 0):
      dmgRed = math.floor((100 - sen) / 2)
   if (dmgRed > level):
      dmgRed = level
   dmg = math.floor(Percent() / eweapon + eStr / 2 - dmgRed)
   if (dmg < 0):
      dmg = 0
   return dmg

def EnemyName():
   global enemyID
   tempStr = "ENEMY NAME ERROR"
   if (enemyID == 101):
      tempStr = "cock-snake"
   if (enemyID == 102):
      tempStr = "desiccating dust devil"
   if (enemyID == 201):
      tempStr = "lone male wolf"
   if (enemyID == 202):
      tempStr = "gay wolf"
   if (enemyID == 301):
      tempStr = "felin in heat"
   if (enemyID == 302):
      tempStr = "drunken equan"
   if (enemyID == 303):
      tempStr = "octopus girl"
   if (enemyID == 304):
      tempStr = "little big bunny-man"
   if (enemyID == 305):
      tempStr = "little big bunny-girl"
   if (enemyID == 306):
      tempStr = "fierce naga"
   if (enemyID == 307):
      tempStr = "Minotaur"
   if (enemyID == 308):
      tempStr = "freaky little girl"
   if (enemyID == 309):
      tempStr = "succubus"
   return tempStr

def EnemyBaseStats():
   global enemyID
   if (enemyID == 101):
      SetEnemyStats(30,16,4,8,0,0,0,4,0,15,202)
   if (enemyID == 102):
      SetEnemyStats(25,0,20,0,50,0,0,0,0,10,231)
   if (enemyID == 201):
      SetEnemyStats(45,22,16,13,11,30,1,2,0,20,203)
   if (enemyID == 202):
      SetEnemyStats(45,26,16,20,11,40,1,1,0,20,203)
   if (enemyID == 301):
      SetEnemyStats(50,12,10,24,30,40,2,4,math.floor(Percent() / 10),25,204)
   if (enemyID == 302):
      SetEnemyStats(60,28,9,18,14,30,1,4,math.floor(Percent() / 10),25,205)
   if (enemyID == 303):
      SetEnemyStats(150,45,30,25,35,20,2,4,0,50,216)
   if (enemyID == 304):
      SetEnemyStats(55,35,30,35,45,10,1,4,math.floor(Percent() / 10),30,222)
   if (enemyID == 305):
      SetEnemyStats(50,35,30,45,35,10,2,4,math.floor(Percent() / 10),30,222)
   if (enemyID == 306):
      SetEnemyStats(100,50,20,40,2,40,2,4,math.floor(Percent() / 5),55,230)
   if (enemyID == 307):
      SetEnemyStats(250,70,20,50,20,10,1,4,math.floor(Percent() / 4 + 5),50,525)
   if (enemyID == 308):
      SetEnemyStats(175,80,40,70,60,10,2,4,math.floor(Percent() / 4 + 5),55,259)
   if (enemyID == 309):
      SetEnemyStats(150,35,80,40,40,0,2,4,math.floor(Percent() / 4 + 5),60,260)

def EnemyBaby():
   global enemyID
   tempNum = 0
   if (enemyID == 201):
      tempNum = 100
   if (enemyID == 302):
      tempNum = 2
   if (enemyID == 304):
      tempNum = 7
   if (enemyID == 307):
      tempNum = 307
   if (enemyID == 308):
      tempNum = 308
   return tempNum

def EnemyAttack():
   global enemyID, edmg, cockTotal, cockSize, cockSizeMod, cockSnakeVenom, clitSize, vagTotal, vagSizeMod, vagSize, milkEngorgement, milkEngorgementLevel, udderEngorgement, udderEngorgementLevel, udders, balls, showBalls, ballSize, butt, vulvaSize, breastSize, udderSize, teatSize, nippleSize, eSen, lib, gender, eLust, _str_, currentState, eHP, hips, hipMod, butt, buttMod, hair, hairLength
   _loc2_ = 0
   _loc1_ = percent()
   if (enemyID == 101):
      if (_loc1_ <= 50):
         OutputMainText("\n"+ "\n" + "The cock-snake whips around, slapping you harshly with its tail and causing a painful welt.",False)
         DoHP(-eDmg(9))
      elif (_loc1_ > 50):
         OutputMainText("\n"+ "\n" + "The cock-snake opens its maw, long thin fangs dripping with venom, and it springs forward at your crotch. Its mouth bites down onto the crotch of your " + ClothesBottom() + ", fangs sinking right into",False)
         if (cockTotal > 0):
            OutputMainText(" " + OneYour(1) + " cock" + Plural(1) + ". It doesn't hurt much, but the venom that spills into you makes you feel strangely aroused and your cock" + Plural(1) + " swell" + Plural(3) + " within your " + ClothesBottom() + ", becoming permanently larger, while the venom continues to make it feel warm...",False)
            DoLust(math.floor(cockSize * cockSizeMod / 5 + Percent() / 10),1)
            CockChange(1,0)
            cockSnakeVenom += 5
         elif (cockTotal < 1) and (vagTotal > 0):
            if (clitSize > 20) and (Percent() <= 5):
               OutputMainText(" " + OneYour(2) + " " + ClitDesc() + " clit" + Plural(2) + ". You feel it swell and shift within your " + ClothesBottom() + ", your lips started to grow quite oddly as well...",False)
               VagChange(0,-1)
               CockChange(math.ceil(clitSize * 5 / 2),1)
               DoLust(math.floor(cockSize * cockSizeMod / 5 + Percent() / 10),1)
            else:
               OutputMainText("  " + OneYour(2) + " " + ClitDesc() + " clit" + Plural(2) + ". It doesn't hurt much, but the venom that spills into you makes you feel strangely aroused as your clit" + Plural(2) + " swell" + Plural(4) + " a little within your " + ClothesBottom() + ", becoming permanently larger, while the venom continues to make it feel warm...",False)
               cockSnakeVenom += 5
               clitSize += 1
               DoLust(math.floor(clitSize / 5 + Percent() / 10),1)
         elif (Percent() <= 40):
            OutputMainText(" your groin. It doesn't hurt much, but you feel a little odd...",False)
            CockChange(1,0)
            DoLust(math.floor(Percent() / 10),1)
         else:
            OutputMainText(" your groin. Though the endeavor proves fruitless, as all its venom manages to do is arouse you a little.",False)
            DoLust(math.floor(Percent() / 20),1)
   if (enemyID == 102):
      if (_loc1_ <= 30):
         OutputMainText("\n"+ "\n" + "The sentient dust devil overcomes you and whooshes about your body, getting sand all over your " + SkinDesc() + " and into some crevices you'd rather not think of, making you very uncomfortable and wearing away some of your sensitivity.",False)
         Stats(0,0,0,-1)
         DoLust(-5,0)
      elif((_loc1_ <= 60) and ((MoistCalc(1) > 11 and cockTotal > 0) or (MoistCalc(2) > 11 and vagTotal > 0) or (milkEngorgement > 200 and milkEngorgementLevel > 1) or (udderEngorgement > 200 and udderEngorgementLevel > 1 and udders == True))):
         if milkEngorgement > 200 and milkEngorgementLevel > 1:
            OutputMainText("\n"+ "\n" + "The whirling sand leaps out at your " + BoobDesc() + " chest and laps up some of the milk that spills from it, sucking it back in and strengthening the devil's endurance.",False)
            DoeHP(5 + math.floor(Percent() / 20))
         elif (udderEngorgement > 200) and (udderEngorgementLevel > 1) and (udders == True):
            OutputMainText("\n"+ "\n" + "The whirling sand leaps out at your " + UdderDesc() + " udder and laps up some of the milk that spills from it, sucking it back in and strengthening the devil's endurance.",False)
            DoeHP(5 + math.floor(Percent() / 20))
         elif (MoistCalc(1) > 11) and (cockTotal > 0):
            OutputMainText("\n"+ "\n" + "The whirling sand across the " + CockDesc() + " bulge in your " + ClothesBottom() + " and laps up some of the slick lubrication that spills from it, sucking the stuff back in and strengthening the devil's endurance.",False)
            DoeHP(5 + math.floor(Percent() / 20))
         elif (MoistCalc(2) > 11) and (vagTotal > 0):
            OutputMainText("\n"+ "\n" + "The whirling sand licks up " + LegWhere(1) + " your " + LegDesc(2) + ", across your " + VulvaDesc() + " groin, and laps up some of the slick lubrication that spills from it, sucking the stuff back in and strengthening the devil's endurance.",False)
            DoeHP(5 + math.floor(Percent() / 20))
      elif (_loc1_ <= 90):
         _loc2_ = Percent()
         if (_loc2_ < 12) and (cockTotal > 0):
            OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and softly drags across your " + CockDesc() + " masculine length" + Plural(1) + ", soaking up some of the moisture from within and causing " + Plural(9) + " to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
            cockSize -= 1
            DoeHP(2)
         elif (_loc2_ < 23) and (balls > 0) and (showBalls == True):
            if (ballSize < 2):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and softly drags across your " + BallDesc() + " scrotum. However, your balls are so puny that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and softly drags across your " + BallDesc() + " scrotum, soaking up some of the moisture from the testicles within and causing them to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               ballSize -= 1
               DoeHP(2)
         elif (_loc2_ < 34):
            if (butt < 1):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and whisks across your " + ButtDesc() + " rump. However, your butt is so flat that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and whisks across your " + ButtDesc() + " rump, soaking up some of the moisture from within and causing it to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               butt -= 1
               DoeHP(2)
         elif (_loc2_ < 45) and (vagTotal > 0):
               if (vulvaSize < 2):
                  OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and slips through your " + VulvaDesc() + " lips. However, your vulva is so tiny that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
               else:
                  OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and slips through your " + VulvaDesc() + " lips, soaking up some of the moisture from within and causing them to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
                  vulvaSize -= 1
                  DoeHP(2)
         elif (_loc2_ < 56) and (vagTotal > 0):
            if (clitSize < 2):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and whirls about your " + ClitDesc() + " clit" + Plural(2) + ". However, your button" + Plural(2) + " " + Plural(14) + " so tiny that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and whirls about your " + ClitDesc() + " clit" + Plural(2) + ", soaking up some of the moisture from within and causing " + Plural(10) + " to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               vulvaSize -= 1
               DoeHP(2)
         elif (_loc2_ < 67):
            if (breastSize < 1):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesTop() + " and gropes about your " + BoobDesc() + " breasts. However, your chest is so flat that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesTop() + " and gropes about your " + BoobDesc() + " breasts, soaking up some of the moisture from within and causing them to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               butt -= 1
               DoeHP(2)
         elif (_loc2_ < 78) and (udders == True):
            if (udderSize < 2):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand blow across your " + UdderDesc() + " udder. However, your milk-bag is so small that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand blow across your " + UdderDesc() + " udder, soaking up some of the moisture from within and causing it to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               butt -= 1
               DoeHP(2)
         elif (_loc2_ < 89) and (udders == True):
            if (teatSize < 3):
               OutputMainText("\n"+ "\n" + "Some of the devil's sand licks across your " + TeatDesc() + " teats. However, your bovine-nipples are so little that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
            else:
               OutputMainText("\n"+ "\n" + "Some of the devil's sand licks across your " + TeatDesc() + " teats, soaking up some of the moisture from within and causing it to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
               butt -= 1
               DoeHP(2)
         elif (nippleSize < 2):
            OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesBottom() + " and brushes over your " + NipDesc() + "nipples. However, your nipples are so little that there is hardly any moisture for the sand to take, doing nothing for the devil.",False)
         else:
            OutputMainText("\n"+ "\n" + "Some of the devil's sand creeps into your " + ClothesTop() + " and brushes over your " + NipDesc() + "nipples, soaking up some of the moisture from within and causing them to shrink a little. The sand then returns to the devil, renewing some of windy essence.",False)
            butt -= 1
            DoeHP(2)
      elif (_loc1_ <= 100):
         _loc2_ = Percent()
         OutputMainText("\n"+ "\n" + "A funnel of sand shoots out from the devil's form, whipping out and latching onto your ",False)
         if (_loc2_ < 12) and (cockTotal > 0):
            OutputMainText("" + CockDesc() + " cock" + Plural(1) + ", siphoning out a lot of moisture and causing " + Plural(9) + " to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
            cockSize -= 5
            DoeHP(10)
         elif (_loc2_ < 23) and (balls > 0) and (showBalls == True):
            if (ballSize < 1):
               OutputMainText("balls. However, they're already so puny that the devil can't siphon any more moisture from them, proving a fruitless attack.",False)
            else:
               OutputMainText("" + BallDesc() + " testicles, siphoning out a lot of moisture and causing them to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               ballSize -= 5
               if (ballSize < 0):
                  ballSize = 0
               DoeHP(10)
         elif (_loc2_ < 34):
            if (butt < 1):
               OutputMainText("butt. However, it's so flat that the devil can't siphon any more moisture from it, proving a fruitless attack.",False)
            else:
               OutputMainText("" + ButtDesc() + " butt, siphoning out a lot of moisture and causing them to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               butt -= 5
               if (butt < 0):
                  butt = 0
               DoeHP(10)
         elif (_loc2_ < 45) and (vagTotal > 0):
            if (vulvaSize < 2):
               OutputMainText("vulva. However, your lips are so thin and tiny that the devil can't siphon any more moisture from them, proving a fruitless attack.",False)
            else:
               OutputMainText("" + VulvaDesc() + " vulva, siphoning out a lot of moisture and causing it to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               vulvaSize -= 5
               if (vulvaSize < 1):
                  vulvaSize = 1
               DoeHP(10)
         elif (_loc2_ < 56) and (vagTotal > 0):
            if (clitSize < 2):
               OutputMainText("clit" + Plural(2) + ". However, your button" + Plural(14) + " so tiny that the devil can't siphon any more moisture from " + Plural(10) + ", proving a fruitless attack.",False)
            else:
               OutputMainText("" + ClitDesc() + " clit" + Plural(2) + ", siphoning out a lot of moisture and causing " + Plural(10) + " to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               clitSize -= 5
               if (clitSize < 1):
                  clitSize = 1
               DoeHP(10)
         elif (_loc2_ < 67):
            if (breastSize < 1):
               OutputMainText("chest. However, it's so flat that the devil can't siphon any more moisture from it, proving a fruitless attack.",False)
            else:
               OutputMainText("" + BoobDesc() + " bust, siphoning out a lot of moisture and causing your breasts to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               breastSize -= 5
               if (breastSize < 0):
                  breastSize = 0
               DoeHP(10)
         elif (_loc2_ < 78) and (udders == True):
            if (udderSize < 2):
               OutputMainText("udder. However, it's so small that the devil can't siphon any more moisture from it, proving a fruitless attack.",False)
            else:
               OutputMainText("" + UdderDesc() + " udder, siphoning out a lot of moisture and causing it to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               udderSize -= 5
               if (udderSize < 1):
                  udderSize = 1
               DoeHP(10)
         elif (_loc2_ < 89) and (udders == True):
            if (teatSize < 3):
               OutputMainText("teats. However, they're so tiny that the devil can't siphon any more moisture from them, proving a fruitless attack.",False)
                  else:
                     OutputMainText("" + TeatDesc() + " teats, siphoning out a lot of moisture and causing them to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
                     teatSize -= 5
                     if (teatSize < 2):
                        teatSize = 2
                     DoeHP(10)
            elif (nippleSize < 2):
               OutputMainText("nipples. However, they're so tiny that the devil can't siphon any more moisture from them, proving a fruitless attack.",False)
            else:
               OutputMainText("" + NipDesc() + "nipples, siphoning out a lot of moisture and causing them to shrink dramatically, restoring a good deal of power to the devil's winds.",False)
               nippleSize -= 5
               if (nippleSize < 1):
                  nippleSize = 1
               DoeHP(10)
      if (enemyID == 201):
         if (_loc1_ > 35) and (_loc1_ <= 50):
               OutputMainText("\n" + "\n" + "The lone wolf leaps at you, taking a large bite with its sharp teeth.",False)
               DoHP(-this.eDmg(6))
            elif (_loc1_ > 50) and (_loc1_ <= 70) and (lust > 15):
               OutputMainText("\n" + "\n" + "His cock beating against his belly with each step, his lust overcomes him for a moment. He runs up to you, jumping onto your " + LegDesc(1) + " and humps wildly, smearing his canine pre up and down your " + LegDesc(1) + ". A small spurt of cum shoots out, the large drop oozing down to your " + LegDesc(10) + ". Not exactly a full climax, but enough for now, the wolf backs off.",False)
               DoLust(lib / 3,1)
               DoeLust(-math.floor(Percent() / 10 + eSen / 2))
            elif (_loc1_ > 70) and (gender != 0) and (gender != 1):
               OutputMainText("\n" + "\n" + "The lone wolf lifts his leg after running up beside you, a bit of urine splashing out onto your " + LegDesc(10) + ". However, he was simply peeing, as the heady smell wafts up to your nose, the pheromones making your body shudder with arousal.",False)
               DoLust(math.floor(Percent() / 10 + lib / 4),1)
            else:
               OutputMainText("\n" + "\n" + "The lone wolf rushes at you, scratching you with its claws.",False)
               DoHP(-eDmg(8))
      if (enemyID == 202): 
         if (_loc1_ > 35) and (_loc1_ <= 50):
            OutputMainText("\n" + "\n" + "The gay wolf leaps at you, taking a large bite with its sharp teeth.",False)
            DoHP(-eDmg(6))
         elif (_loc1_ > 50) and (_loc1_ <= 70) and (lust > 15):
            OutputMainText("\n" + "\n" + "His cock beating against his belly with each step, his lust overcomes him for a moment. He runs up to you, jumping onto your " + LegDesc(1) + " and humps wildly, smearing his canine pre up and down your " + LegDesc(1) + ". A small spurt of cum shoots out, the large drop oozing down to your " + LegDesc(10) + ". Not exactly a full climax, but enough for now, the wolf backs off.",False)
            DoLust(lib / 3,1)
            DoeLust(-math.floor(Percent() / 10 + eSen / 2))
         elif (_loc1_ > 70) and (gender != 0) and (gender != 1):
            OutputMainText("\n" + "\n" + "The gay wolf lifts his leg after running up beside you, a bit of urine splashing out onto your " + LegDesc(10) + ". However, he was simply peeing, as the heady smell wafts up to your nose, the pheromones making your body shudder with arousal.",False)
            DoLust(math.floor(Percent() / 10 + this.lib / 4),1)
         else:
            OutputMainText("\n" + "\n" + "The gay wolf rushes at you, scratching you with its claws.",False)
            DoHP(-eDmg(8))
      if (enemyID == 301):
         if (_loc1_ > 30) and (_loc1_ <= 60) and (eLust > 20):
            OutputMainText("\n" + "\n" + "The horny felin woman comes in close, embracing you as she grinds her slick cunt up and down your " + LegDesc(1) + ". She licks your " + BoobDesc() + " chest while her feminine fluids spill down your thigh. She mewls a little as she has a small climax, alleviating some of her own frustrations while increasing yours in the process.",False)
            DoLust(math.floor(Percent() / 10 + lib / 3),1)
            DoeLust(-math.floor(Percent() / 10 + eSen / 2))
         elif (_loc1_ > 60) and (_loc1_ <= 85) and (eLust > 10):
            OutputMainText("\n" + "\n" + "Utterly thirsting for sex, she turns away from you and gets on all fours. She bends down further while raising her butt high into the air, showing off her lithe body while also showing off the swollen lips that bulge out of either side of her bikini bottom beneath the loin cloth, her tail waving enticingly above. Her sex-driven display makes you a little hot as well.",False)
            DoLust(math.floor(Percent() / 10 + lib / 4),1)
         elif (_loc1_ > 85):
            OutputMainText("\n" + "\n" + "Playfully, she lunges forward and bites you... hard. The pain is quite noticeable, but her giggling afterwards might also arouse you slightly, if you didn't know better...",False)
            DoHP(-eDmg(7))
            DoLust(math.floor(lib / 6),1)
         else:
            OutputMainText("\n" + "\n" + "In her frustration, she claws at you.",False)
            DoHP(-eDmg(10))
      if (enemyID == 302):
         if (_loc1_ > 30) and (_loc1_ <= 60) and (eLust >= 20):
            OutputMainText("\n" + "\n" + "The drunken equan adjusts the giant bulge in his pants, grunting as a large gob of pre smears across his knee and blotches his pants. While not the most erotic display, whatever he's drinking makes the stuff smell extremely enticing...",False)
            DoLust(math.floor(lib / 5),1)
         elif (_loc1_ > 60) and (_loc1_ <= 80):
            OutputMainText("\n" + "\n" + "He lifts his large mug up to his lips, taking a big swig. He burps after downing it, his wounds seemingly less severe than before.",False)
            DoeHP(math.floor(Percent() / 10 + 5))
         elif (_loc1_ > 80):
            OutputMainText("\n" + "\n" + "Stumbling uncontrollably, he plows into you.",False)
            DoHP(-eDmg(7))
         else:
            OutputMainText("\n" + "\n" + "With a hearty laugh, he bonks you on the head with his mug.",False)
            DoHP(-eDmg(9))
      if (enemyID == 303):
         if (_loc1_ > 30) and (_loc1_ <= 55):
            OutputMainText("\n" + "\n" + "With a giggle that makes her breasts quiver, her hands move up to one of the starfish on her chest. She pries it away, her plump nipple popping out with a squirt of slightly pink milk. Giving you a quick wink, her other hand squeezes her breast, shooting a spurt of the stuff onto your body. The sweet-smelling liquid quickly absorbs into your " + SkinDesc() + ", making you grow warm and aroused.",False)
            DoLust(math.floor(20 + Percent() / 10),1)
         elif (_loc1_ > 55) and (_loc1_ <= 80):
            OutputMainText("\n" + "\n" + "One of her tentacles lashes out at you and whips up " + LegWhere(1) + " your " + LegDesc(2) + ". It smarts a bit, but it seems as though she intentionally hit you with the softer underside. The suction cups tear through your " + ClothesBottom() + " and stick to ",False)
            ChangeBot(-1)
            if (vagTotal > 0):
               OutputMainText("the front of your feminine cleft" + Plural(2) + ". You can feel fluid seep from the cups and into your clit" + Plural(2) + ", arousing you further. She twists with a focused expression, tugging again and again at your clit" + Plural(2) + ", trying to wrench herself free after the attack and making your hips buck in turn. By the time she manages to remove her tentacle with a pop, your poor button" + Plural(2) + " feel" + Plural(4) + " a bit larger than before...",False)
               DoLust(math.floor(20 + Percent() / 5),1)
               DoHP(-5)
               clitSize += 1
            elif (vagTotal < 1) and (cockTotal > 0):
               OutputMainText(OneYour(1) + " cock" + Plural(1) + ". You can feel fluid seep from the cups and into your cock" + Plural(2) + ", arousing you further. The tentacle wraps around, tugging again and again at your erection, as through she were masturbating you. Although, from the focused expression on her first, she seems to simply be trying to wrench herself free after the attack. Not that it arouses you any less...",False)
               DoLust(math.floor(10 + Percent() / 10 + lib / 5),1)
            elif (vagTotal < 1) and (cockTotal < 1):
               OutputMainText("your empty groin. You can feel fluid seep from the cups and into your crotch, arousing you further. She twists with a focused expression, tugging again and again at your " + SkinDesc() + ", trying to wrench herself free after the attack. By the time she manages to remove her tentacle with a pop, you spot several hickies from where she had her way with you.",False)
               DoLust(math.floor(10 + Percent() / 10),1)
         elif (_loc1_ > 80) and (attireBot == -1):
            OutputMainText("\n" + "\n" + "She lunges forward at you with a naughty look in her large eyes. She comes intimately close to your face, a long tongue drawing from her mouth and licking you up your cheek. Caught off guard by the sudden sign of affection, you fail to notice her tentacles move in around you.",False)
            if (vagTotal > 0):
               OutputMainText(" Some creep up your " + LegDesc(2) + " and sneak beneath your " + ClothesBottom() + ", sliding through your " + VulvaDesc() + " nether-lips. With a jump, you find your naughty hole" + Plural(2) + " being penetrated. The slick tentacle" + Plural(2) + " thrust in and out slightly, as if gauging your size.",False)
               if (VagLimit() < 20):
                  OutputMainText(" Not quite satisfied, the tentacle" + Plural(2) + " plunge" + Plural(4) + " in deep, stretching you wider than before.",False)
                  VagChange(2,0)
               DoLust(math.floor(lib / 3),1)
            if (cockTotal > 0):
               OutputMainText(" A few wrap around your " + HipDesc() + " hips and pull out your " + CockDesc() + " erection" + Plural(1) + " from your " + ClothesBottom() + ". Your hips buck as she wraps her tentacle" + Plural(1) + " around your shaft" + Plural(1) + ", the slick skin seemingly gauging your girth more by touch than sight.",False)
               DoLust(floor(lib / 3),1)
            OutputMainText(" Her tentacles then wrap around your " + ButtDesc() + " bum with a hug as she leans in, her breasts pressing against your " + BoobDesc() + " chest. She kisses you lightly on the lips, slipping her tongue into your mouth. The sweet taste lingers for a moment, making you shiver in pleasure, before she moves back. Her tentacles then slime through your " + ClothesBottom() + ", leaving your " + ButtDesc() + " ass nice and wet before she gives it a light smack.",False)
            DoLust(math.floor(10),1)
            DoHP(-2)
         else:
            OutputMainText("\n" + "\n" + "One of her eight tentacles whips out and lashs you, leaving a welt. She still smiles, however, as she seems to find the act a little kinky.",False)
            DoHP(-eDmg(4))
      if (enemyID == 304):
         if (_loc1_ > 30) and (_loc1_ <= 55):
            OutputMainText("\n" + "\n" + "With a chuckle, he bounces past you and gives you a quick swat to your " + ButtDesc() + " tush with his large foot in a rather playful manner.",False)
            DoHP(-eDmg(15))
            DoLust(math.floor(Percent() / 10 + lib / 10),1)
         elif (_loc1_ > 55) and (_loc1_ <= 85):
            OutputMainText("\n" + "\n" + "Grabbing his own fuzzy scrotum, his eyes roll up into his head for a moment, biting his lip as he massages the testicles. A bit of pre drips down his fur and lathers around his balls until they're nice and shiny. Enjoying it a little too much, he decides to include you in the fun.",False)
            if (tallness <= 144):
               OutputMainText(" He skips right up to you, towering over you. His legs bend down, lowering his testicles before your face, his knees straddling either side of your head. He presses his relatively enormous balls into your face, practically smothering you with the scent of his nuts while he grinds his hips into your head." + "\n" + "\n" + "Happy with the quick massage, he bounds back, letting you breath again.",False)
            elif (tallness > 144):
               OutputMainText(" His feet spring him forward at you, his legs wrapping around your neck. Sitting on your shoulders, he presses his relatively giant balls into your face, making sure you get a nice whiff while he grinds his hips into your head." + "\n" + "\n" + "Happy with the quick massage, he bounds back, letting you breath again.",False)
            DoLust(math.floor(Percent() / 10 + lib / 5),1)
            DoeLust(10)
         elif (_loc1_ > 85) and (eLust >= 70):
            OutputMainText("\n" + "\n" + "His pointy, carrot-like prick standing from his fuzzy sheath and dripping with pre, he decides to lunge at you.",False)
            if (breastSize >= 100):
               OutputMainText(" He hops up to your " + BoobDesc() + " chest and abruptly turns around. Bending forward, his fluffy tail brushes over your face as his rump slips by. His balls rest upon your head, his sheath pressing into your face. You can feel his slick prick slip into your cleavage, the pointy tip easily drilling a path between your breasts. Within seconds the rabbity fellow begins hopping up and down upon your chest with fervor, squeezing the sides of your tits to crush his cock. You can feel his pulse beat strongly through his sheath and very soon you feel his muscles tense again and again. He lets out a groan as your " + ClothesTop() + " floods with hot spunk, spurting between your flesh with a naughty sound and leaving your front completly swamped in a warm, sticky mess." + "\n" + "\n" + "The whole thing taking less than a minute, he hops off of you, slapping a strand of cum across your face before returning to the battle, his lust somewhat sated.",False)
            elif (butt >= 50):
               OutputMainText(" He hops behind you, leaning down to grab the cheeks of your " + ButtDesc() + " ass and making the cleavage in your " + ClothesBottom() + " much deeper. His slick prick slips into the crack and in seconds he's fervently humping through your rear. Very quickly, he lets out a groan behind you as his cock shudders in your bum, ",False)
               if (tail > 1):
                  OutputMainText("his hand yanking your " + TailDesc() + " high,",False)
               OutputMainText(" while ribbons of spunk flying up your back and over your hair, decorating you in white." + "\n" + "\n" + "The whole thing taking less than a minute, he hops off of you, leaving your back a cum-coated mess before returning to the battle, his lust somewhat sated.",False)
            else:
               OutputMainText(" He aims at your chest, ramming the cock against it. The slick prick slides up your body and past your head, the wet flesh pressing against your cheek. He hugs you tight as he fervently humps you, blurring your vision with the pre that flood down to lubricate. Very quickly, he lets out a groan as the conical member geysers above you, showering you in his hot spunk." + "\n" + "\n" + "The whole thing taking less than a minute, he hops off of you, leaving you a cum-coated mess and a sore cheek before returning to the battle, his lust somewhat sated.",False)
            DoeLust(-30)
            DoLust(math.floor(Percent() / 5 + lib / 6),1)
         else:
            OutputMainText("\n" + "\n" + "He bounces closer and kicks you with one of his big feet, trying to soften you up a little.",False)
            DoHP(-eDmg(8))
      if (enemyID == 305):
         if (_loc1_ > 30) and (_loc1_ <= 55):
            OutputMainText("\n" + "\n" + "With a giggle, she leans down and tickles you, amused by how cute you look. And as she stands back up, her relatively giant breasts thwap you upside the head.",False)
            DoHP(-eDmg(15))
            DoLust(math.floor(Percent() / 10 + lib / 10),1)
            if (sen >= 70):
               OutputMainText("\n" + "\n" + "Your body is so sensitive that her tickling has left you in a laughing fit. She takes the opportunity to 'attack' again.",False)
               EnemyAttack()
         elif (_loc1_ > 55) and (_loc1_ <= 85):
            OutputMainText("\n" + "\n" + "Her thighs press together as her hands reaches down to her naked groin. Biting her lip, she massages her pussy, her eyes closing with muffled whines. A bit of honey drips down her fur and lathers between her thighs until they're nice and shiny. Enjoying it a little too much, she decides to include you in the fun.",False)
            if (tallness <= 144):
               OutputMainText(" She skips right up to you, towering over you. Her legs bend down, lowering her nether-lips to your face, her knees straddling either side of your head. She presses her relatively enormous pussy into your face, her clit rubbing across your cheek, practically smothering you with the scent of her arousal as she grinds her hips into your head." + "\n" + "\n" + "Happy with the quick massage, she bounds back, letting you breath again.",False)
            elif (tallness > 144):
               OutputMainText(" Her feet spring her forward at you, her legs wrapping around your neck. Sitting on your shoulders, she presses her relatively enormous pussy into your face, her clit rubbing across your cheek, practically smothering you with the scent of her arousal as she grinds her hips into your head." + "\n" + "\n" + "Happy with the quick massage, she bounds back, letting you breath again.",False)
            if (hair > 0):
               OutputMainText(" However, the intense humidity and her thighs squeezing you so tightly has left your hair squished up into a mohawk.",False)
               hair = 6
            DoLust(math.floor(Percent() / 10 + lib / 4),1)
            DoeLust(10)
         elif (_loc1_ > 85) and (eLust >= 70):
            OutputMainText("\n" + "\n" + "The bunny-girl's vulva looks rather swollen and red, and her clitoris peeks through the clothes like a very small yet erect penis. Her arousal gets the best of her and she lunges at you.",False)
            if (tallness > 80):
               OutputMainText(" Her legs spread wide and her clit rams into your side, grinding up your ribs. She does her best to clamp her thighs around your body." + "\n" + "\n" + "One hand hugs your head while the other reaches down her backside and past her tail, nearly disappearing into her hungry cunny hole. She rapidly fists herself with loud schlicking sounds, her fem-juice squirting out across your " + LegDesc(2) + " with each pump, while her hips pound again and against against your, powerfully dragging her relatively large clit up and down your " + ClothesTop() + "." + "\n" + "\n" + "Not surprisingly, it doesn't take long before she quivers, one last splash messing your " + ClothesBottom() + ", as she comes to a small orgasm.",False)
            else:
               OutputMainText(" Her legs spread wide as she hops over you, casting you in the shadow of her cunt. You feel a splash across your face as you look up, a strand of her fem-juice falling down as one of her hands spreads her lips open. The other hand pinches her clit, masturbating it fiercely as her rump comes down upon you." + "\n" + "\n" + "Before you know it, you're surrounding by wet soft flesh. Two of her fingers clamp onto your " + LegDesc(2) + ", holding you against the ground while she stands back up, nearly lifting your " + ClothesTop() + " off of your body. You have a small moment to breath before she descends once again, ramming your whole body into her vagina. The hot walls pulse and contract around you, squeezing you tightly. You can hear her furiously stroke her clit and moans escape from above. Then she rises, exposing you to the cooler air. She continues to use her like her own personal dildo, thrusting you in and out again and again until she lets out a howl, a waterfall of slime spilling out around you and forming a puddle where you stand.",False)
            OutputMainText("\n" + "\n" + "She then steps away, her quick climax being enough to satiate herself for a bit. However, she's not quite done with you yet.",False)
            DoeLust(-30)
            DoLust(math.floor(Percent() / 5 + lib / 6),1)
         else:
            OutputMainText("\n" + "\n" + "She bounces closer and kicks you with one of her big feet, trying to soften you up a little.",False)
            DoHP(-eDmg(8))
      if (enemyID == 306):
         if (_loc1_ > 25) and (_loc1_ <= 45):
            OutputMainText("\n" + "\n" + "She lunges forward with open maw and bites you! Though her bite isn\'t exactly the strongest...",False)
            DoHP(-eDmg(10))
         elif (_loc1_ > 45) and (_loc1_ <= 55):
            OutputMainText("\n" + "\n" + "The naga whips around and slams into you with her powerfule tail!",False)
            DoHP(-eDmg(4))
         elif (_loc1_ > 55) and (_loc1_ <= 75):
            OutputMainText("\n" + "\n" + "Her tail coils and springs her into the air, leaping at you with wings outspread and closes them around you, battering your head about and knocking you slightly senseless.",False)
            DoHP(-this.eDmg(7))
            Stats(0,-1,0,0)
         elif (_loc1_ > 75):
            OutputMainText("\n" + "\n" + "The fierce naga twirls about, flourishing her prismatic wings and sending a cloud of sparkly colored dust in your direction. You sneeze a bit as you're forced to breath it in, feeling tingly as its magical effects settle in.",False)
            if (eggLaying > 0) and (vagTotal > 0):
               OutputMainText("\n" + "\n" + "Your womb feels more active, like your next egg is ready to come out faster...",False)
               eggRate += 1
               eggceleratorTime += 10
               eggceleratorDose += 1
               if (eggceleratorDose > (8 + math.ceil(Percent() / 20))):
                  OutputMainText("A little too fast..." + "\n" + "\n" + "Your " + BellyDesc() + " belly lets out a groan as you feel the fresh egg already press against your lips, demanding its way out. In the midst of battle, you squat where you stand, already in the process of laying.",False)
                  if (attireBot == -2) or (attireBot == 5) or (attireBot == 7) or (attireBot == 12) or (attireBot == 13) or (attireBot == 14) or (attireBot == 16) or (attireBot == 25):
                     OutputMainText(" Without time to remove your clothes, you're thankful for your " + ClothesBottom + "'s open crotch as the egg immediately slips through " + OneYour(2) + " " + VulvaDesc() + " opening" + Plural(2) + " and falls to the ground where it shatters and spills its unfertilized contents. Your " + LegDesc(6) + " quake to hold yourself up as another egg is already on its way, with another close behind, firing from your poor cunt in such rapid succession that when you open your mouth to scream in climax, nothing can come out.",False)
                  else:
                     OutputMainText(" Without time to remove your clothes, the egg immediately slips through " + OneYour(2) + " " + VulvaDesc() + " opening" + Plural(2) + " and pushes at your " + ClothesBottom() + ". Just one stuck in the crotch of the fabric isn't too much of an issue, but you grip your quaking " + LegDesc(6) + " as there are plenty more to come. Another egg pushes against the first, expanding your " + ClothesBottom() + " further, their shells cracking slightly against each other, with a third forcing its way through you right behind. After four or five eggs filling your crotch, the cloth finally gives way and tears through, a mess of yolk and shell falling below you. Without any more blockage, the rest of the eggs are free to fly out of your poor cunt and shatter upon the ground, in such rapid succession that when you open your mouth to scream in climax, nothing can come out.",False)
                     ChangeBot(-1)
                  OutputMainText("\n" + "\n" + "It doesn't take long before your " + LegDesc(2) + " finally give" + LegPlural(1) + " out and you fall into the mess, eggs still slipping through your slit. It doesn't take long for your body to burn through its production, your loins crying out in arousal as the laying slows. And once the last egg slips out, the naga licks her lips and closes in on the defenseless prey...",False)
                  DoLust(1000,0)
                  eggceleratorTime = 0
                  eggRate -= eggceleratorDose
                  eggceleratorDose = 0
                  hrs += 1
            elif (PregCheck(0) == True):
               OutputMainText("\n" + "\n" + "Your womb feels warmer and more active as your belly rapidly swells a bit. The gestation of the offspring inside leaps forward, a sudden increase in maturation thanks to the dust.",False)
               i = 0
               while (i < len(pregArray)):
                  if (pregArray[i] == True)
                     pregArray[i + 3] += 10
                  i += 5
            elif (gender != 0):
               OutputMainText("\n" + "\n" + "Your loins feel suddenly more fertile. If you can consider the desire to fuck as being more 'fertile'...",False)
               DoLust(20,1)
            else:
               OutputMainText("\n" + "\n" + "However, the tingle quickly subsides and seems to have had no effect on you. Though you won't be letting the naga know that.",False)
         else:
            OutputMainText("\n" + "\n" + "Lashing out with her claws, the naga slashes at you.",False)
            DoHP(-eDmg(8))
      if (enemyID == 307):
         if (_loc1_ <= 25):
            this.outputMainText("\r\rBANG, ZOOM! Straight to the moon! He slams into your chest with such force that he knocks the breath out of you, giving him time for another attack",False);
            this.doHP(-this.eDmg(6));
            if (currentState == 2):
               EnemyAttack()
         elif (_loc1_ <= 45):
            OutputMainText("\n" + "\n" + "\"Err...\" He stops for a moment, forgetting what he was going to do next... He's not a smart one, that's for sure.",False)
         elif (_loc1_ <= 65) and (eLust > 40):
            OutputMainText("\n" + "\n" + "With his cock growing erect out the side of his loin cloth, he pauses his assault for a moment to take care of himself... right in front of you. His large hand wraps around his thick cock and furiously begins to masturbate, the skin from his shaft dragging over the wide head again and again so quickly that it looks like it's winking. Then, with a grunt, a geyser of spunk sprays in your direction like a firehose.",False)
            if (Percent() > _str_):
               OutputMainText(" It hits you with such force that you're blasted back against the wall and lose your breath for a moment, giving the Minotaur a chance for a followup attack while you catch your breath and wipe off some of the heady thick spooge.",False)
               DoLust(math.floor(eLust / 2),1)
               eLust -= 20
               if (currentState == 2):
                  EnemyAttack()
            else:
               OutputMainText(" The spooge splatters all over you and the heady scent fills your nostrils...",False)
               DoLust(math.floor(eLust / 2),1)
               eLust -= 20
         else:
            OutputMainText("\n" + "\n" + "POW! He punches you right in the kisser.",False)
            DoHP(-eDmg(8))
      if (enemyID == 308):
         if (_loc1_ <= 23):
            OutputMainText("\n" + "\n" + "Her schizophrenic bloodlust subsides for a moment as she looks down. \"Oh no! My shoe came undone!\"" + "\n" + "\n" + "She turns away from you, acting as though not seeing you means you're not there, and she proceeds to bend over at the hip so she can reach down to fix her shoe. Inevitably, her skirt rises, showing off the backside of her panties. Despite the big cute looking Minotaur face embroided on the back, the fabric sinks into her cheeks and outlines her tight little rump so perfectly. You can't help but gaze at it until she twirls back around to continue with the battle.",False)
            DoLust(math.floor((Percent() / 10) + (lib / 4)),1)
         elif (_loc1_ <= 46):
            OutputMainText("\n" + "\n" + "She coos... or snarls? Either way, you find her sinking her teeth into your " + SkinDesc() + ", making you yelp a little in turn. And as soon as she lets go, she is suddenly much more timid, saying \"Aww, I'm sorry... I'll kiss your boo-boo and make it better...\". She proceeds to lick the wound she just cause, kissing it rather... sensually.",False)
            DoHP(-eDmg(4))
            DoLust(math.floor((Percent() / 10) + (sen / 5)),1)
         elif (_loc1_ > 46) and (_loc1_ <= 61) and (eHP < 85):
            OutputMainText("\n" + "\n" + "\"YOU THINK YOU CAN HURT ME?! ATTACK, MR. SNUGGLES!\"" + "\n" + "\n" + "Mr. Snuggles comes flying at you as she swing him around by his leg. The doll hits you with a surprising amount of force - extremely hard and heavy - and you lose your breath for a moment. You could swear the thing must be full of heavy metal and it's almost amazing a girl her size could even lift such a thing...",False)
            DoHP(-eDmg(2))
         elif (_loc1_ > 61) and (_loc1_ <= 76) and (eLust > 50):
            OutputMainText("\n" + "\n" + "\"Mmm...\" The little girl actually seems like a little girl again as she holds her dolly close. Then a hand sinks down beneath her skirt. She lifts the frilly thing as she grabs at her crotch, exposing her panties and pulling them up through her slit, giving you a good view of her crevices. \"It's so tingly down there...\"",False)
            DoLust((Percent() / 10) + (lib / 4),1)
         else:
            OutputMainText("\n" + "\n" + "With a growl, she jumps in and slashes at you with her claw-like fingernails. She lets out a gutteral giggle when she connects, licking her nails clean right away.",False)
            DoHP(-eDmg(3))
      if (enemyID == 309):
         if (_loc1_ <= 25):
            if (breastSize < 8):
               OutputMainText("\n" + "\n" + "\"Hmm... Your chest isn't quite up to par~\" Her wings flutter as she darts about and you feel her spaded tail graze across your " + BoobDesc() + " chest. When she stops back where she started, one of her vials glows slightly and she smiles. You look down to see why and notice you chest has become more swollen, jiggling slightly!",False)
               BoobChange(1)
            elif ((hips * hipMod) < 16):
               OutputMainText("\n" + "\n" + "\"Those hips need to match your tits more, give you some more curves~\" She steps up and her tail wraps around your " + HipDesc() + " hips before pulling back. As she steps back, one of her vials glows and she smiles. You wince as you feel your " + ClothesBottom() + " grow tighter, your hips stretching out furhter than before!",False)
               hips += 1
            elif ((butt * buttMod) < 15):
               OutputMainText("\n" + "\n" + "\"Mmm... You backside needs some more attention, doesn't it?\" She rushes around behind you, the spade of her tail giving your " + ButtDesc() + " rear a quick spank. One of her vials glows and she smiles as your rump presses against your " + ClothesBottom() + ", jiggling slightly as you stand.",False)
               butt += 1
            elif (cockTotal > 0):
               OutputMainText("\n" + "\n" + "\"And this thing you've got here just totally ruins your womanly figure now. We should take care of that~\" The woman steps behind you but her tail reaches around to your " + CockDesc() + " bulge, cradling it with the spade and giving it a shake. You can feel your cock" + Plural(1) + " shrink slightly within your " + ClothesBottom() + " while one of her vials glow.",False)
               if (cockSize > 1):
                  CockChange(-1,0)
               else:
                  CockChange(-1,0)
                  VagChange(0,1)
                  OutputMainText("\n" + "\n" + "\"Now that's my girl~ Who needs all those manly features when you can be a slut~?\" She seems quite pleased with the change.",False)
            else:
               OutputMainText("\n" + "\n" + "\"You\'re such a good girl~ Don't you just want to use that body for all sorts of kinky things~?\" ",False)
               if (Percent() < ment):
                  this.outputMainText("The woman tries to tempt you, but you manage to resist.",False)
               else:
                  OutputMainText(" You feel yourself falling to the woman's temptations, your arousal growing stronger with the thoughts of what you could do.",False)
                  Stats(0,0,1,0)
         elif (_loc1_ <= 45):
            _loc2_ = Percent()
            if (_loc2_ <= 20) and (hair > 0) and (HairstyleLength(hair) == True) and (hairLength < 10):
               OutputMainText("\n" + "\n" + "\"You know what helps make a slut look good?\" She steps up behind you and runs her fingers through your " + HairDesc() + " hair. A tingly sensation envelops your skull",False)
               if (Percent() < ment):
                  OutputMainText(", but you manage to resist and interrupt her efforts.",False)
               else:
                  OutputMainText(" and your hair begins to grow longer, a sort of kinky sensation overcoming you as you swish it about. The succubus steps back, a vial on her belt glowing from her success.",False)
                  hairLength += 2
                  DoLust(15,1)
            elif (_loc2_ <= 40):
               OutputMainText("\n" + "\n" + "\"A good slut needs some big jiggly tits, don't you think?\" The woman steps up behind you, her hands wrapping around to grope your " + BoobDesc() + " chest. A tingly sensation spreads throughout it",False)
               if (Percent() < ment):
                  OutputMainText(", but you manage to resist and interrupt her efforts.",False)
               else:
                  OutputMainText(" and your breasts swell within your " + ClothesTop() + ", a sort of kinky sensation overcoming you as you absentmindedly bounce their greater size. The succubus steps back, a vial on her belt glowing from her success.",False)
                  BoobChange(2)
                  DoLust(15,1)
            elif (_loc2_ <= 60) and (cockTotal > 0) and (cockSize > 2):
               OutputMainText("\n" + "\n" + "\"A good girl doesn't need such garish things.\" She steps up to you and blatantly grabs the " + CockDesc() + " bulge in your " + ClothesBottom() + ". You feel it tingly in a rather pleasant way",False)
               if (Percent() < ment):
                  OutputMainText(", but you manage to resist and interrupt her efforts.",False)
               else:
                  OutputMainText(" and you succumb to the pleasure while your cock" + Plural(1) + " shrink" + Plural(3) + " in her grasp. The succubus steps back, a vial on her belt glowing from her success.",False)
                  CockChange(-2,0)
                  DoLust(15,1)
            else if(_loc2_ <= 80)
               OutputMainText("\n" + "\n" + "\"You know a slut is good for the taking when her hips are nice and wide, made to be used~\" The woman steps up and places her hands upon your hips as though preparing to dance with you. A tingly sensation spreads throughout them",False)
               if (Percent() < ment):
                  OutputMainText(", but you manage to resist and interrupt her efforts.",False)
               else:
                  OutputMainText(" and your hips stretch outward, pushing at your " + ClothesBottom() + ", a sort of kinky sensation overcoming you as you can't help but sway your girthy loins. The succubus steps back, a vial on her belt glowing from her success.",False)
                  hips += 2
                  DoLust(15,1)
            else:
               OutputMainText("\n" + "\n" + "\"A nice big rump is perfect for spanking a naughty slut~\" She steps behind you and gives you a quick slap across your " + ButtDesc() + " rear and grabs the cheeks. A tingly sensation spreads throughout them",False)
               if (Percent() < ment):
                  OutputMainText(", but you manage to resist and interrupt her efforts.",False)
               else:
                  OutputMainText(" and your ass swells in her grasping, stretching your " + ClothesBottom() + " while a sort of kinky sensation overcomes you and you can't help but shake your booty a little. The succubus steps back, a vial on her belt glowing from her success.",False)
                  butt += 2
                  DoLust(15,1)
         elif (_loc1_ <= 65):
            OutputMainText("\n" + "\n" + "She stops for a moment and one hand dips into her cleavage while the other slinks between her thighs. Her tail curls like a finger hithering you closer as she rocks her hips and jounces her bosom. \"This is so much fun, don't you think~?\" She tries to tempt you with a rather sensual tone.",False)
            DoLust(math.floor(lib / 3),1)
         elif (_loc1_ <= 85) and (eHP < 80):
            OutputMainText("\n" + "\n" + "Feeling a bit winded from your attacks, she plucks a vial from her belt and brings it to her lips. As she drinks from it, she seems to be reinvigorated.",False)
            DoeHP(math.floor((Percent() / 5) + 10))
         else:
            OutputMainText("\n" + "\n" + "The whip snaps across the room and strikes you. \"Just need to keep you awake, hun~\"",False)
            DoHP(-eDmg(15))

!def DoStatus(param1:int):
   global hrs, pregnancyTime, pregArray, pregTimeMod, pregRate
   _loc2_ = 0
   _loc3_ = 0
   _loc4_ = 0
   OutputMainText("Afterwards...",True)
   hrs = 0
   pregnancyTime = 0
   _loc2_ = 0
   i = 0
   while (i < len(pregArray)):
      if (pregArray[i] == True):
         if (pregArray[i + 3] + math.ceil(param1 * pregRate) > pregArray[i + 2] + pregTimeMod):
            pregArray[i] = False
            pregArray[i + 3] = 0
            DoBirth(pregArray[i + 1], pregArray[i + 4], _loc2_)
            _loc2_ += 1
         else:
            if (pregArray[i + 1] != 503):
               pregArray[i + 3] += math.ceil(param1 * pregRate)
            pregnancyTime += pregArray[i + 3]
      i += 5
   if(this.pregnancyTime >= 80 && this.pregnancyTime < 140 && this.pregStatus < 1)
   {
      this.pregStatus = 1;
      this.lactChange(1,10);
      this.lactChange(2,10);
      this.boobChange(1);
      this.udderChange(1);
      if(this.lactation - 50 <= 0)
      {
         this.outputMainText(" Your body must be getting ready for the baby that\'s growing inside of you. Even your breasts feel fuller...",False);
      }
      else
      {
         this.outputMainText("\r\rYour breasts are producing even more milk than normal. They\'re even a little fuller... Your body must be getting ready for the baby that\'s growing inside of you.",False);
      }
   }
   else if(this.pregnancyTime >= 140 && this.pregnancyTime < 210 && this.pregStatus < 2)
   {
      this.pregStatus = 2;
      this.lactChange(1,20);
      this.lactChange(2,20);
      this.boobChange(2);
      this.udderChange(2);
      this.outputMainText("\r\rYour breasts feel sore from the all the milky swelling. They\'ve grown three cup sizes since you\'ve gotten pregnant and dribble more and more!",False);
   }
   else if(this.pregnancyTime >= 210 && this.pregStatus < 3)
   {
      this.pregStatus = 3;
      this.lactChange(1,50);
      this.lactChange(2,50);
      this.boobChange(1);
      this.udderChange(1);
      this.outputMainText("\r\rYour breasts have slowed in their pregnant swelling. They should definitely be prepared for whatever you might give birth to... you hope.",False);
   }
   if(this.pregnancyTime < 80 && this.pregStatus > 0)
   {
      this.pregStatus = 0;
   }
   if(this.eggLaying > 0 && this.vagTotal > 0 && this.pregCheck(1) && param1 > 0)
   {
      _loc3_ = param1 + 2 * this.eggRate;
      _loc4_ = 0;
      while(_loc3_ > 0)
      {
         --this.eggTime;
         _loc3_--;
         if(this.eggTime <= 0)
         {
            _loc4_++;
            this.eggTime = this.eggMaxTime;
         }
      }
      if(_loc4_ == 1)
      {
         if(this.percent() < this.ment / 2 + 20)
         {
            if(this.eggType == 0)
            {
               this.outputMainText("\r\rHaving missed your body\'s signals, you suddenly double over and begin to groan as you feel something press against the inside of " + this.oneYour(2) + " " + this.vulvaDesc() + " nether-lips. Your thighs clench to hold it back, but the smooth slick object spreads your cunt wide, squeezing out into your " + this.clothesBottom() + " where it cracks and spreads into a wet mess.\r\rYolky goop squishing in your groin with little bits of white shell jabbing you here and there, you take a moment to pull out the broken unfertilized egg and attempt to clean up after yourself...",False);
            }
            if(this.eggType == 1)
            {
               this.outputMainText("\r\rHaving missed your body\'s signals, you suddenly double over and begin to groan as you feel something press against the inside of " + this.oneYour(2) + " " + this.vulvaDesc() + " nether-lips. Your thighs clench to hold it back, but the smooth slick object spreads your cunt wide, squeezing out into your " + this.clothesBottom() + " where it squishes and spreads into a wet mess.\r\rSlimy goop squishing in your groin with little bits of squishy shell sliding about, you take a moment to pull out the broken unfertilized bug egg and attempt to clean up after yourself...",False);
            }
         }
         else
         {
            if(this.eggType == 0)
            {
               this.outputMainText("\r\rYou pause for a moment as you feel something drop within your womb. Groaning a bit, you " + this.legVerb(1) + " your " + this.legDesc(2) + " in preparation, a hand pushing your " + this.clothesBottom() + " aside and helping spread " + this.vulvaDesc() + " nether-lips. You hold your breath and with a quick push, you feel " + this.oneYour(2) + " cunt" + this.plural(2) + " stretch wide. Your fingers feel the hard shell beginning to crown and with a grunt it slips out into your palm.\r\rYou take a moment to gather yourself, slipping the smooth, round egg through your slit, still wet from your inner-slime, before you finally pull it out from your " + this.clothesBottom() + ". Drying it off, you have something to snack on later.",False);
               this.itemAdd(219);
            }
            if(this.eggType == 1)
            {
               this.outputMainText("\r\rYou pause for a moment as you feel something drop within your womb. Groaning a bit, you " + this.legVerb(1) + " your " + this.legDesc(2) + " in preparation, a hand pushing your " + this.clothesBottom() + " aside and helping spread " + this.vulvaDesc() + " nether-lips. You hold your breath and with a quick push, you feel " + this.oneYour(2) + " cunt" + this.plural(2) + " stretch wide. Your fingers feel the soft shell beginning to crown and with a grunt it slips out into your palm.\r\rYou take a moment to gather yourself, slipping the squishy round egg through your slit, still wet from your inner-slime, before you finally pull it out from your " + this.clothesBottom() + ". Drying it off, you have something to snack on later.",False);
               this.itemAdd(253);
            }
         }
      }
      if(_loc4_ > 1)
      {
         if(this.percent() < this.ment / 2 + 20 - 4 * _loc4_)
         {
            if(this.eggType == 0)
            {
               this.outputMainText("\r\rHaving been distracted and unable to lay for such a long time, you are unprepared for the buildup of ovid objects within your womb. You double over as you feel them crowd against the inside of your " + this.vulvaDesc() + " nether-lips, your thighs clenching to hold them back, but the smooth slick objects press on through anyways. They squeeze out into your " + this.clothesBottom() + " where they pile up and crack, spreading into a wet mess.\r\rYolky goop squishing in your groin with little bits of white shell jabbing you here and there, you take a moment to pull out the broken unfertilized eggs and attempt to clean up after yourself...",False);
            }
            if(this.eggType == 1)
            {
               this.outputMainText("\r\rHaving been distracted and unable to lay for such a long time, you are unprepared for the buildup of spherical objects within your womb. You double over as you feel them crowd against the inside of your " + this.vulvaDesc() + " nether-lips, your thighs clenching to hold them back, but the smooth slick objects press on through anyways. They squeeze out into your " + this.clothesBottom() + " where they pile up and squish, spreading into a wet mess.\r\rSlimy goop squishing in your groin with little bits of squishy shell sliding about, you take a moment to pull out the broken unfertilized bug eggs and attempt to clean up after yourself...",False);
            }
         }
         else
         {
            if(this.eggType == 0)
            {
               this.outputMainText("\r\rHaving been distracted and unable to lay for such a long time, you pause for a moment as you prepare for the objects that have built up within your womb. Groaning a bit, you " + this.legVerb(1) + " your " + this.legDesc(2) + " in preparation, a hand pushing your " + this.clothesBottom() + " aside and helping spread " + this.vulvaDesc() + " nether-lips. You hold your breath and with a quick push, you feel " + this.oneYour(2) + " cunt" + this.plural(2) + " stretch wide. Your fingers feel the hard shell beginning to crown and with a grunt it slips out into your palm. You place it down beside you and continue to lay until you are completely empty.\r\rYou take a moment to gather yourself, slipping the last smooth, round egg through your slit, still wet from your inner-slime, before you finally pull it out from your " + this.clothesBottom() + ". Drying them all off, you have some snacks for later.",False);
               while(_loc4_ > 0)
               {
                  this.itemAdd(219);
                  _loc4_--;
               }
            }
            if(this.eggType == 1)
            {
               this.outputMainText("\r\rHaving been distracted and unable to lay for such a long time, you pause for a moment as you prepare for the objects that have built up within your womb. Groaning a bit, you " + this.legVerb(1) + " your " + this.legDesc(2) + " in preparation, a hand pushing your " + this.clothesBottom() + " aside and helping spread " + this.vulvaDesc() + " nether-lips. You hold your breath and with a quick push, you feel " + this.oneYour(2) + " cunt" + this.plural(2) + " stretch wide. Your fingers feel the soft shell beginning to crown and with a grunt it slips out into your palm. You place it down beside you and continue to lay until you are completely empty.\r\rYou take a moment to gather yourself, slipping the last squishy round egg through your slit, still wet from your inner-slime, before you finally pull it out from your " + this.clothesBottom() + ". Drying them all off, you have some snacks for later.",False);
               while(_loc4_ > 0)
               {
                  this.itemAdd(253);
                  _loc4_--;
               }
            }
         }
      }
   }
   if(this.cockSnakePreg > 0)
   {
      if(this.cockSnakePreg - param1 <= 0)
      {
         _loc2_ = 0;
         this.outputMainText("\r\rYou feel a sudden squirming within your womb. You brace yourself as you feel the cock-snake within slither its way through your passage. Your " + this.clothesBottom() + " becomes drenched by your feminine lubricant as a bunch of it splashes out, the phallic head of the snake breaching your " + this.vulvaDesc() + " lips. Its body constantly drags over your sensitive flesh as it flees what is about to come, making you shudder in mild orgasm as the creature descends down your " + this.legDesc(1) + ". You gasp and regain yourself, the snake slithering away. It must have been too hungry too survive inside you any longer...",False);
         this.cockSnakePreg = 0;
         this.i = 0;
         while(this.i < len(pregArray))
         {
            if(this.pregArray[this.i + 1] == 503)
            {
               this.pregArray[this.i] = False
               this.pregArray[this.i + 3] = 0;
               _loc2_++;
               if(_loc2_ == 2)
               {
                  this.outputMainText("\r\rAnd it\'s not the first; you shudder again as another snake in another womb escapes out from your " + this.clothesBottom() + " and down your " + this.legDesc(1) + ", giving up on you like the first.",False);
               }
               if(_loc2_ == 3)
               {
                  this.outputMainText("\r\rFollowed by another...",False);
               }
               if(_loc2_ > 3)
               {
                  this.outputMainText("\r\rAnd another...",False);
               }
               this.doLust(-Math.floor(this.sen / 4),2,2);
            }
            this.i += 5;
         }
      }
      else if(this.cockSnakePreg - param1 <= 10)
      {
         this.outputMainText("\r\rYour " + this.bellyDesc() + " belly twists and jiggles about as the snake inside boinks about your womb. It seems to know all the best places to touch, greatly arousing you over time with its squirming, teasing you much more vigorously to make you thirst for cum down below...",False);
         this.cockSnakePreg -= param1;
         this.doLust(5 * param1,1);
      }
      else if(this.cockSnakePreg - param1 <= 30)
      {
         this.outputMainText("\r\rYour " + this.bellyDesc() + " belly shudders as the snake inside clamors for cum, arousing you over time with its twisting and squirming, helping your passage grow sensitive and thirsty for penetration...",False);
         this.cockSnakePreg -= param1;
         this.doLust(3 * param1,1);
      }
      else if(this.cockSnakePreg - param1 <= 50)
      {
         this.outputMainText("\r\rYour " + this.bellyDesc() + " belly wiggles a bit as the snake inside tries to tease your passage, making you thirsty for cock below and arousing you over time...",False);
         this.cockSnakePreg -= param1;
         this.doLust(param1,1);
      }
      else
      {
         this.cockSnakePreg -= param1;
      }
   }
   if(this.malonRep == 4)
   {
      this.malonPreg += param1;
   }
   if(this.lilaPreg + param1 > 40 && this.lilaPreg <= 40 && this.lilaPreg > 0)
   {
      ++this.lilaMilk;
      if(this.lilaMilk > 19)
      {
         this.lilaMilk = 19;
      }
   }
   if(this.lilaPreg + param1 > 80 && this.lilaPreg <= 80 && this.lilaPreg > 0)
   {
      this.lilaMilk += 2;
      if(this.lilaMilk > 19)
      {
         this.lilaMilk = 19;
      }
   }
   if(this.lilaPreg > 0)
   {
      this.lilaPreg += param1;
   }
   if(this.silPreg > 0 && this.silRep < 5 && param1 > 0)
   {
      this.silPreg += param1 + 2 * this.silRate;
      _loc3_ = param1 + this.silRate;
      if(this.silPreg > 30 && this.silTied == False)
      {
         while(_loc3_ > 0)
         {
            --this.silLay;
            _loc3_--;
            if(this.silLay <= 0)
            {
               this.silPreg -= 10;
               this.silLay = 10;
            }
         }
      }
   }
   else if(this.silPreg > 0 && this.silRep == 5 && param1 > 0 && this.silGrowthTime <= 360 && this.silPreg < 10000)
   {
      this.silPreg += param1 + 2 * this.silRate;
      this.silGrowthTime += param1;
   }
   if(this.heat > 0 && this.vagTotal > 0 && !this.pregCheck(0))
   {
      if(this.heatTime >= 0 && this.heatTime - param1 < 0)
      {
         this.outputMainText("\r\rYour crotch feels hot and tingly, your face becoming flush. Thoughts of sex, being pounded and filled with seed until your womb has been sufficiently impregnated, permeate your mind and makes you greatly aroused. You\'re feeling especially fertile and extremely lustful as you go into heat...",False);
         this.pregChanceMod += 15;
         this.statsMod(0,-5,10,0);
         this.doLust(15,0);
         this.vagMoistMod += 3;
         this.heatTime = -24;
      }
      else if(this.heatTime < 0 && this.heatTime + param1 >= 0)
      {
         this.outputMainText("\r\rYou breath a sigh of relief as the heat finally passes, your body calming and no longer needing to reproduce as much.",False);
         this.pregChanceMod -= 15;
         this.statsMod(0,5,-10,0);
         this.vagMoistMod -= 3;
         this.heatTime = this.heatMaxTime;
      }
      else if(this.heatTime > 0 && this.heatTime - param1 > 0)
      {
         this.heatTime -= param1;
      }
      else if(this.heatTime < 0 && this.heatTime + param1 < 0)
      {
         this.heatTime += param1;
      }
   }
   else if(this.heat > 0 && this.heatTime < 0 && this.pregCheck(0))
   {
      this.outputMainText("\r\rYou breath a sigh of relief as the heat passes, your body calming and no longer needing to reproduce as much. However, it seems to have ended a bit early...",False);
      this.pregChanceMod -= 15;
      this.statsMod(0,5,-10,0);
      this.vagMoistMod -= 3;
      this.heatTime = this.heatMaxTime;
   }
   else if(this.heat > 0 && this.heatTime != this.heatMaxTime && this.pregCheck(0))
   {
      this.heatTime = this.heatMaxTime;
   }
   else if(this.heat < 1 && this.heatTime > 0)
   {
      this.heatMaxTime = 0;
      this.heatTime = 0;
   }
   else if((this.heat < 1 || this.vagTotal < 1) && this.heatTime < 0)
   {
      this.pregChanceMod -= 15;
      this.statsMod(0,5,-10,0);
      this.vagMoistMod -= 3;
      this.heatMaxTime = 0;
      this.heatTime = 0;
   }
   if(this.lactation > 0)
   {
      if(this.milkEngorgementLevel < 3 && this.milkEngorgement + (this.lactation + this.milkMod) * param1 > ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2 && this.milkEngorgement <= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2)
      {
         this.outputMainText("\r\rPulling " + this.pullUD(1) + " your " + this.clothesTop() + ", streams of milk shoot from your aching tits. Your nipples dribble uncontrollably, occasionally spitting the milk quite far. Your mammaries are producing far more milk than your breasts can hold and will continue to waste breastmilk until you drain them or they dry up from lack of demand.",False);
         if(this.milkEngorgementLevel < 1)
         {
            this.boobChange(3);
         }
         else if(this.milkEngorgementLevel < 2)
         {
            this.boobChange(2);
         }
         else
         {
            this.boobChange(1);
         }
         ++this.milkEngorgementLevel;
      }
      else if(this.milkEngorgementLevel < 2 && this.milkEngorgement + (this.lactation + this.milkMod) * param1 > ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5 && this.milkEngorgement <= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5)
      {
         this.outputMainText("\r\rYour " + this.clothesTop() + " is soaked in front. Milk dribbles from your nipples almost constantly, your breasts slightly overfull and engorged. The abundant supply is getting to be a little more than the plush mounds can handle.",False);
         if(this.milkEngorgementLevel < 1)
         {
            this.boobChange(2);
         }
         else
         {
            this.boobChange(1);
         }
         ++this.milkEngorgementLevel;
      }
      else if(this.milkEngorgementLevel < 1 && this.milkEngorgement + (this.lactation + this.milkMod) * param1 > (this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap && this.milkEngorgement <= (this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap)
      {
         this.outputMainText("\r\rYour " + this.clothesTop() + " feels moist around your nipples. Your breasts feel slightly swollen as the wet blotches spread, milk leaking from your laden mammaries. It\'s a sign that they are nice and full for a good breastfeeding, or whatever your kinky mind has for them.",False);
         ++this.milkEngorgementLevel;
         this.boobChange(1);
      }
      this.milkEngorgement += (this.lactation + this.milkMod) * param1;
   }
   if(this.udderLactation > 0 && this.udders == True)
   {
      if(this.udderEngorgementLevel < 3 && this.udderEngorgement + (this.udderLactation + this.milkMod) * param1 > ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2 && this.udderEngorgement <= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2)
      {
         this.outputMainText("\r\rJets of milk shoot from the teats of your udder with each step. When standing still, it dribbles constantly, your udder so big and sore and especially sensitive from being stretched and heavy with engorgement. The production of milk far exceeds its capacities, wasting milk until you drain it or it dries up.",False);
         if(this.udderEngorgementLevel < 1)
         {
            this.udderChange(5);
         }
         else if(this.udderEngorgementLevel == 1)
         {
            this.udderChange(3);
         }
         ++this.udderEngorgementLevel;
         this.udderChange(3);
      }
      else if(this.udderEngorgementLevel < 2 && this.udderEngorgement + (this.udderLactation + this.milkMod) * param1 > ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5 && this.udderEngorgement <= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5)
      {
         this.outputMainText("\r\rYour " + this.clothesBottom() + " is soaked in front. Milk dribbles from your teats almost constantly, too much to retain. The abundant supply seems to be overwhelming the lack of demand...",False);
         if(this.udderEngorgementLevel < 1)
         {
            this.udderChange(2);
         }
         ++this.udderEngorgementLevel;
         this.udderChange(3);
      }
      else if(this.udderEngorgementLevel < 1 && this.udderEngorgement + (this.udderLactation + this.milkMod) * param1 > (this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap && this.udderEngorgement <= (this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap)
      {
         this.outputMainText("\r\rYour " + this.clothesBottom() + " feels moist beneath your teats. Your udder feels slightly swollen as milk leaks out. It is nice and full enough for a good milking.",False);
         ++this.udderEngorgementLevel;
         this.udderChange(2);
      }
      this.udderEngorgement += (this.udderLactation + this.milkMod) * param1;
   }
   if(this.nipplePlay > 100 && this.lactation > 0)
   {
      this.lactChange(1,15);
      this.outputMainText("\r\rYour breasts feel even more active, the high demand on their motherly supply increase your production rate.",False);
      this.nipplePlay = 0;
   }
   if(this.udderPlay > 100 && this.udderLactation > 0)
   {
      this.lactChange(2,25);
      this.outputMainText("\r\rYour breasts feel even more active, the high demand on their motherly supply increase your production rate.",False);
      this.udderPlay = 0;
   }
   if(this.lactation > 0 && !(this.attireTop == 28 && this.percent() < 50))
   {
      this.nipplePlay -= param1;
   }
   if(this.nipplePlay > 100 && this.lactation <= 0)
   {
      this.lactChange(1,15);
      this.outputMainText(" All of the attention to your nipples has induced your milky state.",False);
      this.nipplePlay = 0;
   }
   if(this.udderLactation > 0 && this.udders == True)
   {
      this.udderPlay -= param1;
   }
   else if(this.udderPlay > 100)
   {
      this.lactChange(2,25);
      this.outputMainText(" All of the attention to your teats has induced your milky state.",False);
      this.udderPlay = 0;
   }
   if(this.lactation > 0 && this.nipplePlay < -20)
   {
      this.lactChange(1,-10);
      if(this.lactation == 0)
      {
         this.outputMainText(" It seems as though the mammary glands in your breasts have adapted to the lack of demand.",False);
      }
      this.nipplePlay = 0;
   }
   if(this.udderLactation > 0 && this.udderPlay < -20 && this.udders == True)
   {
      this.lactChange(2,-15);
      if(this.udderLactation == 0)
      {
         this.outputMainText(" It seems as though the mammary glands in your udder have adapted to the lack of demand.",False);
      }
      this.udderPlay = 0;
   }
   if((this.lactation > 0 || this.udderLactation > 0) && this.milkSuppressant > 0)
   {
      this.outputMainText("\r\rThe flow of milk quickly seizes up and stops as the milk suppressant takes over and prevents any more from escaping.",False);
      this.milkSuppressantLact += this.lactation;
      this.milkSuppressantUdder += this.udderLactation;
      this.lactation = 0;
      this.udderLactation = 0;
   }
   if(this.milkSuppressant > 0)
   {
      if(this.milkSuppressantLact > 0)
      {
         if(this.milkEngorgementLevel < 3 && this.milkEngorgement + (this.milkSuppressantLact + this.milkMod) * param1 > ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2 && this.milkEngorgement <= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2)
         {
            this.outputMainText("\r\rYour breasts are so swollen that they feel like balloons on your chest. When standing still, it takes a while for the fluid inside to stop swishing, they\'re so big and sore and especially sensitive from being stretched and heavy with engorgement. The production of milk far exceeds their capacities, but the excess just gets absorbed back into your body since the milk suppressant prevents any other escape...",False);
            if(this.milkEngorgementLevel < 1)
            {
               this.boobChange(3);
            }
            else if(this.milkEngorgementLevel < 2)
            {
               this.boobChange(2);
            }
            else
            {
               this.boobChange(1);
            }
            ++this.milkEngorgementLevel;
         }
         else if(this.milkEngorgementLevel < 2 && this.milkEngorgement + (this.milkSuppressantLact + this.milkMod) * param1 > ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5 && this.milkEngorgement <= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5)
         {
            this.outputMainText("\r\rYour breasts feel stretched and heavy, so full of milk and almost aching because none of the white fluid will escape with the milk suppressant active...",False);
            if(this.milkEngorgementLevel < 1)
            {
               this.boobChange(2);
            }
            else
            {
               this.boobChange(1);
            }
            ++this.milkEngorgementLevel;
         }
         else if(this.milkEngorgementLevel < 1 && this.milkEngorgement + (this.milkSuppressantLact + this.milkMod) * param1 > (this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap && this.milkEngorgement <= (this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap)
         {
            this.outputMainText("\rYour breasts feel slightly swollen and heavy, your mammaries laden with milk. It\'s a sign that they are nice and full for a good breastfeeding, or whatever your kinky mind has for them, if you could only leak...",False);
            ++this.milkEngorgementLevel;
            this.boobChange(1);
         }
         this.milkEngorgement += (this.milkSuppressantLact + this.milkMod) * param1;
         if(this.milkEngorgement >= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 7)
         {
            this.milkEngorgement = ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 7;
         }
      }
      if(this.milkSuppressantUdder > 0 && this.udders == True)
      {
         if(this.udderEngorgementLevel < 3 && this.udderEngorgement + (this.milkSuppressantUdder + this.milkMod) * param1 > ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2 && this.udderEngorgement <= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2)
         {
            this.outputMainText("\r\rYour udder is so swollen that it feels like a balloon. When standing still, it takes a while for the fluid inside to stop swishing, it\'s so big and sore and especially sensitive from being stretched and heavy with engorgement. The production of milk far exceeds its capacities, but the excess just gets absorbed back into your body since the milk suppressant prevents any other escape...",False);
            if(this.udderEngorgementLevel < 1)
            {
               this.udderChange(5);
            }
            else if(this.udderEngorgementLevel == 1)
            {
               this.udderChange(3);
            }
            ++this.udderEngorgementLevel;
            this.udderChange(3);
         }
         else if(this.udderEngorgementLevel < 2 && this.udderEngorgement + (this.milkSuppressantUdder + this.milkMod) * param1 > ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5 && this.udderEngorgement <= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1.5)
         {
            this.outputMainText("\r\rYour udder feels so stretch and heavy, so full of milk and almost aching because none of the white fluid will escape with the milk suppressant active...",False);
            if(this.udderEngorgementLevel < 1)
            {
               this.udderChange(2);
            }
            ++this.udderEngorgementLevel;
            this.udderChange(3);
         }
         else if(this.udderEngorgementLevel < 1 && this.udderEngorgement + (this.milkSuppressantUdder + this.milkMod) * param1 > (this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap && this.udderEngorgement <= (this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap)
         {
            this.outputMainText("\r\rYour udder feels slightly swollen, even though there is no milk flowing. It is nice and full enough for a good milking, if the milk suppressant wasn\'t stopping it.",False);
            ++this.udderEngorgementLevel;
            this.udderChange(2);
         }
         this.udderEngorgement += (this.milkSuppressantUdder + this.milkMod) * param1;
         if(this.udderEngorgement >= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 7)
         {
            this.udderEngorgement = ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 7;
         }
      }
      this.milkSuppressant -= param1;
      if(this.milkSuppressant <= 0)
      {
         if(this.milkEngorgement >= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 6)
         {
            this.outputMainText("\r\rYou feel a rumbling in your breasts as the milk suppressant begins to wear off. Your arms shake as you try to take care of your " + this.clothesTop() + ", but to no avail.\r\rYou only see white as a roaring sound escapes your chest. Milk explodes from your nipples, spraying around and around, tearing apart your " + this.clothesTop() + " from the sheer pressure and drenching everything in the area. You can\'t hear or see anything and milk end up in nearly every hole. It takes a few minutes before the eruption dies down, leaving your nipples feeling limp and de-sensitized, your breasts still huge from the engorgement though feeling much more lighter. There\'s not much that can be said about your " + this.clothesTop() + " anymore though...",False);
            this.milkEngorgement = ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 0.5;
            this.milkEngorgementLevel = 0;
            this.stats(0,0,0,-5);
            this.changeTop(-1);
         }
         else if(this.milkEngorgement >= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 4)
         {
            this.outputMainText("\r\rYou suddenly can\'t breath as your chest tenses up. For an instant, you feel your " + this.nipDesc() + " nipples soften.\r\rMilk sprays with fervor all around you, spewing from your nipples like hoses. You shudder in orgasm from the force, milk getting everywhere. There\'s so much in there that you nearly tear apart your " + this.clothesTop() + " from the pressure of the gushing. But thankfully, the fabric survives and your nipples die back down, allowing you to see again... So much milk lost, but your breasts have returned to normal in those few moments...",False);
            this.milkAmount(1);
            this.doLust(-Math.floor(this.sen / 2),2,3);
         }
         else if(this.milkEngorgement >= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2)
         {
            this.outputMainText("\r\rJets of milk spray from beneath your " + this.clothesTop() + " as the milk suppressant wears off. It quickly dies down without losing much milk, but you\'re now leaking again.",False);
            this.milkEngorgement = ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2;
         }
         else if(this.milkEngorgement >= ((this.breastSize * (this.breastSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1)
         {
            this.outputMainText("\r\rMilk spurts up and begins dribbling down your chest as the milk suppressant wears off, your nipples calming down and leaking again.",False);
         }
         else
         {
            this.outputMainText("\r\rYour nipples soften up as the milk suppressant wears off, allowing you to leak once more.",False);
         }
         if(this.udderEngorgement >= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 6 && this.udders == True)
         {
            this.outputMainText("\r\rYou feel a rumbling in your udder as the milk suppressant begins to wear off. Your legs shake as you try to take care of your " + this.clothesBottom() + ", but to no avail.\r\rYou only see white as a roaring sound echoes around your belly. Milk explodes from your teats, spraying around and around, tearing apart your " + this.clothesBottom() + " from the sheer pressure and drenching everything in the area. You can\'t hear or see anything and milk end up in nearly every hole. It takes a few minutes before the eruption dies down, leaving your teats feeling limp and de-sensitized, your udder still huge from the engorgement though feeling much more lighter. There\'s not much that can be said about your " + this.clothesBottom() + " anymore though...",False);
            this.udderEngorgement = ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 0.5;
            this.udderEngorgementLevel = 0;
            this.stats(0,0,0,-5);
            this.changeBot(-1);
         }
         else if(this.udderEngorgement >= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 4 && this.udders == True)
         {
            this.outputMainText("\r\rYou suddenly feel sick as your belly tenses up. For an instant, you feel your " + this.teatDesc() + " teats soften.\r\rMilk sprays with fervor all around you, spewing from your teats like hoses. You shudder in orgasm from the force, milk getting everywhere. There\'s so much in there that you nearly tear apart your " + this.clothesBottom() + " from the pressure of the gushing. But thankfully, the fabric survives and your teats die back down, allowing you to see again... So much milk lost, but your udder has returned to normal in those few moments...",False);
            this.milkAmount(1);
            this.doLust(-Math.floor(this.sen / 2),2,4);
         }
         else if(this.udderEngorgement >= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2 && this.udders == True)
         {
            this.outputMainText("\r\rJets of milk spray from beneath your " + this.clothesBottom() + " as the milk suppressant wears off. It quickly dies down without losing much milk, but you\'re now leaking again.",False);
            this.udderEngorgement = ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 2;
         }
         else if(this.udderEngorgement >= ((this.udderSize * (this.udderSize + 1) + this.tallness / 4) * 4 + this.milkCap) * 1 && this.udders == True)
         {
            this.outputMainText("\r\rMilk spurts up and begins dribbling down your " + this.legDesc(2) + " as the milk suppressant wears off, your teats calming down and leaking again.",False);
         }
         else
         {
            this.outputMainText("\r\rYour teats soften up as the milk suppressant wears off, allowing you to leak once more.",False);
         }
         this.lactation = this.milkSuppressantLact;
         this.udderLactation = this.milkSuppressantUdder;
         this.milkSuppressantLact = 0;
         this.milkSuppressantUdder = 0;
         this.milkSuppressant = 0;
      }
   }
   if(this.hunger - param1 <= -50)
   {
      this.outputMainText("\r\rWith the lack of eating and all the action, you\'ve managed to shave off a bit of your excess weight around your belly.",False);
      this.bellyMod -= 2;
      this.hunger = 0;
      if(this.bellyMod <= 0)
      {
         this.outputMainText(" Although, you don\'t exactly have any belly to shave off anymore, so instead your stomach growls with the hunger pains...",False);
         this.hunger = 0;
         this.bellyMod = 0;
      }
   }
   else if(this.hunger - param1 >= 100)
   {
      this.outputMainText("\r\rYou notice a bit more chub around your belly thanks to all you\'ve been eating lately. You may want to watch your diet more closely.",False);
      this.bellyMod += 5;
      this.hunger = this.hunger - param1 - 30;
   }
   else
   {
      this.hunger -= param1;
   }
   if(this.skipExhaustion == True)
   {
      this.skipExhaustion = False
   }
   else
   {
      this.exhaustion += param1;
   }
   if(this.exhaustion > 20 && this.exhaustion <= 32)
   {
      this.outputMainText("\r\rYour body is getting tired, affecting your ability to do things. Sleep is sounding like a nice idea...",False);
      if(this.exhaustionPenalty == 0)
      {
         this.exhaustionPenalty = 1;
         this.statsMod(-3,-3,0,0);
      }
   }
   else if(this.exhaustion > 32 && this.exhaustion <= 44)
   {
      this.outputMainText("\r\rExhaustion is creeping over you, making any task seem tedious. Your wits are a lot less witty and your muscles are fatigued.",False);
      if(this.exhaustionPenalty == 1)
      {
         this.exhaustionPenalty = 2;
         this.statsMod(-8,-8,0,0);
      }
      if(this.exhaustionPenalty == 0)
      {
         this.exhaustionPenalty = 2;
         this.statsMod(-11,-11,0,0);
      }
   }
   else if(this.exhaustion > 44)
   {
      this.currentState = 1;
   }
   else
   {
      if(this.exhaustionPenalty == 1 && this.exhaustion <= 20)
      {
         this.exhaustionPenalty = 0;
         this.statsMod(3,3,0,0);
      }
      if(this.exhaustionPenalty == 2 && this.exhaustion <= 20)
      {
         this.exhaustionPenalty = 0;
         this.statsMod(11,11,0,0);
      }
      if(this.exhaustionPenalty == 2 && this.exhaustion <= 32)
      {
         this.exhaustionPenalty = 1;
         this.statsMod(8,8,0,0);
      }
   }
   if(param1 > 0)
   {
      if(this.percent() <= this.lib && this.lust < 90)
      {
         this.doLust(Math.floor(this.lib / 25 + 1),0);
      }
   }
   if(this.lust < 90 && this.lustPenalty == 3)
   {
      this.outputMainText("\r\rYour " + this.skinDesc() + " feels calmer, no longer hypersensitive.",False);
      this.statsMod(0,0,0,-10);
      this.lustPenalty = 2;
   }
   if(this.lust < 60 && this.lustPenalty == 2)
   {
      this.outputMainText("\r\rStrength returns to your muscles now that the strong arousal has been sated.",False);
      this.statsMod(5,0,0,0);
      this.lustPenalty = 1;
   }
   if(this.lust < 30 && this.lustPenalty == 1)
   {
      this.outputMainText("\r\rWith the distracting \'itch\' lifted from your mind, you\'re now able to focus better than before.",False);
      this.statsMod(0,4,0,0);
      this.lustPenalty = 0;
   }
   this.vagBellyChange(0,0);
   if(this.blueBalls + param1 > 84 && this.blueBalls <= 84 && this.showBalls == True && this.balls > 0)
   {
      this.outputMainText("\r\rYour " + this.ballDesc() + " balls feel swollen and heavy within your " + this.clothesBottom() + ". The need to spill your seed makes you a little aroused.",False);
      this.doLust(Math.ceil(this.ballSize / 4),0);
   }
   if(this.balls > 0)
   {
      this.blueBalls += param1;
   }
   if(this.bodyOil > 0)
   {
      if(this.bodyOil - param1 <= 0)
      {
         this.outputMainText("\r\rThe body oil finally dries off, leaving you " + this.skinDesc() + " not looking quite as shiny and attractive as before.",False);
         this.enticeMod -= 5;
         this.bodyOil = 0;
      }
      else
      {
         this.bodyOil -= 5;
      }
   }
   if(this.masoPot - param1 <= 0 && this.masoPot > 0)
   {
      this.outputMainText("\r\rYou shiver a little as your nerves seem to feel more... normal. The effects of the Masochism Potion have apparently worn off, so you might want to be slightly more cautious once again.",False);
      this.masoPot = 0;
   }
   else if(this.masoPot > 0)
   {
      this.masoPot -= param1;
   }
   if(this.sMasoPot - param1 <= 0 && this.sMasoPot > 0)
   {
      this.outputMainText("\r\rYou shiver a lot as your nerves seem to feel more... normal. The effects of the Superior Masochism Potion have apparently worn off, so you might want to be much more cautious once again.",False);
      this.sMasoPot = 0;
   }
   else if(this.sMasoPot > 0)
   {
      this.sMasoPot -= param1;
   }
   if(this.babyFree - param1 <= 0 && this.babyFree > 0)
   {
      this.outputMainText("\r\rYour belly groans as you feel your fertility return to you, urging you to remain cautious of becoming pregnant again. It seems as though you\'re no longer as baby free as before.",False);
      if(this.vagTotal < 1)
      {
         this.outputMainText(" Not that any of that means anything to you, considering you don\'t even have a womb to become pregnant in the first place.",False);
      }
      this.babyFree = 0;
   }
   else if(this.babyFree > 0)
   {
      this.babyFree -= param1;
   }
   if(this.charmTime > 0)
   {
      if(this.charmTime - param1 <= 0)
      {
         this.outputMainText("\r\rYour charming effect wears off, making you not so alluring as before.",False);
         this.charmTime = 0;
         this.enticeMod -= 13;
      }
      else
      {
         this.charmTime -= param1;
      }
   }
   if(this.pheromone > 0)
   {
      if(this.pheromone - param1 <= 0)
      {
         this.outputMainText("\r\rThe scent of pheromones finally fades away, leaving you not so unexpectedly desireable to nearly everything.",False);
         this.pheromone = 0;
         this.enticeMod -= 25;
         this.statsMod(0,0,-3,0);
      }
      else
      {
         this.pheromone -= param1;
      }
   }
   if(this.eggceleratorTime > 0)
   {
      if(this.eggceleratorTime - param1 <= 0)
      {
         this.outputMainText("\r\rYour belly feels calmer as the eggcelerator wears off, allowing your womb to relax a little.",False);
         this.eggceleratorTime = 0;
         this.eggRate -= this.eggceleratorDose;
         this.eggceleratorDose = 0;
      }
      else
      {
         this.eggceleratorTime -= param1;
      }
   }
   if(this.fertileGel > 0)
   {
      if(this.fertileGel - param1 <= 0)
      {
         this.outputMainText("\r\rYour womb cools off a little as the fertile gel wears off.",False);
         this.fertileGel = 0;
         this.pregChanceMod -= 10;
      }
      else
      {
         this.fertileGel -= param1;
      }
   }
   if(this.plumpQuats > 0)
   {
      if(this.plumpQuats - param1 <= 0)
      {
         this.outputMainText("\r\rThe last of the quat dissolves inside your stomach, your belly bloating further as the abundant energy is added to your figure. Your stomach cools off, finished with the digestive process.",False);
         this.bellyMod += 5 * this.plumpQuats;
         this.plumpQuats = 0;
      }
      else
      {
         this.outputMainText("\r\rYour stomach gurgles warmly as it continues to digest the quat. So much energy from the fruit\'s flesh gets absorbed by your body, swelling your belly a little and giving you a bit more girth...",False);
         this.bellyMod += 5 * param1;
         this.plumpQuats -= param1;
      }
   }
   if(this.fertilityStatueCurse > 0)
   {
      if(this.fertilityStatueCurse - param1 <= 0)
      {
         this.outputMainText("\r\rThe overbearing feeling of lust finally subdues. Seems as though the statue\'s curse has finally worn off, so you won\'t be getting as much of a lesson about how to please the female gender. Well, at least for now...",False);
         this.fertilityStatueCurse = 0;
         this.minLust -= 10;
      }
      else
      {
         this.fertilityStatueCurse -= param1;
      }
   }
   if(this.lilaWetStatus > 0)
   {
      if(this.lilaWetStatus - param1 <= 0)
      {
         this.outputMainText("\r\rThe flow in your loins calms down a bit after not having been influenced by a certain little felin in a while.",False);
         this.lilaWetStatus = 0;
         this.cockMoistMod -= 6;
         this.vagMoistMod -= 6;
         this.minLust -= 5;
      }
      else
      {
         this.lilaWetStatus -= param1;
      }
   }
   if(this.milkCPoisonNip > 0)
   {
      if(this.milkCPoisonNip - param1 <= 0)
      {
         this.outputMainText("\r\rThe warmth from the poison in your bosom fades, no longer as tingly.",False);
         this.milkCPoisonNip = 0;
      }
      else
      {
         this.milkCPoisonNip -= param1;
      }
   }
   if(this.milkCPoisonUdd > 0)
   {
      if(this.milkCPoisonUdd - param1 <= 0)
      {
         this.outputMainText("\r\rThe warmth from the poison in your bosom fades, no longer as tingly.",False);
         this.milkCPoisonUdd = 0;
      }
      else
      {
         this.milkCPoisonUdd -= param1;
      }
   }
   if(this.cockSnakeVenom > 0)
   {
      if(this.cockSnakeVenom - param1 <= 0)
      {
         this.outputMainText("\r\rThe warmth from the venom in your loins fades, your body fully metabolizing it and rendering it neutral.",False);
         this.cockSnakeVenom = 0;
      }
      else
      {
         this.cockSnakeVenom -= param1;
      }
   }
   this.statDisplay();
   if(this.currentText == "Afterwards...")
   {
      this.outputMainText("",True);
      this.doProcess();
   }
   else
   {
      this.doEnd();
   }
}
def Affinity(humanChange:int, horseChange:int, wolfChange:int, catChange:int, cowChange:int, lizardChange:int, rabbitChange:int):
   global human, horse, wolf, cat, cow, lizard, rabbit
   human += math.ceil(humanChange * changeMod)
   horse += math.ceil(horseChange * changeMod)
   wolf += math.ceil(wolfChange * changeMod)
   cat += math.ceil(catChange * changeMod)
   cow += math.ceil(cowChange * changeMod)
   lizard += math.ceil(lizardChange * changeMod)
   rabbit += math.ceil(rabbitChange * changeMod)

def Aff(tempRace, tempChange, otherChange):
   global changeMod, human, horse, wolf, cat, cow, lizard, rabbit, mouse, bird, pig, skunk, bug, twoBoobAffinity, fourBoobAffinity, sixBoobAffinity, eightBoobAffinity, tenBoobAffinity, cowTaurAffinity, humanTaurAffinity
   human += math.ceil(otherChange * changeMod)
   horse += math.ceil(otherChange * changeMod)
   wolf += math.ceil(otherChange * changeMod)
   cat += math.ceil(otherChange * changeMod)
   cow += math.ceil(otherChange * changeMod)
   lizard += math.ceil(otherChange * changeMod)
   rabbit += math.ceil(otherChange * changeMod)
   mouse += math.ceil(otherChange * changeMod)
   bird += math.ceil(otherChange * changeMod)
   pig += math.ceil(otherChange * changeMod)
   skunk += math.ceil(otherChange * changeMod)
   bug += math.ceil(otherChange * changeMod)
   twoBoobAffinity += math.ceil(otherChange * changeMod)
   fourBoobAffinity += math.ceil(otherChange * changeMod)
   sixBoobAffinity += math.ceil(otherChange * changeMod)
   eightBoobAffinity += math.ceil(otherChange * changeMod)
   tenBoobAffinity += math.ceil(otherChange * changeMod)
   cowTaurAffinity += math.ceil(otherChange * changeMod)
   humanTaurAffinity += math.ceil(otherChange * changeMod)
   if (tempRace == 1):
      human += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 2):
      horse += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 3):
      wolf += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 4):
      cat += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 5):
      cow += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 6):
      lizard += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 7):
      rabbit += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 8):
      mouse += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 9):
      bird += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 10):
      pig += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 11):
      skunk += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)
   if (tempRace == 12):
      bug += math.ceil(tempChange * changeMod) - math.ceil(otherChange * changeMod)

!def AffinityChange():
   global humanAffinity, human, horseAffinity, horse, wolfAffinity, wolf, catAffinity, cat, cowAffinity, cow, lizardAffinity, lizard, rabbitAffinity, rabbit, mouseAffinity, mouse, birdAffinity, bird, pigAffinity, pig, skunkAffinity, skunk, bugAffinity, bug, changeMod, cockTotal, vagTotal, cockSizeMod, vagSizeMod, knot, cumMod, heat, heatMaxTime, heatTime, nippleSize, milkMod, hips, udders, udderSize, teatSize, udderLactation, udderEngorgement, udderEngorgementLevel, udderPlay, eggLaying, eggType, eggMaxTime, eggTime, pregRate, runMod, balls, showBalls, coinMod, bellyMod, buttMod, skinType, tail, enticeMod, butt, lockSkin, lockFace, faceType, lockTail, wings, lockEars, ears, lockBreasts, breastSize, boobTotal, lockLegs, legType, cowTaurAffinity, humanTaurAffinity, lockNipples, nipType, lockCock, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, rabbitCocks, bugCocks
   affinityCheckArray = list(())
   domCheck = 0
   second = 0
   var maxSkin:* = undefined;
   var maxFur:* = undefined;
   var maxScale:* = undefined;
   var maxFeather:* = undefined;
   var maxChitin:* = undefined;
   var maxNonSkin:* = undefined;
   var maxNonFur:* = undefined;
   var maxNonScale:* = undefined;
   var maxNonFeather:* = undefined;
   var maxNonChitin:* = undefined;
   var hasMuzzle:Boolean = False
   var tempTailArray:Array = null;
   var maxTail:* = undefined;
   var secondTail:* = undefined;
   var maxNonTail:* = undefined;
   var maxNonWings:* = undefined;
   var maxWings:* = undefined;
   twoBoob = 0
   sixBoob = 0
   fourBoob = 0
   eightBoob = 0
   tenBoob = 0
   nonTwoBoob = 0
   nonSixBoob = 0
   nonFourBoob = 0
   nonEightBoob = 0
   nonTenBoob = 0
   bipedal = 0
   bipedalDigiPaw = 0
   otherLegs = list(())
   legArray = list(())
   secondLegs = 0
   nip0 = 0
   nip1 = 0
   nip2 = 0
   nonNip0 = 0
   nonNip1 = 0
   nonNip2 = 0
   egg0 = 0
   egg1 = 0
   var nonEgg0:* = undefined;
   var nonEgg1:* = undefined;
   OutputMainText("Something feels odd...",True)
   chance = Percent()
   affinityCheckArray = []
   affinityCheckArray.push(humanAffinity + human)
   affinityCheckArray.push(horseAffinity + horse)
   affinityCheckArray.push(wolfAffinity + wolf)
   affinityCheckArray.push(catAffinity + cat)
   affinityCheckArray.push(cowAffinity + cow)
   affinityCheckArray.push(lizardAffinity + lizard)
   affinityCheckArray.push(rabbitAffinity + rabbit)
   affinityCheckArray.push(mouseAffinity + mouse)
   affinityCheckArray.push(birdAffinity + bird)
   affinityCheckArray.push(pigAffinity + pig)
   affinityCheckArray.push(skunkAffinity + skunk)
   affinityCheckArray.push(bugAffinity + bug)
   affinityCheckArray.sort(16)
   domCheck = affinityCheckArray.pop()
   second = affinityCheckArray.pop()
   if (domCheck == (humanAffinity + human)) and (human >= 0):
      dominant = 1
   elif (domCheck == (horseAffinity + horse)) and (horse >= 0):
      dominant = 2
   elif (domCheck == (wolfAffinity + wolf)) and (wolf >= 0):
      dominant = 3
   elif (domCheck == (catAffinity + cat)) and (cat >= 0):
      dominant = 4
   elif (domCheck == (cowAffinity + cow)) and (cow >= 0):
      dominant = 5
   elif (domCheck == (lizardAffinity + lizard)) and (lizard >= 0):
      dominant = 6
   elif (domCheck == (rabbitAffinity + rabbit)) and (rabbit >= 0):
      dominant = 7
   elif (domCheck == (mouseAffinity + mouse)) and (mouse >= 0):
      dominant = 8
   elif (domCheck == (birdAffinity + bird)) and (bird >= 0):
      dominant = 9
   elif (domCheck == (pigAffinity + pig)) and (pig >= 0):
      dominant = 10
   elif (domCheck == (skunkAffinity + skunk)) and (skunk >= 0):
      dominant = 11
   elif (domCheck == (bugAffinity + bug)) and (bug >= 0):
      dominant = 12
   if ((humanAffinity + human) >= 40) and (humanAffinity < 40):
      OutputMainText("\n" + "\n" + "Your body feels quite... adaptive? There's a strange sense of being more susceptible to change",False)
      changeMod += 0.5
   if ((humanAffinity + human) < 40) and (humanAffinity >= 40):
      OutputMainText("\n" + "\n" + "Your body feels less ready to bend to your surroundings as much as it had anymore.",False)
      changeMod -= 0.5
   if ((horseAffinity + horse) >= 40) and (horseAffinity < 40):
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "Your " + ClothesBottom() + " grows tight, filling with extra cockflesh. Opening the " + ClothesBottom() + ", your cock" + Plural(1) + " spill" + Plural(3) + " out, dangling while swelling larger and larger. The growth slows to a halt, much, much longer than before. 'Hung like a horse' seems like the appropriate phrase. And you're also going to have to sneak back into town while you hide your perverse excess flesh, rushing to a tailor to refit you.",False)
      if (vagTotal > 0):
         OutputMainText("\n" + "\n" + "Doubling over, you hug your belly as it begins to cramp. You can clearly feel your vaginal flesh grow within, the walls growing much deeper. By the time it's over, you feel somewhat like a mare, able to take cocks much larger than you could have before...",False)
      CockSizeMod += 1
      VagSizeMod += 1
      VagBellyChange(0,0)
   if ((horseAffinity + horse) < 40) and (horseAffinity >= 40):
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "Your " + ClothesBottom() + " feel baggier. Opening the " + ClothesBottom() + ", your cock" + Plural(1) + " shrinking towards your groin, losing a great deal of length. It seems like you have lost your equine engorgement.",False)
      if (vagTotal > 0):
         OutputMainText("\n" + "\n" + "Your belly feels rather empty all of a sudden. Placing your hand over it, you can feel the vaginal flesh recede, no longer built like mare.",False)
      cockSizeMod -= 1
      vagSizeMod -= 1
      VagBellyChange(0,0)
   if ((wolfAffinity + wolf) >= 40) and (wolfAffinity < 40):
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "A sudden wave of lust washes over you, your cock" + Plural(1) + " growing stiff in your " + ClothesBottom() + ". You quickly open open your " + ClothesBottom() + " to see what's going on. Within, the base" + Plural(1) + " of your shaft" + Plural(1) + " swell" + Plural(3) + ". In an instant, you're surprised by spurts of cum that shower you, a small volley from a quick unexpected orgasm. Wiping your eyes so you can see, the swelling persists as you continue to come for a while. It would be very difficult to remove your cock from a hot hole with a large 'knot' like that, until finished draining your seed.",False)
      knot = True
      cumMod += 0.5
   if ((wolfAffinity + wolf) < 40) and (wolfAffinity >= 40):
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "An odd draining fills your " + ClothesBottom() + ". Looking within, you see your cock" + Plural(1) + " grow slightly stiff, your knot" + Plural(1) + " swelling. Pre lazily seeps from your urethra" + Plural(1) + " as the knot" + Plural(1) + " deflate" + Plural(1) + " immediately while your cock" + Plural(1) + " remain" + Plural(3) + " stiff. It seems as though you have lost your knot" + Plural(1) + ".",False)
      knot = False
      cumMod -= 0.5
   if ((catAffinity + cat) >= 40) and (catAffinity < 40):
      if (vagTotal > 0):
         OutputMainText("\n" + "\n" + "Your " + ClothesBottom() + " grows slightly moist, your cunt" + Plural(2) + " burning with arousal. The feeling quickly fades, but something tells you your reproductive instincts might occasionally take over...",False)
      if (heat < 1):
         heatMaxTime = 96
         heatTime = 96
         heat += 1
      elif (heat >= 1):
         heatMaxTime -= 12
         heat += 1
   if ((catAffinity + cat) < 40) and (catAffinity >= 40):
      if (vagTotal > 0):
         OutputMainText(" You also feel your vagina" + Plural(2) + " cool a little, no longer as eager to be impregnated on certain days.",False)
      if (heat >= 2):
         heatMaxTime += 12
      heat -= 1
   #trace(cowAffinity + cow);
   if(this.cowAffinity + this.cow >= 10 && this.cowAffinity < 10)
   {
      this.outputMainText("\r\rYour nipples stiffen beneath your " + this.clothesTop() + ". They protrude nearly half an inch further than before!",False);
      this.nippleSize += 2;
      this.milkMod += 50;
   }
   if(this.cowAffinity + this.cow >= 25 && this.cowAffinity < 25)
   {
      this.outputMainText("\r\rYour nipples stiffen beneath your " + this.clothesTop() + ". They protrude an inch further than before! And your hips seem slightly broader...",False);
      this.lactChange(1,75);
      this.nippleSize += 5;
      this.hips += 4;
      this.milkMod += 50;
   }
   if(this.cowAffinity + this.cow >= 40 && this.cowAffinity < 40)
   {
      this.outputMainText("\r\rYour nipples squirm within your " + this.clothesTop() + ". They\'ve grown over an inch and a half in length! And your hips feel like they\'re more \'square\' than before...",False);
      this.lactChange(1,75);
      this.nippleSize += 8;
      this.hips += 6;
      this.milkMod += 50;
   }
   if(this.cowAffinity + this.cow >= 55 && this.cowAffinity < 55)
   {
      this.outputMainText("\r\rJust above your groin, your belly begins to feel bloated. You wince as it pushes against your " + this.clothesBottom() + ", especially noticing the increased sensitivity of four spots in particular. Before you can act, your " + this.clothesBottom() + " tears at the waist, as a mound crashes through. Hanging naked and free, with four teats twice as long as your nipples, an udder about twice as large as your chest dribbles milk. You\'ll definitely be getting a special bra or perhaps adjust your " + this.clothesBottom() + " when you get back to town, at least to account for your surprisingly wider hips... ",False);
      this.lactChange(1,150);
      this.lactChange(2,this.lactation);
      this.hips += 8;
      this.udders = True
      this.udderSize = 2 * this.breastSize;
      this.teatSize = 2 * this.nippleSize;
   }
   if(this.cowAffinity + this.cow < 10 && this.cowAffinity >= 10)
   {
      this.outputMainText("\r\rYour nipples are less noticeable, shrinking by nearly half an inch.",False);
      this.nippleSize -= 2;
      this.milkMod -= 50;
   }
   if(this.cowAffinity + this.cow < 25 && this.cowAffinity >= 25)
   {
      this.outputMainText("\r\rYour nipples seem less noticeable as they shrink by an inch and your hips are less wide.",False);
      this.lactChange(1,-50);
      if(this.udders == True)
      {
         this.lactChange(2,-50);
      }
      this.nippleSize -= 5;
      this.hips -= 4;
      this.milkMod -= 50;
   }
   if(this.cowAffinity + this.cow < 40 && this.cowAffinity >= 40)
   {
      this.outputMainText("\r\rYour " + this.clothesTop() + " feels slightly looser, as your nipples shrink by over an inch and a half. You hips also narrow a little, protruding less than before.",False);
      this.lactChange(1,-50);
      if(this.udders == True)
      {
         this.lactChange(2,-50);
      }
      this.hips -= 6;
      this.nippleSize -= 8;
      this.milkMod -= 50;
   }
   if(this.cowAffinity + this.cow < 55 && this.cowAffinity >= 55)
   {
      if(!this.udderCheck(1))
      {
         this.outputMainText("\r\rThe fleshy bag of milk at your abdomen shrinks to nothing, disappearing along with its teats. You\'re no longer lugging around an udder. Plus your waistbands seem quite loose after your hips shrink by a few inches.",False);
         this.lactChange(1,-100);
         this.hips -= 8;
         this.udders = False
         this.udderLactation = 0;
         this.udderEngorgement = 0;
         this.udderEngorgementLevel = 0;
         this.udderPlay = 0;
         this.udderSize = 0;
         this.teatSize = 0;
      }
      else
      {
         this.outputMainText("\r\rYour waistbands seem quite loose after your hips shrink by a few inches.",False);
         this.lactChange(1,-100);
         this.hips -= 8;
      }
   }
   if(this.lizardAffinity + this.lizard >= 40 && this.lizardAffinity < 40)
   {
      if(this.cockTotal == 1)
      {
         this.cockChange(0,1);
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rAn odd sensation of warmth fills your womb" + this.plural(2) + ". You can literally feel your eggs stir within, preparing themselves to cycle much more frequently, growing hard shells to protect them, whenever you\'re not pregnant.",False);
      }
      if(this.eggLaying == 0)
      {
         ++this.eggLaying;
         this.eggType = 0;
         this.eggMaxTime = 36;
         this.eggTime = 36;
      }
      else
      {
         this.eggMaxTime -= 6;
         ++this.eggLaying;
      }
   }
   if(this.lizardAffinity + this.lizard < 40 && this.lizardAffinity >= 40)
   {
      if(this.cockTotal == 2)
      {
         this.cockChange(0,-1);
      }
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour womb" + this.plural(2) + " calm" + this.plural(4) + " down, no longer working as hard to pop out more eggs.",False);
      }
      if(this.eggLaying == 1)
      {
         --this.eggLaying;
         this.eggMaxTime = 0;
         this.eggTime = 0;
      }
      else if(this.eggLaying > 1)
      {
         this.eggMaxTime += 6;
         --this.eggLaying;
      }
   }
   if(this.rabbitAffinity + this.rabbit >= 10 && this.rabbitAffinity < 10)
   {
      this.stats(0,0,2,0);
   }
   if(this.rabbitAffinity + this.rabbit >= 30 && this.rabbitAffinity < 30)
   {
      this.stats(0,0,5,0);
   }
   if(this.rabbitAffinity + this.rabbit >= 50 && this.rabbitAffinity < 50)
   {
      this.stats(0,0,7,0);
   }
   if(this.rabbitAffinity + this.rabbit >= 40 && this.rabbitAffinity < 40)
   {
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour womb" + this.plural(2) + " feel" + this.plural(4) + " a bit... hyperactive. It feels as though you could breed like some sort of cute, small, fuzzy animal.",False);
      }
      this.pregRate += 1;
   }
   if(this.rabbitAffinity + this.rabbit < 10 && this.rabbitAffinity >= 10)
   {
      this.stats(0,0,-2,0);
   }
   if(this.rabbitAffinity + this.rabbit < 30 && this.rabbitAffinity >= 30)
   {
      this.stats(0,0,-5,0);
   }
   if(this.rabbitAffinity + this.rabbit < 50 && this.rabbitAffinity >= 50)
   {
      this.stats(0,0,-7,0);
   }
   if(this.rabbitAffinity + this.rabbit < 40 && this.rabbitAffinity >= 40)
   {
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour womb" + this.plural(2) + " feel" + this.plural(4) + " calmer. Now you can take your fertility nice and easy... relatively.",False);
      }
      this.pregRate = this.pregRate - 1;
   }
   if(this.mouseAffinity + this.mouse >= 40 && this.mouseAffinity < 40)
   {
      this.outputMainText("\r\rA slight paranoia lingers in your mind, making you feel quite skittish. If you needed to, you could probably run from a threat at the drop of a needle.",False);
      if(this.balls > 0 && this.showBalls == True)
      {
         this.outputMainText(" Your " + this.ballDesc() + " nuts also feel slightly \'skittish\', like they\'re making far more than they just were...",False);
      }
      this.runMod += 25;
      this.cumMod += 3;
   }
   if(this.mouseAffinity + this.mouse < 40 && this.mouseAffinity >= 40)
   {
      this.outputMainText("\r\rThe paranoia dissipates from your mind, your body languishing and no longer as flighty.",False);
      if(this.balls > 0 && this.showBalls == True)
      {
         this.outputMainText(" Your " + this.ballDesc() + " nuts also calm down, their production diminishing.",False);
      }
      this.runMod -= 25;
      this.cumMod -= 3;
   }
   if(this.birdAffinity + this.bird >= 40 && this.birdAffinity < 40)
   {
      this.outputMainText("\r\rYours eyes dart about for a moment as shiny things become suddenly more noticeable. After a few moments, you calm down, but your definitely able to spot shiny things more accurately, able to find an extra couple coins whenever you come across any.",False);
      this.coinMod += 2;
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rAn odd sensation of warmth fills your womb" + this.plural(2) + ". You can literally feel your eggs stir within, preparing themselves to cycle much more frequently, growing hard shells to protect them, whenever you\'re not pregnant.",False);
      }
      if(this.eggLaying == 0)
      {
         ++this.eggLaying;
         this.eggMaxTime = 36;
         this.eggTime = 36;
         this.eggType = 0;
      }
      else
      {
         this.eggMaxTime -= 6;
         ++this.eggLaying;
      }
   }
   if(this.birdAffinity + this.bird < 40 && this.birdAffinity >= 40)
   {
      this.outputMainText("\r\rYour affinity for shinies dissipates. Not quite as focused on them, you aren\'t able to find an extra couple coins anymore.",False);
      this.coinMod -= 2;
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour womb" + this.plural(2) + " calm" + this.plural(4) + " down, no longer working as hard to pop out more eggs.",False);
      }
      if(this.eggLaying == 1)
      {
         --this.eggLaying;
         this.eggMaxTime = 0;
         this.eggTime = 0;
      }
      else if(this.eggLaying > 1)
      {
         --this.eggLaying;
         this.eggMaxTime += 6;
      }
   }
   if(this.pigAffinity + this.pig >= 10 && this.pigAffinity < 10)
   {
      this.outputMainText("\r\rYour belly jiggles a bit more than you remember. Seems you\'ve gotten a bit chubbier, despite what you have eaten...",False);
      this.bellyMod += 20;
   }
   if(this.pigAffinity + this.pig >= 30 && this.pigAffinity < 30)
   {
      this.outputMainText("\r\rYour belly jiggles a bit more than you remember. Seems you\'ve gotten a bit chubbier, despite what you have eaten...",False);
      this.bellyMod += 20;
   }
   if(this.pigAffinity + this.pig >= 50 && this.pigAffinity < 50)
   {
      this.outputMainText("\r\rYour belly jiggles a bit more than you remember. Seems you\'ve gotten a bit chubbier, despite what you have eaten...",False);
      this.bellyMod += 20;
   }
   if(this.pigAffinity + this.pig >= 70 && this.pigAffinity < 70)
   {
      this.outputMainText("\r\rYour belly jiggles a bit more than you remember. Seems you\'ve gotten a bit chubbier, despite what you have eaten...",False);
      this.bellyMod += 20;
   }
   if(this.pigAffinity + this.pig >= 40 && this.pigAffinity < 40)
   {
      this.outputMainText("\r\rYou groan as you feel some of your extra weight grow heavier. Your hips grow wider and your ass grows larger, exaggerating your chubbiness.",False);
      if(this.balls > 0 && this.showBalls == True)
      {
         this.outputMainText(" Your " + this.ballDesc() + " balls also feel rather \'fat\', growing heavy with seed...",False);
      }
      this.cumMod += 5;
      this.hipMod += 0.5;
      this.buttMod += 0.5;
   }
   if(this.pigAffinity + this.pig < 10 && this.pigAffinity >= 10)
   {
      this.outputMainText("\r\rYour belly feels lighter, your extra porkiness dissipating.",False);
      this.bellyMod -= 20;
   }
   if(this.pigAffinity + this.pig < 30 && this.pigAffinity >= 30)
   {
      this.outputMainText("\r\rYour belly feels lighter, your extra porkiness diminishing.",False);
      this.bellyMod -= 20;
   }
   if(this.pigAffinity + this.pig < 50 && this.pigAffinity >= 50)
   {
      this.outputMainText("\r\rYour belly feels lighter, your extra porkiness diminishing.",False);
      this.bellyMod -= 20;
   }
   if(this.pigAffinity + this.pig < 70 && this.pigAffinity >= 70)
   {
      this.outputMainText("\r\rYour belly feels lighter, your extra porkiness diminishing.",False);
      this.bellyMod -= 20;
   }
   if(this.pigAffinity + this.pig < 40 && this.pigAffinity >= 40)
   {
      this.outputMainText("\r\rYou moan as you feel some of your extra weight lift from you. Your hips and rump shrink, no longer nearly as chubby.",False);
      if(this.balls > 0 && this.showBalls == True)
      {
         this.outputMainText(" Your " + this.ballDesc() + " balls also feel lighter, no longer producing as much seed.",False);
      }
      this.cumMod -= 5;
      this.hipMod -= 0.5;
      this.buttMod -= 0.5;
   }
   if(this.skunkAffinity + this.skunk >= 40 && this.skunkAffinity < 40)
   {
      this.outputMainText("\r\rYou feel your " + this.buttDesc() + " rump grow slightly larger. Then a strange scent fills your nose, casually rising from your backside. It... It doesn\'t stink at all like you would expect from the area, but rather smells quite pleasant. A nice, pleasing, and even somewhat alluring aroma.\r\rYou try to see if you can control this scent, pushing some glands inside you never noticed before. And sure enough, you manage to spray out a more concentrated mist. However, you immediately start gagging. It smells horrible... Not something you want to try normally, but rather reserve for more severe occassions.",False);
      if(this.skinType == 2)
      {
         this.outputMainText("\r\rAnd to accentuate the change further, two parallel stripes emerge in your fur, connecting together at your brow and rung over your head all the way down to your rump",False);
         if(this.tail == 11)
         {
            this.outputMainText(" where it connects to the stripes on your tail",False);
         }
         this.outputMainText(".",False);
      }
      this.enticeMod += 10;
      this.butt += 2;
   }
   if(this.skunkAffinity + this.skunk < 40 && this.skunkAffinity >= 40)
   {
      this.outputMainText("\r\rYou feel your " + this.buttDesc() + " rump shrink slightly. The pleasant scent that exudes from it disappears, as well as the other scent you could produce.",False);
      if(this.skinType == 2)
      {
         this.outputMainText("\r\rThe twin stripes in your fur from your head to your rump also fade",False);
         if(this.tail == 11)
         {
            this.outputMainText(", though the ones on your tail remain",False);
         }
         this.outputMainText(".",False);
      }
      this.enticeMod -= 10;
      this.butt -= 2;
   }
   if(this.bugAffinity + this.bug >= 40 && this.bugAffinity < 40)
   {
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rAn odd sensation of warmth fills your womb" + this.plural(2) + ". You can literally feel your eggs stir within, preparing themselves to cycle much more frequently, growing soft shells to protect them, whenever you\'re not pregnant.",False);
      }
      if(this.eggLaying == 0)
      {
         ++this.eggLaying;
         this.eggType = 1;
         this.eggMaxTime = 14;
         this.eggTime = 14;
      }
      else
      {
         this.eggMaxTime -= 6;
         ++this.eggLaying;
      }
   }
   if(this.bugAffinity + this.bug < 40 && this.bugAffinity >= 40)
   {
      if(this.vagTotal > 0)
      {
         this.outputMainText("\r\rYour womb" + this.plural(2) + " calm" + this.plural(4) + " down, no longer working as hard to pop out more insect-like eggs.",False);
      }
      if(this.eggLaying == 1)
      {
         --this.eggLaying;
         this.eggMaxTime = 0;
         this.eggTime = 0;
      }
      else if(this.eggLaying > 1)
      {
         this.eggMaxTime += 6;
         --this.eggLaying;
      }
   }
   if(this.humanAffinity + this.human < 0)
   {
      this.humanAffinity = 0;
   }
   else if(this.humanAffinity + this.human > 100)
   {
      this.humanAffinity = 100;
   }
   else
   {
      this.humanAffinity += this.human;
   }
   if(this.horseAffinity + this.horse < 0)
   {
      this.horseAffinity = 0;
   }
   else if(this.horseAffinity + this.horse > 100)
   {
      this.horseAffinity = 100;
   }
   else
   {
      this.horseAffinity += this.horse;
   }
   if(this.wolfAffinity + this.wolf < 0)
   {
      this.wolfAffinity = 0;
   }
   else if(this.wolfAffinity + this.wolf > 100)
   {
      this.wolfAffinity = 100;
   }
   else
   {
      this.wolfAffinity += this.wolf;
   }
   if(this.catAffinity + this.cat < 0)
   {
      this.catAffinity = 0;
   }
   else if(this.catAffinity + this.cat > 100)
   {
      this.catAffinity = 100;
   }
   else
   {
      this.catAffinity += this.cat;
   }
   if(this.cowAffinity + this.cow < 0)
   {
      this.cowAffinity = 0;
   }
   else if(this.cowAffinity + this.cow > 100)
   {
      this.cowAffinity = 100;
   }
   else
   {
      this.cowAffinity += this.cow;
   }
   if(this.lizardAffinity + this.lizard < 0)
   {
      this.lizardAffinity = 0;
   }
   else if(this.lizardAffinity + this.lizard > 100)
   {
      this.lizardAffinity = 100;
   }
   else
   {
      this.lizardAffinity += this.lizard;
   }
   if(this.rabbitAffinity + this.rabbit < 0)
   {
      this.rabbitAffinity = 0;
   }
   else if(this.rabbitAffinity + this.rabbit > 100)
   {
      this.rabbitAffinity = 100;
   }
   else
   {
      this.rabbitAffinity += this.rabbit;
   }
   if(this.mouseAffinity + this.mouse < 0)
   {
      this.mouseAffinity = 0;
   }
   else if(this.mouseAffinity + this.mouse > 100)
   {
      this.mouseAffinity = 100;
   }
   else
   {
      this.mouseAffinity += this.mouse;
   }
   if(this.birdAffinity + this.bird < 0)
   {
      this.birdAffinity = 0;
   }
   else if(this.birdAffinity + this.bird > 100)
   {
      this.birdAffinity = 100;
   }
   else
   {
      this.birdAffinity += this.bird;
   }
   if(this.pigAffinity + this.pig < 0)
   {
      this.pigAffinity = 0;
   }
   else if(this.pigAffinity + this.pig > 100)
   {
      this.pigAffinity = 100;
   }
   else
   {
      this.pigAffinity += this.pig;
   }
   if(this.skunkAffinity + this.skunk < 0)
   {
      this.skunkAffinity = 0;
   }
   else if(this.skunkAffinity + this.skunk > 100)
   {
      this.skunkAffinity = 100;
   }
   else
   {
      this.skunkAffinity += this.skunk;
   }
   if(this.bugAffinity + this.bug < 0)
   {
      this.bugAffinity = 0;
   }
   else if(this.bugAffinity + this.bug > 100)
   {
      this.bugAffinity = 100;
   }
   else
   {
      this.bugAffinity += this.bug;
   }
   maxSkin = Math.max(this.humanAffinity,this.pigAffinity);
   maxFur = Math.max(this.horseAffinity,this.wolfAffinity,this.catAffinity,this.cowAffinity,this.rabbitAffinity,this.mouseAffinity,this.skunkAffinity);
   maxScale = Math.max(this.lizardAffinity);
   maxFeather = Math.max(this.birdAffinity);
   maxChitin = Math.max(this.bugAffinity);
   maxNonSkin = Math.max(maxFur,maxScale,maxFeather,maxChitin);
   maxNonFur = Math.max(maxSkin,maxScale,maxFeather,maxChitin);
   maxNonScale = Math.max(maxFur,maxSkin,maxFeather,maxChitin);
   maxNonFeather = Math.max(maxFur,maxScale,maxSkin,maxChitin);
   maxNonChitin = Math.max(maxFur,maxScale,maxSkin,maxFeather);
   if(this.lockSkin == 0)
   {
      if(maxSkin > maxNonSkin + 35 && this.skinType != 1)
      {
         this.outputMainText("\r\rYour " + this.skinDesc() + " feels oddly cool. Looking at it, your " + this.skinDesc() + " shrinks into your skin, leaving you \'bald\' all over. You feel a little naked as you get used to your bare skin.",False);
         this.skinType = 1;
      }
      if(maxFur > maxNonFur + 35 && this.skinType != 2)
      {
         this.outputMainText("\r\rYour " + this.skinDesc() + " begins to itch all over as soft hairs begin to sprout in patches. Before you know it, your whole body is soon covered in a coat of fur.",False);
         this.skinType = 2;
         if(this.skunkAffinity >= 40)
         {
            this.outputMainText(" The fur is mostly a single color, except for two parallel stripes that connect at your brow and run over your head and down your back to your rump",False);
            if(this.tail == 11)
            {
               this.outputMainText(" where it connects to the stripes on your tail",False);
            }
            this.outputMainText(".",False);
         }
      }
      if(maxScale > maxNonScale + 35 && this.skinType != 3)
      {
         this.outputMainText("\r\rYour " + this.skinDesc() + " begins to feel oddly dry, feeling somewhat flaky. Before you know it, your whole body feels soft and extremely smooth, covered in a thin layer of scales.",False);
         this.skinType = 3;
      }
      if(maxFeather > maxNonFeather + 35 && this.skinType != 4)
      {
         this.outputMainText("\r\rYour " + this.skinDesc() + " begins to tickle all over, tiny hair sprouting up all over and collecting into groups. Before you know it, you\'re rustling and fluffing up, sleeking back a layer of feathers.",False);
         this.skinType = 4;
      }
      if(maxChitin > maxNonChitin + 35 && this.skinType != 5)
      {
         this.outputMainText("\r\rYour " + this.skinDesc() + " begins to feel stiff, as though it were getting harder. Before you know it, your whole body is covered with a layer of chitin, almost like full suit of segmented armor. However, unlike armor, this doesn\'t really afford you any protection, since you seem to have all the usual sensations through it like any other kind of skin.",False);
         if(this.legDesc(10) == "feet")
         {
            this.outputMainText(" And more of the chitin extends from your heels, making you stand higher without actually being taller as you walk more on your toes.",False);
         }
         this.skinType = 5;
      }
   }
   hasMuzzle = False
   if(this.lockFace == 0)
   {
      if(this.faceType == 21 || this.faceType == 31 || this.faceType == 61)
      {
         hasMuzzle = True
      }
      if(this.dominant == 1 && this.faceType != 10)
      {
         this.outputMainText("\r\r",False);
         if(hasMuzzle == True)
         {
            this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
         }
         this.outputMainText("Your face rounds out and your nose resizes so it nestles neatly between your eyes, reaching from your brow down to just above your mouth and looks much like a human\'s.",False);
         this.faceType = 10;
         hasMuzzle = False
      }
      if(this.dominant == 2 && (this.faceType != 20 || this.faceType != 21))
      {
         if(this.faceType != 20 && this.faceType != 21)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour facial demeanor softens and becomes more focused as your eyes grow wide and round, giving you a more considerate yet strong appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw seems to be a bit low and wide, your face looking longer than average. Your nose also appears wider to make up for the slightly stretched appearance.",False);
            }
            this.faceType = 20;
         }
         else if(this.faceType != 21 && this.horseAffinity > 70)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour muzzle widens along with your teeth until your smile is full and your teeth gently rest flatly upon each other. With your large eyes peering down the strong jaw, you seem to have a more equine appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw juts outward, growing forward, taking your mouth and the end of your nose with it. The bridge of your nose flattens as it reaches away from your face, molding around your upper teeth and forming a distinct muzzle. With its width and strength of character, you look much more like a horse.",False);
            }
            this.faceType = 21;
            hasMuzzle = True
         }
      }
      if(this.dominant == 3 && (this.faceType != 30 || this.faceType != 31))
      {
         if(this.faceType != 30 && this.faceType != 31)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour facial demeanor becomes more fierce as your eyes narrow slightly and your teeth become sharper, giving you a more carnivorous appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour teeth grow sharper and your eyes focus more. The tip of your nose also moistens and becomes softer, giving you a more feral appearance.",False);
            }
            this.faceType = 30;
         }
         else if(this.faceType != 31 && this.wolfAffinity > 70)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour muzzle narrows and your teeth grow long and sharp, your canines especially visible. With your narrow eyes peering down the vicious jaw, you seem to have a more lupin appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw juts outward, growing forward, taking your mouth and nose with it. The bridge of your nose flattens as it stretches from your brow, molding around your upper teeth and forming a distinct muzzle. The whole muzzle narrow and filled with sharp teeth, you look much more like a wolf.",False);
            }
            this.faceType = 31;
            hasMuzzle = True
         }
      }
      if(this.dominant == 4 && (this.faceType != 40 || this.faceType != 41))
      {
         if(this.faceType != 40 && this.faceType != 41)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your face flattens and your nose shrinks a bit, the tip changing color slightly and becoming softer. Your eyes grow narrow as well, making you seem like a hunter.",False);
            this.faceType = 40;
            hasMuzzle = False
         }
         else if(this.faceType != 41 && this.catAffinity > 60)
         {
            this.outputMainText("\r\rYour upper lip curls up at the center and long stiff thin whiskers sprout from the front of your cheeks. They\'re a bit sensitive when you touch them and give you a rather cat-like appearance.",False);
            this.faceType = 41;
         }
      }
      if(this.dominant == 5 && (this.faceType != 50 || this.faceType != 51))
      {
         if(this.faceType != 50 && this.faceType != 51)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour facial demeanor softens and becomes more focused as your eyes grow round and slightly droopy, giving you a domesticated appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw seems to be a bit low and wide, your face looking longer than average. Your nose also seems noticeably broader.",False);
            }
            this.faceType = 50;
         }
         else if(this.faceType != 51 && this.cowAffinity > 70)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour muzzle widens along with your teeth until your smile is full and your teeth gently rest flatly upon each other. With your large droopy eyes peering down the broad muzzle, you seem to have a more bovine appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw juts outward, growing forward, taking your mouth and the end of your nose with it. The bridge of your nose flattens as it reaches away from your face, molding around your upper teeth and forming a distinct muzzle. With its broadness and rather sedate appearance, you look much more like a cow.",False);
            }
            this.faceType = 51;
            hasMuzzle = True
         }
      }
      if(this.dominant == 6 && (this.faceType != 60 || this.faceType != 61))
      {
         if(this.faceType != 60 && this.faceType != 61)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour nostrils flatten into slits against your muzzle, giving you a more reptillian appearance.",False);
            }
            else
            {
               this.outputMainText("\r\rYour nose flattens until your nostrils are almost merely slits. Your lips also thin slightly, giving you a more reptillian appearance.",False);
            }
            this.faceType = 60;
         }
         else if(this.faceType != 61 && this.lizardAffinity > 70)
         {
            if(hasMuzzle == True)
            {
               this.outputMainText("\r\rYour muzzle narrows and flattens out a bit more, making you look more like some kind of lizard.",False);
            }
            else
            {
               this.outputMainText("\r\rYour jaw juts outward, growing forward, taking your mouth and nostrils with it, forming a sort of muzzle. It narrows almost to a point as it stretches, making you look like some kind of lizard.",False);
            }
            this.faceType = 61;
            hasMuzzle = True
         }
      }
      if(this.dominant == 7 && (this.faceType != 70 || this.faceType != 71))
      {
         if(this.faceType != 70 && this.faceType != 71)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your face flattens while your nose shrinks a bit, the tip changing color slightly and becoming softer and twitchy. Your eyes become round and soft, making you seem relatively meek.",False);
            this.faceType = 70;
            hasMuzzle = False
         }
         else if(this.faceType != 71 && this.rabbitAffinity > 60)
         {
            this.outputMainText("\r\rYour upper lip curls up at the center and long stiff thin whiskers sprout from the front of your cheeks. Your two front teeth stick out from the rest, almost protruding from your lips, making you look much like a bunny.",False);
            this.faceType = 71;
         }
      }
      if(this.dominant == 8 && (this.faceType != 80 || this.faceType != 81))
      {
         if(this.faceType != 80 && this.faceType != 81)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your lower face protrudes outward while your nose shrinks a bit, the tip changing color slightly and becoming softer and twitchy. Your eyes become slightly smaller yet more open, making you seem more cautious of your surroundings.",False);
            this.faceType = 80;
            hasMuzzle = False
         }
         else if(this.faceType != 81 && this.mouseAffinity > 60)
         {
            this.outputMainText("\r\rThin whiskers sprout from the front of your cheeks. Your two front teeth stick out from the rest, almost protruding from your lips, making you look much like a mouse.",False);
            this.faceType = 81;
         }
      }
      if(this.dominant == 9 && (this.faceType != 90 || this.faceType != 91))
      {
         if(this.faceType != 90 && this.faceType != 91)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your jaw becomes sharper while your nose grows larger from the rest of your face, almost have a hooked shape. Your eyes become wide and aware, making you seem more focused.",False);
            this.faceType = 90;
            hasMuzzle = False
         }
         else if(this.faceType != 91 && this.birdAffinity > 70)
         {
            this.outputMainText("\r\rYour upper lip molds up against your large nose, becoming stiff and hard while the bottom lip protrudes and matches the hooked shape. Your nose and mouth morph into a sturdy powerful beak, making you look much like a bird.",False);
            this.faceType = 91;
         }
      }
      if(this.dominant == 10 && (this.faceType != 100 || this.faceType != 101 || this.faceType != 102))
      {
         if(this.faceType != 100 && this.faceType != 101 && this.faceType != 102)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your cheeks become fuller, your face growing fatter, giving you a bit of a pudgy look.",False);
            this.faceType = 100;
            hasMuzzle = False
         }
         else if(this.faceType != 101 && this.faceType != 102 && this.pigAffinity > 60)
         {
            this.outputMainText("\r\rYour nose flattens and turns upward, your nostrils growing larger and pointing straight out, making you look much like a pig.",False);
            this.faceType = 101;
         }
         else if(this.faceType != 102 && this.pigAffinity > 85)
         {
            this.outputMainText("\r\rTwo of your lower teeth suddenly begin to surge outward, growing rapidly into two large tusks that stick out from your lips and curl upward.",False);
            this.faceType = 102;
         }
      }
      if(this.dominant == 11 && (this.faceType != 110 || this.faceType != 111))
      {
         if(this.faceType != 110 && this.faceType != 111)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your face stretches out along your nose a bit, the tip growing smaller and more narrow and becoming softer. Your eyes become soft and gentle, but with the potential to become defensive and vicious at any moment.",False);
            this.faceType = 110;
            hasMuzzle = False
         }
         else if(this.faceType != 111 && this.skunkAffinity > 60)
         {
            this.outputMainText("\r\rLong stiff thin whiskers sprout from the front of your cheeks. They\'re a bit sensitive when you touch them and give you a rather skunk-like appearance.",False);
            this.faceType = 111;
         }
      }
      if(this.dominant == 12 && (this.faceType != 120 || this.faceType != 121))
      {
         if(this.faceType != 120 && this.faceType != 121)
         {
            this.outputMainText("\r\r",False);
            if(hasMuzzle == True)
            {
               this.outputMainText("The muzzle that stretches from your face begins to shrink back, your jaw returning to the rest of your skull. ",False);
            }
            this.outputMainText("Your face flattens and your nose shrinks a bit, a chitinous \'bandage\' forming over the bridge of your nose to protect it. Your eyes grow much larger compared to the rest of your face, almost alien but still able to show plenty of emotion.",False);
            this.faceType = 120;
            hasMuzzle = False
         }
         else if(this.faceType != 121 && this.bugAffinity > 60)
         {
            this.outputMainText("\r\rYour lips grow large and plush, looking like they could suck nectar out of even the largest flowers. Your eyes also turn completely black, and with their large size they give you a rather bug-like appearance.",False);
            this.faceType = 121;
         }
      }
   }
   trace("Face :" + this.faceType);
   tempTailArray = [this.horseAffinity,this.wolfAffinity,this.catAffinity,this.cowAffinity,this.lizardAffinity,this.rabbitAffinity,this.mouseAffinity,this.pigAffinity,this.skunkAffinity,this.bugAffinity,this.humanTaurAffinity];
   tempTailArray.sort(16);
   maxTail = tempTailArray.pop();
   secondTail = tempTailArray.pop();
   maxNonTail = Math.max(this.humanAffinity);
   if(this.lockTail == 0)
   {
      if(this.tail < 1)
      {
         if(this.dominant == 2 && this.horseAffinity > maxNonTail + 15)
         {
            this.tail = 2;
         }
         if(this.dominant == 3 && this.wolfAffinity > maxNonTail + 15)
         {
            this.tail = 3;
         }
         if(this.dominant == 4 && this.catAffinity > maxNonTail + 15)
         {
            this.tail = 4;
         }
         if(this.dominant == 5 && this.cowAffinity > maxNonTail + 15)
         {
            this.tail = 5;
         }
         if(this.dominant == 6 && this.lizardAffinity > maxNonTail + 15)
         {
            this.tail = 6;
         }
         if(this.dominant == 7 && this.rabbitAffinity > maxNonTail + 15)
         {
            this.tail = 7;
         }
         if(this.dominant == 8 && this.mouseAffinity > maxNonTail + 15)
         {
            this.tail = 8;
         }
         if(this.dominant == 9 && this.birdAffinity > maxNonTail + 15)
         {
            this.tail = 9;
         }
         if(this.dominant == 10 && this.pigAffinity > maxNonTail + 15)
         {
            this.tail = 10;
         }
         if(this.dominant == 11 && this.skunkAffinity > maxNonTail + 15)
         {
            this.tail = 11;
         }
         if(this.dominant == 12 && this.bugAffinity > maxNonTail + 15)
         {
            this.tail = 12;
         }
         if(this.tail > 1)
         {
            this.outputMainText("\r\rYou feel a tickle upon your backside as your " + this.clothesBottom() + " feels tight. With a groan, the pressure builds behind you, until a tearing sound fills the air and the pain is gone. Checking your backside, you see a new " + this.tailDesc() + " tail bobbing above your " + this.buttDesc() + " bum. Next time you go to town, you\'ll be visiting a tailor to fix your clothes to account for your new appendage...",False);
         }
      }
      if(this.dominant == 1 && this.humanAffinity > maxTail + 10 && this.tail > 1)
      {
         this.tail = 0;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it shrinks into your back, disappearing altogether. You no longer have a tail.",False);
      }
      if(this.dominant == 2 && this.horseAffinity > secondTail + 10 && this.tail > 1 && this.tail != 2)
      {
         this.tail = 2;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it bursts into hundreds of long hairs. Any control you had over it before is gone, save for the muscles at the base that allow you to swish it with your mood and swat against your thighs. Just like a horse\'s.",False);
      }
      if(this.dominant == 3 && this.wolfAffinity > secondTail + 10 && this.tail > 1 && this.tail != 3)
      {
         this.tail = 3;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it widens with long hairs around a skeletal base. It wags with your mood and reflexes, though you don\'t really have control over it otherwise, and it\'s oh so fluffy. Just like a wolf\'s.",False);
      }
      if(this.dominant == 4 && this.catAffinity > secondTail + 10 && this.tail > 1 && this.tail != 4)
      {
         this.tail = 4;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it narrows with short hairs around a skeletal base. It wags with your mood and reflexes and likes to curl around your touch with limited control, and it\'s oh so soft. Just like a cat\'s.",False);
      }
      if(this.dominant == 5 && this.cowAffinity > secondTail + 10 && this.tail > 1 && this.tail != 5)
      {
         this.tail = 5;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it narrows with short hairs around a skeletal base and a tuft of long hair bursts at the tip. It sways lazily across your " + this.buttDesc() + " backside and you can swat yourself with the tip like a soft whip. Just like a cow\'s.",False);
      }
      if(this.dominant == 6 && this.lizardAffinity > secondTail + 10 && this.tail > 1 && this.tail != 6)
      {
         this.tail = 6;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it thickens at the base and narrows gradually to a point. It\'s quite agile, able to move at your whim, the tip even being slightly prehensile. Much like a lizard\'s.",False);
      }
      if(this.dominant == 7 && this.rabbitAffinity > secondTail + 10 && this.tail > 1 && this.tail != 7)
      {
         this.tail = 7;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as shrinks into your back, exploding into a tuft of soft puffy hair before it disappears. It wiggles above your " + this.buttDesc() + " bum cutely and quite fluffy. Much like a rabbit\'s.",False);
      }
      if(this.dominant == 8 && this.mouseAffinity > secondTail + 10 && this.tail > 1 && this.tail != 8)
      {
         this.tail = 8;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it narrows with fine hairs around a skeletal base. Thin and lithe, the fur doesn\'t really hide the pink skin underneath. It whips above your " + this.buttDesc() + " bum and you can curl it around with limited control. Just like a mouse\'s.",False);
      }
      if(this.dominant == 9 && this.birdAffinity > secondTail + 10 && this.tail > 1 && this.tail != 9)
      {
         this.tail = 9;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it shrinks to your back and burst into a plume of feathers. Long and somewhat controllable, you can adjust their direction for aerodynamic turning. Just like a bird\'s.",False);
      }
      if(this.dominant == 10 && this.pigAffinity > secondTail + 10 && this.tail > 1 && this.tail != 10)
      {
         this.tail = 10;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it shrinks into your back, shriveling in girth and coiling around. It twitches a bit when you try to wiggle it and you can try to straighten it out but it pops right back into its curly state. Just like a pig\'s.",False);
      }
      if(this.dominant == 11 && this.skunkAffinity > secondTail + 10 && this.tail > 1 && this.tail != 11)
      {
         this.tail = 11;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it poofs into a large, long, wide fluffy tail that curls up behind your back with the pointed tip gently sagging away from you. Two parrallel stripes run closely together from the tip of your tail, widening with the tail, and down to the base",False);
         if(this.skinType == 2 && this.skunkAffinity >= 40)
         {
            this.outputMainText(" where it meets up with the stripes of your fur",False);
         }
         this.outputMainText(". Just like a skunk\'s.",False);
      }
      if(this.dominant == 12 && this.bugAffinity > secondTail + 10 && this.tail > 1 && this.tail != 12)
      {
         this.tail = 12;
         this.outputMainText("\r\rYour tail begins to tingle. As you turn around, you watch as it bloats up, growing nearly as thick as your waist and nearly as stout. It\'s so big and weighty with flesh that you can hardly move it, merely resting against your " + this.buttDesc() + " butt. And at the tip where it\'s rather blunt, you can feel another hole. It\'s not terribly large, but it looks large enough to fit a small-ish egg, your finger able to easily poke up inside to feel the warm moist interior. If you were to venture a guess, it seems more like an ovipositor than an actual tail, though such a large change to your anatomy would be impossible, so what could it be for?",False);
      }
      if(this.weapon == 127 && this.tail != 4 && this.tail != 5 && this.tail != 6 && this.tail != 8)
      {
         this.weapon = 10;
      }
   }
   maxNonWings = Math.max(this.humanAffinity,this.horseAffinity,this.wolfAffinity,this.catAffinity,this.cowAffinity,this.lizardAffinity,this.rabbitAffinity,this.mouseAffinity,this.pigAffinity);
   maxWings = Math.max(this.birdAffinity);
   if(this.wings < 1 && maxWings > maxNonWings + 60)
   {
      if(this.dominant == 9 && this.birdAffinity > maxNonWings + 60)
      {
         this.outputMainText("\r\rA sharp pain engulfs your back, centered around your shoulder blades. You keel forward, falling to your hands and " + this.legDesc(6) + " as you try to brace yourself against the sharp ache. Then, you cry out as feathers tear through your " + this.clothesTop() + ", stretching out across new appendages. As soon as they grow, the pain stops and you gather yourself.\r\rStanding, you flap your new feathery wings. While not strong enough to carry you long distances, they\'ll definitely help you flee from unwanted threats.",False);
         this.wings = 9;
      }
      this.runMod += 20;
   }
   if(this.wings > 0 && maxNonWings > maxWings + 60)
   {
      this.outputMainText("\r\rYour wings feel strange and rapidly begin to shrivel. Shrinking down, they disappear into your shoulder blades, the " + this.skinDesc() + " left smooth as though there were never anything there. You have lost your wings, it seems.",False);
      this.runMod -= 20;
      this.wings = 0;
   }
   if(this.wings > 0 && this.dominant != this.wings)
   {
   }
   if(this.lockEars == 0)
   {
      if(this.dominant == 1 && this.humanAffinity > second + 15 && this.ears != 1)
      {
         this.ears = 1;
         this.outputMainText("\r\rYour ears twitch as they become rounded and hug the sides of you head, looking more like a human\'s.",False);
      }
      if(this.dominant == 2 && this.horseAffinity > second + 15 && this.ears != 2)
      {
         this.ears = 2;
         this.outputMainText("\r\rYour ears twitch as they become rounded and pointed at the tip, flicking atop your head, looking more like a horse\'s.",False);
      }
      if(this.dominant == 3 && this.wolfAffinity > second + 15 && this.ears != 3)
      {
         this.ears = 3;
         this.outputMainText("\r\rYour ears twitch as they become triangular, standing pert atop your head, looking more like a wolf\'s.",False);
      }
      if(this.dominant == 4 && this.catAffinity > second + 15 && this.ears != 4)
      {
         this.ears = 4;
         this.outputMainText("\r\rYour ears twitch as they become triangular, standing pert atop your head, looking more like a cat\'s.",False);
      }
      if(this.dominant == 5 && this.cowAffinity > second + 15 && this.ears != 5)
      {
         this.ears = 5;
         this.outputMainText("\r\rYour ears twitch as they become rounded and large, standing several inches out from the sides of your head, looking more like a cow\'s.",False);
      }
      if(this.dominant == 6 && this.lizardAffinity > second + 15 && this.ears != 6)
      {
         this.ears = 6;
         this.outputMainText("\r\rYour ears feel quite strange, shrinking into the sides of your head before they disappear, becoming sleek holes.",False);
      }
      if(this.dominant == 7 && this.rabbitAffinity > second + 15 && this.ears != 7)
      {
         this.ears = 7;
         this.outputMainText("\r\rYour ears twitch as they become quite long, standing several inches high atop your head, looking more like a rabbit\'s.",False);
      }
      if(this.dominant == 8 && this.mouseAffinity > second + 15 && this.ears != 8)
      {
         this.ears = 8;
         this.outputMainText("\r\rYour ears twitch as they grow larger and larger, rounding out into thin discs standing out from the sides of your head, looking more like a mouse\'s.",False);
      }
      if(this.dominant == 9 && this.birdAffinity > second + 15 && this.ears != 9)
      {
         this.ears = 9;
         this.outputMainText("\r\rYour ears feel quite strange, shrinking into the sides of your head before disappearing behind a small patch of feathers, looking more like a bird\'s.",False);
      }
      if(this.dominant == 10 && this.pigAffinity > second + 15 && this.ears != 10)
      {
         this.ears = 10;
         this.outputMainText("\r\rYour ears feel quite strange, growing long and triangular out the sides of your head, folding over and dropping as they get too long, looking more like a pig\'s.",False);
      }
      if(this.dominant == 11 && this.skunkAffinity > second + 15 && this.ears != 11)
      {
         this.ears = 11;
         this.outputMainText("\r\rYour ears twitch as they become rounded and small, standing pert atop your head, looking more like a skunk\'s.",False);
      }
      if(this.dominant == 12 && this.bugAffinity > second + 15 && this.ears != 12)
      {
         this.ears = 12;
         this.outputMainText("\r\rYour ears twitch as they grow long and narrow to a point on the sides of your head, becoming a vibrant color while the lobes become wavy with a delicate design, looking almost like butterfly wings.",False);
      }
   }
   twoBoob = Math.max(this.twoBoobAffinity,this.humanAffinity,this.horseAffinity,this.cowAffinity,this.lizardAffinity,this.rabbitAffinity,this.mouseAffinity,this.birdAffinity);
   sixBoob = Math.max(this.sixBoobAffinity,this.catAffinity,this.wolfAffinity,this.skunkAffinity);
   fourBoob = Math.max(this.fourBoobAffinity);
   eightBoob = Math.max(this.eightBoobAffinity,this.pigAffinity);
   tenBoob = Math.max(this.tenBoobAffinity,this.bugAffinity);
   nonTwoBoob = Math.max(sixBoob,fourBoob,eightBoob,tenBoob);
   nonSixBoob = Math.max(twoBoob,fourBoob,eightBoob,tenBoob);
   nonFourBoob = Math.max(twoBoob,sixBoob,eightBoob,tenBoob);
   nonEightBoob = Math.max(twoBoob,sixBoob,fourBoob,tenBoob);
   nonTenBoob = Math.max(twoBoob,fourBoob,eightBoob,sixBoob);
   if(this.lockBreasts == 0)
   {
      if(twoBoob > nonTwoBoob + 20 && this.boobTotal != 2)
      {
         if(this.boobTotal == 4)
         {
            this.outputMainText("\r\rYour lower chest tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", both growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your second set of nipples disappear flat into your " + this.skinDesc() + ", leaving you with only the highest pair on your chest.",False);
         }
         if(this.boobTotal == 6)
         {
            this.outputMainText("\r\rYour lower chest and belly tickle",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", both growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your extra sets of nipples disappear flat into your " + this.skinDesc() + ", leaving you with only the primary pair on your chest.",False);
         }
         if(this.boobTotal == 8)
         {
            this.outputMainText("\r\rYour lower chest and belly tickle",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", both growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your extra sets of nipples disappear flat into your " + this.skinDesc() + ", leaving you with only the primary pair on your chest, which seems to have grown larger.",False);
         }
         if(this.boobTotal == 10)
         {
            this.outputMainText("\r\rYour lower chest and belly tickle",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", both growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your extra sets of nipples disappear flat into your " + this.skinDesc() + ", leaving you with only the primary pair on your chest, which seems to have grown larger.",False);
         }
         this.boobTotal = 2;
      }
      if(fourBoob > nonFourBoob + 20 && this.boobTotal != 4)
      {
         if(this.boobTotal == 2)
         {
            this.outputMainText("\r\rYour lower chest, close beneath your nipples, begins to tickle. A new pair of sensitive areolas form amongst your " + this.skinDesc() + ", creating an extra row of breasts beneath the originals.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The new nipples protrude as fleshy mounds form from beneath them. The new boobs wobble as they grow to the same size of your original pair, lifting the originals slightly with their girth.\tWhen you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 6)
         {
            this.outputMainText("\r\rYour belly tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your bottom set of nipples disappear flat into your " + this.skinDesc() + ", while your middle pair swells to match the first, leaving you with two sets of equally sized breasts, the top resting upon the bottom.",False);
         }
         if(this.boobTotal == 8)
         {
            this.outputMainText("\r\rYour belly tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your two lowest sets of nipples disappear flat into your " + this.skinDesc() + ", while the other two pairs swell slightly, leaving you with two sets of breasts larger than before.",False);
         }
         if(this.boobTotal == 10)
         {
            this.outputMainText("\r\rYour belly tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your three lowest sets of nipples disappear flat into your " + this.skinDesc() + ", while the other two pairs swell slightly, leaving you with two sets of breasts larger than before.",False);
         }
         this.boobTotal = 4;
      }
      if(sixBoob > nonSixBoob + 20 && this.boobTotal != 6)
      {
         if(this.boobTotal == 2)
         {
            this.outputMainText("\r\rYour lower chest and belly tickle. Four new nipples form amongst your " + this.skinDesc() + ", a fresh pair below your original two and another pair below that, leaving you with three rows of two breasts from your chest down to your upper belly.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The nipples protrude as fleshy mounds form beneath them. Breast-flesh wobbles, each row a fraction in size of the one above it. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 4)
         {
            this.outputMainText("\r\rYour belly tickles. Two new nipples form amongst your " + this.skinDesc() + ", right below your second pair on your upper belly, leaving you with three rows of two breasts.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The nipples protrude as fleshy mounds form beneath them, while your second pair seems to shrink in turn. Breast-flesh wobbles, each row a fraction in size of the one above it. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 8)
         {
            this.outputMainText("\r\rYour lower belly tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your lowest set of nipples disappear flat into your " + this.skinDesc() + ", while the next lowest pair shrinks and the top pair swells, giving you a slope of three rows of breasts.",False);
         }
         if(this.boobTotal == 10)
         {
            this.outputMainText("\r\rYour lower belly and the area above your crotch tickle",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your two lowest sets of nipples disappear flat into your " + this.skinDesc() + ", while the next lowest pair shrinks and the top pair swells, giving you a slope of three rows of breasts.",False);
         }
         this.boobTotal = 6;
      }
      if(eightBoob > nonEightBoob + 20 && this.boobTotal != 8)
      {
         if(this.boobTotal == 2)
         {
            this.outputMainText("\r\rYour lower chest and belly, close beneath your nipples, begin to tickle. A new pair of sensitive areolas form amongst your " + this.skinDesc() + ", creating an extra row of breasts beneath the originals. The process repeats twice more, for a total of 8 breasts from your chest to your lower belly! And they\'re all slightly smaller than your original pair.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The new nipples protrude as fleshy mounds form from beneath them. The new boobs wobble as they grow to the same size of your original pair, lifting the originals slightly with their girth.\tWhen you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 4)
         {
            this.outputMainText("\r\rYour chest and belly tickle. Four new nipples form amongst your " + this.skinDesc() + ", right below your second pair above your belly, leaving you with four rows of two breasts, from your chest to your lower belly.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" Your original breasts shrink a little to match the ingrowing ones, until they\'re all the same size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 6)
         {
            this.outputMainText("\r\rYour belly tickles. Two new nipples form amongst your " + this.skinDesc() + ", right below your second pair above your belly, leaving you with four rows of two breasts, from your chest to your lower belly.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The lower pairs continue to grow while your top pair shrinks a little, all equalizing in size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 10)
         {
            this.outputMainText("\r\rThe area above your crotch tickles",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(", growing much lighter",False);
            }
            this.outputMainText(". Checking, you catch your two lowest sets of nipples disappear flat into your " + this.skinDesc() + ", while the rest grow slightly larger.",False);
         }
         this.boobTotal = 8;
      }
      if(tenBoob > nonTenBoob + 20 && this.boobTotal != 10)
      {
         if(this.boobTotal == 2)
         {
            this.outputMainText("\r\rYour lower chest and belly, close beneath your nipples, begin to tickle. A new pair of sensitive areolas form amongst your " + this.skinDesc() + ", creating an extra row of breasts beneath the originals. The process repeats three more times, for a total of 10 breasts from your chest to your just above your crotch! And they\'re all slightly smaller than your original pair.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The new nipples protrude as fleshy mounds form from beneath them. The new boobs wobble as they grow to the same size of your original pair, lifting the originals slightly with their girth.\tWhen you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 4)
         {
            this.outputMainText("\r\rYour chest and belly tickle. Six new nipples form amongst your " + this.skinDesc() + ", right below your second pair above your belly, leaving you with five rows of two breasts, from your chest to just above your crtoch.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" Your original breasts shrink a little to match the ingrowing ones, until they\'re all the same size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 6)
         {
            this.outputMainText("\r\rYour lower belly  and the area above your crotch tickle. Four new nipples form amongst your " + this.skinDesc() + ", right below your third pair, leaving you with five rows of two breasts, from your chest down to your crotch.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The lower pairs continue to grow while your top pair shrinks a little, all equalizing in size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         if(this.boobTotal == 8)
         {
            this.outputMainText("\r\rThe area above your crotch tickles. Two new nipples form amongst your " + this.skinDesc() + ", right below your fourth pair below your belly, leaving you with five rows of two breasts, from your chest to your crotch.",False);
            if(this.breastSize > 4)
            {
               this.outputMainText(" The lower pairs continue to grow while your top pair shrinks a little, all equalizing in size. When you head back to town, you\'ll be covering your extra indecency with your arms the best you can while you head for the tailor to update your " + this.clothesTop() + " accordingly.",False);
            }
         }
         this.boobTotal = 10;
      }
   }
   bipedal = Math.max(this.humanAffinity,this.horseAffinity,this.wolfAffinity,this.catAffinity,this.cowAffinity,this.lizardAffinity,this.rabbitAffinity,this.mouseAffinity,this.birdAffinity,this.pigAffinity);
   bipedalDigiPaw = Math.max(this.skunkAffinity);
   otherLegs = [this.cowTaurAffinity,this.humanTaurAffinity];
   legArray = [bipedal,bipedalDigiPaw,0];
   legArray = legArray.concat(otherLegs);
   legArray.sort(16);
   legArray.pop();
   secondLegs = legArray.pop();
   if(this.lockLegs == 0)
   {
      if(bipedalDigiPaw > secondLegs + 50 && this.legType != 1)
      {
         this.legChange(1);
      }
      if(bipedal > secondLegs + 50 && this.legType != 0)
      {
         this.legChange(0);
      }
      if(this.cowTaurAffinity > secondLegs + 50 && this.legType != 1001)
      {
         this.legChange(1001);
      }
      if(this.humanTaurAffinity > secondLegs + 50 && this.legType != 1002)
      {
         this.legChange(1002);
      }
   }
   nip0 = Math.max(this.humanAffinity,this.horseAffinity,this.wolfAffinity,this.catAffinity,this.lizardAffinity,this.rabbitAffinity,this.mouseAffinity,this.birdAffinity,this.pigAffinity);
   nip1 = Math.max(this.cowAffinity);
   nip2 = Math.max(this.bugAffinity);
   nonNip0 = Math.max(nip1,nip2);
   nonNip1 = Math.max(nip0,nip2);
   nonNip2 = Math.max(nip0,nip1);
   if(this.lockNipples == 0)
   {
      if(nip0 > nonNip0 + 60 && this.nipType != 0)
      {
         if(this.nipType == 1)
         {
            this.outputMainText("\r\rMany of your nipples begin to tickle. They begin to shrink beneath your " + this.clothesTop() + ", receding back into your breasts. As you lift the clothing away to see what\'s going on, the extra three nipples on each of your breasts fade away, leaving you with only one each.",False);
         }
         if(this.nipType == 2)
         {
            this.outputMainText("\r\rYour nipples pop out from your breast, no longer sunken or hidden within.",False);
         }
         this.nipType = 0;
      }
      if(nip1 > nonNip1 + 60 && this.nipType != 1)
      {
         if(this.nipType == 2)
         {
            this.outputMainText("\r\rYour nipples pop out from your breast, no longer sunken or hidden within.",False);
         }
         if(this.nipType == 0 || this.nipType == 2)
         {
            this.outputMainText("\r\rSpots begin to tingle around your nipples. Your hand roves under your " + this.clothesTop() + " to inspect the areas, noticeably more sensitive than before. The patches grow softer and puff up beneath your fingertips, feeling rather... familiar? Pulling your " + this.clothesTop() + " " + this.pullUD(1) + ", you can see extra nipples form around the ones you already have, complete with darkened areoles and matching size.\r\rYour breasts now each have four nipples equidistant from each other, just as functional as the originals, and just as sensitive, each looking almost like a cow\'s udder...",False);
         }
         this.nipType = 1;
      }
      if(nip2 > nonNip2 + 60 && this.nipType != 2)
      {
         if(this.nipType == 1)
         {
            this.outputMainText("\r\rMany of your nipples begin to tickle. They begin to shrink beneath your " + this.clothesTop() + ", receding back into your breasts. As you lift the clothing away to see what\'s going on, the extra three nipples on each of your breasts fade away, leaving you with only one each.",False);
         }
         if(this.nipType == 0 || this.nipType == 1)
         {
            this.outputMainText("\r\rYour nipples sink into your breasts, becoming inverted slits within your areola, only coming out when aroused.",False);
         }
         this.nipType = 2;
      }
   }
   if(this.eggLaying > 0)
   {
      egg0 = Math.max(this.lizardAffinity,this.birdAffinity);
      egg1 = Math.max(this.bugAffinity);
      nonEgg0 = Math.max(egg1);
      nonEgg1 = Math.max(egg0);
      if(egg0 > nonEgg0 + 20 && this.eggType != 0)
      {
         this.outputMainText("\r\rYou sense your womb shifting, the eggs inside feeling like their forming somehow differently than they did before.",False);
         if(this.eggType == 1)
         {
            this.eggMaxTime += 22;
         }
         this.eggType = 0;
      }
      if(egg1 > nonEgg1 + 20 && this.eggType != 1)
      {
         this.outputMainText("\r\rYou sense your womb shifting, the eggs inside feeling like their forming somehow differently than they did before.",False);
         if(this.eggType == 0)
         {
            this.eggMaxTime -= 22;
         }
         this.eggType = 1;
      }
   }
   if(this.lockCock == 0)
   {
      if(this.dominant == 1 && this.humanAffinity > second + 25 && this.human > 0 && this.cockTotal > 0 && this.humanCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to see " + this.oneYour(1) + " cock" + this.plural(1) + " hanging out from your body, limp and flaccid. It\'s smooth and fleshy, easily teased into erection. Its skin is slightly less sensitive, but the thick mushroom-like head twitches in your grip. It looks very much like a human\'s.",False);
         ++this.humanCocks;
         this.cockLoss();
      }
      if(this.dominant == 2 && this.horseAffinity > second + 25 && this.horse > 0 && this.cockTotal > 0 && this.horseCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to watch as a thick sheath envelopes " + this.oneYour(1) + " cock" + this.plural(1) + ". Relaxing your muscles, the cock slowly droops out over your " + this.clothesBottom() + ". It\'s long and smooth, with the prepuce only reaching halfway down its length making an obvious ring. The head is flat and as you knead it in your hand, it flares wide. It looks very much like a horse\'s.",False);
         ++this.horseCocks;
         this.cockLoss();
      }
      if(this.dominant == 3 && this.wolfAffinity > second + 25 && this.wolf > 0 && this.cockTotal > 0 && this.wolfCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to watch as a thin sheath envelopes " + this.oneYour(1) + " cock" + this.plural(1) + ". Flexing your muscles, " + this.oneYour(1) + " cock" + this.plural(1) + " slowly pushes out, red and hard, no matter how aroused you are. It\'s veiny and smooth, already a bit moist from being within the sheath. The head narrows off to a pointy tip where you can feel the urethra resides. It looks very much like a wolf\'s.",False);
         ++this.wolfCocks;
         this.cockLoss();
      }
      if(this.dominant == 4 && this.catAffinity > second + 25 && this.cat > 0 && this.cockTotal > 0 && this.catCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to watch as a thin sheath envelopes " + this.oneYour(1) + " cock" + this.plural(1) + ". Flexing your muscles, " + this.oneYour(1) + " cock" + this.plural(1) + " slowly pushes out, pink and soft. It\'s smooth and already a bit moist from being within the sheath, covered in tiny barbs that feel rough as your hand strokes against them. The head narrows off to a pointy tip where you can feel the urethra resides. It looks very much like a cat\'s.",False);
         ++this.catCocks;
         this.cockLoss();
      }
      if(this.dominant == 6 && this.lizardAffinity > second + 25 && this.lizard > 0 && this.cockTotal > 0 && this.lizardCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to watch as your cock" + this.plural(1) + " sink" + this.plural(3) + " into your body, leaving behind a small slit at the front. Flexing your muscles, the slit pushes open and " + this.oneYour(1) + " cock" + this.plural(1) + " slowly pushes out, looking quite purple. It\'s bumpy, with ribs along its upper side and a head that looks bulbous before rapidly narrowing into a pointy tip where you can feel the urethra resides. You think it looks like a lizard\'s?",False);
         ++this.lizardCocks;
         this.cockLoss();
      }
      if(this.dominant == 7 && this.rabbitAffinity > second + 25 && this.rabbit > 0 && this.cockTotal > 0 && this.rabbitCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to watch as a thin sheath envelopes " + this.oneYour(1) + " cock" + this.plural(1) + ". Flexing your muscles, " + this.oneYour(1) + " cock" + this.plural(1) + " slowly pushes out, red and pointy. It\'s smooth and already a bit moist from being within the sheath, its whole length gradually narrowing to the pointy tip, reminiscent of a carrot. It looks very much like a rabbit\'s.",False);
         ++this.rabbitCocks;
         this.cockLoss();
      }
      if(this.dominant == 12 && this.bugAffinity > second + 25 && this.bug > 0 && this.cockTotal > 0 && this.bugCocks < this.cockTotal)
      {
         this.outputMainText("\r\rYour " + this.hipDesc() + " hips twitch as " + this.oneYour(1) + " cock" + this.plural(1) + " begins to feel strange. You open your " + this.clothesBottom() + " to see what is happening, only to see " + this.oneYour(1) + " cock" + this.plural(1) + " hanging out from your body, with four fleshy spikes pointing back towards you from the rim of the glans, not hard enough to hurt but enough to definitely get a grip inside tender walls. The underside is also adorned with extra grip, a ridge following down the middle with many bumps along its length. You\'re not really sure what it is, but some bugs do have rather... \'wild\' penises that could come close.",False);
         ++this.bugCocks;
         this.cockLoss();
      }
   }
   this.human = 0;
   this.horse = 0;
   this.wolf = 0;
   this.cat = 0;
   this.cow = 0;
   this.lizard = 0;
   this.rabbit = 0;
   this.mouse = 0;
   this.bird = 0;
   this.pig = 0;
   this.skunk = 0;
   this.bug = 0;
   if(this.currentText == "Something feels odd...")
   {
      this.outputMainText("",True);
      this.doProcess();
   }
   else
   {
      this.doEnd();
   }}}}
def CockChange(sizeChange:int, totalChange:int):
   global humanAffinity, horseAffinity, wolfAffinity, catAffinity, lizardAffinity, rabbitAffinity, bugAffinity, dominant, nonCock, cockSize, cockTotal, vagTotal, gender, balls, ballSize, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, rabbitCocks, bugCocks, maxCock, showBalls
   maxCock = max(humanAffinity, horseAffinity, wolfAffinity, catAffinity, lizardAffinity, rabbitAffinity, bugAffinity)
   nonCock = False
   if (dominant == 5) or (dominant == 8) or (dominant == 9) or (dominant == 10) or (dominant == 11):
      nonCock = True
   if (((cockSize + sizeChange) <= 0) or ((cockTotal + totalChange) < 1)) and (cockSize > 0) and (cockTotal > 0):
      OutputMainText("\n" + "\n" + "You shiver a little as your cock" + Plural(1) + " and balls shrink into your body, disappearing",False)
      if vagTotal > 0:
         OutputMainText(", leaving you with only your vagina" + Plural(2) + " and making you solely female.",False)
         gender = 2
      if vagTotal < 1:
         OutputMainText(", leaving you with no genitals whatsoever. This is going to make things tough...",False)
         gender = 0
      balls = 0
      Stats(0,0,-(2 * cockTotal),0)
      ballSize = 0
      cockSize = 0
      cockTotal = 0
      humanCocks = 0
      horseCocks = 0
      wolfCocks = 0
      catCocks = 0
      lizardCocks = 0
      rabbitCocks = 0
      bugCocks = 0
   elif((cockTotal + totalChange) > 0) and (cockTotal < 1):
      OutputMainText("\n" + "\n" + "A strange sensation of arousal engulfs your groin. Your " + ClothesBottom() + " grows tight as you feel something swell within. You don't have much time to pull " + PullUD(2) + " your " + ClothesBottom() + " as flesh bulges over the fitted garment. Throbbing and dripping with pre, a fresh, new ",False)
      if (dominant == 1) or (nonCock == True) and (maxCock == humanAffinity):
         OutputMainText("human ",False)
         humanCocks += 1
      elif (dominant == 2) or (nonCock == True) and (maxCock == horseAffinity):
         OutputMainText("equine ",False)
         horseCocks += 1
      elif (dominant == 3) or (nonCock == True) and (maxCock == wolfAffinity)
         OutputMainText("canine ",False)
         wolfCocks += 1
      elif (dominant == 4) or (nonCock == True) and (maxCock == catAffinity):
         OutputMainText("feline ",False)
         catCocks += 1
      elif (dominant == 6) or (nonCock == True) and (maxCock == lizardAffinity):
         OutputMainText("reptillian ",False)
         lizardCocks += 1
      elif (dominant == 7) or (nonCock == True) and (maxCock == rabbitAffinity):
         OutputMainText("lapin ",False)
         rabbitCocks += 1
      elif (dominant == 12) or (nonCock == True) and (maxCock == bugAffinity):
         OutputMainText("insectile ",False)
         bugCocks += 1
      OutputMainText("penis stands erect and balls to match settle within your crotch beneath",False)
      if vagTotal > 0:
         OutputMainText(", slipping into your " + VulvaDesc() + " lips. You now are considered a cross between genders, a herm.",False)
         gender = 3
      else:
         OutputMainText(". You have now graduated from androgynous to male, congratulations!",False)
         gender = 1
      ballSize = 1
      balls = 2
      showBalls = True
      cockSize = 1
      Stats(0,0,2,0)
      cockTotal = 1
      cockSize += sizeChange
      totalChange -= 1
      CockChange(0,totalChange)
   elif (totalChange > 0) and (cockTotal > 0):
      this.outputMainText("\r\rA strange sensation of arousal engulfs your groin. Your " + this.clothesBottom() + " grows tight as you feel something swell within. You don\'t have much time to open your " + this.clothesBottom() + " as flesh bulges over the fitted garment. Throbbing and dripping with pre, fresh and new,",False);
      if (totalChange > 1):
         OutputMainText(" " + totalChange,False)
      if (dominant == 1) or ((nonCock == True) and (maxCock == humanAffinity)):
         OutputMainText(" human ",False)
         humanCocks += totalChange
      elif (dominant == 2) or ((nonCock == True) and (maxCock == horseAffinity)):
         OutputMainText(" equine ",False)
         horseCocks += totalChange
      elif (dominant == 3) or ((nonCock == True) and (maxCock == wolfAffinity)):
         OutputMainText(" canine ",False)
         wolfCocks += totalChange
      elif (dominant == 4) or ((nonCock == True) and (maxCock == this.catAffinity)):
         OutputMainText(" feline ",False)
         catCocks += totalChange
      elif (dominant == 6) or ((nonCock == True) and (maxCock == lizardAffinity)):
         OutputMainText(" reptillian ",False)
         lizardCocks += totalChange
      elif (dominant == 7) or ((nonCock == True) and (maxCock == rabbitAffinity)):
         OutputMainText(" lapin ",False)
         rabbitCocks += totalChange
      elif (dominant == 12) or ((nonCock == True) and (maxCock == bugAffinity)):
         OutputMainText(" insectile ",False)
         bugCocks += totalChange
      OutputMainText("penis",False)
      if (totalChange > 1):
         OutputMainText("es",False)
      OutputMainText(" standing erect with the other" + Plural(1) + ".",False)
      Stats(0,0,2 * totalChange,0)
      cockTotal += totalChange
      cockSize += sizeChange
   elif (totalChange < 0) and (cockTotal > 0) and (cockSize > 0):
      this.outputMainText("\n" + "\n" + "You notice an odd sensation of numbness within your groin. Your " + ClothesBottom() + " feels looser, something going missing within. By the time you open your " + ClothesBottom() + " you notice that you have lost something.",False)
      cockTotal += totalChange
      while (totalChange < 0):
         CockLoss()
         totalChange += 1
      Stats(0,0,2 * totalChange,0)
   elif (cockTotal > 0):
      cockSize += sizeChange

def CockLoss():
   global humanCocks, humanAffinity, horseCocks, horseAffinity, wolfCocks, wolfAffinity, catCocks, catAffinity, lizardCocks, lizardAffinity, rabbitCocks, rabbitAffinity, bugCocks, bugAffinity
   hasHumanCock = 101
   hasHorseCock = 101
   hasWolfCock = 101
   hasCatCock = 101
   hasLizardCock = 101
   hasRabbitCock = 101
   hasBugCock = 101
   if (humanCocks > 0):
      hasHumanCock = humanAffinity
   if (horseCocks > 0):
      hasHorseCock = horseAffinity
   if (wolfCocks > 0):
      hasWolfCock = wolfAffinity
   if (catCocks > 0):
      hasCatCock = catAffinity
   if (lizardCocks > 0):
      hasLizardCock = lizardAffinity
   if (rabbitCocks > 0):
      hasRabbitCock = rabbitAffinity
   if (bugCocks > 0):
      hasBugCock = bugAffinity
   minCock = min(hasHumanCock,hasHorseCock,hasWolfCock,hasCatCock,hasLizardCock,hasRabbitCock,hasBugCock)
   if (minCock == humanAffinity) and (humanCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one human cock.",False)
      humanCocks -= 1
   elif (minCock == horseAffinity) and (horseCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one horse cock.",False)
      horseCocks -= 1
   elif (minCock == wolfAffinity) and (wolfCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one wolf cock.",False)
      wolfCocks -= 1
   elif (minCock == catAffinity) and (catCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one cat cock.",False)
      catCocks -= 1
   elif (minCock == lizardAffinity) and (lizardCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one lizard cock.",False)
      lizardCocks -= 1
   elif (minCock == rabbitAffinity) and (rabbitCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one rabbit cock.",False)
      rabbitCocks -= 1
   elif (minCock == bugAffinity) and (bugCocks > 0):
      OutputMainText("\n" + "\n" + "You have lost one bug cock.",False)
      bugCocks -= 1

!def VagChange(sizeChange:int, totalChange:int):
   global cockSnakePreg, pregArray, birthCount, sen, vagSize, vagTotal, cockTotal, gender, vulvaSize, clitSize
   birthCount = 0
   if (cockSnakePreg > 0):
      birthCount = 0
      if (sizeChange < 0) or (totalChange < 0):
         OutputMainText("\n" + "\n" + "With the changing size of your passageway, you feel a sudden squirming within your womb. You brace yourself as you feel the cock-snake within slither its way through your passage. Your " + ClothesBottom() + " becomes drenched by your feminine lubricant as a bunch of it splashes out, the phallic head of the snake breaching your " + VulvaDesc() + " lips. Its body constantly drags over your sensitive flesh as it flees what is about to come, making you shudder in mild orgasm as the creature descends down your " + LegDesc(1) + ". You gasp and regain yourself, the snake slithering away. It must have been frightened by the shrinking of its home and fleed...",False)
         cockSnakePreg = 0
         i = 0
         while (i < len(pregArray)):
            if (pregArray[i + 1] == 503):
               pregArray[i] = False
               pregArray[i + 3] = 0
               birthCount += 1
               if (birthCount == 2):
                  OutputMainText("\n" + "\n" + "And it's not the first; you shudder again as another snake in another womb escapes out from your " + ClothesBottom() + " and down your " + LegDesc(1) + ", fleeing like the first.",False)
               if (birthCount == 3):
                  OutputMainText("\n" + "\n" + "Followed by another...",False)
               if (birthCount > 3):
                  OutputMainText("\n" + "\n" + "And another...",False)
               DoLust(-math.floor(sen / 4),2,2)
            i += 5
         cockSnakePreg = 0
   if (vagSize + sizeChange <= 0) or (vagTotal + totalChange < 1) and (vagSize > 0) and (vagTotal > 0):
      OutputMainText("\n" + "\n" + "Sudden intense cramping makes you double over. A slight moistness in your " + ClothesBottom() + " causes your hand to inspect the situation. It reaches your once " + VulvaDesc() + " vulva just in time to feel it shrink to nothing, sealing over with " + SkinDesc() + ". It seems you have lost your vagina" + Plural(2) + ", ",False)
      if (cockTotal > 0):
         OutputMainText("leaving only your cock" + Plural(1) + " remaining. You are now considered only male.",False)
         gender = 1
      if (cockTotal < 1):
         OutputMainText("leaving you with no genetalia, completely androgynous where it matters. Things might be difficult...",False)
         gender = 0
      VagBellyChange(sizeChange,totalChange)
      Stats(0,0,2 * this.vagTotal,0)
      vagSize = 0
      vagTotal = 0
      vulvaSize = 0
      clitSize = 0
      i = 0
      while (i < len(pregArray)):
         if (pregArray[i] == False):
            FE.lists.splice(pregArray, i, 5)
#            pregArray.splice(i,5)
            i = -5
         i += 5
   elif (vagTotal + totalChange > 0) and (vagTotal < 1):
      OutputMainText("\n" + "\n" + "Your tummy feels weird as your thighs rub against each other. Your " + ClothesBottom() + " feels wet in the crotch, an oddly new sensation. Reaching in, your hand slips across sensitive and supple flesh. It splits beneath your touch, letting your finger slip in between the moist folds. You let out a moan as your palm slips across the sensitive bump at the front of the crevice, your finger sinking into a hole. The tip brushes against an even more sensitive ring that sinks further into your body - a fresh womb.",False)
      if (totalChange > 1):
         OutputMainText(" Yet, that's simply the first. More moistness slimes your hand as " + totalChange + " more gashes fill your " + VulvaDesc() + " groin, all as sensitive and large as the first. A bevy of pussies for your fingers to slip into, your hand rolling over all the labia and making you gasp with all the separate erotic thrills.",False)
      vagSize = 1
      vulvaSize = 1
      clitSize = 1
      Stats(0,0,2 * totalChange,0)
      VagBellyChange(sizeChange,totalChange)
      vagTotal += totalChange
      vagSize += sizeChange
      if (cockTotal > 0):
         OutputMainText("\n" + "\n" + "You lay your " + CockDesc() + " cock back down to cover your new slit, as you're now considered to be both genders... A herm.",False)
         gender = 3
      else:
         OutputMainText("\n" + "\n" + "You have now graduated from androgynous to female, congratulations!",False)
         gender = 2
      while (totalChange > 0):
         if ((len(pregArray) / 5) < vagTotal):
            pregArray.push(False,0,0,0,0)
            totalChange -= 1
         else:
            totalChange = 0
   elif (totalChange > 0) and (vagTotal > 0):
      OutputMainText("\n" + "\n" + "Your " + ClothesBottom() + " feels wet in the crotch, an oddly new sensation. Reaching in, your hand slips across another slit of sensitive and supple flesh. It splits beneath your touch, letting your finger slip in between the moist folds. You let out a moan as your palm slips across another bump at the front of the crevice, your finger sinking into a hole. A brand new vagina to go with the rest.",False)
      if (totalChange > 1)
         OutputMainText(" Yet, that's simply the first. More moistness slimes your hand as " + totalChange + " more gashes fill your " + VulvaDesc() + " groin, all as sensitive and large as the first. A bevy of pussies for your fingers to slip into, your hand rolling over all the labia and making you gasp with all the separate erotic thrills.",False)
      VagBellyChange(sizeChange,totalChange)
      Stats(0,0,2 * totalChange,0)
      vagTotal += totalChange
      vagSize += sizeChange
      while (totalChange > 0):
         if ((len(pregArray) / 5) < vagTotal):
            pregArray.push(False,0,0,0,0)
            totalChange -= 1
         else:
            totalChange = 0
   elif (totalChange < 0) and ((vagTotal + totalChange) > 0):
      OutputMainText("\n" + "\n" + "You notice an odd sensation of numbness within your groin. Slipping a hand into your " + ClothesBottom() + ", you notice you're missing " + -totalChange + " of your vaginas.",False)
      VagBellyChange(sizeChange,totalChange)
      Stats(0,0,2 * totalChange,0)
      vagTotal += totalChange
      vagSize += sizeChange
      while (totalChange < 0):
         if (pregCheck(1) == True)
            i = 0
            while (i < len(pregArray)):
               if (pregArray[i] == False):
                  totalChange += 1
                  FE.lists.splice(pregArray, i, 5)
#                  pregArray.splice(i,5)
                  i += len(pregArray)
               i += 5
         else:
            totalChange = 0
   elif (vagTotal > 0):
      VagBellyChange(sizeChange,totalChange)
      vagSize += sizeChange

def VagBellyChange(sizeChange:int, totalChange:int):
   global vagSize, vagTotal, vagSizeMod, tallness, vagBellyMod
   newBelly = (vagSize + sizeChange) * (vagTotal + totalChange) * vagSizeMod - tallness / 2
   if (newBelly < 0):
      newBelly = 0
   if (newBelly < vagBellyMod):
      OutputMainText("\n" + "\n" + "Your belly flattens slightly as the amount of vaginal flesh within becomes less disproportionate to your body.",False)
   elif (newBelly > vagBellyMod):
      OutputMainText("\n" + "\n" + "Your belly bulges slightly more as the vaginal flesh within takes up more room than your belly can handle...",False)
   vagBellyMod = newBelly
   if (vagBellyMod < 0):
      vagBellyMod = 0

def LegChange(which:int):
   global legType, udders, udderLactation, udderEngourgement, udderEngourgementLevel, udderPlay, udderSize, teatSize, tail, runMod, carryMod, hair, skinType
   if (legType > 1000) and (which < 1000):
      OutputMainText("\n" + "\n" + "A strange sensation envelopes your tauric half. Things pop and grow tight as the backside shrinks, your back legs dwindling down into your rear crotch while your secondary chest shrivels and your spine shortens up. The entirety of your tauric half shrinks back to your primary body, leaving you to fall back onto your " + ButtDesc() + " ass while your crotch shifts forward to nestle between your front legs.",False)
      if (legType == 1001):
         OutputMainText(" Your keratin hooves soften and elongate into bipedal feet, the black and white fur disappearing to match your " + SkinDesc() + ".",False)
         if (UdderCheck(2) != True) and (udders == True):
            OutputMainText(" Your udder also shrinks away into nothing...",False)
            udders = False
            udderLactation = 0
            udderEngorgement = 0
            udderEngorgementLevel = 0
            udderPlay = 0
            udderSize = 0
            teatSize = 0
         else:
            OutputMainText(" Your udder is still there, though, hanging just below your belly, having slipped up through your legs just before your crotch came through.",False)
      if (legType == 1002):
         if (tail == 1002):
            OutputMainText(" Your " + TailDesc() + " tail, also disappears with your extra half, no longer swishing above your backside.",False)
            tail = 0
         runMod += 10
         carryMod -= 15
      OutputMainText("\n" + "\n" + "It takes several minutes before you can manage to stand without the extra legs to square you off... It feels so strange, like a great weight has been lifted yet at the same time things feel heavier. It's going to take a bit of walking to get used to...",False)
      carryMod -= 100
   if (legType != 0) and (which == 0):
      if (legType == 1):
         OutputMainText("\n" + "\n" + "Your paws feel strange as they begin to narrow and shrink. You almost lose your balance and fall over, but your ankles touch against the floor, having grown away from your knees and forming heels. The space between your paws and ankles thicken, providing a wider base to stand upon. Feet. Not quite as agile, but a bit sturdier.",False)
   if (legType != 1) and (which == 1):
      if (legType == 0):
         OutputMainText("\n" + "\n" + "Your feet ache as your ankles lengthen and your lower-leg shortens. Your knees bend out to keep you balanced and you rise up onto your toes to stand digitigrade. Your toes also change to help, growing larger and rounder, with soft pads beneath, until the ends of your feet become a paws. Eventually, you quickly learn to balance and walk with these paws on your digitigrade legs, feeling much lighter on your 'feet', though it's more difficult to carry as much weight on such agile things.",False)
      if (legType >= 1000):
         OutputMainText("\n" + "\n" + "But then, your feet ache as your ankles lengthen and your lower-leg shortens. Your knees bend out to keep you balanced and you rise up onto your toes to stand digitigrade. Your toes also change to help, growing larger and rounder, with soft pads beneath, until the ends of your feet become a paws. Eventually, you quickly learn to balance and walk with these paws on your digitigrade legs, feeling much lighter on your 'feet', though it's more difficult to carry as much weight on such agile things.",False)
      carryMod -= 10
      runMod += 10
   if (legType == 1) and (which != 1):
      carryMod += 10
      runMod -= 10
   if (legType < 1000) and (which > 1000):
      if (legType == 0) or (legType == 1):
         OutputMainText("\n" + "\n" + "Your " + HipDesc() + " hips begin to ache as you feel something grow from them within your " + ClothesBottom() + ". Not outward, however, but towards your backside. As your hands grasp them, you can feel your thickening pelvis split in two. Your " + ButtDesc() + " rear moves away from your body as the second pelvis grows along your tailbone, your spine forming more vertebrae to extend further. You collapse to your knees while your ass tears through your " + ClothesBottom() + ", taking your crotch away from your original legs with it. Bumps form from the new pelvis as two new limbs begin to grow from the sides of your crotch, a second set of legs that touch down upon the ground, making you stumble as they grow longer and turn your rump and crotch upwards to face straight out, as though you were bending over. Your insides feel even stranger as many of your internal organs shift around, doubling or expanding down in between your two sets of legs. More ribs sprout from the lengthening spine, forming a second chest cavity that guards the organs." + "\n" + "\n" + "It takes a few minutes before your body finishes growing its second set of legs and nearly a complete second body. A tauric body. You falter a bit as you try to stand on all 4 of your legs, your arms helping pick you up from the ground but waving for balance as your original torso teeters on top. It's a very strange sensation as your mind adjusts to account for a second set of legs, working them in unison until you can walk while your second belly swings between them. Though you do feel like you can hold up much more with this strong, broader frame, so that's a plus. On the other hand, your ass and genital region are much further away now, while your original crotch feels more like a neck to the second body, so that's going to take some getting used to...",False)
      if (legType == 1):
         carryMod += 10
         runMod -= 10
      ChangeBot(-1)
      carryMod += 100
   if (legType != 1001) and (which == 1001):
      OutputMainText("\n" + "\n" + "Your tauric half feels strange and tingly.",False)
      if (skinType != 2):
         OutputMainText(" Short fur sprouts up from your " + SkinDesc() + ", only on your tauric half, white in color with large black spots",False)
      else:
         OutputMainText(" The fur on your tauric half turns white in color, with large black spots around it",False)
      OutputMainText(", while your " + ButtDesc() + " ass grows larger and more square from the second hips. The ends of your legs harden, your ankles rising as the balls of your feet terminate in keratin hooves.",False)
      if (udders == False):
         OutputMainText(" And you feel a weight growing from your tauric belly. You look around yourself to see 4 long teats extend, an udder growing beneath you, making your lower half look much like a dairy cow...",False)
         udders = True
         udderSize = 2 * breastSize
         teatSize = 2 * nippleSize
      else:
         OutputMainText(" Your udder also went along with the rest of your crotch, now hanging down from your tauric belly and threatening to drag across the ground if it gets too big, instead of sitting at your normal waist.",False)
   if (legType == 1001) and (which != 1001) and (which > 1000):
      if (UdderCheck(2) != True) and (udders == True):
         OutputMainText("\n" + "\n" + "Your udder shrinks into your " + SkinDesc() + " and disappears...",False)
         udders = False
         udderLactation = 0
         udderEngorgement = 0
         udderEngorgementLevel = 0
         udderPlay = 0
         udderSize = 0
         teatSize = 0
   if (legType != 1002) and (which == 1002):
      OutputMainText("\n" + "\n" + "All four feet relax themselves against the ground, level from toes to heels, standing plantigrade and sturdy. Not exactly fast and a bit awkward, but they can hold much more weight, especially considering your second half is as thin as the first and would have otherwise not been the best frame for carrying things across your extended back.",False)
      if (tail > 0) and (tail != 1002) and (hair != 0):
         OutputMainText(" And your " + TailDesc() + " shifts into hairs that matches the hair on your head.",False)
      elif (tail) == 0 and (hair != 0):
         OutputMainText(" And to finish off the transformation, just above your butt sprouts a tail of hairs from your tailbone that matches the hair on your head and swishes with your control.",False)
      else:
         OutputMainText(" You also feel some extra muscle control above your butt, around your tailbone, where it feels like you've got a tail, but there's nothing there to speak of yet.",False)
      tail = 1002
      runMod -= 10
      carryMod += 15
   if (legType == 1002) and (which != 1002) and (which > 1000):
      runMod += 10
      carryMod -= 15
   legType = which

def BoobChange(sizeChange:int):
   global breastSize, nippleSize
   breastSize += sizeChange
   nippleSize += sizeChange

def UdderChange(sizeChange:int):
   global udderSize, teatSize
   udderSize += sizeChange
   teatSize += sizeChange

def UdderCheck(which:int):
   global cowAffinity, legType
   tempBool = False
   if (which != 1) and (cowAffinity >= 55):
      tempBool = True
   if (which != 2) and (legType == 1001):
      tempBool = True
   return tempBool

def LactChange(which:int, amount:int):
   global lactation, nipplePlay, udderLactation, udderPlay, milkEngourgementLevel, milkEngourgement, udders, udderEngourgementLevel, udderEngourgement, milkSuppressant, pregStatus
   if (which == 1) and ((lactation + amount) >= 1) and lactation < 1:
      OutputMainText("\n" + "\n" + "Blotches spread across your " + ClothesTop() + " around your nipples. Curiously, you dab your finger in the moistness and take a taste. Milk... Your breasts seem to have begun lactating!",False)
      nipplePlay = 20
   if (which == 2) and ((udderLactation + amount) >= 1) and (udderLactation < 1) and (udders == True):
      OutputMainText("\n" + "\n" + "Blotches spread across your " + ClothesBottom() + ", starting from your teats. Curiously, you dab your finger in the moistness and take a taste. Milk... Your udder seems to have begun lactating!",False)
      udderPlay = 20
   if (which == 1) and ((lactation + amount) < 1) and (lactation >= 1):
      OutputMainText("\n" + "\n" + "Your nipples feel exceptionally dry... It seems your breasts are no longer producing milk.",False)
      nipplePlay = 0
      if (milkEngorgementLevel == 1):
         BoobChange(-1)
      if (milkEngorgementLevel == 2):
         BoobChange(-2)
      if (milkEngorgementLevel == 3):
         BoobChange(-3)
      milkEngorgementLevel = 0
      milkEngorgement = 0
   if (which == 2) and ((udderLactation + amount) < 1) and (udderLactation >= 1) and (udders == True):
      OutputMainText("\n" + "\n" + "Your teats feel exceptionally dry... It seems your udder is no longer producing milk.",False)
      if (udderEngorgementLevel == 1):
         UdderChange(-2)
      if (udderEngorgementLevel == 2):
         UdderChange(-5)
      if (udderEngorgementLevel == 3):
         UdderChange(-8)
      udderEngorgementLevel = 0
      udderEngorgement = 0
      udderPlay = 0
   if (which == 1):
      lactation += amount
   if (which == 2):
      udderLactation += amount
   if (milkSuppressant <= 0):
      if (lactation <= 0) or ((udderLactation <= 0) and (udders == True) and (pregStatus > 0)):
         OutputMainText(" ...However a few minutes later your milk starts right back up. Seems your body needs the milk for something else.",False)
         lactation = 20
         if udders == True:
            udderLactation = 20
      if (lactation < 3000) or ((udderLactation < 3000) and (udders == True) and (checkItem(252) == True)):
         OutputMainText(" ...However a few minutes later you begin to squirt again, soaking your outfit. The milky pendant feels warmer than usual, suffusing its essence back into your body and preventing you from being less drippy...",False)
         lactation = 3000
         if (udders == True):
            udderLactation = 3000
   if (lactation < 0):
      lactation = 0
   if (udderLactation < 0):
      udderLactation = 0

def PregCheck(amount:int):
   global pregArray
   tempBool = False
   if (amount == 0):
      i = 0
      while (i < len(pregArray)):
         if (pregArray[i] == True):
            tempBool = True
         i += 5
   elif (amount == 1):
      i = 0
      while (i < len(pregArray)):
         if (pregArray[i] == False):
            tempBool = True
         i += 5
   elif (amount > 1):
      i = 0
      while (i < len(pregArray)):
         if (pregArray[i + 1] == amount):
            tempBool = True
         i += 5
   return tempBool


!def DoImpregnate(erace:int):
     global babyFree, cockSnakePreg, pregChanceMod, extraPregChance, pregArray
     tempPregMod = 0
     extra = 0
     chance = Percent()
     if (babyFree > 0):
         tempPregMod -= 50
     if (cockSnakePreg > 0):
         OutputMainText("\n" + "\n" + "As the cum fills your " + BellyDesc() + " belly, you feel it diminish from your passage as the cum-hungry snake inside squirms to drink it down. It then settles, happy with its meal and giving you some rest...",False,"snakes")
         cockSnakePreg += 25
         if (cockSnakePreg > 100):
            cockSnakePreg = 100
         tempPregMod -= 100000
     trace(chance + " " + pregChanceMod + " " + tempPregMod)
     if (pregCheck(1) == True) and ((chance + pregChanceMod + tempPregMod) >= 90):
         i = 0
         extra = 0
         while (Percent() < (extraPregChance + 10 - 4 * (i + 1) * i)):
            extra++
            i += 1
         i = 0
         while (i < len(pregArray)):
            if pregArray[i] == False:
               if erace == 100:
                  pregArray[i + 2] = 80 + math.floor(Percent() / 10) + extra * 30
                  pregArray[i + 4] = extra * 2
               if erace == 101:
                  pregArray[i + 2] = 220 + math.floor(Percent() / 5) + extra * 110
                  pregArray[i + 4] = extra
               if erace == 307:
                  pregArray[i + 2] = 280 + math.floor(Percent() / 5) + extra * 140
                  pregArray[i + 4] = extra
               if erace == 308:
                  pregArray[i + 2] = 80 + math.floor(Percent() / 5) + extra * 30
                  pregArray[i + 4] = extra * 2
               if erace == 1:
                  pregArray[i + 2] = 140 + math.floor(Percent() / 5) + extra * 70
                  pregArray[i + 4] = extra
               if erace == 2:
                  pregArray[i + 2] = 210 + math.floor(Percent() / 5) + extra * 100
                  pregArray[i + 4] = extra
               if erace == 3
                  pregArray[i + 2] = 110 + math.floor(Percent() / 5) + extra * 40
                  pregArray[i + 4] = extra * 2
               if erace == 4:
                  pregArray[i + 2] = 90 + math.floor(Percent() / 5) + extra * 35
                  pregArray[i + 4] = extra * 2
               if erace == 5:
                  pregArray[i + 2] = 240 + math.floor(Percent() / 5) + extra * 120
                  pregArray[i + 4] = extra
               if erace == 6:
                  pregArray[i + 2] = 80 + math.floor(Percent() / 10) + extra * 60
                  pregArray[i + 4] = extra * 3
               if erace == 7:
                  pregArray[i + 2] = 50 + math.floor(Percent() / 10) + extra * 40
                  pregArray[i + 4] = extra * 3
               if erace == 8:
                  pregArray[i + 2] = 40 + math.floor(Percent() / 10) + extra * 60
                  pregArray[i + 4] = extra * 5
               if erace == 9:
                  pregArray[i + 2] = 90 + math.floor(Percent() / 10) + extra * 40
                  pregArray[i + 4] = extra
               if erace == 10:
                  pregArray[i + 2] = 180 + math.floor(Percent() / 10) + extra * 70
                  pregArray[i + 4] = extra * 2
               if erace == 11:
                  pregArray[i + 2] = 120 + math.floor(Percent() / 10) + extra * 50
                  pregArray[i + 4] = extra * 2
               if erace == 12:
                  pregArray[i + 2] = 50 + math.floor(Percent() / 10) + extra * 40
                  pregArray[i + 4] = extra * 4
               pregArray[i + 1] = erace
                    pregArray[i] = True
                    i = lwn(pregArray)
               i += 5

def DoBirth(pregnancyType:int, extra:int, birthCount:int):
   global pregArray, vagTotal, hrs, vulvaSize, wolfPupChildren, calfChildren, minotaurChildren, freaktGirlChildren, humanChildren, equanChildren, lupanChildren, felinChildren, cowChildren, bunnionChildren, miceChildren, birdEggs, pigChildren, skunkChildren, bugEggs, sen, dominant
   birthNumber = 0
   if (len(pregArray) > (vagTotal * 5)):
      VagChange(0,1)
   hrs += 1
   if (birthCount == 0):
      OutputMainText("\n" + "\n" + "Suddenly, you feel water splash across your thighs, flooding from " + OneYour(2) + " cunt" + Plural(2) + ". You've gone into labor!" + "\n" + "\n" + "You sit on the ground, huffing and heaving as pain envelops your body. Between each heave and your hands on your belly, you push with all your might!",False)
   if (birthCount > 0):
      OutputMainText("\n" + "\n" + "Yet, you're still not quite done with the birthing process as fluid splashes out of another one of your vaginas. You tense yourself, already on the ground, and your breathing progresses rapidly as your nearly crush your belly, trying to get more of your babies out!",False)
   if (pregnancyType == 100):
      birthNumber = math.floor(Percent() / 20 + 3 + extra)
      OutputMainText(" Rather quickly, a small body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a small, high-pitched whine come from it. Pausing from your labor, you pull the child up to your chest, cradling it. Covered in fur, eyes shut to the world, it's a small puppy. A wolf puppy, to be more accurate. Although, you have little time to consider the symantics as another contraction makes you seize in pain. Soon, another whine cries out. Followed by another contraction... Until you have given birth to a litter of " + birthNumber + " wolf pups! Congratulations, Mommy!" + "\n" + "\n" + "You'll bring the pups to your personal day-care the next time you're in town.",False)
      if (VagLimit() < 12):
         vulvaSize += 1
         VagChange(1,0)
      wolfPupChildren += birthNumber
   if (pregnancyType == 101):
      birthNumber = 1 + extra
      OutputMainText(" Slowly, a large body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". Hooves scrape across the ground as the forelegs come out first. Shortly after, you heave for fresh air as the rest of the body slides out. As the newborn lets out a surprised moo, trying to figure out what happened, you reach down and bring it up to your " + BoobDesc() + " chest. A cow from head to hoof, the calf is already licking over the fabric in an attempt to latch onto your teat. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting it suckle from its mother.",False);
      if (VagLimit() < 36):
         vulvaSize += 1
         VagChange(1,0)
      if (VagLimit() < 20):
         OutputMainText("\n" + "\n" + "You're also quite a bit looser than before, from giving birth to such a big body...",False)
         VulvaSize += 2
         VagChange(2,0)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "However, a contraction in the middle of suckling returns your attention to your spread loins. Apparently, the single newborn wasn't the only one in there. You grunt and heave some more as you push out " + (birthNumber - 1) + " more calves, each as large as the first! By the time you're finished, you're quite exhausted, holding them all to your bosom and letting them suckle as they can.",False)
      if (birthNumber == 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the calf to bring to your own personal day-care the next time you're in town.",False)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the calves to your bring to own personal day-care the next time you're in town.",False)
      calfChildren += birthNumber
   if (pregnancyType == 307):
      birthNumber = 1 + extra
      OutputMainText(" Slowly, a large body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a snort as the long muzzle breaches " + OneYour(2) + " " + VulvaDesc() + " pair" + Plural(2) + " of lips. Shortly after, you heave for fresh air as the rest of the body slides out. As the newborn cries out, you reach down and bring it up to your " + BoobDesc() + " chest. With a bull-like muzzle, small horns, and rather huge human-like body, it looks like you've given birth to the Minotaur's child. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting it suckle from its mother.",False)
      if (VagLimit() < 25):
         vulvaSize += 1
         VagChange(1,0)
      if (VagLimit() < 15):
         OutputMainText("\n" + "\n" + "You're also quite a bit looser than before, from giving birth to such a big body...",False)
         vulvaSize += 3
         VagChange(3,0)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "However, a contraction in the middle of suckling returns your attention to your spread loins. Apparently, the single newborn wasn't the only one in there. You grunt and heave some more as you push out " + (birthNumber - 1) + " more minotaur babies, each as large as the first! By the time you're finished, you're quite exhausted, holding them all to your bosom and letting them suckle as they can.",False)
      if (birthNumber == 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the Minotaur's child to bring to your own personal day-care the next time you're in town.",False)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the Minotaur's children to your bring to own personal day-care the next time you're in town.",False)
      minotaurChildren += birthNumber
   if (pregnancyType == 308):
      birthNumber = math.floor(Percent() / 20 + 2 + extra)
      OutputMainText(" Quite soon, you feel a small fuzzy body push out " + LegWhere(1) + " your " + LegDesc(2) + ". A soft mewl escapes its lips, taking its first gasp of air. Pulling the babe up to your chest and cradling it, it's... just a ball of fuzz with the face of a human in the center and two large long ears poking out on either side. You're not exactly sure what it is, only the ears look familiar, like that girl from the cave... Plus it's rather small, obviously just the first, as several more could easily fit within your belly... As another contraction yanks back your attention, another mewl cries out, with another soon on its way..." + "\n" + "\n" + "Eventually, you have given birth to a pile of " + birthNumber + " strange round fuzzy babies. They roll around your body as you let them suckle from your nipples and you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      freakyGirlChildren += birthNumber
   if (pregnancyType == 1):
      birthNumber = 1 + extra
      OutputMainText(" Slowly, a large round head pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a cry as it breaches " + OneYour(2) + " " + VulvaDesc() + " pair" + Plural(2) + " of lips. Shortly after, you heave for fresh air as the rest of the body slides out. As the newborn cries out, your reach down and bring it up to your " + BoobDesc() + " chest. With a round face and soft skin, it's easy to tell you've given birth to a human child. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting it suckle from its mother.",False)
      if (VagLimit() < 16):
         vulvaSize += 1
         VagChange(1,0)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "However, a contraction in the middle of suckling returns your attention to your spread loins. Apparently, the single newborn wasn't the only one in there. You grunt and heave some more as you push out " + (birthNumber - 1) + " more human babies, each about the same size as the first. By the time you're finished, you're quite exhausted, holding them all to your bosom and letting them suckle as they can.",False)
      if (birthNumber == 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the human child to bring to your own personal day-care the next time you're in town.",False)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the human children to bring to your own personal day-care the next time you're in town.",False)
      humanChildren += birthNumber
   if (pregnancyType == 2):
      birthNumber = 1 + extra
      OutputMainText(" Slowly, a large body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a snort as the long muzzle breaches " + OneYour(2) + " " + VulvaDesc() + " pair" + Plural(2) + " of lips. Shortly after, you heave for fresh air as the rest of the body slides out. As the newborn cries out, you reach down and bring it up to your " + BoobDesc() + " chest. With a horse-like muzzle and rather large body, it's easy to tell you've given birth to an equan child. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting it suckle from its mother.",False)
      if (VagLimit() < 36):
         vulvaSize += 1
         VagChange(1,0)
      if (VagLimit() < 20):
         OutputMainText("\n" + "\n" + "You're also quite a bit looser than before, from giving birth to such a big body...",False)
         vulvaSize += 2
         VagChange(2,0)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "However, a contraction in the middle of suckling returns your attention to your spread loins. Apparently, the single newborn wasn't the only one in there. You grunt and heave some more as you push out " + (birthNumber - 1) + " more equan babies, each as large as the first! By the time you're finished, you're quite exhausted, holding them all to your bosom and letting them suckle as they can.",False)
      if (birthNumber == 1):
         this.outputMainText("\n" + "\n" + "Eventually, you prepare the equan child to bring to your own personal day-care the next time you're in town.",False)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the equan children to your bring to own personal day-care the next time you're in town.",False)
      equanChildren += birthNumber
   if (pregnancyType == 3):
      birthNumber = math.floor(Percent() / 20 + 2 + extra)
      OutputMainText(" Quite soon, you feel a small fuzzy body push out " + LegWhere(1) + " your " + LegDesc(2) + ". A soft yip escapes its lips, taking its first gasp of air. Pulling the babe up to your chest and cradling it, the small humanoid body is covered in fur with wolf-like ears and tail. Especially small, the lupan child is just the first, as several more could easily fit within your belly... As another contraction yanks back your attention, another whimper cries out, with another soon on its way..." + "\n" + "\n" + "Eventually, you have given birth to a litter of " + birthNumber + " pup-like lupan babies. They crawl around your body as you let them suckle from your nipples and you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      lupanChildren += birthNumber
   if (pregnancyType == 4):
      birthNumber = math.floor(Percent() / 20 + 2 + extra)
      OutputMainText(" Quite soon, you feel a small fuzzy body push out " + LegWhere(1) + " your " + LegDesc(2) + ". A soft mewl escapes its lips, taking its first gasp of air. Pulling the babe up to your chest and cradling it, the small humanoid body is covered in fur with cat-like ears and tail. Especially small, the felin child is just the first, as several more could easily fit within your belly... As another contraction yanks back your attention, another mewl cries out, with another soon on its way..." + "\n" + "\n" + "Eventually, you have given birth to a litter of " + birthNumber + " kitten-like felin babies. They crawl around your body as you let them suckle from your nipples and you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      felinChildren += birthNumber
   if (pregnancyType == 5):
      birthNumber = 1 + extra
      OutputMainText(" Slowly, a large body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a quiet groan as the muzzle breaches " + OneYour(2) + " " + VulvaDesc() + " pair" + Plural(2) + " of lips. Shortly after, you heave for fresh air as the rest of the body slides out. As the newborn cries out, your reach down and bring it up to your " + BoobDesc() + " chest. With a cow-like muzzle and rather large body, it seems as though you have given birth to a cow-like child. The relatively large nipples for a newborn and small udder, its obviously a she before even checking her genitals, and a long thin tail that ends with a bushy-haired tip. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting her suckle from her mother.",False)
      if (VagLimit() < 36):
         vulvaSize
         VagChange(1,0)
      if (VagLimit() < 20):
         OutputMainText("\n" + "\n" + "You're also quite a bit looser than before, from giving birth to such a big body...",False)
         vulvaSize += 2
         VagChange(2,0)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "However, a contraction in the middle of suckling returns your attention to your spread loins. Apparently, the single newborn wasn't the only one in there. You grunt and heave some more as you push out " + (birthNumber - 1) + " more bovine baby girls, each as large as the first! By the time you're finished, you're quite exhausted, holding them all to your bosom",False)
         if (udders == True):
            OutputMainText(" and udder",False)
         OutputMainText(", letting them suckle as they can, which they do to great length.",False)
      if (birthNumber == 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the bovine child to bring to your own personal day-care the next time you're in town.",False)
      if (birthNumber > 1):
         OutputMainText("\n" + "\n" + "Eventually, you prepare the bovine children to your bring to own personal day-care the next time you're in town.",False)
      cowChildren += birthNumber
   if (pregnancyType == 6):
      birthNumber = math.floor(Percent() / 15 + 3 + extra)
      OutputMainText(" You soon feel your passage begin to stretch as a hard, smooth body begins to slip out past your lips. It doesn't take much effort before it plops to the floor and rolls a little, a white egg a bit larger than your average unfertilized Lizan egg. Another contraction gets you pushing again as the rest of its brood push out, one egg right after the next." + "\n" + "\n" + "Eventually, you have laid a batch of " + birthNumber + " fertilized eggs, all with Lizan embryos slowly growing inside them. You have no idea how long they'll take to hatch, but you'll bring them back to your personal day-care anyways to make sure they're taken care of until they do.",False)
      lizanEggs += birthNumber
   if (pregnancyType == 7):
      birthNumber = math.floor(Percent() / 20 + 3 + extra)
      OutputMainText(" Quite rapidly, you feel a small fuzzy body push out " + LegWhere(1) + " your " + LegDesc(2) + ". Cute squeaks erupt from it as it takes its first breaths, writhing around softly. You pull it up to your chest, cradling the small humanoid body that is covered in downy fur with long ears and a puffy tail. So small, the bunny-like child is just the first, as more are most definitely on the way. They don't call it 'breeding like rabbits' for nothing..." + "\n" + "\n" + "More squeaks are soon heard as the bunny-like babes pour from your womb, until you have a litter of " + birthNumber + ". They kick about your body, trying to crawl and suckle from you, until you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      bunnionChildren += birthNumber
   if (pregnancyType == 8):
      birthNumber = math.floor(Percent() / 20 + 4 + extra)
      OutputMainText(" Quite rapidly, you feel a small naked body push out " + LegWhere(1) + " your " + LegDesc(2) + ". Cute squeaks erupt from it as it takes its first breaths, pawing at the ground confusedly. You pull it up to your chest, cradling the small humanoid body that is quite naked, not having grown any fur yet, with large circular ears and long thin tail. So small, the mouse-like child is just the first, as more are most definitely on the way. Mice are very... 'excessive' breeders..." + "\n" + "\n" + "More squeaks are soon heard as the mouse-like babes pour from your womb, until you have a litter of " + birthNumber + ". They blindly grope about your body, trying to figure out what the hell is going on, drinking from your nipples when they can, until you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      miceChildren += birthNumber
   if (pregnancyType == 9):
      birthNumber = math.floor(Percent() / 15 + 3 + extra)
      OutputMainText(" You soon feel your passage begin to stretch as a hard, smooth body begins to slip out past your lips. It takes a bit of effort before it plops to the floor and rolls a little, a speckled egg much larger than your average unfertilized egg. Another contraction gets you pushing again as the rest of the clutch push out, one egg right after the next." + "\n" + "\n" + "Eventually, you have laid a batch of " + birthNumber + " fertilized eggs, all with embryos slowly growing inside them. You have no idea how long they'll take to hatch, but you'll bring them back to your personal day-care anyways to make sure they're taken care of until they do.",False)
      birdEggs += birthNumber
   if (pregnancyType == 10):
      birthNumber = math.floor(Percent() / 33 + 1 + extra)
      OutputMainText(" Slowly, a round body pushes out from " + LegWhere(1) + " your " + LegDesc(2) + ". You hear a squeal cutely as it breaches " + OneYour(2) + " " + VulvaDesc() + " pair" + Plural(2) + " of lips. Shortly after, you heave for fresh air before the next body begins to make its way out. A litter of " + birthNumber + " smooth-skinned babes cry and squeal, trying to crawl around and looking for their mother's bosom. With snubbed noses and long floppy ears with little curly tails, these humanoid babies look a bit like pigs. With a sigh, you pull " + PullUD(1) + " your " + ClothesTop() + ", letting them suckle before you bring them to the day-care where they'll be carefully watched after.",False)
      pigChildren += birthNumber
   if (pregnancyType == 11):
      birthNumber = math.floor(Percent() / 20 + 2 + extra)
      OutputMainText(" Quite soon, you feel a small fuzzy body push out " + LegWhere(1) + " your " + LegDesc(2) + ". A soft mewl escapes its lips, taking its first gasp of air. Pulling the babe up to your chest and cradling it, the small humanoid body is covered in fur with skunk-like ears and a big fluffy tail. Especially small, the skunk-like child is just the first, as several more could easily fit within your belly... As another contraction yanks back your attention, another mewl cries out, with another soon on its way..." + "\n" + "\n" + "Eventually, you have given birth to a litter of " + birthNumber + " skunk-like babies. They crawl around your body as you let them suckle from your nipples and you eventually prepare them to bring to your personal day-care the next time you're in town.",False)
      skunkChildren += birthNumber
   if (pregnancyType == 12):
      birthNumber = math.floor(Percent() / 10 + 4 + extra)
      OutputMainText(" You soon feel your passage begin to stretch as a soft, smooth body begins to slip out past your lips. It slides out rather quickly, hitting the floor with a wet plop and rolls away, a soft-shelled translucent gooey egg much larger than your average bug egg, a body visibly growing within. Another contraction gets you pushing again as the rest of the clutch push out, one egg right after the next until you have a small pile." + "\n" + "\n" + "Eventually, you have laid a batch of " + birthNumber + " fertilized eggs, all with embryos slowly growing inside them. You have no idea how long they'll take to hatch, but you'll bring them back to your personal day-care anyways to make sure they're taken care of until they do.",False)
      bugEggs += birthNumber
   if (pregnancyType == 200):
      OutputMainText(" It doesn't take much effort as you feel a round object roll out of " + OneYour(2) + " " + VulvaDesc() + " cunt" + Plural(2) + " with a wet plop. You attempt to look around your body to see what it is, but you don't have much time before another squeezes through your cervix, demanding your attention to get back to pushing." + "\n" + "\n" + "There's not much of a rest in between contractions to see what is coming out exactly, but all you can tell is that there are a lot. At least a dozen; although it's impossible to keep track amidst all the birthing. It's not until the very last one exits that you're given a long enough reprieve to actually look..." + "\n" + "\n" + "You seem to be just in time to spot the clear, jelly-like egg unravel around something pink in the center. The pink thing tumbles out from the egg, spreading apart into several small tentacles. Eight, to be exact. And in the center of them is a cute little girl. Not quite a baby, just a really small child, no taller than half a foot. You can hear her giggle a little as she kisses your thighs, thanking you a little before wiggling her way away from you." + "\n" + "\n" + "Your " + LegDesc(2) + " are too weak at the moment to chase after her, but you can see a trail of slime that all of the others had used. They seem to be headed in the same direction: back to the beach where you had obtained them.",False)
      ItemAdd(217)
   if (pregnancyType == 201):
      OutputMainText(" However, it takes less effort than you thought possible as small hands manually spread you wider and then anchor themselves further and further out. Two tall, narrow ears pop out " + LegWhere(1) + " your " + LegDesc(2) + ", your slime forming a web between them. In another moment, an entire body rolls out of you, wet and almost covered in white fur, around two feet tall." + "\n" + "\n" + "Her well-developed chest wobbles about as she turns to look at you with am absolutely naughty grin. Then she dashes off, hopping away with her large feet and one hand still jerking furiously between her legs..." + "\n" + "\n" + "Seems like you had obtained a horny stowaway during your time as a giant, though you're unsure if it was an accident on your part or intentional on hers... Shortly after, however, you realize she had left something behind, fishing it out after having been caught between your " + VulvaDesc() + " pussy-lips. ",False)
      ItemAdd(222)
   if (pregnancyType == 202):
      OutputMainText(" However, it takes less effort than you thought possible as small hands manually spread you wider and then anchor themselves further and further out. Two tall, narrow ears pop out " + LegWhere(1) + " your " + LegDesc(2) + ", your slime forming a web between them. In another moment, an entire body rolls out of you, wet and almost covered in white fur, around two feet tall." + "\n" + "\n" + "His hand still on his pointy prick, a strand of cum drooling from its tip back to your pussy, he turns to look at you with am absolutely naughty grin. Then he dashes off, hopping away with his large feet and one hand still jerking furiously between his legs..." + "\n" + "\n" + "Seems like you had obtained a horny stowaway during your time as a giant, though you're unsure if it was an accident on your part or intentional on his... Shortly after, however, you realize he had left something behind, fishing it out after having been caught between your " + VulvaDesc() + " pussy-lips. ",False)
      DoImpregnate(7)
      ItemAdd(222)
   if (pregnancyType == 501):
      OutputMainText(" Thick bull-cum splorts out from between your legs, coating your " + LegDesc(4) + " with the white sticky spunk. More continues to lewdly pour from your vagina, your belly deflating as the stuff forms a puddle beneath you. You shudder as the warm stuff flows out, feeling like you just ejaculated through your cunt..." + "\n" + "\n" + "It is like a great weight has been lifted from you, your womb twitching from holding all that stuff inside for several hours. Rather embarassing, you leave the puddle behind, quickly escaping while some leftover stuff dribbles out as you go...",False)
      DoImpregnate(101)
      DoImpregnate(101)
      DoImpregnate(101)
      DoImpregnate(101)
      DoImpregnate(101)
      DoLust(-math.floor(sen / 4),2,2)
   if (pregnancyType == 502):
      OutputMainText(" Your own thick cum splorts out from between your legs, coating your " + LegDesc(4) + " with the white sticky spunk. More continues to lewdly pour from your vagina, your belly deflating as the stuff forms a puddle beneath you. You shudder as the warm stuff flows out, feeling like you just ejaculated through your cunt..." + "\n" + "\n" + "It is like a great weight has been lifted from you, your womb twitching from holding all that stuff inside for several hours. Rather embarassing, you leave the puddle behind, quickly escaping while some leftover stuff dribbles out as you go...",False)
      DoImpregnate(dominant)
      DoImpregnate(dominant)
      doImpregnate(dominant)
      DoLust(-math.floor(sen / 4),2,2)
   if (pregnancyType == 504):
      OutputMainText(" White fluids explode from your fresh pussy, drenching your " + LegDesc(4) + " and slightly flooding the area around you. It only takes a few moments for it to all escape, your belly quickly deflating. Dabbing your fresh new pussy and taking a taste, the white fluid was a bunch of milk..." + "\n" + "\n" + "The statue must have enjoyed it's practical joke on you.",False)

def Plural(topic:int):
   global cocktotal, vagtotal
   tempStr = ""
   if (topic == 1) and (cockTotal > 1):
      tempStr = "s"
   if (topic == 2) and (vagTotal > 1):
      tempStr = "s"
   if (topic == 3) and (cockTotal < 2):
      tempStr = "s"
   if (topic == 4) and (vagTotal < 2):
      tempStr = "s"
   if (topic == 5) and (cockTotal < 2):
      tempStr = "its"
   if (topic == 5) and (cockTotal > 1):
      tempStr = "their"
   if (topic == 6) and (vagTotal < 2):
      tempStr = "its"
   if (topic == 6) and (vagTotal > 1):
      tempStr = "their"
   if (topic == 7) and (cockTotal < 2):
      tempStr = "it's"
   if (topic == 7) and (cockTotal > 1):
      tempStr = "they're"
   if (topic == 8) and (vagTotal < 2):
      tempStr = "it's"
   if (topic == 8) and (vagTotal > 1):
      tempStr = "they're"
   if (topic == 9) and (cockTotal < 2):
      tempStr = "it"
   if (topic == 9) and (cockTotal > 1):
      tempStr = "them"
   if (topic == 10) and (vagTotal < 2):
      tempStr = "it"
   if (topic == 10) and (vagTotal > 1):
      tempStr = "them"
   if (topic == 11) and (cockTotal < 2):
      tempStr = "it"
   if (topic == 11) and (cockTotal > 1):
      tempStr = "they"
   if (topic == 12) and (vagTotal < 2):
      tempStr = "it"
   if (topic == 12) and (vagTotal > 1):
      tempStr = "they"
   if (topic == 13) and (cockTotal < 2):
      tempStr = "is"
   if (topic == 13) and (cockTotal > 1):
      tempStr = "are"
   if (topic == 14) and (vagTotal < 2):
      tempStr = "is"
   if (topic == 14) and (vagTotal > 1):
      tempStr = "are"
   if (topic == 15) and (cockTotal > 1):
      tempStr = "es"
   if (topic == 16) and (vagTotal < 2):
      tempStr = "y"
   if (topic == 16) and (vagTotal > 1):
      tempStr = "ies"
   return tempStr

def OneYour(topic:int):
   global cockTotal, vagTotal
   tempStr = "ONE YOUR ERROR " + cockTotal + " " + vagTotal
   if (topic == 1):
      if (cockTotal > 1):
         tempStr = "one of your"
      if (cockTotal == 1):
         tempStr = "your"
   if (topic == 2):
      if (vagTotal > 1):
         tempStr = "one of your"
      if (vagTotal == 1):
         tempStr = "your"
   return tempStr

def BodyDesc():
   global gender, body, hips, breastSize, butt
   tempStr = "BODY ERROR " + gender + " " + body
   if (gender == 1):
      if (body > 11) and (body <= 17):
         if (hips > 3) and (breastSize > 4):
            tempStr = "shemale"
         elif (hips > 2):
            tempStr = "femme-boyish"
         else:
            tempStr = "boyish"
      elif (body > 17) and (body <= 25):
         tempStr = "manly"
      elif (body <= 11):
         tempStr = "childish"
#      elif (body > 25):
#         tempStr = "musclebound"
   elif (gender == 2):
      if (body > 9) and (body <= 14):
         tempStr = "girly"
      if (body > 14) and (body <= 20):
         if (hips > 4) or (butt > 4) or (breastSize > 4):
            tempStr = "voluptuous"
         else:
            tempStr = "womanly"
      if (body <= 10):
         tempStr = "childish"
      if (body > 17) and (breastSize <= 2):
         tempStr = "cunt-boy"
#      elif (body > 20):
#         tempStr = "musclebound"
   elif (gender == 3):
      if (body > 11) and (body <= 23):
         if (hips > 2) and (breastSize > 2):
            tempStr = "feminine"
         else:
            tempStr = "masculine"
      elif (body <= 11):
         tempStr = "childish"
#      elif (body > 23):
#         tempStr = "musclebound"
   elif (gender == 0):
      if (body > 11) and (body <= 15):
         tempStr = "teenage"
      elif (body > 15) and (body <= 23):
         tempStr = "fully grown"
      elif (body <= 11):
         tempStr = "childish"
#      elif (body > 23):
#         tempStr = "musclebound"
   return tempStr

def TailDesc():
   global tail
   chance = Percent()
   tempStr = "TAIL ERROR " + tail
   if (chance <= 100):
      if (tail == 2):
         tempStr = "equine"
      if (tail == 3):
         tempStr = "wolfish"
      if (tail == 4):
         tempStr = "cat-like"
      if (tail == 5):
         tempStr = "bovine"
      if (tail == 6):
         tempStr = "reptillian"
      if (tail == 7):
         tempStr = "bunny"
      if (tail == 8):
         tempStr = "mousy"
      if (tail == 9):
         tempStr = "birdy"
      if (tail == 10):
         tempStr = "piggy"
      if (tail == 11):
         tempStr = "skunky"
      if (tail == 12):
         tempStr = "thick ovipositor"
      if (tail == 1002):
         tempStr = HumanTaurTailDesc()
   if (chance <= 50):
      if (tail == 2):
         tempStr = "bristly"
      if (tail == 3):
         tempStr = "fluffy"
      if (tail == 4):
         tempStr = "lithe"
      if (tail == 5):
         tempStr = "skinny, bristly-tipped"
      if (tail == 6):
         tempStr = "thick, sleek"
      if (tail == 7):
         tempStr = "poofy puff-ball"
      if (tail == 8):
         tempStr = "thin, naked"
      if (tail == 9):
         tempStr = "feathery"
      if (tail == 10):
         tempStr = "short, curly"
      if (tail == 11):
         tempStr = "big striped fluffy"
      if (tail == 12):
         tempStr = "wide bulbous"
      if (tail == 1002):
         tempStr = HumanTaurTailDesc()
   return tempStr

def HumanTaurTailDesc():
   global hair, hairLength
   tempStr = ""
   if (HairstyleLength(hair) == True):
      if (hairLength == 2):
         tempStr = "short "
      if (hairLength == 4):
         tempStr = ""
      if (hairLength == 6):
         tempStr = "long "
      if (hairLength == 8):
         tempStr = "very long "
      if (hairLength == 10):
         tempStr = "ground-dragging "
   tempStr += HairC()
   if (hair == 0):
      tempStr = "hairy"
   if (hair == 1):
      tempStr = "wavy haired"
   if (hair == 2):
      tempStr = "pigtailed"
   if (hair == 3):
      tempStr = "ponytailed"
   if (hair == 4):
      tempStr = "straight haired"
   if (hair == 5):
      tempStr = "stubbly haired"
   if (hair == 6):
      tempStr = "mohawked"
   if (hair == 7):
      tempStr = "bunned"
   if (hair == 8):
      tempStr = "curly haired"
   if (hair == 9):
      tempStr = "braided pigtailed"
   if (hair == 10):
      tempStr = "braided ponytailed "
   if (hair == 11):
      tempStr = "braided"
   if (hair == 12):
      tempStr = "spiky haired"
   if (hair == 13):
      tempStr = "stiff haired"
   if (hair == 14):
      tempStr = "poofball"
   return tempStr

def EarDesc():
   global ears
   chance = Percent()
   tempStr = "EAR ERROR " + ears
   if (chance <= 100):
      if (ears == 1):
         tempStr = "Hugging the sides of your head, you have small rounded ears that can easily be hidden by your hair, like that of a human's"
      if (ears == 2):
         tempStr = "Atop your head, you have large tear-drop shaped ears that flick every now and then, able to hear quite well, like that of a horse's"
      if (ears == 3):
         tempStr = "Atop your head, you have small triangular ears that stand perk, like that of a wolf's"
      if (ears == 4):
         tempStr = "Atop your head, you have small triangular ears that stand perk, like that of a cat's"
      if (ears == 5):
         tempStr = "Standing out perpendicular from the sides of your head, you have large oval ears that that droop slightly from their size, like that of a cow's"
      if (ears == 6):
         tempStr = "On the sides of your head, you have sleek holes for ears, like many lizards have"
      if (ears == 7):
         tempStr = "Atop your head, you have long ears that stand high and vigilant, like that of a rabbit's"
      if (ears == 8):
         tempStr = "Standing out perpendicular the sides of your head, large rounded ears practically flap when they twitch, looking like you glued discs to the sides of your head, like that of a mouse's"
      if (ears == 9):
         tempStr = "On the sides of your head, have flat patches of feathers covering your holes, like a bird's"
      if (ears == 10):
         tempStr = "Standing out perpendicular from the sides of your head, you have triangular ears that fold near the ends and droop down from their length, like that of a pig's"
      if (ears == 11):
         tempStr = "Atop your head, you have small round ears that stand perk, like that of a skunk's"
      if (ears == 12):
         tempStr = "Hugging the sides of your head, you have long pointy ears with wavy-shaped lobes, colored vibrantly like the wings of a butterfly"
   return tempStr

def FaceDesc():
   global faceType
   tempStr = ""
   if (faceType == 10):
      tempStr += ", your face round with a moderate-sized nose"
   if (faceType == 20):
      tempStr += ", your face slightly longer than normal with large confident eyes"
   if (faceType == 21):
      tempStr += ", your face having a wide and strong muzzle with large confident eyes"
   if (faceType == 30):
      tempStr += ", your face looking slightly fierce with sharp teeth and focused eyes"
   if (faceType == 31):
      tempStr += ", your face having a narrow and toothy muzzle with focused eyes"
   if (faceType == 40):
      tempStr += ", your face somewhat flat with a small button nose"
   if (faceType == 41):
      tempStr += ", your face somewhat flat with a small button nose, long whiskers, and a general catty grin"
   if (faceType == 50):
      tempStr += ", your face seemingly docile with a broad nose and slightly gentle eyes"
   if (faceType == 51):
      tempStr += ", your face having a broad muzzle and calm gentle eyes"
   if (faceType == 60):
      tempStr += ", your face somewhat flat with a nose that is mostly a slight bump with two slits for nostrils"
   if (faceType == 61):
      tempStr += ", your face narrowing down a short muzzle with only slits for nostrils"
   if (faceType == 70):
      tempStr += ", your face somewhat flat with a twitchy button nose and large friendly eyes"
   if (faceType == 71):
      tempStr += ", your face somewhat flat with a twitchy button nose and whiskers, slightly buck-toothed, and your eyes large and friendly"
   if (faceType == 80):
      tempStr += ", your face somewhat narrowed with a curious button nose, your eyes careful of their surroundings"
   if (faceType == 81):
      tempStr += ", your face somewhat narrowed with a curious button nose, your eyes careful of their surroundings while your buck-teeth chitter as the whiskers on your puffy cheeks twitch"
   if (faceType == 90):
      tempStr += ", your face rather awake with your large hooked nose and constantly alert eyes"
   if (faceType == 91):
      tempStr += ", your face narrowing down to a razor-sharp beak that makes up your nose and mouth while your eyes are constantly watchful"
   if (faceType == 100):
      tempStr += ", your face rather round and somewhat pudgy"
   if (faceType == 101):
      tempStr += ", your face rather round and somewhat pudgy with a large upturned nose"
   if (faceType == 102):
      tempStr += ", your face rather round and somewhat pudgy with a large upturned nose and pointed tusks that grow up from the sides of your mouth to nearly obstruct your vision"
   if (faceType == 110):
      tempStr += ", your face somewhat long with a small button nose and cute eyes"
   if (faceType == 111):
      tempStr += ", your face somewhat long with a small button nose, long whiskers, and cute gentle eyes"
   if (faceType == 120):
      tempStr += ", your face somewhat flat with a chitinous bandage over the bridge of your nose and large gazing eyes"
   if (faceType == 121):
      tempStr += ", your face somewhat flat with a chitinous bandage over the bridge of your nose and large nectar-sucking lips that offset your large darkened eyes"
   return tempStr

def BoobDesc():
   global breastSize
   chance = Percent()
   tempStr = "BOOB ERROR " + breastSize
   if (chance <= 100):
      if (breastSize <= 0):
         tempStr = "flat"
      if (breastSize > 0) and (breastSize <= 2):
         tempStr = "nearly flat"
      if (breastSize > 2) and  (breastSize <= 8):
         tempStr = "noticeable"
      if (breastSize > 8) and (breastSize <= 20):
         tempStr = "large"
      if (breastSize > 20) and (breastSize <= 40):
         tempStr = "huge"
      if (breastSize > 40) and (breastSize <= 76):
         tempStr = "humongous"
      if (breastSize > 76) and (breastSize <= 146):
         tempStr = "massive"
      if (breastSize > 146) and (breastSize <= 210):
         tempStr = "gargantuan"
      if (breastSize > 210) and (breastSize <= 280):
         tempStr = "tremendous"
      if (breastSize > 280) and (breastSize <= 560):
         tempStr = "colossal"
      if (breastSize > 560):
         tempStr = "ridiculously huge"
   if (chance > 50):
      if (breastSize <= 0):
         tempStr = ""
      if (breastSize > 0) and (breastSize <= 2):
         tempStr = "tiny"
      if (breastSize > 2) and (breastSize <= 4):
         tempStr = "palmable"
      if (breastSize > 8) and (breastSize <= 20):
         tempStr = "ample"
      if (breastSize > 20) and (breastSize <= 40):
         tempStr = "head-sized"
      if (breastSize > 40) and (breastSize <= 76):
         tempStr = "hefty"
      if (breastSize > 76) and (breastSize <= 146):
         tempStr = "beachball-sized"
      if (breastSize > 146) and (breastSize <= 210):
         tempStr = "normally back-breaking"
      if (breastSize > 210) and (breastSize <= 280):
         tempStr = "view-obscuring"
      if (breastSize > 280) and (breastSize <= 560):
         tempStr = "bed-sized"
      if (breastSize > 560):
         tempStr = "road-filling"
   return tempStr

def UdderDesc():
   global udderSize
   chance = Percent()
   tempStr = "udder ERROR " + (udderSize / 2)
   if (chance <= 100):
      if ((udderSize / 2) <= 2):
         tempStr = "nearly flat"
      if ((udderSize / 2) > 2) and ((udderSize / 2) <= 8):
         tempStr = "noticeable"
      if ((udderSize / 2) > 8) and ((udderSize / 2) <= 20):
         tempStr = "large"
      if ((udderSize / 2) > 20) and ((udderSize / 2) <= 40):
         tempStr = "huge"
      if ((udderSize / 2) > 40) and ((udderSize / 2) <= 76):
         tempStr = "humongous"
      if ((udderSize / 2) > 76) and ((udderSize / 2) <= 146):
         tempStr = "massive"
      if ((udderSize / 2) > 146) and ((udderSize / 2) <= 210):
         tempStr = "gargantuan"
      if ((udderSize / 2) > 210) and ((udderSize / 2) <= 280):
         tempStr = "tremendous"
      if ((udderSize / 2) > 280) and ((udderSize / 2) <= 560):
         tempStr = "colossal"
      if ((udderSize / 2) > 560):
         tempStr = "ridiculously huge"
   if (chance > 50):
      if ((udderSize / 2) <= 2):
         tempStr = "tiny"
      if ((udderSize / 2) > 2) and ((udderSize / 2) <= 8):
         tempStr = "palmable"
      if ((udderSize / 2) > 8) and ((udderSize / 2) <= 20):
         tempStr = "ample"
      if ((udderSize / 2) > 20) and ((udderSize / 2) <= 40):
         tempStr = "head-sized"
      if ((udderSize / 2) > 40) and ((udderSize / 2) <= 76):
         tempStr = "hefty"
      if ((udderSize / 2) > 76) and ((udderSize / 2) <= 146):
         tempStr = "beachball-sized"
      if ((udderSize / 2) > 146) and ((udderSize / 2) <= 210):
         tempStr = "normally back-breaking"
      if ((udderSize / 2) > 210) and ((udderSize / 2) <= 280):
         tempStr = "view-obscuring"
      if ((udderSize / 2) > 280) and ((udderSize / 2) <= 560):
         tempStr = "bed-sized"
      if ((udderSize / 2) > 560):
         tempStr = "road-filling"
   return tempStr

def TeatDesc():
   global teatSize
   chance = Percent()
   tempStr = "TEAT ERROR " + teatSize
   if (chance <= 100):
      if (teatSize <= 2):
         tempStr = "normal"
      if (teatSize > 2) and (teatSize <= 5):
         tempStr = "noticeable"
      if (teatSize > 5) and (teatSize <= 9):
         tempStr = "blatant"
      if (teatSize > 9) and (teatSize <= 30):
         tempStr = "normal-for-a-cow"
      if (teatSize > 30) and (teatSize <= 50):
         tempStr = "cock-like"
      if (teatSize > 50) and (teatSize <= 100):
         tempStr = "horsecock-like"
      if (teatSize > 100) and (teatSize <= 140):
         tempStr = "arm-length"
      if (teatSize > 140) and (teatSize <= 300):
         tempStr = "street-clearing"
      if (teatSize > 300):
         tempStr = "obscene"
   if (chance > 50):
      if (teatSize <= 2):
         tempStr = ""
      if (teatSize > 2) and (teatSize <= 5):
         tempStr = "perky"
      if (teatSize > 5) and (teatSize <= 9):
         tempStr = "hypnotizing"
      if (teatSize > 9) and (teatSize <= 30):
         tempStr = "long"
      if (teatSize > 30) and (teatSize <= 50):
         tempStr = "huge"
      if (teatSize > 50) and (teatSize <= 100):
         tempStr = "enormous"
      if (teatSize > 100) and (teatSize <= 140):
         tempStr = "extreme"
      if (teatSize > 140) and (teatSize <= 300):
         tempStr = "ridiculous"
      if (teatSize > 300):
         tempStr = "obscene"
   return tempStr

def ButtDesc():
   global butt, buttMod
   chance = Percent()
   tempStr = "BUTT ERROR " + butt
   if (chance <= 100):
      if ((butt * buttMod) <= 2):
         tempStr = "flat"
      if ((butt * buttMod) > 2) and ((butt * buttMod) <= 5):
         tempStr = "tight"
      if ((butt * buttMod) > 5) and ((butt * buttMod) <= 15):
         tempStr = "ample"
      if ((butt * buttMod) > 15) and ((butt * buttMod) <= 30):
         tempStr = "large"
      if ((butt * buttMod) > 30) and ((butt * buttMod) <= 50):
         tempStr = "huge"
      if ((butt * buttMod) > 50) and ((butt * buttMod) <= 80):
         tempStr = "grand"
      if ((butt * buttMod) > 80) and ((butt * buttMod) <= 130):
         tempStr = "jumbo"
      if ((butt * buttMod) > 130) and ((butt * buttMod) <= 175):
         tempStr = "giant"
      if ((butt * buttMod) > 175):
         tempStr = "ginormous"
   if (chance > 50):
      if ((butt * buttMod) <= 2):
         tempStr = "boney"
      if ((butt * buttMod) > 2) and ((butt * buttMod) <= 5):
         tempStr = "firm"
      if ((butt * buttMod) > 5) and ((butt * buttMod) <= 15):
         tempStr = "grope-able"
      if ((butt * buttMod) > 15) and ((butt * buttMod) <= 30):
         tempStr = "jiggly"
      if ((butt * buttMod) > 30) and ((butt * buttMod) <= 50):
         tempStr = "pillow-like"
      if ((butt * buttMod) > 50) and ((butt * buttMod) <= 80):
         tempStr = "wobbling"
      if ((butt * buttMod) > 80) and ((butt * buttMod) <= 130):
         tempStr = "swaying"
      if ((butt * buttMod) > 130) and ((butt * buttMod) <= 175):
         tempStr = "bouncing"
      if ((butt * buttMod) > 175):
         tempStr = "constantly quivering"
   return tempStr

def VulvaDesc():
   global vulvaSize
   chance = Percent()
   tempStr = "VULVA ERROR " + vulvaSize
   if (chance <= 100):
      if (vulvaSize <= 2):
         tempStr = "tiny"
      if (vulvaSize > 2) and (vulvaSize <= 8):
         tempStr = "plush"
      if (vulvaSize > 8) and (vulvaSize <= 16):
         tempStr = "plump"
      if (vulvaSize > 16) and (vulvaSize <= 24):
         tempStr = "huge"
      if (vulvaSize > 24) and (vulvaSize <= 36):
         tempStr = "enormous"
      if (vulvaSize > 36) and (vulvaSize <= 54):
         tempStr = "gigantic"
      if (vulvaSize > 54) and (vulvaSize <= 84):
         tempStr = "humongous"
      if (vulvaSize > 84) and (vulvaSize <= 124):
         tempStr = "tremendous"
      if (vulvaSize > 124) and (vulvaSize <= 160):
         tempStr = "colossal"
      if (vulvaSize > 160):
         tempStr = "ridiculous"
   if (chance > 50):
      if (vulvaSize == 2):
         tempStr = "childlike"
      if (vulvaSize > 2) and (vulvaSize <= 8):
         tempStr = "dainty"
      if (vulvaSize > 8) and (vulvaSize <= 16):
         tempStr = "kissable"
      if (vulvaSize > 16) and (vulvaSize <= 24):
         tempStr = "groin-filling"
      if (vulvaSize > 24) and (vulvaSize <= 36):
         tempStr = "thigh-spreading"
      if (vulvaSize > 36) and (vulvaSize <= 54):
         tempStr = "" + LegDesc(1) + "-" + LegVerb(2) + ""
      if (vulvaSize > 54) and (vulvaSize <= 84):
         tempStr = "ground-scraping"
      if (vulvaSize > 84) and (vulvaSize <= 124):
         tempStr = "person-sized"
      if (vulvaSize > 124) and (vulvaSize <= 160):
         tempStr = "room-sized"
      if (vulvaSize > 160):
         tempStr = "building-sized"
   return tempStr

def CockDesc():
   global cockSize, cockSizeMod
   chance = Percent()
   tempCock = str(cockSize) * str(cockSizeMod)
   tempStr = "COCK ERROR " + tempCock
   if (chance <= 100):
      if (tempCock <= 8):
         tempStr = "puny"
      if (tempCock > 8) and (tempCock <= 12):
         tempStr = "average-sized"
      if (tempCock > 12) and (tempCock <= 24):
         tempStr = "big"
      if (tempCock > 24) and (tempCock <= 32):
         tempStr = "large"
      if (tempCock > 32) and (tempCock <= 56):
         tempStr = "huge"
      if (tempCock > 56) and (tempCock <= 72):
         tempStr = "enormous"
      if (tempCock > 72) and (tempCock <= 100):
         tempStr = "gigantic"
      if (tempCock > 100) and (tempCock <= 152):
         tempStr = "humongous"
      if (tempCock > 152) and (tempCock <= 304):
         tempStr = "tremendous"
      if (tempCock > 304) and (tempCock <= 608):
         tempStr = "colossal"
      if (tempCock > 608) and (tempCock <= 1200):
         tempStr = "ridiculous"
      if (tempCock > 1200):
         tempStr = "impossibly-ginormous"
   if (chance > 50):
      if (tempCock <= 8):
         tempStr = "infantile"
      if (tempCock > 8) and (tempCock <= 12):
         tempStr = "hand-length"
      if (tempCock > 12) and (tempCock <= 24):
         tempStr = "larger than normal"
      if (tempCock > 24) and (tempCock <= 32):
         tempStr = "foot-long"
      if (tempCock > 32) and (tempCock <= 56):
         tempStr = "thigh-slapping"
      if (tempCock > 56) and (tempCock <= 72):
         tempStr = "knee-knocking"
      if (tempCock > 72) and (tempCock <= 100):
         tempStr = "leg-sized"
      if (tempCock > 100) and (tempCock <= 152):
         tempStr = "person-sized"
      if (tempCock > 152) and (tempCock <= 304):
         tempStr = "car-sized"
      if (tempCock > 304) and (tempCock <= 608):
         tempStr = "bus-sized"
      if (tempCock > 608) and (tempCock <= 1200):
         tempStr = "building-sized"
      if (tempCock > 1200):
         tempStr = "landscape-filling"
   return tempStr

def BallDesc():
   global ballSize
   chance = Percent()
   tempStr = "BALLS ERROR " + ballSize
   if (chance <= 100):
      if (ballSize <= 1):
         tempStr = "tiny"
      if (ballSize > 1) and (ballSize <= 3):
         tempStr = "small"
      if (ballSize > 3) and (ballSize <= 5):
         tempStr = "big"
      if (ballSize > 5) and (ballSize <= 8):
         tempStr = "large"
      if (ballSize > 8) and (ballSize <= 13):
         tempStr = "hand-filling"
      if (ballSize > 13) and (ballSize <= 17):
         tempStr = "huge"
      if (ballSize > 17) and (ballSize <= 26):
         tempStr = "barely palmable"
      if (ballSize > 26) and (ballSize <= 40):
         tempStr = "enormous"
      if (ballSize > 40) and (ballSize <= 80):
         tempStr = "tremendous"
      if (ballSize > 80) and (ballSize <= 120):
         tempStr = "huggable"
      if (ballSize > 120) and (ballSize <= 240):
         tempStr = "gargantuan"
      if (ballSize > 240):
         tempStr = "colossal"
   if (chance > 50):
      if (ballSize <= 1):
         tempStr = "marble-sized"
      if (ballSize > 1) and (ballSize <= 3):
         tempStr = "golfball-sized"
      if (ballSize > 3) and (ballSize <= 5):
         tempStr = "kiwi-sized"
      if (ballSize > 5) and (ballSize <= 8):
         tempStr = "tennisball-sized"
      if (ballSize > 8) and (ballSize <= 13):
         tempStr = "baseball-sized"
      if (ballSize > 13) and (ballSize <= 17):
         tempStr = "softball-sized"
      if (ballSize > 17) and (ballSize <= 26):
         tempStr = "cantaloupe-sized"
      if (ballSize > 26) and (ballSize <= 40):
         tempStr = "basketball-sized"
      if (ballSize > 40) and (ballSize <= 80):
         tempStr = "watermelon-sized"
      if (ballSize > 80) and (ballSize <= 120):
         tempStr = "beachball-sized"
      if (ballSize > 120) and (ballSize <= 240):
         tempStr = "boulder-sized"
      if (ballSize > 240):
         tempStr = "landscape-crushing"
   return tempStr

def NipDesc():
   global nippleSize
   chance = Percent()
   tempStr = "NIPPLE ERROR " + nippleSize
   if (chance <= 100):
      if (nippleSize <= 2):
         tempStr = "small "
      if (nippleSize > 2) and (nippleSize <= 5):
         tempStr = "noticeable "
      if (nippleSize > 5) and (nippleSize <= 15):
         tempStr = "blatant "
      if (nippleSize > 15) and (nippleSize <= 30):
         tempStr = "teat-like "
      if (nippleSize > 30) and (nippleSize <= 50):
         tempStr = "cock-like "
      if (nippleSize > 50) and (nippleSize <= 100):
         tempStr = "horsecock-like "
      if (nippleSize > 100) and (nippleSize <= 140):
         tempStr = "arm-length "
      if (nippleSize > 140) and (nippleSize <= 300):
         tempStr = "street-clearing "
      if (nippleSize > 300):
         tempStr = "obscene "
      if (nipType == 2) and (lust < 50):
         tempStr = "inverted "
   if (chance > 50):
      if (nippleSize <= 2):
         tempStr = ""
      if (nippleSize > 2) and (nippleSize <= 5):
         tempStr = "perky "
      if (nippleSize > 5) and (nippleSize <= 15):
         tempStr = "hypnotizing "
      if (nippleSize > 15) and (nippleSize <= 30):
         tempStr = "long "
      if (nippleSize > 30) and (nippleSize <= 50):
         tempStr = "huge "
      if (nippleSize > 50) and (nippleSize <= 100):
         tempStr = "enormous "
      if (nippleSize > 100) and (nippleSize <= 140):
         tempStr = "extreme "
      if (nippleSize > 140) and (nippleSize <= 300):
         tempStr = "ridiculous "
      if (nippleSize > 300):
         tempStr = "obscene "
      if (nipType == 2) and (lust < 50):
         tempStr = "sunken "
   chance = Percent()
   if (nipType == 1):
      if (chance <= 50):
         tempStr += " quad-"
      else:
         tempStr = "quartets of " + tempStr
   return tempStr

def ClitDesc():
   global clitSize
   chance = Percent()
   tempStr = "CLIT ERROR " + clitSize
   if (chance <= 100):
      if (clitSize <= 2):
         tempStr = "tiny"
      if (clitSize > 2) and (clitSize <= 3):
         tempStr = "nibble-able"
      if (clitSize > 3) and (clitSize <= 6):
         tempStr = "protruding"
      if (clitSize > 6) and (clitSize <= 12):
         tempStr = "blatant"
      if (clitSize > 12) and (clitSize <= 25):
         tempStr = "suckable"
      if (clitSize > 25) and (clitSize <= 50):
         tempStr = "cock-like"
      if (clitSize > 50) and (clitSize <= 100):
         tempStr = "horsecock-like"
      if (clitSize > 100) and (clitSize <= 140):
         tempStr = "arm-length"
      if (clitSize > 140) and (clitSize <= 300):
         tempStr = "person-sized"
      if (clitSize > 300):
         tempStr = "obscene"
   if (chance > 50):
      if (clitSize <= 2):
         tempStr = "small"
      if (clitSize > 2) and (clitSize <= 3):
         tempStr = "pinchable"
      if (clitSize > 3) and (clitSize <= 6):
         tempStr = "flickable"
      if (clitSize > 6) and (clitSize <= 12):
         tempStr = "panty-tenting"
      if (clitSize > 12) and (clitSize <= 25):
         tempStr = "stroke-able"
      if (clitSize > 25) and (clitSize <= 50):
         tempStr = "huge"
      if (clitSize > 50) and (clitSize <= 100):
         tempStr = "gigantic"
      if (clitSize > 100) and (clitSize <= 140):
         tempStr = "doorway-smacking"
      if (clitSize > 140) and (clitSize <= 300):
         tempStr = "snuggle-able"
      if (clitSize > 300):
         tempStr = "obscene"
   return tempStr

def HipDesc():
   global hips, hipMod
   chance = Percent()
   tempStr = "HIP ERROR " + hips
   if (chance <= 100):
      if ((hips * hipMod) <= 3):
         tempStr = "narrow"
      if ((hips * hipMod) > 3) and ((hips * hipMod) <= 8):
         tempStr = "unnoticeable"
      if ((hips * hipMod) > 8) and ((hips * hipMod) <= 16):
         tempStr = "wide"
      if ((hips * hipMod) > 16) and ((hips * hipMod) <= 28):
         tempStr = "endowed"
      if ((hips * hipMod) > 28) and ((hips * hipMod) <= 40):
         tempStr = "protruding"
      if ((hips * hipMod) > 40) and ((hips * hipMod) <= 55):
         tempStr = "cow-like"
      if ((hips * hipMod) > 55) and ((hips * hipMod) <= 75):
         tempStr = "shelf-like"
      if ((hips * hipMod) > 75) and ((hips * hipMod) <= 100):
         tempStr = "doorway-jamming"
      if ((hips * hipMod) > 100):
         tempStr = "perpetually-swaying"
   if (chance > 50):
      if ((hips * hipMod) <= 3):
         tempStr = "prepubescent"
      if (((hips * hipMod) > 3) and ((hips * hipMod) <= 8)):
         tempStr = "average"
      if (((hips * hipMod) > 8) and ((hips * hipMod) <= 16)):
         tempStr = "child-bearing"
      if (((hips * hipMod) > 16) and ((hips * hipMod) <= 28)):
         tempStr = "especially fertile"
      if (((hips * hipMod) > 28) and ((hips * hipMod) <= 40)):
         tempStr = "hypnotizing"
      if (((hips * hipMod) > 40) and ((hips * hipMod) <= 55)):
         tempStr = "blatantly obvious"
      if (((hips * hipMod) > 55) and ((hips * hipMod) <= 75)):
         tempStr = "excessively wide"
      if (((hips * hipMod) > 75) and ((hips * hipMod) <= 100)):
         tempStr = "greatly protruding"
      if ((hips * hipMod) > 100):
         tempStr = "gigantic"
   return tempStr

def BellyDesc():
   global pregnancyTime, vagBellyMod, bellyMod, tallness
   chance = Percent()
   tempBelly = ((pregnancyTime / 10) + (vagBellyMod / 3) + (bellyMod / 5)) * 60 / tallness
   tempStr = "BELLY ERROR " + tempBelly
   if (pregnancyTime > bellyMod):
      if (tempBelly <= 2):
         tempStr = "flat"
      elif (tempBelly <= 4):
         tempStr = "hardly noticeable"
      elif (tempBelly <= 7):
         tempStr = "protruding"
      elif (tempBelly <= 11):
         tempStr = "swollen"
      elif (tempBelly <= 14):
         tempStr = "cradleable"
      elif (tempBelly <= 19):
         tempStr = "unbalancing"
      elif (tempBelly <= 24):
         tempStr = "huggable"
      elif (tempBelly <= 30):
         tempStr = "path-crowding"
      elif (tempBelly <= 36):
         tempStr = "larger-than-you"
      elif (tempBelly <= 42):
         tempStr = "ground-dragging"
      elif (tempBelly <= 49):
         tempStr = "view-blocking"
      elif (tempBelly <= 57):
         tempStr = "impossibly huge"
      elif (tempBelly <= 66):
         tempStr = "bed-sized"
      elif (tempBelly <= 76):
         tempStr = "portable-apartment"
      else:
         tempStr = "breeding-factory"
      if ((chance <= 50) and (tempBelly > 11)):
         tempStr += " pregnant"
      elif (tempBelly > 11):
         tempStr += " gravid"
   else:
      if (tempBelly <= 2):
         tempStr = "flat"
      elif (tempBelly <= 4):
         tempStr = "hardly noticeable"
      elif (tempBelly <= 7):
         tempStr = "chubby"
      elif (tempBelly <= 11):
         tempStr = "porky"
      elif (tempBelly <= 14):
         tempStr = "multi-rolled"
      elif (tempBelly <= 19):
         tempStr = "pillow-like"
      elif (tempBelly <= 24):
         tempStr = "morbidly obese"
      elif (tempBelly <= 30):
         tempStr = "bed-like"
      elif (tempBelly <= 36):
         tempStr = "fat-encompassing"
      elif (tempBelly <= 42):
         tempStr = "item-losing"
      elif (tempBelly <= 49):
         tempStr = "almost spherical"
      elif (tempBelly <= 57):
         tempStr = "limb-engulfing"
      elif (tempBelly <= 66):
         tempStr = "blob-like"
      elif (tempBelly <= 76):
         tempStr = "inhumanly large"
      else:
         tempStr = "gigantic blubbery mass of"
      if ((chance <= 50) and (tempBelly > 11)):
         tempStr += " jiggly"
      elif (tempBelly > 11):
         tempStr += " meaty"
   return tempStr

def SkinDesc():
   global skinType, snuggleBall, skinColor
   tempStr = "SKIN ERROR " + skinType
   if (skinType == 1):
      tempStr = "skin"
   if (skinType == 2):
      tempStr = "fur"
   if (skinType == 3):
      tempStr = "scales"
   if (skinType == 4):
      tempStr = "feathers"
   if (skinType == 5):
      tempStr = "chitin"
   if (snuggleBall == True):
      tempStr = "plush and snuggly " + tempStr
   if (skinColor > 0):
      tempStr = "" + SkinC() + "" + tempStr
   return tempStr

def SkinC():
   global skinColor
   tempStr = "SKIN COLOR ERROR " + skinColor
   if (skinColor == 0):
      tempStr = ""
   if (skinColor == 1):
      tempStr = "black "
   if (skinColor == 2):
      tempStr = "blonde "
   if (skinColor == 3):
      tempStr = "red "
   if (skinColor == 4):
      tempStr = "brown "
   if (skinColor == 5):
      tempStr = "coral pink "
   if (skinColor == 6):
      tempStr = "auburn "
   if (skinColor == 7):
      tempStr = "brown "
   if (skinColor == 8):
      tempStr = "grey "
   if (skinColor == 9):
      tempStr = "white "
   return tempStr

def legDesc(part:int):
   global legType
   tempStr = "LEG ERROR PART " + part + " TYPE " + legType
   if (part == 1):
      tempStr = "leg"
   if (part == 2):
      tempStr = "legs"
   if (part == 3):
      tempStr = "thigh"
   if (part == 4):
      tempStr = "thighs"
   if (part == 5):
      tempStr = "knee"
   if (part == 6):
      tempStr = "knees"
   if (part == 7):
      tempStr = "ankle"
   if (part == 8):
      tempStr = "ankles"
   if (part == 9):
      tempStr = "foot"
      if (legType == 1):
         tempStr = "paw"
      if (legType == 1001):
         tempStr = "hoof"
      if (CheckItem(102) == True):
         tempStr = "hoof"
   if (part == 10):
      tempStr = "feet"
      if (legType == 1):
         tempStr = "paws"
      if (legType == 1001):
         tempStr = "hooves"
      if (CheckItem(102) == True):
         tempStr = "hooves"
   return tempStr

def LegVerb(part:int):
   global legType
   tempStr = "LEG VERB ERROR " + part + " TYPE " + legType
   if (part == 1):
      tempStr = "spreading"
   if (part == 2):
      tempStr = "spread wide"
   if (part == 3):
      tempStr = "spread"
   if (part == 4):
      tempStr = "clench"
   if (part == 5):
      tempStr = "straddling"
   return tempStr

def LegWhere(part:int):
   global legType
   tempStr = "LEG WHERE ERROR " + part + " TYPE " + legType
   if (part == 1):
      tempStr = "between"
      if (legType == 1001):
         tempStr = "behind"
   if (part == 2):
      tempStr = "between"
   return tempStr

def LegPlural(which:int):
   global legType
   tempStr = "LEG PLURAL ERROR TYPE " + legType
   if (which == 1):
      tempStr = ""
   if (which == 2):
      tempStr = "are"
   return tempStr

def RegionName(tempInt:int):
   global currentZone
   tempStr = "REGION ERROR " + currentZone
   if (tempInt == 1):
      tempStr = "Softlik"
   if (tempInt == 2):
      tempStr = "Firmshaft"
   if (tempInt == 3):
      tempStr = "Tieden"
   if (tempInt == 4):
      tempStr = "Siz'Calit"
   if (tempInt == 6):
      tempStr = "Oviasis"
   if (tempInt == 12):
      tempStr = "Sanctuary"
   return tempStr

def RaceName():
   global race
   tempStr = "RACE ERROR " + race
   if (race == 1):
      tempStr = "Human"
   if (race == 2):
      tempStr = "Equan"
   if (race == 3):
      tempStr = "Lupan"
   if (race == 4):
      tempStr = "Felin"
   if (race == 6):
      tempStr = "Lizan"
   return tempStr

def DomName():
   global dominant
   tempStr = "DOMINANT ERROR " + dominant
   if (dominant == 1):
      tempStr = "human"
   if (dominant == 2):
      tempStr = "horse"
   if (dominant == 3):
      tempStr = "wolf"
   if (dominant == 4):
      tempStr = "cat"
   if (dominant == 5):
      tempStr = "cow"
   if (dominant == 6):
      tempStr = "lizard"
   if (dominant == 7):
      empStr = "bunny"
   if (dominant == 8):
      tempStr = "mouse"
   if (dominant == 9):
      tempStr = "bird"
   if (dominant == 10):
      tempStr = "pig"
   if (dominant == 11):
      tempStr = "skunk"
   if (dominant == 12):
      tempStr = "bug"
   return tempStr

def GenName():
   global gender, hips, breastSize, body.
   tempStr = "GENDER ERROR " + gender
   if (gender == 0):
      tempStr = "n androgynous"
   if (gender == 1):
      tempStr = " male"
   if ((gender == 1) and (hips > 3) and (breastSize > 4)):
      tempStr = " female"
   if gender == 2:
      tempStr = " female"
   if ((gender == 2) and (body > 17) and (breastSize <= 2)):
      tempStr = " male"
   if (gender == 3):
      tempStr = " herm"
   return tempStr

def CumAmount():
   global blueBalls, ballSize, balls, cumMod
   tempNum = 0
   if (blueBalls <= 12):
      tempNum = ballSize * (ballSize / 2) * balls * cumMod * 0.5
   if ((blueBalls > 12) and (blueBalls <= 36)):
      tempNum = ballSize * (ballSize / 2) * balls * cumMod * 1
   if ((blueBalls > 36) and (blueBalls <= 84)):
      tempNum = ballSize * (ballSize / 2) * balls * cumMod * 2
   if (blueBalls > 84):
      tempNum = ballSize * (ballSize / 2) * balls * cumMod * 2.5
   blueBalls = 0
   return int(math.floor(tempNum))

def MilkAmount(origin:int):
   global milkEngorgement, breastSize, tallness, milkCap, milkEngorgementLevel, udderEngorgement, udderSize
   tempNum = 0
   if origin == 1:
      if (milkEngorgement > ((breastSize * (breastSize + 1) + (tallness / 4) + milkCap) * 2)):
         milkEngorgement = (breastSize * (breastSize + 1) + (tallness / 4) + milkCap) * 2
      if (milkEngorgementLevel == 0):
         if (boobTotal == 2):
            tempNum = milkEngorgement * 0.5 * 2
         if (boobTotal == 4):
            tempNum = milkEngorgement * 0.5 * 4
         if (boobTotal == 6):
            tempNum = milkEngorgement * 0.5 * 3.5
         if (boobTotal == 8):
            tempNum = milkEngorgement * 0.5 * 6
         if (boobTotal == 10):
            tempNum = milkEngorgement * 0.5 * 8
      if (milkEngorgementLevel == 1):
         if (boobTotal == 2):
            tempNum = milkEngorgement * 1 * 2
         if (boobTotal == 4):
            tempNum = milkEngorgement * 1 * 4
         if (boobTotal == 6):
            tempNum = milkEngorgement * 1 * 3.5
         if (boobTotal == 8):
            tempNum = milkEngorgement * 1 * 6
         if (boobTotal == 10):
            tempNum = milkEngorgement * 1 * 8
      if (milkEngorgementLevel == 2):
         if (boobTotal == 2):
            tempNum = milkEngorgement * 1.2 * 2
         if (boobTotal == 4):
            tempNum = milkEngorgement * 1.2 * 4
         if (boobTotal == 6):
            tempNum = milkEngorgement * 1.2 * 3.5
         if (boobTotal == 8):
            tempNum = milkEngorgement * 1.2 * 6
         if (boobTotal == 10):
            tempNum = milkEngorgement * 1.2 * 8
      if (milkEngorgementLevel == 3):
         if (boobTotal == 2):
            tempNum = milkEngorgement * 1.5 * 2
         if (boobTotal == 4):
            tempNum = milkEngorgement * 1.5 * 4
         if (boobTotal == 6):
            tempNum = milkEngorgement * 1.5 * 3.5
         if (boobTotal == 8):
            tempNum = milkEngorgement * 1.5 * 6
         if (boobTotal == 10):
            tempNum = milkEngorgement * 1.5 * 8
      if (milkEngorgementLevel == 1):
         milkEngorgementLevel = 0
         BoobChange(-1)
      if (milkEngorgementLevel == 2):
         milkEngorgementLevel = 0
         BoobChange(-2)
      if (milkEngorgementLevel > 2):
         milkEngorgementLevel = 0
         BoobChange(-3)
      milkEngorgement = 0
   if origin == 2:
      if (udderEngorgement > ((udderSize * (udderSize + 1) + (tallness / 4) + milkCap) * 2)):
         udderEngorgement = (udderSize * (udderSize + 1) + (tallness / 4) + milkCap) * 2
      if (udderEngorgementLevel == 0):
         tempNum = udderEngorgement * 1
      if (udderEngorgementLevel == 1):
         tempNum = udderEngorgement * 2.1
      if (udderEngorgementLevel == 2):
         tempNum = udderEngorgement * 2.7
      if (udderEngorgementLevel == 3):
         tempNum = udderEngorgement * 3.5
      if (udderEngorgementLevel == 1):
         udderEngorgementLevel = 0
         UdderChange(-2)
      if (udderEngorgementLevel == 2):
         udderEngorgementLevel = 0
         UdderChange(-5)
      if (udderEngorgementLevel > 2):
         udderEngorgementLevel = 0
         UdderChange(-8)
      udderEngorgement = 0
   return int(math.floor(tempNum))

#def __setProp_scrollBar2_Scene1_TextFields_0():
#def __setProp_scrollBar1_Scene1_TextFields_0():
def Frame1():
   global versionNumber, theme, fontSize, fontBold, fontColor, showSide, i, buttonChoice, currentText, sideText, sideFocus, pregTempInt, pregTempBool, lustArray, bg, rndResult, rndArray, textCheckArray, choiceListArray, choiceListResult, choicePage, moveItemID, moveItemStack, skipExhaustion, shiftHeld, currentState, inBag, inShop, currentZone, day, hour, inDungeon, currentDungeon, _str_, ment, lib, sen, HP, lust, coin, strMod, mentMod, libMod, senMod, strength, mentality, libido, sensitivity, hunger, hrs, itemGainArray, human, horse, wolf, cat, cow, lizard, rabbit, mouse, bird, pig, skunk, bug, SexP, levelUP, level, runMod, rapeMod, cumMod, cockSizeMod, vagSizeMod, vagElastic, milkMod, carryMod, vagBellyMod, pregChanceMod, extraPregChance, pregTimeMod, enticeMod, milkHPMod, changeMod, HPMod, SexPMod, minLust, milkCap, coinMod, hipMod, buttMod, bellyMod, cockMoistMod, vagMoistMod, lockTail, lockFace, lockSkin, lockBreasts, lockEars, lockLegs, lockNipples, lockCock, enemyID, eHP, eStr, eMenta, eSen, eLib, eLust, eGen, ePref, eCoin, eSexP, eItem, gender, race, body, dominant, hips, butt, tallness, skinType, tial, ears, hair, hairLength, hairColor, legType, wings, faceType, skinColor, cockTotal, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, rabbitCocks, cockSize, cockMoist, balls, ballSize, showBalls, knot, bugCocks, breastSize, boobTotal, nippleSize, udders, udderSize, teatSize, clitSize, vagTotal, vagSize, vagMoist, vulvaSize, nipType, attireTop, attireBot, weapon, pregArray, pregStatus, pregnancyTime, pregRate, eggLaying, eggMaxTime, eggTime, eggRate, exhaustion, exhaustionPenalty, milkEngorgement, milkEngorgementLevel, udderEngorgement, udderEngorgementLevel, heat, heatTime, heatMaxTime, lactation, udderLactation, nipplePlay, udderPlay, blueBalls, teatPump, nipPump, cockPump, clitPump, vulvaPump, masoPot, sMasoPot, babyFree, charmTime, pheromone, eggceleratorTime, eggceleratorDose, bodyOil, lustPenalty, snuggleBall, fertileGel, eggType, milkSuppressant, milkSuppressantLact, milkSuppressantUdder, suppHarness, fertilityStatueCurse, plumpQuats, lilaWetStatus, cockSnakePreg, milkCPoisonNip, milkCPoisonUdd, cockSnakeVenom, humanAffinity, horseAffinity, wolfAffinity, catAffinity, cowAffinity, lizardAffinity, rabbitAffinity, fourBoobAffinity, mouseAffinity, birdAffinity, pigAffinity, twoBoobAffinity, sixBoobAffinity, eightBoobAffinity, tenBoobAffinity, cowTaurAffinity, humanTaurAffinity, skunkAffinity, bugAffinity, lilaRep, lilaVulva, lilaMilk, lilaPreg, malonRep, malonPreg, malonChildren, mistressRep, jamieRep, jamieSize, jamieChildren, silRep, silPreg, silRate, silLay, silTired, silGrowthTime, lilaUB, dairyFarmBrand, jamieRep1, jamieRep2, jamieRep3, lilaWetness, jamieButt, jamieBreasts, jamieHair, travArray, foundSoftlik, foundFirmshaft, foundTieden, foundSizCalit, foundOviasis, foundValley, foundSanctuary, defeatedMinotaur, defeatedFreakyGirl, defeatedSuccubus, firstExplore, knowLustDraft, knowRejuvPot, knowExpPreg, knowBallSwell, knowMaleEnhance, knowSLustDraft, knowSRejuvPot, knowSExpPreg, knowSBallSwell, knowBabyFree, knowPotPot, knowGenSwap, knowMasoPot, knowMilkSuppress, knowSGenSwap, knowSMasoPot, knowSBabyFree, knowSPotPot, knowPussJuice, knowPheromone, knowBazoomba, babyFactLevel, bodyBuildLevel, hyperHappyLevel, alchemistLevel, fetishMasterLevel, milkMaidLevel, shapeshiftyLevel, shapeshiftyFirst, shapeshiftySecond, maleFetish, femaleFetish, hermFetish, narcissistFetish, dependentFetish, dominantFetish, submissiveFetish, lboobFetish, sboobFetish, furryFetish, scalyFetish, smoothyFetish, pregnancyFetish, bestialityFetish, milkFetish, sizeFetish, unbirthingFetish, ovipositionFetish, toyFetish, hyperFetish, currentDayCare, humanChildren, equanChildren, lupanChildren, felinChildren, cowChildren, lizanEggs, lizanChildren, bunnionChildren, wolfPupChildren, miceChildren, birdEggs, birdChildren, pigChildren, calfChildren, bugEggs, bugChildren, skunkChildren, minotaurChildren, freakyGirlChildren, bagPage, bagArray, bagStackArray, stashArray, stashStackArray, statPaneVisible, levelPaneVisible, currentRegionVisible, regionVisible, saveGameVisible, DayPaneVisible, Option7Visible, appearanceTextVisible, appearanceBoxVisible
   versionNumber = "0.975o"
   theme = 0
   fontSize = 14
   fontBold = False
   fontColor = "000000"
   showSide = True
   i = 0
   buttonChoice = 0
   currentText = ""
   sideText = ""
   sideFocus = 1
   pregTempInt = 0
   pregTempBool = False
   lustArray = list(())
   bg = new Sprite()
   rndResult = 0
   rndArray = list(())
   textCheckArray = list(())
   choiceListArray = list(())
   choiceListResult = list(())
   choicePage = 0
   moveItemID = 0
   moveItemStack = 0
   skipExhaustion = False
   shiftHeld = False
   currentState = 0
   inBag = False
   inShop = False
   currentZone = 0
   day = 0
   hour = 8
   inDungeon = False
   currentDungeon = 0
   _str_ = 0
   ment = 0
   lib = 0
   sen = 0
   HP = 0
   lust = 0
   coin = 0
   strMod = 0
   mentMod = 0
   libMod = 0
   senMod = 0
   strength = 0
   mentality = 0
   libido = 0
   sensitivity = 0
   hunger = 0
   hrs = 0
   itemGainArray = list(())
   human = 0
   horse = 0
   wolf = 0
   cat = 0
   cow = 0
   lizard = 0
   rabbit = 0
   mouse = 0
   bird = 0
   pig = 0
   skunk = 0
   bug = 0
   SexP = 0
   levelUP = 0
   level = 0
   eunMod = 0
   rapeMod = 0
   cumMod = 1
   cockSizeMod = 1
   vagSizeMod = 1
   vagElastic = 1
   milkMod = 0
   carryMod = 0
   vagBellyMod = 0
   pregChanceMod = 0
   extraPregChance = 0
   pregTimeMod = 0
   enticeMod = 0
   milkHPMod = 0
   changeMod = 1
   HPMod = 0
   SexPMod = 1
   minLust = 0
   milkCap = 0
   coinMod = 0
   hipMod = 1
   buttMod = 1
   bellyMod = 0
   cockMoistMod = 0
   vagMoistMod = 0
   lockTail = 0
   lockFace = 0
   lockSkin = 0
   lockBreasts = 0
   lockEars = 0
   lockLegs = 0
   lockNipples = 0
   lockCock = 0
   enemyID = 0
   eHP = 0
   eMaxHP = 0
   eStr = 0
   eMenta = 0
   eSen = 0
   eLib = 0
   eLust = 0
   eGen = 0
   ePref = 0
   eCoin = 0
   eSexP = 0
   eItem = 0
   gender = 0
   race = 0
   body = 0
   dominant = 0
   hips = 0
   butt = 0
   tallness = 0
   skinType = 0
   tail = 0
   ears = 0
   hair = 0
   hairLength = 0
   hairColor = 0
   legType = 0
   wings = 0
   faceType = 0
   skinColor = 0
   cockTotal = 0
   humanCocks = 0
   horseCocks = 0
   wolfCocks = 0
   catCocks = 0
   lizardCocks = 0
   rabbitCocks = 0
   cockSize = 0
   cockMoist = 0
   balls = 0
   ballSize = 0
   showBalls = True
   knot = False
   bugCocks = 0
   breastSize = 0
   boobTotal = 0
   nippleSize = 1
   udders = False
   udderSize = 0
   teatSize = 0
   clitSize = 0
   vagTotal = 0
   globalvagSize
   vagSize = 0
   vagMoist = 0
   vulvaSize = 0
   nipType = 0
   attireTop = 1
   attireBot = 2
   weapon = 10
   pregArray = list(())
   pregStatus = 0
   pregnancyTime = 0
   pregRate = 1
   eggLaying = 0
   eggMaxTime = 0
   eggTime = 0
   eggRate = 0
   exhaustion = 0
   exhaustionPenalty = 0
   milkEngorgement = 0
   milkEngorgementLevel = 0
   udderEngorgement = 0
   udderEngorgementLeve = 0
   heat = 0
   heatTime = 0
   heatMaxTime = 0
   lactation = 0
   udderLactation = 0
   nipplePlay = 0
   udderPlay = 0
   blueBalls = 0
   teatPump = 0
   nipPump = 0
   cockPump = 0
   clitPump = 0
   vulvaPump = 0
   masoPot = 0
   sMasoPot = 0
   babyFree = 0
   charmTime = 0
   pheromone = 0
   eggceleratorTime = 0
   eggceleratorDose = 0
   bodyOil = 0
   lustPenalty = 0
   suggleBall = False
   fertileGel = 0
   eggType = 0
   milkSuppressany = 0
   milkSuppressantLact = 0
   milkSuppressantUdder = 0
   suppHarness = False
   fertilityStatueCurse = 0
   plumpGuats = 0
   lilaWetStatus = 0
   cockSnakePreg = 0
   milkCPoisonNip = 0
   milkCPoisonUdd = 0
   cockSnakeVenom = 0
   humanAffinity = 0
   horseAffinity = 0
   wolfAffinity = 0
   catAffinity = 0
   cowAffinity = 0
   lizardAffinity = 0
   rabbitAffinity = 0
   fourBoobAffinity = 0
   mouseAffinity = 0
   birdAffinity = 0
   pigAffinity = 0
   twoBoobAffinity = 0
   sixBoobAffinity = 0
   eightBoobAffinity = 0
   tenBoobAffinity = 0
   cowTaurAffinity = 0
   humanTaurAffinity = 0
   skunkAffinity = 0
   bugAffinity = 0
   lilaRep = 0
   lilaVulva = 0
   lilaMilk = 0
   lilaPreg = -2
   malonRep = 0
   malonPreg = 0
   malonChildren = 0
   mistressRep = 0
   jamieRep = 0
   jamieSize = 4
   jamieChildren = 0
   silRep = 0
   silPreg = 0
   silRate = 0
   silLay = 10
   silTied = False
   silGrowthTime = 0
   lilaUB = False
   dairyFarmBrand = False
   jamieRep1 = 0
   jamieRep2 = 0
   jamieRep3 = 0
   lilaWetness = 0
   jamieButt = False
   jamieBreasts = False
   jamieHair = False
   travArray = list(())
   foundSoftlik = False
   foundFirmshaft = False
   foundTieden = False
   foundSizCalit = False
   foundOviasis = False
   foundValley = False
   foundSanctuary = False
   defeatedMinotaur = False
   defeatedFreakyGirl = False
   defeatedSuccubus = False
   firstExplore = False
   knowLustDraft = False
   knowRejuvPot = False
   knowExpPreg = False
   knowBallSwell = False
   knowMaleEnhance = False
   knowSLustDraft = False
   knowSRejuvPot = False
   knowSExpPreg = False
   knowSBallSwell = False
   knowBabyFree = False
   knowPotPot = False
   knowGenSwap = False
   knowMasoPot = False
   knowMilkSuppress = False
   knowSGenSwap = False
   knowSMasoPot = False
   knowSBabyFree = False
   knowSPotPot = False
   knowPussJuice = False
   knowPheromone = False
   knowBazoomba = False
   babyFactLevel = 0
   bodyBuildLevel = 0
   hyperHappyLevel = 0
   alchemistLevel = 0
   fetishMasterLevel = 0
   milkMaidLevel = 0
   shapeshiftyLevel = 0
   ShapeshiftyFirst = ""
   shapeshiftySecond = ""
   maleFetish = 1
   femaleFetish = 1
   hermFetish = 1
   narcissistFetish = 1
   dependentFetish = 1
   dominantFetish = 1
   submissiveFetish = 1
   lboobFetish = 1
   sboobFetish = 1
   furryFetish = 1
   scalyFetish = 1
   smoothyFetish = 1
   pregnancyFetish = 1
   bestialityFetish = 1
   milkFetish = 1
   sizeFetish = 1
   unbirthingFetish = 1
   ovipostitionFetish = 1
   toyFetish = 1
   hyperFetish = 1
   currentDayCare = 0
   humanChildren = 0
   equanChildren = 0
   lupanChildren = 0
   felinChildren = 0
   cowChildren = 0
   lizanEggs = 0
   lizanChildren = 0
   bunnionChildren = 0
   wolfPupChildren = 0
   miceChildren = 0
   birdEggs = 0
   birdChildren = 0
   pigChildren = 0
   calfChildren = 0
   bugEggs = 0
   bugChildren = 0
   skunkChildren = 0
   minotaurChildren = 0
   freakyGirlChildren = 0
   bagPage = 1
   bagArray = list(())
   bagStackArray = list(())
   stashArray = list(())
   stashStackArray = list(())
   statPaneVisible = False
   levelPaneVisible = False
   currentRegionVisible = False
   regionVisible = False
   saveGameVisible = False
   DayPaneVisible = False
   Option7Visible = False
   appearanceTextVisible = False
   appearanceBoxVisible = False
   SideHide()
   ButtonFunctions.Visible(0,0,0,0,0,0,0,0,0,0,0,0)
   HideAmount()
   HideUpDown()
   LoadPreferences()
   OutputMainText("Nimin: Fetish Fantasy" + "\n" + "    v" + versionNumber + "\n" + "\n" + "Click 'New Game' to begin a new game." + "\n" + "\n" + "Created by:    --Xadera" + "\n" + "    www.furaffinity.net/user/xadera/" + "\n" + "\n" + "Original concept by:     --Fenoxo" + "\n" + "    fenoxo.com" + "\n" + "\n" + "Currently maintained by:    ajdelguidice" + "\n" + "    github.com/ajdelguidice" + "\n" + "For tutorial/guide, questions, or bug reports, visit github.com/ajdelguidice/pymin/", True)

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
        global button1, button1Visible
    def Show():
        if button1Visible == False:
            button1 = tkinter.Button(buttonpanel, text="Button 1", command=ButtonEvent1)
            button1.place(anchor=NW, height=46, width=140, x=0, y=0)
            button1Visible = True
    def Hide():
        if button1Visible == True:
            button1.destroy()
            button1Visible = False
class PanelButton2:
    def __init__():
        global button2, button2Visible
    def Show():
        if button2Visible == False:
            button2 = tkinter.Button(buttonpanel, text="Button 2", command=ButtonEvent2)
            button2.place(anchor=NW, height=46, width=140, x=160, y=0)
            button2Visible = True
    def Hide():
        if button2Visible == True:
            button2.destroy()
            button2Visible = False 
class PanelButton3:
    def __init__():
        global button3, button3Visible
    def Show():
        if button3Visible == False:
            button3 = tkinter.Button(buttonpanel, text="Button 3", command=ButtonEvent3)
            button3.place(anchor=NW, height=46, width=140, x=320, y=0)
            button3Visible = True
    def Hide():
        if button3Visible == True:
            button3.destroy()
            button3Visible = False
class PanelButton4:
    def __init__():
        global button4, button4Visible
    def Show():
        if button4Visible == False:
            button4 = tkinter.Button(buttonpanel, text="Button 4", command=ButtonEvent4)
            button4.place(anchor=NW, height=46, width=140, x=480, y=0)
            button4Visible = True
    def Hide():
        if button4Visible == True:
            button4.destroy()
            button4Visible = False
class PanelButton5:
    def __init__():
        global button5, button5Visible
    def Show():
        if button5Visible == False:
            button5 = tkinter.Button(buttonpanel, text="Button 5", command=ButtonEvent5)
            button5.place(anchor=NW, height=46, width=140, x=0, y=66)
            button5Visible = True
    def Hide():
        if button5Visible ==True:
            button5.destroy()
            button5Visible = False
class PanelButton6:
    def __init__():
        global button6, button6Visible
    def Show():
        if button6Visible == False:
            button6 = tkinter.Button(buttonpanel, text="Button 6", command=ButtonEvent6)
            button6.place(anchor=NW, height=46, width=140, x=160, y=66)
            button6Visible = True
    def Hide():
        if button6Visible ==True:
            button6.destroy()
            button6Visible = False
class PanelButton7:
    def __init__():
        global button7, button7Visible
    def Show():
        if button7Visible == False:
            button7 = tkinter.Button(buttonpanel, text="Button 7", command=ButtonEvent7)
            button7.place(anchor=NW, height=46, width=140, x=320, y=66)
            button7Visible = True
    def Hide():
        if button7Visible == True:
            button7.destroy()
            button7Visible = False
class PanelButton8:
    def __init__():
        global button8, button8Visible
    def Show():
        if button8Visible == False:
            button8 = tkinter.Button(buttonpanel, text="Button 8", command=ButtonEvent8)
            button8.place(anchor=NW, height=46, width=140, x=480, y=66)
            button8Visible = True
    def Hide():
        if button8Visible == True:
            button8.destroy()
            button8Visible = False
class PanelButton9:
    def __init__():
        global button9, button9Visible
    def Show():
        if button9Visible == False:
            button9 = tkinter.Button(buttonpanel, text="Button 9", command=ButtonEvent9)
            button9.place(anchor=NW, height=46, width=140, x=0, y=132)
            button9Visible = True
    def Hide():
        if button9Visible == True:
            button9.destroy()
            button9Visible = False
class PanelButton10:
    def __init__():
        global button10, button10Visible
    def Show():
        if button10Visible == False:
            button10 = tkinter.Button(buttonpanel, text="Button 10", command=ButtonEvent10)
            button10.place(anchor=NW, height=46, width=140, x=160, y=132)
            button10Visible = True
    def Hide():
        if button10Visible == True:
            button10.destroy()
            button10Visible = False
class PanelButton11:
    def __init__():
        global button11, button11Visible
    def Show():
        if button11Visible == False:
            button11 = tkinter.Button(buttonpanel, text="Button 11", command=ButtonEvent11)
            button11.place(anchor=NW, height=46, width=140, x=320, y=132)
            button11Visible = True
    def Hide():
        if button11Visible == True:
            button11.destroy()
            button11Visible = False
class PanelButton12:
    def __init__():
        global button12, button12Visible
    def Show():
        if button12Visible == False:
            button12 = tkinter.Button(buttonpanel, text="Button 12", command=ButtonEvent12)
            button12.place(anchor=NW, height=46, width=140, x=480, y=132)
            button12Visible = True
    def Hide():
        if button12Visible == True:
            button12.destroy()
            button12Visible = False

class ButtonFunctions:
   def __init__():
      global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12
   def Visible(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
      if a1 == 0:
         PanelButton1.Hide()
      elif a1 == 1:
         PanelButton1.Show()
      if a2 == 0:
         PanelButton2.Hide()
      elif a2 == 1:
         PanelButton2.Show()
      if a3 == 0:
         PanelButton3.Hide()
      elif a3 == 1:
         PanelButton3.Show()
      if a4 == 0:
         PanelButton4.Hide()
      elif a4 == 1:
         PanelButton4.Show()
      if a5 == 0:
         PanelButton5.Hide()
      elif a5 == 1:
         PanelButton5.Show()
      if a6 == 0:
         PanelButton6.Hide()
      elif a6 == 1:
         PanelButton6.Show()
      if a7 == 0:
         PanelButton7.Hide()
      elif a7 == 1:
         PanelButton7.Show()
      if a8 == 0:
         PanelButton8.Hide()
      elif a8 == 1:
         PanelButton8.Show()
      if a9 == 0:
         PanelButton9.Hide()
      elif a9 == 1:
         PanelButton9.Show()
      if a10 == 0:
         PanelButton10.Hide()
      elif a10 == 1:
         PanelButton10.Show()
      if a11 == 0:
         PanelButton11.Hide()
      elif a11 == 1:
         PanelButton11.Show()
      if a12 == 0:
         PanelButton12.Hide()
      elif a12 == 1:
         PanelButton12.Show()

   def WriteText(a, b):
      if a == 1:
         button1["text"] = b
      if a == 2:
         button2["text"] = b
      if a == 3:
         button3["text"] = b
      if a == 4:
         button4["text"] = b
      if a == 5:
         button5["text"] = b
      if a == 6:
         button6["text"] = b
      if a == 7:
         button7["text"] = b
      if a == 8:
         button8["text"] = b
      if a == 9:
         button9["text"] = b
      if a == 10:
         button10["text"] = b
      if a == 11:
         button11["text"] = b
      if a == 12:
         button12["text"] = b

    def WriteCommand():
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
newgamebutton = tkinter.Button(statframe, text="New Game", command="NewGameStart")
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

button1 = tkinter.Button(buttonpanel, text="Button 1", command=ButtonEvent1)
button1.place(anchor=NW, height=46, width=140, x=0, y=0)
button2 = tkinter.Button(buttonpanel, text="Button 2", command=ButtonEvent2)
button2.place(anchor=NW, height=46, width=140, x=160, y=0)
button3 = tkinter.Button(buttonpanel, text="Button 3", command=ButtonEvent3)
button3.place(anchor=NW, height=46, width=140, x=320, y=0)
button4 = tkinter.Button(buttonpanel, text="Button 4", command=ButtonEvent4)
button4.place(anchor=NW, height=46, width=140, x=480, y=0)
button5 = tkinter.Button(buttonpanel, text="Button 5", command=ButtonEvent5)
button5.place(anchor=NW, height=46, width=140, x=0, y=66)
button6 = tkinter.Button(buttonpanel, text="Button 6", command=ButtonEvent6)
button6.place(anchor=NW, height=46, width=140, x=160, y=66)
button7 = tkinter.Button(buttonpanel, text="Button 7", command=ButtonEvent7)
button7.place(anchor=NW, height=46, width=140, x=320, y=66)
button8 = tkinter.Button(buttonpanel, text="Button 8", command=ButtonEvent8)
button8.place(anchor=NW, height=46, width=140, x=480, y=66)
button9 = tkinter.Button(buttonpanel, text="Button 9", command=ButtonEvent9)
button9.place(anchor=NW, height=46, width=140, x=0, y=132)
button10 = tkinter.Button(buttonpanel, text="Button 10", command=ButtonEvent10)
button10.place(anchor=NW, height=46, width=140, x=160, y=132)
button11 = tkinter.Button(buttonpanel, text="Button 11", command=ButtonEvent11)
button11.place(anchor=NW, height=46, width=140, x=320, y=132)
button12 = tkinter.Button(buttonpanel, text="Button 12", command=ButtonEvent12)
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

themebutton = tkinter.Button(sidebar, text="Theme", command=Option1Event)
themebutton.place(anchor=NW, height=30, width=60, x=0, y=385)
textsizedownbutton = tkinter.Button(sidebar, text="A", command=Option2Event)
textsizedownbutton.place(anchor=NW, height=30, width=30, x=83, y=385)
textsizedownbutton["font"] = ("Times New Roman", 10)
textsizeresetbutton = tkinter.Button(sidebar, text="A", command=Option3Event)
textsizeresetbutton.place(anchor=NW, height=30, width=30, x=118, y=385)
textsizeresetbutton["font"] = ("Times New Roman", 12)
textsizeupbutton = tkinter.Button(sidebar, text="A", command=Option4Event)
textsizeupbutton.place(anchor=NW, height=30, width=30, x=153, y=385)
textsizeupbutton["font"] = ("Times New Roman", 14)
textboldbutton = tkinter.Button(sidebar, text="B", command=Option5Event)
textboldbutton.place(anchor=NW, height=30, width=30, x=200, y=385)
textcolorbutton = tkinter.Button(sidebar, text="C", command=Option6Event)
textcolorbutton.place(anchor=NW, height=30, width=30, x=245, y=385)
themebutton7 = tkinter.Button(sidebar, text="O", command=Option7Event)
themebutton7.place(anchor=NW, height=30, width=30, x=301, y=385)
"""
appearancebutton.destroy()
ChangeTKBColor("#FFFFFF")
ChangeTKFColor("#000000")
UpdateText()
"""
Frame1()
root.mainloop()