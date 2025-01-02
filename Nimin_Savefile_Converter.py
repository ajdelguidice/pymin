import tkinter
from tkinter import filedialog, ttk
try:
   from miniamf import sol, amf3, AMF3
except:
   print("Import Error: Can not import required library Mini-AMF")
   exit()
from pathlib import Path
import xml.etree.ElementTree as xmletree
from platform import system
from functools import partial
from sys import argv

platform = system()

class NullData(Exception):...

def repintorfloat(number):
   """
   Determines whether a number should be displayed as an integer or float based on its value and returns the corrected value. This is a substitute for the way ActionScript 3 displayed numbers as strings.
   EX:
      1.05 should be displayed as a float
      1.00 should be displayed as an integer
   """
   if type(number) == str:
      number = float(number)
   elif type(number) == int:
      return number
   if number.is_integer():
      return int(number)
   else:
      return number
def strtobool(a:str):
   match a.lower():
      case "true":
         return True
      case "false":
         return False
def convertButton(*args):
   convertSave(inputfileentry.get(),inputfiletypecombo.get(),outputfileentry.get(),outputfiletypecombo.get())
def convertSave(inputfile,inputfiletype,outputfile,outputfiletype):
   message["text"]=""
   message["foreground"]="#FF1111"
   if inputfile in (None,"") or outputfile == (None,""):
      print("SaveConverter: Error: Input/Output file can not be \"None\" or empty")
      message["text"]="Error: Input/Output file can not be \"None\" or empty"
      return
   if inputfiletype == outputfiletype and inputfiletype != "detect":
      print("SaveConverter: Error: Input and Output file types can not be the same.")
      message["text"]="Error: Input and Output file types can not be the same."
      return
   if inputfile == outputfile:
      print("SaveConverter: Error: Input and Output files can not be the same.")
      message["text"]="Error: Input and Output files can not be the same."
      return
   match inputfiletype:
      case "xml":
         xml = xmletree.parse(inputfile).getroot() #Loads file directly as xml
      case "sol":
         xml = toXmlReturn(inputfile) #Converts SOL file to xml
      case "nim":
         xml = toXmlReturnNIM(inputfile) #Converts NIM file to xml
      case "detect":
         ext = inputfile.split(".")[-1].lower()
         match ext:
            case "xml":
               xml = xmletree.parse(inputfile).getroot() #Loads file directly as xml
            case "sol":
               xml = toXmlReturn(inputfile) #Converts SOL file to xml
            case "nim":
               xml = toXmlReturnNIM(inputfile) # Converts NIM to xml
            case _:
               print(f"Type Check: Error: Detected input file type {ext} is not a supported file type")
               message["text"]=f"Error: Detected input file type {ext} is not a supported file type"
               return
   if xml == None:
      print("File Loader: Error: Input save data is null. Try again")
      return
   match outputfiletype:
      case "xml":
         xmletree.indent(xml,space="\t")
         xml.write(outputfile,encoding="UTF-8",xml_declaration=True)
      case "sol":
         toSOL(None,outputfile,None,xml)
      case "nim":
         toNim(None,outputfile,None,xml)
      case "detect":
         ext = outputfile.split(".")[-1].lower()
         match ext:
            case "xml":
               try:
                  xmletree.indent(xml,space="\t")
                  xml.write(outputfile,encoding="UTF-8",xml_declaration=True)
               except:
                  print("File Saver: Error: Failed to save file")
                  message["text"]="Error: Failed to save file"
               else:
                  message["foreground"]="#11FF11"
                  message["text"]="Success"
            case "sol":
               toSOL(None,outputfile,None,xml)
            case "nim":
               toNim(None,outputfile,None,xml)
            case _:
               print(f"File Output: Error: Detected output file type {ext} is not a supported file type")
               message["text"]=f"Error: Detected output file type {ext} is not a supported file type"
               return
def toNim(inputfile,outputfile,xmlobject=None,xmlroot=None):
   try:
      so = {"data":toSOLReturn(inputfile,outputfile,xmlobject,xmlroot)}
      if so["data"] == None:
         raise NullData()
      byteData = amf3.ByteArray()
      byteData.writeObject(so)
      with open(outputfile,"wb") as f:
         f.write(byteData.getvalue())
      message["foreground"]="#11FF11"
      message["text"]="Success"
   except NullData:
      print("NIM File Saver: Error: Nim save file data is null. Try again")
      message["text"]="Error: File data is null"
   except:
      print("NIM File Saver: Error: Failed to convert file to type \"nim\"")
      message["text"]="Error: Failed to save file"
def solString(string):
   return "" if string in (None,"None","undefined") else str(string)
def solGetFileName(path:str|Path):
   if type(path) == str:
      match platform:
         case "Windows":
            templist = path.split("\\")[-1].split(".")
         case "Linux" | "Darwin":
            templist = path.split("/")[-1].split(".")
      templist.pop(-1)
      tempstr = ""
      for i in templist:
         if i == templist[-1]:
            tempstr += i
         else:
            tempstr += f"{i}."
      return tempstr
   else: #Is path object
      filename = path.resolve().name.split(".")
      if len(filename) == 1:
         return filename[0]
      elif len(filename) > 1:
         filename.pop()
         return ".".join(filename)
def toSOLReturn(inputfile,outputfile,xmlobject=None,xmlroot=None):
   try:
      if xmlroot != None:
         xmlfile = xmlroot
      elif xmlobject != None:
         xmlfile = xmlobject.getroot()
      else:
         xmlfile = xmletree.parse(inputfile).getroot()
      data = sol.SOL(solGetFileName(outputfile))
      if xmlfile.find("version") != None:
         data["versionNumber"] = xmlfile.find("version").find("original").text
         data["versionNumberPymin"] = xmlfile.find("version").find("port").text
      ltrack = xmlfile.find("track")
      data["track"] = [int(ltrack.find("currentState").text),int(ltrack.find("currentZone").text),int(ltrack.find("day").text),int(ltrack.find("hour").text),int(ltrack.find("currentDayCare").text),strtobool(ltrack.find("inDungeon").text),int(ltrack.find("currentDungeon").text),0.75]
      lstats = xmlfile.find("stats")
      data["stats"] = [int(lstats.find("strength").text),int(lstats.find("mentality").text),int(lstats.find("libido").text),int(lstats.find("sensitivity").text),int(lstats.find("HP").text),int(lstats.find("lust").text),int(lstats.find("coin").text),int(lstats.find("strMod").text),int(lstats.find("mentMod").text),int(lstats.find("libMod").text),int(lstats.find("senMod").text),int(lstats.find("hunger").text)]
      llevel = xmlfile.find("level")
      data["level"] = [int(llevel.find("SexP").text),int(llevel.find("levelUP").text),int(llevel.find("level").text),int(llevel.find("babyFactLevel").text),int(llevel.find("bodyBuildLevel").text),int(llevel.find("hyperHappyLevel").text),int(llevel.find("alchemistLevel").text),int(llevel.find("fetishMasterLevel").text),int(llevel.find("milkMaidLevel").text),int(llevel.find("shapeshiftyLevel").text),solString(llevel.find("shapeshiftyFirst").text),solString(llevel.find("shapeshiftySecond").text)]
      lmod = xmlfile.find("mod")
      data["mod"] = [int(lmod.find("runMod").text),int(lmod.find("rapeMod").text),repintorfloat(lmod.find("cumMod").text),repintorfloat(lmod.find("cockSizeMod").text),int(lmod.find("milkMod").text),int(lmod.find("carryMod").text),int(lmod.find("vagBellyMod").text),int(lmod.find("pregChanceMod").text),int(lmod.find("extraPregChance").text),int(lmod.find("pregTimeMod").text),int(lmod.find("enticeMod").text),int(lmod.find("milkHPMod").text),repintorfloat(lmod.find("vagSizeMod").text),repintorfloat(lmod.find("vagElastic").text),repintorfloat(lmod.find("changeMod").text),int(lmod.find("HPMod").text),repintorfloat(lmod.find("SexPMod").text),int(lmod.find("minLust").text),int(lmod.find("milkCap").text),int(lmod.find("coinMod").text),int(lmod.find("hipMod").text),int(lmod.find("buttMod").text),int(lmod.find("bellyMod").text),int(lmod.find("cockMoistMod").text),int(lmod.find("vagMoistMod").text),int(lmod.find("lockTail").text),int(lmod.find("lockFace").text),int(lmod.find("lockSkin").text),int(lmod.find("lockBreasts").text),int(lmod.find("lockEars").text),int(lmod.find("lockLegs").text),int(lmod.find("lockNipples").text),int(lmod.find("lockCock").text)]
      lquality = xmlfile.find("quality")
      data["quality"] = [int(lquality.find("gender").text),int(lquality.find("race").text),int(lquality.find("body").text),int(lquality.find("dominant").text),int(lquality.find("hips").text),int(lquality.find("butt").text),int(lquality.find("tallness").text),int(lquality.find("skinType").text),int(lquality.find("tail").text),int(lquality.find("ears").text),int(lquality.find("hair").text),int(lquality.find("hairColor").text),int(lquality.find("hairLength").text),int(lquality.find("legType").text),int(lquality.find("wings").text),int(lquality.find("faceType").text),int(lquality.find("skinColor").text)]
      lcock = xmlfile.find("cock")
      data["cock"] = [int(lcock.find("cockTotal").text),int(lcock.find("humanCocks").text),int(lcock.find("horseCocks").text),int(lcock.find("wolfCocks").text),int(lcock.find("catCocks").text),int(lcock.find("rabbitCocks").text),int(lcock.find("lizardCocks").text),int(lcock.find("cockSize").text),int(lcock.find("cockMoist").text),int(lcock.find("balls").text),int(lcock.find("ballSize").text),strtobool(lcock.find("showBalls").text),strtobool(lcock.find("knot").text),int(lcock.find("bugCocks").text)]
      if lcock.find("neuterizerHideBalls") != None:
         data["cock"].append(lcock.find("neuterizerHideBalls").text)
      lgirl = xmlfile.find("girl")
      data["girl"] = [int(lgirl.find("breastSize").text),int(lgirl.find("boobTotal").text),int(lgirl.find("nippleSize").text),strtobool(lgirl.find("udders").text),int(lgirl.find("udderSize").text),int(lgirl.find("teatSize").text),int(lgirl.find("clitSize").text),int(lgirl.find("vagTotal").text),int(lgirl.find("vagSize").text),int(lgirl.find("vagMoist").text),int(lgirl.find("vulvaSize").text),int(lgirl.find("nipType").text)]
      lgear = xmlfile.find("gear")
      data["gear"] = [int(lgear.find("attireTop").text),int(lgear.find("attireBot").text),int(lgear.find("weapon").text),]
      lstatus = xmlfile.find("status")
      data["status"] = [repintorfloat(lstatus.find("pregRate").text),int(lstatus.find("pregnancyTime").text),int(lstatus.find("pregStatus").text),int(lstatus.find("eggLaying").text),int(lstatus.find("eggMaxTime").text),int(lstatus.find("eggTime").text),int(lstatus.find("eggRate").text),int(lstatus.find("exhaustion").text),int(lstatus.find("exhaustionPenalty").text),int(lstatus.find("milkEngorgement").text),int(lstatus.find("milkEngorgementLevel").text),int(lstatus.find("udderEngorgement").text),int(lstatus.find("udderEngorgementLevel").text),int(lstatus.find("heat").text),int(lstatus.find("heatTime").text),int(lstatus.find("heatMaxTime").text),int(lstatus.find("lactation").text),int(lstatus.find("udderLactation").text),repintorfloat(lstatus.find("nipplePlay").text),repintorfloat(lstatus.find("udderPlay").text),int(lstatus.find("blueBalls").text),int(lstatus.find("teatPump").text),int(lstatus.find("nipPump").text),int(lstatus.find("cockPump").text),int(lstatus.find("clitPump").text),int(lstatus.find("vulvaPump").text),int(lstatus.find("masoPot").text),int(lstatus.find("sMasoPot").text),int(lstatus.find("babyFree").text),int(lstatus.find("charmTime").text),int(lstatus.find("pheromone").text),int(lstatus.find("eggceleratorTime").text),int(lstatus.find("eggceleratorDose").text),int(lstatus.find("bodyOil").text),int(lstatus.find("lustPenalty").text),int(lstatus.find("fertileGel").text),strtobool(lstatus.find("snuggleBall").text),int(lstatus.find("eggType").text),int(lstatus.find("milkSuppressant").text),int(lstatus.find("milkSuppressantLact").text),int(lstatus.find("milkSuppressantUdder").text),strtobool(lstatus.find("suppHarness").text),int(lstatus.find("fertilityStatueCurse").text),int(lstatus.find("plumpQuats").text),int(lstatus.find("lilaWetStatus").text),int(lstatus.find("cockSnakePreg").text),int(lstatus.find("milkCPoisonNip").text),int(lstatus.find("milkCPoisonUdd").text),int(lstatus.find("cockSnakeVenom").text)]
      laffinity = xmlfile.find("affinity")
      data["affinity"] = [int(laffinity.find("humanAffinity").text),int(laffinity.find("horseAffinity").text),int(laffinity.find("wolfAffinity").text),int(laffinity.find("catAffinity").text),int(laffinity.find("cowAffinity").text),int(laffinity.find("lizardAffinity").text),int(laffinity.find("rabbitAffinity").text),int(laffinity.find("fourBoobAffinity").text),int(laffinity.find("mouseAffinity").text),int(laffinity.find("birdAffinity").text),int(laffinity.find("pigAffinity").text),int(laffinity.find("twoBoobAffinity").text),int(laffinity.find("sixBoobAffinity").text),int(laffinity.find("eightBoobAffinity").text),int(laffinity.find("tenBoobAffinity").text),int(laffinity.find("cowTaurAffinity").text),int(laffinity.find("humanTaurAffinity").text),int(laffinity.find("skunkAffinity").text),int(laffinity.find("bugAffinity").text)]
      lrep = xmlfile.find("rep")
      data["rep"] = [int(lrep.find("lilaRep").text),int(lrep.find("lilaVulva").text),int(lrep.find("lilaMilk").text),int(lrep.find("lilaPreg").text),int(lrep.find("malonRep").text),int(lrep.find("malonPreg").text),int(lrep.find("malonChildren").text),int(lrep.find("mistressRep").text),int(lrep.find("jamieRep").text),int(lrep.find("jamieSize").text),int(lrep.find("jamieChildren").text),int(lrep.find("silRep").text),int(lrep.find("silPreg").text),int(lrep.find("silRate").text),int(lrep.find("silLay").text),int(lrep.find("silGrowthTime").text),strtobool(lrep.find("silTied").text),strtobool(lrep.find("lilaUB").text),strtobool(lrep.find("dairyFarmBrand").text),int(lrep.find("lilaWetness").text),strtobool(lrep.find("jamieButt").text),strtobool(lrep.find("jamieBreasts").text),strtobool(lrep.find("jamieHair").text)]
      lknowledge = xmlfile.find("knowledge")
      data["knowledge"] = [strtobool(lknowledge.find("foundSoftlik").text),strtobool(lknowledge.find("foundFirmshaft").text),strtobool(lknowledge.find("foundTieden").text),strtobool(lknowledge.find("foundSizCalit").text),strtobool(lknowledge.find("foundOviasis").text),strtobool(lknowledge.find("foundValley").text),strtobool(lknowledge.find("foundSanctuary").text)]
      lboss = xmlfile.find("boss")
      data["boss"] = [strtobool(lboss.find("defeatedMinotaur").text),strtobool(lboss.find("defeatedFreakyGirl").text),strtobool(lboss.find("defeatedSuccubus").text)]
      lknowsimplealchemy = xmlfile.find("knowSimpleAlchemy")
      data["knowSimpleAlchemy"] = [strtobool(lknowsimplealchemy.find("knowLustDraft").text),strtobool(lknowsimplealchemy.find("knowRejuvPot").text),strtobool(lknowsimplealchemy.find("knowExpPreg").text),strtobool(lknowsimplealchemy.find("knowBallSwell").text),strtobool(lknowsimplealchemy.find("knowMaleEnhance").text)]
      lknowadvancedalchemy = xmlfile.find("knowAdvancedAlchemy")
      data["knowAdvancedAlchemy"] = [strtobool(lknowadvancedalchemy.find("knowSLustDraft").text),strtobool(lknowadvancedalchemy.find("knowSRejuvPot").text),strtobool(lknowadvancedalchemy.find("knowSExpPreg").text),strtobool(lknowadvancedalchemy.find("knowSBallSwell").text),strtobool(lknowadvancedalchemy.find("knowGenSwap").text),strtobool(lknowadvancedalchemy.find("knowMasoPot").text),strtobool(lknowadvancedalchemy.find("knowBabyFree").text),strtobool(lknowadvancedalchemy.find("knowPotPot").text),strtobool(lknowadvancedalchemy.find("knowMilkSuppress").text)]
      lknowcomplexalchemy = xmlfile.find("knowComplexAlchemy")
      data["knowComplexAlchemy"] = [strtobool(lknowcomplexalchemy.find("knowSGenSwap").text),strtobool(lknowcomplexalchemy.find("knowSMasoPot").text),strtobool(lknowcomplexalchemy.find("knowSBabyFree").text),strtobool(lknowcomplexalchemy.find("knowSPotPot").text),strtobool(lknowcomplexalchemy.find("knowPussJuice").text),strtobool(lknowcomplexalchemy.find("knowPheromone").text),strtobool(lknowcomplexalchemy.find("knowBazoomba").text)]
      lmajorfetish = xmlfile.find("majorFetish")
      data["majorFetish"] = [repintorfloat(lmajorfetish.find("maleFetish").text),repintorfloat(lmajorfetish.find("femaleFetish").text),repintorfloat(lmajorfetish.find("hermFetish").text),repintorfloat(lmajorfetish.find("narcissistFetish").text),repintorfloat(lmajorfetish.find("dependentFetish").text)]
      lmoderatefetish = xmlfile.find("moderateFetish")
      data["moderateFetish"] = [repintorfloat(lmoderatefetish.find("dominantFetish").text),repintorfloat(lmoderatefetish.find("submissiveFetish").text),repintorfloat(lmoderatefetish.find("lboobFetish").text),repintorfloat(lmoderatefetish.find("sboobFetish").text),repintorfloat(lmoderatefetish.find("furryFetish").text),repintorfloat(lmoderatefetish.find("scalyFetish").text),repintorfloat(lmoderatefetish.find("smoothyFetish").text)]
      lminorfetish = xmlfile.find("minorFetish")
      data["minorFetish"] = [repintorfloat(lminorfetish.find("pregnancyFetish").text),repintorfloat(lminorfetish.find("bestialityFetish").text),repintorfloat(lminorfetish.find("milkFetish").text),repintorfloat(lminorfetish.find("sizeFetish").text),repintorfloat(lminorfetish.find("unbirthingFetish").text),repintorfloat(lminorfetish.find("ovipositionFetish").text),repintorfloat(lminorfetish.find("toyFetish").text),repintorfloat(lminorfetish.find("hyperFetish").text)]
      lkid = xmlfile.find("kid")
      data["kid"] = [int(lkid.find("humanChildren").text),int(lkid.find("equanChildren").text),int(lkid.find("lupanChildren").text),int(lkid.find("felinChildren").text),int(lkid.find("cowChildren").text),int(lkid.find("lizanChildren").text),int(lkid.find("lizanEggs").text),int(lkid.find("bunnionChildren").text),int(lkid.find("wolfPupChildren").text),int(lkid.find("miceChildren").text),int(lkid.find("birdEggs").text),int(lkid.find("birdChildren").text),int(lkid.find("pigChildren").text),int(lkid.find("calfChildren").text),int(lkid.find("bugEggs").text),int(lkid.find("bugChildren").text),int(lkid.find("skunkChildren").text),int(lkid.find("minotaurChildren").text),int(lkid.find("freakyGirlChildren").text)]
      data["trav"] = []
      tba = []
      tbsa = []
      tsa = []
      tssa = []
      lb = xmlfile.find("bag")
      lbs = xmlfile.find("bagStack")
      ls = xmlfile.find("stash")
      lss = xmlfile.find("stashStack")
      for i in range(0,27):
         tba.append(int(lb.find(f"slot{i}").text))
         tbsa.append(int(lbs.find(f"slot{i}").text))
         tsa.append(int(ls.find(f"slot{i}").text))
         tssa.append(int(lss.find(f"slot{i}").text))
      data["bagSave"] = tba
      data["bagStackSave"] = tbsa
      data["stashSave"] = tsa
      data["stashStackSave"] = tssa
      tpa = []
      lp = xmlfile.find("preg")
      i = 0
      while i < len(lp):
         tpa.append(strtobool(lp.find(f"i{i}").text))
         tpa.append(int(lp.find(f"i{i+1}").text))
         tpa.append(int(lp.find(f"i{i+2}").text))
         tpa.append(int(lp.find(f"i{i+3}").text))
         tpa.append(int(lp.find(f"i{i+4}").text))
         i += 5
      data["pregSave"] = tpa
      return data
   except:
      print("SOL File Converter: Error: Failed to convert file")
      message["text"]="Error"
def toSOL(inputfile,outputfile,xmlobject=None,xmlroot=None):
   try:
      if xmlroot != None:
         xmlfile = xmlroot
      elif xmlobject != None:
         xmlfile = xmlobject.getroot()
      else:
         xmlfile = xmletree.parse(inputfile).getroot()
      data = sol.SOL(solGetFileName(outputfile))
      if xmlfile.find("version") != None:
         data["versionNumber"] = xmlfile.find("version").find("original").text
         data["versionNumberPymin"] = xmlfile.find("version").find("port").text
      ltrack = xmlfile.find("track")
      data["track"] = [int(ltrack.find("currentState").text),int(ltrack.find("currentZone").text),int(ltrack.find("day").text),int(ltrack.find("hour").text),int(ltrack.find("currentDayCare").text),strtobool(ltrack.find("inDungeon").text),int(ltrack.find("currentDungeon").text),0.75]
      lstats = xmlfile.find("stats")
      data["stats"] = [int(lstats.find("strength").text),int(lstats.find("mentality").text),int(lstats.find("libido").text),int(lstats.find("sensitivity").text),int(lstats.find("HP").text),int(lstats.find("lust").text),int(lstats.find("coin").text),int(lstats.find("strMod").text),int(lstats.find("mentMod").text),int(lstats.find("libMod").text),int(lstats.find("senMod").text),int(lstats.find("hunger").text)]
      llevel = xmlfile.find("level")
      data["level"] = [int(llevel.find("SexP").text),int(llevel.find("levelUP").text),int(llevel.find("level").text),int(llevel.find("babyFactLevel").text),int(llevel.find("bodyBuildLevel").text),int(llevel.find("hyperHappyLevel").text),int(llevel.find("alchemistLevel").text),int(llevel.find("fetishMasterLevel").text),int(llevel.find("milkMaidLevel").text),int(llevel.find("shapeshiftyLevel").text),solString(llevel.find("shapeshiftyFirst").text),solString(llevel.find("shapeshiftySecond").text)]
      lmod = xmlfile.find("mod")
      data["mod"] = [int(lmod.find("runMod").text),int(lmod.find("rapeMod").text),repintorfloat(lmod.find("cumMod").text),repintorfloat(lmod.find("cockSizeMod").text),int(lmod.find("milkMod").text),int(lmod.find("carryMod").text),int(lmod.find("vagBellyMod").text),int(lmod.find("pregChanceMod").text),int(lmod.find("extraPregChance").text),int(lmod.find("pregTimeMod").text),int(lmod.find("enticeMod").text),int(lmod.find("milkHPMod").text),repintorfloat(lmod.find("vagSizeMod").text),repintorfloat(lmod.find("vagElastic").text),repintorfloat(lmod.find("changeMod").text),int(lmod.find("HPMod").text),repintorfloat(lmod.find("SexPMod").text),int(lmod.find("minLust").text),int(lmod.find("milkCap").text),int(lmod.find("coinMod").text),int(lmod.find("hipMod").text),int(lmod.find("buttMod").text),int(lmod.find("bellyMod").text),int(lmod.find("cockMoistMod").text),int(lmod.find("vagMoistMod").text),int(lmod.find("lockTail").text),int(lmod.find("lockFace").text),int(lmod.find("lockSkin").text),int(lmod.find("lockBreasts").text),int(lmod.find("lockEars").text),int(lmod.find("lockLegs").text),int(lmod.find("lockNipples").text),int(lmod.find("lockCock").text)]
      lquality = xmlfile.find("quality")
      data["quality"] = [int(lquality.find("gender").text),int(lquality.find("race").text),int(lquality.find("body").text),int(lquality.find("dominant").text),int(lquality.find("hips").text),int(lquality.find("butt").text),int(lquality.find("tallness").text),int(lquality.find("skinType").text),int(lquality.find("tail").text),int(lquality.find("ears").text),int(lquality.find("hair").text),int(lquality.find("hairColor").text),int(lquality.find("hairLength").text),int(lquality.find("legType").text),int(lquality.find("wings").text),int(lquality.find("faceType").text),int(lquality.find("skinColor").text)]
      lcock = xmlfile.find("cock")
      data["cock"] = [int(lcock.find("cockTotal").text),int(lcock.find("humanCocks").text),int(lcock.find("horseCocks").text),int(lcock.find("wolfCocks").text),int(lcock.find("catCocks").text),int(lcock.find("rabbitCocks").text),int(lcock.find("lizardCocks").text),int(lcock.find("cockSize").text),int(lcock.find("cockMoist").text),int(lcock.find("balls").text),int(lcock.find("ballSize").text),strtobool(lcock.find("showBalls").text),strtobool(lcock.find("knot").text),int(lcock.find("bugCocks").text)]
      if lcock.find("neuterizerHideBalls") != None:
         data["cock"].append(lcock.find("neuterizerHideBalls").text)
      lgirl = xmlfile.find("girl")
      data["girl"] = [int(lgirl.find("breastSize").text),int(lgirl.find("boobTotal").text),int(lgirl.find("nippleSize").text),strtobool(lgirl.find("udders").text),int(lgirl.find("udderSize").text),int(lgirl.find("teatSize").text),int(lgirl.find("clitSize").text),int(lgirl.find("vagTotal").text),int(lgirl.find("vagSize").text),int(lgirl.find("vagMoist").text),int(lgirl.find("vulvaSize").text),int(lgirl.find("nipType").text)]
      lgear = xmlfile.find("gear")
      data["gear"] = [int(lgear.find("attireTop").text),int(lgear.find("attireBot").text),int(lgear.find("weapon").text),]
      lstatus = xmlfile.find("status")
      data["status"] = [repintorfloat(lstatus.find("pregRate").text),int(lstatus.find("pregnancyTime").text),int(lstatus.find("pregStatus").text),int(lstatus.find("eggLaying").text),int(lstatus.find("eggMaxTime").text),int(lstatus.find("eggTime").text),int(lstatus.find("eggRate").text),int(lstatus.find("exhaustion").text),int(lstatus.find("exhaustionPenalty").text),int(lstatus.find("milkEngorgement").text),int(lstatus.find("milkEngorgementLevel").text),int(lstatus.find("udderEngorgement").text),int(lstatus.find("udderEngorgementLevel").text),int(lstatus.find("heat").text),int(lstatus.find("heatTime").text),int(lstatus.find("heatMaxTime").text),int(lstatus.find("lactation").text),int(lstatus.find("udderLactation").text),repintorfloat(lstatus.find("nipplePlay").text),repintorfloat(lstatus.find("udderPlay").text),int(lstatus.find("blueBalls").text),int(lstatus.find("teatPump").text),int(lstatus.find("nipPump").text),int(lstatus.find("cockPump").text),int(lstatus.find("clitPump").text),int(lstatus.find("vulvaPump").text),int(lstatus.find("masoPot").text),int(lstatus.find("sMasoPot").text),int(lstatus.find("babyFree").text),int(lstatus.find("charmTime").text),int(lstatus.find("pheromone").text),int(lstatus.find("eggceleratorTime").text),int(lstatus.find("eggceleratorDose").text),int(lstatus.find("bodyOil").text),int(lstatus.find("lustPenalty").text),int(lstatus.find("fertileGel").text),strtobool(lstatus.find("snuggleBall").text),int(lstatus.find("eggType").text),int(lstatus.find("milkSuppressant").text),int(lstatus.find("milkSuppressantLact").text),int(lstatus.find("milkSuppressantUdder").text),strtobool(lstatus.find("suppHarness").text),int(lstatus.find("fertilityStatueCurse").text),int(lstatus.find("plumpQuats").text),int(lstatus.find("lilaWetStatus").text),int(lstatus.find("cockSnakePreg").text),int(lstatus.find("milkCPoisonNip").text),int(lstatus.find("milkCPoisonUdd").text),int(lstatus.find("cockSnakeVenom").text)]
      laffinity = xmlfile.find("affinity")
      data["affinity"] = [int(laffinity.find("humanAffinity").text),int(laffinity.find("horseAffinity").text),int(laffinity.find("wolfAffinity").text),int(laffinity.find("catAffinity").text),int(laffinity.find("cowAffinity").text),int(laffinity.find("lizardAffinity").text),int(laffinity.find("rabbitAffinity").text),int(laffinity.find("fourBoobAffinity").text),int(laffinity.find("mouseAffinity").text),int(laffinity.find("birdAffinity").text),int(laffinity.find("pigAffinity").text),int(laffinity.find("twoBoobAffinity").text),int(laffinity.find("sixBoobAffinity").text),int(laffinity.find("eightBoobAffinity").text),int(laffinity.find("tenBoobAffinity").text),int(laffinity.find("cowTaurAffinity").text),int(laffinity.find("humanTaurAffinity").text),int(laffinity.find("skunkAffinity").text),int(laffinity.find("bugAffinity").text)]
      lrep = xmlfile.find("rep")
      data["rep"] = [int(lrep.find("lilaRep").text),int(lrep.find("lilaVulva").text),int(lrep.find("lilaMilk").text),int(lrep.find("lilaPreg").text),int(lrep.find("malonRep").text),int(lrep.find("malonPreg").text),int(lrep.find("malonChildren").text),int(lrep.find("mistressRep").text),int(lrep.find("jamieRep").text),int(lrep.find("jamieSize").text),int(lrep.find("jamieChildren").text),int(lrep.find("silRep").text),int(lrep.find("silPreg").text),int(lrep.find("silRate").text),int(lrep.find("silLay").text),int(lrep.find("silGrowthTime").text),strtobool(lrep.find("silTied").text),strtobool(lrep.find("lilaUB").text),strtobool(lrep.find("dairyFarmBrand").text),int(lrep.find("lilaWetness").text),strtobool(lrep.find("jamieButt").text),strtobool(lrep.find("jamieBreasts").text),strtobool(lrep.find("jamieHair").text)]
      lknowledge = xmlfile.find("knowledge")
      data["knowledge"] = [strtobool(lknowledge.find("foundSoftlik").text),strtobool(lknowledge.find("foundFirmshaft").text),strtobool(lknowledge.find("foundTieden").text),strtobool(lknowledge.find("foundSizCalit").text),strtobool(lknowledge.find("foundOviasis").text),strtobool(lknowledge.find("foundValley").text),strtobool(lknowledge.find("foundSanctuary").text)]
      lboss = xmlfile.find("boss")
      data["boss"] = [strtobool(lboss.find("defeatedMinotaur").text),strtobool(lboss.find("defeatedFreakyGirl").text),strtobool(lboss.find("defeatedSuccubus").text)]
      lknowsimplealchemy = xmlfile.find("knowSimpleAlchemy")
      data["knowSimpleAlchemy"] = [strtobool(lknowsimplealchemy.find("knowLustDraft").text),strtobool(lknowsimplealchemy.find("knowRejuvPot").text),strtobool(lknowsimplealchemy.find("knowExpPreg").text),strtobool(lknowsimplealchemy.find("knowBallSwell").text),strtobool(lknowsimplealchemy.find("knowMaleEnhance").text)]
      lknowadvancedalchemy = xmlfile.find("knowAdvancedAlchemy")
      data["knowAdvancedAlchemy"] = [strtobool(lknowadvancedalchemy.find("knowSLustDraft").text),strtobool(lknowadvancedalchemy.find("knowSRejuvPot").text),strtobool(lknowadvancedalchemy.find("knowSExpPreg").text),strtobool(lknowadvancedalchemy.find("knowSBallSwell").text),strtobool(lknowadvancedalchemy.find("knowGenSwap").text),strtobool(lknowadvancedalchemy.find("knowMasoPot").text),strtobool(lknowadvancedalchemy.find("knowBabyFree").text),strtobool(lknowadvancedalchemy.find("knowPotPot").text),strtobool(lknowadvancedalchemy.find("knowMilkSuppress").text)]
      lknowcomplexalchemy = xmlfile.find("knowComplexAlchemy")
      data["knowComplexAlchemy"] = [strtobool(lknowcomplexalchemy.find("knowSGenSwap").text),strtobool(lknowcomplexalchemy.find("knowSMasoPot").text),strtobool(lknowcomplexalchemy.find("knowSBabyFree").text),strtobool(lknowcomplexalchemy.find("knowSPotPot").text),strtobool(lknowcomplexalchemy.find("knowPussJuice").text),strtobool(lknowcomplexalchemy.find("knowPheromone").text),strtobool(lknowcomplexalchemy.find("knowBazoomba").text)]
      lmajorfetish = xmlfile.find("majorFetish")
      data["majorFetish"] = [repintorfloat(lmajorfetish.find("maleFetish").text),repintorfloat(lmajorfetish.find("femaleFetish").text),repintorfloat(lmajorfetish.find("hermFetish").text),repintorfloat(lmajorfetish.find("narcissistFetish").text),repintorfloat(lmajorfetish.find("dependentFetish").text)]
      lmoderatefetish = xmlfile.find("moderateFetish")
      data["moderateFetish"] = [repintorfloat(lmoderatefetish.find("dominantFetish").text),repintorfloat(lmoderatefetish.find("submissiveFetish").text),repintorfloat(lmoderatefetish.find("lboobFetish").text),repintorfloat(lmoderatefetish.find("sboobFetish").text),repintorfloat(lmoderatefetish.find("furryFetish").text),repintorfloat(lmoderatefetish.find("scalyFetish").text),repintorfloat(lmoderatefetish.find("smoothyFetish").text)]
      lminorfetish = xmlfile.find("minorFetish")
      data["minorFetish"] = [repintorfloat(lminorfetish.find("pregnancyFetish").text),repintorfloat(lminorfetish.find("bestialityFetish").text),repintorfloat(lminorfetish.find("milkFetish").text),repintorfloat(lminorfetish.find("sizeFetish").text),repintorfloat(lminorfetish.find("unbirthingFetish").text),repintorfloat(lminorfetish.find("ovipositionFetish").text),repintorfloat(lminorfetish.find("toyFetish").text),repintorfloat(lminorfetish.find("hyperFetish").text)]
      lkid = xmlfile.find("kid")
      data["kid"] = [int(lkid.find("humanChildren").text),int(lkid.find("equanChildren").text),int(lkid.find("lupanChildren").text),int(lkid.find("felinChildren").text),int(lkid.find("cowChildren").text),int(lkid.find("lizanChildren").text),int(lkid.find("lizanEggs").text),int(lkid.find("bunnionChildren").text),int(lkid.find("wolfPupChildren").text),int(lkid.find("miceChildren").text),int(lkid.find("birdEggs").text),int(lkid.find("birdChildren").text),int(lkid.find("pigChildren").text),int(lkid.find("calfChildren").text),int(lkid.find("bugEggs").text),int(lkid.find("bugChildren").text),int(lkid.find("skunkChildren").text),int(lkid.find("minotaurChildren").text),int(lkid.find("freakyGirlChildren").text)]
      data["trav"] = []
      tba = []
      tbsa = []
      tsa = []
      tssa = []
      lb = xmlfile.find("bag")
      lbs = xmlfile.find("bagStack")
      ls = xmlfile.find("stash")
      lss = xmlfile.find("stashStack")
      for i in range(0,27):
         tba.append(int(lb.find(f"slot{i}").text))
         tbsa.append(int(lbs.find(f"slot{i}").text))
         tsa.append(int(ls.find(f"slot{i}").text))
         tssa.append(int(lss.find(f"slot{i}").text))
      data["bagSave"] = tba
      data["bagStackSave"] = tbsa
      data["stashSave"] = tsa
      data["stashStackSave"] = tssa
      tpa = []
      lp = xmlfile.find("preg")
      i = 0
      while i < len(lp):
         tpa.append(strtobool(lp.find(f"i{i}").text))
         tpa.append(int(lp.find(f"i{i+1}").text))
         tpa.append(int(lp.find(f"i{i+2}").text))
         tpa.append(int(lp.find(f"i{i+3}").text))
         tpa.append(int(lp.find(f"i{i+4}").text))
         i += 5
      data["pregSave"] = tpa
      sol.save(data,str(outputfile),AMF3)
      message["foreground"]="#11FF11"
      message["text"]="Success"
   except:
      print("SOL File Saver: Error: Failed to convert file")
      message["text"]="Error: Failed to convert file"
def toXmlReturn(inputfile):
   try:
      so = sol.load(str(inputfile))
      strack = so["track"]
      sstats = so["stats"]
      slevel = so["level"]
      smod = so["mod"]
      squality = so["quality"]
      scock = so["cock"]
      sgirl = so["girl"]
      sgear = so["gear"]
      sstatus = so["status"]
      saffinity = so["affinity"]
      srep = so["rep"]
      sknowledge = so["knowledge"]
      sboss = so["boss"]
      sknowSimpleAlchemy = so["knowSimpleAlchemy"]
      sknowAdvancedAlchemy = so["knowAdvancedAlchemy"]
      sknowComplexAlchemy = so["knowComplexAlchemy"]
      smajorFetish = so["majorFetish"]
      smoderateFetish = so["moderateFetish"]
      sminorFetish = so["minorFetish"]
      skid = so["kid"]
      trav = so["trav"]
      string = f"<data><track><currentState>{strack[0]}</currentState><currentZone>{strack[1]}</currentZone><day>{strack[2]}</day><hour>{strack[3]}</hour><currentDayCare>{strack[4]}</currentDayCare><inDungeon>{strack[5]}</inDungeon><currentDungeon>{strack[6]}</currentDungeon><v7>{strack[7]}</v7></track>"
      if 'versionNumber' in so.keys():
         string += f"<version><original>{so['versionNumber']}</original>"
         if 'versionNumberPymin' in so.keys():
            string += f"<port>{so['versionNumberPymin']}</port>"
         string += "</version>"
      string += f"<stats><strength>{sstats[0]}</strength><mentality>{sstats[1]}</mentality><libido>{sstats[2]}</libido><sensitivity>{sstats[3]}</sensitivity><HP>{sstats[4]}</HP><lust>{sstats[5]}</lust><coin>{sstats[6]}</coin><strMod>{sstats[7]}</strMod><mentMod>{sstats[8]}</mentMod><libMod>{sstats[9]}</libMod><senMod>{sstats[10]}</senMod><hunger>{sstats[11]}</hunger></stats><level><SexP>{slevel[0]}</SexP><levelUP>{slevel[1]}</levelUP><level>{slevel[2]}</level><babyFactLevel>{slevel[3]}</babyFactLevel><bodyBuildLevel>{slevel[4]}</bodyBuildLevel><hyperHappyLevel>{slevel[5]}</hyperHappyLevel><alchemistLevel>{slevel[6]}</alchemistLevel><fetishMasterLevel>{slevel[7]}</fetishMasterLevel><milkMaidLevel>{slevel[8]}</milkMaidLevel><shapeshiftyLevel>{slevel[9]}</shapeshiftyLevel><shapeshiftyFirst>{slevel[10]}</shapeshiftyFirst><shapeshiftySecond>{slevel[11]}</shapeshiftySecond></level><mod><runMod>{smod[0]}</runMod><rapeMod>{smod[1]}</rapeMod><cumMod>{smod[2]}</cumMod><cockSizeMod>{smod[3]}</cockSizeMod><milkMod>{smod[4]}</milkMod><carryMod>{smod[5]}</carryMod><vagBellyMod>{smod[6]}</vagBellyMod><pregChanceMod>{smod[7]}</pregChanceMod><extraPregChance>{smod[8]}</extraPregChance><pregTimeMod>{smod[9]}</pregTimeMod><enticeMod>{smod[10]}</enticeMod><milkHPMod>{smod[11]}</milkHPMod><vagSizeMod>{smod[12]}</vagSizeMod><vagElastic>{smod[13]}</vagElastic><changeMod>{smod[14]}</changeMod><HPMod>{smod[15]}</HPMod><SexPMod>{smod[16]}</SexPMod><minLust>{smod[17]}</minLust><milkCap>{smod[18]}</milkCap><coinMod>{smod[19]}</coinMod><hipMod>{smod[20]}</hipMod><buttMod>{smod[21]}</buttMod><bellyMod>{smod[22]}</bellyMod><cockMoistMod>{smod[23]}</cockMoistMod><vagMoistMod>{smod[24]}</vagMoistMod><lockTail>{smod[25]}</lockTail><lockFace>{smod[26]}</lockFace><lockSkin>{smod[27]}</lockSkin><lockBreasts>{smod[28]}</lockBreasts><lockEars>{smod[29]}</lockEars><lockLegs>{smod[30]}</lockLegs><lockNipples>{smod[31]}</lockNipples><lockCock>{smod[32]}</lockCock></mod><quality><gender>{squality[0]}</gender><race>{squality[1]}</race><body>{squality[2]}</body><dominant>{squality[3]}</dominant><hips>{squality[4]}</hips><butt>{squality[5]}</butt><tallness>{squality[6]}</tallness><skinType>{squality[7]}</skinType><tail>{squality[8]}</tail><ears>{squality[9]}</ears><hair>{squality[10]}</hair><hairColor>{squality[11]}</hairColor><hairLength>{squality[12]}</hairLength><legType>{squality[13]}</legType><wings>{squality[14]}</wings><faceType>{squality[15]}</faceType><skinColor>{squality[16]}</skinColor></quality><cock><cockTotal>{scock[0]}</cockTotal><humanCocks>{scock[1]}</humanCocks><horseCocks>{scock[2]}</horseCocks><wolfCocks>{scock[3]}</wolfCocks><catCocks>{scock[4]}</catCocks><rabbitCocks>{scock[5]}</rabbitCocks><lizardCocks>{scock[6]}</lizardCocks><cockSize>{scock[7]}</cockSize><cockMoist>{scock[8]}</cockMoist><balls>{scock[9]}</balls><ballSize>{scock[10]}</ballSize><showBalls>{scock[11]}</showBalls><knot>{scock[12]}</knot><bugCocks>{scock[13]}</bugCocks>"
      if len(scock) == 15:
         string += f"<neuterizerHideBalls>{scock[14]}</neuterizerHideBalls>"
      string += f"</cock><girl><breastSize>{sgirl[0]}</breastSize><boobTotal>{sgirl[1]}</boobTotal><nippleSize>{sgirl[2]}</nippleSize><udders>{sgirl[3]}</udders><udderSize>{sgirl[4]}</udderSize><teatSize>{sgirl[5]}</teatSize><clitSize>{sgirl[6]}</clitSize><vagTotal>{sgirl[7]}</vagTotal><vagSize>{sgirl[8]}</vagSize><vagMoist>{sgirl[9]}</vagMoist><vulvaSize>{sgirl[10]}</vulvaSize><nipType>{sgirl[11]}</nipType></girl><gear><attireTop>{sgear[0]}</attireTop><attireBot>{sgear[1]}</attireBot><weapon>{sgear[2]}</weapon></gear><status><pregRate>{sstatus[0]}</pregRate><pregnancyTime>{sstatus[1]}</pregnancyTime><pregStatus>{sstatus[2]}</pregStatus><eggLaying>{sstatus[3]}</eggLaying><eggMaxTime>{sstatus[4]}</eggMaxTime><eggTime>{sstatus[5]}</eggTime><eggRate>{sstatus[6]}</eggRate><exhaustion>{sstatus[7]}</exhaustion><exhaustionPenalty>{sstatus[8]}</exhaustionPenalty><milkEngorgement>{sstatus[9]}</milkEngorgement><milkEngorgementLevel>{sstatus[10]}</milkEngorgementLevel><udderEngorgement>{sstatus[11]}</udderEngorgement><udderEngorgementLevel>{sstatus[12]}</udderEngorgementLevel><heat>{sstatus[13]}</heat><heatTime>{sstatus[14]}</heatTime><heatMaxTime>{sstatus[15]}</heatMaxTime><lactation>{sstatus[16]}</lactation><udderLactation>{sstatus[17]}</udderLactation><nipplePlay>{sstatus[18]}</nipplePlay><udderPlay>{sstatus[19]}</udderPlay><blueBalls>{sstatus[20]}</blueBalls><teatPump>{sstatus[21]}</teatPump><nipPump>{sstatus[22]}</nipPump><cockPump>{sstatus[23]}</cockPump><clitPump>{sstatus[24]}</clitPump><vulvaPump>{sstatus[25]}</vulvaPump><masoPot>{sstatus[26]}</masoPot><sMasoPot>{sstatus[27]}</sMasoPot><babyFree>{sstatus[28]}</babyFree><charmTime>{sstatus[29]}</charmTime><pheromone>{sstatus[30]}</pheromone><eggceleratorTime>{sstatus[31]}</eggceleratorTime><eggceleratorDose>{sstatus[32]}</eggceleratorDose><bodyOil>{sstatus[33]}</bodyOil><lustPenalty>{sstatus[34]}</lustPenalty><fertileGel>{sstatus[35]}</fertileGel><snuggleBall>{sstatus[36]}</snuggleBall><eggType>{sstatus[37]}</eggType><milkSuppressant>{sstatus[38]}</milkSuppressant><milkSuppressantLact>{sstatus[39]}</milkSuppressantLact><milkSuppressantUdder>{sstatus[40]}</milkSuppressantUdder><suppHarness>{sstatus[41]}</suppHarness><fertilityStatueCurse>{sstatus[42]}</fertilityStatueCurse><plumpQuats>{sstatus[43]}</plumpQuats><lilaWetStatus>{sstatus[44]}</lilaWetStatus><cockSnakePreg>{sstatus[45]}</cockSnakePreg><milkCPoisonNip>{sstatus[46]}</milkCPoisonNip><milkCPoisonUdd>{sstatus[47]}</milkCPoisonUdd><cockSnakeVenom>{sstatus[48]}</cockSnakeVenom></status><affinity><humanAffinity>{saffinity[0]}</humanAffinity><horseAffinity>{saffinity[1]}</horseAffinity><wolfAffinity>{saffinity[2]}</wolfAffinity><catAffinity>{saffinity[3]}</catAffinity><cowAffinity>{saffinity[4]}</cowAffinity><lizardAffinity>{saffinity[5]}</lizardAffinity><rabbitAffinity>{saffinity[6]}</rabbitAffinity><fourBoobAffinity>{saffinity[7]}</fourBoobAffinity><mouseAffinity>{saffinity[8]}</mouseAffinity><birdAffinity>{saffinity[9]}</birdAffinity><pigAffinity>{saffinity[10]}</pigAffinity><twoBoobAffinity>{saffinity[11]}</twoBoobAffinity><sixBoobAffinity>{saffinity[12]}</sixBoobAffinity><eightBoobAffinity>{saffinity[13]}</eightBoobAffinity><tenBoobAffinity>{saffinity[14]}</tenBoobAffinity><cowTaurAffinity>{saffinity[15]}</cowTaurAffinity><humanTaurAffinity>{saffinity[16]}</humanTaurAffinity><skunkAffinity>{saffinity[17]}</skunkAffinity><bugAffinity>{saffinity[18]}</bugAffinity></affinity><rep><lilaRep>{srep[0]}</lilaRep><lilaVulva>{srep[1]}</lilaVulva><lilaMilk>{srep[2]}</lilaMilk><lilaPreg>{srep[3]}</lilaPreg><malonRep>{srep[4]}</malonRep><malonPreg>{srep[5]}</malonPreg><malonChildren>{srep[6]}</malonChildren><mistressRep>{srep[7]}</mistressRep><jamieRep>{srep[8]}</jamieRep><jamieSize>{srep[9]}</jamieSize><jamieChildren>{srep[10]}</jamieChildren><silRep>{srep[11]}</silRep><silPreg>{srep[12]}</silPreg><silRate>{srep[13]}</silRate><silLay>{srep[14]}</silLay><silGrowthTime>{srep[15]}</silGrowthTime><silTied>{srep[16]}</silTied><lilaUB>{srep[17]}</lilaUB><dairyFarmBrand>{srep[18]}</dairyFarmBrand><lilaWetness>{srep[19]}</lilaWetness><jamieButt>{srep[20]}</jamieButt><jamieBreasts>{srep[21]}</jamieBreasts><jamieHair>{srep[22]}</jamieHair></rep><knowledge><foundSoftlik>{sknowledge[0]}</foundSoftlik><foundFirmshaft>{sknowledge[1]}</foundFirmshaft><foundTieden>{sknowledge[2]}</foundTieden><foundSizCalit>{sknowledge[3]}</foundSizCalit><foundOviasis>{sknowledge[4]}</foundOviasis><foundValley>{sknowledge[5]}</foundValley><foundSanctuary>{sknowledge[6]}</foundSanctuary></knowledge><boss><defeatedMinotaur>{sboss[0]}</defeatedMinotaur><defeatedFreakyGirl>{sboss[1]}</defeatedFreakyGirl><defeatedSuccubus>{sboss[2]}</defeatedSuccubus></boss><knowSimpleAlchemy><knowLustDraft>{sknowSimpleAlchemy[0]}</knowLustDraft><knowRejuvPot>{sknowSimpleAlchemy[1]}</knowRejuvPot><knowExpPreg>{sknowSimpleAlchemy[2]}</knowExpPreg><knowBallSwell>{sknowSimpleAlchemy[3]}</knowBallSwell><knowMaleEnhance>{sknowSimpleAlchemy[4]}</knowMaleEnhance></knowSimpleAlchemy><knowAdvancedAlchemy><knowSLustDraft>{sknowAdvancedAlchemy[0]}</knowSLustDraft><knowSRejuvPot>{sknowAdvancedAlchemy[1]}</knowSRejuvPot><knowSExpPreg>{sknowAdvancedAlchemy[2]}</knowSExpPreg><knowSBallSwell>{sknowAdvancedAlchemy[3]}</knowSBallSwell><knowGenSwap>{sknowAdvancedAlchemy[4]}</knowGenSwap><knowMasoPot>{sknowAdvancedAlchemy[5]}</knowMasoPot><knowBabyFree>{sknowAdvancedAlchemy[6]}</knowBabyFree><knowPotPot>{sknowAdvancedAlchemy[7]}</knowPotPot><knowMilkSuppress>{sknowAdvancedAlchemy[8]}</knowMilkSuppress></knowAdvancedAlchemy><knowComplexAlchemy><knowSGenSwap>{sknowComplexAlchemy[0]}</knowSGenSwap><knowSMasoPot>{sknowComplexAlchemy[1]}</knowSMasoPot><knowSBabyFree>{sknowComplexAlchemy[2]}</knowSBabyFree><knowSPotPot>{sknowComplexAlchemy[3]}</knowSPotPot><knowPussJuice>{sknowComplexAlchemy[4]}</knowPussJuice><knowPheromone>{sknowComplexAlchemy[5]}</knowPheromone><knowBazoomba>{sknowComplexAlchemy[6]}</knowBazoomba></knowComplexAlchemy><majorFetish><maleFetish>{smajorFetish[0]}</maleFetish><femaleFetish>{smajorFetish[1]}</femaleFetish><hermFetish>{smajorFetish[2]}</hermFetish><narcissistFetish>{smajorFetish[3]}</narcissistFetish><dependentFetish>{smajorFetish[4]}</dependentFetish></majorFetish><moderateFetish><dominantFetish>{smoderateFetish[0]}</dominantFetish><submissiveFetish>{smoderateFetish[1]}</submissiveFetish><lboobFetish>{smoderateFetish[2]}</lboobFetish><sboobFetish>{smoderateFetish[3]}</sboobFetish><furryFetish>{smoderateFetish[4]}</furryFetish><scalyFetish>{smoderateFetish[5]}</scalyFetish><smoothyFetish>{smoderateFetish[6]}</smoothyFetish></moderateFetish><minorFetish><pregnancyFetish>{sminorFetish[0]}</pregnancyFetish><bestialityFetish>{sminorFetish[1]}</bestialityFetish><milkFetish>{sminorFetish[2]}</milkFetish><sizeFetish>{sminorFetish[3]}</sizeFetish><unbirthingFetish>{sminorFetish[4]}</unbirthingFetish><ovipositionFetish>{sminorFetish[5]}</ovipositionFetish><toyFetish>{sminorFetish[6]}</toyFetish><hyperFetish>{sminorFetish[7]}</hyperFetish></minorFetish><kid><humanChildren>{skid[0]}</humanChildren><equanChildren>{skid[1]}</equanChildren><lupanChildren>{skid[2]}</lupanChildren><felinChildren>{skid[3]}</felinChildren><cowChildren>{skid[4]}</cowChildren><lizanChildren>{skid[5]}</lizanChildren><lizanEggs>{skid[6]}</lizanEggs><bunnionChildren>{skid[7]}</bunnionChildren><wolfPupChildren>{skid[8]}</wolfPupChildren><miceChildren>{skid[9]}</miceChildren><birdEggs>{skid[10]}</birdEggs><birdChildren>{skid[11]}</birdChildren><pigChildren>{skid[12]}</pigChildren><calfChildren>{skid[13]}</calfChildren><bugEggs>{skid[14]}</bugEggs><bugChildren>{skid[15]}</bugChildren><skunkChildren>{skid[16]}</skunkChildren><minotaurChildren>{skid[17]}</minotaurChildren><freakyGirlChildren>{skid[18]}</freakyGirlChildren></kid><trav></trav><bag>"
      _bagArray = so["bagSave"]
      _bagStackArray = so["bagStackSave"]
      _stashArray = so["stashSave"]
      _stashStackArray = so["stashStackSave"]
      _pregArray = so["pregSave"]
      for i in range(0, 27):
         string += f"<slot{i}>{_bagArray[i]}</slot{i}>"
      string += "</bag><bagStack>"
      for i in range(0, 27):
         string += f"<slot{i}>{_bagStackArray[i]}</slot{i}>"
      string += "</bagStack><stash>"
      for i in range(0, 27):
         string += f"<slot{i}>{_stashArray[i]}</slot{i}>"
      string += "</stash><stashStack>"
      for i in range(0, 27):
         string += f"<slot{i}>{_stashStackArray[i]}</slot{i}>"
      string += "</stashStack><preg>"
      i = 0
      while i < len(_pregArray):
         string += f"<i{i}>{_pregArray[i]}</i{i}>"
         i += 1
      string += "</preg></data>"
      data = xmletree.fromstring(string)
      return xmletree.ElementTree(element=data)
   except:
      print("SOL File Loader: Error: Malformed save file")
def toXmlReturnNIM(inputfile):
   try:
      with open(inputfile, "rb") as file:
         so = amf3.ByteArray(file).readObject()["data"]
      strack = so["track"]
      sstats = so["stats"]
      slevel = so["level"]
      smod = so["mod"]
      squality = so["quality"]
      scock = so["cock"]
      sgirl = so["girl"]
      sgear = so["gear"]
      sgear[2] = int(sgear[2])
      sstatus = so["status"]
      saffinity = so["affinity"]
      srep = so["rep"]
      sknowledge = so["knowledge"]
      sboss = so["boss"]
      sknowSimpleAlchemy = so["knowSimpleAlchemy"]
      sknowAdvancedAlchemy = so["knowAdvancedAlchemy"]
      sknowComplexAlchemy = so["knowComplexAlchemy"]
      smajorFetish = so["majorFetish"]
      smoderateFetish = so["moderateFetish"]
      sminorFetish = so["minorFetish"]
      skid = so["kid"]
      trav = so["trav"]
      string = f"<data><track><currentState>{strack[0]}</currentState><currentZone>{strack[1]}</currentZone><day>{strack[2]}</day><hour>{strack[3]}</hour><currentDayCare>{strack[4]}</currentDayCare><inDungeon>{strack[5]}</inDungeon><currentDungeon>{strack[6]}</currentDungeon><v7>{strack[7]}</v7></track>"
      if 'versionNumber' in so.keys():
            string += f"<version><original>{so['versionNumber']}</original>"
            if 'versionNumberPymin' in so.keys():
               string += f"<port>{so['versionNumberPymin']}</port>"
            string += "</version>"
      string += f"<stats><strength>{sstats[0]}</strength><mentality>{sstats[1]}</mentality><libido>{sstats[2]}</libido><sensitivity>{sstats[3]}</sensitivity><HP>{sstats[4]}</HP><lust>{sstats[5]}</lust><coin>{sstats[6]}</coin><strMod>{sstats[7]}</strMod><mentMod>{sstats[8]}</mentMod><libMod>{sstats[9]}</libMod><senMod>{sstats[10]}</senMod><hunger>{sstats[11]}</hunger></stats><level><SexP>{slevel[0]}</SexP><levelUP>{slevel[1]}</levelUP><level>{slevel[2]}</level><babyFactLevel>{slevel[3]}</babyFactLevel><bodyBuildLevel>{slevel[4]}</bodyBuildLevel><hyperHappyLevel>{slevel[5]}</hyperHappyLevel><alchemistLevel>{slevel[6]}</alchemistLevel><fetishMasterLevel>{slevel[7]}</fetishMasterLevel><milkMaidLevel>{slevel[8]}</milkMaidLevel><shapeshiftyLevel>{slevel[9]}</shapeshiftyLevel><shapeshiftyFirst>{slevel[10]}</shapeshiftyFirst><shapeshiftySecond>{slevel[11]}</shapeshiftySecond></level><mod><runMod>{smod[0]}</runMod><rapeMod>{smod[1]}</rapeMod><cumMod>{smod[2]}</cumMod><cockSizeMod>{smod[3]}</cockSizeMod><milkMod>{smod[4]}</milkMod><carryMod>{smod[5]}</carryMod><vagBellyMod>{smod[6]}</vagBellyMod><pregChanceMod>{smod[7]}</pregChanceMod><extraPregChance>{smod[8]}</extraPregChance><pregTimeMod>{smod[9]}</pregTimeMod><enticeMod>{smod[10]}</enticeMod><milkHPMod>{smod[11]}</milkHPMod><vagSizeMod>{smod[12]}</vagSizeMod><vagElastic>{smod[13]}</vagElastic><changeMod>{smod[14]}</changeMod><HPMod>{smod[15]}</HPMod><SexPMod>{smod[16]}</SexPMod><minLust>{smod[17]}</minLust><milkCap>{smod[18]}</milkCap><coinMod>{smod[19]}</coinMod><hipMod>{smod[20]}</hipMod><buttMod>{smod[21]}</buttMod><bellyMod>{smod[22]}</bellyMod><cockMoistMod>{smod[23]}</cockMoistMod><vagMoistMod>{smod[24]}</vagMoistMod><lockTail>{smod[25]}</lockTail><lockFace>{smod[26]}</lockFace><lockSkin>{smod[27]}</lockSkin><lockBreasts>{smod[28]}</lockBreasts><lockEars>{smod[29]}</lockEars><lockLegs>{smod[30]}</lockLegs><lockNipples>{smod[31]}</lockNipples><lockCock>{smod[32]}</lockCock></mod><quality><gender>{squality[0]}</gender><race>{squality[1]}</race><body>{squality[2]}</body><dominant>{squality[3]}</dominant><hips>{squality[4]}</hips><butt>{squality[5]}</butt><tallness>{squality[6]}</tallness><skinType>{squality[7]}</skinType><tail>{squality[8]}</tail><ears>{squality[9]}</ears><hair>{squality[10]}</hair><hairColor>{squality[11]}</hairColor><hairLength>{squality[12]}</hairLength><legType>{squality[13]}</legType><wings>{squality[14]}</wings><faceType>{squality[15]}</faceType><skinColor>{squality[16]}</skinColor></quality><cock><cockTotal>{scock[0]}</cockTotal><humanCocks>{scock[1]}</humanCocks><horseCocks>{scock[2]}</horseCocks><wolfCocks>{scock[3]}</wolfCocks><catCocks>{scock[4]}</catCocks><rabbitCocks>{scock[5]}</rabbitCocks><lizardCocks>{scock[6]}</lizardCocks><cockSize>{scock[7]}</cockSize><cockMoist>{scock[8]}</cockMoist><balls>{scock[9]}</balls><ballSize>{scock[10]}</ballSize><showBalls>{scock[11]}</showBalls><knot>{scock[12]}</knot><bugCocks>{scock[13]}</bugCocks>"
      if len(scock) == 15:
         string += f"<neuterizerHideBalls>{scock[14]}</neuterizerHideBalls>"
      string += f"</cock><girl><breastSize>{sgirl[0]}</breastSize><boobTotal>{sgirl[1]}</boobTotal><nippleSize>{sgirl[2]}</nippleSize><udders>{sgirl[3]}</udders><udderSize>{sgirl[4]}</udderSize><teatSize>{sgirl[5]}</teatSize><clitSize>{sgirl[6]}</clitSize><vagTotal>{sgirl[7]}</vagTotal><vagSize>{sgirl[8]}</vagSize><vagMoist>{sgirl[9]}</vagMoist><vulvaSize>{sgirl[10]}</vulvaSize><nipType>{sgirl[11]}</nipType></girl><gear><attireTop>{sgear[0]}</attireTop><attireBot>{sgear[1]}</attireBot><weapon>{sgear[2]}</weapon></gear><status><pregRate>{sstatus[0]}</pregRate><pregnancyTime>{sstatus[1]}</pregnancyTime><pregStatus>{sstatus[2]}</pregStatus><eggLaying>{sstatus[3]}</eggLaying><eggMaxTime>{sstatus[4]}</eggMaxTime><eggTime>{sstatus[5]}</eggTime><eggRate>{sstatus[6]}</eggRate><exhaustion>{sstatus[7]}</exhaustion><exhaustionPenalty>{sstatus[8]}</exhaustionPenalty><milkEngorgement>{sstatus[9]}</milkEngorgement><milkEngorgementLevel>{sstatus[10]}</milkEngorgementLevel><udderEngorgement>{sstatus[11]}</udderEngorgement><udderEngorgementLevel>{sstatus[12]}</udderEngorgementLevel><heat>{sstatus[13]}</heat><heatTime>{sstatus[14]}</heatTime><heatMaxTime>{sstatus[15]}</heatMaxTime><lactation>{sstatus[16]}</lactation><udderLactation>{sstatus[17]}</udderLactation><nipplePlay>{sstatus[18]}</nipplePlay><udderPlay>{sstatus[19]}</udderPlay><blueBalls>{sstatus[20]}</blueBalls><teatPump>{sstatus[21]}</teatPump><nipPump>{sstatus[22]}</nipPump><cockPump>{sstatus[23]}</cockPump><clitPump>{sstatus[24]}</clitPump><vulvaPump>{sstatus[25]}</vulvaPump><masoPot>{sstatus[26]}</masoPot><sMasoPot>{sstatus[27]}</sMasoPot><babyFree>{sstatus[28]}</babyFree><charmTime>{sstatus[29]}</charmTime><pheromone>{sstatus[30]}</pheromone><eggceleratorTime>{sstatus[31]}</eggceleratorTime><eggceleratorDose>{sstatus[32]}</eggceleratorDose><bodyOil>{sstatus[33]}</bodyOil><lustPenalty>{sstatus[34]}</lustPenalty><fertileGel>{sstatus[35]}</fertileGel><snuggleBall>{sstatus[36]}</snuggleBall><eggType>{sstatus[37]}</eggType><milkSuppressant>{sstatus[38]}</milkSuppressant><milkSuppressantLact>{sstatus[39]}</milkSuppressantLact><milkSuppressantUdder>{sstatus[40]}</milkSuppressantUdder><suppHarness>{sstatus[41]}</suppHarness><fertilityStatueCurse>{sstatus[42]}</fertilityStatueCurse><plumpQuats>{sstatus[43]}</plumpQuats><lilaWetStatus>{sstatus[44]}</lilaWetStatus><cockSnakePreg>{sstatus[45]}</cockSnakePreg><milkCPoisonNip>{sstatus[46]}</milkCPoisonNip><milkCPoisonUdd>{sstatus[47]}</milkCPoisonUdd><cockSnakeVenom>{sstatus[48]}</cockSnakeVenom></status><affinity><humanAffinity>{saffinity[0]}</humanAffinity><horseAffinity>{saffinity[1]}</horseAffinity><wolfAffinity>{saffinity[2]}</wolfAffinity><catAffinity>{saffinity[3]}</catAffinity><cowAffinity>{saffinity[4]}</cowAffinity><lizardAffinity>{saffinity[5]}</lizardAffinity><rabbitAffinity>{saffinity[6]}</rabbitAffinity><fourBoobAffinity>{saffinity[7]}</fourBoobAffinity><mouseAffinity>{saffinity[8]}</mouseAffinity><birdAffinity>{saffinity[9]}</birdAffinity><pigAffinity>{saffinity[10]}</pigAffinity><twoBoobAffinity>{saffinity[11]}</twoBoobAffinity><sixBoobAffinity>{saffinity[12]}</sixBoobAffinity><eightBoobAffinity>{saffinity[13]}</eightBoobAffinity><tenBoobAffinity>{saffinity[14]}</tenBoobAffinity><cowTaurAffinity>{saffinity[15]}</cowTaurAffinity><humanTaurAffinity>{saffinity[16]}</humanTaurAffinity><skunkAffinity>{saffinity[17]}</skunkAffinity><bugAffinity>{saffinity[18]}</bugAffinity></affinity><rep><lilaRep>{srep[0]}</lilaRep><lilaVulva>{srep[1]}</lilaVulva><lilaMilk>{srep[2]}</lilaMilk><lilaPreg>{srep[3]}</lilaPreg><malonRep>{srep[4]}</malonRep><malonPreg>{srep[5]}</malonPreg><malonChildren>{srep[6]}</malonChildren><mistressRep>{srep[7]}</mistressRep><jamieRep>{srep[8]}</jamieRep><jamieSize>{srep[9]}</jamieSize><jamieChildren>{srep[10]}</jamieChildren><silRep>{srep[11]}</silRep><silPreg>{srep[12]}</silPreg><silRate>{srep[13]}</silRate><silLay>{srep[14]}</silLay><silGrowthTime>{srep[15]}</silGrowthTime><silTied>{srep[16]}</silTied><lilaUB>{srep[17]}</lilaUB><dairyFarmBrand>{srep[18]}</dairyFarmBrand><lilaWetness>{srep[19]}</lilaWetness><jamieButt>{srep[20]}</jamieButt><jamieBreasts>{srep[21]}</jamieBreasts><jamieHair>{srep[22]}</jamieHair></rep><knowledge><foundSoftlik>{sknowledge[0]}</foundSoftlik><foundFirmshaft>{sknowledge[1]}</foundFirmshaft><foundTieden>{sknowledge[2]}</foundTieden><foundSizCalit>{sknowledge[3]}</foundSizCalit><foundOviasis>{sknowledge[4]}</foundOviasis><foundValley>{sknowledge[5]}</foundValley><foundSanctuary>{sknowledge[6]}</foundSanctuary></knowledge><boss><defeatedMinotaur>{sboss[0]}</defeatedMinotaur><defeatedFreakyGirl>{sboss[1]}</defeatedFreakyGirl><defeatedSuccubus>{sboss[2]}</defeatedSuccubus></boss><knowSimpleAlchemy><knowLustDraft>{sknowSimpleAlchemy[0]}</knowLustDraft><knowRejuvPot>{sknowSimpleAlchemy[1]}</knowRejuvPot><knowExpPreg>{sknowSimpleAlchemy[2]}</knowExpPreg><knowBallSwell>{sknowSimpleAlchemy[3]}</knowBallSwell><knowMaleEnhance>{sknowSimpleAlchemy[4]}</knowMaleEnhance></knowSimpleAlchemy><knowAdvancedAlchemy><knowSLustDraft>{sknowAdvancedAlchemy[0]}</knowSLustDraft><knowSRejuvPot>{sknowAdvancedAlchemy[1]}</knowSRejuvPot><knowSExpPreg>{sknowAdvancedAlchemy[2]}</knowSExpPreg><knowSBallSwell>{sknowAdvancedAlchemy[3]}</knowSBallSwell><knowGenSwap>{sknowAdvancedAlchemy[4]}</knowGenSwap><knowMasoPot>{sknowAdvancedAlchemy[5]}</knowMasoPot><knowBabyFree>{sknowAdvancedAlchemy[6]}</knowBabyFree><knowPotPot>{sknowAdvancedAlchemy[7]}</knowPotPot><knowMilkSuppress>{sknowAdvancedAlchemy[8]}</knowMilkSuppress></knowAdvancedAlchemy><knowComplexAlchemy><knowSGenSwap>{sknowComplexAlchemy[0]}</knowSGenSwap><knowSMasoPot>{sknowComplexAlchemy[1]}</knowSMasoPot><knowSBabyFree>{sknowComplexAlchemy[2]}</knowSBabyFree><knowSPotPot>{sknowComplexAlchemy[3]}</knowSPotPot><knowPussJuice>{sknowComplexAlchemy[4]}</knowPussJuice><knowPheromone>{sknowComplexAlchemy[5]}</knowPheromone><knowBazoomba>{sknowComplexAlchemy[6]}</knowBazoomba></knowComplexAlchemy><majorFetish><maleFetish>{smajorFetish[0]}</maleFetish><femaleFetish>{smajorFetish[1]}</femaleFetish><hermFetish>{smajorFetish[2]}</hermFetish><narcissistFetish>{smajorFetish[3]}</narcissistFetish><dependentFetish>{smajorFetish[4]}</dependentFetish></majorFetish><moderateFetish><dominantFetish>{smoderateFetish[0]}</dominantFetish><submissiveFetish>{smoderateFetish[1]}</submissiveFetish><lboobFetish>{smoderateFetish[2]}</lboobFetish><sboobFetish>{smoderateFetish[3]}</sboobFetish><furryFetish>{smoderateFetish[4]}</furryFetish><scalyFetish>{smoderateFetish[5]}</scalyFetish><smoothyFetish>{smoderateFetish[6]}</smoothyFetish></moderateFetish><minorFetish><pregnancyFetish>{sminorFetish[0]}</pregnancyFetish><bestialityFetish>{sminorFetish[1]}</bestialityFetish><milkFetish>{sminorFetish[2]}</milkFetish><sizeFetish>{sminorFetish[3]}</sizeFetish><unbirthingFetish>{sminorFetish[4]}</unbirthingFetish><ovipositionFetish>{sminorFetish[5]}</ovipositionFetish><toyFetish>{sminorFetish[6]}</toyFetish><hyperFetish>{sminorFetish[7]}</hyperFetish></minorFetish><kid><humanChildren>{skid[0]}</humanChildren><equanChildren>{skid[1]}</equanChildren><lupanChildren>{skid[2]}</lupanChildren><felinChildren>{skid[3]}</felinChildren><cowChildren>{skid[4]}</cowChildren><lizanChildren>{skid[5]}</lizanChildren><lizanEggs>{skid[6]}</lizanEggs><bunnionChildren>{skid[7]}</bunnionChildren><wolfPupChildren>{skid[8]}</wolfPupChildren><miceChildren>{skid[9]}</miceChildren><birdEggs>{skid[10]}</birdEggs><birdChildren>{skid[11]}</birdChildren><pigChildren>{skid[12]}</pigChildren><calfChildren>{skid[13]}</calfChildren><bugEggs>{skid[14]}</bugEggs><bugChildren>{skid[15]}</bugChildren><skunkChildren>{skid[16]}</skunkChildren><minotaurChildren>{skid[17]}</minotaurChildren><freakyGirlChildren>{skid[18]}</freakyGirlChildren></kid><trav></trav><bag>"
      _bagArray = so["bagSave"]
      _bagStackArray = so["bagStackSave"]
      _stashArray = so["stashSave"]
      _stashStackArray = so["stashStackSave"]
      _pregArray = so["pregSave"]
      for i in range(0, 27):
         string += f"<slot{i}>{_bagArray[i]}</slot{i}>"
      string += "</bag><bagStack>"
      for i in range(0, 27):
         string += f"<slot{i}>{_bagStackArray[i]}</slot{i}>"
      string += "</bagStack><stash>"
      for i in range(0, 27):
         string += f"<slot{i}>{_stashArray[i]}</slot{i}>"
      string += "</stash><stashStack>"
      for i in range(0, 27):
         string += f"<slot{i}>{_stashStackArray[i]}</slot{i}>"
      string += "</stashStack><preg>"
      i = 0
      while i < len(_pregArray):
         string += f"<i{i}>{_pregArray[i]}</i{i}>"
         i += 1
      string += "</preg></data>"
      data = xmletree.fromstring(string)
      return xmletree.ElementTree(element=data)
   except:
      print("NIM File Loader: Error: Malformed save file")
      message["text"]="Error: Malformed save file"
def IFileChoose():
   file = filedialog.askopenfilename(initialdir=dir_)
   if type(file) != tuple and file != "":
      inputfilepath.set(file)
def OFileChoose():
   file = filedialog.asksaveasfilename(initialdir=dir_)
   if type(file) != tuple and file != "":
      outputfilepath.set(file)

def buttonSetThemeDefault(button,*args):
   button["background"]="#FFFFFF"
   button["activebackground"]="#FFFFFF"
   button["highlightcolor"]="#000000"
   button["highlightbackground"]="#000000"
   button.bind("<Enter>",partial(buttonBorderSet,button))
   button.bind("<Leave>",partial(buttonBorderUnset,button))
   button.bind("<Button-1>",partial(buttonBackgroundSet,button))
   button.bind("<ButtonRelease-1>",partial(buttonBackgroundUnset,button))
def buttonBorderSet(button,*args):
   button["highlightcolor"]="#0074BE"
   button["highlightbackground"]="#0074BE"
def buttonBorderUnset(button,*args):
   button["highlightcolor"]="#000000"
   button["highlightbackground"]="#000000"
def buttonBackgroundSet(button,*args):
   button["background"]="#A1D9FD"
   button["activebackground"]="#A1D9FD"
def buttonBackgroundUnset(button,*args):
   button["background"]="#FFFFFF"
   button["activebackground"]="#FFFFFF"

def entrySetThemeDefault(entry,*args):
   entry["background"]="#FFFFFF"
   entry["highlightcolor"]="#000000"
   entry["highlightbackground"]="#000000"
   entry.bind("<Enter>",partial(entryBorderSet,entry))
   entry.bind("<Leave>",partial(entryBorderUnset,entry))
def entryBorderSet(entry,*args):
   entry["highlightcolor"]="#0074BE"
   entry["highlightbackground"]="#0074BE"
def entryBorderUnset(entry,*args):
   entry["highlightcolor"]="#000000"
   entry["highlightbackground"]="#000000"

def cliDoMultipleFiles(files,outputformat):
   i = 0
   while i < len(files):
      message["text"] = ""
      inputfile = Path(files[i])
      if inputfile.exists() == False:
         message["text"] = f"{files[i]}: Error: Input file does not exist"
      if inputfile.is_dir() == True:
         message["text"] = f"{files[i]}: Error: Input must be a file"
      tempin = str(inputfile.name).split(".")
      if len(tempin) == 1:
         message["text"] = f"{files[i]}: Error: Input file must have an extension"
      if tempin[-1] not in ("xml","sol","nim"):
         message["text"] = f"{files[i]}: Error: Input file type is not supported"
      if tempin[-1] == outputformat:
         message["text"] = f"{files[i]}: Error: Output file type can not be the same as input file type"
      outputfile = inputfile.parent / (".".join(tempin[:-1]) + f".{outputformat}")
      if outputfile.is_dir() == True:
         message["text"] = f"{files[i]}: Error: Output must be a file"
      if outputfile.exists():
         ans = input(f"{files[i]}: Output file exists, would you like to overwrite it? (y/N) ")
         if ans.lower() in ("","n"):
            message["text"] = f"{files[i]}: Aborted"
      if message["text"] == "":
         convertSave(str(inputfile),"detect",str(outputfile),outputformat)
      if message["text"] != "Success":
         print(f"{files[i]}:" + message["text"])
      i += 1

def help():
   print("""Nimin_Savefile_Converter.py [mode] [...files]\nModes:\n-s --single\tTakes two arguesments, inputfile and outputfile/format. If a format is used instead of an output file, the file will be of the same name as the original with the new format.\n-m --many\tTakes many arguements, the first of which must be the output format, all of the rest are input files.\n-d --dir\tConverts all files in a directory (non-recursive). The first arguement is the output format, the second is the directory.""")

if __name__ == "__main__":
   if len(argv) == 1:
      dir_ = Path(__file__).parent
      root = tkinter.Tk()
      root.geometry("500x334")
      root.resizable(False,False)
      root.title("Pymin Savefile Converter")
      root["background"]="#FFFFFF"

      style = ttk.Style()
      style.theme_settings(
         "default", {
            "TCombobox": {
               "map": {
                  "background": [
                     ("active","#FFFFFF")
                  ],
                  "fieldbackground": [
                     ("!disabled","#FFFFFF")
                  ]
               }
            }
         }
      )
      fileimage = tkinter.PhotoImage(data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0c\x08\x06\x00\x00\x00k\xe7=\x81\x00\x00\x01\x84iCCPICC profile\x00\x00(\x91}\x91=H\xc3P\x14\x85OSE\x91\x8a\x88\x1dD\x1c2T\x17\xdbEE\x1ck\x15\x8aP!\xd4\n\xad:\x98\xbc\xf4\x0f\x9a4$).\x8e\x82k\xc1\xc1\x9f\xc5\xaa\x83\x8b\xb3\xae\x0e\xae\x82 \xf8\x03\xe2.8)\xbaH\x89\xf7%\x85\x161\xde\xf0\xc8\xc7y\xf7\x1c\xde\xbb\x0f\x10\x1a\x15\xa6Y]q@\xd3m3\x9dL\x88\xd9\xdc\xaa\xd8\xf3\x8a\x00}\x83\x88bBf\x961\'I)\xf8\xd6\xd7=\xf5R\xdd\xc5x\x96\x7f\xdf\x9f\xd5\xaf\xe6-\x06\x04D\xe283L\x9bx\x83xf\xd368\xef\x13\x87YIV\x89\xcf\x89\xa3&\x1d\x90\xf8\x91\xeb\x8a\xc7o\x9c\x8b.\x0b<3lf\xd2\xf3\xc4ab\xb1\xd8\xc1J\x07\xb3\x92\xa9\x11O\x13GTM\xa7|!\xeb\xb1\xcay\x8b\xb3V\xa9\xb1\xd69\xf9\rCy}e\x99\xeb\xb4F\x91\xc4"\x96 A\x84\x82\x1a\xca\xa8\xc0F\x8c\xfe:)\x16\xd2\xb4\x9f\xf0\xf1\x8f\xb8~\x89\\\n\xb9\xca`\xe4X@\x15\x1ad\xd7\x0f\xfe\x06\xbfgk\x15\xa6&\xbd\xa4P\x02\xe8~q\x9c\x8f1\xa0g\x17h\xd6\x1d\xe7\xfb\xd8q\x9a\'@\xf0\x19\xb8\xd2\xdb\xfej\x03\x98\xfd$\xbd\xde\xd6"G\xc0\xc06pq\xdd\xd6\x94=\xe0r\x07\x18~2dSv\xa5 -\xa1P\x00\xde\xcf\xe8\x99r\xc0\xd0-\xd0\xb7\xe6\xcd\xad\xb5\x8f\xd3\x07 C\xb3J\xdd\x00\x07\x87\xc0x\x91\xb2\xd7}\xee\xdd\xdb9\xb7\x7f{Z\xf3\xfb\x01\xa8\x9er\xbc\xeb \xb8\x8a\x00\x00\x00\x06bKGD\x00\xd3\x00\x9d\x00JT\xd4=\xdb\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x00\x07tIME\x07\xe9\x01\x01\x11-.\x99[0X\x00\x00\x00\x19tEXtComment\x00Created with GIMPW\x81\x0e\x17\x00\x00\x00JIDAT(\xcfc` \x00^l\xcf\xe1{\xb1=\x87\t\x97<\x0bT\xd1\x7f<fp3000300\xfc\xc3&\xc9H\x84\x018\x81\x84\xe7\x14F\x16B\x8a^?\xbb\x87W\x9e\x85\x18E\xf8\x00\x13\x03\x85`\xd4\x00*\x18@1\x00\x00l\t\x11\xb4\x84N\xcd\xaf\x00\x00\x00\x00IEND\xaeB`\x82')
      titlelabel = tkinter.Label(root,justify="center",text="Pymin Savefile Converter",font=('TimesNewRoman',20,'bold'))
      titlelabel.place(x=250,y=50,width=300,height=32,anchor="n")
      titlelabel["background"]="#FFFFFF"

      message = tkinter.Label(root,justify="center",text="",font=('TimesNewRoman',12),wraplength=300)
      message.place(x=250,y=100,width=300,height=50,anchor="n")
      message["foreground"]="#FF1111"
      message["background"]="#FFFFFF"

      inputfilelabel = tkinter.Label(root,text="Input File",font=('TimesNewRoman',12))
      inputfilelabel.place(x=50,y=150,height=24)
      inputfilelabel["background"]="#FFFFFF"
      inputfilepath = tkinter.StringVar()
      inputfileentry = tkinter.Entry(root,textvariable=inputfilepath)
      inputfileentry.place(x=50,y=174,width=296,height=24,anchor="nw")
      entrySetThemeDefault(inputfileentry)
      inputfilepicker = tkinter.Button(root,command=IFileChoose,image=fileimage)
      inputfilepicker.place(x=346,y=174,width=24,height=24,anchor="nw")
      buttonSetThemeDefault(inputfilepicker)

      inputfiletypelabel = tkinter.Label(root,text="Type",font=("TimesNewRoman",12))
      inputfiletypelabel.place(x=390,y=150,width=40,height=24,anchor="nw")
      inputfiletypelabel["background"]="#FFFFFF"
      inputfiletypevar = tkinter.StringVar()
      inputfiletypecombo = ttk.Combobox(root,font=("TimesNewRoman",12),textvariable=inputfiletypevar,state="readonly")
      inputfiletypecombo["values"] = ("detect","xml","sol","nim")
      inputfiletypevar.set("detect")
      inputfiletypecombo.place(x=390,y=174,width=60,height=24,anchor="nw")

      outputfilelabel = tkinter.Label(root,text="Output File",font=('TimesNewRoman',12))
      outputfilelabel.place(x=50,y=210,height=24)
      outputfilelabel["background"]="#FFFFFF"
      outputfilepath = tkinter.StringVar()
      outputfileentry = tkinter.Entry(root,textvariable=outputfilepath)
      outputfileentry.place(x=50,y=234,width=296,height=24,anchor="nw")
      entrySetThemeDefault(outputfileentry)
      outputfilepicker = tkinter.Button(root,command=OFileChoose,image=fileimage)
      outputfilepicker.place(x=346,y=234,width=24,height=24,anchor="nw")
      buttonSetThemeDefault(outputfilepicker)

      outputfiletypetext = tkinter.Label(root,text="Type",font=("TimesNewRoman",12))
      outputfiletypetext.place(x=390,y=210,width=40,height=24,anchor="nw")
      outputfiletypetext["background"]="#FFFFFF"
      outputfiletypevar = tkinter.StringVar()
      outputfiletypecombo = ttk.Combobox(root,font=("TimesNewRoman",12),textvariable=outputfiletypevar,state="readonly")
      outputfiletypecombo["values"] = ("detect","xml","sol","nim")
      outputfiletypevar.set("detect")
      outputfiletypecombo.place(x=390,y=234,width=60,height=24,anchor="nw")

      convertbutton = tkinter.Button(root,font=("TimesNewRoman",12),text="Convert",command=convertButton)
      convertbutton.place(x=386,y=270,width=64,height=24,anchor="nw")
      buttonSetThemeDefault(convertbutton)

      root.mainloop()
   else: #comandline args
      message = {"text":""}
      if argv[1] == "help" or "--help" in argv or "-h" in argv or "/?" in argv:
         help()
      elif argv[1] in ("-s","--single","/s","/S"): #one file then output file or output type
         inputfile = Path(argv[2]).resolve()
         if inputfile.exists() == False:
            print("Error: Input file does not exist")
            exit()
         if inputfile.is_dir() == False:
            print("Error: Input must be a file")
            exit()
         tempin = str(inputfile.name).split(".")
         if len(tempin) == 1:
            print("Error: Input file must have an extension")
            exit()
         if tempin[-1] not in ("xml","sol","nim"):
            print("Error: Input file type is not supported")
            exit()
         if argv[3] in ("xml","sol","nim"):
            if tempin[-1] == argv[3]:
               print("Error: Output file type can not be the same as input file type")
               exit()
            outputfile = inputfile.parent / (".".join(tempin[:-1]) + f".{argv[3]}")
            if outputfile.is_dir() == True:
               print("Error: Output must be a file")
               exit()
            if outputfile.exists():
               ans = input("Output file exists, would you like to overwrite it? (y/N) ")
               if ans.lower() in ("","n"):
                  print("Aborted")
                  exit()
            convertSave(str(inputfile),"detect",str(outputfile),argv[3])
            print(message["text"])
         else:
            outputfile = Path(argv[3]).resolve()
            if outputfile.is_dir() == True:
               print("Error: Output must be a file")
               exit()
            tempout = str(outputfile.name).split(".")
            if tempout[-1] == tempin[-1]:
               print("Error: Output file type can not be the same as input file type")
               exit()
            if len(tempout) == 1:
               print("Error: Output file must have an extension")
               exit()
            if tempout[-1] not in ("xml","sol","nim"):
               print("Error: Output file type is not supported")
               exit()
            if outputfile.exists():
               ans = input("Output file exists, would you like to overwrite it? (y/N) ")
               if ans.lower() in ("","n"):
                  print("Aborted")
                  exit()
            convertSave(str(inputfile),"detect",str(outputfile),"detect")
            print(message["text"])
      elif argv[1] in ("-m","--many","/m","/M"): #convert all after this
         if len(argv) < 4:
            print("Error: Not enough arguements")
            exit()
         outputformat = argv[2]
         if outputformat not in ("xml","sol","nim"):
            print("Error: Output file type is not supported")
            exit()
         files = argv[3:]
         cliDoMultipleFiles(files,outputformat)
         print("Done")
      elif argv[1] in ("-d","--dir","/d","/D"):
         if len(argv) < 4:
            print("Error: Incorrect number of arguements")
            exit()
         outputformat = argv[2]
         if outputformat not in ("xml","sol","nim"):
            print("Error: Output file type is not supported")
            exit()
         dir_ = Path(argv[3]).resolve()
         if dir_.exists() == False:
            print("Error: Provided path does not exist")
            exit()
         if dir_.is_dir() == False:
            print("Error: Provided path must be a directory")
            exit()
         files = [str(f) for f in dir_.iterdir() if (dir_ / f).is_file() and str(f.name).split(".")[-1] in ("xml","sol","nim") and str(f.name).split(".")[-1] != outputformat]
         cliDoMultipleFiles(files,outputformat)
         print("Done")
      else:
         help()