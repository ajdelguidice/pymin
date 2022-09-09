import math
import random




def init():
     global Option3 #TextField
     global Side2 #TextField
     global lustDown #downArrow
     global Amount1 #TextField
     global Amount11 #TextField
     global AmountOutline2 #MovieClip
     global Choice3 #TextField
     global Choice2Outline #MovieClip
     global Option4 #TextField
     global Side3 #TextField
     global scrollBar1 #UIScrollBar
     global Amount2 #TextField
     global Amount12 #TextField
     global AmountOutline1 #MovieClip
     global AmountOutline10 #MovieClip
     global Choice4 #TextField
     global Choice10 #TextField
     global Choice1Outline #MovieClip
     global Option5 #TextField
     global Side4 #TextField
     global scrollBar2 #UIScrollBar
     global strDown #downArrow
     global DayPane #TextField
     global Amount3 #TextField
     global AmountOutline11 #MovieClip
     global Choice5 #TextField
     global Choice11 #TextField
     global Option6 #TextField
     global Option4Outline #MovieClip
     global Side5 #TextField
     global Amount4 #TextField
     global AmountOutline12 #MovieClip
     global Choice12 #TextField
     global Choice6 #TextField
     global Choice7Outline #MovieClip
     global newGame #TextField
     global newGameOutline #MovieClip
     global Option7 #TextField
     global Option5Outline #MovieClip
     global Side6 #TextField
     global Side3Outline #MovieClip
     global senUp #upArrow
     global currentRegion #TextField
     global Amount5 #TextField
     global Choice7 #TextField
     global Choice6Outline #MovieClip
     global Option6Outline #MovieClip
     global Side7 #TextField
     global Side2Outline #MovieClip
     global statPane #TextField
     global Amount6 #TextField
     global Choice8 #TextField
     global Choice5Outline #MovieClip
     global loadGameOutline #MovieClip
     global Option7Outline #MovieClip
     global Side8 #TextField
     global Side1Outline #MovieClip
     global Amount7 #TextField
     global Choice9 #TextField
     global Choice4Outline #MovieClip
     global saveGameOutline #MovieClip
     global senDown #downArrow
     global Amount8 #TextField
     global loadGame #TextField
     global appearanceBox #MovieClip
     global Option1Outline #MovieClip
     global Side7Outline #MovieClip
     global region #TextField
     global moveItemAmount #TextField
     global Amount9 #TextField
     global Option2Outline #MovieClip
     global Side6Outline #MovieClip
     global lustUp #upArrow
     global levelPane #TextField
     global Option3Outline #MovieClip
     global Side5Outline #MovieClip
     global AmountOutline9 #MovieClip
     global Choice9Outline #MovieClip
     global pageNum #TextField
     global Side4Outline #MovieClip
     global hpUp #upArrow
     global libUp #upArrow
     global mentaUp #upArrow
     global AmountOutline8 #MovieClip
     global moveItem #TextField
     global Choice8Outline #MovieClip
     global AmountOutline7 #MovieClip
     global Choice12Outline #MovieClip
     global outputWindow #TextField
     global AmountOutline6 #MovieClip
     global Choice11Outline #MovieClip
     global sideWindow #TextField
     global hpDown #downArrow
     global libDown #downArrow
     global AmountOutline5 #MovieClip
     global MoveOutline #MovieClip
     global Choice10Outline #MovieClip
     global Option1 #TextField
     global AmountOutline4 #MovieClip
     global Choice1 #TextField
     global appearanceText #TextField
     global Option2 #TextField
     global Side1 #TextField
     global Side8Outline #MovieClip
     global strUp #upArrow
     global mentaDown #downArrow
     global Amount10 #TextField
     global MoveAmountOutline #MovieClip
     global AmountOutline3 #MovieClip
     global Choice2 #TextField
     global Choice3Outline #MovieClip
     global saveGame #TextField
     global doListen #Function
     global versionNumber #str
     global theme #int
     global fontSize #int
     global fontBold #bool
     global fontColor #str
     global showSide #bool
     global i #int
     global buttonChoice #int
     global currentText #str
     global sideText #str
     global sideFocus #int
     global pregTempInt #int
     global pregTempBool #bool
     global lustArray #Array
     global loadFile #FileReference
     global fileLoader #URLLoader
     global bg #Sprite
     global rndResult #int
     global rndArray #Array
     global textCheckArray #Array
     global choiceListArray #Array
     global choiceListResult #Array
     global choicePage #int
     global moveItemID #int
     global moveItemStack #int
     global skipExhaustion #bool
     global shiftHeld #bool
     global currentState #int
     global inBag #bool
     global inShop #bool
     global currentZone #int
     global day #int
     global hour #int
     global inDungeon #bool
     global currentDungeon #int
     global _str_ #int
     global ment #int
     global lib #int
     global sen #int
     global HP #int
     global lust #int
     global coin #int
     global strMod #int
     global mentMod #int
     global libMod #int
     global senMod #int
     global strength #int
     global mentality #int
     global libido #int
     global sensitivity #int
     global hunger #int
     global hrs #int
     global itemGainArray #Array
     global human #int
     global horse #int
     global wolf #int
     global cat #int
     global cow #int
     global lizard #int
     global rabbit #int
     global mouse #int
     global bird #int
     global pig #int
     global skunk #int
     global bug #int
     global SexP #int
     global levelUP #int
     global level #int
     global runMod #int
     global rapeMod #int
     global cumMod #Number
     global cockSizeMod #Number
     global vagSizeMod #Number
     global vagElastic #Number
     global milkMod #int
     global carryMod #int
     global vagBellyMod #int
     global pregChanceMod #int
     global extraPregChance #int
     global pregTimeMod #int
     global enticeMod #int
     global milkHPMod #int
     global changeMod #Number
     global HPMod #int
     global SexPMod #Number
     global minLust #int
     global milkCap #int
     global coinMod #int
     global hipMod #int
     global buttMod #int
     global bellyMod #int
     global cockMoistMod #int
     global vagMoistMod #int
     global lockTail #int
     global lockFace #int
     global lockSkin #int
     global lockBreasts #int
     global lockEars #int
     global lockLegs #int
     global lockNipples #int
     global lockCock #int
     global enemyID #int
     global eHP #int
     global eMaxHP #int
     global eStr #int
     global eMenta #int
     global eSen #int
     global eLib #int
     global eLust #int
     global eGen #int
     global ePref #int
     global eCoin #int
     global eSexP #int
     global eItem #int
     global gender #int
     global race #int
     global body #int
     global dominant #int
     global hips #int
     global butt #int
     global tallness #int
     global skinType #int
     global tail #int
     global ears #int
     global hair #int
     global hairLength #int
     global hairColor #int
     global legType #int
     global wings #int
     global faceType #int
     global skinColor #int
     global cockTotal #int
     global humanCocks #int
     global horseCocks #int
     global wolfCocks #int
     global catCocks #int
     global lizardCocks #int
     global rabbitCocks #int
     global cockSize #int
     global cockMoist #int
     global balls #int
     global ballSize #int
     global showBalls #bool
     global knot #bool
     global bugCocks #int
     global breastSize #int
     global boobTotal #int
     global nippleSize #int
     global udders #bool
     global udderSize #int
     global teatSize #int
     global clitSize #int
     global vagTotal #int
     global vagSize #int
     global vagMoist #int
     global vulvaSize #int
     global nipType #int
     global attireTop #int
     global attireBot #int
     global weapon #Number
     global pregArray #Array
     global pregStatus #int
     global pregnancyTime #int
     global pregRate #Number
     global eggLaying #int
     global eggMaxTime #int
     global eggTime #int
     global eggRate #int
     global exhaustion #int
     global exhaustionPenalty #int
     global milkEngorgement #int
     global milkEngorgementLevel #int
     global udderEngorgement #int
     global udderEngorgementLevel #int
     global heat #int
     global heatTime #int
     global heatMaxTime #int
     global lactation #int
     global udderLactation #int
     global nipplePlay #Number
     global udderPlay #Number
     global blueBalls #int
     global teatPump #int
     global nipPump #int
     global cockPump #int
     global clitPump #int
     global vulvaPump #int
     global masoPot #int
     global sMasoPot #int
     global babyFree #int
     global charmTime #int
     global pheromone #int
     global eggceleratorTime #int
     global eggceleratorDose #int
     global bodyOil #int
     global lustPenalty #int
     global snuggleBall #bool
     global fertileGel #int
     global eggType #int
     global milkSuppressant #int
     global milkSuppressantLact #int
     global milkSuppressantUdder #int
     global suppHarness #bool
     global fertilityStatueCurse #int
     global plumpQuats #int
     global lilaWetStatus #int
     global cockSnakePreg #int
     global milkCPoisonNip #int
     global milkCPoisonUdd #int
     global cockSnakeVenom #int
     global humanAffinity #int
     global horseAffinity #int
     global wolfAffinity #int
     global catAffinity #int
     global cowAffinity #int
     global lizardAffinity #int
     global rabbitAffinity #int
     global fourBoobAffinity #int
     global mouseAffinity #int
     global birdAffinity #int
     global pigAffinity #int
     global twoBoobAffinity #int
     global sixBoobAffinity #int
     global eightBoobAffinity #int
     global tenBoobAffinity #int
     global cowTaurAffinity #int
     global humanTaurAffinity #int
     global skunkAffinity #int
     global bugAffinity #int
     global lilaRep #int
     global lilaVulva #int
     global lilaMilk #int
     global lilaPreg #int
     global malonRep #int
     global malonPreg #int
     global malonChildren #int
     global mistressRep #int
     global jamieRep #int
     global jamieSize #int
     global jamieChildren #int
     global silRep #int
     global silPreg #int
     global silRate #int
     global silLay #int
     global silTied #bool
     global silGrowthTime #int
     global lilaUB #bool
     global dairyFarmBrand #bool
     global jamieRep1 #int
     global jamieRep2 #int
     global jamieRep3 #int
     global lilaWetness #int
     global jamieButt #bool
     global jamieBreasts #bool
     global jamieHair #bool
     global travArray #Array
     global foundSoftlik #bool
     global foundFirmshaft #bool
     global foundTieden #bool
     global foundSizCalit #bool
     global foundOviasis #bool
     global foundValley #bool
     global foundSanctuary #bool
     global defeatedMinotaur #bool
     global defeatedFreakyGirl #bool
     global defeatedSuccubus #bool
     global firstExplore #bool
     global knowLustDraft #bool
     global knowRejuvPot #bool
     global knowExpPreg #bool
     global knowBallSwell #bool
     global knowMaleEnhance #bool
     global knowSLustDraft #bool
     global knowSRejuvPot #bool
     global knowSExpPreg #bool
     global knowSBallSwell #bool
     global knowBabyFree #bool
     global knowPotPot #bool
     global knowGenSwap #bool
     global knowMasoPot #bool
     global knowMilkSuppress #bool
     global knowSGenSwap #bool
     global knowSMasoPot #bool
     global knowSBabyFree #bool
     global knowSPotPot #bool
     global knowPussJuice #bool
     global knowPheromone #bool
     global knowBazoomba #bool
     global babyFactLevel #int
     global bodyBuildLevel #int
     global hyperHappyLevel #int
     global alchemistLevel #int
     global fetishMasterLevel #int
     global milkMaidLevel #int
     global shapeshiftyLevel #int
     global shapeshiftyFirst #str
     global shapeshiftySecond #str
     global maleFetish #Number
     global femaleFetish #Number
     global hermFetish #Number
     global narcissistFetish #Number
     global dependentFetish #Number
     global dominantFetish #Number
     global submissiveFetish #Number
     global lboobFetish #Number
     global sboobFetish #Number
     global furryFetish #Number
     global scalyFetish #Number
     global smoothyFetish #Number
     global pregnancyFetish #Number
     global bestialityFetish #Number
     global milkFetish #Number
     global sizeFetish #Number
     global unbirthingFetish #Number
     global ovipositionFetish #Number
     global toyFetish #Number
     global hyperFetish #Number
     global currentDayCare #int
     global humanChildren #int
     global equanChildren #int
     global lupanChildren #int
     global felinChildren #int
     global cowChildren #int
     global lizanEggs #int
     global lizanChildren #int
     global bunnionChildren #int
     global wolfPupChildren #int
     global miceChildren #int
     global birdEggs #int
     global birdChildren #int
     global pigChildren #int
     global calfChildren #int
     global bugEggs #int
     global bugChildren #int
     global skunkChildren #int
     global minotaurChildren #int
     global freakyGirlChildren #int
     global bagPage #int
     global bagArray #Array
     global bagStackArray #Array
     global stashArray #Array
     global stashStackArray #Array

#def MainTimeline():
#     super()
#     addFrameScript(0,this.frame1)
#     __setProp_scrollBar2_Scene1_TextFields_0()
#     __setProp_scrollBar1_Scene1_TextFields_0()

def ButtonEvent1():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(1)
     else:
          buttonChoice = 1
          HideUpDown()
          DoListen()

def ButtonEvent2():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(2)
     else:
          buttonChoice = 2
          HideUpDown()
          DoListen()

def ButtonEvent3():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(3)
     else:
          buttonChoice = 3
          HideUpDown()
          DoListen()

def ButtonEvent4():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          break
     else:
          buttonChoice = 4
          HideUpDown()
          DoListen()

def ButtonEvent5():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(5)
     else:
          buttonChoice = 5
          HideUpDown()
          DoListen()

def ButtonEvent6():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(6)
     else:
          buttonChoice = 6
          HideUpDown()
          DoListen()

def ButtonEvent7():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(7)
     else:
          buttonChoice = 7
          HideUpDown()
          DoListen()

def ButtonEvent8():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          break
     else:
          buttonChoice = 8
          HideUpDown()
          DoListen()

def ButtonEvent9():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(9)
     else:
          buttonChoice = 9
          HideUpDown()
          DoListen()

def ButtonEvent10():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(10)
     else:
          buttonChoice = 10
          HideUpDown()
          DoListen()

def ButtonEvent11():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          ItemMove(11)
     else:
          buttonChoice = 11
          HideUpDown()
          DoListen()

def ButtonEvent12():
     global shiftHeld
     global inBag
     global buttonChoice
     if (shiftHeld == true) and (inBag == true):
          break
     else:
          buttonChoice = 12
          HideUpDown()
          DoListen()

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

def SideEvent(a):
     global sideFocus
     sideFocus = a
     if a == 1:
          AppearanceGo()
     if a == 2:
          DetailedStats()
     if a == 3:
          DetailedStatuses()
     if a == 4:
          DetailedHelp()
     if a == 5:
          DetailedLevels()
     if a == 6:
          DetailedGear()
     if a == 7:
          DetailedTitles()
     if a == 8:
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

def KeysUp():
"""
def HotKeys():
     if shiftHeld == False
          if((e.keyCode == 103 || e.keyCode == 81) && this.Choice1.visible == true)
               this.buttonChoice = 1;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 104 || e.keyCode == 87) && this.Choice2.visible == true)
               this.buttonChoice = 2;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 105 || e.keyCode == 69) && this.Choice3.visible == true)
               this.buttonChoice = 3;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 109 || e.keyCode == 82) && this.Choice4.visible == true)
               this.buttonChoice = 4;
               this.hideUpDown();
               this.doListen();
            if((e.keyCode == 100 || e.keyCode == 65) && this.Choice5.visible == true)
            {
               this.buttonChoice = 5;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 101 || e.keyCode == 83) && this.Choice6.visible == true)
            {
               this.buttonChoice = 6;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 102 || e.keyCode == 68) && this.Choice7.visible == true)
            {
               this.buttonChoice = 7;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 107 || e.keyCode == 70) && this.Choice8.visible == true)
            {
               this.buttonChoice = 8;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 97 || e.keyCode == 90) && this.Choice9.visible == true)
            {
               this.buttonChoice = 9;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 98 || e.keyCode == 88) && this.Choice10.visible == true)
            {
               this.buttonChoice = 10;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 99 || e.keyCode == 67) && this.Choice11.visible == true)
            {
               this.buttonChoice = 11;
               this.hideUpDown();
               this.doListen();
            }
            if((e.keyCode == 13 || e.keyCode == 86) && this.Choice12.visible == true)
            {
               this.buttonChoice = 12;
               this.hideUpDown();
               this.doListen();
            }
         }
         if(e.keyCode == 85 && this.showSide == true)
         {
            this.sideEvent(1);
         }
         else if(e.keyCode == 85 && this.showSide == false && this.appearanceText.visible == true)
         {
            this.appearanceGo();
         }
         if(e.keyCode == 73 && this.showSide == true)
         {
            this.sideEvent(2);
         }
         if(e.keyCode == 79 && this.showSide == true)
         {
            this.sideEvent(3);
         }
         if(e.keyCode == 80 && this.showSide == true)
         {
            this.sideEvent(4);
         }
         if(e.keyCode == 72 && this.showSide == true)
         {
            this.sideEvent(5);
         }
         if(e.keyCode == 74 && this.showSide == true)
         {
            this.sideEvent(6);
         }
         if(e.keyCode == 75 && this.showSide == true)
         {
            this.sideEvent(7);
         }
         if(e.keyCode == 76 && this.showSide == true)
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
         if(e.keyCode == 190 && this.Option7.visible == true)
         {
            this.toggleSide();
         }
         if(e.keyCode == 191)
         {
            this.toggleBold();
         }
         if(e.keyCode == 113 && this.saveGame.visible == true)
         {
            this.saveGo();
         }
         if(e.keyCode == 115 && this.loadGame.visible == true)
         {
            this.loadGo();
         }
         if(e.keyCode == 8 && this.newGame.visible == true)
         {
            this.newGameGo();
         }
         if(e.shiftKey)
         {
            this.shiftHeld = true;
         }
         if(this.inBag == true)
         {
            if(this.shiftHeld)
            {
               if((e.keyCode == 103 || e.keyCode == 81) && this.Choice1.visible == true)
               {
                  this.itemMove(1);
               }
               if((e.keyCode == 104 || e.keyCode == 87) && this.Choice2.visible == true)
               {
                  this.itemMove(2);
               }
               if((e.keyCode == 105 || e.keyCode == 69) && this.Choice3.visible == true)
               {
                  this.itemMove(3);
               }
               if((e.keyCode == 100 || e.keyCode == 65) && this.Choice5.visible == true)
               {
                  this.itemMove(5);
               }
               if((e.keyCode == 101 || e.keyCode == 83) && this.Choice6.visible == true)
               {
                  this.itemMove(6);
               }
               if((e.keyCode == 102 || e.keyCode == 68) && this.Choice7.visible == true)
               {
                  this.itemMove(7);
               }
               if((e.keyCode == 97 || e.keyCode == 90) && this.Choice9.visible == true)
               {
                  this.itemMove(9);
               }
               if((e.keyCode == 98 || e.keyCode == 88) && this.Choice10.visible == true)
               {
                  this.itemMove(10);
               }
               if((e.keyCode == 99 || e.keyCode == 67) && this.Choice11.visible == true)
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
     if theme == 6:
          theme = 0
     UpdateTheme()
     SavePreferences()
"""
def ChangeBGColor():
     bg.graphics.beginFill(color)
     bg.graphics.drawRect(0,0,stage.stageWidth,stage.stageHeight)
     bg.graphics.endFill()
"""
def UpdateTheme():
     global theme
     if theme == 0:
          ChangeBGColor(16777215)
     elif theme == 1:
          ChangeBGColor(0)
     elif theme == 2:
          ChangeBGColor(15695286)
     elif theme == 3:
          ChangeBGColor(2715740)
     elif theme == 4:
          ChangeBGColor(4343974)
     elif theme == 5:
          ChangeBGColor(7477015)
     else:
          ChangeBGColor(16777215)
          theme = 0

def FontSizeDown():
     global fontSize
     if fontSize > 4:
          fontSize -= 2
     UpdateText()
     SavePreferences()

def FontSizeReset():
     global fontSize
     fontSize = 14
     UpdateText()
     SavePreferences()

def FontSizeUp():
     global fontSize
     if fontSize < 26:
          fontSize += 2
     UpdateText()
     SavePreferences()

def ToggleBold():
     global fontBold
     if fontBold == False:
          fontBold = True
     else:
          fontBold = False
     UpdateText()
     SavePreferences()

def ToggleColor():
     global fontColor
     if fontColor == "000000":
          fontColor = "FFFFFF"
     elif fontColor == "FFFFFF":
          fontColor = "808080"
     elif fontColor == "808080":
          fontColor = "0000FF"
     elif fontColor == "0000FF":
          fontColor = "800080"
     elif fontColor == "800080":
          fontColor = "FF0000"
     elif fontColor == "FF0000":
          fontColor = "FFA500"
     elif fontColor == "FFA500":
          fontColor = "FFFF00"
     elif fontColor == "FFFF00":
          fontColor = "008000"
     elif fontColor == "008000":
          fontColor = "EF7DB6"
     elif fontColor == "EF7DB6":
          fontColor = "29705C"
     elif fontColor == "29705C":
          fontColor = "000000"
     else:
          fontColor = "FFFFFF"     
     UpdateText()
     SavePreferences()

def ToggleSide():
     global showSide
     if showSide == True:
          showSide = False
          SideHide()
          Option7.htmlText = "--"
     else:
          showSide = True
          SideShow()
          UpdateSide()
          Option7.htmlText = "O"
     if Option7Visible == True:
          SavePreferences()
"""
def SideHide():
     this.sideWindow.visible = false;
         this.scrollBar2.visible = false;
         this.Side1.visible = false;
         this.Side1Outline.visible = false;
         this.Side2.visible = false;
         this.Side2Outline.visible = false;
         this.Side3.visible = false;
         this.Side3Outline.visible = false;
         this.Side4.visible = false;
         this.Side4Outline.visible = false;
         this.Side5.visible = false;
         this.Side5Outline.visible = false;
         this.Side6.visible = false;
         this.Side6Outline.visible = false;
         this.Side7.visible = false;
         this.Side7Outline.visible = false;
         this.Side8.visible = false;
         this.Side8Outline.visible = false;
         if(this.saveGame.visible == true)
         {
            this.appearanceText.visible = true;
            this.appearanceBox.visible = true;
         }
def SideShow():
     this.sideWindow.visible = true;
         this.scrollBar2.visible = true;
         this.Side1.visible = true;
         this.Side1Outline.visible = true;
         this.Side2.visible = true;
         this.Side2Outline.visible = true;
         this.Side3.visible = true;
         this.Side3Outline.visible = true;
         this.Side4.visible = true;
         this.Side4Outline.visible = true;
         this.Side5.visible = true;
         this.Side5Outline.visible = true;
         this.Side6.visible = true;
         this.Side6Outline.visible = true;
         this.Side7.visible = true;
         this.Side7Outline.visible = true;
         this.Side8.visible = true;
         this.Side8Outline.visible = true;
         this.appearanceText.visible = false;
         this.appearanceBox.visible = false;
         this.updateSide();
"""
"""
def SavePreferences():
def LoadPreferences():
"""
def UpdateText():
def OutputMainText():
def OutputSideText():
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
     this.strUp.visible = false;
         this.strDown.visible = false;
         this.mentaUp.visible = false;
         this.mentaDown.visible = false;
         this.libUp.visible = false;
         this.libDown.visible = false;
         this.senDown.visible = false;
         this.senUp.visible = false;
         this.lustUp.visible = false;
         this.lustDown.visible = false;
         this.hpUp.visible = false;
         this.hpDown.visible = false;
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
def ViewButtonText():
def ViewButtonOutline():
def AmountWrite():
def ViewAmount():
def HideAmount():
def ChoiceListButtons():
def ChoiceListBlanks():
def ChoiceListSelect():
def ChoiceListCheck():
def ShowPage():
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
     if pregArray.length < vagTotal * 5:
          while pregArray.length < vagTotal * 5:
               pregArray.push(false,0,0,0,0)

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
     ViewButtonText(0,0,0,0,0,1,1,0,0,0,0,0)
     ViewButtonOutline(0,0,0,0,0,1,1,0,0,0,0,0)
     ButtonWrite(6,"Yes")
     ButtonWrite(7,"No")

def DoNext():
     BC()
     ViewButtonOutline(0,0,0,0,0,1,0,0,0,0,0,0)
     ViewButtonText(0,0,0,0,0,1,0,0,0,0,0,0)
     ButtonWrite(6,"Next")

def DoEnd():
     global choicePage, inBag, lust, currentState, buttonChoice
     choicePage = 1
     ShowPage(false,"")
     StatDisplay()
     if inBag == True and lust > 99 and currentState == 2:
          inBag = False
          HideAmount()
          DoLustForcedMasturbate()
     else:
          DoNext()
          if buttonChoice == 6:
               DoProcess()

def DoProcess():
     global choicePage, moveItemID, moveItemStack, itemGainArray,human, horse, wolf, cat, cow, hrs
     choicePage = 1
     if inBag == False and moveItemID != 0:
          OutputMainText("You seem to have not placed your " + ItemName(moveItemID) + "",true)
          if moveItemStack > 1:
               OutputMainText(" x" + moveItemStack,false)
          OutputMainText(" in your bag. Do you want to discard the item?",false)
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
          if itemGainArray.length != 0:
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
          ShowPage(false,"")
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

def EVagLimit(limit:int):
     a = limit + limit * MoistCalc(1) / 10
     return a

def DecGet(number, places:int):
     tempStr = str(number)
     tempStr2 = ""
     tempInt = 0
     tempInt = tempStr.index(".", 0)
     if tempInt > 0:
          tempStr2 = tempStr[0: tempInt + places + 1]
     else:
          tempStr2 = tempStr
     return tempStr2

def DoWeight():
     tempBool:Boolean = false
     if ((cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60))):
          OutputMainText("\n" + "\n" + "The weight of your " + CockDesc() + " cock" + Plural(1) + " is too much to carry, making it impossible to walk. You're stuck in this town until either you get stronger or the bulge in your " + clothesBottom() + " gets smaller...",false)
          tempBool = true
     elif (cockSize * cockSizeMod > (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6):
          OutputMainText("\n" + "\n" + "The weight of your " + cockDesc() + " cock" + Plural(1) + " is almost constantly on your mind... Your walk has a noticeable sway in its step just trying to hold it off the ground while you move. You're cautious when moving, or else you will lose control and slam it into something or someone.",false)
     elif (cockSize * cockSizeMod > (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3):
          OutputMainText("\n" + "\n" + "The weight of your " + cockDesc() + " cock" + Plural(1) + " is becoming a bit of a nuisance. Whenever you move around, you're subconsciously afraid your bulge will accidentally gain more momentum than intended and potentially hurt someone or break something.",false)
     elif (cockSize * cockSizeMod) > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2):
          OutputMainText("\n" + "\n" + "You are rather aware of the weight of your " + cockDesc() + " cock" + Plural(1) + ". You often find yourself slipping a hand into your " + clothesBottom() + " to readjust your bulge in an attempt to be a little less mindful about it.",false):
     if (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60)) or ((boobTotal == 4) and ((breastSize) > (0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60)))) or ((boobTotal == 6) and (breastSize > 0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60))) or ((boobTotal == 8) and (breastSize > 0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60))) or ((boobTotal == 10) and (breastSize > 0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60)))):
          OutputMainText("\n" + "\n" + "The weight of your " + boobDesc() + " tits is too much to really carry, making even standing a chore. You're stuck in this town until either you get stronger or they get smaller...",false)
          tempBool = true
     elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6) or ((boobTotal == 4) and (breastSize > 0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6)) or ((boobTotal == 6) and (breastSize > 0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6)) or ((boobTotal == 8) and (breastSize > 0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6)) or ((boobTotal == 10) and (breastSize > 0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 5 / 6))):
          OutputMainText("\n" + "\n" + "The weight of your " + boobDesc() + " tits is rather troubling. Not only does your back ache from trying to keep them aloft, but you're also afraid you won't be able to get back up when you lay down.",false)
     elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3) or ((boobTotal == 4) and (breastSize > 0.5 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3)) or ((boobTotal == 6) and (breastSize > 0.66 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3)) or ((boobTotal == 8) and (breastSize > 0.33 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3)) or ((boobTotal == 10) and (breastSize > 0.25 * (body * 2 + _str_ + carryMod) * (tallness / 60) * 2 / 3))):
          OutputMainText("\n" + "\n" + "The weight of your " + boobDesc() + " tits is becoming worrisome. Your back aches a little from holding them up and you often find yourself resting them on tables whenever you sit down, to keep the load off yourself.",false)
     elif (breastSize > ((body * 2 + _str_ + carryMod) * (tallness / 60) * 1 / 2)  this.boobTotal == 4 && this.breastSize > 0.5 * (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2 || this.boobTotal == 6 && this.breastSize > 0.66 * (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2 || this.boobTotal == 8 && this.breastSize > 0.33 * (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2 || this.boobTotal == 10 && this.breastSize > 0.25 * (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2)
          OutputMainText("\r\rYou are rather aware of the weight of your " + this.boobDesc() + " tits. Your hands are frequently beneath your " + this.clothesTop() + ", trying to readjust the things. They\'re so heavy, you\'re subconsciouly drawing more attention to them with the way you keep swinging them around and absent-mindedly handling them.",false)
     if(this.ballSize * this.balls / 2 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) && this.showBalls == true)
          OutputMainText("\r\rThe weight of your " + this.ballDesc() + " nuts is too much to carry, anchoring you to the ground. You\'re stuck here until you get strong or your balls get smaller...",false)
          tempBool = true
     elif(this.ballSize * this.balls / 2 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 5 / 6 && this.showBalls == true)
          OutputMainText("\r\rThe weight of your " + this.ballDesc() + " nuts is troublesome. Your " + this.legDesc(6) + " bend" + this.legPlural(1) + " with the heaviness and you have difficulty standing up whenever you sit down. And you\'re afraid of running because once those things start swaying, they\'re quite difficult to stop.",false)
     else if(this.ballSize * this.balls / 2 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 2 / 3 && this.showBalls == true)
          OutputMainText("\r\rThe weight of your " + this.ballDesc() + " nuts is becoming annoying. You\'re walking with your crotch sagging quite often and frequently consider buying a bra for them...",false)
     else if(this.ballSize * this.balls / 2 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2 && this.showBalls == true)
          OutputMainText("\r\rYou are rather aware of the weight of your " + this.ballDesc() + " nuts. Even in public, a hand is dipping into your " + this.clothesBottom() + " to readjust them and massaging your stretched scrotum is quickly becoming a hobby of yours.",false)
     if(this.udderSize > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) && this.udders == true)
          OutputMainText("\r\rThe weight of your " + this.udderDesc() + " udder is too much to carry, sitting heavily in front of you. You\'re stuck in this town until either you get stronger or it gets smaller...",false)
          tempBool = true
     else if(this.udderSize > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 5 / 6 && this.udders == true)
          OutputMainText("\r\rThe weight of your " + this.udderDesc() + " udder makes you uneasy. The momentum it gains when you walk makes you fear falling on your face and every now and then your " + this.legDesc(2) + " go numb while you\'re sitting or laying down.",false)
     else if(this.udderSize > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 2 / 3 && this.udders == true)
          OutputMainText("\r\rThe weight of your " + this.udderDesc() + " udder is becoming an inconvenience. Whenever you turn from side to side, it lifts off slightly and acts like a fleshy wrecking ball that you\'re unable to stop.",false)
     else if(this.udderSize > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2 && this.udders == true)
          OoutputMainText("\r\rYou are rather aware of the weight of your " + this.udderDesc() + " udder. You often find yourself fondling it in an attempt to make it settle more appropriately, wondering if they make bras for this sort of thing...",false)
     if((this.pregnancyTime + this.bellyMod * 2) / 5 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60))
          OutputMainText("\r\rThe weight of your " + this.bellyDesc() + " belly is too much carry, putting your weight more on it than you can yourself. You\'re stuck in this town until either you get stronger or you lose some of the girth...",false)
          tempBool = true
     else if((this.pregnancyTime + this.bellyMod * 2) / 5 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 5 / 6)
          OutputMainText("\r\rThe weight of your " + this.bellyDesc() + " belly is rather alarming... You\'re almost constantly trying to cradle it, subconsciously fearing it will drag you down to the ground if you don\'t. Whenever you sit down, you always prop it up against a table simply so you don\'t roll forward.",false)
     else if((this.pregnancyTime + this.bellyMod * 2) / 5 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 2 / 3)
          OutputMainText("\r\rThe weight of your " + this.bellyDesc() + " belly is becoming irksome. You take a bit more time to come to a halt whenever you move as it retains much of your momentum. And whenever you bend over, it\'s difficult to rise back up.",false)
     else if((this.pregnancyTime + this.bellyMod * 2) / 5 > (this.body * 2 + this.str + this.carryMod) * (this.tallness / 60) * 1 / 2)
          OutputMainText("\r\rYou are rather aware of the weight of your " + this.bellyDesc() + " belly. You often subconsciously center your weight more by resting your hands on top of it rather than let them hang at your sides.",false)
     return tempBool

def CheckItem():
def CheckMagicItem():
     tempBool:bool = false
     if checkItem(101):
          tempBool = true
     elif checkItem(102):
          tempBool = true
     elif checkItem(200):
          tempBool = true
     elif checkItem(215):
          tempBool = true
     elif checkItem(231):
          tempBool = true
     elif checkItem(233):
          tempBool = true
     elif checkItem(234):
          tempBool = true
     elif checkItem(235):
          tempBool = true
     elif checkItem(236):
          tempBool = true
     elif checkItem(237):
          tempBool = true
     elif checkItem(252)
          tempBool = true
     return tempBool

def CheckStash():
def CountItem():
def Percent():
     a = math.floor(random.random() * (1 + 100 - 1)) + 1
     return a

def ChooseFrom():
     global rndArray
     global hour
     tempInt:int = 0
     rndResult = 0
     if rndArray.length < 1:
          outputMainText("\n" + "\n" + "An ERROR has occured in the choice array. Please report this bug and where you saw it (" + rndArray[0] + " at " + hour + "hour), or else you'll get the hose.",false)
          rndArray = list(())
     else:
          tempInt = round(random.random() * (rndArray.length - 1))
          rndResult = rndArray[tempInt]
          rndArray = list(())
     return rndResult

def Stats():
def StatsMod():
def StatsDisplay():
def DoSexP():
     global SexP, SexPMod, level, levelUP, coin
     if (SexP + changes * SexPMod) >= 100:
          changes -= math.ceil((100 - SexP) / SexPMod)
          SexP = 0
          level += 1
          levelUP += 1
          doSexP(changes)
     else:
          SexP += changes * SexPMod
          levelPane.text = "Level  : " + level + "\rSexP   : " + SexP + "\rCoin   : " + coin
          levelPane.textColor = uint("0x" + fontColor)

def RegionChange(changes:int):
     if inDungeon == False:
          currentZone = changes
          if changes == 1:
               region.text = "Softlik"
          if changes == 2:
               region.text = "Firmshaft"
          if changes == 3:
               region.text = "Tieden"
          if changes == 4:
               region.text = "Siz'Calit"
          if changes == 6:
               region.text = "Oviasis"
          if changes == 12:
               region.text = "Sanctuary"
     if inDungeon == True:
          currentDungeon = changes
          if (changes > 1000) and (changes < 1010):
               region.text = "Cave Descent"
     region.textColor = uint("0x" + fontColor)

def DayTime(Time):
     global hour, day
     addTime:int = Time
     while hour + addTime >= 24:
          addTime -= 24 - hour
          hour = 0
          day += 1
     hour += addTime
     DayPane.text = "Day : " + int(day) + "\n" + "Hour: " + int(hour) + ":00"
     DayPane.textColor = uint("0x" + fontColor)
     DoStatus(Time)

def DoCoin(changes:int):
     global coin, coinMod
     if coin + changes < 0:
          coin = 0
          changes = 0
     if changes > 0:
          changes += coinMod
     coin += changes
     DoSexP(0)

def DoHP(changes:int):
     global masoPot, sMasoPot, lust, HP, _str_, HPMod
     if (masoPot > 0) and (sMasoPot <= 0) and (changes < 0):
          doLust(math.floor(-changes / 2),0)
          changes -= math.ceil(changes / 2)
     if (sMasoPot > 0) and (lust < 100) and (changes < 0):
          doLust(-changes,0)
          changes = 0
     if (sMasoPot > 0) and (lust >= 100) and (changes < 0):
          outputMainText("\n" + "\n" + "It seems that no matter how much fun you had getting beaten like that, there's just some things your body wasn't meant to withstand.",false)
     if changes < 0:
          hpDown.visible = true
     if changes > 0:
          hpUp.visible = true
     if (HP + changes) <= 0:
          HP = 1
          changes = 0
          doPassOut()
     if (HP + changes) > (30 + math.floor(_str_ / 2) + HPMod):
          HP = 30 + math.floor(_str_ / 2) + HPMod
     else:
          HP += changes
     StatDisplay()

def DoPassOut():
     global level, coin, currentState, inDungeon, exhaustion, skipExhaustion, hrs
     tempNum:int = math.floor(Percent() / 10 * level + level * Percent() / 10)
     if (coin - tempNum) < 0
          tempNum = coin
     SpecialKOLose()
     OutputMainText("\n" + "\n" + "You pass out from all the pain. When you wake back up, you manage to stumble back to town. However, it seems as though your pockets are a bit lighter for some reason or another." + "\n" + "\n" + "You have lost " + tempNum + " coins.",false)
     if currentState == 2:
          currentState = 1
     if inDungeon == True:
          inDungeon = False
     DoCoin(-tempNum)
     exhaustion -= math.floor(Percent() / 20)
     skipExhaustion = True
     hrs = 2 + math.floor(Percent() / 20)
     DoEnd()

def DoLust(changes:int, source:int, ... triggers):
     if(source == 1)
         {
            if(changes > 0)
            {
               changes -= Math.floor(changes * this.ment / 125);
               if(changes < 0)
               {
                  changes = 0;
               }
            }
         }
         if(source == 2)
         {
            if(changes <= 0)
            {
               changes += Math.floor(changes * this.ment / 125);
            }
         }
         if(changes <= 0 && source == 2)
         {
            changes -= 6;
            if(this.fertilityStatueCurse > 0)
            {
               this.outputMainText("\r\rWith your orgasm, you feel strange as wispy fumes escape from your crotch, just like those that descended from the statue you encountered...",false);
               this.vagChange(0,1);
            }
            if(this.cockSnakeVenom > 0 && triggers.indexOf(1) != -1 && this.cockTotal > 0)
            {
               this.outputMainText("\r\rHowever, after you have finished, you realize there\'s a bit more meat to your meat... The venom from the cock-snake fed off of your orgasm, causing your appendage" + this.plural(1) + " to flop a bit lower down your " + this.legDesc(3) + " as " + this.plural(11) + " shrink" + this.plural(3) + " back down...",false);
               this.cockChange(2,0);
            }
            if(this.cockSnakeVenom > 0 && triggers.indexOf(2) != -1 && this.vagTotal > 0)
            {
               this.outputMainText("\r\rHowever, after you have finished, you realize your clit" + this.plural(2) + " " + this.plural(14) + " a bit more prominent... The venom from the cock-snake fed off of your orgasm, causing the button" + this.plural(2) + " swell larger than before, and aren\'t shrinking all the way back down...",false);
               this.clitSize += 3;
            }
            if(this.milkCPoisonNip > 0 && triggers.indexOf(3) != -1)
            {
               this.outputMainText("\r\rHowever, now that you\'ve calmed down, you notice a bit more weight at your chest... The warmth from the milk creeper poison in your bosom intensified with your pleasure, causing your flesh to grow larger while you were distracted by the climax. A hefty reminder.",false);
               this.boobChange(1);
               this.nipplePlay += 15;
            }
            if(this.milkCPoisonUdd > 0 && triggers.indexOf(4) != -1)
            {
               this.outputMainText("\r\rHowever, now that you\'ve calmed down, you notice a bit more weight at your belly... The warmth from the milk creeper poison in your udder intensified with your pleasure, causing your flesh to grow larger while you were distracted by the climax. A hefty reminder.",false);
               this.boobChange(1);
               this.nipplePlay += 15;
            }
            if(this.level < 50)
            {
               if(this.lust + changes >= 0 && -changes > this.level + 6 + this.str / 3)
               {
                  this.doSexP(Math.floor(-changes - (this.level + 6 + this.str / 3)));
               }
               else if(this.lust + changes < 0 && this.lust > this.level + 6 + this.str / 3)
               {
                  this.doSexP(Math.floor(this.lust - (this.level + 6 + this.str / 3)));
               }
            }
            else if(this.lust + changes >= 0 && -changes > 50 + 6 + this.str / 3)
            {
               this.doSexP(Math.floor(-changes - (50 + 6 + this.str / 3)));
            }
            else if(this.lust + changes < 0 && this.lust > 50 + 6 + this.str / 3)
            {
               this.doSexP(Math.floor(this.lust - (50 + 6 + this.str / 3)));
            }
         }
         if(changes < 0)
         {
            this.lustDown.visible = true;
         }
         if(changes > 0)
         {
            this.lustUp.visible = true;
         }
         if(this.lust + changes >= 75 && this.lust < 75)
         {
            if(this.cockTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.cockDesc() + " cock" + this.plural(1) + " squirm" + this.plural(3) + " in your " + this.clothesBottom() + ", throbbing and wanting desperately to come.",false);
               if(this.moistCalc(1) > 0 && this.moistCalc(1) <= 3)
               {
                  this.outputMainText(" A small amount of pre leaks out, making a moist blotch on your " + this.clothesBottom() + ".",false);
               }
               if(this.moistCalc(1) > 3 && this.moistCalc(1) <= 7)
               {
                  this.outputMainText(" Steady drops of pre leak out, blotching your " + this.clothesBottom() + " with small patches of slime.",false);
               }
               if(this.moistCalc(1) > 7 && this.moistCalc(1) <= 11)
               {
                  this.outputMainText(" You feel your cock" + this.plural(1) + " slimed from tip to belly with " + this.plural(5) + " own pre, a steady dribble down your thigh and your " + this.clothesBottom() + " looking more like you peed yourself.",false);
               }
               if(this.moistCalc(1) > 11)
               {
                  this.outputMainText(" You feel your cock" + this.plural(1) + " swimming in " + this.plural(5) + " own pre, as long strands of slime seep through your " + this.clothesBottom() + " and stretch down to the ground. With each step, you fling the stuff around you like a whip, smacking across whatever is nearby",false);
               }
            }
            if(this.vagTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.vulvaDesc() + " lips feel swollen and hot in your " + this.clothesBottom() + ", making your " + this.legDesc(2) + " feel weak. Your " + this.clitDesc() + " clit" + this.plural(2) + " seem" + this.plural(4) + " on the verge of exploding without any attention soon, stiffly rubbing against your " + this.clothesBottom() + " with each move.",false);
               if(this.moistCalc(2) > 0 && this.moistCalc(2) <= 3)
               {
                  this.outputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",false);
               }
               if(this.moistCalc(2) > 3 && this.moistCalc(2) <= 7)
               {
                  this.outputMainText(" You can feel webs of slime smear across the inside of your " + this.clothesBottom() + ", your honey dribbling lightly within.",false);
               }
               if(this.moistCalc(2) > 7 && this.moistCalc(2) <= 11)
               {
                  this.outputMainText(" You swear you can hear yourself squish with each step as your " + this.clothesBottom() + " is completely soaked through with your honey. Your thighs feel like they\'ve been completely oiled down by the warm, sensuous fluid.",false);
               }
               if(this.moistCalc(2) > 11)
               {
                  this.outputMainText(" There must be a waterfall in your " + this.clothesBottom() + " as a steady flow of clear honey drools from " + this.legWhere(1) + " your " + this.legDesc(2) + ". You have to be extra careful of slipping in your own slime...",false);
               }
            }
            this.outputMainText("\r\rYour " + this.nipDesc() + "nipples threaten to pierce through your " + this.clothesTop() + ". They feel as hard as diamonds with all your arousal, making you shiver whenever something brushes them.",false);
         }
         else if(this.lust + changes >= 50 && this.lust < 50)
         {
            if(this.cockTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.cockDesc() + " cock" + this.plural(1) + " feel" + this.plural(3) + " stiff and engorged with blood. Oh how nice it would be to take care of that problem... ",false);
               if(this.moistCalc(1) > 0 && this.moistCalc(1) <= 3)
               {
                  this.outputMainText(" A small amount of pre leaks out, making a moist blotch on your " + this.clothesBottom() + ".",false);
               }
               if(this.moistCalc(1) > 3 && this.moistCalc(1) <= 7)
               {
                  this.outputMainText(" Steady drops of pre leak out, blotching your " + this.clothesBottom() + " with small patches of slime.",false);
               }
               if(this.moistCalc(1) > 7)
               {
                  this.outputMainText(" You feel your cock" + this.plural(1) + " slimed from tip to belly with its own pre, a steady dribble down your thigh and your " + this.clothesBottom() + " looking more like you peed yourself.",false);
               }
            }
            if(this.vagTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.vulvaDesc() + " vulva feels puffy with engorgement, making you walk a little awkwardly so as to not squeeze them so much. Your " + this.clitDesc() + " clit" + this.plural(2) + " stir" + this.plural(4) + " in your " + this.clothesBottom() + ", throbbing gently in anticipation.",false);
               if(this.moistCalc(2) > 0 && this.moistCalc(2) <= 3)
               {
                  this.outputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",false);
               }
               if(this.moistCalc(2) > 3 && this.moistCalc(2) <= 7)
               {
                  this.outputMainText(" You can feel webs of slime smear across the inside of your " + this.clothesBottom() + ", your honey dribbling lightly within.",false);
               }
               if(this.moistCalc(2) > 7)
               {
                  this.outputMainText(" You swear you can hear yourself squish with each step as your " + this.clothesBottom() + " is completely soaked through with your honey. Your thighs feel like they\'ve been completely oiled down by the warm, sensuous fluid.",false);
               }
            }
            if(this.nipType == 2)
            {
               this.outputMainText("\r\rYour sunken nipples rise out of your " + this.boobDesc() + " mounds, standing to attention in your " + this.clothesTop() + ". They tingle slightly with your arousal.",false);
            }
            else
            {
               this.outputMainText("\r\rYour " + this.nipDesc() + "nipples stand at attention in your " + this.clothesTop() + ". They tingle slightly with your arousal.",false);
            }
         }
         else if(this.lust + changes >= 25 && this.lust < 25)
         {
            if(this.cockTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.cockDesc() + " cock" + this.plural(1) + " wiggle" + this.plural(3) + " in your " + this.clothesBottom() + ", stirring awake and growing erect. Bulging against the fabric, you silently wonder if anybody else will notice...",false);
               if(this.moistCalc(1) > 0 && this.moistCalc(1) <= 3)
               {
                  this.outputMainText(" A small amount of pre leaks out, making a moist blotch on your " + this.clothesBottom() + ".",false);
               }
               if(this.moistCalc(1) > 3)
               {
                  this.outputMainText(" Steady drops of pre leak out, blotching your " + this.clothesBottom() + " with small patches of slime.",false);
               }
            }
            if(this.vagTotal > 0)
            {
               this.outputMainText("\r\rYour " + this.vulvaDesc() + " slit tingles and sparks. You feel a little giggly and warm with the sensation, delighting in the pleasantness of it all. Your " + this.clitDesc() + " clit" + this.plural(2) + " tug" + this.plural(4) + " at the hood" + this.plural(4) + ", pulsing awake in your " + this.clothesBottom() + ".",false);
               if(this.moistCalc(2) > 0 && this.moistCalc(2) <= 3)
               {
                  this.outputMainText(" Your pussy lips slip over each other with each step, slightly lubricated with your arousal.",false);
               }
               if(this.moistCalc(2) > 3)
               {
                  this.outputMainText(" You can feel webs of slime smear across the inside of your " + this.clothesBottom() + ", your honey dribbling lightly within.",false);
               }
            }
         }
         if(this.lust + changes >= 30 && this.lustPenalty == 0)
         {
            this.outputMainText("\r\rThe distraction weighs on your mind constantly, making it hard to focus on normal tasks.",false);
            this.statsMod(0,-4,0,0);
            this.lustPenalty = 1;
         }
         if(this.lust + changes >= 60 && this.lustPenalty == 1)
         {
            this.outputMainText("\r\rYour muscles are twitchy and feeling weak from the strong tingle of arousal.",false);
            this.statsMod(-5,0,0,0);
            this.lustPenalty = 2;
         }
         if(this.lust + changes >= 90 && this.lustPenalty == 2)
         {
            this.outputMainText("\r\rThe intense lust has overwhelmed your body, leaving your " + this.skinDesc() + " hypersensitive.",false);
            this.statsMod(0,0,0,10);
            this.lustPenalty = 3;
         }
         if(this.lust + changes >= 100)
         {
            this.lust = 100;
            changes = 0;
            if(this.inBag == false)
            {
               this.doLustForcedMasturbate();
            }
         }
         if(this.lust + changes < this.minLust + 20 && this.heat > 0 && this.heatTime < 0 && !this.pregCheck(0))
         {
            this.lust = this.minLust + 20;
            changes = 0;
         }
         else if(this.lust + changes < this.minLust)
         {
            this.lust = this.minLust;
            changes = 0;
         }
         this.lust += changes;
         this.statDisplay();

def DoLustForcedMasturbate():
     global currentState, ePref, gender
     if currentState == 2:
          OutputMainText("\n" + "\n" + "Amidst the heat of battle, your " + LegDesc(2) + " buckle" + LegPlural(1) + " from your intense arousal, preventing you from fighting any further.",false)
          if inBag == False:
               currentState = 1
          DoNext();
          doListen = function():void
               if ((ePref == 0) or ((ePref == 1) and (gender == 2)) or ((ePref == 2) and (gender == 1)) or (gender == 0)):
                    OutputMainText("Unfortunately, the " + EnemyName() + " has no interest in taking advantage of your state and lands a heavy blow, knocking you out.",true)
                    DoHP(-100000)
               else:
                    DoGetRaped()

def NewGameGo():
     appearanceText.visible = false;
     appearanceBox.visible = false;
     saveGame.visible = false;
     saveGameOutline.visible = false;
     buttonConfirm();
     outputMainText("Are you sure you would like to start a new game?",true);
     if currentState == 0:
          this.Choice7.visible = false
     doListen = function():void
          if(buttonChoice == 6)
               hideUpDown()
               statPane.visible = true;
               DayPane.visible = true;
               levelPane.visible = true;
               Option7.visible = false;
               sideHide();
               currentState = 0;
               currentZone = 0;
               inBag = false;
               inShop = false;
               inDungeon = false;
               currentDungeon = 0;
               str = 0;
               ment = 0;
               lib = 0;
               sen = 0;
               HP = 0;
               lust = 0;
               coin = 0;
               strMod = 0;
               mentMod = 0;
               libMod = 0;
               senMod = 0;
               hunger = 0;
               day = 0;
               hour = 8;
               SexP = 0;
               levelUP = 0;
               level = 0;
               runMod = 0;
               rapeMod = 0;
               cumMod = 1;
               cockSizeMod = 1;
               vagSizeMod = 1;
               vagElastic = 1;
               milkMod = 0;
               carryMod = 0;
               vagBellyMod = 0;
               pregChanceMod = 0;
               extraPregChance = 0;
               pregTimeMod = 0;
               enticeMod = 0;
               milkHPMod = 0;
               changeMod = 1;
               HPMod = 0;
               SexPMod = 1;
               minLust = 0;
               milkCap = 0;
               coinMod = 0;
               hipMod = 1;
               buttMod = 1;
               bellyMod = 0;
               cockMoistMod = 0;
               vagMoistMod = 0;
               lockTail = 0;
               lockFace = 0;
               lockSkin = 0;
               lockBreasts = 0;
               lockEars = 0;
               lockLegs = 0;
               lockNipples = 0;
               lockCock = 0;
               gender = 0;
               race = 0;
               body = 0;
               dominant = 0;
               hips = 0;
               butt = 0;
               tallness = 0;
               skinType = 0;
               tail = 0;
               ears = 0;
               hair = 0;
               hairLength = 0;
               hairColor = 0;
               legType = 0;
               wings = 0;
               faceType = 0;
               skinColor = 0;
               cockTotal = 0;
               humanCocks = 0;
               horseCocks = 0;
               wolfCocks = 0;
               catCocks = 0;
               lizardCocks = 0;
               rabbitCocks = 0;
               cockSize = 0;
               cockMoist = 0;
               balls = 0;
               ballSize = 0;
               showBalls = true;
               knot = false;
               bugCocks = 0;
               breastSize = 0;
               boobTotal = 0;
               nippleSize = 1;
               udders = false;
               udderSize = 0;
               teatSize = 0;
               clitSize = 0;
               vagTotal = 0;
               vagSize = 0;
               vagMoist = 0;
               vulvaSize = 0;
               nipType = 0;
               attireTop = 1;
               attireBot = 2;
               weapon = 10;
               pregArray = [];
               pregStatus = 0;
               pregnancyTime = 0;
               pregRate = 1;
               eggLaying = 0;
               eggMaxTime = 0;
               eggTime = 0;
               eggRate = 0;
               exhaustion = 0;
               exhaustionPenalty = 0;
               milkEngorgement = 0;
               milkEngorgementLevel = 0;
               udderEngorgement = 0;
               udderEngorgementLevel = 0;
               heat = 0;
               heatTime = 0;
               heatMaxTime = 0;
               lactation = 0;
               udderLactation = 0;
               nipplePlay = 0;
               udderPlay = 0;
               blueBalls = 0;
               teatPump = 0;
               nipPump = 0;
               cockPump = 0;
               clitPump = 0;
               vulvaPump = 0;
               masoPot = 0;
               sMasoPot = 0;
               babyFree = 0;
               charmTime = 0;
               pheromone = 0;
               eggceleratorTime = 0;
               eggceleratorDose = 0;
               bodyOil = 0;
               lustPenalty = 0;
               snuggleBall = false;
               fertileGel = 0;
               eggType = 0;
               milkSuppressant = 0;
               milkSuppressantLact = 0;
               milkSuppressantUdder = 0;
               suppHarness = false;
               fertilityStatueCurse = 0;
               plumpQuats = 0;
               lilaWetStatus = 0;
               cockSnakePreg = 0;
               milkCPoisonNip = 0;
               milkCPoisonUdd = 0;
               cockSnakeVenom = 0;
               humanAffinity = 0;
               horseAffinity = 0;
               wolfAffinity = 0;
               catAffinity = 0;
               cowAffinity = 0;
               lizardAffinity = 0;
               rabbitAffinity = 0;
               fourBoobAffinity = 0;
               mouseAffinity = 0;
               birdAffinity = 0;
               pigAffinity = 0;
               twoBoobAffinity = 0;
               sixBoobAffinity = 0;
               eightBoobAffinity = 0;
               tenBoobAffinity = 0;
               cowTaurAffinity = 0;
               humanTaurAffinity = 0;
               skunkAffinity = 0;
               bugAffinity = 0;
               lilaRep = 0;
               lilaVulva = 0;
               lilaMilk = 0;
               lilaPreg = -2;
               malonRep = 0;
               malonPreg = 0;
               malonChildren = 0;
               mistressRep = 0;
               jamieRep = 0;
               jamieSize = 4;
               jamieChildren = 0;
               silRep = 0;
               silPreg = 0;
               silRate = 0;
               silLay = 10;
               silTied = false;
               silGrowthTime = 0;
               lilaUB = false;
               dairyFarmBrand = false;
               jamieRep1 = 0;
               jamieRep2 = 0;
               jamieRep3 = 0;
               lilaWetness = 0;
               foundSoftlik = false;
               foundFirmshaft = false;
               foundTieden = false;
               foundSizCalit = false;
               foundOviasis = false;
               foundValley = false;
               foundSanctuary = false;
               defeatedMinotaur = false;
               defeatedFreakyGirl = false;
               defeatedSuccubus = false;
               firstExplore = false;
               knowLustDraft = false;
               knowRejuvPot = false;
               knowExpPreg = false;
               knowBallSwell = false;
               knowMaleEnhance = false;
               knowSLustDraft = false;
               knowSRejuvPot = false;
               knowSExpPreg = false;
               knowSBallSwell = false;
               knowGenSwap = false;
               knowMasoPot = false;
               knowBabyFree = false;
               knowPotPot = false;
               knowMilkSuppress = false;
               knowSGenSwap = false;
               knowSMasoPot = false;
               knowSBabyFree = false;
               knowSPotPot = false;
               knowPussJuice = false;
               knowPheromone = false;
               knowBazoomba = false;
               babyFactLevel = 0;
               bodyBuildLevel = 0;
               hyperHappyLevel = 0;
               alchemistLevel = 0;
               fetishMasterLevel = 0;
               milkMaidLevel = 0;
               shapeshiftyLevel = 0;
               shapeshiftyFirst = "";
               shapeshiftySecond = "";
               maleFetish = 1;
               femaleFetish = 1;
               hermFetish = 1;
               narcissistFetish = 1;
               dependentFetish = 1;
               dominantFetish = 1;
               submissiveFetish = 1;
               lboobFetish = 1;
               sboobFetish = 1;
               furryFetish = 1;
               scalyFetish = 1;
               smoothyFetish = 1;
               pregnancyFetish = 1;
               bestialityFetish = 1;
               milkFetish = 1;
               sizeFetish = 1;
               unbirthingFetish = 1;
               ovipositionFetish = 1;
               toyFetish = 1;
               hyperFetish = 1;
               currentDayCare = 0;
               humanChildren = 0;
               equanChildren = 0;
               lupanChildren = 0;
               felinChildren = 0;
               cowChildren = 0;
               lizanEggs = 0;
               lizanChildren = 0;
               bunnionChildren = 0;
               miceChildren = 0;
               birdEggs = 0;
               birdChildren = 0;
               pigChildren = 0;
               bugEggs = 0;
               bugChildren = 0;
               skunkChildren = 0;
               minotaurChildren = 0;
               freakyGirlChildren = 0;
               wolfPupChildren = 0;
               calfChildren = 0;
               bagPage = 1;
               bagArray = [];
               bagStackArray = [];
               bagSlotAdd(27);
               stashArray = [];
               stashStackArray = [];
               stashSlotAdd(27);
               doRace();
          else
               doReturn();

def AppearanceGo():
def DetailedStats():
def DetailedTitles():
def DetailedStatuses():
def DetailedLevels():
def DetailedGear():
def DetailedFetishes():
def DetailedHelp():
def DetailedCredits():
def SaveGo():
def LoadGo():
def DoSave():
def DoLoad():
def CheckUpdate():
def LoadFromFile():
def FileSelected():
def LoadError():
def DataLoaded():
def DoRace():
def DoGender():
def BodyType():
def DoStartingDescription():
def DoGeneral():
def DoJizzPants():
def DoBag():
def UseItem():
def ItemAdd():
def GainItem():
def CheckOpenSlots():
def BagSlotAdd():
def BagSlotRemove():
def BagSlotClear():
def DoDiscard():
def ItemMove():
def ShowMoveItem():
def ItemMove():
def ItemDescription():
def UsableItem():
def CanLose():
def ConItem():
def PassiveItemAdd():
def PassiveItemRemove():
def LoseManyItem():
def ItemValue():
def ItemStackMax():
def FoodItem():
def DoItemUse():
def DoStash():
def DoStoreStash():
def DoRemoveStash():
def StashStore():
def StashRemove():
def StashSlotAdd():
def StashSlotRemove():
def DoShops():
def DoShop():
def DoSell():
def GoodsID():
def DoDyeShop():
def DyeID():
def DyeThing():
def DoApothecary():
def ApothID():
def ApothLearn():
def ApothName():
def ApothDescription():
def ApothValue():
def DoSalon():
def HairstyleName():
def HairDesc():
def HairC():
def HairL():
def HairstyleID():
def HairstyleValue():
def HairstyleLength():
def HairstyleDescription():
def DoTailor():
def ClothesName():
def ClothesID():
def ClothesValue():
def ClothesDescription():
def ClothesTop():
def ClothesBottom():
def CurrentClothes():
def PullUD():
def ClothesChange():
def ChangeTop():
def ChangeBot():
def DoDayCare():
def DoProstitute():
def DoSleep():
def DoMasturbate():
def DoCockMasturbate():
def DoVagMasturbate():
def DoBothMasturbate():
def DoBoobMasturbate():
def DoUdderMasturbate():
def DoAlchemy():
def SimpleAlchemy():
def ComplexAlchemy():
def AdvancedAlchemy():
def MakeAlchemy():
def DoLevelUp():
def DoExplore():
def EventSelect():
def DoSoftlik():
def DoFirmshaft():
def DoTieden():
def DoSizCalit():
def DoOviasis():
def DoSanctuary():
def DoForest():
def DoJungle():
def DoPlains():
def DoSavanna():
def DoDesert():
def DoBeach():
def DoDairyFarm():
def DoOldCave():
def DoDen():
def DoValley():
def DoDungeon():
def DoOldCaveDescent():
def LilaDesc():
def Gibberish():
def GibButt():
def KnotholeMain():
def KnotholeLeave():
def KnotholeUpstairs():
def DoBattle():
def WeaponAttack():
def DoSpecialAbility():
def SpecialAbilityName():
def SpecialAbilityDescription():
def SpecialAbilityUse():
def DoEntice():
def BattleWin():
def SpecialRapeWin():
def SpecialKOWin():
def SpecailKOLose():
def DoRape():
def DoGetRaped():
def SetEnemyStats():
def DoeHP():
def DoeLust():
def eDmg():
def EnemyName():
def EnemyBaseStats():
def EnemyBaby():
def EnemyAttack():
def DoStatus():
def Affinity():
def Aff():
def AffinityChange():
def CockChange():
def CockLoss():
def VagChange():
def VagBellyChange():
def LegChange():
def BoobChange():
def UdderChange():
def UdderCheck():
def LactChange():
def PregCheck():
def DoImpregnate():
def DoBirth():
def Plural():
def OneYour(topic:int):
     global cockTotal, vagTotal
     tempStr:str
     tempStr = "ONE YOUR ERROR " + cockTotal + " " + vagTotal
     if topic == 1:
          if cockTotal > 1:
               tempStr = "one of your"
          if cockTotal == 1:
               tempStr = "your"
     if topic == 2:
          if vagTotal > 1:
               tempStr = "one of your"
          if vagTotal == 1:
               tempStr = "your"
     return tempStr

def BodyDesc():
     global gender, body, hips, breastSize, butt
     tempStr:str
     tempStr = "BODY ERROR " + gender + " " + body
     if gender == 1:
          if (body > 11) and (body <= 17):
               if (hips > 3) and (breastSize > 4):
                    tempStr = "shemale"
               elif hips > 2:
                    tempStr = "femme-boyish"
               else:
                  tempStr = "boyish"
          elif (body > 17) and (body <= 25):
               tempStr = "manly"
          elif body <= 11:
               tempStr = "childish"
          elif body > 25:
               tempStr = "musclebound"
     elif gender == 2:
          if (body > 9) and (body <= 14):
               tempStr = "girly"
          if (body > 14) and (body <= 20):
               if (hips > 4) or (butt > 4) or (breastSize > 4):
                    tempStr = "voluptuous"
               else:
                    tempStr = "womanly"
          if body <= 10:
               tempStr = "childish"
          if (body > 17) and (breastSize <= 2):
               tempStr = "cunt-boy"
          elif body > 20:
               tempStr = "musclebound"
     elif gender == 3:
          if (body > 11) and (body <= 23):
               if (hips > 2) and (breastSize > 2):
                    tempStr = "feminine"
               else:
                    tempStr = "masculine"
          elif body <= 11:
               tempStr = "childish"
          elif body > 23:
               tempStr = "musclebound"
     elif gender == 0:
          if (body > 11) and (body <= 15):
               tempStr = "teenage"
          elif (body > 15) and (body <= 23):
               tempStr = "fully grown"
          elif body <= 11:
               tempStr = "childish"
          elif body > 23:
               tempStr = "musclebound"
     return tempStr

def TailDesc():
     global tail
     chance:int = 0
     tempStr:str
     chance = Percent();
     tempStr = "TAIL ERROR " + tail
     if chance <= 100:
          if tail == 2:
               tempStr = "equine"
          if tail == 3:
               tempStr = "wolfish"
          if tail == 4:
               tempStr = "cat-like"
          if tail == 5:
               tempStr = "bovine"
          if tail == 6:
               tempStr = "reptillian"
          if tail == 7:
               tempStr = "bunny"
          if tail == 8:
               tempStr = "mousy"
          if tail == 9:
               tempStr = "birdy"
          if tail == 10:
               tempStr = "piggy"
          if tail == 11:
               tempStr = "skunky"
          if tail == 12:
               tempStr = "thick ovipositor"
          if tail == 1002:
               tempStr = HumanTaurTailDesc()
     if chance <= 50:
          if tail == 2:
               tempStr = "bristly"
          if tail == 3:
               tempStr = "fluffy"
          if tail == 4:
               tempStr = "lithe"
          if tail == 5:
               tempStr = "skinny, bristly-tipped"
          if tail == 6:
               tempStr = "thick, sleek"
          if tail == 7:
               tempStr = "poofy puff-ball"
          if tail == 8:
               tempStr = "thin, naked"
          if tail == 9:
               tempStr = "feathery"
          if tail == 10:
               tempStr = "short, curly"
          if tail == 11:
               tempStr = "big striped fluffy"
          if tail == 12:
               tempStr = "wide bulbous"
          if tail == 1002:
               tempStr = HumanTaurTailDesc()
     return tempStr

def HumanTaurTailDesc():
     global hair, hairLength
     tempStr:str
     tempStr = ""
     if HairstyleLength(hair):
          if hairLength == 2:
              tempStr = "short "
          if hairLength == 4:
               tempStr = ""
          if hairLength == 6:
               tempStr = "long "
          if hairLength == 8:
               tempStr = "very long "
          if hairLength == 10:
               tempStr = "ground-dragging "
     tempStr += HairC()
     if hair == 0:
          tempStr = "hairy"
     if hair == 1:
            tempStr = "wavy haired"
     if hair == 2:
          tempStr = "pigtailed"
     if hair == 3:
          tempStr = "ponytailed"
     if hair == 4:
          tempStr = "straight haired"
     if hair == 5:
          tempStr = "stubbly haired"
     if hair == 6:
          tempStr = "mohawked"
     if hair == 7:
            tempStr = "bunned"
     if hair == 8:
          tempStr = "curly haired"
     if hair == 9:
          tempStr = "braided pigtailed"
     if hair == 10:
            tempStr = "braided ponytailed "
     if hair == 11:
          tempStr = "braided"
     if hair == 12:
          tempStr = "spiky haired"
     if hair == 13:
          tempStr = "stiff haired"
     if hair == 14:
          tempStr = "poofball"
     return tempStr

def EarDesc():
     global ears
     chance:int
     tempStr:str
     chance = Percent()
     tempStr = "EAR ERROR " + ears
     if chance <= 100:
          if ears == 1:
               tempStr = "Hugging the sides of your head, you have small rounded ears that can easily be hidden by your hair, like that of a human's"
          if ears == 2:
               tempStr = "Atop your head, you have large tear-drop shaped ears that flick every now and then, able to hear quite well, like that of a horse's"
          if ears == 3:
               tempStr = "Atop your head, you have small triangular ears that stand perk, like that of a wolf's"
          if ears == 4:
               tempStr = "Atop your head, you have small triangular ears that stand perk, like that of a cat's"
          if ears == 5:
               tempStr = "Standing out perpendicular from the sides of your head, you have large oval ears that that droop slightly from their size, like that of a cow's"
          if ears == 6:
               tempStr = "On the sides of your head, you have sleek holes for ears, like many lizards have"
          if ears == 7:
               tempStr = "Atop your head, you have long ears that stand high and vigilant, like that of a rabbit's"
          if ears == 8:
               tempStr = "Standing out perpendicular the sides of your head, large rounded ears practically flap when they twitch, looking like you glued discs to the sides of your head, like that of a mouse's"
          if ears == 9:
               tempStr = "On the sides of your head, have flat patches of feathers covering your holes, like a bird's"
          if ears == 10:
               tempStr = "Standing out perpendicular from the sides of your head, you have triangular ears that fold near the ends and droop down from their length, like that of a pig's"
          if ears == 11:
               tempStr = "Atop your head, you have small round ears that stand perk, like that of a skunk's"
          if ears == 12:
               tempStr = "Hugging the sides of your head, you have long pointy ears with wavy-shaped lobes, colored vibrantly like the wings of a butterfly"
     return tempStr

def FaceDesc():
     global faceType
     tempStr = ""
     if faceType == 10:
          tempStr += ", your face round with a moderate-sized nose"
     if faceType == 20:
          tempStr += ", your face slightly longer than normal with large confident eyes"
     if faceType == 21:
          tempStr += ", your face having a wide and strong muzzle with large confident eyes"
     if faceType == 30:
          tempStr += ", your face looking slightly fierce with sharp teeth and focused eyes"
     if faceType == 31:
          tempStr += ", your face having a narrow and toothy muzzle with focused eyes"
     if faceType == 40:
          tempStr += ", your face somewhat flat with a small button nose"
     if faceType == 41:
          tempStr += ", your face somewhat flat with a small button nose, long whiskers, and a general catty grin"
     if faceType == 50:
          tempStr += ", your face seemingly docile with a broad nose and slightly gentle eyes"
     if faceType == 51:
          tempStr += ", your face having a broad muzzle and calm gentle eyes"
     if faceType == 60:
          tempStr += ", your face somewhat flat with a nose that is mostly a slight bump with two slits for nostrils"
     if faceType == 61:
          tempStr += ", your face narrowing down a short muzzle with only slits for nostrils"
     if faceType == 70:
          tempStr += ", your face somewhat flat with a twitchy button nose and large friendly eyes"
     if faceType == 71:
            tempStr += ", your face somewhat flat with a twitchy button nose and whiskers, slightly buck-toothed, and your eyes large and friendly"
     if faceType == 80:
          tempStr += ", your face somewhat narrowed with a curious button nose, your eyes careful of their surroundings"
     if faceType == 81:
          tempStr += ", your face somewhat narrowed with a curious button nose, your eyes careful of their surroundings while your buck-teeth chitter as the whiskers on your puffy cheeks twitch"
     if faceType == 90:
          tempStr += ", your face rather awake with your large hooked nose and constantly alert eyes"
     if faceType == 91:
          tempStr += ", your face narrowing down to a razor-sharp beak that makes up your nose and mouth while your eyes are constantly watchful"
     if faceType == 100:
          tempStr += ", your face rather round and somewhat pudgy"
     if faceType == 101:
          tempStr += ", your face rather round and somewhat pudgy with a large upturned nose"
     if faceType == 102:
          tempStr += ", your face rather round and somewhat pudgy with a large upturned nose and pointed tusks that grow up from the sides of your mouth to nearly obstruct your vision"
     if faceType == 110:
          tempStr += ", your face somewhat long with a small button nose and cute eyes"
     if faceType == 111:
          tempStr += ", your face somewhat long with a small button nose, long whiskers, and cute gentle eyes"
     if faceType == 120:
          tempStr += ", your face somewhat flat with a chitinous bandage over the bridge of your nose and large gazing eyes"
     if faceType == 121:
          tempStr += ", your face somewhat flat with a chitinous bandage over the bridge of your nose and large nectar-sucking lips that offset your large darkened eyes"
     return tempStr

def BoobDesc():
     global breastSize
     chance = Percent()
     tempStr = "BOOB ERROR " + breastSize
     if chance <= 100:
          if breastSize <= 0:
               tempStr = "flat"
          if breastSize > 0 and breastSize <= 2:
               tempStr = "nearly flat"
          if breastSize > 2 and  breastSize <= 8:
               tempStr = "noticeable"
          if breastSize > 8 and breastSize <= 20:
               tempStr = "large"
          if breastSize > 20 and breastSize <= 40:
               tempStr = "huge"
          if breastSize > 40 and breastSize <= 76:
               tempStr = "humongous"
          if breastSize > 76 and breastSize <= 146:
               tempStr = "massive"
          if breastSize > 146 and breastSize <= 210:
               tempStr = "gargantuan"
          if breastSize > 210 and breastSize <= 280:
               tempStr = "tremendous"
          if breastSize > 280 and breastSize <= 560:
               tempStr = "colossal"
          if breastSize > 560:
               tempStr = "ridiculously huge"
     if chance > 50
          if breastSize <= 0:
               tempStr = ""
          if breastSize > 0 and breastSize <= 2:
               tempStr = "tiny"
          if breastSize > 2 and breastSize <= 4:
               tempStr = "palmable"
          if breastSize > 8 and breastSize <= 20:
               tempStr = "ample"
          if breastSize > 20 and breastSize <= 40:
               tempStr = "head-sized"
          if breastSize > 40 and breastSize <= 76:
               tempStr = "hefty"
          if breastSize > 76 and breastSize <= 146:
               tempStr = "beachball-sized"
          if breastSize > 146 and breastSize <= 210:
               tempStr = "normally back-breaking"
          if breastSize > 210 and breastSize <= 280:
               tempStr = "view-obscuring"
          if breastSize > 280 and breastSize <= 560:
               tempStr = "bed-sized"
          if breastSize > 560:
               tempStr = "road-filling"
     return tempStr

def UdderDesc():
     global udderSize
     chance = Percent()
     tempStr = "udder ERROR " + (udderSize / 2)
     if chance <= 100:
          if (udderSize / 2) <= 2:
               tempStr = "nearly flat"
          if (udderSize / 2) > 2 and (udderSize / 2) <= 8:
               tempStr = "noticeable"
          if (udderSize / 2) > 8 and (udderSize / 2) <= 20:
               tempStr = "large"
          if (udderSize / 2) > 20 and (udderSize / 2) <= 40
               tempStr = "huge"
          if (udderSize / 2) > 40 and (udderSize / 2) <= 76
               tempStr = "humongous"
          if (udderSize / 2) > 76 and (udderSize / 2) <= 146
               tempStr = "massive"
          if (udderSize / 2) > 146 and (udderSize / 2) <= 210
               tempStr = "gargantuan"
          if (udderSize / 2) > 210 and (udderSize / 2) <= 280
               tempStr = "tremendous"
          if (udderSize / 2) > 280 and (udderSize / 2) <= 560
               tempStr = "colossal"
          if (udderSize / 2) > 560
               tempStr = "ridiculously huge"
     if chance > 50:
          if (udderSize / 2) <= 2:
               tempStr = "tiny"
          if (udderSize / 2) > 2 and (udderSize / 2) <= 8:
               tempStr = "palmable"
          if (udderSize / 2) > 8 and (udderSize / 2) <= 20:
               tempStr = "ample"
          if (udderSize / 2) > 20 and (udderSize / 2) <= 40:
               tempStr = "head-sized"
          if (udderSize / 2) > 40 and (udderSize / 2) <= 76:
               tempStr = "hefty"
          if (udderSize / 2) > 76 and (udderSize / 2) <= 146:
               tempStr = "beachball-sized"
          if (udderSize / 2) > 146 and (udderSize / 2) <= 210:
               tempStr = "normally back-breaking"
          if (udderSize / 2) > 210 and (udderSize / 2) <= 280:
               tempStr = "view-obscuring"
          if (udderSize / 2) > 280 and (udderSize / 2) <= 560:
               tempStr = "bed-sized"
          if (udderSize / 2) > 560:
               tempStr = "road-filling"
     return tempStr

def TeatDesc():
     global teatSize
     chance = Percent()
     tempStr = "TEAT ERROR " + teatSize
     if chance <= 100:
          if teatSize <= 2:
               tempStr = "normal"
          if teatSize > 2 and teatSize <= 5:
               tempStr = "noticeable"
          if teatSize > 5 and teatSize <= 9:
               tempStr = "blatant"
          if teatSize > 9 and teatSize <= 30:
               tempStr = "normal-for-a-cow"
          if teatSize > 30 and teatSize <= 50:
               tempStr = "cock-like"
          if teatSize > 50 and teatSize <= 100:
               tempStr = "horsecock-like"
          if teatSize > 100 and teatSize <= 140:
               tempStr = "arm-length"
          if teatSize > 140 and teatSize <= 300:
               tempStr = "street-clearing"
          if teatSize > 300:
               tempStr = "obscene"
     if chance > 50:
          if teatSize <= 2:
               tempStr = ""
          if teatSize > 2 and teatSize <= 5:
               tempStr = "perky"
          if teatSize > 5 and teatSize <= 9:
               tempStr = "hypnotizing"
          if teatSize > 9 and teatSize <= 30:
               tempStr = "long"
          if teatSize > 30 and teatSize <= 50:
               tempStr = "huge"
          if teatSize > 50 and teatSize <= 100:
               tempStr = "enormous"
          if teatSize > 100 and teatSize <= 140:
               tempStr = "extreme"
          if teatSize > 140 and teatSize <= 300:
               tempStr = "ridiculous"
          if teatSize > 300:
               tempStr = "obscene"
     return tempStr

def ButtDesc():
     global butt, buttMod
     chance = Percent()
     tempStr = "BUTT ERROR " + butt
     if chance <= 100:
          if (butt * buttMod) <= 2:
               tempStr = "flat"
          if (butt * buttMod) > 2 and (butt * buttMod) <= 5:
               tempStr = "tight"
          if (butt * buttMod) > 5 and (butt * buttMod) <= 15:
               tempStr = "ample"
          if (butt * buttMod) > 15 and (butt * buttMod) <= 30:
               tempStr = "large"
          if (butt * buttMod) > 30 and (butt * buttMod) <= 50:
               tempStr = "huge"
          if (butt * buttMod) > 50 and (butt * buttMod) <= 80:
               tempStr = "grand"
          if (butt * buttMod) > 80 and (butt * buttMod) <= 130:
               tempStr = "jumbo"
          if (butt * buttMod) > 130 and (butt * buttMod) <= 175:
               tempStr = "giant"
          if (butt * buttMod) > 175:
               tempStr = "ginormous"
     if chance > 50:
          if (butt * buttMod) <= 2:
               tempStr = "boney"
          if (butt * buttMod) > 2 and (butt * buttMod) <= 5:
               tempStr = "firm"
          if (butt * buttMod) > 5 and (butt * buttMod) <= 15:
               tempStr = "grope-able"
          if (butt * buttMod) > 15 and (butt * buttMod) <= 30:
               tempStr = "jiggly"
          if (butt * buttMod) > 30 and (butt * buttMod) <= 50:
               tempStr = "pillow-like"
          if (butt * buttMod) > 50 and (butt * buttMod) <= 80:
               tempStr = "wobbling"
          if (butt * buttMod) > 80 and (butt * buttMod) <= 130:
               tempStr = "swaying"
          if (butt * buttMod) > 130 and (butt * buttMod) <= 175:
               tempStr = "bouncing"
          if (butt * buttMod) > 175:
               tempStr = "constantly quivering"
     return tempStr

def VulvaDesc():
     global vulvaSize
     chance = Percent()
     tempStr = "VULVA ERROR " + vulvaSize
     if chance <= 100:
          if vulvaSize <= 2:
               tempStr = "tiny"
          if vulvaSize > 2 and vulvaSize <= 8:
               tempStr = "plush"
          if vulvaSize > 8 and vulvaSize <= 16:
               tempStr = "plump"
          if vulvaSize > 16 and vulvaSize <= 24:
               tempStr = "huge"
          if vulvaSize > 24 and vulvaSize <= 36:
               tempStr = "enormous"
          if vulvaSize > 36 and vulvaSize <= 54:
               tempStr = "gigantic"
          if vulvaSize > 54 and vulvaSize <= 84:
               tempStr = "humongous"
          if vulvaSize > 84 and vulvaSize <= 124:
               tempStr = "tremendous"
          if vulvaSize > 124 and vulvaSize <= 160:
               tempStr = "colossal"
          if vulvaSize > 160:
               tempStr = "ridiculous"
     if chance > 50:
          if vulvaSize == 2:
               tempStr = "childlike"
          if vulvaSize > 2 and vulvaSize <= 8:
               tempStr = "dainty"
          if vulvaSize > 8 and vulvaSize <= 16:
               tempStr = "kissable"
          if vulvaSize > 16 and vulvaSize <= 24:
               tempStr = "groin-filling"
          if vulvaSize > 24 and vulvaSize <= 36:
               tempStr = "thigh-spreading"
          if vulvaSize > 36 and vulvaSize <= 54:
               tempStr = "" + LegDesc(1) + "-" + LegVerb(2) + ""
          if vulvaSize > 54 and vulvaSize <= 84:
               tempStr = "ground-scraping"
          if vulvaSize > 84 and vulvaSize <= 124:
               tempStr = "person-sized"
          if vulvaSize > 124 and vulvaSize <= 160:
               tempStr = "room-sized"
          if vulvaSize > 160:
               tempStr = "building-sized"
     return tempStr

def CockDesc():
     global cockSize, cockSizeMod
     chance = Percent()
     tempCock = str(cockSize) * str(cockSizeMod)
     tempStr = "COCK ERROR " + tempCock
     if chance <= 100:
          if tempCock <= 8:
               tempStr = "puny"
          if tempCock > 8 and tempCock <= 12:
               tempStr = "average-sized"
          if tempCock > 12 and tempCock <= 24:
               tempStr = "big"
          if tempCock > 24 and tempCock <= 32:
               tempStr = "large"
          if tempCock > 32 and tempCock <= 56:
               tempStr = "huge"
          if tempCock > 56 and tempCock <= 72:
               tempStr = "enormous"
          if tempCock > 72 and tempCock <= 100:
               tempStr = "gigantic"
            if tempCock > 100 and tempCock <= 152:
               tempStr = "humongous"
            if tempCock > 152 and tempCock <= 304:
               tempStr = "tremendous"
            if tempCock > 304 and tempCock <= 608:
               tempStr = "colossal"
            if tempCock > 608 and tempCock <= 1200:
               tempStr = "ridiculous"
            if tempCock > 1200:
               tempStr = "impossibly-ginormous"
     if chance > 50:
          if tempCock <= 8:
               tempStr = "infantile"
          if tempCock > 8 and tempCock <= 12:
               tempStr = "hand-length"
          if tempCock > 12 and tempCock <= 24:
               tempStr = "larger than normal"
          if tempCock > 24 and tempCock <= 32:
               tempStr = "foot-long"
          if tempCock > 32 and tempCock <= 56:
               tempStr = "thigh-slapping"
          if tempCock > 56 and tempCock <= 72:
               tempStr = "knee-knocking"
          if tempCock > 72 and tempCock <= 100:
               tempStr = "leg-sized"
          if tempCock > 100 and tempCock <= 152:
               tempStr = "person-sized"
          if tempCock > 152 and tempCock <= 304:
               tempStr = "car-sized"
          if tempCock > 304 and tempCock <= 608:
               tempStr = "bus-sized"
          if tempCock > 608 and tempCock <= 1200:
               tempStr = "building-sized"
          if tempCock > 1200:
               tempStr = "landscape-filling"
     return tempStr

def BallDesc():
     global ballSize
     chance = Percent()
     tempStr = "BALLS ERROR " + ballSize
     if chance <= 100:
          if ballSize <= 1:
               tempStr = "tiny"
          if ballSize > 1 and ballSize <= 3:
               tempStr = "small"
          if ballSize > 3 and ballSize <= 5:
               tempStr = "big"
          if ballSize > 5 and ballSize <= 8:
               tempStr = "large"
          if ballSize > 8 and ballSize <= 13:
               tempStr = "hand-filling"
          if ballSize > 13 and ballSize <= 17:
               tempStr = "huge"
          if ballSize > 17 and ballSize <= 26:
               tempStr = "barely palmable"
          if ballSize > 26 and ballSize <= 40:
               tempStr = "enormous"
          if ballSize > 40 and ballSize <= 80:
               tempStr = "tremendous"
          if ballSize > 80 and ballSize <= 120:
               tempStr = "huggable"
          if ballSize > 120 and ballSize <= 240:
               tempStr = "gargantuan"
          if ballSize > 240:
               tempStr = "colossal"
     if chance > 50:
          if ballSize <= 1:
               tempStr = "marble-sized"
          if ballSize > 1 and ballSize <= 3:
               tempStr = "golfball-sized"
          if ballSize > 3 and ballSize <= 5:
               tempStr = "kiwi-sized"
          if ballSize > 5 and ballSize <= 8:
               tempStr = "tennisball-sized"
          if ballSize > 8 and ballSize <= 13:
               tempStr = "baseball-sized"
          if ballSize > 13 and ballSize <= 17:
               tempStr = "softball-sized"
          if ballSize > 17 and ballSize <= 26:
               tempStr = "cantaloupe-sized"
          if ballSize > 26 and ballSize <= 40:
               tempStr = "basketball-sized"
          if ballSize > 40 and ballSize <= 80:
               tempStr = "watermelon-sized"
          if ballSize > 80 and ballSize <= 120:
               tempStr = "beachball-sized"
          if ballSize > 120 and ballSize <= 240:
               tempStr = "boulder-sized"
          if ballSize > 240:
               tempStr = "landscape-crushing"
     return tempStr

def NipDesc():
     global nippleSize
     chance = Percent()
     tempStr = "NIPPLE ERROR " + nippleSize
     if chance <= 100:
          if nippleSize <= 2:
               tempStr = "small "
          if nippleSize > 2 and nippleSize <= 5:
               tempStr = "noticeable "
          if nippleSize > 5 and nippleSize <= 15:
               tempStr = "blatant "
          if nippleSize > 15 and nippleSize <= 30:
               tempStr = "teat-like "
          if nippleSize > 30 and nippleSize <= 50:
               tempStr = "cock-like "
          if nippleSize > 50 and nippleSize <= 100:
               tempStr = "horsecock-like "
          if nippleSize > 100 and nippleSize <= 140:
               tempStr = "arm-length "
          if nippleSize > 140 and nippleSize <= 300:
               tempStr = "street-clearing "
          if nippleSize > 300:
               tempStr = "obscene "
          if nipType == 2 and lust < 50:
               tempStr = "inverted "
     if chance > 50:
          if nippleSize <= 2:
               tempStr = ""
          if nippleSize > 2 and nippleSize <= 5:
               tempStr = "perky "
          if nippleSize > 5 and nippleSize <= 15:
               tempStr = "hypnotizing "
          if nippleSize > 15 and nippleSize <= 30:
               tempStr = "long "
          if nippleSize > 30 and nippleSize <= 50:
               tempStr = "huge "
          if nippleSize > 50 and nippleSize <= 100:
               tempStr = "enormous "
          if nippleSize > 100 and nippleSize <= 140:
               tempStr = "extreme "
          if nippleSize > 140 and nippleSize <= 300:
               tempStr = "ridiculous "
          if nippleSize > 300:
               tempStr = "obscene "
          if nipType == 2 and lust < 50:
               tempStr = "sunken "
     chance = Percent()
     if nipType == 1:
          if chance <= 50:
               tempStr += " quad-"
          else:
               tempStr = "quartets of " + tempStr
     return tempStr

def ClitDesc():
     global clitSize
     chance = Percent()
     tempStr = "CLIT ERROR " + clitSize
     if chance <= 100:
          if clitSize <= 2:
               tempStr = "tiny"
          if clitSize > 2 and clitSize <= 3:
               tempStr = "nibble-able"
          if clitSize > 3 and clitSize <= 6:
               tempStr = "protruding"
          if clitSize > 6 and clitSize <= 12:
               tempStr = "blatant"
          if clitSize > 12 and clitSize <= 25:
               tempStr = "suckable"
          if clitSize > 25 and clitSize <= 50:
               tempStr = "cock-like"
          if clitSize > 50 and clitSize <= 100:
               tempStr = "horsecock-like"
          if clitSize > 100 and clitSize <= 140:
               tempStr = "arm-length"
          if clitSize > 140 and clitSize <= 300:
               tempStr = "person-sized"
          if clitSize > 300:
               tempStr = "obscene"
     if chance > 50:
          if clitSize <= 2:
               tempStr = "small"
          if clitSize > 2 and clitSize <= 3:
               tempStr = "pinchable"
          if clitSize > 3 and clitSize <= 6:
               tempStr = "flickable"
          if clitSize > 6 and clitSize <= 12:
               tempStr = "panty-tenting"
          if clitSize > 12 and clitSize <= 25:
               tempStr = "stroke-able"
          if clitSize > 25 and clitSize <= 50:
               tempStr = "huge"
          if clitSize > 50 and clitSize <= 100:
               tempStr = "gigantic"
          if clitSize > 100 and clitSize <= 140:
               tempStr = "doorway-smacking"
          if clitSize > 140 and clitSize <= 300:
               tempStr = "snuggle-able"
          if clitSize > 300:
               tempStr = "obscene"
     return tempStr

def HipDesc():
     global hips, hipMod
     chance = Percent()
     tempStr = "HIP ERROR " + hips
     if chance <= 100:
          if (hips * hipMod) <= 3:
               tempStr = "narrow"
          if (hips * hipMod) > 3 and (hips * hipMod) <= 8:
               tempStr = "unnoticeable"
          if (hips * hipMod) > 8 and (hips * hipMod) <= 16:
               tempStr = "wide"
          if (hips * hipMod) > 16 and (hips * hipMod) <= 28:
               tempStr = "endowed"
          if (hips * hipMod) > 28 and (hips * hipMod) <= 40:
               tempStr = "protruding"
          if (hips * hipMod) > 40 and (hips * hipMod) <= 55:
               tempStr = "cow-like"
          if (hips * hipMod) > 55 and (hips * hipMod) <= 75:
               tempStr = "shelf-like"
          if (hips * hipMod) > 75 and (hips * hipMod) <= 100:
               tempStr = "doorway-jamming"
          if (hips * hipMod) > 100:
               tempStr = "perpetually-swaying"
     if chance > 50:
          if (hips * hipMod) <= 3:
               tempStr = "prepubescent"
          if (hips * hipMod) > 3 and (hips * hipMod) <= 8:
               tempStr = "average"
          if (hips * hipMod) > 8 and (hips * hipMod) <= 16:
               tempStr = "child-bearing"
          if (hips * hipMod) > 16 and (hips * hipMod) <= 28:
               tempStr = "especially fertile"
          if (hips * hipMod) > 28 and (hips * hipMod) <= 40:
               tempStr = "hypnotizing"
          if (hips * hipMod) > 40 and (hips * hipMod) <= 55:
               tempStr = "blatantly obvious"
          if (hips * hipMod) > 55 and (hips * hipMod) <= 75:
               tempStr = "excessively wide"
          if (hips * hipMod) > 75 and (hips * hipMod) <= 100:
               tempStr = "greatly protruding"
          if (hips * hipMod) > 100:
               tempStr = "gigantic"
     return tempStr

def BellyDesc():
     global pregnancyTime, vagBellyMod, bellyMod, tallness
     chance = Percent()
     tempBelly = ((pregnancyTime / 10) + (vagBellyMod / 3) + (bellyMod / 5)) * 60 / tallness
     tempStr = "BELLY ERROR " + tempBelly
     if pregnancyTime > bellyMod:
          if tempBelly <= 2:
               tempStr = "flat"
          elif tempBelly <= 4:
               tempStr = "hardly noticeable"
          elif tempBelly <= 7:
               tempStr = "protruding"
          elif tempBelly <= 11:
               tempStr = "swollen"
          elif tempBelly <= 14:
               tempStr = "cradleable"
          elif tempBelly <= 19:
               tempStr = "unbalancing"
          elif tempBelly <= 24:
               tempStr = "huggable"
          elif tempBelly <= 30:
               tempStr = "path-crowding"
          elif tempBelly <= 36:
               tempStr = "larger-than-you"
          elif tempBelly <= 42:
               tempStr = "ground-dragging"
          elif tempBelly <= 49:
               tempStr = "view-blocking"
          elif tempBelly <= 57:
               tempStr = "impossibly huge"
          elif tempBelly <= 66:
               tempStr = "bed-sized"
          elif tempBelly <= 76:
               tempStr = "portable-apartment"
          else:
               tempStr = "breeding-factory"
          if chance <= 50 and tempBelly > 11:
               tempStr += " pregnant"
          elif tempBelly > 11:
               tempStr += " gravid"
     else:
          if tempBelly <= 2:
               tempStr = "flat"
          elif tempBelly <= 4:
               tempStr = "hardly noticeable"
          elif tempBelly <= 7:
               tempStr = "chubby"
          elif tempBelly <= 11:
               tempStr = "porky"
          elif tempBelly <= 14:
               tempStr = "multi-rolled"
          elif tempBelly <= 19:
               tempStr = "pillow-like"
          elif tempBelly <= 24:
               tempStr = "morbidly obese"
          elif tempBelly <= 30:
               tempStr = "bed-like"
          elif tempBelly <= 36:
               tempStr = "fat-encompassing"
          elif tempBelly <= 42:
               tempStr = "item-losing"
          elif tempBelly <= 49:
               tempStr = "almost spherical"
          elif tempBelly <= 57:
               tempStr = "limb-engulfing"
          elif tempBelly <= 66:
               tempStr = "blob-like"
          elif tempBelly <= 76:
               tempStr = "inhumanly large"
          else:
               tempStr = "gigantic blubbery mass of"
          if chance <= 50 and tempBelly > 11:
               tempStr += " jiggly"
          elif tempBelly > 11:
               tempStr += " meaty"
     return tempStr

def SkinDesc():
     global skinType, snuggleBall, skinColor
     tempStr = "SKIN ERROR " + skinType
     if skinType == 1:
          tempStr = "skin"
     if skinType == 2:
          tempStr = "fur"
     if skinType == 3:
          tempStr = "scales"
     if skinType == 4:
          tempStr = "feathers"
     if skinType == 5:
          tempStr = "chitin"
     if snuggleBall == true:
          tempStr = "plush and snuggly " + tempStr
     if skinColor > 0:
          tempStr = "" + SkinC() + "" + tempStr
     return tempStr

def SkinC():
     global skinColor
     tempStr = "SKIN COLOR ERROR " + skinColor
     if skinColor == 0:
          tempStr = ""
     if skinColor == 1:
          tempStr = "black "
     if skinColor == 2:
          tempStr = "blonde "
     if skinColor == 3:
          tempStr = "red "
     if skinColor == 4:
          tempStr = "brown "
     if skinColor == 5:
          tempStr = "coral pink "
     if skinColor == 6:
          tempStr = "auburn "
     if skinColor == 7:
          tempStr = "brown "
     if skinColor == 8:
          tempStr = "grey "
     if skinColor == 9:
          tempStr = "white "
     return tempStr

def legDesc(part:int):
     global legType
     tempStr = "LEG ERROR PART " + part + " TYPE " + legType
     if part == 1:
          tempStr = "leg"
     if part == 2:
          tempStr = "legs"
     if part == 3:
          tempStr = "thigh"
     if part == 4:
          tempStr = "thighs"
     if part == 5:
          tempStr = "knee"
     if part == 6:
          tempStr = "knees"
     if part == 7:
          tempStr = "ankle"
     if part == 8:
          tempStr = "ankles"
     if part == 9:
          tempStr = "foot"
          if legType == 1:
               tempStr = "paw"
          if legType == 1001:
               tempStr = "hoof"
          if CheckItem(102) == True:
               tempStr = "hoof
     if part == 10:
          tempStr = "feet"
          if legType == 1:
               tempStr = "paws"
          if legType == 1001:
               tempStr = "hooves"
          if CheckItem(102) == True:
               tempStr = "hooves"
     return tempStr

def LegVerb(part:int):
     global legType
     tempStr = "LEG VERB ERROR " + part + " TYPE " + legType
     if part == 1:
            tempStr = "spreading"
     if part == 2:
            tempStr = "spread wide"
     if part == 3:
            tempStr = "spread"
     if part == 4:
            tempStr = "clench"
     if part == 5:
            tempStr = "straddling"
     return tempStr

def LegWhere(part:int):
     global legType
         tempStr = "LEG WHERE ERROR " + part + " TYPE " + legType
     if part == 1:
          tempStr = "between"
          if legType == 1001:
               tempStr = "behind"
     if part == 2:
          tempStr = "between"
     return tempStr

def LegPlural(which:int):
     global legType
         tempStr = "LEG PLURAL ERROR TYPE " + legType
     if which == 1:
          tempStr = ""
     if which == 2:
          tempStr = "are"
     return tempStr

def RegionName(tempInt:int):
     global currentZone
     tempStr = "REGION ERROR " + currentZone
     if tempInt == 1:
          tempStr = "Softlik"
     if tempInt == 2:
          tempStr = "Firmshaft"
     if tempInt == 3:
          tempStr = "Tieden"
     if tempInt == 4:
          tempStr = "Siz'Calit"
     if tempInt == 6:
          tempStr = "Oviasis"
     if tempInt == 12:
          tempStr = "Sanctuary"
     return tempStr

def RaceName():
     global race
     tempStr = "RACE ERROR " + race
     if race == 1:
          tempStr = "Human"
     if race == 2:
          tempStr = "Equan"
     if race == 3:
          tempStr = "Lupan"
     if race == 4:
          tempStr = "Felin"
     if race == 6:
          tempStr = "Lizan"
     return tempStr

def DomName():
     global dominant
         tempStr = "DOMINANT ERROR " + dominant
     if dominant == 1:
          tempStr = "human"
     if dominant == 2:
          tempStr = "horse"
     if dominant == 3:
          tempStr = "wolf"
     if dominant == 4:
          tempStr = "cat"
     if dominant == 5:
          tempStr = "cow"
     if dominant == 6:
          tempStr = "lizard"
     if dominant == 7:
          tempStr = "bunny"
     if dominant == 8:
          tempStr = "mouse"
     if dominant == 9:
          tempStr = "bird"
     if dominant == 10:
          tempStr = "pig"
     if dominant == 11:
          tempStr = "skunk"
     if dominant == 12:
          tempStr = "bug"
     return tempStr

def GenName():
     global gender #, hips, breastSize, body.
         tempStr = "GENDER ERROR " + gender
     if gender == 0:
          tempStr = "n androgynous"
     if gender == 1:
          tempStr = " male"
#     if gender == 1 && this.hips > 3 && this.breastSize > 4:
#          tempStr = " female"
     if gender == 2:
          tempStr = " female"
#     if gender == 2 && this.body > 17 && this.breastSize <= 2:
#          tempStr = " male"
     if gender == 3:
          tempStr = " herm"
     return tempStr

def CumAmount():
     global blueBalls, ballSize, balls, cumMod
     tempNum = 0
     if blueBalls <= 12:
          tempNum = ballSize * (ballSize / 2) * balls * cumMod * 0.5
     if blueBalls > 12 and blueBalls <= 36:
          tempNum = ballSize * (ballSize / 2) * balls * cumMod * 1
     if blueBalls > 36 and blueBalls <= 84:
          tempNum = ballSize * (ballSize / 2) * balls * cumMod * 2
     if blueBalls > 84:
          tempNum = ballSize * (ballSize / 2) * balls * cumMod * 2.5
     blueBalls = 0
     return int(math.floor(tempNum))

def MilkAmount(origin:int):
     global milkEngorgement, breastSize, tallness, milkCap, milkEngorgementLevel, udderEngorgement, udderSize
     tempNum = 0
     if origin == 1:
          if milkEngorgement > ((breastSize * (breastSize + 1) + (tallness / 4) + milkCap) * 2):
               milkEngorgement = (breastSize * (breastSize + 1) + (tallness / 4) + milkCap) * 2
          if milkEngorgementLevel == 0:
               if boobTotal == 2:
                    tempNum = milkEngorgement * 0.5 * 2
               if boobTotal == 4:
                    tempNum = milkEngorgement * 0.5 * 4
               if boobTotal == 6:
                    tempNum = milkEngorgement * 0.5 * 3.5
               if boobTotal == 8:
                    tempNum = milkEngorgement * 0.5 * 6
               if boobTotal == 10:
                    tempNum = milkEngorgement * 0.5 * 8
          if milkEngorgementLevel == 1:
               if boobTotal == 2:
                    tempNum = milkEngorgement * 1 * 2
               if boobTotal == 4:
                    tempNum = milkEngorgement * 1 * 4
               if boobTotal == 6:
                    tempNum = milkEngorgement * 1 * 3.5
               if boobTotal == 8:
                    tempNum = milkEngorgement * 1 * 6
               if boobTotal == 10:
                    tempNum = milkEngorgement * 1 * 8
          if milkEngorgementLevel == 2:
               if boobTotal == 2:
                    tempNum = milkEngorgement * 1.2 * 2
               if boobTotal == 4:
                    tempNum = milkEngorgement * 1.2 * 4
               if boobTotal == 6:
                    tempNum = milkEngorgement * 1.2 * 3.5
               if boobTotal == 8:
                    tempNum = milkEngorgement * 1.2 * 6
               if boobTotal == 10:
                    tempNum = milkEngorgement * 1.2 * 8
          if milkEngorgementLevel == 3:
               if boobTotal == 2:
                    tempNum = milkEngorgement * 1.5 * 2
               if boobTotal == 4:
                    tempNum = milkEngorgement * 1.5 * 4
               if boobTotal == 6:
                    tempNum = milkEngorgement * 1.5 * 3.5
               if boobTotal == 8:
                    tempNum = milkEngorgement * 1.5 * 6
               if boobTotal == 10:
                    tempNum = milkEngorgement * 1.5 * 8
          if milkEngorgementLevel == 1:
               .milkEngorgementLevel = 0
               BoobChange(-1)
          if milkEngorgementLevel == 2:
               milkEngorgementLevel = 0
               BoobChange(-2)
          if milkEngorgementLevel > 2:
               milkEngorgementLevel = 0
               BoobChange(-3)
          milkEngorgement = 0
     if origin == 2:
          if udderEngorgement > ((udderSize * (udderSize + 1) + (tallness / 4) + milkCap) * 2):
               udderEngorgement = (udderSize * (udderSize + 1) + (tallness / 4) + milkCap) * 2
          if udderEngorgementLevel == 0:
               tempNum = udderEngorgement * 1
          if udderEngorgementLevel == 1:
               tempNum = udderEngorgement * 2.1
          if udderEngorgementLevel == 2:
               tempNum = udderEngorgement * 2.7
          if udderEngorgementLevel == 3:
               tempNum = udderEngorgement * 3.5
          if udderEngorgementLevel == 1:
               udderEngorgementLevel = 0
               UdderChange(-2)
          if udderEngorgementLevel == 2:
               udderEngorgementLevel = 0
               UdderChange(-5)
          if udderEngorgementLevel > 2:
               udderEngorgementLevel = 0
               UdderChange(-8)
          udderEngorgement = 0
     return int(math.floor(tempNum))

def __setProp_scrollBar2_Scene1_TextFields_0():
def __setProp_scrollBar1_Scene1_TextFields_0():
def Frame1():
     global versionNumber
     versionNumber = "0.975o"
     global theme
     theme = 0
     global fontSize
     fontSize = 14
     global fontBold
     fontBold = false
     global fontColor
     fontColor = "000000"
     global showSide
     showSide = true
     global i
     i = 0
     global buttonChoice
     buttonChoice = 0
     global currentText
     currentText = ""
     global sideText
     sideText = ""
     global sideFocus
     sideFocus = 1
     global pregTempInt
     pregTempInt = 0
     global pregTempBool
     pregTempBool = false
     global lustArray
     lustArray = list(())
     global bg
     bg = new Sprite()
     global rndResult
     rndResult = 0
     global rndArray
     rndArray = list(())
     global textCheckArray
     textCheckArray = list(())
     global choiceListArray
     choiceListArray = list(())
     global choiceListResult
     choiceListResult = list(())
     global choicePage
     choicePage = 0
     global moveItemID
     moveItemID = 0
     global moveItemStack
     moveItemStack = 0
     global skipExhaustion
     skipExhaustion = false
     global shiftHeld
     shiftHeld = false
     global currentState
     currentState = 0
     global inBag
     inBag = false
     global inShop
     inShop = false
     global currentZone
     currentZone = 0
     global day
     day = 0
     global hour
     hour = 8
     global inDungeon
     inDungeon = false
     global currentDungeon
     currentDungeon = 0
     global _str_
     _str_ = 0
     global ment
     ment = 0
     global lib
     lib = 0
     global sen
     sen = 0
     global HP
     HP = 0
     global lust
     lust = 0
     global coin
     coin = 0
     global strMod
     strMod = 0
     global mentMod
     mentMod = 0
     global libMod
     libMod = 0
     global senMod
     senMod = 0
     global strength
     strength = 0
     global mentality
     mentality = 0
     global libido
     libido = 0
     global sensitivity
     sensitivity = 0
     global hunger
     hunger = 0
     global hrs
     hrs = 0
     global itemGainArray
     itemGainArray = list(())
     global human
     human = 0
     global horse
     horse = 0
     global wolf
     wolf = 0
     global cat
     cat = 0
     global cow
     cow = 0
     global lizard
     lizard = 0
     global rabbit
     rabbit = 0
     global mouse
     mouse = 0
     global bird
     bird = 0
     global pig
     pig = 0
     global skunk
     skunk = 0
     global bug
     bug = 0
     global SexP
     SexP = 0
     global levelUP
     levelUP = 0
     global level
     level = 0
     global runMod
     eunMod = 0
     global rapeMod
     rapeMod = 0
     global cumMod
     cumMod = 1
     global cockSizeMod
     cockSizeMod = 1
     global vagSizeMod
     vagSizeMod = 1
     global vagElastic
     vagElastic = 1
     global milkMod
     milkMod = 0
     global carryMod
     carryMod = 0
     global vagBellyMod
     vagBellyMod = 0
     global pregChanceMod
     pregChanceMod = 0
     global extraPregChance
     extraPregChance = 0
     global pregTimeMod
     pregTimeMod = 0
     global enticeMod
     enticeMod = 0
     global milkHPMod
     milkHPMod = 0
     global changeMod
     changeMod = 1
     global HPMod
     HPMod = 0
     global SexPMod
     SexPMod = 1
     global minLust
     minLust = 0
     global milkCap
     milkCap = 0
     global coinMod
     coinMod = 0
     global hipMod
     hipMod = 1
     global buttMod
     buttMod = 1
     global bellyMod
     bellyMod = 0
     global cockMoistMod
     cockMoistMod = 0
     global vagMoistMod
     vagMoistMod = 0
     global lockTail
     lockTail = 0
     global lockFace
     lockFace = 0
     global lockSkin
     lockSkin = 0
     global lockBreasts
     lockBreasts = 0
     global lockEars
     lockEars = 0
     global lockLegs
     lockLegs = 0
     global lockNipples
     lockNipples = 0
     global lockCock
     lockCock = 0
     global enemyID
     enemyID = 0
     global eHP
     eHP = 0
     global eMaxHP
     eMaxHP = 0
     global eStr
     eStr = 0
     global eMenta
     eMenta = 0
     global eSen
     eSen = 0
     global eLib
     eLib = 0
     global eLust
     eLust = 0
     global eGen
     eGen = 0
     global ePref
     ePref = 0
     global eCoin
     eCoin = 0
     global eSexP
     eSexP = 0
     global eItem
     eItem = 0
     global gender
     gender = 0
     global race
     race = 0
     global body
     body = 0
     global dominant
     dominant = 0
     global hips
     hips = 0
     global butt
     butt = 0
     global tallness
     tallness = 0
     global skinType
     skinType = 0
     global tail
     tail = 0
     global ears
     ears = 0
     global hair
     hair = 0
     global hairLength
     hairLength = 0
     global hairColor
     hairColor = 0
     global legType
     legType = 0
     global wings
     wings = 0
     global faceType
     faceType = 0
     global skinColor
     skinColor = 0
     global cockTotal
     cockTotal = 0
     global humanCocks
     humanCocks = 0
     global horseCocks
     horseCocks = 0
     global wolfCocks
     wolfCocks = 0
     global catCocks
     catCocks = 0
     global lizardCocks
     lizardCocks = 0
     global rabbitCocks
     rabbitCocks = 0
     global cockSize
     cockSize = 0
     global cockMoist
     cockMoist = 0
     global balls
     balls = 0
     global ballSize
     ballSize = 0
     global showBalls
     showBalls = true
     global knot
     knot = false
     global bugCocks
     bugCocks = 0
     global breastSize
     breastSize = 0
     global boobTotal
     boobTotal = 0
     global nippleSize
     nippleSize = 1
     global udders
     udders = false
     global udderSize
     udderSize = 0
     global teatSize
     teatSize = 0
     global clitSize
     clitSize = 0
     global vagTotal
     vagTotal = 0
     global vagSize
     vagSize = 0
     global vagMoist
     vagMoist = 0
     global vulvaSize
     vulvaSize = 0
     global nipType
     nipType = 0
     global attireTop
     attireTop = 1
     global attireBot
     attireBottom = 2
     global weapon
     weapon = 10
     global pregArray
     pregArray = list(())
     global pregStatus
     pregStatus = 0
     global pregnancyTime
     pregnancyTime = 0
     global pregRate
     pregRate = 1
     global eggLaying
     eggLaying = 0
     global eggMaxTime
     eggMaxTime = 0
     global eggTime
     eggTime = 0
     global eggRate
     eggRate = 0
     global exhaustion
     exhaustion = 0
     global exhaustionPenalty
     exhaustionPenalty = 0
     global milkEngorgement
     milkEngorgement = 0
     global milkEngorgementLevel
     milkEngorgementLevel = 0
     global udderEngorgement
     udderEngorgement = 0
     global udderEngorgementLevel
     udderEngorgementLeve = 0
     global heat
     heat = 0
     global heatTime
     heatTime = 0
     global heatMaxTime
     heatMaxTime = 0
     global lactation
     lactation = 0
     global udderLactation
     udderLactation = 0
     global nipplePlay
     nipplePlay = 0
     global udderPlay
     udderPlay = 0
     global blueBalls
     blueBalls = 0
     global teatPump
     teatPump = 0
     global nipPump
     nipPump = 0
     global cockPump
     cockPump = 0
     global clitPump
     clitPump = 0
     global vulvaPump
     vulvaPump = 0
     global masoPot
     masoPot = 0
     global sMasoPot
     sMasoPot = 0
     global babyFree
     babyFree = 0
     global charmTime
     charmTime = 0
     global pheromone
     pheromone = 0
     global eggceleratorTime
     eggceleratorTime = 0
     global eggceleratorDose
     eggceleratorDose = 0
     global bodyOil
     bodyOil = 0
     global lustPenalty
     lustPenalty = 0
     global snuggleBall
     suggleBall = false
     global fertileGel
     fertileGel = 0
     global eggType
     eggType = 0
     global milkSuppressant
     milkSuppressany = 0
     global milkSuppressantLact
     milkSuppressantLact = 0
     global milkSuppressantUdder
     milkSuppressantUdder = 0
     global suppHarness
     suppHarness = false
     global fertilityStatueCurse
     fertilityStatueCurse = 0
     global plumpQuats
     plumpGuats = 0
     global lilaWetStatus
     lilaWetStatus = 0
     global cockSnakePreg
     cockSnakePreg = 0
     global milkCPoisonNip
     milkCPoisonNip = 0
     global milkCPoisonUdd
     milkCPoisonUdd = 0
     global cockSnakeVenom
     cockSnakeVenom = 0
     global humanAffinity
     humanAffinity = 0
     global horseAffinity
     horseAffinity = 0
     global wolfAffinity
     wolfAffinity = 0
     global catAffinity
     catAffinity = 0
     global cowAffinity
     cowAffinity = 0
     global lizardAffinity
     lizardAffinity = 0
     global rabbitAffinity
     rabbitAffinity = 0
     global fourBoobAffinity
     fourBoobAffinity = 0
     global mouseAffinity
     mouseAffinity = 0
     global birdAffinity
     birdAffinity = 0
     global pigAffinity
     pigAffinity = 0
     global twoBoobAffinity
     twoBoobAffinity = 0
     global sixBoobAffinity
     sixBoobAffinity = 0
     global eightBoobAffinity
     eightBoobAffinity = 0
     global tenBoobAffinity
     tenBoobAffinity = 0
     global cowTaurAffinity
     cowTaurAffinity = 0
     global humanTaurAffinity
     humanTaurAffinity = 0
     global skunkAffinity
     skunkAffinity = 0
     global bugAffinity
     bugAffinity = 0
     global lilaRep
     lilaRep = 0
     global lilaVulva
     lilaVulva = 0
     global lilaMilk
     lilaMilk = 0
     global lilaPreg
     lilaPreg = -2
     global malonRep
     malonRep = 0
     global malonPreg
     malonPreg = 0
     global malonChildren
     malonChildren = 0
     global mistressRep
     mistressRep = 0
     global jamieRep
     jamieRep = 0
     global jamieSize
     jamieSize = 4
     global jamieChildren
     jamieChildren = 0
     global silRep
     silRep = 0
     global silPreg
     silPreg = 0
     global silRate
     silRate = 0
     global silLay
     silLay = 10
     global silTied
     silTied = false
     global silGrowthTime
     silGrowthTime = 0
     global lilaUB
     lilaUB = false
     global dairyFarmBrand
     dairyFarmBrand = false
     global jamieRep1
     jamieRep1 = 0
     global jamieRep2
     jamieRep2 = 0
     global jamieRep3
     jamieRep3 = 0
     global lilaWetness
     lilaWetness = 0
     global jamieButt
     jamieButt = false
     global jamieBreasts
     jamieBreasts = false
     global jamieHair
     jamieHair = false
     global travArray
     travArray = list(())
     global foundSoftlik
     foundSoftlik = false
     global foundFirmshaft
     foundFirmshaft = false
     global foundTieden
     foundTieden = false
     global foundSizCalit
     foundSizCalit = false
     global foundOviasis
     foundOviasis = false
     global foundValley
     foundValley = false
     global foundSanctuary
     foundSanctuary = false
     global defeatedMinotaur
     defeatedMinotaur = false
     global defeatedFreakyGirl
     defeatedFreakyGirl = false
     global defeatedSuccubus
     defeatedSuccubus = false
     global firstExplore
     firstExplore = false
     global knowLustDraft
     knowLustDraft = false
     global knowRejuvPot
     knowRejuvPot = false
     global knowExpPreg
     knowExpPreg = false
     global knowBallSwell
     knowBallSwell = false
     global knowMaleEnhance
     knowMaleEnhance = false
     global knowSLustDraft
     knowLustDraft = false
     global knowSRejuvPot
     knowSRejuvPot = false
     global knowSExpPreg
     knowSExpPreg = false
     global knowSBallSwell
     knowSBallSwell = false
     global knowBabyFree
     knowBabyFree = false
     global knowPotPot
     knowPotPot = false
     global knowGenSwap
     knowGenSwap = false
     global knowMasoPot
     knowMasoPot = false
     global knowMilkSuppress
     knowMilkSuppress = false
     global knowSGenSwap
     knowSGenSwap = false
     global knowSMasoPot
     knowSMasoPot = false
     global knowSBabyFree
     knowSBabyFree = false
     global knowSPotPot
     knowSPotPot = false
     global knowPussJuice
     knowPussJuice = false
     global knowPheromone
     knowPheromone = false
     global knowBazoomba
     knowBazoomba = false
     global babyFactLevel
     babyFactLevel = 0
     global bodyBuildLevel
     bodyBuildLevel = 0
     global hyperHappyLevel
     hyperHappyLevel = 0
     global alchemistLevel
     alchemistLevel = 0
     global fetishMasterLevel
     fetishMasterLevel = 0
     global milkMaidLevel
     milkMaidLevel = 0
     global shapeshiftyLevel
     shapeshiftyLevel = 0
     global shapeshiftyFirst
     ShapeshiftyFirst = ""
     global shapeshiftySecond
     shapeshiftySecond = ""
     global maleFetish
     maleFetish = 1
     global femaleFetish
     femaleFetish = 1
     global hermFetish
     hermFetish = 1
     global narcissistFetish
     narcissistFetish = 1
     global dependentFetish
     dependentFetish = 1
     global dominantFetish
     dominantFetish = 1
     global submissiveFetish
     submissiveFetish = 1
     global lboobFetish
     lboobFetish = 1
     global sboobFetish
     sboobFetish = 1
     global furryFetish
     furryFetish = 1
     global scalyFetish
     scalyFetish = 1
     global smoothyFetish
     smoothyFetish = 1
     global pregnancyFetish
     pregnancyFetish = 1
     global bestialityFetish
     bestialityFetish = 1
     global milkFetish
     milkFetish = 1
     global sizeFetish
     sizeFetish = 1
     global unbirthingFetish
     unbirthingFetish = 1
     global ovipositionFetish
     ovipostitionFetish = 1
     global toyFetish
     toyFetish = 1
     global hyperFetish
     hyperFetish = 1
     global currentDayCare
     currentDayCare = 0
     global humanChildren
     humanChildren = 0
     global equanChildren
     equanChildren = 0
     global lupanChildren
     lupanChildren = 0
     global felinChildren
     felinChildren = 0
     global cowChildren
     cowChildren = 0
     global lizanEggs
     lizanEggs = 0
     global lizanChildren
     lizanChildren = 0
     global bunnionChildren
     bunnionChildren = 0
     global wolfPupChildren
     wolfPupChildren = 0
     global miceChildren
     miceChildren = 0
     global birdEggs
     birdEggs = 0
     global birdChildren
     birdChildren = 0
     global pigChildren
     pigChildren = 0
     global calfChildren
     caljChildren = 0
     global bugEggs
     bugEggs = 0
     global bugChildren
     bugChildren = 0
     global skunkChildren
     skunkChildren = 0
     global minotaurChildren
     minotaurChildren = 0
     global freakyGirlChildren
     freakyGirlChildren = 0
     global bagPage
     bagPage = 1
     global bagArray
     bagArray = list(())
     global bagStackArray
     bagStackArray = list(())
     global stashArray
     stashArray = list(())
     global stashStackArray
     stashStackArray = list(())
#    stage.addEventListener(KeyboardEvent.KEY_DOWN,this.hotKeys)
#    stage.addEventListener(KeyboardEvent.KEY_UP,this.keysUp)
#    global newGame.addEventListener(MouseEvent.CLICK,this.newGameStart)
#    global Choice1.addEventListener(MouseEvent.CLICK,this.buttonEvent1)
#    global Choice2.addEventListener(MouseEvent.CLICK,this.buttonEvent2)
#    global Choice3.addEventListener(MouseEvent.CLICK,this.buttonEvent3)
#    global Choice4.addEventListener(MouseEvent.CLICK,this.buttonEvent4)
#    global Choice5.addEventListener(MouseEvent.CLICK,this.buttonEvent5)
#    global Choice6.addEventListener(MouseEvent.CLICK,this.buttonEvent6)
#    global Choice7.addEventListener(MouseEvent.CLICK,this.buttonEvent7)
#    global Choice8.addEventListener(MouseEvent.CLICK,this.buttonEvent8)
#    global Choice9.addEventListener(MouseEvent.CLICK,this.buttonEvent9)
#    global Choice10.addEventListener(MouseEvent.CLICK,this.buttonEvent10)
#    global Choice11.addEventListener(MouseEvent.CLICK,this.buttonEvent11)
#    global Choice12.addEventListener(MouseEvent.CLICK,this.buttonEvent12)
#    global appearanceText.addEventListener(MouseEvent.CLICK,this.appearance)
#    global saveGame.addEventListener(MouseEvent.CLICK,this.saveG)
#    global loadGame.addEventListener(MouseEvent.CLICK,this.loadG)
#    global Side1.addEventListener(MouseEvent.CLICK,this.side1Event)
#    global Side2.addEventListener(MouseEvent.CLICK,this.side2Event)
#    global Side3.addEventListener(MouseEvent.CLICK,this.side3Event)
#    global Side4.addEventListener(MouseEvent.CLICK,this.side4Event)
#    global Side5.addEventListener(MouseEvent.CLICK,this.side5Event)
#    global Side6.addEventListener(MouseEvent.CLICK,this.side6Event)
#    global Side7.addEventListener(MouseEvent.CLICK,this.side7Event)
#    global Side8.addEventListener(MouseEvent.CLICK,this.side8Event)
#    global Option1.addEventListener(MouseEvent.CLICK,this.option1Event)
#    global Option2.addEventListener(MouseEvent.CLICK,this.option2Event)
#    global Option3.addEventListener(MouseEvent.CLICK,this.option3Event)
#    global Option4.addEventListener(MouseEvent.CLICK,this.option4Event)
#    global Option5.addEventListener(MouseEvent.CLICK,this.option5Event)
#    global Option6.addEventListener(MouseEvent.CLICK,this.option6Event)
#    global Option7.addEventListener(MouseEvent.CLICK,this.option7Event)
#    global scrollBar1.scrollTarget = this.outputWindow
#    global scrollBar2.scrollTarget = this.sideWindow
     global statPaneVisible
     statPaneVisible = false
     global levelPaneVisible
     levelPaneVisible = false
     global currentRegionVisible
     currentRegionVisible = false
     global regionVisible
     regionVisible = false
     global saveGameVisible
     saveGameVisible = false
     global DayPaneVisible
     DayPaneVisible = false
     global Option7Visible
     Option7Visible = false
     global appearanceTextVisible
     appearanceTextVisible = false
     global appearanceBoxVisible
     appearanceBoxVisible = false
"""
     global pageNum.embedFonts = true
     global pageNum.visible = false
     global pageNum.rotation += 90
"""
#    global moveItem.visible = false
#    global moveItemAmount.visible = false
#    global MoveOutline.visible = false
#    global MoveAmountOutline.visible = false
     SideHide()
     addChildAt(this.bg,0)
     viewButtonText(0,0,0,0,0,0,0,0,0,0,0,0)
     viewButtonOutline(0,0,0,0,0,0,0,0,0,0,0,0)
     HideAmount()
     HideUpDown()
     LoadPreferences()
     OutputMainText("Nimin: Fetish Fantasy" + "\n" + "    v" + versionNumber + "\n" + "\n" + "Click 'New Game' to begin a new game." + "\n" + "\n" + "Created by:    --Xadera" + "\n" + "    www.furaffinity.net/user/xadera/" + "\n" + "\n" + "Original concept by:     --Fenoxo" + "\n" + "    fenoxo.com" + "\n" + "\n" + "Currently maintained by:    ajdelguidice" + "\n" + "    github.com/ajdelguidice" + "\n" + "For tutorial/guide, questions, or bug reports, visit github.com/ajdelguidice/pymin/")