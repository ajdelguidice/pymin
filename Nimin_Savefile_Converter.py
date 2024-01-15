import tkinter
from tkinter import filedialog
from miniamf import sol, AMF3
import pathlib
import xml.dom.minidom as xmlminidom
from platform import system
import xml.etree.ElementTree as xmletree

platform = system()

def repintorfloat(number):
   if type(number) == str:
      number = float(number)
   if type(number) == int:
      return number
   match number.is_integer():
      case True:
         return int(number)
      case False:
         return number
def strtobool(a:str):
   match a.lower():
      case "true":
         return True
      case "false":
         return False
def checkExtension(file,extension):
   match platform:
      case "Windows":
         ext = file.split("\\")[-1].split(".")[-1].lower()
      case "Linux" | "Darwin":
         ext = file.split("/")[-1].split(".")[-1].lower()
   if ext == extension.lower():
      return True
   else:
      return False
def solString(string):
   if string in [None,"None","undefined"]:
      return ""
   else:
      return str(string)
def solGetFileName(string):
   match platform:
      case "Windows":
         templist = string.split("\\")[-1].split(".")
         templist.pop(-1)
      case "Linux" | "Darwin":
         templist = string.split("/")[-1].split(".")
         templist.pop(-1)
   tempstr = ""
   for i in templist:
      if i == templist[-1]:
         tempstr += i
      else:
         tempstr += f"{i}."
   return tempstr
def soltoxml(*args):
   global messagebox
   inputfilename = filedialog.askopenfilename()
   if (type(inputfilename) == tuple):
      messagebox["text"] = "Please select an input file"
   else:
      outputfilename = filedialog.asksaveasfilename()
      if outputfilename == "":
         messagebox["text"] = "Please select an output file location"
      elif inputfilename == outputfilename:
         messagebox["text"] = "Input file can not be the same as output file"
      else:
         if pathlib.Path(inputfilename).is_file() == True:
            if checkExtension(outputfilename,"xml") == True:
               toxml(inputfilename, outputfilename)
            else:
               toxml(inputfilename, f"{outputfilename}.xml")
         elif pathlib.Path(inputfilename).is_dir() == True:
            messagebox["text"] = "Error: Input file is not a file"
         else:
            messagebox["text"] = "Error: Input file does not exist"
def toxml(inputfile,outputfile):
   global messagebox
   try:
      __version__ = "1.0.8"
      so = sol.load(inputfile)
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
      string = f"<data><track><currentState>{strack[0]}</currentState><currentZone>{strack[1]}</currentZone><day>{strack[2]}</day><hour>{strack[3]}</hour><currentDayCare>{strack[4]}</currentDayCare><inDungeon>{strack[5]}</inDungeon><currentDungeon>{strack[6]}</currentDungeon><v7>{strack[7]}</v7></track><version><original>{so['versionNumber']}</original><port>{__version__}</port></version><stats><strength>{sstats[0]}</strength><mentality>{sstats[1]}</mentality><libido>{sstats[2]}</libido><sensitivity>{sstats[3]}</sensitivity><HP>{sstats[4]}</HP><lust>{sstats[5]}</lust><coin>{sstats[6]}</coin><strMod>{sstats[7]}</strMod><mentMod>{sstats[8]}</mentMod><libMod>{sstats[9]}</libMod><senMod>{sstats[10]}</senMod><hunger>{sstats[11]}</hunger></stats><level><SexP>{slevel[0]}</SexP><levelUP>{slevel[1]}</levelUP><level>{slevel[2]}</level><babyFactLevel>{slevel[3]}</babyFactLevel><bodyBuildLevel>{slevel[4]}</bodyBuildLevel><hyperHappyLevel>{slevel[5]}</hyperHappyLevel><alchemistLevel>{slevel[6]}</alchemistLevel><fetishMasterLevel>{slevel[7]}</fetishMasterLevel><milkMaidLevel>{slevel[8]}</milkMaidLevel><shapeshiftyLevel>{slevel[9]}</shapeshiftyLevel><shapeshiftyFirst>{slevel[10]}</shapeshiftyFirst><shapeshiftySecond>{slevel[11]}</shapeshiftySecond></level><mod><runMod>{smod[0]}</runMod><rapeMod>{smod[1]}</rapeMod><cumMod>{smod[2]}</cumMod><cockSizeMod>{smod[3]}</cockSizeMod><milkMod>{smod[4]}</milkMod><carryMod>{smod[5]}</carryMod><vagBellyMod>{smod[6]}</vagBellyMod><pregChanceMod>{smod[7]}</pregChanceMod><extraPregChance>{smod[8]}</extraPregChance><pregTimeMod>{smod[9]}</pregTimeMod><enticeMod>{smod[10]}</enticeMod><milkHPMod>{smod[11]}</milkHPMod><vagSizeMod>{smod[12]}</vagSizeMod><vagElastic>{smod[13]}</vagElastic><changeMod>{smod[14]}</changeMod><HPMod>{smod[15]}</HPMod><SexPMod>{smod[16]}</SexPMod><minLust>{smod[17]}</minLust><milkCap>{smod[18]}</milkCap><coinMod>{smod[19]}</coinMod><hipMod>{smod[20]}</hipMod><buttMod>{smod[21]}</buttMod><bellyMod>{smod[22]}</bellyMod><cockMoistMod>{smod[23]}</cockMoistMod><vagMoistMod>{smod[24]}</vagMoistMod><lockTail>{smod[25]}</lockTail><lockFace>{smod[26]}</lockFace><lockSkin>{smod[27]}</lockSkin><lockBreasts>{smod[28]}</lockBreasts><lockEars>{smod[29]}</lockEars><lockLegs>{smod[30]}</lockLegs><lockNipples>{smod[31]}</lockNipples><lockCock>{smod[32]}</lockCock></mod><quality><gender>{squality[0]}</gender><race>{squality[1]}</race><body>{squality[2]}</body><dominant>{squality[3]}</dominant><hips>{squality[4]}</hips><butt>{squality[5]}</butt><tallness>{squality[6]}</tallness><skinType>{squality[7]}</skinType><tail>{squality[8]}</tail><ears>{squality[9]}</ears><hair>{squality[10]}</hair><hairColor>{squality[11]}</hairColor><hairLength>{squality[12]}</hairLength><legType>{squality[13]}</legType><wings>{squality[14]}</wings><faceType>{squality[15]}</faceType><skinColor>{squality[16]}</skinColor></quality><cock><cockTotal>{scock[0]}</cockTotal><humanCocks>{scock[1]}</humanCocks><horseCocks>{scock[2]}</horseCocks><wolfCocks>{scock[3]}</wolfCocks><catCocks>{scock[4]}</catCocks><rabbitCocks>{scock[5]}</rabbitCocks><lizardCocks>{scock[6]}</lizardCocks><cockSize>{scock[7]}</cockSize><cockMoist>{scock[8]}</cockMoist><balls>{scock[9]}</balls><ballSize>{scock[10]}</ballSize><showBalls>{scock[11]}</showBalls><knot>{scock[12]}</knot><bugCocks>{scock[13]}</bugCocks></cock><girl><breastSize>{sgirl[0]}</breastSize><boobTotal>{sgirl[1]}</boobTotal><nippleSize>{sgirl[2]}</nippleSize><udders>{sgirl[3]}</udders><udderSize>{sgirl[4]}</udderSize><teatSize>{sgirl[5]}</teatSize><clitSize>{sgirl[6]}</clitSize><vagTotal>{sgirl[7]}</vagTotal><vagSize>{sgirl[8]}</vagSize><vagMoist>{sgirl[9]}</vagMoist><vulvaSize>{sgirl[10]}</vulvaSize><nipType>{sgirl[11]}</nipType></girl><gear><attireTop>{sgear[0]}</attireTop><attireBot>{sgear[1]}</attireBot><weapon>{sgear[2]}</weapon></gear><status><pregRate>{sstatus[0]}</pregRate><pregnancyTime>{sstatus[1]}</pregnancyTime><pregStatus>{sstatus[2]}</pregStatus><eggLaying>{sstatus[3]}</eggLaying><eggMaxTime>{sstatus[4]}</eggMaxTime><eggTime>{sstatus[5]}</eggTime><eggRate>{sstatus[6]}</eggRate><exhaustion>{sstatus[7]}</exhaustion><exhaustionPenalty>{sstatus[8]}</exhaustionPenalty><milkEngorgement>{sstatus[9]}</milkEngorgement><milkEngorgementLevel>{sstatus[10]}</milkEngorgementLevel><udderEngorgement>{sstatus[11]}</udderEngorgement><udderEngorgementLevel>{sstatus[12]}</udderEngorgementLevel><heat>{sstatus[13]}</heat><heatTime>{sstatus[14]}</heatTime><heatMaxTime>{sstatus[15]}</heatMaxTime><lactation>{sstatus[16]}</lactation><udderLactation>{sstatus[17]}</udderLactation><nipplePlay>{sstatus[18]}</nipplePlay><udderPlay>{sstatus[19]}</udderPlay><blueBalls>{sstatus[20]}</blueBalls><teatPump>{sstatus[21]}</teatPump><nipPump>{sstatus[22]}</nipPump><cockPump>{sstatus[23]}</cockPump><clitPump>{sstatus[24]}</clitPump><vulvaPump>{sstatus[25]}</vulvaPump><masoPot>{sstatus[26]}</masoPot><sMasoPot>{sstatus[27]}</sMasoPot><babyFree>{sstatus[28]}</babyFree><charmTime>{sstatus[29]}</charmTime><pheromone>{sstatus[30]}</pheromone><eggceleratorTime>{sstatus[31]}</eggceleratorTime><eggceleratorDose>{sstatus[32]}</eggceleratorDose><bodyOil>{sstatus[33]}</bodyOil><lustPenalty>{sstatus[34]}</lustPenalty><fertileGel>{sstatus[35]}</fertileGel><snuggleBall>{sstatus[36]}</snuggleBall><eggType>{sstatus[37]}</eggType><milkSuppressant>{sstatus[38]}</milkSuppressant><milkSuppressantLact>{sstatus[39]}</milkSuppressantLact><milkSuppressantUdder>{sstatus[40]}</milkSuppressantUdder><suppHarness>{sstatus[41]}</suppHarness><fertilityStatueCurse>{sstatus[42]}</fertilityStatueCurse><plumpQuats>{sstatus[43]}</plumpQuats><lilaWetStatus>{sstatus[44]}</lilaWetStatus><cockSnakePreg>{sstatus[45]}</cockSnakePreg><milkCPoisonNip>{sstatus[46]}</milkCPoisonNip><milkCPoisonUdd>{sstatus[47]}</milkCPoisonUdd><cockSnakeVenom>{sstatus[48]}</cockSnakeVenom></status><affinity><humanAffinity>{saffinity[0]}</humanAffinity><horseAffinity>{saffinity[1]}</horseAffinity><wolfAffinity>{saffinity[2]}</wolfAffinity><catAffinity>{saffinity[3]}</catAffinity><cowAffinity>{saffinity[4]}</cowAffinity><lizardAffinity>{saffinity[5]}</lizardAffinity><rabbitAffinity>{saffinity[6]}</rabbitAffinity><fourBoobAffinity>{saffinity[7]}</fourBoobAffinity><mouseAffinity>{saffinity[8]}</mouseAffinity><birdAffinity>{saffinity[9]}</birdAffinity><pigAffinity>{saffinity[10]}</pigAffinity><twoBoobAffinity>{saffinity[11]}</twoBoobAffinity><sixBoobAffinity>{saffinity[12]}</sixBoobAffinity><eightBoobAffinity>{saffinity[13]}</eightBoobAffinity><tenBoobAffinity>{saffinity[14]}</tenBoobAffinity><cowTaurAffinity>{saffinity[15]}</cowTaurAffinity><humanTaurAffinity>{saffinity[16]}</humanTaurAffinity><skunkAffinity>{saffinity[17]}</skunkAffinity><bugAffinity>{saffinity[18]}</bugAffinity></affinity><rep><lilaRep>{srep[0]}</lilaRep><lilaVulva>{srep[1]}</lilaVulva><lilaMilk>{srep[2]}</lilaMilk><lilaPreg>{srep[3]}</lilaPreg><malonRep>{srep[4]}</malonRep><malonPreg>{srep[5]}</malonPreg><malonChildren>{srep[6]}</malonChildren><mistressRep>{srep[7]}</mistressRep><jamieRep>{srep[8]}</jamieRep><jamieSize>{srep[9]}</jamieSize><jamieChildren>{srep[10]}</jamieChildren><silRep>{srep[11]}</silRep><silPreg>{srep[12]}</silPreg><silRate>{srep[13]}</silRate><silLay>{srep[14]}</silLay><silGrowthTime>{srep[15]}</silGrowthTime><silTied>{srep[16]}</silTied><lilaUB>{srep[17]}</lilaUB><dairyFarmBrand>{srep[18]}</dairyFarmBrand><lilaWetness>{srep[19]}</lilaWetness><jamieButt>{srep[20]}</jamieButt><jamieBreasts>{srep[21]}</jamieBreasts><jamieHair>{srep[22]}</jamieHair></rep><knowledge><foundSoftlik>{sknowledge[0]}</foundSoftlik><foundFirmshaft>{sknowledge[1]}</foundFirmshaft><foundTieden>{sknowledge[2]}</foundTieden><foundSizCalit>{sknowledge[3]}</foundSizCalit><foundOviasis>{sknowledge[4]}</foundOviasis><foundValley>{sknowledge[5]}</foundValley><foundSanctuary>{sknowledge[6]}</foundSanctuary></knowledge><boss><defeatedMinotaur>{sboss[0]}</defeatedMinotaur><defeatedFreakyGirl>{sboss[1]}</defeatedFreakyGirl><defeatedSuccubus>{sboss[2]}</defeatedSuccubus></boss><knowSimpleAlchemy><knowLustDraft>{sknowSimpleAlchemy[0]}</knowLustDraft><knowRejuvPot>{sknowSimpleAlchemy[1]}</knowRejuvPot><knowExpPreg>{sknowSimpleAlchemy[2]}</knowExpPreg><knowBallSwell>{sknowSimpleAlchemy[3]}</knowBallSwell><knowMaleEnhance>{sknowSimpleAlchemy[4]}</knowMaleEnhance></knowSimpleAlchemy><knowAdvancedAlchemy><knowSLustDraft>{sknowAdvancedAlchemy[0]}</knowSLustDraft><knowSRejuvPot>{sknowAdvancedAlchemy[1]}</knowSRejuvPot><knowSExpPreg>{sknowAdvancedAlchemy[2]}</knowSExpPreg><knowSBallSwell>{sknowAdvancedAlchemy[3]}</knowSBallSwell><knowGenSwap>{sknowAdvancedAlchemy[4]}</knowGenSwap><knowMasoPot>{sknowAdvancedAlchemy[5]}</knowMasoPot><knowBabyFree>{sknowAdvancedAlchemy[6]}</knowBabyFree><knowPotPot>{sknowAdvancedAlchemy[7]}</knowPotPot><knowMilkSuppress>{sknowAdvancedAlchemy[8]}</knowMilkSuppress></knowAdvancedAlchemy><knowComplexAlchemy><knowSGenSwap>{sknowComplexAlchemy[0]}</knowSGenSwap><knowSMasoPot>{sknowComplexAlchemy[1]}</knowSMasoPot><knowSBabyFree>{sknowComplexAlchemy[2]}</knowSBabyFree><knowSPotPot>{sknowComplexAlchemy[3]}</knowSPotPot><knowPussJuice>{sknowComplexAlchemy[4]}</knowPussJuice><knowPheromone>{sknowComplexAlchemy[5]}</knowPheromone><knowBazoomba>{sknowComplexAlchemy[6]}</knowBazoomba></knowComplexAlchemy><majorFetish><maleFetish>{smajorFetish[0]}</maleFetish><femaleFetish>{smajorFetish[1]}</femaleFetish><hermFetish>{smajorFetish[2]}</hermFetish><narcissistFetish>{smajorFetish[3]}</narcissistFetish><dependentFetish>{smajorFetish[4]}</dependentFetish></majorFetish><moderateFetish><dominantFetish>{smoderateFetish[0]}</dominantFetish><submissiveFetish>{smoderateFetish[1]}</submissiveFetish><lboobFetish>{smoderateFetish[2]}</lboobFetish><sboobFetish>{smoderateFetish[3]}</sboobFetish><furryFetish>{smoderateFetish[4]}</furryFetish><scalyFetish>{smoderateFetish[5]}</scalyFetish><smoothyFetish>{smoderateFetish[6]}</smoothyFetish></moderateFetish><minorFetish><pregnancyFetish>{sminorFetish[0]}</pregnancyFetish><bestialityFetish>{sminorFetish[1]}</bestialityFetish><milkFetish>{sminorFetish[2]}</milkFetish><sizeFetish>{sminorFetish[3]}</sizeFetish><unbirthingFetish>{sminorFetish[4]}</unbirthingFetish><ovipositionFetish>{sminorFetish[5]}</ovipositionFetish><toyFetish>{sminorFetish[6]}</toyFetish><hyperFetish>{sminorFetish[7]}</hyperFetish></minorFetish><kid><humanChildren>{skid[0]}</humanChildren><equanChildren>{skid[1]}</equanChildren><lupanChildren>{skid[2]}</lupanChildren><felinChildren>{skid[3]}</felinChildren><cowChildren>{skid[4]}</cowChildren><lizanChildren>{skid[5]}</lizanChildren><lizanEggs>{skid[6]}</lizanEggs><bunnionChildren>{skid[7]}</bunnionChildren><wolfPupChildren>{skid[8]}</wolfPupChildren><miceChildren>{skid[9]}</miceChildren><birdEggs>{skid[10]}</birdEggs><birdChildren>{skid[11]}</birdChildren><pigChildren>{skid[12]}</pigChildren><calfChildren>{skid[13]}</calfChildren><bugEggs>{skid[14]}</bugEggs><bugChildren>{skid[15]}</bugChildren><skunkChildren>{skid[16]}</skunkChildren><minotaurChildren>{skid[17]}</minotaurChildren><freakyGirlChildren>{skid[18]}</freakyGirlChildren></kid><trav></trav><bag>"
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
      spref = xmlminidom.parseString(string).toprettyxml()
      spref = '<?xml version="1.0" encoding="UTF-8" ?>' + spref[spref.find("\n"):]
      with open(outputfile, "w") as xmldoc:
         xmldoc.write(spref)
      messagebox["text"] = "Success"
   except Exception as e:
      messagebox["text"] = "Error"
      print(e)
def xmltosol(*args):
   global messagebox
   inputfilename = filedialog.askopenfilename()
   if (type(inputfilename) == tuple):
      messagebox["text"] = "Please select an input file"
   else:
      outputfilename = filedialog.asksaveasfilename()
      if outputfilename == "":
         messagebox["text"] = "Please select an output file location"
      elif inputfilename == outputfilename:
         messagebox["text"] = "Input file can not be the same as output file"
      else:
         if pathlib.Path(inputfilename).is_file() == True:
            if checkExtension(outputfilename,"sol") == True:
               tosol(inputfilename, outputfilename)
            else:
               tosol(inputfilename, f"{outputfilename}.sol")
         elif pathlib.Path(inputfilename).is_dir() == True:
            messagebox["text"] = "Error: Input file is not a file"
         else:
            messagebox["text"] = "Error: Input file does not exist"
def tosol(inputfile,outputfile):
   global messagebox
   try:
      xmlfile = xmletree.parse(inputfile).getroot()
      data = sol.SOL(solGetFileName(outputfile))
      data["versionNumber"] = xmlfile.find("version").find("original").text
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
      sol.save(data,outputfile,AMF3)
      messagebox["text"] = "Success"
   except Exception as e:
      messagebox["text"] = "Error"
      print(e)

#Tkinter window
root = tkinter.Tk()
root.title("Nimin Savefile Converter")
root.geometry("500x300")

title = tkinter.Label(root, justify="center", text="Nimin Savefile Converter", font=('TimesNewRoman', 20, 'bold'))
title.place(anchor="n", height=25, width=300, x=250, y=50)

messagebox = tkinter.Label(root, justify="center", text="")
messagebox.place(anchor="n", height=25, width=300, x=250, y=150)

toxmlbutton = tkinter.Button(root, text="Convert .sol to .xml", command=soltoxml)
toxmlbutton.place(anchor="nw", height=50, width=200, x=50, y=200)
tosolbutton = tkinter.Button(root, text="Convert .xml to .sol", command=xmltosol)
tosolbutton.place(anchor="nw", height=50, width=200, x=250, y=200)

root.mainloop()