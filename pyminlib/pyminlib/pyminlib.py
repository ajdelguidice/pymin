#!/usr/bin/python3

import test
import bdb
import pdb
import timeit
import math
import decimal
import os
import pathlib
import fileinput
import io
import importlib
import PIL
import dataclasses
#codecs, datetime and/or time, random, statistics, wave, colorsys, itertools, more-itertools, functools, operator, tempfile, shutil, zlib, gzip, bz2, lzma, zipfile, tarfile, configparser, logging, logging.config, logging.handlers, errno, asyncio, json, base64, binhex, binascii, html, uuid, sys

#Clock
def ClockStep (time, timeMod):
   """
   Takes in (time, timeMod)
   Changes currentTime by timeMod and if needed, changes currentDay
   Returns (time)
   """
   a = time
   b = timeMod
   a[1] += b
   a[2] += b
   while a[1] >= 24.00:
      a[1] -= 24.00
      a[0] += 1
      continue
   return a

def Wait (time, hunger):
   """
   Takes in (time, hunger)
   Changes currentTime by +1.00 and hunger by -1
   Returns (time, hunger)
   """
   a = ClockStep(time, 1.00)
   b = hunger - 1
   return a, b

def Sleep (time, hunger):
   """
   Takes in (time, hunger)
   Changes currentTime by +8.00, hunger by -8, and resets timeSinceLastSleep
   Returns (time, hunger)
   """
   a = ClockStep(time, 8.00)
   b = hunger - 8
   a[2] = 0
   return a, b

#GameVars
def ThemeChange (theme):
   """
   Takes in (theme)
   Changes the Theme
   Returns (theme)
   """
   a = theme
   if a <= 7:
      a = 0
      return a
   else:
      a += 1
      return a

def FontSizeUp (fontSize):
   """
   Takes in (fontSize)
   Changes fontSize by +2
   Returns (FontSize)
   """
   a = fontSize
   if a < 26:
      a += 2
      return a
   else:
      return a

def FontSizeReset (fontSize):
   """
   Takes in (fontSize)
   Resets fontSize to 14
   Returns (fontSize)
   """
   a = fontSize
   a = 14
   return a

def FontSizeDown (fontSize):
   """
   Takes in (fontSize)
   Changes fontSize by -2
   Returns (fontSize)
   """
   a = fontSize
   if a > 4:
      a -= 2
      return a
   else:
      return a

def ChangeBold (fontBold):
   """
   Takes in (fontBold)
   Changes fontBold
   Returns (fontBold)
   """
   a = fontBold
   if a == True:
      a = False
      return a
   elif a == False:
      a = True
      return a
   else:
      a = False
      return a

def FontColourChange (fontColour):
   """
   Takes in (fontColour)
   Changes fontColour
   Returns (fontColour)
   """
   a = fontColour
   if a == "000000":
      a = "FFFFFF"
      return a
   elif a == "FFFFFF":
      a = "808080"
      return a
   elif a == "808080":
      a = "0000FF"
      return a
   elif a == "0000FF":
      a = "800080"
      return a
   elif a == "800080":
      a = "FF0000"
      return a
   elif a == "FF0000":
      a = "FFA500"
      return a
   elif a == "FFA500":
      a = "FFFF00"
      return a
   elif a == "FFFF00":
      a = "008000"
      return a
   elif a == "008000":
      a = "EF7DB6"
      return a
   elif a == "EF7DB6":
      a = "29705C"
      return a
   elif a == "29705C":
      a = "000000"
      return a
   else:
      a = "000000"
      return a


#options buttons
def Option1Event ():
   ThemeChange()

def Option2Event ():
   FontSizeDown()
      
def Option3Event ():
   FontSizeReset()
      
def Option4Event ():
   FontSizeUp()
      
def Option5Event ():
   ChangeBold()
      
def Option6Event ():
   FontColourChange()
      
def Option7Event ():
   toggleSide()


#items
def ItemName (ID):
   a = ID
   b = ""
   if a == 0:
      b = " "
      return b
   elif a == 1:
      b = "Test"
      return b
   elif a == 101:
      b = "Anc Claws"
      return b
   elif a == 102:
      b = "Imb Shoes"
      return b
   elif a == 103:
      b = "Dry Sand"
      return b
   elif a == 104:
      b = "Milker"
      return b
   elif a == 105:
      b = "Cat's Meow"
      return b
   elif a == 106:
      b = "Penis Pump"
      return b
   elif a == 108:
      b = "Blood Gge"
      return b
   elif a == 109:
      b = "Edu Egg"
      return b
   elif a == 110:
      b = "Reduction"
      return b
   elif a == 111:
      b = "Skin Balm"
      return b
   elif a == 112:
      b = "Bol Juice"
      return b
   elif a == 113:
      b = "Taint Leaf"
      return b
   elif a == 114:
      b = "Sweet Sap"
      return b
   elif a == 115:
      b = "Poultice"
      return b
   elif a == 116:
      b = "Dagger"
      return b
   elif a == 117:
      b = "Hammer"
      return b
   elif a == 118:
      b = "Saber"
      return b
   elif a == 119:
      b = "Whip"
      return b
   elif a == 120:
      b = "Neuter"
      return b
   elif a == 121:
      b = "TS Soft"
      return b
   elif a == 122:
      b = "TS Firm"
      return b
   elif a == 123:
      b = "TS Tied"
      return b
   elif a == 124:
      b = "TS Siz"
      return b
   elif a == 125:
      b = "TS Ovi"
      return b
   elif a == 126:
      b = "Oas Water"
      return b
   elif a == 127:
      b = "Tail Spike"
      return b
   elif a == 128:
      b = "TS Sanct"
      return b
   elif a == 200:
      b = "Lila's Gift"
      return b
   elif a == 201:
      b = "Milk C Pois"
      return b
   elif a == 202:
      b = "Co-Snak Ven"
      return b
   elif a == 203:
      b = "Wolf Fur"
      return b
   elif a == 204:
      b = "Sm Pouch"
      return b
   elif a == 205:
      b = "Sm Pouch"
      return b
   elif a == 206:
      b = "Trinket"
      return b
   elif a == 207:
      b = "Cock Carv"
      return b
   elif a == 208:
      b = "Blo Berry"
      return b
   elif a == 209:
      b = "Grain"
      return b
   elif a == 210:
      b = "Puss Fruit"
      return b
   elif a == 211:
      b = "DairE Pill"
      return b
   elif a == 212:
      b = "Red Mush"
      return b
   elif a == 213:
      b = "Wet Cloth"
      return b
   elif a == 214:
      b = "Lon Milk"
      return b
   elif a == 215:
      b = "Lon Pendant"
      return b
   elif a == 216:
      b = "Pink Ink"
      return b
   elif a == 217:
      b = "Egg Jelly"
      return b
   elif a == 218:
      b = "Bul Berry"
      return b
   elif a == 219:
      b = "Fresh Egg"
      return b
   elif a == 220:
      b = "Blondie"
      return b
   elif a == 221:
      b = "Puss Juice"
      return b
   elif a == 222:
      b = "Kinky Carr"
      return b
   elif a == 223:
      b = "Eq Snack"
      return b
   elif a == 224:
      b = "Lila's Milk"
      return b
   elif a == 225:
      b = "Body Wash"
      return b
   elif a == 226:
      b = "Felin Tea"
      return b
   elif a == 227:
      b = "Oral Wash"
      return b
   elif a == 228:
      b = "Body Oil"
      return b
   elif a == 229:
      b = "Leath Strap"
      return b
   elif a == 230:
      b = "Eggcelerator"
      return b
   elif a == 231:
      b = "Desi Sand"
      return b
   elif a == 232:
      b = "Flying Carp"
      return b
   elif a == 233:
      b = "A-Grav Rock"
      return b
   elif a == 234:
      b = "Rein Charm"
      return b
   elif a == 235:
      b = "Fell Rod"
      return b
   elif a == 236:
      b = "Recept Bell"
      return b
   elif a == 237:
      b = "Dewy Gift"
      return b
   elif a == 238:
      b = "Squ Cheese"
      return b
   elif a == 239:
      b = "Shiny Rock"
      return b
   elif a == 240:
      b = "Auburn Dye"
      return b
   elif a == 241:
      b = "Brown Dye"
      return b
   elif a == 242:
      b = "Grey Dye"
      return b
   elif a == 243:
      b = "White Dye"
      return b
   elif a == 244:
      b = "Snuggle Ball"
      return b
   elif a == 245:
      b = "Facial Mud"
      return b
   elif a == 246:
      b = "Fertile Gel"
      return b
   elif a == 247:
      b = "Supp Harness"
      return b
   elif a == 248:
      b = "Breeder Pot"
      return b
   elif a == 249:
      b = "Treant's Tear"
      return b
   elif a == 250:
      b = "Foomp Bomb"
      return b
   elif a == 251:
      b = "Plump Quat"
      return b
   elif a == 252:
      b = "Milky Pend"
      return b
   elif a == 253:
      b = "Bug Egg"
      return b
   elif a == 254:
      b = "Lantern"
      return b
   elif a == 255:
      b = "Frag Flower"
      return b
   elif a == 256:
      b = "Nectar Candy"
      return b
   elif a == 257:
      b = "Too Human"
      return b
   elif a == 258:
      b = "Tainted Pot"
      return b
   elif a == 259:
      b = "Sweet&Sour"
      return b
   elif a == 260:
      b = "Succ Draft"
      return b
   elif a == 500:
      b = "Milk Bottle"
      return b
   elif a == 501:
      b = "Milk Jug"
      return b
   elif a == 502:
      b = "Milk Barrel"
      return b
   elif a == 503:
      b = "Lust Draft"
      return b
   elif a == 504:
      b = "Rejuv Pot"
      return b
   elif a == 505:
      b = "Bad Exper"
      return b
   elif a == 506:
      b = "Exp Preg"
      return b
   elif a == 507:
      b = "Ball Sweller"
      return b
   elif a == 508:
      b = "S Lust Draft"
      return b
   elif a == 509:
      b = "S Rejuv Pot"
      return b
   elif a == 510:
      b = "S Bad Exper"
      return b
   elif a == 511:
      b = "S Exp Preg"
      return b
   elif a == 512:
      b = "S Ball Sweller"
      return b
   elif a == 513:
      b = "Gen Swap"
      return b
   elif a == 514:
      b = "Maso Pot"
      return b
   elif a == 515:
      b = "Black Dye"
      return b
   elif a == 516:
      b = "Baby Free"
      return b
   elif a == 517:
      b = "Pot Pot"
      return b
   elif a == 518:
      b = "S Gen Swap"
      return b
   elif a == 519:
      b = "S Maso Pot"
      return b
   elif a == 520:
      b = "Red Dye"
      return b
   elif a == 521:
      b = "S Baby Free"
      return b
   elif a == 522:
      b = "S Pot Pot"
      return b
   elif a == 523:
      b = "Cum Vial"
      return b
   elif a == 524:
      b = "Cum Bottle"
      return b
   elif a == 525:
      b = "Cum Jug"
      return b
   elif a == 526:
      b = "Cum Barrel"
      return b
   elif a == 527:
      b = "Good Egg"
      return b
   elif a == 528:
      b = "Bad Egg"
      return b
   elif a == 529:
      b = "Strange Egg"
      return b
   elif a == 530:
      b = "Charmed Egg"
      return b
   elif a == 531:
      b = "Divine Egg"
      return b
   elif a == 532:
      b = "Pheromone"
      return b
   elif a == 533:
      b = "Reduc Reduc"
      return b
   elif a == 534:
      b = "Male Enhance"
      return b
   elif a == 535:
      b = "Milk Suppress"
      return b
   elif a == 536:
      b = "Bazoomba!"
      return b
   elif a == 537:
      b = "Queen Egg"
      return b
   elif a == 538:
      b = "Soldier Egg"
      return b
   elif a == 539:
      b = "Drone Egg"
      return b
   elif a == 540:
      b = "Worker Egg"
      return b
   else:
      b = "ITEM NAME ERROR " + b
      return b


def ItemDesc (ID):
   a = ID
   b = ""
   if a == 0:
      b = " "
      return b
   elif a == 1:
      b = "test"
      return b
   elif a == 101:
      b = "Claws of the Lupine Ancestors" + "\n" + "\n" + "Harkening back to supposed Lupan ancestry, as long as this item remains in your bag, your hands will change into clawed paws that will help hold down your foes, just like the wolves of the forest." + "\n" + "\n" + "Although, in your case, it just gives you a bonus to Rape attempts..."
      return b
   elif a == 102:
      b = "Imbued Horseshoes" + "\n" + "\n" + "Crafted by the Equans of Firmshaft, these horseshoes help improve your running capabilities as long as they're in your bag. And they'll turn your feet into hooves."
      return b
   elif a == 103:
      b = "Magical Sands of the Dry Dunes" + "\n" + "\n" + "Applying this special sand to your genitalia will permanently make it a bit less moist than usual. Often used by the women of Siz'Calit when their heat makes them a little too moist. Or when they're producing a bit too much milk (though that's rarely the case in Siz'Calit)."
      return b
   elif a == 104:
      b = "Milking Machine" + "\n" + "\n" + "A compact device that produces enough suction to pump any breasts/udder you wish to collect the lactation of. Doing so will allow you to store the milk to be used or sold later, if you can produce enough. Comes with 2 hoses and multiple cups to work on almost any nipple/teat." + "\n" + "\n" + "Warning: Excessive use may result in permanent nipple/teat growth." + "\n" + "\n" + "Can only be used during Masturbation."
      return b
   elif a == 105:
      b = "'Cat's Meow' Potion" + "\n" + "\n" + "Favored by the Felins of Siz'Calit, this potion helps increase the production of breastmilk. Just try not to show off in Siz'Calit, or you may draw a crowd."
      return b
   elif a == 106:
      b = "Penis Pump" + "\n" + "\n" + "A simple device with an elastic cylinder that's intended to slip over a penis and pump it until it climaxes. Doing so will allow you to store the semen to be used or sold later, if you can produce enough." + "\n" + "\n" + "Can only be used during Masturbation."
      return b
   elif a == 108:
      b = "Blood Gauge" + "\n" + "\n" + "Due to their propensity to be swayed by outside blood, humans developed this nifty little gadget. Pressing it against your pulse, the magic of the device can detect the levels of racial influence in your body."
      return b
   elif a == 109:
      b = "Educated Eggdicator" + "\n" + "\n" + "With so many unfertilized eggs around the oasis, Lizan developed this to be able to tell a good egg from a bad egg. Even though an egg is just an egg beforehand, once put through this eggdicator its wave function collapses into a more determinable state." + "\n" + "\n" + "Warning: Using this item requires 1 Fresh Egg to operate."
      return b
   elif a == 110:
      b = "A Reduction of Reducer Agents" + "\n" + "\n" + "This is a powerful - yet often necessary in Nimin - elixer that, when rubbed on a part of your body, will permanently shrink that part to half its original size. Be careful!" + "\n" + "\n" + "Warning: This item is not useful against your enemies."
      return b
   elif a == 111:
      b = "Skin Balm" + "\n" + "\n" + "Used and created by the Humans of Softlik, this balm helps increase their skin's supplesness and other human attributes, as well as decrease those of other races."
      return b
   elif a == 112:
      b = "Bolstering Juice" + "\n" + "\n" + "This white 'juice' is often used and created by the Equans of Firmshaft. It helps strengthen their equan attributes and  decrease those of other races."
      return b
   elif a == 113:
      b = "Tainted Leaf" + "\n" + "\n" + "This paw-shaped leaf is farmed and used by the Lupans of Tieden to fend off the attributes of other races, usually the more violent ones, and increase their lupan strengths."
      return b
   elif a == 114:
      b = "Sweet Sap" + "\n" + "\n" + "Used and created by the Felins of Siz'Calit, this vial of clear liquid helps increase their felin sensitivities as well as ward off outside influences."
      return b
   elif a == 115:
      b = "Poultice" + "\n" + "\n" + "A generic swathe of cloth soaked in soothing balms, this poultice will heal 20 HP. It'll also make you a little aroused from rubbing it all over yourself..."
      return b
   elif a == 116:
      b = "Dagger" + "\n" + "\n" + "A relatively cheap weapon, the dagger is a nice way to defend oneself in Nimin." + "\n" + "\n" + "Base damage: 5-12"
      return b
   elif a == 117:
      b = "Warhammer" + "\n" + "\n" + "A rather blunt weapon, it's a bit unwieldy but gets the job done." + "\n" + "\n" + "Base damage: 2-20"
      return b
   elif a == 118:
      b = "Saber" + "\n" + "\n" + "A well-designed blade, the saber can deal significant damage to foes." + "\n" + "\n" + "Base damage: 10-25"
      return b
   elif a == 119:
      b = "Whip" + "\n" + "\n" + "A somewhat kinky weapon, the whip can leave some rather nasty welts." + "\n" + "\n" + "Base damage: 12-18"
      return b
   elif a == 120:
      b = "Neuterizer" + "\n" + "\n" + "Developed by the Lupans of Tieden, this isn't actually intended to be used on most of their inhabitants. Instead, it was created as a post-defensive measure against the... oddities of Nimin."
      return b
   elif a == 121:
      b = "Teleport Scroll: Softlik" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Softlik." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 122:
      b = "Teleport Scroll: Firmshaft" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Firmshaft." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 123:
      b = "Teleport Scroll: Tieden" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Tieden." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 124:
      b = "Teleport Scroll: Siz'Calit" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Siz'Calit." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 125:
      b = "Teleport Scroll: Oviasis" + "\n" + "\n" + "Created to make sure explorers can find their way back home, this scroll of teleportation will instantly return the user to the city of Oviasis." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 126:
      b = "Oasis Water" + "\n" + "\n" + "A vial of the fresh water from the oasis in the lizan city of Oviasis, it helps the residents cool off and moisten their scales so they can hunt and sunbathe more, as well as ward off the influences of other races."
      return b
   elif a == 127:
      b = "Tail Spike" + "\n" + "\n" + "This large spike is held firm upon leather straps. When attached to a tail, it can be used as a rather effective weapon." + "\n" + "\n" + "Base damage: 10-20" + "\n" + "\n" + "Requirement: Must have a muscular/skeletal tail to equip (tails of hair or excessively fluffy tails will not work)."
      return b
   elif a == 128:
      b = "Teleport Scroll: Sanctuary" + "\n" + "\n" + "Created for an easy return, this scroll of teleportation will instantly return the user to the city of Sanctuary." + "\n" + "\n" + "Can be used at any time, even in the midst of battle."
      return b
   elif a == 200:
      b = "Lila's Gift" + "\n" + "\n" + "A small charm given to you by the young felin girl in Siz'Calit, it seems to be pretty decoration made from flowers and leaves and some other cute little things. However, as you hold it, you notice it makes you wetter down under... This might have been the reason the girl was so wet to begin with, or maybe her extreme wetness for such a young age rubbed off onto her charm? Either way, as long as you carry it, you'll be wetter than usual. And you seem much more sensitive than usual..." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
      return b
   elif a == 201:
      b = "Milk Creeper Poison" + "\n" + "\n" + "Obtained from a passed out Milk Creeper, this poison is a bit diluted from her ingestion from so much of your milk. It is unlikely that it will affect your lactation rate directly like the pure poison does, but rubbing it into your mammary glands will cause them to swell slightly larger."
      return b
   elif a == 202:
      b = "Cock-Snake Venom" + "\n" + "\n" + "Obtained from the fangs of a passed out cock-snake, this venom is a potent male enhancement. And if you aren't male when you use it, you will be, if at least partially..."
      return b
   elif a == 203:
      b = "Tuft of Wolf Fur" + "\n" + "\n" + "Obtained from an encounter with a feral wolf, a tuft of their fur has been known to decrease sensitivity, and thus increase your toughness against attacks, when rubbed onto your " + this.skinDesc() + "."
      return b
   elif a == 204:
      b = "Small Pouch" + "\n" + "\n" + "This is a small pouch you have obtained somewhere. Use it to see what it contains!"
      return b
   elif a == 205:
      b = "Small Pouch" + "\n" + "\n" + "This is a small pouch you have obtained somewhere. Use it to see what it contains!"
      return b
   elif a == 206:
      b = "Shiny Trinket" + "\n" + "\n" + "Other than being a pretty decoration, this thing isn't much use to you. However, it probably sells fairly well."
      return b
   elif a == 207:
      b = "Wooden Cock Carving" + "\n" + "\n" + "This thing looks like a dildo made of wood, with decorated carvings all around. It sounds hollow, so maybe you could break it open and see if anything is inside?"
      return b
   elif a == 208:
      b = "Bloated Berry" + "\n" + "\n" + "A berry from across the ocean, it looks oddly bloated, nearly two berries in one. It seems edible though."
      return b
   elif a == 209:
      b = "Handful of Grain" + "\n" + "\n" + "A handful of fresh grain, it smells slightly sweet in your hands. Eating it will provide you some energy from the carbs!"
      return b
   elif a == 210:
      b = "Pussy Fruit" + "\n" + "\n" + "It is unknown whether the name derives from the cat-like felin people that enjoy this fruit or from the fruit's rather... lewd shape. Either way, it is a very sweet and juicy fruit that felin females love."
      return b
   elif a == 211:
      b = "DairE Pill" + "\n" + "\n" + "Produced by the farmers of the Dairy Farm outside of Softlik, this pill supposedly helps increase the lactation rate of dairy cows. It is not suggested to be ingested by anything other than cows, though that's just a suggestion."
      return b
   elif a == 212:
      b = "Red Mushroom" + "\n" + "\n" + "An odd looking mushroom with a red cap with a few white dots found on the walls of the Old Cave. You're not really sure what it does, but you think you'll get bigger so you can smash some blocks... or something."
      return b
   elif a == 213:
      b = "Wet, Slimy Cloth" + "\n" + "\n" + "This piece of white cloth seems to be perpetually wet and slimy, no matter how long you keep it in your bag. You have no idea what it can do, however."
      return b
   elif a == 214:
      b = "Malon's Milk" + "\n" + "\n" + "Unlike the other bottles of milk that come from the Dairy Farm, this wasn't from a cow. From Malon's own supply, you're unsure exactly how it's different from the rest, though it does taste better."
      return b
   elif a == 215:
      b = "Malon's Pendant" + "\n" + "\n" + "Given to you by Malon from the Dairy Farm, this gift of admiration seems to have been a keepsake of hers since she was a child and has imbued by her long-time love of animals and rather bovine qualities. As long as you hold onto it, everything is a bit more consensual towards being 'raped', be a bit more lenient to you running away, and all milk products heal you slightly more than usual." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
      return b
   elif a == 216:
      b = "Pink Ink" + "\n" + "\n" + "Octopus ink gained from a rather pink octopus girl, this ink serves as a very rare and valuable hair dye. Should you use it, your hair will turn a coral pink color, if you have hair."
      return b
   elif a == 217:
      b = "Octopus Egg Jelly" + "\n" + "\n" + "The jelly from the eggs of the octopus girls you gave birth to, it seems like it'd make you very aroused if you rubbed it on your genitals. Although, you're not quite sure what it would do beyond that..."
      return b
   elif a == 218:
      b = "Bulging Berry" + "\n" + "\n" + "A cousin of the bloated berry, this fruit splits into multiple spheres from the same stem, somewhat like cherries but can often have three of four from the same stem. It is quite edible, though it is highly suggested to not eat many."
      return b
   elif a == 219:
      b = "Fresh Egg" + "\n" + "\n" + "An unfertilized egg from a lizan female (or herm), eggs like this are common in the lizan diet. High in protein, they're good for your health."
      return b
   elif a == 220:
      b = "Blonde Dye" + "\n" + "\n" + "A dye made from mashed grain, this will turn your hair blonde in color when used, if you have hair, or it can be sold for a decent sum."
      return b
   elif a == 221:
      b = "Concentrated Pussy Fruit Juice" + "\n" + "\n" + "Created by a notable mistress in Siz'calit, this vial contains some rather concentrated juice from the Pussy Fruit. It is likely to have a notable effect on a woman's loins, more potent than its source."
      return b
   elif a == 222:
      b = "Kinky Carrot" + "\n" + "\n" + "Used in lewd fashions by a small rabbit-like people, you're sure to clean this off as soon as you got it. Although you're not entirely certain what would happen if you ate it, besides being in better health for keeping veggies in your diet."
      return b
   elif a == 223:
      b = "Equan Snack" + "\n" + "\n" + "A common snack amongst the equan people, this sweet little thing has the kind of carbs that will help you get through the day, no matter what life may put on your shoulders. And it seems to be the cause of some bellies of some equan women..."
      return b
   elif a == 224:
      b = "Lila's Milk" + "\n" + "\n" + "From the ample supply of a certain little felin girl, this milk seems to be a tad sweeter than normal milk and also slightly tainted by the poor girl's constant heat."
      return b
   elif a == 225:
      b = "Body Wash" + "\n" + "\n" + "This nice body wash is scented like a meadow of flowers. It can help clean up some dirty thoughts and make your body feel much fresher."
      return b
   elif a == 226:
      b = "Felin Tea Mix" + "\n" + "\n" + "A common brew amongst felins, this tea helps calm the body and mind. Especially the body, which is often necessary for Felins..."
      return b
   elif a == 227:
      b = "Felin Oral Wash" + "\n" + "\n" + "With bath by licking being commonplace amongst felins, this wash is to aid in such endeavors. Delightfully tingly, this stuff will leave both your breath and your fur feeling fresh."
      return b
   elif a == 228:
      b = "Body Oil" + "\n" + "\n" + "Nice and slick, this stuff is great for your skin or scales and makes you look quite shiny and alluring for the next 5 hours."
      return b
   elif a == 229:
      b = "Leather Strap" + "\n" + "\n" + "Found somewhere in Silandrias' den, this leather strap seems to be fitted to tie tightly around the base of her tail. Otherwise, you have no idea what it could be for."
      return b
   elif a == 230:
      b = "Eggcelerator" + "\n" + "\n" + "Meant to temporarily increase the rate of egg production in Lizan females, this pill looks to be a little egg-shaped itself, with more of a torpedo-like tip. This pill also seems to be too large to be ingested orally by the average person, which you deduct means it's meant as a suppository... Though, considering its nature, it's safe to say it's not meant to be administered anally, at least." + "\n" + "\n" + "Its effect stacks."
      return b
   elif a == 231:
      b = "Desiccating Sand" + "\n" + "\n" + "Obtained from a sentient dust devil, this sand is specially imbued with the ability to suck moisture from a body. Though the Dust Devil only uses it to feed, in this quantity it can be rather damaging if thrown at an enemy all at once. Be wary of blow-back, though." + "\n" + "\n" + "This item can only be used during battle."
      return b
   elif a == 232:
      b = "Flying Carpet" + "\n" + "\n" + "Borrowed from Silandrias, this flying carpet can take you on a magical ride to see a whole new world. However, it can only take you to towns you have already found, since you wouldn't know how to guide it someplace you haven't been, so the whole 'new' aspect is rather moot. But it is still quite convenient!" + "\n" + "\n" + "You cannot activate the flying carpet in amidst the heat of battle or amidst the heat of masturbation."
      return b
   elif a == 233:
      b = "Anti-Gravity Rock" + "\n" + "\n" + "Borrowed from Silandrias, this small rock, more of a pebble really, just kind of floats there and defies gravity. Yet, as you carry it, even you seem to defy gravity to a degree. You feel much lighter on your " + this.legDesc(10) + " and your carry capacity increases by a whole 75! '75 what', you have no idea, but it's a big number so it's got to be good, right?"
      return b
   elif a == 234:
      b = "Reindeer Charm" + "\n" + "\n" + "Borrowed from Silandrias, this sapphire charm is carved into the shape of a reindeer's head, with large antlers. Carrying it imbues you with the essence of a reindeer mother, providing you with a nice set of antlers and a matching deer-butt, as well as speeding up your pregnancies and increasing your minimum lust, urging you to give birth to plenty of children."
      return b
   elif a == 235:
      b = "Fellatio Rod" + "\n" + "\n" + "Borrowed from Silandrias, this rather phallic rod is actually a weapon. When the base is pointed at the target, you can siphon out some of their life force by placing your lips around the bulbous end of the rod and gently sucking. If you're very skilled, you can make the weapon perform even stronger. It even ignores their natural resistance to physical attacks."
      return b
   elif a == 236:
      b = "Reception Bell" + "\n" + "\n" + "Borrowed from Silandrias, this small cowbell is worn around the neck and makes one more receptive to outside influences. In other words, the wearer gains 50% more SexP than usual *ding*. They also tend to be 30% more susceptible to blood-changes though... *dong*"
      return b
   elif a == 237:
      b = "Lila's Dewy Gift" + "\n" + "\n" + "Originally given to you by Lila, dew drops have started forming on and falling from the leaves and flowers constantly, ever since it became more 'infused' with your relationship with Lila. As long as you hold it, you're sexual lubrication flows much more and makes you quite sensitive. It even feels warm to the touch, a warmth that sometimes may spread to you..." + "\n" + "\n" + "Warning: You cannot regain this item should you lose it."
      return b
   elif a == 238:
      b = "Squeaky Cheese" + "\n" + "\n" + "Some cheese found in an alley that kinda squeaks when you rub it, it smells quite delicious and would help restore your energy if you're hurt. Other than that, though, well... you did find it in an alley, after all."
      return b
   elif a == 239:
      b = "Shiny Rock" + "\n" + "\n" + "A rather shiny rock you found, you're almost intent at staring at it. If anything, it at least improves your focus."
      return b
   elif a == 240:
      b = "Auburn Dye" + "\n" + "\n" + "A dark reddish color, this dye will turn your hair auburn when used, if you have hair"
      return b
   elif a == 241:
      b = "Brown Dye" + "\n" + "\n" + "A simple brownish, this dye will turn your hair brown when used, if you have hair"
      return b
   elif a == 242:
      b = "Grey Dye" + "\n" + "\n" + "A shade, this dye will turn your hair grey when used, if you have hair"
      return b
   elif a == 243:
      b = "White Dye" + "\n" + "\n" + "Lacking any color, this dye will turn your hair pure white when used, if you have hair"
      return b
   elif a == 244:
      if snuggleBall == True:
         b = "Snuggle Ball" + "\n" + "\n" + "Not really a 'ball' at the moment, this squishy thing is currently coating your body with a thick plush layer of shiny snuggliness. You can attempt to take it off, though it does make you look kinda cute, like a cuddly toy."
         return b
      else:
         b = "Snuggle Ball" + "\n" + "\n" + "Squishy and plush, this odd ball is made out of seemingly unnatural materials. Almost like a living liquid, it wobbles around in your hand and is slightly pliable. It feels so pleasant, you kinda want to snuggle with it."
         return b
   elif a == 245:
      b = "Facial Mud" + "\n" + "\n" + "Some mud you found at a secluded mudhole in the savanna, this particular mud is quite clean and rich in minerals and would really help your complexion."
      return b
   elif a == 246:
      b = "Fertile Gel" + "\n" + "\n" + "A soft gel that gives off a pleasant warmth, it helps increase the fertility of women who want to be mothers or want a nice big swollen belly." + "\n" + "\n" + "Extra doses extend the duration of the gel."
      return b
   elif a == 247:
      b = "Support Harness" + "\n" + "\n" + "This contraption of straps and slings can be equipped to help support all those sizable appendages. Like a bra, except for the whole body!"
      if suppHarness == True:
         b += "" + "\n" + "\n" + "You currently have a harness equipped. Using it will unequip the harness."
         return b
      else:
         return b
   elif a == 248:
      b = "Breeder Potion" + "\n" + "\n" + "This potion is normally used by animal breeders to increase the litter sizes of their animals and make their animals more frequently fertily receptive."
      return b
   elif a == 249:
      b = "Treant's Tear" + "\n" + "\n" + "This small tear-shaped piece of wood looks almost like a seed. However, across its surface are etched images of tree-like beings losing their limbs as they dance around the tear, progressively larger and larger with the more limbs they have lost. It's like some sort of ancient ritual, one you have never heard of..."
      return b
   elif a == 250:
      b = "Foomp Bomb" + "\n" + "\n" + "Much like a smoke bomb, this small ball can be tossed at an enemy to provide you an immediate escape from battle." + "\n" + "\n" + "This item can only be used during battle. This item will automatically successfully run from battle."
      return b
   elif a == 251:
      b = "Plump Quat" + "\n" + "\n" + "The quats is a very delicious fruit, so plump and ripe and full of mmm-mmm-goodness."
      return b
   elif a == 252:
      b = "Malon's Milky Pendant" + "\n" + "\n" + "This is the pendant Malon had given you, except now infused with a sort of milky complexion that ensures you'll always share her milky tendancies as long as you hold it, supporting your relationship as a couple of drippy cows~ It still seems to retain all the properties it had before as well."
      return b
   elif a == 253:
      b = "Bug Egg" + "\n" + "\n" + "Relatively small, this squishy unfertilized egg seems rather gooey. You could eat it, but the thought of doing so is somewhat nasty."
      if tail == 12:
         b += "" + "\n" + "\n" + "However, you do notice that the egg is just about the right size for the ovipositor hanging off your backside."
         return b
      else:
         return b
   elif a == 254:
      b = "Lantern" + "\n" + "\n" + "This is a fairly basic lantern that you found at the hidden entrance below the ground in the valley. And though it might be basic and have no other function, the light it gives off can help you access areas that are otherwise too dark."
      return b
   elif a == 255:
      b = "Fragrant Flower" + "\n" + "\n" + "A very pleasant smelling flower whose petals are black with white stripes. If you took a good whiff, it would likely help hone your senses a bit."
      return b
   elif a == 256:
      b = "Nectar Candy" + "\n" + "\n" + "A sweet treat that bugs seem to swarm if not stored properly. It bolsters your muscles and helps egg laying."
      return b
   elif a == 257:
      b = "Too Human Potion" + "\n" + "\n" + "This potion was made to help the humans of Softlik regain some of their human attributes. However, this batch was apparently a failure for being too effective, somehow?"
      return b
   elif a == 258:
      b = "Tainted Potion" + "\n" + "\n" + "This potion was tainted by your DairE Pill, so you don't really know what it will do until you ingest it."
      return b
   elif a == 259:
      b = "Sweet & Sour Candy" + "\n" + "\n" + "This rare little treat is a favorite among many, if you can find it. It's that the sweetness is so sweet that you'll drop from the bliss and that the sourness is so sour that you'll suck yourself in."
      return b
   elif a == 260:
      b = "Succubus Draft" + "\n" + "\n" + "One of the glowing vials from the succubus, this is some concentrated masculinity that has been drained from various people, quite possibly even yourself. For her, it's a source of food and power, for you... the effects are probably different."
      return b
   elif a == 500:
      b = "Bottle of Milk" + "\n" + "\n" + "A bottle of delicious milk that, when drunk, will heal 10 HP and help you stay awake a little longer."
      return b
   elif a == 501:
      b = "Jug of Milk" + "\n" + "\n" + "A large jug of delicious milk that, when drunk, will heal 40 HP and help you stay awake a while longer. When you're done peeing, of course."
      return b
   elif a == 502:
      b = "Barrel of Milk" + "\n" + "\n" + "A barrel full of delicious milk, this is mostly meant to be used for easy handling by merchants. However, if you use it, you will gain 4 Jugs of Milk instantly."
      return b
   elif a == 503:
      b = "Lust Draft" + "\n" + "\n" + "A potion that will increase your lust by 20 instantly when used."
      return b
   elif a == 504:
      b = "Rejuvenating Potion" + "\n" + "\n" + "A potion that will heal 30 HP and reduce your lust by 15 instantly when used."
      return b
   elif a == 505:
      b = "Bad Experiment" + "\n" + "\n" + "This combustable concoction will deal 10-20 damage to your enemy before they can react!" + "\n" + "\n" + "This item can only be used during battle."
      return b
   elif a == 506:
      b = "Express Pregnancy Potion" + "\n" + "\n" + "When that baby is taking a while to gestate, this potion up the pregnancy as though 50 hours had passed."
      return b
   elif a == 507:
      b = "Ball Sweller" + "\n" + "\n" + "Imbibing this will make your balls feel as though you hadn't ejaculated in 30 hours."
      return b
   elif a == 508:
      b = "Superior Lust Draft" + "\n" + "\n" + "A potion that will increase your lust by 50 instantly when used."
      return b
   elif a == 509:
      b = "Superior Rejuvenating Potion" + "\n" + "\n" + "A potion that will heal 70 HP and reduce your lust by 40 instantly when used."
      return b
   elif a == 510:
      b = "Super Bad Experiment" + "\n" + "\n" + "This extremely combustable concoction will deal 20-40 damage to your enemy before they can react!" + "\n" + "\n" + "This item can only be used during battle."
      return b
   elif a == 511:
      b = "Superior Express Pregnancy Potion" + "\n" + "\n" + "When that baby is taking a while to gestate, this potion up the pregnancy as though 120 hours had passed."
      return b
   elif a == 512:
      b = "Superior Ball Sweller" + "\n" + "\n" + "Imbibing this will make your balls feel as though you hadn't ejaculated in 70 hours."
      return b
   elif a == 513:
      b = "Gender Swap Potion" + "\n" + "\n" + "If you want to try out the opposite sex, this potion will revert your genitals back to infancy, allowing them to reform as their opposite counterparts. If a hermaphrodite takes this, it reverts all genitals to their smallest value. If a genderless person takes this, the resulting gender is random."
      return b
   elif a == 514:
      b = "Masochism Potion" + "\n" + "\n" + "After this potion is imbibed, your nervous system confuses half of all damage as pleasure for a whole day."
      return b
   elif a == 515:
      b = "Black Dye" + "\n" + "\n" + "This will turn your hair black in color when used, if you have hair."
      return b
   elif a == 516:
      b = "Baby Free Potion" + "\n" + "\n" + "Sipping this potion will reduce your chance of becoming pregnancy by 50% for the next 3 days. This contraceptive is not gauranteed to prevent pregnancy, especially if you're especially fertile. It will work whether you have the appropriate plumbing or not. Multiple instances of Baby Free Potion will only extend the time of its duration, not increase the reduction in chance."
      return b
   elif a == 517:
      b = "Potency Potion" + "\n" + "\n" + "Kicking your balls into gear, they will permanently produce 20% more cum, despite their size."
      return b
   elif a == 518:
      b = "Superior Gender Swap Potion" + "\n" + "\n" + "If you want to try out the opposite sex, this potion will transform your genitals into their opposite counterparts, retaining the relative size. If a hermaphrodite takes this, the genitals swap sizes. If a genderless person takes this, the resulting gender is random, along with the sizes of their genitals (up to a certain amount)."
      return b
   elif a == 519:
      b = "Superior Masochism Potion" + "\n" + "\n" + "After this potion is imbibed, your nervous system confuses all damage as pleasure for a whole day."
      return b
   elif a == 520:
      b = "Red Dye" + "\n" + "\n" + "This will turn your hair red in color when used, if you have hair."
      return b
   elif a == 521:
      b = "Superior Baby Free Potion" + "\n" + "\n" + "Sipping this potion will reduce your chance of becoming pregnancy by 50% for the next 9 days. This contraceptive is not gauranteed to prevent pregnancy, especially if you're especially fertile. It will work whether you have the appropriate plumbing or not. Multiple instances of Superior Baby Free Potion will only extend the time of its duration, not increase the reduction in chance."
      return b
   elif a == 522:
      b = "Superior Potency Potion" + "\n" + "\n" + "Drop-kicking your balls into gear, they will permanently produce 50% more cum, despite their size."
      return b
   elif a == 523:
      b = "Vial of Cum" + "\n" + "\n" + "Still kinda warm, this vial of goop will arouse you slightly when imbibed, plus heal a bit."
      return b
   elif a == 524:
      b = "Bottle of Cum" + "\n" + "\n" + "A bottle of warm cum that will arouse you and heal you slightly when imbibed. If you can get it all down."
      return b
   elif a == 525:
      b = "Jug of Cum" + "\n" + "\n" + "A jug full of hot cum, this is mostly meant to be used for easy handling by the merchants that might be able to find a use for it. However, if you use it, you will gain 3 Bottles of Cum instantly."
      return b
   elif a == 526:
      b = "Barrel of Cum" + "\n" + "\n" + "There's... not really much you can do with a barrel full of hot cum. The merchants will still buy it, but at a very low price, since there's not much they can do with it either..."
      return b
   elif a == 527:
      b = "Good Egg" + "\n" + "\n" + "An unfertilized fresh egg that is especially good for your health and body."
      return b
   elif a == 528:
      b = "Bad Egg" + "\n" + "\n" + "An unfertilized fresh egg that should never be eaten... Instead it can be thrown at your enemy for a quick 10-20 damage." + "\n" + "\n" + "This item can only be used during battle."
      return b
   elif a == 529:
      b = "Strange Egg" + "\n" + "\n" + "An unfertilized fresh egg that can do... odd things to your body."
      return b
   elif a == 530:
      b = "Charmed Egg" + "\n" + "\n" + "An unfertilized fresh egg that will make you quite alluring for 20 hours."
      return b
   elif a == 531:
      b = "Divine Egg" + "\n" + "\n" + "A very rare unfertilized fresh egg, eating it will make you closer to a diety of fertility."
      return b
   elif a == 532:
      b = "Strong Pheromone" + "\n" + "\n" + "Originally meant to be fishing bait, this concoction is much more potent than originally intended and attracts far more than fish for 30 hours..."
      return b
   elif a == 533:
      b = "Reduced Reduction" + "\n" + "\n" + "A weaker form of a Reduction, this will shrink the desired body part by a regular amount instead of halving its size."
      return b
   elif a == 534:
      b = "Male Enhancement Drug" + "\n" + "\n" + "A simple pill that, when ingested, will increase the size of you male genitals." + "\n" + "\n" + "Caution: females taking this pill may have similar side-effects."
      return b
   elif a == 535:
      b = "Milk Suppressant" + "\n" + "\n" + "This drug will prevent any milk from leaking from your body. It does not prevent your mammary glands from producing milk, but it does prevent the milk from escaping for its duration, avoiding most unsightly leaks."
      return b
   elif a == 536:
      b = "Bazoomba!" + "\n" + "\n" + "This glowing squishy orb is a secret recipe that creates more of one of the best things in life when ingested...!" + "\n" + "\n" + "Warning - Be wary of overload."
      return b
   elif a == 537:
      b = "Queen Egg" + "\n" + "\n" + "Not the egg of a queen, but rather an unfertilized egg fit for a queen! This wonderful egg would make any queen's abdomen larger and sexier. Though, if you're not an insect, this mostly translates to things below the waist. It will also help shorten the gestation period for quicker offspring and help your breasts hold more milk for all those births."
      return b
   elif a == 538:
      b = "Soldier Egg" + "\n" + "\n" + "Not the egg of a soldier, but rather an unfertilized egg suitable for a soldier. This powerful egg will make you taller, stronger, and more physically fit just by eating it!"
      return b
   elif a == 539:
      b = "Drone Egg" + "\n" + "\n" + "Not the egg of a drone, but rather an unfertilized egg better fed to the sex-craving drones, those mindless males that are only useful for impregnating a queen. This will make them even better at that singular duty."
      return b
   elif a == 540:
      b = "Worker Egg" + "\n" + "\n" + "Not the egg of a worker, but rather an unfertilized egg that would help any worker. Munching down this little thing will help anybody feel less exhausted and thus allow them to work even more!"
      return b
   else:
      b = "ITEM DESCRIPTION ERROR " + a
      return b

def ItemMaxStack (ID):
   a = ID
   b = ""
   if a == 0:
      b = 1
      return b
   elif a == 1:
      b = 1
      return b
   elif a == 101:
      b = 1
      return b
   elif a == 102:
      b = 1
      return b
   elif a == 103:
      b = 15
      return b
   elif a == 104:
      b = 1
      return b
   elif a == 105:
      b = 5
      return b
   elif a == 106:
      b = 1
      return b
   elif a == 108:
      b = 1
      return b
   elif a == 109:
      b = 1
      return b
   elif a == 110:
      b = 5
      return b
   elif a == 111:
      b = 5
      return b
   elif a == 112:
      b = 5
      return b
   elif a == 113:
      b = 5
      return b
   elif a == 114:
      b = 5
      return b
   elif a == 115:
      b = 10
      return b
   elif a == 116:
      b = 1
      return b
   elif a == 117:
      b = 1
      return b
   elif a == 118:
      b = 1
      return b
   elif a == 119:
      b = 1
      return b
   elif a == 120:
      b = 5
      return b
   elif a == 121:
      b = 10
      return b
   elif a == 122:
      b = 10
      return b
   elif a == 123:
      b = 10
      return b
   elif a == 124:
      b = 10
      return b
   elif a == 125:
      b = 10
      return b
   elif a == 126:
      b = 5
      return b
   elif a == 127:
      b = 1
      return b
   elif a == 128:
      b = 10
      return b
   elif a == 200:
      b = 1
      return b
   elif a == 201:
      b = 5
      return b
   elif a == 202:
      b = 5
      return b
   elif a == 203:
      b = 15
      return b
   elif a == 204:
      b = 5
      return b
   elif a == 205:
      b = 5
      return b
   elif a == 206:
      b = 10
      return b
   elif a == 207:
      b = 5
      return b
   elif a == 208:
      b = 10
      return b
   elif a == 209:
      b = 15
      return b
   elif a == 210:
      b = 5
      return b
   elif a == 211:
      b = 15
      return b
   elif a == 212:
      b = 10
      return b
   elif a == 213:
      b = 10
      return b
   elif a == 214:
      b = 10
      return b
   elif a == 215:
      b = 1
      return b
   elif a == 216:
      b = 5
      return b
   elif a == 217:
      b = 5
      return b
   elif a == 218:
      b = 10
      return b
   elif a == 219:
      b = 5
      return b
   elif a == 220:
      b = 5
      return b
   elif a == 221:
      b = 10
      return b
   elif a == 222:
      b = 5
      return b
   elif a == 223:
      b = 10
      return b
   elif a == 224:
      b = 10
      return b
   elif a == 225:
      b = 10
      return b
   elif a == 226:
      b = 15
      return b
   elif a == 227:
      b = 10
      return b
   elif a == 228:
      b = 10
      return b
   elif a == 229:
      b = 1
      return b
   elif a == 230:
      b = 5
      return b
   elif a == 231:
      b = 10
      return b
   elif a == 232:
      b = 1
      return b
   elif a == 233:
      b = 1
      return b
   elif a == 234:
      b = 1
      return b
   elif a == 235:
      b = 1
      return b
   elif a == 236:
      b = 1
      return b
   elif a == 237:
      b = 1
      return b
   elif a == 238:
      b = 15
      return b
   elif a == 239:
      b = 15
      return b
   elif a == 240:
      b = 5
      return b
   elif a == 241:
      b = 5
      return b
   elif a == 242:
      b = 5
      return b
   elif a == 243:
      b = 5
      return b
   elif a == 244:
      b = 1
      return b
   elif a == 245:
      b = 15
      return b
   elif a == 246:
      b = 10
      return b
   elif a == 247:
      b = 1
      return b
   elif a == 248:
      b = 10
      return b
   elif a == 249:
      b = 5
      return b
   elif a == 250:
      b = 5
      return b
   elif a == 251:
      b = 15
      return b
   elif a == 252:
      b = 1
      return b
   elif a == 253:
      b = 15
      return b
   elif a == 254:
      b = 1
      return b
   elif a == 255:
      b = 15
      return b
   elif a == 256:
      b = 15
      return b
   elif a == 257:
      b = 5
      return b
   elif a == 258:
      b = 5
      return b
   elif a == 259:
      b = 10
      return b
   elif a == 260:
      b = 10
      return b
   elif a == 500:
      b = 10
      return b
   elif a == 501:
      b = 5
      return b
   elif a == 502:
      b = 1
      return b
   elif a == 503:
      b = 10
      return b
   elif a == 504:
      b = 10
      return b
   elif a == 505:
      b = 5
      return b
   elif a == 506:
      b = 10
      return b
   elif a == 507:
      b = 10
      return b
   elif a == 508:
      b = 10
      return b
   elif a == 509:
      b = 10
      return b
   elif a == 510:
      b = 10
      return b
   elif a == 511:
      b = 10
      return b
   elif a == 512:
      b = 10
      return b
   elif a == 513:
      b = 5
      return b
   elif a == 514:
      b = 5
      return b
   elif a == 515:
      b = 5
      return b
   elif a == 516:
      b = 5
      return b
   elif a == 517:
      b = 5
      return b
   elif a == 518:
      b = 5
      return b
   elif a == 519:
      b = 5
      return b
   elif a == 520:
      b = 5
      return b
   elif a == 521:
      b = 5
      return b
   elif a == 522:
      b = 5
      return b
   elif a == 523:
      b = 15
      return b
   elif a == 524:
      b = 10
      return b
   elif a == 525:
      b = 5
      return b
   elif a == 526:
      b = 1
      return b
   elif a == 527:
      b = 10
      return b
   elif a == 528:
      b = 10
      return b
   elif a == 529:
      b = 5
      return b
   elif a == 530:
      b = 5
      return b
   elif a == 531:
      b = 1
      return b
   elif a == 532:
      b = 5
      return b
   elif a == 533:
      b = 15
      return b
   elif a == 534:
      b = 10
      return b
   elif a == 535:
      b = 10
      return b
   elif a == 536:
      b = 5
      return b
   elif a == 537:
      b = 5
      return b
   elif a == 538:
      b = 10
      return b
   elif a == 539:
      b = 10
      return b
   elif a == 540:
      b = 15
      return b
   else:
      b = 0
      return b




def ItemValue (ID):
   a = ID
   b = ""
   if a == 0:
      b = 0
      return b
   elif a == 1:
      b = 13
      return b
   elif a == 101:
      b = 50
      return b
   elif a == 102:
      b = 50
      return b
   elif a == 103:
      b = 20
      return b
   elif a == 104:
      b = 100
      return b
   elif a == 105:
      b = 30
      return b
   elif a == 106:
      b = 75
      return b
   elif a == 108:
      b = 50
      return b
   elif a == 109:
      b = 125
      return b
   elif a == 110:
      b = 20
      return b
   elif a == 111:
      b = 15
      return b
   elif a == 112:
      b = 15
      return b
   elif a == 113:
      b = 15
      return b
   elif a == 114:
      b = 15
      return b
   elif a == 115:
      b = 5
      return b
   elif a == 116:
      b = 20
      return b
   elif a == 117:
      b = 30
      return b
   elif a == 118:
      b = 55
      return b
   elif a == 119:
      b = 40
      return b
   elif a == 120:
      b = 30
      return b
   elif a == 121:
      b = 15
      return b
   elif a == 122:
      b = 15
      return b
   elif a == 123:
      b = 15
      return b
   elif a == 124:
      b = 15
      return b
   elif a == 125:
      b = 15
      return b
   elif a == 126:
      b = 15
      return b
   elif a == 127:
      b = 35
      return b
   elif a == 128:
      b = 25
      return b
   elif a == 200:
      b = 0
      return b
   elif a == 201:
      b = 15
      return b
   elif a == 202:
      b = 15
      return b
   elif a == 203:
      b = 5
      return b
   elif a == 204:
      b = 1
      return b
   elif a == 205:
      b = 1
      return b
   elif a == 206:
      b = 30
      return b
   elif a == 207:
      b = 20
      return b
   elif a == 208:
      b = 15
      return b
   elif a == 209:
      b = 3
      return b
   elif a == 210:
      b = 17
      return b
   elif a == 211:
      b = 10
      return b
   elif a == 212:
      b = 14
      return b
   elif a == 213:
      b = 5
      return b
   elif a == 214:
      b = 5
      return b
   elif a == 215:
      b = 0
      return b
   elif a == 216:
      b = 150
      return b
   elif a == 217:
      b = 40
      return b
   elif a == 218:
      b = 20
      return b
   elif a == 219:
      b = 5
      return b
   elif a == 220:
      b = 50
      return b
   elif a == 221:
      b = 30
      return b
   elif a == 222:
      b = 15
      return b
   elif a == 223:
      b = 15
      return b
   elif a == 224:
      b = 10
      return b
   elif a == 225:
      b = 10
      return b
   elif a == 226:
      b = 5
      return b
   elif a == 227:
      b = 10
      return b
   elif a == 228:
      b = 10
      return b
   elif a == 229:
      b = 0
      return b
   elif a == 230:
      b = 25
      return b
   elif a == 231:
      b = 15
      return b
   elif a == 232:
      b = 0
      return b
   elif a == 233:
      b = 0
      return b
   elif a == 234:
      b = 0
      return b
   elif a == 235:
      b = 0
      return b
   elif a == 236:
      b = 0
      return b
   elif a == 237:
      b = 0
      return b
   elif a == 238:
      b = 10
      return b
   elif a == 239:
      b = 3
      return b
   elif a == 240:
      b = 75
      return b
   elif a == 241:
      b = 30
      return b
   elif a == 242:
      b = 45
      return b
   elif a == 243:
      b = 100
      return b
   elif a == 244:
      b = 35
      return b
   elif a == 245:
      b = 15
      return b
   elif a == 246:
      b = 20
      return b
   elif a == 247:
      b = 80
      return b
   elif a == 248:
      b = 25
      return b
   elif a == 249:
      b = 45
      return b
   elif a == 250:
      b = 45
      return b
   elif a == 251:
      b = 10
      return b
   elif a == 252:
      b = 0
      return b
   elif a == 253:
      b = 3
      return b
   elif a == 254:
      b = 0
      return b
   elif a == 255:
      b = 15
      return b
   elif a == 256:
      b = 20
      return b
   elif a == 257:
      b = 30
      return b
   elif a == 258:
      b = 30
      return b
   elif a == 259:
      b = 50
      return b
   elif a == 260:
      b = 45
      return b
   elif a == 500:
      b = 5
      return b
   elif a == 501:
      b = 15
      return b
   elif a == 502:
      b = 70
      return b
   elif a == 503:
      b = 10
      return b
   elif a == 504:
      b = 10
      return b
   elif a == 505:
      b = 10
      return b
   elif a == 506:
      b = 10
      return b
   elif a == 507:
      b = 10
      return b
   elif a == 508:
      b = 25
      return b
   elif a == 509:
      b = 25
      return b
   elif a == 510:
      b = 25
      return b
   elif a == 511:
      b = 25
      return b
   elif a == 512:
      b = 25
      return b
   elif a == 513:
      b = 20
      return b
   elif a == 514:
      b = 20
      return b
   elif a == 515:
      b = 20
      return b
   elif a == 516:
      b = 20
      return b
   elif a == 517:
      b = 20
      return b
   elif a == 518:
      b = 50
      return b
   elif a == 519:
      b = 50
      return b
   elif a == 520:
      b = 150
      return b
   elif a == 521:
      b = 50
      return b
   elif a == 522:
      b = 50
      return b
   elif a == 523:
      b = 2
      return b
   elif a == 524:
      b = 7
      return b
   elif a == 525:
      b = 25
      return b
   elif a == 526:
      b = 5
      return b
   elif a == 527:
      b = 10
      return b
   elif a == 528:
      b = 2
      return b
   elif a == 529:
      b = 30
      return b
   elif a == 530:
      b = 40
      return b
   elif a == 531:
      b = 69
      return b
   elif a == 532:
      b = 75
      return b
   elif a == 533:
      b = 5
      return b
   elif a == 534:
      b = 10
      return b
   elif a == 535:
      b = 20
      return b
   elif a == 536:
      b = 20
      return b
   elif a == 537:
      b = 30
      return b
   elif a == 538:
      b = 20
      return b
   elif a == 539:
      b = 10
      return b
   elif a == 540:
      b = 5
      return b
   else:
      b = 0
      return b
      
#Bag+Stash
def moveStackBag (BagItemId, BagStack, x, y):
   a = BagItemId
   b = BagStack
   c = BagItemId[x]
   d = BagStack[x]
   e = BagItemId[y]
   f = BagStack[y]
   a[x] = e
   a[y] = c
   b[x] = f
   b[y] = d
   return a, b

def moveBagStash (BagItemId, BagStack, StashItemId, StashStack, x, y):
   a = BagItemId
   b = BagStack
   c = StashItemId
   d = StashStack
   e = BagItemId[x]
   f = BagStack[x]
   g = StashItemId[y]
   h = StashStack[y]
   a[x] = g
   b[x] = h
   c[y] = e
   d[y] = f
   return a, b, c, d

def moveStackStash (StashItemId, StashStack, x, y):
   a = StashItemId
   b = StashStack
   c = StashItemId[x]
   d = StashStack[x]
   e = StashItemId[y]
   f = StashStack[y]
   a[x] = e
   a[y] = c
   b[x] = f
   b[y] = d
   return a, b

#Actions
def doAlchemy ():
   #placeholder
   return

def doBattle ():
   #placeholder
   return

def doDiscard (BorS, BagItemId, BagStack, StashItemId, StashStack, x):
   a = BagItemId
   b = BagStack
   c = StashItemId
   d = StashStack
   if BorS == 0:
      a[x] = ""
      b[x] = ""
      return a, b, c, d
   elif BorS == 1:
      c[x] = ""
      d[x] = ""
      return a, b, c, d
   else:
      return

def doExplore ():
   #placeholder
   return

def ItemSubtract (BagStack, Amount, Slot):
   a = BagStack
   b = Amount
   c = Slot
   """
   if a[c] == "":
      return a
   elif a[c] == b:
      a[c] -= b
      checkZero()
      return a
   elif a[c] > b:
      a[c] -= b
      return a
   """

def ItemAdd (BagItemId, BagStack, ItemId, Amount):
   a = BagItemId
   b = BagStack
   c = ItemId
   d = Amount
   e = ItemMaxStack(c)
   """
   for i in range(0, 26):
      if (a[i] == c) and (b[i] < e):
         if (b[i] + d) < e:
            b[i] += d
            return a, b
            break
         else:
            l = (b[i] + d) - e
            b[i] = e
            d = l
            continue
      elif (a[i] == c) and (b[i] == e):
         continue
      else:
         continue
   while d > 0:
      for i in range(0, 26):
         if a[i] == "":
            if d <= e:
               a[i] = c
               b[i] = d
               d = 0
               return a, b
               break
            else:
               a[i] = c
               b[i] = e
               d -= e
               continue
   """



"""
   if a[e] == "":
      a[e] = c
      b[e] = d
      return a, b
   else:
      if a[e] == c:
         b[e] += d
         return a, b
      elif a[e] != c:
         f = ?itemOverride?(a, b, c, d, e)
         a = f[0]
         b = f[1]
         return a, b
      else:
         return a, b
"""
def doItemUse (BagItemId, BagStack, x):
   a = BagItemId
   b = BagStack
   useItem(a[x])

def doJizzPants ():
   #placeholder
   return

def doLustForcedMasturbate ():
   #placeholder
   return

def doMasturbate ():
   #placeholder
   return

def doSell (playerStats, BagItemId, BagStack, x, y, ItemValue):
   #placeholder
   return

def doSpecialAbility ():
   #placeholder
   return

def dyeThing ():
   #placeholder
   return

def useItem ():
   #placeholder
   return

def doNewGame ():
   CurrentText = ""
   SideText = ""
    
   time = list(("0", "08.00", "0"))
    #currentDay, currentTime, timeSinceLastSleep

   inBag = false
   inShop = false

   zoneData = list(("0", "false", "0", "true", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false"))
   #currentZone(1=Softlik, 2=Firmshaft, 3=Tieden 4=Siz'Calit, 5=Oviasis, 6=Sanctuary), inDungeon(true/false), currentDungeon, firstExplore(true/false), foundSoftlik(true/false), foundFirmshaft(true/false), foundTieden(true/false), foundSizCalit(true/false), foundOviasis(true/false), foundValley(true/false), foundSanctuary(true/false), defeatedMinotaur(true/false), defeatedFreakyGirl(true/false), defeatedSuccubus(true/false)

   playerStats = list(("100", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0"))
   #HP, lust, coin, strength, mentality, libido, sensitivity, hunger, HPMod, minLust, coinMod, strMod, mentMod, libMod, senMod, SexP, SexPMod, level, levelUP


   playerRace = ""
   #Original race of player
   playerAffinities = list(("0", "0", "0", "0" ))
   #humanAffinity, horseAffinity, wolfAffinity, catAffinity, lizardAffinity, cowAffinity, rabbitAffinity, mouseAffinity, birdAffinity, pigAffinity, skunkAffinity, bugAffinity, 

   fourBoobAffinity = 0
   twoBoobAffinity = 0
   sixBoobAffinity = 0
   eightBoobAffinity = 0
   tenBoobAffinity = 0
   cowTaurAffinity = 0
   humanTaurAffinity = 0

   playerAttributes = list(("", "", "", "", "", "", "", "" ))
   #gender(0=andro, 1=male, 2=female, 3=herm), race(1=human, 2=horse, 3=wolf, 4=cat, 5=lizard), body, dominant, hips, butt, tallness, skinType, tail, ears, hair, hairLength, hairColor, legType, wings, faceType, skinColor, cockTotal, humanCocks, horseCocks, wolfCocks, catCocks, lizardCocks, rabbitCocks, cockSize, cockMoistMod, balls, ballSize, showBalls(true/false), knot(true/false), bugCocks, breastSize, boobTotal, nippleSize, udders(true/false), udderSize, teatSize, clitSize, vagTotal, vagSize, vagMoist, vulvaSize, nipType, attireTop, attireBot, weapon, pregArray, pregStatus, pregnancyTime, pregRate, eggLaying, eggMaxTime, eggTime, eggRate, exhaustion, exhaustionPenalty, milkEngorgement, milkEngorgementLevel, udderEngorgement, udderEngorgementLevel, heat, heatTime, heatMaxTime, lactation, udderLactation,        runMod, rapeMod, cumMod, cockSizeMod, vagSizeMod, vagElastic, milkMod, carryMod, vagBellyMod, pregChanceMod, extraPregChance, pregTimeMod, enticeMod, milkHPMod, changeMod, milkCap, hipMod, buttMod, bellyMod, cockMoistMod, vagMoistMod,

   playerEffects = list(())

#Player

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
   snuggleBall = false
   fertileGel = 0
   eggType = 0
   milkSuppressant = 0
   milkSuppressantLact = 0
   milkSuppressantUdder = 0
   suppHarness = false
   fertilityStatueCurse = 0
   plumpQuats = 0
   cockSnakePreg = 0
   milkCPoisonNip = 0
   milkCPoisonUdd = 0
   cockSnakeVenom = 0
    
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
    
   #shapeshifty
   lockTail = 0
   lockFace = 0
   lockSkin = 0
   lockBreasts = 0
   lockEars = 0
   lockLegs = 0
   lockNipples = 0
   lockCock = 0
    
   #enemy
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
    
    
   lila = list(("0", "0", "0", "-2", "0", "0", "false"))
   #lilaRep, lilaVulva, lilaMilk, lilaPreg, lilaWetness, lilaWetStatus, lilaUB(true/false)

   malon = list(("0", "0", "0"))
   #malonRep, malonPreg, malonChildren 

    
   #mistress
   mistressRep = 0

   jamie = list(("0", "4", "0", "0", "0", "0", "false", "false", "false"))
   #jamieRep1, jamieSize, jamieChildren, jamieRep1, jamieRep2, jamieRep3, jamieButt(true/false), jamieBreasts(true/false), jamieHair(true/false)
    
   sil = list(("0", "0", "0", "10", "false", "0"))
   #silRep, silPreg, silRate, silLay, silTied, silGrowthTime

    
    
   dairyFarmBrand = false
   travArray = []

    
   playerAlchRecip = list(("false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false"))
   #knowLustDraft, knowRejuvPot, knowExpPreg, knowBallSwell, knowMaleEnhance, knowSLustDraft, knowSRejuvPot, knowSExpPreg, knowSBallSwell, knowBabyFree, knowPotPot, knowGenSwap, knowMasoPot, knowMilkSuppress, knowSGenSwap, knowSMasoPot, knowSBabyFree, knowSPotPot, knowPussJuice, knowPheromone, knowBazoomba

   playerSkills = list(("0", "0", "0", "0", "0", "0", "0", "", ""))
   #babyFactLevel, bodyBuildLevel, hyperHappyLevel, alchemistLevel, fetishMasterLevel, milkMaidLevel, shapeshiftyLevel, shapeshiftyFirst, shapeshiftySecond

   fetish = list(())

   #fetish
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
    
   children = list(())
   #currentDayCare(), 
   #children
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
   BagItemId = list(())
   BagStach = list(())
   StashItemId = list(())
   StashStack = list(())


def doRace ():
   #placeholder
   return

def doGender ():
   #placeholder
   return


#Places
def doBeach ():
   #placeholder
   return

def doDairyFarm ():
   #placeholder
   return

def doDayCare ():
   #placeholder
   return

def doDen ():
   #placeholder
   return

def doDesert ():
   #placeholder
   return

def doFirmshaft ():
   #placeholder
   return

def doForest ():
   #placeholder
   return

def doJungle ():
   #placeholder
   return

def doLake ():
   #placeholder
   return

def doOldCave ():
   #placeholder
   return

def doOldCaveDescent ():
   #placeholder
   return

def doOviasis ():
   #placeholder
   return

def doPlains ():
   #placeholder
   return

def doSavanna ():
   #placeholder
   return

def doSizCalit ():
   #placeholder
   return

def doSoftlik ():
   #placeholder
   return

def doTieden ():
   #placeholder
   return

def doValley ():
   #placeholder
   return

def knotholeMain ():
   #placeholder
   return

def knotholeUpstairs ():
   #placeholder
   return

#Shops
def doApothecary ():
   #placeholder
   return

def doDyeShop ():
   #placeholder
   return

def doGeneral ():
   #placeholder
   return

def doSalon ():
   #placeholder
   return

def doTailor ():
   #placeholder
   return
   
def GameStartup ():
   """
   Function called at game startup. Sets all variables to default values and sets main welcom text.
   """
   CurrentText = "Nimin: Fetish Fantasy" + "\n" + "v" + str(__version__) + "\n\n" + "Click 'New Game' to begin a new game." + "\n\n" + "Created by:    --Xadera" + "\n" + "     www.furaffinity.net/user/xadera/" + "\n\n" + "Original concept by:     --Fenoxo" + "\n" + "     fenoxo.com" + "\n\n\n" + "Currently maintained by ajdelguidice" + "\n" + "https://github.com/ajdelguidice"

#Game Functions
def checkZero ():
   for i in range(0, 26):
      if BagStack[i] == 0:
         BagItemId[i] = ""
         BagStack[i] = ""
   for i in range(0, 26):
      if StashStack[i] == 0:
         StashItemId[i] = ""
         StashStack[i] = ""
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

def checkDecimal ():
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

def windowRefresh ():
   checkZero()
   checkDecimal()

def GameStartup ():
   """
   Function called at game startup. Sets all variables to default values and sets main welcom text.
   """
   global versionNumber = __version__
   global theme = 0
   global fontSize = 14
   global fontBold = false
   global fontColour = "000000"
   global showSide = true
   global i = 0
   global buttonChoice = 0
   global currentText = ""
   global sideText = ""
   global sideFocus = 1
   global pregTempInt = 0
   global pregTempBool = false
   global lustArray = []
#   global bg = new Sprite()
   global rndResult = 0
   global rndArray = []
   global textCheckArray = []
   global choiceListArray = []
   global choiceListResult = []
   global choicePage = 0
   global moveItemID = 0
   global moveItemStack = 0
   global skipExhaustion = false
   global shiftHeld = false
   global currentState = 0
   global inBag = false
   global inShop = false
   global currentZone = 0
   global day = 0
   global hour = 8
   global inDungeon = false
   global currentDungeon = 0
   global str = 0
   global ment = 0
   global lib = 0
   global sen = 0
   global HP = 0
   global lust = 0
   global coin = 0
   global strMod = 0
   global mentMod = 0
   global libMod = 0
   global senMod = 0
   global strength = 0
   global mentality = 0
   global libido = 0
   global sensitivity = 0
   global hunger = 0
   global hrs = 0
   global itemGainArray = []
   global human = 0
   global horse = 0
   global wolf = 0
   global cat = 0
   global cow = 0
   global lizard = 0
   global rabbit = 0
   global mouse = 0
   global bird = 0
   global pig = 0
   global skunk = 0
   global bug = 0
   global SexP = 0
   global levelUP = 0
   global level = 0
   global runMod = 0
   global rapeMod = 0
   global cumMod = 1
   global cockSizeMod = 1
   global vagSizeMod = 1
   global vagElastic = 1
   global milkMod = 0
   global carryMod = 0
   global vagBellyMod = 0
   global pregChanceMod = 0
   global extraPregChance = 0
   global pregTimeMod = 0
   global enticeMod = 0
   global milkHPMod = 0
   global changeMod = 1
   global HPMod = 0
   global SexPMod = 1
   global minLust = 0
   global milkCap = 0
   global coinMod = 0
   global hipMod = 1
   global buttMod = 1
   global bellyMod = 0
   global cockMoistMod = 0
   global vagMoistMod = 0
   global lockTail = 0
   global lockFace = 0
   global lockSkin = 0
   global lockBreasts = 0
   global lockEars = 0
   global lockLegs = 0
   global lockNipples = 0
   global lockCock = 0
   global enemyID = 0
   global eHP = 0
   global eMaxHP = 0
   global eStr = 0
   global eMenta = 0
   global eSen = 0
   global eLib = 0
   global eLust = 0
   global eGen = 0
   global ePref = 0
   global eCoin = 0
   global eSexP = 0
   global eItem = 0
   global gender = 0
   global race = 0
   global body = 0
   global dominant = 0
   global hips = 0
   global butt = 0
   global tallness = 0
   global skinType = 0
   global tail = 0
   global ears = 0
   global hair = 0
   global hairLength = 0
   global hairColor = 0
   global legType = 0
   global wings = 0
   global faceType = 0
   global skinColor = 0
   global cockTotal = 0
   global humanCocks = 0
   global horseCocks = 0
   global wolfCocks = 0
   global catCocks = 0
   global lizardCocks = 0
   global rabbitCocks = 0
   global cockSize = 0
   global cockMoist = 0
   global balls = 0
   global ballSize = 0
   global showBalls = true
   global knot = false
   global bugCocks = 0
   global breastSize = 0
   global boobTotal = 0
   global nippleSize = 1
   global udders = false
   global udderSize = 0
   global teatSize = 0
   global clitSize = 0
   global vagTotal = 0
   global vagSize = 0
   global vagMoist = 0
   global vulvaSize = 0
   global nipType = 0
   global attireTop = 1
   global attireBot = 2
   global weapon = 10
   global pregArray = []
   global pregStatus = 0
   global pregnancyTime = 0
   global pregRate = 1
   global eggLaying = 0
   global eggMaxTime = 0
   global eggTime = 0
   global eggRate = 0
   global exhaustion = 0
   global exhaustionPenalty = 0
   global milkEngorgement = 0
   global milkEngorgementLevel = 0
   global udderEngorgement = 0
   global udderEngorgementLevel = 0
   global heat = 0
   global heatTime = 0
   global heatMaxTime = 0
   global lactation = 0
   global udderLactation = 0
   global nipplePlay = 0
   global udderPlay = 0
   global blueBalls = 0
   global teatPump = 0
   global nipPump = 0
   global cockPump = 0
   global clitPump = 0
   global vulvaPump = 0
   global masoPot = 0
   global sMasoPot = 0
   global babyFree = 0
   global charmTime = 0
   global pheromone = 0
   global eggceleratorTime = 0
   global eggceleratorDose = 0
   global bodyOil = 0
   global lustPenalty = 0
   global snuggleBall = false
   global fertileGel = 0
   global eggType = 0
   global milkSuppressant = 0
   global milkSuppressantLact = 0
   global milkSuppressantUdder = 0
   global suppHarness = false
   global fertilityStatueCurse = 0
   global plumpQuats = 0
   global lilaWetStatus = 0
   global cockSnakePreg = 0
   global milkCPoisonNip = 0
   global milkCPoisonUdd = 0
   global cockSnakeVenom = 0
   global humanAffinity = 0
   global horseAffinity = 0
   global wolfAffinity = 0
   global catAffinity = 0
   global cowAffinity = 0
   global lizardAffinity = 0
   global rabbitAffinity = 0
   global fourBoobAffinity = 0
   global mouseAffinity = 0
   global birdAffinity = 0
   global pigAffinity = 0
   global twoBoobAffinity = 0
   global sixBoobAffinity = 0
   global eightBoobAffinity = 0
   global tenBoobAffinity = 0
   global cowTaurAffinity = 0
   global humanTaurAffinity = 0
   global skunkAffinity = 0
   global bugAffinity = 0
   global lilaRep = 0
   global lilaVulva = 0
   global lilaMilk = 0
   global lilaPreg = -2
   global malonRep = 0
   global malonPreg = 0
   global malonChildren = 0
   global mistressRep = 0
   global jamieRep = 0
   global jamieSize = 4
   global jamieChildren = 0
   global silRep = 0
   global silPreg = 0
   global silRate = 0
   global silLay = 10
   global silTied = false
   global silGrowthTime = 0
   global lilaUB = false
   global dairyFarmBrand = false
   global jamieRep1 = 0
   global jamieRep2 = 0
   global jamieRep3 = 0
   global lilaWetness = 0
   global jamieButt = false
   global jamieBreasts = false
   global jamieHair = false
   global travArray = []
   global foundSoftlik = false
   global foundFirmshaft = false
   global foundTieden = false
   global foundSizCalit = false
   global foundOviasis = false
   global foundValley = false
   global foundSanctuary = false
   global defeatedMinotaur = false
   global defeatedFreakyGirl = false
   global defeatedSuccubus = false
   global firstExplore = false
   global knowLustDraft = false
   global knowRejuvPot = false
   global knowExpPreg = false
   global knowBallSwell = false
   global knowMaleEnhance = false
   global knowSLustDraft = false
   global knowSRejuvPot = false
   global knowSExpPreg = false
   global knowSBallSwell = false
   global knowBabyFree = false
   global knowPotPot = false
   global knowGenSwap = false
   global knowMasoPot = false
   global knowMilkSuppress = false
   global knowSGenSwap = false
   global knowSMasoPot = false
   global knowSBabyFree = false
   global knowSPotPot = false
   global knowPussJuice = false
   global knowPheromone = false
   global knowBazoomba = false
   global babyFactLevel = 0
   global bodyBuildLevel = 0
   global hyperHappyLevel = 0
   global alchemistLevel = 0
   global fetishMasterLevel = 0
   global milkMaidLevel = 0
   global shapeshiftyLevel = 0
   global shapeshiftyFirst = ""
   global shapeshiftySecond = ""
   global maleFetish = 1
   global femaleFetish = 1
   global hermFetish = 1
   global narcissistFetish = 1
   global dependentFetish = 1
   global dominantFetish = 1
   global submissiveFetish = 1
   global lboobFetish = 1
   global sboobFetish = 1
   global furryFetish = 1
   global scalyFetish = 1
   global smoothyFetish = 1
   global pregnancyFetish = 1
   global bestialityFetish = 1
   global milkFetish = 1
   global sizeFetish = 1
   global unbirthingFetish = 1
   global ovipositionFetish = 1
   global toyFetish = 1
   global hyperFetish = 1
   global currentDayCare = 0
   global humanChildren = 0
   global equanChildren = 0
   global lupanChildren = 0
   global felinChildren = 0
   global cowChildren = 0
   global lizanEggs = 0
   global lizanChildren = 0
   global bunnionChildren = 0
   global wolfPupChildren = 0
   global miceChildren = 0
   global birdEggs = 0
   global birdChildren = 0
   global pigChildren = 0
   global calfChildren = 0
   global bugEggs = 0
   global bugChildren = 0
   global skunkChildren = 0
   global minotaurChildren = 0
   global freakyGirlChildren = 0
   global bagPage = 1
   global bagArray = []
   global bagStackArray = []
   global stashArray = []
   global stashStackArray = []
   global stage.addEventListener(KeyboardEvent.KEY_DOWN,this.hotKeys)
   global stage.addEventListener(KeyboardEvent.KEY_UP,this.keysUp)
   global newGame.addEventListener(MouseEvent.CLICK,this.newGameStart)
   global Choice1.addEventListener(MouseEvent.CLICK,this.buttonEvent1)
   global Choice2.addEventListener(MouseEvent.CLICK,this.buttonEvent2)
   global Choice3.addEventListener(MouseEvent.CLICK,this.buttonEvent3)
   global Choice4.addEventListener(MouseEvent.CLICK,this.buttonEvent4)
   global Choice5.addEventListener(MouseEvent.CLICK,this.buttonEvent5)
   global Choice6.addEventListener(MouseEvent.CLICK,this.buttonEvent6)
   global Choice7.addEventListener(MouseEvent.CLICK,this.buttonEvent7)
   global Choice8.addEventListener(MouseEvent.CLICK,this.buttonEvent8)
   global Choice9.addEventListener(MouseEvent.CLICK,this.buttonEvent9)
   global Choice10.addEventListener(MouseEvent.CLICK,this.buttonEvent10)
   global Choice11.addEventListener(MouseEvent.CLICK,this.buttonEvent11)
   global Choice12.addEventListener(MouseEvent.CLICK,this.buttonEvent12)
   global appearanceText.addEventListener(MouseEvent.CLICK,this.appearance)
   global saveGame.addEventListener(MouseEvent.CLICK,this.saveG)
   global loadGame.addEventListener(MouseEvent.CLICK,this.loadG)
   global Side1.addEventListener(MouseEvent.CLICK,this.side1Event)
   global Side2.addEventListener(MouseEvent.CLICK,this.side2Event)
   global Side3.addEventListener(MouseEvent.CLICK,this.side3Event)
   global Side4.addEventListener(MouseEvent.CLICK,this.side4Event)
   global Side5.addEventListener(MouseEvent.CLICK,this.side5Event)
   global Side6.addEventListener(MouseEvent.CLICK,this.side6Event)
   global Side7.addEventListener(MouseEvent.CLICK,this.side7Event)
   global Side8.addEventListener(MouseEvent.CLICK,this.side8Event)
   global Option1.addEventListener(MouseEvent.CLICK,this.option1Event)
   global Option2.addEventListener(MouseEvent.CLICK,this.option2Event)
   global Option3.addEventListener(MouseEvent.CLICK,this.option3Event)
   global Option4.addEventListener(MouseEvent.CLICK,this.option4Event)
   global Option5.addEventListener(MouseEvent.CLICK,this.option5Event)
   global Option6.addEventListener(MouseEvent.CLICK,this.option6Event)
   global Option7.addEventListener(MouseEvent.CLICK,this.option7Event)
   global scrollBar1.scrollTarget = this.outputWindow
   global scrollBar2.scrollTarget = this.sideWindow
   global statPane.visible = false
   global levelPane.visible = false
   global currentRegion.visible = false
   global region.visible = false
   global saveGame.visible = false
   global saveGameOutline.visible = false
   global DayPane.visible = false
   global Option7.visible = false
   global sideHide()
   global appearanceText.visible = false
   global appearanceBox.visible = false
   global pageNum.embedFonts = true
   global pageNum.visible = false
   global pageNum.rotation += 90
   global moveItem.visible = false
   global moveItemAmount.visible = false
   global MoveOutline.visible = false
   global MoveAmountOutline.visible = false
   global addChildAt(this.bg,0)
   global viewButtonText(0,0,0,0,0,0,0,0,0,0,0,0)
   global viewButtonOutline(0,0,0,0,0,0,0,0,0,0,0,0)
   global hideAmount()
   global hideUpDown()
   global loadPreferences()
   global CurrentText = "Nimin: Fetish Fantasy" + "\n" + "v" + versionNumber + "\n\n" + "Click 'New Game' to begin a new game." + "\n\n" + "Created by:    --Xadera" + "\n" + "     www.furaffinity.net/user/xadera/" + "\n\n" + "Original concept by:     --Fenoxo" + "\n" + "     fenoxo.com" + "\n\n\n" + "Currently maintained by ajdelguidice" + "\n" + "https://github.com/ajdelguidice"

#Tests
def Test ():
   """
   Test function
   """
   a = list((0, 0.00, 0))
   print(ClockStep(a, 9.50))
   print(Wait(a, 80))
   print(Sleep(a, 80))
   b = list(("","","","115","","","","","","","","","","","","","","","","","","","","","","","",""))
   c = list(("","","","2","","","","","","","","","","","","","","","","","","","","","","",""))
   #print(ItemSubtract(c, 1, 4))
   #print(ItemAdd(b, c, 115, 2))
   #print(ItemAdd(b, c, 115, 6))
Test()


"""

public function newGameGo() : void
      {
         this.appearanceText.visible = false;
         this.appearanceBox.visible = false;
         this.saveGame.visible = false;
         this.saveGameOutline.visible = false;
         this.buttonConfirm();
         this.outputMainText("Are you sure you would like to start a new game?",true);
         if(this.currentState == 0)
         {
            this.Choice7.visible = false;
         }
         this.doListen = function():void
         {
            if(buttonChoice == 6)
            {
               hideUpDown();
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
               submissiveFetish = 1;this.
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
            }
            else
            {
               doReturn();
            }
         };
      }
public function doRace() : void
      {
         trace("race");
         trace(this.tallness);
         this.bc();
         this.viewButtonText(1,0,1,0,0,1,0,0,1,0,1,0);
         this.viewButtonOutline(1,0,1,0,0,1,0,0,1,0,1,0);
         this.Choice1.htmlText = "Equan";
         this.Choice3.htmlText = "Lupan";
         this.Choice6.htmlText = "Human";
         this.Choice9.htmlText = "Felin";
         this.Choice11.htmlText = "Lizan";
         this.outputMainText("Choose which race you want to be:",true);
         this.outputMainText("\r\rHuman - A race supposedly descendant of apes, their curious minds are more open to change and their skin is slightly more sensitive.",false);
         this.outputMainText("\r\rEquan - A race supposedly descendant of horses, their large genitals make them slightly more sexual and their muscles are more powerful.",false);
         this.outputMainText("\r\rLupan - A race supposedly descendant of wolves, their lean bodies are stronger and their minds more quick-witted.",false);
         this.outputMainText("\r\rFelin - A race supposedly descendant of cats, their lust-driven society makes them a bit more sexual and sensitive.",false);
         this.outputMainText("\r\rLizan - A race supposedly descendant of some kind of reptile, their desert-adapted bodies have made them stronger, but they\'re still careful as their scales make them somewhat sensitive.",false);
         this.doListen = function():void
         {
            boobTotal = 2;
            if(buttonChoice == 6)
            {
               race = 1;
               changeMod += 0.5;
               currentZone = 1;
               foundSoftlik = true;
               humanAffinity = 50;
               dominant = 1;
               ears = 1;
               skinType = 1;
               faceType = 10;
               strength = 15;
               mentality = 17;
               libido = 15;
               sensitivity = 17;
               doGender();
            }
            if(buttonChoice == 1)
            {
               race = 2;
               foundFirmshaft = true;
               currentZone = 2;
               horseAffinity = 50;
               cockSizeMod += 1;
               vagSizeMod += 1;
               dominant = 2;
               tail = 2;
               ears = 2;
               skinType = 2;
               faceType = 20;
               strength = 17;
               mentality = 15;
               libido = 17;
               sensitivity = 15;
               tallness += 4;
               doGender();
            }
            if(buttonChoice == 3)
            {
               race = 3;
               foundTieden = true;
               currentZone = 3;
               wolfAffinity = 50;
               knot = true;
               boobTotal = 6;
               dominant = 3;
               tail = 3;
               ears = 3;
               skinType = 2;
               faceType = 30;
               strength = 17;
               mentality = 17;
               libido = 15;
               sensitivity = 15;
               tallness += -2;
               doGender();
            }
            if(buttonChoice == 9)
            {
               race = 4;
               foundSizCalit = true;
               currentZone = 4;
               catAffinity = 50;
               dominant = 4;
               ++heat;
               heatMaxTime = 96;
               heatTime = 96;
               boobTotal = 6;
               tail = 4;
               ears = 4;
               skinType = 2;
               faceType = 40;
               strength = 15;
               mentality = 15;
               libido = 17;
               sensitivity = 17;
               tallness += -3;
               doGender();
            }
            if(buttonChoice == 11)
            {
               race = 6;
               foundOviasis = true;
               currentZone = 6;
               lizardAffinity = 50;
               dominant = 6;
               eggLaying = 1;
               eggTime = 36;
               eggMaxTime = 36;
               tail = 6;
               ears = 6;
               skinType = 3;
               faceType = 60;
               strength = 17;
               mentality = 16;
               libido = 15;
               sensitivity = 16;
               tallness += 2;
               doGender();
            }
         };
      }
      
      public function doGender() : void
      {
         this.currentDayCare = this.dominant;
         this.statDisplay();
         this.viewButtonText(0,0,0,0,1,1,1,0,0,0,0,0);
         this.viewButtonOutline(0,0,0,0,1,1,1,0,0,0,0,0);
         this.Choice5.htmlText = "Male";
         this.Choice6.htmlText = "Female";
         this.Choice7.htmlText = "Herm";
         this.outputMainText("Choose which gender you want to be:\r\rMale - You has painus!\r\rFemale - You has vagoo!\r\rHerm - You has painus and vagoo!",true);
         this.doListen = function():void
         {
            if(buttonChoice == 5)
            {
               gender = 1;
            }
            if(buttonChoice == 6)
            {
               gender = 2;
            }
            if(buttonChoice == 7)
            {
               gender = 3;
            }
            if(gender == 1)
            {
               cockSize = 12;
               ballSize = 3;
               balls = 2;
               cockTotal = 1;
               cockMoist = 1;
               ++strength;
               if(dominant == 1)
               {
                  humanCocks = 1;
               }
               if(dominant == 2)
               {
                  horseCocks = 1;
               }
               if(dominant == 3)
               {
                  wolfCocks = 1;
               }
               if(dominant == 4)
               {
                  catCocks = 1;
               }
               if(dominant == 6)
               {
                  lizardCocks = 2;
                  ++cockTotal;
               }
            }
            if(gender == 2)
            {
               vagSize = 12;
               vulvaSize = 5;
               pregArray = [false,0,0,0,0];
               vagTotal = 1;
               vagMoist = 1;
               clitSize = 2;
               ++mentality;
            }
            if(gender == 3)
            {
               cockSize = 8;
               ballSize = 2;
               balls = 2;
               cockTotal = 1;
               cockMoist = 1;
               pregArray = [false,0,0,0,0];
               vagTotal = 1;
               vagMoist = 1;
               vagSize = 8;
               vulvaSize = 3;
               if(dominant == 1)
               {
                  humanCocks = 1;
               }
               if(dominant == 2)
               {
                  horseCocks = 1;
               }
               if(dominant == 3)
               {
                  wolfCocks = 1;
               }
               if(dominant == 4)
               {
                  catCocks = 1;
               }
               if(dominant == 6)
               {
                  lizardCocks = 2;
                  ++cockTotal;
               }
               ++libido;
            }
            bodyType();
         };
      }
      
      public function bodyType() : void
      {
         this.statDisplay();
         if(this.gender == 1)
         {
            this.viewButtonOutline(1,0,1,0,1,0,1,0,0,1,0,0);
            this.viewButtonText(1,0,1,0,1,0,1,0,0,1,0,0);
            this.buttonWrite(1,"Bodybuilder");
            this.buttonWrite(3,"Average");
            this.buttonWrite(5,"Cunt Boy");
            this.buttonWrite(7,"Femme Boy");
            this.buttonWrite(10,"Childlike");
         }
         if(this.gender == 2)
         {
            this.viewButtonOutline(0,1,1,0,1,0,0,0,0,1,0,0);
            this.viewButtonText(0,1,1,0,1,0,0,0,0,1,0,0);
            this.buttonWrite(2,"Bodybuilder");
            this.buttonWrite(5,"Average");
            this.buttonWrite(3,"Voluptuous");
            this.buttonWrite(10,"Childlike");
         }
         if(this.gender == 3)
         {
            this.viewButtonOutline(0,1,0,0,1,1,0,0,0,1,0,0);
            this.viewButtonText(0,1,0,0,1,1,0,0,0,1,0,0);
            this.buttonWrite(2,"Bodybuilder");
            this.buttonWrite(5,"Masculine");
            this.buttonWrite(6,"Feminine");
            this.buttonWrite(10,"Childlike");
         }
         this.outputMainText("Choose your body type. Types determine height and a few beginning characteristics. Their names describe what they look like and may potentially alter your true gender.",true);
         this.doListen = function():void
         {
            if(gender == 1)
            {
               if(buttonChoice == 1)
               {
                  body = 29;
                  hips = 4;
                  butt = 4;
                  tallness += 70 + Math.floor(percent() / 10);
                  strength += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 3)
               {
                  body = 20;
                  hips = 3;
                  butt = 3;
                  tallness += 68 + Math.floor(percent() / 10);
                  libido += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 5)
               {
                  body = 20;
                  hips = 3;
                  butt = 3;
                  tallness += 68 + Math.floor(percent() / 10);
                  libido += 1;
                  stats(0,0,0,0);
                  cockSize = 0;
                  ballSize = 0;
                  balls = 0;
                  cockTotal = 0;
                  cockMoist = 0;
                  humanCocks = 0;
                  horseCocks = 0;
                  wolfCocks = 0;
                  catCocks = 0;
                  lizardCocks = 0;
                  vagSize = 8;
                  vulvaSize = 3;
                  pregArray = [false,0,0,0,0];
                  gender = 2;
                  vagTotal = 1;
                  vagMoist = 1;
                  clitSize = 2;
                  doStartingDescription();
               }
               if(buttonChoice == 7)
               {
                  body = 15;
                  hips = 7;
                  butt = 6;
                  breastSize = 2;
                  nippleSize = 2;
                  tallness += 60 + Math.floor(percent() / 10);
                  sensitivity += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 10)
               {
                  body = 7;
                  hips = 1;
                  butt = 2;
                  tallness += 42 + Math.floor(percent() / 10);
                  sensitivity += 2;
                  mentality -= 2;
                  strength -= 4;
                  libido += 2;
                  cockSize = 6;
                  cockMoist = 1;
                  ballSize = 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
            }
            if(gender == 2)
            {
               if(buttonChoice == 2)
               {
                  body = 29;
                  hips = 5;
                  butt = 4;
                  tallness += 68 + Math.floor(percent() / 10);
                  breastSize = 4;
                  nippleSize = 4;
                  strength += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 3)
               {
                  body = 16;
                  hips = 9;
                  butt = 6;
                  tallness += 60 + Math.floor(percent() / 10);
                  breastSize = 10;
                  nippleSize = 10;
                  libido += 2;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 5)
               {
                  body = 13;
                  hips = 6;
                  butt = 5;
                  tallness += 60 + Math.floor(percent() / 10);
                  breastSize = 6;
                  nippleSize = 6;
                  mentality += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 10)
               {
                  body = 7;
                  hips = 2;
                  butt = 2;
                  tallness += 41 + Math.floor(percent() / 10);
                  sensitivity += 2;
                  mentality -= 2;
                  strength -= 4;
                  libido += 2;
                  vagSize = 6;
                  breastSize = 2;
                  nippleSize = 2;
                  vulvaSize = 2;
                  clitSize = 1;
                  vagMoist = 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
            }
            if(gender == 3)
            {
               if(buttonChoice == 2)
               {
                  body = 29;
                  hips = 4;
                  butt = 4;
                  tallness += 68 + Math.floor(percent() / 10);
                  breastSize = 6;
                  nippleSize = 6;
                  strength += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 5)
               {
                  body = 19;
                  hips = 3;
                  butt = 3;
                  tallness += 62 + Math.floor(percent() / 10);
                  breastSize = 2;
                  nippleSize = 2;
                  libido += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 6)
               {
                  body = 14;
                  hips = 5;
                  butt = 4;
                  tallness += 58 + Math.floor(percent() / 10);
                  breastSize = 6;
                  nippleSize = 6;
                  mentality += 1;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
               if(buttonChoice == 10)
               {
                  body = 7;
                  hips = 2;
                  butt = 2;
                  tallness += 42 + Math.floor(percent() / 10);
                  sensitivity += 2;
                  mentality -= 2;
                  strength -= 4;
                  libido += 2;
                  cockSize = 4;
                  cockMoist = 1;
                  ballSize = 1;
                  vagSize = 4;
                  clitSize = 1;
                  vagMoist = 1;
                  vulvaSize = 1;
                  breastSize = 2;
                  nippleSize = 2;
                  stats(0,0,0,0);
                  doStartingDescription();
               }
            }
         };
      }
"""