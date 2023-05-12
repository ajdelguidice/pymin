import sys
from miniamf import sol
import pathlib
import xml.dom.minidom as xmlminidom

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
         currentState = strack[0]
         currentZone = strack[1]
         day = strack[2]
         hour = strack[3]
         currentDayCare = strack[4]
         inDungeon = strack[5]
         currentDungeon = strack[6]
         v7 = strack[7]
         strength = sstats[0]
         mentality = sstats[1]
         libido = sstats[2]
         sensitivity = sstats[3]
         HP = sstats[4]
         lust = sstats[5]
         coin = sstats[6]
         strMod = sstats[7]
         mentMod = sstats[8]
         libMod = sstats[9]
         senMod = sstats[10]
         hunger = sstats[11]
         SexP = slevel[0]
         levelUP = slevel[1]
         level = slevel[2]
         babyFactLevel = slevel[3]
         bodyBuildLevel = slevel[4]
         hyperHappyLevel = slevel[5]
         alchemistLevel = slevel[6]
         fetishMasterLevel = slevel[7]
         milkMaidLevel = slevel[8]
         shapeshiftyLevel = slevel[9]
         shapeshiftyFirst = slevel[10]
         shapeshiftySecond = slevel[11]
         runMod = smod[0]
         rapeMod = smod[1]
         cumMod = smod[2]
         cockSizeMod = smod[3]
         milkMod = smod[4]
         carryMod = smod[5]
         vagBellyMod = smod[6]
         pregChanceMod = smod[7]
         extraPregChance = smod[8]
         pregTimeMod = smod[9]
         enticeMod = smod[10]
         milkHPMod = smod[11]
         vagSizeMod = smod[12]
         vagElastic = smod[13]
         changeMod = smod[14]
         HPMod = smod[15]
         SexPMod = smod[16]
         minLust = smod[17]
         milkCap = smod[18]
         coinMod = smod[19]
         hipMod = smod[20]
         buttMod = smod[21]
         bellyMod = smod[22]
         cockMoistMod = smod[23]
         vagMoistMod = smod[24]
         lockTail = smod[25]
         lockFace = smod[26]
         lockSkin = smod[27]
         lockBreasts = smod[28]
         lockEars = smod[29]
         lockLegs = smod[30]
         lockNipples = smod[31]
         lockCock = smod[32]
         gender = squality[0]
         race = squality[1]
         body = squality[2]
         dominant = squality[3]
         hips = squality[4]
         butt = squality[5]
         tallness = squality[6]
         skinType = squality[7]
         tail = squality[8]
         ears = squality[9]
         hair = squality[10]
         hairColor = squality[11]
         hairLength = squality[12]
         legType = squality[13]
         wings = squality[14]
         faceType = squality[15]
         skinColor = squality[16]
         cockTotal = scock[0]
         humanCocks = scock[1]
         horseCocks = scock[2]
         wolfCocks = scock[3]
         catCocks = scock[4]
         rabbitCocks = scock[5]
         lizardCocks = scock[6]
         cockSize = scock[7]
         cockMoist = scock[8]
         balls = scock[9]
         ballSize = scock[10]
         showBalls = scock[11]
         knot = scock[12]
         bugCocks = scock[13]
         breastSize = sgirl[0]
         boobTotal = sgirl[1]
         nippleSize = sgirl[2]
         udders = sgirl[3]
         udderSize = sgirl[4]
         teatSize = sgirl[5]
         clitSize = sgirl[6]
         vagTotal = sgirl[7]
         vagSize = sgirl[8]
         vagMoist = sgirl[9]
         vulvaSize = sgirl[10]
         nipType = sgirl[11]
         attireTop = sgear[0]
         attireBot = sgear[1]
         weapon = sgear[2]
         pregRate = sstatus[0]
         pregnancyTime = sstatus[1]
         pregStatus = sstatus[2]
         eggLaying = sstatus[3]
         eggMaxTime = sstatus[4]
         eggTime = sstatus[5]
         eggRate = sstatus[6]
         exhaustion = sstatus[7]
         exhaustionPenalty = sstatus[8]
         milkEngorgement = sstatus[9]
         milkEngorgementLevel = sstatus[10]
         udderEngorgement = sstatus[11]
         udderEngorgementLevel = sstatus[12]
         heat = sstatus[13]
         heatTime = sstatus[14]
         heatMaxTime = sstatus[15]
         lactation = sstatus[16]
         udderLactation = sstatus[17]
         nipplePlay = sstatus[18]
         udderPlay = sstatus[19]
         blueBalls = sstatus[20]
         teatPump = sstatus[21]
         nipPump = sstatus[22]
         cockPump = sstatus[23]
         clitPump = sstatus[24]
         vulvaPump = sstatus[25]
         masoPot = sstatus[26]
         sMasoPot = sstatus[27]
         babyFree = sstatus[28]
         charmTime = sstatus[29]
         pheromone = sstatus[30]
         eggceleratorTime = sstatus[31]
         eggceleratorDose = sstatus[32]
         bodyOil = sstatus[33]
         lustPenalty = sstatus[34]
         fertileGel = sstatus[35]
         snuggleBall = sstatus[36]
         eggType = sstatus[37]
         milkSuppressant = sstatus[38]
         milkSuppressantLact = sstatus[39]
         milkSuppressantUdder = sstatus[40]
         suppHarness = sstatus[41]
         fertilityStatueCurse = sstatus[42]
         plumpQuats = sstatus[43]
         lilaWetStatus = sstatus[44]
         cockSnakePreg = sstatus[45]
         milkCPoisonNip = sstatus[46]
         milkCPoisonUdd = sstatus[47]
         cockSnakeVenom = sstatus[48]
         humanAffinity = saffinity[0]
         horseAffinity = saffinity[1]
         wolfAffinity = saffinity[2]
         catAffinity = saffinity[3]
         cowAffinity = saffinity[4]
         lizardAffinity = saffinity[5]
         rabbitAffinity = saffinity[6]
         fourBoobAffinity = saffinity[7]
         mouseAffinity = saffinity[8]
         birdAffinity = saffinity[9]
         pigAffinity = saffinity[10]
         twoBoobAffinity = saffinity[11]
         sixBoobAffinity = saffinity[12]
         eightBoobAffinity = saffinity[13]
         tenBoobAffinity = saffinity[14]
         cowTaurAffinity = saffinity[15]
         humanTaurAffinity = saffinity[16]
         skunkAffinity = saffinity[17]
         bugAffinity = saffinity[18]
         lilaRep = srep[0]
         lilaVulva = srep[1]
         lilaMilk = srep[2]
         lilaPreg = srep[3]
         malonRep = srep[4]
         malonPreg = srep[5]
         malonChildren = srep[6]
         mistressRep = srep[7]
         jamieRep = srep[8]
         jamieSize = srep[9]
         jamieChildren = srep[10]
         silRep = srep[11]
         silPreg = srep[12]
         silRate = srep[13]
         silLay = srep[14]
         silGrowthTime = srep[15]
         silTied = srep[16]
         lilaUB = srep[17]
         dairyFarmBrand = srep[18]
         lilaWetness = srep[19]
         jamieButt = srep[20]
         jamieBreasts = srep[21]
         jamieHair = srep[22]
         foundSoftlik = sknowledge[0]
         foundFirmshaft = sknowledge[1]
         foundTieden = sknowledge[2]
         foundSizCalit = sknowledge[3]
         foundOviasis = sknowledge[4]
         foundValley = sknowledge[5]
         foundSanctuary = sknowledge[6]
         defeatedMinotaur = sboss[0]
         defeatedFreakyGirl = sboss[1]
         defeatedSuccubus = sboss[2]
         knowLustDraft = sknowSimpleAlchemy[0]
         knowRejuvPot = sknowSimpleAlchemy[1]
         knowExpPreg = sknowSimpleAlchemy[2]
         knowBallSwell = sknowSimpleAlchemy[3]
         knowMaleEnhance = sknowSimpleAlchemy[4]
         knowSLustDraft = sknowAdvancedAlchemy[0]
         knowSRejuvPot = sknowAdvancedAlchemy[1]
         knowSExpPreg = sknowAdvancedAlchemy[2]
         knowSBallSwell = sknowAdvancedAlchemy[3]
         knowGenSwap = sknowAdvancedAlchemy[4]
         knowMasoPot = sknowAdvancedAlchemy[5]
         knowBabyFree = sknowAdvancedAlchemy[6]
         knowPotPot = sknowAdvancedAlchemy[7]
         knowMilkSuppress = sknowAdvancedAlchemy[8]
         knowSGenSwap = sknowComplexAlchemy[0]
         knowSMasoPot = sknowComplexAlchemy[1]
         knowSBabyFree = sknowComplexAlchemy[2]
         knowSPotPot = sknowComplexAlchemy[3]
         knowPussJuice = sknowComplexAlchemy[4]
         knowPheromone = sknowComplexAlchemy[5]
         knowBazoomba = sknowComplexAlchemy[6]
         maleFetish = smajorFetish[0]
         femaleFetish = smajorFetish[1]
         hermFetish = smajorFetish[2]
         narcissistFetish = smajorFetish[3]
         dependentFetish = smajorFetish[4]
         dominantFetish = smoderateFetish[0]
         submissiveFetish = smoderateFetish[1]
         lboobFetish = smoderateFetish[2]
         sboobFetish = smoderateFetish[3]
         furryFetish = smoderateFetish[4]
         scalyFetish = smoderateFetish[5]
         smoothyFetish = smoderateFetish[6]
         pregnancyFetish = sminorFetish[0]
         bestialityFetish = sminorFetish[1]
         milkFetish = sminorFetish[2]
         sizeFetish = sminorFetish[3]
         unbirthingFetish = sminorFetish[4]
         ovipositionFetish = sminorFetish[5]
         toyFetish = sminorFetish[6]
         hyperFetish = sminorFetish[7]
         humanChildren = skid[0]
         equanChildren = skid[1]
         lupanChildren = skid[2]
         felinChildren = skid[3]
         cowChildren = skid[4]
         lizanChildren = skid[5]
         lizanEggs = skid[6]
         bunnionChildren = skid[7]
         wolfPupChildren = skid[8]
         miceChildren = skid[9]
         birdEggs = skid[10]
         birdChildren = skid[11]
         pigChildren = skid[12]
         calfChildren = skid[13]
         bugEggs = skid[14]
         bugChildren = skid[15]
         skunkChildren = skid[16]
         minotaurChildren = skid[17]
         freakyGirlChildren = skid[18]
         #= .find('').text
         trav = so["trav"]
         bagArray = so["bagSave"]
         bagStackArray = so["bagStackSave"]
         stashArray = so["stashSave"]
         stashStackArray = so["stashStackSave"]
         pregArray = so["pregSave"]
         string = "<data><track><currentState>" + str(currentState) + "</currentState><currentZone>" + str(currentZone) + "</currentZone><day>" + str(day) + "</day><hour>" + str(hour) + "</hour><currentDayCare>" + str(currentDayCare) + "</currentDayCare><inDungeon>" + str(inDungeon) + "</inDungeon><currentDungeon>" + str(currentDungeon) + "</currentDungeon><v7>" + str(0.75) + "</v7></track><stats><strength>" + str(strength) + "</strength><mentality>" + str(mentality) + "</mentality><libido>" + str(libido) + "</libido><sensitivity>" + str(sensitivity) + "</sensitivity><HP>" + str(HP) + "</HP><lust>" + str(lust) + "</lust><coin>" + str(coin) + "</coin><strMod>" + str(strMod) + "</strMod><mentMod>" + str(mentMod) + "</mentMod><libMod>" + str(libMod) + "</libMod><senMod>" + str(senMod) + "</senMod><hunger>" + str(hunger) + "</hunger></stats><level><SexP>" + str(SexP) + "</SexP><levelUP>" + str(levelUP) + "</levelUP><level>" + str(level) + "</level><babyFactLevel>" + str(babyFactLevel) + "</babyFactLevel><bodyBuildLevel>" + str(bodyBuildLevel) + "</bodyBuildLevel><hyperHappyLevel>" + str(hyperHappyLevel) + "</hyperHappyLevel><alchemistLevel>" + str(alchemistLevel) + "</alchemistLevel><fetishMasterLevel>" + str(fetishMasterLevel) + "</fetishMasterLevel><milkMaidLevel>" + str(milkMaidLevel) + "</milkMaidLevel><shapeshiftyLevel>" + str(shapeshiftyLevel) + "</shapeshiftyLevel><shapeshiftyFirst>" + str(shapeshiftyFirst) + "</shapeshiftyFirst><shapeshiftySecond>" + str(shapeshiftySecond) + "</shapeshiftySecond></level><mod><runMod>" + str(runMod) + "</runMod><rapeMod>" + str(rapeMod) + "</rapeMod><cumMod>" + str(cumMod) + "</cumMod><cockSizeMod>" + str(cockSizeMod) + "</cockSizeMod><milkMod>" + str(milkMod) + "</milkMod><carryMod>" + str(carryMod) + "</carryMod><vagBellyMod>" + str(vagBellyMod) + "</vagBellyMod><pregChanceMod>" + str(pregChanceMod) + "</pregChanceMod><extraPregChance>" + str(extraPregChance) + "</extraPregChance><pregTimeMod>" + str(pregTimeMod) + "</pregTimeMod><enticeMod>" + str(enticeMod) + "</enticeMod><milkHPMod>" + str(milkHPMod) + "</milkHPMod><vagSizeMod>" + str(vagSizeMod) + "</vagSizeMod><vagElastic>" + str(vagElastic) + "</vagElastic><changeMod>" + str(changeMod) + "</changeMod><HPMod>" + str(HPMod) + "</HPMod><SexPMod>" + str(SexPMod) + "</SexPMod><minLust>" + str(minLust) + "</minLust><milkCap>" + str(milkCap) + "</milkCap><coinMod>" + str(coinMod) + "</coinMod><hipMod>" + str(hipMod) + "</hipMod><buttMod>" + str(buttMod) + "</buttMod><bellyMod>" + str(bellyMod) + "</bellyMod><cockMoistMod>" + str(cockMoistMod) + "</cockMoistMod><vagMoistMod>" + str(vagMoistMod) + "</vagMoistMod><lockTail>" + str(lockTail) + "</lockTail><lockFace>" + str(lockFace) + "</lockFace><lockSkin>" + str(lockSkin) + "</lockSkin><lockBreasts>" + str(lockBreasts) + "</lockBreasts><lockEars>" + str(lockEars) + "</lockEars><lockLegs>" + str(lockLegs) + "</lockLegs><lockNipples>" + str(lockNipples) + "</lockNipples><lockCock>" + str(lockCock) + "</lockCock></mod><quality><gender>" + str(gender) + "</gender><race>" + str(race) + "</race><body>" + str(body) + "</body><dominant>" + str(dominant) + "</dominant><hips>" + str(hips) + "</hips><butt>" + str(butt) + "</butt><tallness>" + str(tallness) + "</tallness><skinType>" + str(skinType) + "</skinType><tail>" + str(tail) + "</tail><ears>" + str(ears) + "</ears><hair>" + str(hair) + "</hair><hairColor>" + str(hairColor) + "</hairColor><hairLength>" + str(hairLength) + "</hairLength><legType>" + str(legType) + "</legType><wings>" + str(wings) + "</wings><faceType>" + str(faceType) + "</faceType><skinColor>" + str(skinColor) + "</skinColor></quality><cock><cockTotal>" + str(cockTotal) + "</cockTotal><humanCocks>" + str(humanCocks) + "</humanCocks><horseCocks>" + str(horseCocks) + "</horseCocks><wolfCocks>" + str(wolfCocks) + "</wolfCocks><catCocks>" + str(catCocks) + "</catCocks><rabbitCocks>" + str(rabbitCocks) + "</rabbitCocks><lizardCocks>" + str(lizardCocks) + "</lizardCocks><cockSize>" + str(cockSize) + "</cockSize><cockMoist>" + str(cockMoist) + "</cockMoist><balls>" + str(balls) + "</balls><ballSize>" + str(ballSize) + "</ballSize><showBalls>" + str(showBalls) + "</showBalls><knot>" + str(knot) + "</knot><bugCocks>" + str(bugCocks) + "</bugCocks></cock><girl><breastSize>" + str(breastSize) + "</breastSize><boobTotal>" + str(boobTotal) + "</boobTotal><nippleSize>" + str(nippleSize) + "</nippleSize><udders>" + str(udders) + "</udders><udderSize>" + str(udderSize) + "</udderSize><teatSize>" + str(teatSize) + "</teatSize><clitSize>" + str(clitSize) + "</clitSize><vagTotal>" + str(vagTotal) + "</vagTotal><vagSize>" + str(vagSize) + "</vagSize><vagMoist>" + str(vagMoist) + "</vagMoist><vulvaSize>" + str(vulvaSize) + "</vulvaSize><nipType>" + str(nipType) + "</nipType></girl><gear><attireTop>" + str(attireTop) + "</attireTop><attireBot>" + str(attireBot) + "</attireBot><weapon>" + str(weapon) + "</weapon></gear><status><pregRate>" + str(pregRate) + "</pregRate><pregnancyTime>" + str(pregnancyTime) + "</pregnancyTime><pregStatus>" + str(pregStatus) + "</pregStatus><eggLaying>" + str(eggLaying) + "</eggLaying><eggMaxTime>" + str(eggMaxTime) + "</eggMaxTime><eggTime>" + str(eggTime) + "</eggTime><eggRate>" + str(eggRate) + "</eggRate><exhaustion>" + str(exhaustion) + "</exhaustion><exhaustionPenalty>" + str(exhaustionPenalty) + "</exhaustionPenalty><milkEngorgement>" + str(milkEngorgement) + "</milkEngorgement><milkEngorgementLevel>" + str(milkEngorgementLevel) + "</milkEngorgementLevel><udderEngorgement>" + str(udderEngorgement) + "</udderEngorgement><udderEngorgementLevel>" + str(udderEngorgementLevel) + "</udderEngorgementLevel><heat>" + str(heat) + "</heat><heatTime>" + str(heatTime) + "</heatTime><heatMaxTime>" + str(heatMaxTime) + "</heatMaxTime><lactation>" + str(lactation) + "</lactation><udderLactation>" + str(udderLactation) + "</udderLactation><nipplePlay>" + str(nipplePlay) + "</nipplePlay><udderPlay>" + str(udderPlay) + "</udderPlay><blueBalls>" + str(blueBalls) + "</blueBalls><teatPump>" + str(teatPump) + "</teatPump><nipPump>" + str(nipPump) + "</nipPump><cockPump>" + str(cockPump) + "</cockPump><clitPump>" + str(clitPump) + "</clitPump><vulvaPump>" + str(vulvaPump) + "</vulvaPump><masoPot>" + str(masoPot) + "</masoPot><sMasoPot>" + str(sMasoPot) + "</sMasoPot><babyFree>" + str(babyFree) + "</babyFree><charmTime>" + str(charmTime) + "</charmTime><pheromone>" + str(pheromone) + "</pheromone><eggceleratorTime>" + str(eggceleratorTime) + "</eggceleratorTime><eggceleratorDose>" + str(eggceleratorDose) + "</eggceleratorDose><bodyOil>" + str(bodyOil) + "</bodyOil><lustPenalty>" + str(lustPenalty) + "</lustPenalty><fertileGel>" + str(fertileGel) + "</fertileGel><snuggleBall>" + str(snuggleBall) + "</snuggleBall><eggType>" + str(eggType) + "</eggType><milkSuppressant>" + str(milkSuppressant) + "</milkSuppressant><milkSuppressantLact>" + str(milkSuppressantLact) + "</milkSuppressantLact><milkSuppressantUdder>" + str(milkSuppressantUdder) + "</milkSuppressantUdder><suppHarness>" + str(suppHarness) + "</suppHarness><fertilityStatueCurse>" + str(fertilityStatueCurse) + "</fertilityStatueCurse><plumpQuats>" + str(plumpQuats) + "</plumpQuats><lilaWetStatus>" + str(lilaWetStatus) + "</lilaWetStatus><cockSnakePreg>" + str(cockSnakePreg) + "</cockSnakePreg><milkCPoisonNip>" + str(milkCPoisonNip) + "</milkCPoisonNip><milkCPoisonUdd>" + str(milkCPoisonUdd) + "</milkCPoisonUdd><cockSnakeVenom>" + str(cockSnakeVenom) + "</cockSnakeVenom></status><affinity><humanAffinity>" + str(humanAffinity) + "</humanAffinity><horseAffinity>" + str(horseAffinity) + "</horseAffinity><wolfAffinity>" + str(wolfAffinity) + "</wolfAffinity><catAffinity>" + str(catAffinity) + "</catAffinity><cowAffinity>" + str(cowAffinity) + "</cowAffinity><lizardAffinity>" + str(lizardAffinity) + "</lizardAffinity><rabbitAffinity>" + str(rabbitAffinity) + "</rabbitAffinity><fourBoobAffinity>" + str(fourBoobAffinity) + "</fourBoobAffinity><mouseAffinity>" + str(mouseAffinity) + "</mouseAffinity><birdAffinity>" + str(birdAffinity) + "</birdAffinity><pigAffinity>" + str(pigAffinity) + "</pigAffinity><twoBoobAffinity>" + str(twoBoobAffinity) + "</twoBoobAffinity><sixBoobAffinity>" + str(sixBoobAffinity) + "</sixBoobAffinity><eightBoobAffinity>" + str(eightBoobAffinity) + "</eightBoobAffinity><tenBoobAffinity>" + str(tenBoobAffinity) + "</tenBoobAffinity><cowTaurAffinity>" + str(cowTaurAffinity) + "</cowTaurAffinity><humanTaurAffinity>" + str(humanTaurAffinity) + "</humanTaurAffinity><skunkAffinity>" + str(skunkAffinity) + "</skunkAffinity><bugAffinity>" + str(bugAffinity) + "</bugAffinity></affinity><rep><lilaRep>" + str(lilaRep) + "</lilaRep><lilaVulva>" + str(lilaVulva) + "</lilaVulva><lilaMilk>" + str(lilaMilk) + "</lilaMilk><lilaPreg>" + str(lilaPreg) + "</lilaPreg><malonRep>" + str(malonRep) + "</malonRep><malonPreg>" + str(malonPreg) + "</malonPreg><malonChildren>" + str(malonChildren) + "</malonChildren><mistressRep>" + str(mistressRep) + "</mistressRep><jamieRep>" + str(jamieRep) + "</jamieRep><jamieSize>" + str(jamieSize) + "</jamieSize><jamieChildren>" + str(jamieChildren) + "</jamieChildren><silRep>" + str(silRep) + "</silRep><silPreg>" + str(silPreg) + "</silPreg><silRate>" + str(silRate) + "</silRate><silLay>" + str(silLay) + "</silLay><silGrowthTime>" + str(silGrowthTime) + "</silGrowthTime><silTied>" + str(silTied) + "</silTied><lilaUB>" + str(lilaUB) + "</lilaUB><dairyFarmBrand>" + str(dairyFarmBrand) + "</dairyFarmBrand><lilaWetness>" + str(lilaWetness) + "</lilaWetness><jamieButt>" + str(jamieButt) + "</jamieButt><jamieBreasts>" + str(jamieBreasts) + "</jamieBreasts><jamieHair>" + str(jamieHair) + "</jamieHair></rep><knowledge><foundSoftlik>" + str(foundSoftlik) + "</foundSoftlik><foundFirmshaft>" + str(foundFirmshaft) + "</foundFirmshaft><foundTieden>" + str(foundTieden) + "</foundTieden><foundSizCalit>" + str(foundSizCalit) + "</foundSizCalit><foundOviasis>" + str(foundOviasis) + "</foundOviasis><foundValley>" + str(foundValley) + "</foundValley><foundSanctuary>" + str(foundSanctuary) + "</foundSanctuary></knowledge><boss><defeatedMinotaur>" + str(defeatedMinotaur) + "</defeatedMinotaur><defeatedFreakyGirl>" + str(defeatedFreakyGirl) + "</defeatedFreakyGirl><defeatedSuccubus>" + str(defeatedSuccubus) + "</defeatedSuccubus></boss><knowSimpleAlchemy><knowLustDraft>" + str(knowLustDraft) + "</knowLustDraft><knowRejuvPot>" + str(knowRejuvPot) + "</knowRejuvPot><knowExpPreg>" + str(knowExpPreg) + "</knowExpPreg><knowBallSwell>" + str(knowBallSwell) + "</knowBallSwell><knowMaleEnhance>" + str(knowMaleEnhance) + "</knowMaleEnhance></knowSimpleAlchemy><knowAdvancedAlchemy><knowSLustDraft>" + str(knowSLustDraft) + "</knowSLustDraft><knowSRejuvPot>" + str(knowSRejuvPot) + "</knowSRejuvPot><knowSExpPreg>" + str(knowSExpPreg) + "</knowSExpPreg><knowSBallSwell>" + str(knowSBallSwell) + "</knowSBallSwell><knowGenSwap>" + str(knowGenSwap) + "</knowGenSwap><knowMasoPot>" + str(knowMasoPot) + "</knowMasoPot><knowBabyFree>" + str(knowBabyFree) + "</knowBabyFree><knowPotPot>" + str(knowPotPot) + "</knowPotPot><knowMilkSuppress>" + str(knowMilkSuppress) + "</knowMilkSuppress></knowAdvancedAlchemy><knowComplexAlchemy><knowSGenSwap>" + str(knowSGenSwap) + "</knowSGenSwap><knowSMasoPot>" + str(knowSMasoPot) + "</knowSMasoPot><knowSBabyFree>" + str(knowSBabyFree) + "</knowSBabyFree><knowSPotPot>" + str(knowSPotPot) + "</knowSPotPot><knowPussJuice>" + str(knowPussJuice) + "</knowPussJuice><knowPheromone>" + str(knowPheromone) + "</knowPheromone><knowBazoomba>" + str(knowBazoomba) + "</knowBazoomba></knowComplexAlchemy><majorFetish><maleFetish>" + str(maleFetish) + "</maleFetish><femaleFetish>" + str(femaleFetish) + "</femaleFetish><hermFetish>" + str(hermFetish) + "</hermFetish><narcissistFetish>" + str(narcissistFetish) + "</narcissistFetish><dependentFetish>" + str(dependentFetish) + "</dependentFetish></majorFetish><moderateFetish><dominantFetish>" + str(dominantFetish) + "</dominantFetish><submissiveFetish>" + str(submissiveFetish) + "</submissiveFetish><lboobFetish>" + str(lboobFetish) + "</lboobFetish><sboobFetish>" + str(sboobFetish) + "</sboobFetish><furryFetish>" + str(furryFetish) + "</furryFetish><scalyFetish>" + str(scalyFetish) + "</scalyFetish><smoothyFetish>" + str(smoothyFetish) + "</smoothyFetish></moderateFetish><minorFetish><pregnancyFetish>" + str(pregnancyFetish) + "</pregnancyFetish><bestialityFetish>" + str(bestialityFetish) + "</bestialityFetish><milkFetish>" + str(milkFetish) + "</milkFetish><sizeFetish>" + str(sizeFetish) + "</sizeFetish><unbirthingFetish>" + str(unbirthingFetish) + "</unbirthingFetish><ovipositionFetish>" + str(ovipositionFetish) + "</ovipositionFetish><toyFetish>" + str(toyFetish) + "</toyFetish><hyperFetish>" + str(hyperFetish) + "</hyperFetish></minorFetish><kid><humanChildren>" + str(humanChildren) + "</humanChildren><equanChildren>" + str(equanChildren) + "</equanChildren><lupanChildren>" + str(lupanChildren) + "</lupanChildren><felinChildren>" + str(felinChildren) + "</felinChildren><cowChildren>" + str(cowChildren) + "</cowChildren><lizanChildren>" + str(lizanChildren) + "</lizanChildren><lizanEggs>" + str(lizanEggs) + "</lizanEggs><bunnionChildren>" + str(bunnionChildren) + "</bunnionChildren><wolfPupChildren>" + str(wolfPupChildren) + "</wolfPupChildren><miceChildren>" + str(miceChildren) + "</miceChildren><birdEggs>" + str(birdEggs) + "</birdEggs><birdChildren>" + str(birdChildren) + "</birdChildren><pigChildren>" + str(pigChildren) + "</pigChildren><calfChildren>" + str(calfChildren) + "</calfChildren><bugEggs>" + str(bugEggs) + "</bugEggs><bugChildren>" + str(bugChildren) + "</bugChildren><skunkChildren>" + str(skunkChildren) + "</skunkChildren><minotaurChildren>" + str(minotaurChildren) + "</minotaurChildren><freakyGirlChildren>" + str(freakyGirlChildren) + "</freakyGirlChildren></kid><trav></trav><bag>"
         for i in range(0, 26):
            string = string + "<slot" + str(i) + ">" + str(bagArray[i]) + "</slot" + str(i) + ">"
         string = string + "</bag><bagStack>"
         for i in range(0, 26):
            string = string + "<slot" + str(i) + ">" + str(bagStackArray[i]) + "</slot" + str(i) + ">"
         string = string + "</bagStack><stash>"
         for i in range(0, 26):
            string = string + "<slot" + str(i) + ">" + str(stashArray[i]) + "</slot" + str(i) + ">"
         string = string + "</stash><stashStack>"
         for i in range(0, 26):
            string = string + "<slot" + str(i) + ">" + str(stashStackArray[i]) + "</slot" + str(i) + ">"
         string = string + "</stashStack><preg>"
         i = 0
         while i < len(pregArray):
            string = string + "<i" + str(i) + ">" + str(pregArray[i]) + "</i" + str(i) + ">"
            i += 1
         string = string + "</preg></data>"
         data = xmlminidom.parseString(string)
         spref = data.toprettyxml(indent ="\t")
         with open(args[2], "w") as xmldoc:
            xmldoc.write(spref)
   else:
      phelp()
   


