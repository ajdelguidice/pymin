import sys
from miniamf import sol
import pathlib
import xml.dom.minidom as xmlminidom
import platform

def checkExtension(file,extension):
   """
   Checks if the input file has the correct extension.
   Inputs:
      file:string - path to the file
      extension:string - file extension without the dot
   Output:
      result:boolean
   """
   match platform.platform():
      case "Windows":
         ext = file.split("\\")[-1].split(".")[-1].lower()
      case "Linux" | "Darwin":
         ext = file.split("/")[-1].split(".")[-1].lower()
   if ext == extension.lower():
      return True
   else:
      return False

def phelp():
   print("convertsavefile.py [input].sol [output].xml")

if __name__ == "__main__":
   args = sys.argv
   if len(args) == 3 and pathlib.Path(args[1]).is_file():
      if pathlib.Path(args[2]).is_file():
         raise Exception("Can't overwrite existing file")
      else:
         so = sol.load(args[1])
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
         spref = xmlminidom.parseString(string).toprettyxml(indent ="\t")
         if checkExtension(args[2],"xml") == False:
            args[2] = args[2] + ".xml"
         with open(args[2], "w") as xmldoc:
            xmldoc.write(spref)
   else:
      phelp()
   


