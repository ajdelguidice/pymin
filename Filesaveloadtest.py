import xml.etree.ElementTree as xmletree

def originalsavedata():
   """
   bagSaveArray = [];
   bagStackSaveArray = [];
   stashSaveArray = [];
   stashStackSaveArray = [];
   pregSaveArray = [];
   trackSave = [];
   trackSave[0] = this.currentState;
   trackSave[1] = this.currentZone;
   trackSave[2] = this.day;
   trackSave[3] = this.hour;
   trackSave[4] = this.currentDayCare;
   trackSave[5] = this.inDungeon;
   trackSave[6] = this.currentDungeon;
   trackSave[7] = 0.75;
   statsSave = [];
   statsSave[0] = this.strength;
   statsSave[1] = this.mentality;
   statsSave[2] = this.libido;
   statsSave[3] = this.sensitivity;
   statsSave[4] = this.HP;
   statsSave[5] = this.lust;
   statsSave[6] = this.coin;
   statsSave[7] = this.strMod;
   statsSave[8] = this.mentMod;
   statsSave[9] = this.libMod;
   statsSave[10] = this.senMod;
   statsSave[11] = this.hunger;
   levelSave = [];
   levelSave[0] = this.SexP;
   levelSave[1] = this.levelUP;
   levelSave[2] = this.level;
   levelSave[3] = this.babyFactLevel;
   levelSave[4] = this.bodyBuildLevel;
   levelSave[5] = this.hyperHappyLevel;
   levelSave[6] = this.alchemistLevel;
   levelSave[7] = this.fetishMasterLevel;
   levelSave[8] = this.milkMaidLevel;
   levelSave[9] = this.shapeshiftyLevel;
   levelSave[10] = this.shapeshiftyFirst;
   levelSave[11] = this.shapeshiftySecond;
   modSave = [];
   modSave[0] = this.runMod;
   modSave[1] = this.rapeMod;
   modSave[2] = this.cumMod;
   modSave[3] = this.cockSizeMod;
   modSave[4] = this.milkMod;
   modSave[5] = this.carryMod;
   modSave[6] = this.vagBellyMod;
   modSave[7] = this.pregChanceMod;
   modSave[8] = this.extraPregChance;
   modSave[9] = this.pregTimeMod;
   modSave[10] = this.enticeMod;
   modSave[11] = this.milkHPMod;
   modSave[12] = this.vagSizeMod;
   modSave[13] = this.vagElastic;
   modSave[14] = this.changeMod;
   modSave[15] = this.HPMod;
   modSave[16] = this.SexPMod;
   modSave[17] = this.minLust;
   modSave[18] = this.milkCap;
   modSave[19] = this.coinMod;
   modSave[20] = this.hipMod;
   modSave[21] = this.buttMod;
   modSave[22] = this.bellyMod;
   modSave[23] = this.cockMoistMod;
   modSave[24] = this.vagMoistMod;
   modSave[25] = this.lockTail;
   modSave[26] = this.lockFace;
   modSave[27] = this.lockSkin;
   modSave[28] = this.lockBreasts;
   modSave[29] = this.lockEars;
   modSave[30] = this.lockLegs;
   modSave[31] = this.lockNipples;
   modSave[32] = this.lockCock;
   qualitySave = [];
   qualitySave[0] = this.gender;
   qualitySave[1] = this.race;
   qualitySave[2] = this.body;
   qualitySave[3] = this.dominant;
   qualitySave[4] = this.hips;
   qualitySave[5] = this.butt;
   qualitySave[6] = this.tallness;
   qualitySave[7] = this.skinType;
   qualitySave[8] = this.tail;
   qualitySave[9] = this.ears;
   qualitySave[10] = this.hair;
   qualitySave[11] = this.hairColor;
   qualitySave[12] = this.hairLength;
   qualitySave[13] = this.legType;
   qualitySave[14] = this.wings;
   qualitySave[15] = this.faceType;
   qualitySave[16] = this.skinColor;
   cockSave = [];
   cockSave[0] = this.cockTotal;
   cockSave[1] = this.humanCocks;
   cockSave[2] = this.horseCocks;
   cockSave[3] = this.wolfCocks;
   cockSave[4] = this.catCocks;
   cockSave[5] = this.rabbitCocks;
   cockSave[6] = this.lizardCocks;
   cockSave[7] = this.cockSize;
   cockSave[8] = this.cockMoist;
   cockSave[9] = this.balls;
   cockSave[10] = this.ballSize;
   cockSave[11] = this.showBalls;
   cockSave[12] = this.knot;
   cockSave[13] = this.bugCocks;
   girlSave = [];
   girlSave[0] = this.breastSize;
   girlSave[1] = this.boobTotal;
   girlSave[2] = this.nippleSize;
   girlSave[3] = this.udders;
   girlSave[4] = this.udderSize;
   girlSave[5] = this.teatSize;
   girlSave[6] = this.clitSize;
   girlSave[7] = this.vagTotal;
   girlSave[8] = this.vagSize;
   girlSave[9] = this.vagMoist;
   girlSave[10] = this.vulvaSize;
   girlSave[11] = this.nipType;
   gearSave = [];
   gearSave[0] = this.attireTop;
   gearSave[1] = this.attireBot;
   gearSave[2] = this.weapon;
   statusSave = [];
   statusSave[0] = this.pregRate;
   statusSave[1] = this.pregnancyTime;
   statusSave[2] = this.pregStatus;
   statusSave[3] = this.eggLaying;
   statusSave[4] = this.eggMaxTime;
   statusSave[5] = this.eggTime;
   statusSave[6] = this.eggRate;
   statusSave[7] = this.exhaustion;
   statusSave[8] = this.exhaustionPenalty;
   statusSave[9] = this.milkEngorgement;
   statusSave[10] = this.milkEngorgementLevel;
   statusSave[11] = this.udderEngorgement;
   statusSave[12] = this.udderEngorgementLevel;
   statusSave[13] = this.heat;
   statusSave[14] = this.heatTime;
   statusSave[15] = this.heatMaxTime;
   statusSave[16] = this.lactation;
   statusSave[17] = this.udderLactation;
   statusSave[18] = this.nipplePlay;
   statusSave[19] = this.udderPlay;
   statusSave[20] = this.blueBalls;
   statusSave[21] = this.teatPump;
   statusSave[22] = this.nipPump;
   statusSave[23] = this.cockPump;
   statusSave[24] = this.clitPump;
   statusSave[25] = this.vulvaPump;
   statusSave[26] = this.masoPot;
   statusSave[27] = this.sMasoPot;
   statusSave[28] = this.babyFree;
   statusSave[29] = this.charmTime;
   statusSave[30] = this.pheromone;
   statusSave[31] = this.eggceleratorTime;
   statusSave[32] = this.eggceleratorDose;
   statusSave[33] = this.bodyOil;
   statusSave[34] = this.lustPenalty;
   statusSave[35] = this.fertileGel;
   statusSave[36] = this.snuggleBall;
   statusSave[37] = this.eggType;
   statusSave[38] = this.milkSuppressant;
   statusSave[39] = this.milkSuppressantLact;
   statusSave[40] = this.milkSuppressantUdder;
   statusSave[41] = this.suppHarness;
   statusSave[42] = this.fertilityStatueCurse;
   statusSave[43] = this.plumpQuats;
   statusSave[44] = this.lilaWetStatus;
   statusSave[45] = this.cockSnakePreg;
   statusSave[46] = this.milkCPoisonNip;
   statusSave[47] = this.milkCPoisonUdd;
   statusSave[48] = this.cockSnakeVenom;
   affinitySave = [];
   affinitySave[0] = this.humanAffinity;
   affinitySave[1] = this.horseAffinity;
   affinitySave[2] = this.wolfAffinity;
   affinitySave[3] = this.catAffinity;
   affinitySave[4] = this.cowAffinity;
   affinitySave[5] = this.lizardAffinity;
   affinitySave[6] = this.rabbitAffinity;
   affinitySave[7] = this.fourBoobAffinity;
   affinitySave[8] = this.mouseAffinity;
   affinitySave[9] = this.birdAffinity;
   affinitySave[10] = this.pigAffinity;
   affinitySave[11] = this.twoBoobAffinity;
   affinitySave[12] = this.sixBoobAffinity;
   affinitySave[13] = this.eightBoobAffinity;
   affinitySave[14] = this.tenBoobAffinity;
   affinitySave[15] = this.cowTaurAffinity;
   affinitySave[16] = this.humanTaurAffinity;
   affinitySave[17] = this.skunkAffinity;
   affinitySave[18] = this.bugAffinity;
   repSave = [];
   repSave[0] = this.lilaRep;
   repSave[1] = this.lilaVulva;
   repSave[2] = this.lilaMilk;
   repSave[3] = this.lilaPreg;
   repSave[4] = this.malonRep;
   repSave[5] = this.malonPreg;
   repSave[6] = this.malonChildren;
   repSave[7] = this.mistressRep;
   repSave[8] = this.jamieRep;
   repSave[9] = this.jamieSize;
   repSave[10] = this.jamieChildren;
   repSave[11] = this.silRep;
   repSave[12] = this.silPreg;
   repSave[13] = this.silRate;
   repSave[14] = this.silLay;
   repSave[15] = this.silGrowthTime;
   repSave[16] = this.silTied;
   repSave[17] = this.lilaUB;
   repSave[18] = this.dairyFarmBrand;
   repSave[19] = this.lilaWetness;
   repSave[20] = this.jamieButt;
   repSave[21] = this.jamieBreasts;
   repSave[22] = this.jamieHair;
   knowledgeSave = [];
   knowledgeSave[0] = this.foundSoftlik;
   knowledgeSave[1] = this.foundFirmshaft;
   knowledgeSave[2] = this.foundTieden;
   knowledgeSave[3] = this.foundSizCalit;
   knowledgeSave[4] = this.foundOviasis;
   knowledgeSave[5] = this.foundValley;
   knowledgeSave[6] = this.foundSanctuary;
   bossSave = [];
   bossSave[0] = this.defeatedMinotaur;
   bossSave[1] = this.defeatedFreakyGirl;
   bossSave[2] = this.defeatedSuccubus;
   knowSimpleAlchemySave = [];
   knowSimpleAlchemySave[0] = this.knowLustDraft;
   knowSimpleAlchemySave[1] = this.knowRejuvPot;
   knowSimpleAlchemySave[2] = this.knowExpPreg;
   knowSimpleAlchemySave[3] = this.knowBallSwell;
   knowSimpleAlchemySave[4] = this.knowMaleEnhance;
   knowAdvancedAlchemySave = [];
   knowAdvancedAlchemySave[0] = this.knowSLustDraft;
   knowAdvancedAlchemySave[1] = this.knowSRejuvPot;
   knowAdvancedAlchemySave[2] = this.knowSExpPreg;
   knowAdvancedAlchemySave[3] = this.knowSBallSwell;
   knowAdvancedAlchemySave[4] = this.knowGenSwap;
   knowAdvancedAlchemySave[5] = this.knowMasoPot;
   knowAdvancedAlchemySave[6] = this.knowBabyFree;
   knowAdvancedAlchemySave[7] = this.knowPotPot;
   knowAdvancedAlchemySave[8] = this.knowMilkSuppress;
   knowComplexAlchemySave = [];
   knowComplexAlchemySave[0] = this.knowSGenSwap;
   knowComplexAlchemySave[1] = this.knowSMasoPot;
   knowComplexAlchemySave[2] = this.knowSBabyFree;
   knowComplexAlchemySave[3] = this.knowSPotPot;
   knowComplexAlchemySave[4] = this.knowPussJuice;
   knowComplexAlchemySave[5] = this.knowPheromone;
   knowComplexAlchemySave[6] = this.knowBazoomba;
   majorFetishSave = [];
   majorFetishSave[0] = this.maleFetish;
   majorFetishSave[1] = this.femaleFetish;
   majorFetishSave[2] = this.hermFetish;
   majorFetishSave[3] = this.narcissistFetish;
   majorFetishSave[4] = this.dependentFetish;
   moderateFetishSave = [];
   moderateFetishSave[0] = this.dominantFetish;
   moderateFetishSave[1] = this.submissiveFetish;
   moderateFetishSave[2] = this.lboobFetish;
   moderateFetishSave[3] = this.sboobFetish;
   moderateFetishSave[4] = this.furryFetish;
   moderateFetishSave[5] = this.scalyFetish;
   moderateFetishSave[6] = this.smoothyFetish;
   minorFetishSave = [];
   minorFetishSave[0] = this.pregnancyFetish;
   minorFetishSave[1] = this.bestialityFetish;
   minorFetishSave[2] = this.milkFetish;
   minorFetishSave[3] = this.sizeFetish;
   minorFetishSave[4] = this.unbirthingFetish;
   minorFetishSave[5] = this.ovipositionFetish;
   minorFetishSave[6] = this.toyFetish;
   minorFetishSave[7] = this.hyperFetish;
   kidSave = [];
   kidSave[0] = this.humanChildren;
   kidSave[1] = this.equanChildren;
   kidSave[2] = this.lupanChildren;
   kidSave[3] = this.felinChildren;
   kidSave[4] = this.cowChildren;
   kidSave[5] = this.lizanChildren;
   kidSave[6] = this.lizanEggs;
   kidSave[7] = this.bunnionChildren;
   kidSave[8] = this.wolfPupChildren;
   kidSave[9] = this.miceChildren;
   kidSave[10] = this.birdEggs;
   kidSave[11] = this.birdChildren;
   kidSave[12] = this.pigChildren;
   kidSave[13] = this.calfChildren;
   kidSave[14] = this.bugEggs;
   kidSave[15] = this.bugChildren;
   kidSave[16] = this.skunkChildren;
   kidSave[17] = this.minotaurChildren;
   kidSave[18] = this.freakyGirlChildren;
   travSave = [];
   this.i = 0;
   while(this.i < this.pregArray.length)
   {
      pregSaveArray[this.i] = this.pregArray[this.i];
      ++this.i;
   }
   for(this.i = 0; this.i < this.bagArray.length; ++this.i)
   {
      bagSaveArray[this.i] = this.bagArray[this.i];
      bagStackSaveArray[this.i] = this.bagStackArray[this.i];
   }
   for(this.i = 0; this.i < this.stashArray.length; ++this.i)
   {
      stashSaveArray[this.i] = this.stashArray[this.i];
      stashStackSaveArray[this.i] = this.stashStackArray[this.i];
   }
   so.data.versionNumber = this.versionNumber;
   so.data.track = trackSave;
   so.data.stats = statsSave;
   so.data.level = levelSave;
   so.data.mod = modSave;
   so.data.quality = qualitySave;
   so.data.cock = cockSave;
   so.data.girl = girlSave;
   so.data.gear = gearSave;
   so.data.status = statusSave;
   so.data.affinity = affinitySave;
   so.data.rep = repSave;
   so.data.knowledge = knowledgeSave;
   so.data.boss = bossSave;
   so.data.knowSimpleAlchemy = knowSimpleAlchemySave;
   so.data.knowAdvancedAlchemy = knowAdvancedAlchemySave;
   so.data.knowComplexAlchemy = knowComplexAlchemySave;
   so.data.majorFetish = majorFetishSave;
   so.data.moderateFetish = moderateFetishSave;
   so.data.minorFetish = minorFetishSave;
   so.data.kid = kidSave;
   so.data.trav = travSave;
   so.data.bagSave = bagSaveArray;
   so.data.bagStackSave = bagStackSaveArray;
   so.data.stashSave = stashSaveArray;
   so.data.stashStackSave = stashStackSaveArray;
   so.data.pregSave = pregSaveArray;
   """
   pass

def originalloaddata():
   """
   _loc2_ = param1.data.track;
   _loc3_ = param1.data.stats;
   _loc4_ = param1.data.level;
   _loc5_ = param1.data.mod;
   _loc6_ = param1.data.quality;
   _loc7_ = param1.data.cock;
   _loc8_ = param1.data.girl;
   _loc9_ = param1.data.gear;
   _loc10_ = param1.data.status;
   _loc11_ = param1.data.affinity;
   _loc12_ = param1.data.rep;
   _loc13_ = param1.data.knowledge;
   if(param1.data.boss)
   {
      _loc27_ = param1.data.boss;
   }
   else
   {
      _loc27_ = [];
   }
   _loc14_ = param1.data.knowSimpleAlchemy;
   _loc15_ = param1.data.knowAdvancedAlchemy;
   _loc16_ = param1.data.knowComplexAlchemy;
   _loc17_ = param1.data.majorFetish;
   _loc18_ = param1.data.moderateFetish;
   _loc19_ = param1.data.minorFetish;
   _loc20_ = param1.data.kid;
   var _loc21_:Array = param1.data.trav;
   _loc22_ = param1.data.bagSave;
   _loc23_ = param1.data.stashSave;
   _loc24_ = param1.data.bagStackSave;
   _loc25_ = param1.data.stashStackSave;
   _loc26_ = param1.data.pregSave;
   if(!_loc14_)
   {
      _loc14_ = [];
   }
   if(!_loc15_)
   {
      _loc15_ = [];
   }
   if(!_loc16_)
   {
      _loc16_ = [];
   }
   if(!_loc22_)
   {
      _loc24_ = [];
      _loc22_ = [];
      _loc23_ = [];
      _loc25_ = [];
      _loc28_ = param1.data.itemSave;
      _loc29_ = param1.data.stashSave;
      _loc30_ = param1.data.stackSave;
      _loc31_ = param1.data.stashStackSave;
      for(this.i = 1; this.i <= _loc28_.length; ++this.i)
      {
         if(_loc28_[this.i] > 10)
         {
            _loc22_.push(_loc28_[this.i]);
            _loc24_.push(_loc30_[this.i]);
         }
      }
      if(_loc22_.length < 27)
      {
         for(this.i = _loc22_.length; this.i < 27; ++this.i)
         {
            _loc22_.push(0);
            _loc24_.push(0);
         }
      }
      for(this.i = 1; this.i <= _loc29_.length; ++this.i)
      {
         if(_loc29_[this.i] > 10)
         {
            _loc23_.push(_loc29_[this.i]);
            _loc25_.push(_loc31_[this.i]);
         }
      }
      if(_loc23_.length < 27)
      {
         for(this.i = _loc23_.length; this.i < 27; ++this.i)
         {
            _loc23_.push(0);
            _loc25_.push(0);
         }
      }
   }
   this.currentState = _loc2_[0];
   this.currentZone = _loc2_[1];
   this.day = _loc2_[2];
   this.hour = _loc2_[3];
   this.currentDayCare = _loc2_[4];
   this.inDungeon = _loc2_[5];
   this.currentDungeon = _loc2_[6];
   this.strength = _loc3_[0];
   this.mentality = _loc3_[1];
   this.libido = _loc3_[2];
   this.sensitivity = _loc3_[3];
   this.HP = _loc3_[4];
   this.lust = _loc3_[5];
   this.coin = _loc3_[6];
   this.strMod = _loc3_[7];
   this.mentMod = _loc3_[8];
   this.libMod = _loc3_[9];
   this.senMod = _loc3_[10];
   this.hunger = _loc3_[11];
   this.SexP = _loc4_[0];
   this.levelUP = _loc4_[1];
   this.level = _loc4_[2];
   this.babyFactLevel = _loc4_[3];
   this.bodyBuildLevel = _loc4_[4];
   this.hyperHappyLevel = _loc4_[5];
   this.alchemistLevel = _loc4_[6];
   this.fetishMasterLevel = _loc4_[7];
   this.milkMaidLevel = _loc4_[8];
   this.shapeshiftyLevel = _loc4_[9];
   this.shapeshiftyFirst = _loc4_[10];
   this.shapeshiftySecond = _loc4_[11];
   this.runMod = _loc5_[0];
   this.rapeMod = _loc5_[1];
   this.cumMod = _loc5_[2];
   this.cockSizeMod = _loc5_[3];
   this.milkMod = _loc5_[4];
   this.carryMod = _loc5_[5];
   this.vagBellyMod = _loc5_[6];
   this.pregChanceMod = _loc5_[7];
   this.extraPregChance = _loc5_[8];
   this.pregTimeMod = _loc5_[9];
   this.enticeMod = _loc5_[10];
   this.milkHPMod = _loc5_[11];
   this.vagSizeMod = _loc5_[12];
   this.vagElastic = _loc5_[13];
   this.changeMod = _loc5_[14];
   this.HPMod = _loc5_[15];
   this.SexPMod = _loc5_[16];
   this.minLust = _loc5_[17];
   this.milkCap = _loc5_[18];
   this.coinMod = _loc5_[19];
   this.hipMod = _loc5_[20];
   this.buttMod = _loc5_[21];
   this.bellyMod = _loc5_[22];
   this.cockMoistMod = _loc5_[23];
   this.vagMoistMod = _loc5_[24];
   this.lockTail = _loc5_[25];
   this.lockFace = _loc5_[26];
   this.lockSkin = _loc5_[27];
   this.lockBreasts = _loc5_[28];
   this.lockEars = _loc5_[29];
   this.lockLegs = _loc5_[30];
   this.lockNipples = _loc5_[31];
   this.lockCock = _loc5_[32];
   this.gender = _loc6_[0];
   this.race = _loc6_[1];
   this.body = _loc6_[2];
   this.dominant = _loc6_[3];
   this.hips = _loc6_[4];
   this.butt = _loc6_[5];
   this.tallness = _loc6_[6];
   this.skinType = _loc6_[7];
   this.tail = _loc6_[8];
   this.ears = _loc6_[9];
   this.hair = _loc6_[10];
   this.hairColor = _loc6_[11];
   this.hairLength = _loc6_[12];
   this.legType = _loc6_[13];
   this.wings = _loc6_[14];
   this.faceType = _loc6_[15];
   this.skinColor = _loc6_[16];
   this.cockTotal = _loc7_[0];
   this.humanCocks = _loc7_[1];
   this.horseCocks = _loc7_[2];
   this.wolfCocks = _loc7_[3];
   this.catCocks = _loc7_[4];
   this.rabbitCocks = _loc7_[5];
   this.lizardCocks = _loc7_[6];
   this.cockSize = _loc7_[7];
   this.cockMoist = _loc7_[8];
   this.balls = _loc7_[9];
   this.ballSize = _loc7_[10];
   this.showBalls = _loc7_[11];
   this.knot = _loc7_[12];
   this.bugCocks = _loc7_[13];
   this.breastSize = _loc8_[0];
   this.boobTotal = _loc8_[1];
   this.nippleSize = _loc8_[2];
   this.udders = _loc8_[3];
   this.udderSize = _loc8_[4];
   this.teatSize = _loc8_[5];
   this.clitSize = _loc8_[6];
   this.vagTotal = _loc8_[7];
   this.vagSize = _loc8_[8];
   this.vagMoist = _loc8_[9];
   this.vulvaSize = _loc8_[10];
   this.nipType = _loc8_[11];
   this.attireTop = _loc9_[0];
   this.attireBot = _loc9_[1];
   this.weapon = _loc9_[2];
   this.pregRate = _loc10_[0];
   this.pregnancyTime = _loc10_[1];
   this.pregStatus = _loc10_[2];
   this.eggLaying = _loc10_[3];
   this.eggMaxTime = _loc10_[4];
   this.eggTime = _loc10_[5];
   this.eggRate = _loc10_[6];
   this.exhaustion = _loc10_[7];
   this.exhaustionPenalty = _loc10_[8];
   this.milkEngorgement = _loc10_[9];
   this.milkEngorgementLevel = _loc10_[10];
   this.udderEngorgement = _loc10_[11];
   this.udderEngorgementLevel = _loc10_[12];
   this.heat = _loc10_[13];
   this.heatTime = _loc10_[14];
   this.heatMaxTime = _loc10_[15];
   this.lactation = _loc10_[16];
   this.udderLactation = _loc10_[17];
   this.nipplePlay = _loc10_[18];
   this.udderPlay = _loc10_[19];
   this.blueBalls = _loc10_[20];
   this.teatPump = _loc10_[21];
   this.nipPump = _loc10_[22];
   this.cockPump = _loc10_[23];
   this.clitPump = _loc10_[24];
   this.vulvaPump = _loc10_[25];
   this.masoPot = _loc10_[26];
   this.sMasoPot = _loc10_[27];
   this.babyFree = _loc10_[28];
   this.charmTime = _loc10_[29];
   this.pheromone = _loc10_[30];
   this.eggceleratorTime = _loc10_[31];
   this.eggceleratorDose = _loc10_[32];
   this.bodyOil = _loc10_[33];
   this.lustPenalty = _loc10_[34];
   this.fertileGel = _loc10_[35];
   this.snuggleBall = _loc10_[36];
   this.eggType = _loc10_[37];
   this.milkSuppressant = _loc10_[38];
   this.milkSuppressantLact = _loc10_[39];
   this.milkSuppressantUdder = _loc10_[40];
   this.suppHarness = _loc10_[41];
   this.fertilityStatueCurse = _loc10_[42];
   this.plumpQuats = _loc10_[43];
   this.lilaWetStatus = _loc10_[44];
   this.cockSnakePreg = _loc10_[45];
   this.milkCPoisonNip = _loc10_[46];
   this.milkCPoisonUdd = _loc10_[47];
   this.cockSnakeVenom = _loc10_[48];
   this.humanAffinity = _loc11_[0];
   this.horseAffinity = _loc11_[1];
   this.wolfAffinity = _loc11_[2];
   this.catAffinity = _loc11_[3];
   this.cowAffinity = _loc11_[4];
   this.lizardAffinity = _loc11_[5];
   this.rabbitAffinity = _loc11_[6];
   this.fourBoobAffinity = _loc11_[7];
   this.mouseAffinity = _loc11_[8];
   this.birdAffinity = _loc11_[9];
   this.pigAffinity = _loc11_[10];
   this.twoBoobAffinity = _loc11_[11];
   this.sixBoobAffinity = _loc11_[12];
   this.eightBoobAffinity = _loc11_[13];
   this.tenBoobAffinity = _loc11_[14];
   this.cowTaurAffinity = _loc11_[15];
   this.humanTaurAffinity = _loc11_[16];
   this.skunkAffinity = _loc11_[17];
   this.bugAffinity = _loc11_[18];
   this.lilaRep = _loc12_[0];
   this.lilaVulva = _loc12_[1];
   this.lilaMilk = _loc12_[2];
   this.lilaPreg = _loc12_[3];
   this.malonRep = _loc12_[4];
   this.malonPreg = _loc12_[5];
   this.malonChildren = _loc12_[6];
   this.mistressRep = _loc12_[7];
   this.jamieRep = _loc12_[8];
   this.jamieSize = _loc12_[9];
   this.jamieChildren = _loc12_[10];
   this.silRep = _loc12_[11];
   this.silPreg = _loc12_[12];
   this.silRate = _loc12_[13];
   this.silLay = _loc12_[14];
   this.silGrowthTime = _loc12_[15];
   this.silTied = _loc12_[16];
   this.lilaUB = _loc12_[17];
   this.dairyFarmBrand = _loc12_[18];
   this.lilaWetness = _loc12_[19];
   this.jamieButt = _loc12_[20];
   this.jamieBreasts = _loc12_[21];
   this.jamieHair = _loc12_[22];
   if(this.jamieSize == 0 && this.jamieRep > 5)
   {
      this.jamieRep = 3;
   }
   if(this.jamieSize == 0)
   {
      this.jamieSize = 4;
   }
   this.foundSoftlik = _loc13_[0];
   this.foundFirmshaft = _loc13_[1];
   this.foundTieden = _loc13_[2];
   this.foundSizCalit = _loc13_[3];
   this.foundOviasis = _loc13_[4];
   this.foundValley = _loc13_[5];
   this.foundSanctuary = _loc13_[6];
   this.defeatedMinotaur = _loc27_[0];
   this.defeatedFreakyGirl = _loc27_[1];
   this.defeatedSuccubus = _loc27_[2];
   this.knowLustDraft = _loc14_[0];
   this.knowRejuvPot = _loc14_[1];
   this.knowExpPreg = _loc14_[2];
   this.knowBallSwell = _loc14_[3];
   this.knowMaleEnhance = _loc14_[4];
   this.knowSLustDraft = _loc15_[0];
   this.knowSRejuvPot = _loc15_[1];
   this.knowSExpPreg = _loc15_[2];
   this.knowSBallSwell = _loc15_[3];
   this.knowGenSwap = _loc15_[4];
   this.knowMasoPot = _loc15_[5];
   this.knowBabyFree = _loc15_[6];
   this.knowPotPot = _loc15_[7];
   this.knowMilkSuppress = _loc15_[8];
   this.knowSGenSwap = _loc16_[0];
   this.knowSMasoPot = _loc16_[1];
   this.knowSBabyFree = _loc16_[2];
   this.knowSPotPot = _loc16_[3];
   this.knowPussJuice = _loc16_[4];
   this.knowPheromone = _loc16_[5];
   this.knowBazoomba = _loc16_[6];
   this.maleFetish = _loc17_[0];
   this.femaleFetish = _loc17_[1];
   this.hermFetish = _loc17_[2];
   this.narcissistFetish = _loc17_[3];
   this.dependentFetish = _loc17_[4];
   this.dominantFetish = _loc18_[0];
   this.submissiveFetish = _loc18_[1];
   this.lboobFetish = _loc18_[2];
   this.sboobFetish = _loc18_[3];
   this.furryFetish = _loc18_[4];
   this.scalyFetish = _loc18_[5];
   this.smoothyFetish = _loc18_[6];
   this.pregnancyFetish = _loc19_[0];
   this.bestialityFetish = _loc19_[1];
   this.milkFetish = _loc19_[2];
   this.sizeFetish = _loc19_[3];
   this.unbirthingFetish = _loc19_[4];
   this.ovipositionFetish = _loc19_[5];
   this.toyFetish = _loc19_[6];
   this.hyperFetish = _loc19_[7];
   this.humanChildren = _loc20_[0];
   this.equanChildren = _loc20_[1];
   this.lupanChildren = _loc20_[2];
   this.felinChildren = _loc20_[3];
   this.cowChildren = _loc20_[4];
   this.lizanChildren = _loc20_[5];
   this.lizanEggs = _loc20_[6];
   this.bunnionChildren = _loc20_[7];
   this.wolfPupChildren = _loc20_[8];
   this.miceChildren = _loc20_[9];
   this.birdEggs = _loc20_[10];
   this.birdChildren = _loc20_[11];
   this.pigChildren = _loc20_[12];
   this.calfChildren = _loc20_[13];
   this.bugEggs = _loc20_[14];
   this.bugChildren = _loc20_[15];
   this.skunkChildren = _loc20_[16];
   this.minotaurChildren = _loc20_[17];
   this.freakyGirlChildren = _loc20_[18];
   this.i = 0;
   this.pregArray = [];
   while(this.i < _loc26_.length)
   {
      this.pregArray[this.i] = _loc26_[this.i];
      ++this.i;
   }
   this.bagArray = [];
   this.bagStackArray = [];
   for(this.i = 0; this.i < _loc22_.length; ++this.i)
   {
      this.bagArray[this.i] = _loc22_[this.i];
      this.bagStackArray[this.i] = _loc24_[this.i];
   }
   this.stashArray = [];
   this.stashStackArray = [];
   for(this.i = 0; this.i < _loc23_.length; ++this.i)
   {
      this.stashArray[this.i] = _loc23_[this.i];
      this.stashStackArray[this.i] = _loc25_[this.i];
   }
   """

def savetest():
   #[1,1,107,0,2,null,2,0.75],
   trackSave = ["","","","","","","",""]
   trackSave[0] = 1 #this.currentState;
   trackSave[1] = 1 #this.currentZone;
   trackSave[2] = 107 #this.day;
   trackSave[3] = 0 #this.hour;
   trackSave[4] = 2 #this.currentDayCare;
   trackSave[5] = "" #this.inDungeon;
   trackSave[6] = 2 #this.currentDungeon;
   trackSave[7] = 0.75
   a = open("writetest", "w")
   a.write("trackSave = " + str(trackSave))
   a.close()

def loadtest():
   tree = xmletree.parse("blanksave.xml")
   root = tree.getroot()
   track = root.find('track')
   cs = track.find('currentState').text
   cz = track.find('currentZone').text
   d = track.find('day').text
   h = track.find('hour').text
   cdc = track.find('currentDayCare').text
   _id = track.find('inDungeon').text
   cd = track.find('currentDungeon').text
   v7 = track.find('v7').text
   stats = root.find('stats')
   level = root.find('level')
   mod = root.find('mod')
   quality = root.find('quality')
   cock = root.find('cock')
   girl = root.find('girl')
   gear = root.find('gear')
   status = root.find('status')
   affinity = root.find('affinity')
   rep = root.find('rep')
   knowledge = root.find('knowledge')
   boss = root.find('boss')
   knowSimpleAlchemy = root.find('knowSimpleAlchemy')
   knowAdvancedAlchemy = root.find('knowAdvancedAlchemy')
   knowComplexAlchemy = root.find('knowComplexAlchemy')
   majorFetish = root.find('majorFetish')
   moderateFetish = root.find('moderateFetish')
   minorFetish = root.find('minorFetish')
   kid = root.find('kid')
   trav = root.find('trav')
   bag = root.find('bag')
   bagStack = root.find('bagStack')
   stash = root.find('stash')
   stashStack = root.find('stashStack')
   preg = root.find('preg')
   print(len(list(preg)))

loadtest()