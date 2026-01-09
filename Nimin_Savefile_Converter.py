import tkinter
from tkinter import filedialog, ttk
from miniamf import sol, amf3
from pathlib import Path
import xml.etree.ElementTree as xmletree
from platform import system
from io import StringIO
try:
   import tomllib
except:
   import tomli as tomllib

# TODO: Clean up interface logic
# TODO: General cleanup

platform = system()


class NullData(Exception):...


class FileTypeError(TypeError):...


def repintorfloat(number):
   '''
   Determines whether a number should be displayed as an integer or float based on its value and returns the corrected value. This is a substitute for the way ActionScript 3 displayed numbers as strings.
   EX:
      1.05 should be displayed as a float
      1.00 should be displayed as an integer
   '''
   if isinstance(number, int):
      return number
   if isinstance(number, str):
      number = float(number)
   if number.is_integer():
      return int(number)
   return number


def strtobool(a:str):
   low = a.lower()
   if low == 'true':
      return True
   if low == 'false':
      return False


class TOML:
   '''
   Simple TOML writer taken from as3lib. I own both projects so I don't feel
   the need to add a license here.
   '''
   def Value(value):
      if isinstance(value, str):
         return f'"{value}"'
      if isinstance(value, bool):
         return 'true' if value else 'false'
      if isinstance(value, (list, tuple)):
         return TOML.Array(value)
      if isinstance(value, dict):
         return TOML.Table(value)
      return f'{value}'

   def Table(value):
      with StringIO() as text:
         text.write('{')
         for k, v in value.items():
            text.write(f'{k} = {TOML.Value(v)},')
         temp = text.getvalue()
         if temp.endswith(','):  # TODO: Make this better
            return temp[:-1] + '}'
         return temp + '}'

   def Array(value):
      with StringIO() as text:
         text.write('[')
         for i in value:
            text.write(f'{TOML.Value(i)},')
         text.write(']')
         return text.getvalue()

   def Return(valDict):
      nontables = []
      tables = []
      for k, v in valDict.items():
         if isinstance(v, dict):
            tables.append(k)
         else:
            nontables.append(k)
      with StringIO() as text:
         for k in nontables:
            text.write(f'{k} = {TOML.Value(valDict[k])}\n')
         for k in tables:
            text.write('\n')  # This doesn't work when combined with next line for some reason
            text.write(f'["{k}"]\n' if str(k).find('.') != -1 else f'[{k}]\n')
            for k2, v2 in valDict[k].items():
               text.write(f'{k2} = {TOML.Value(v2)}\n')
         return text.getvalue()

   def write(file, valDict, mode='w'):
      with open(file, mode) as f:
         f.write(TOML.Return(valDict))

   def readFile(file):
      return tomllib.load(file)

   def readString(string):
      return tomllib.loads(string)


class ConvButton(tkinter.Button):
   def __init__(self, master, *args, **kwargs):
      super().__init__(master, *args, **kwargs)
      self['background'] = '#FFFFFF'
      self['activebackground'] = '#FFFFFF'
      self['highlightcolor'] = '#000000'
      self['highlightbackground'] = '#000000'
      self.bind('<Enter>', self._borderSet)
      self.bind('<Leave>', self._borderUnset)
      self.bind('<Button-1>', self._backgroundSet)
      self.bind('<ButtonRelease-1>', self._backgroundUnset)

   def _borderSet(self, *args):
      self['highlightcolor'] = '#0074BE'
      self['highlightbackground'] = '#0074BE'

   def _borderUnset(self, *args):
      self['highlightcolor'] = '#000000'
      self['highlightbackground'] = '#000000'

   def _backgroundSet(self, *args):
      self['background'] = '#A1D9FD'
      self['activebackground'] = '#A1D9FD'

   def _backgroundUnset(self, *args):
      self['background'] = '#FFFFFF'
      self['activebackground'] = '#FFFFFF'


class ConvEntry(tkinter.Entry):
   def __init__(self, master, *args, **kwargs):
      super().__init__(master, *args, **kwargs)
      self['background'] = '#FFFFFF'
      self['highlightcolor'] = '#000000'
      self['highlightbackground'] = '#000000'
      self.bind('<Enter>', self._borderSet)
      self.bind('<Leave>', self._borderUnset)

   def _borderSet(self, *args):
      self['highlightcolor'] = '#0074BE'
      self['highlightbackground'] = '#0074BE'

   def _borderUnset(self, *args):
      self['highlightcolor'] = '#000000'
      self['highlightbackground'] = '#000000'


class FileEntry(tkinter.Frame):
   @property
   def file(self):
      return self.entryvar.get()

   @property
   def type(self):
      return self.combovar.get()

   def __init__(self, master, *args, **kwargs):
      text = kwargs.pop('text')
      icon = kwargs.pop('icon')
      self.cls = kwargs.pop('cls')
      tkinter.Frame.__init__(self, master)
      self['background'] = '#FFFFFF'
      self.label = tkinter.Label(self, text=text, font=self.cls.font)
      self.label.place(x=0, y=0, height=24)
      self.label['background'] = '#FFFFFF'

      self.entryvar = tkinter.StringVar()
      self.entry = ConvEntry(self, textvariable=self.entryvar)
      self.entry.place(x=0, y=24, width=296, height=24, anchor='nw')
      self.button = ConvButton(self, command=self.chooseFile, image=icon)
      self.button.place(x=296, y=24, width=24, height=24, anchor='nw')

      self.typelabel = tkinter.Label(self, text='Type', font=self.cls.font)
      self.typelabel.place(x=340, y=0, width=40, height=24, anchor='nw')
      self.typelabel['background'] = '#FFFFFF'

      self.combovar = tkinter.StringVar()
      self.combo = ttk.Combobox(self, font=self.cls.font, textvariable=self.combovar, state='readonly')
      self.combo['values'] = ('detect', 'xml', 'sol', 'nim', 'toml')
      self.combo.set('detect')
      self.combo.place(x=340, y=24, width=60, height=24, anchor='nw')

   def chooseFile(self):
      f = filedialog.askopenfilename(initialdir=self.cls.path)
      if not isinstance(f, tuple) and f != '':
         self.entryvar.set(f)


class Converter:
   # TODO: Move converter stuff into here so global variables can be avoided
   def __init__(self):
      self.path = None

   def gui_open(self):
      self.root = tkinter.Tk()
      self.root.geometry('500x334')
      self.root.resizable(False, False)
      self.root.title('Pymin Savefile Converter')
      self.root['background'] = '#FFFFFF'

      self.fileicon = tkinter.PhotoImage(data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0c\x08\x06\x00\x00\x00k\xe7=\x81\x00\x00\x00\x01sRGB\x01\xd9\xc9,\x7f\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x80\xe8\x00\x00u0\x00\x00\xea`\x00\x00:\x98\x00\x00\x17p\x9c\xbaQ<\x00\x00\x00\x06bKGD\x00\xd3\x00\x9d\x00JT\xd4=\xdb\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x00JIDAT(\xcfc` \x00^l\xcf\xe1{\xb1=\x87\t\x97<\x0bT\xd1\x7f<fp3000300\xfc\xc3&\xc9H\x84\x018\x81\x84\xe7\x14F\x16B\x8a^?\xbb\x87W\x9e\x85\x18E\xf8\x00\x13\x03\x85`\xd4\x00*\x18@1\x00\x00l\t\x11\xb4\x84N\xcd\xaf\x00\x00\x00\x00IEND\xaeB`\x82')

      self.style = ttk.Style()
      self.style.theme_settings(
         'default', {
            'TCombobox': {
               'map': {
                  'background': [
                     ('active', '#FFFFFF')
                  ],
                  'fieldbackground': [
                     ('!disabled', '#FFFFFF')
                  ]
               }
            }
         }
      )
      self.font = ('TimesNewRoman',12)

      self.titlelabel = tkinter.Label(self.root, justify='center', text='Pymin Savefile Converter', font=('TimesNewRoman',20,'bold'))
      self.titlelabel.place(x=250, y=50, width=300, height=32, anchor='n')
      self.titlelabel['background'] = '#FFFFFF'

      self.message = tkinter.Label(self.root, justify='center', text='', font=self.font, wraplength=300)
      self.message.place(x=250, y=100, width=300, height=50, anchor='n')
      self.message['foreground'] = '#FF1111'
      self.message['background'] = '#FFFFFF'

      self.inputfile = FileEntry(self.root, text='Input File', icon=self.fileicon, cls=self)
      self.inputfile.place(x=50, y=150, width=400, height=48)

      self.outputfile = FileEntry(self.root, text='Output File', icon=self.fileicon, cls=self)
      self.outputfile.place(x=50, y=210, width=400, height=48)

      self.convertbutton = ConvButton(self.root, font=self.font, text='Convert', command=self.convertButton)
      self.convertbutton.place(x=386, y=270, width=64, height=24, anchor='nw')

      self.root.mainloop()

   def convertButton(self, *args):
      self.convertSave(self.inputfile.file, self.inputfile.type, self.outputfile.file, self.outputfile.type)

   def convertSave(self, inputfile, inputtype, outputfile, outputtype):
      self.message['text'] = ''
      self.message['foreground'] = '#FF1111'
      if inputfile in {None, ''} or outputfile in {None, ''}:
         self.message['text'] = 'Error: Input/Output file can not be empty.'
         raise Exception('Input/Output file can not be empty.')
      if inputtype == outputtype and inputtype != 'detect':
         self.message['text'] = 'Error: Input and Output file types can not be the same.'
         raise Exception('Input and Output file types can not be the same.')
      if inputfile == outputfile:
         self.message['text'] = 'Error: Input and Output files can not be the same.'
         raise Exception('Input and Output files can not be the same.')
      try:
         if inputtype == '.xml':
            data = self.loadXML(inputfile)
         elif inputtype == '.sol':
            data = self.loadSOL(inputfile)
         elif inputtype == '.nim':
            data = self.loadSOL(inputfile, True)
         elif inputtype == '.toml':
            data = self.loadTOML(inputfile)
         elif inputtype == 'detect':
            infile = inputfile.lower()
            if infile.endswith('.xml'):
               data = self.loadXML(inputfile)
            elif infile.endswith('.sol'):
               data = self.loadSOL(inputfile)
            elif infile.endswith('.nim'):
               data = self.loadSOL(inputfile, True)
            elif infile.endswith('.toml'):
               data = self.loadTOML(inputfile)
            else:
               ext = inputfile.split('.')[-1].lower()
               self.message['text'] = f'Error: Detected input file type {ext} is not a supported file type.'
               raise FileTypeError(f'Detected input file type {ext} is not a supported file type.')
         if data is None:
            self.message['text'] = 'Error: Input file data is null. Try again.'
            raise NullData('Input file data is null. Try again.')
         data = self.dictSave(data)
         if outputtype == '.xml':
            self.saveXML(data, outputfile)
         elif outputtype == '.sol':
            self.saveSOL(data, outputfile)
         elif outputtype == '.nim':
            self.saveNIM(data, outputfile)
         elif outputtype == '.toml':
            self.saveTOML(data, outputfile)
         elif outputtype == 'detect':
            outfile = outputfile.lower()
            if outfile.endswith('.xml'):
               self.saveXML(data, outputfile)
            elif outfile.endswith('.sol'):
               self.saveSOL(data, outputfile)
            elif outfile.endswith('.nim'):
               self.saveNIM(data, outputfile)
            elif outfile.endswith('.toml'):
               self.saveTOML(data, outputfile)
            else:
               ext = outputfile.split('.')[-1].lower()
               self.message['text'] = f'Error: Detected output file type {ext} is not a supported file type'
               raise FileTypeError(f'Detected output file type {ext} is not a supported file type')
      except ValueError as e:
         self.message['text'] = 'Error: One or more saved values is of an unexpected type.'
         raise e
      except FileTypeError as e:
         raise e
      except NullData as e:
         raise e
      except Exception as e:
         self.message['text'] = 'Error'
         raise e
      else:
         self.message['text'] = 'Success'

   def gui_close(self):...

   @staticmethod
   def dictSave(dictionary):
      d = {'mod':('cumMod','cockSizeMod','vagSizeMod','vagElastic','changeMod','SexPMod'),'status':('pregRate',),'majorFetish':('maleFetish','femaleFetish','hermFetish','narcissistFetish','dependentFetish'),'moderateFetish':('dominantFetish','submissiveFetish','lboobFetish','sboobFetish','furryFetish','scalyFetish','smoothyFetish'),'minorFetish':('pregnancyFetish','bestialityFetish','milkFetish','sizeFetish','unbirthingFetish','ovipositionFetish','toyFetish','hyperFetish')}
      for k,v in d.items():
         for i in v:
            dictionary[k][i] = repintorfloat(dictionary[k][i])
      return dictionary

   @staticmethod
   def loadTOML(filename):
      with open(filename, 'rb') as f:
         return TOML.readFile(f)

   @staticmethod
   def loadSOL(filename, nim: bool = False):
      if nim:
         with open(filename, 'rb') as f:
            so = amf3.ByteArray(f).readObject()['data']
      else:
         so = sol.load(str(filename))
      strack = so['track']
      sstats = so['stats']
      slevel = so['level']
      smod = so['mod']
      squality = so['quality']
      scock = so['cock']
      sgirl = so['girl']
      sgear = so['gear']
      sstatus = so['status']
      saffinity = so['affinity']
      srep = so['rep']
      sknowledge = so['knowledge']
      sboss = so.get('boss',[False,False,False])
      sknowSimpleAlchemy = so.get('knowSimpleAlchemy',[False,False,False,False,False])
      sknowAdvancedAlchemy = so.get('knowAdvancedAlchemy',[False,False,False,False,False,False,False,False,False])
      sknowComplexAlchemy = so.get('knowComplexAlchemy',[False,False,False,False,False,False,False])
      smajorFetish = so['majorFetish']
      smoderateFetish = so['moderateFetish']
      sminorFetish = so['minorFetish']
      skid = so['kid']
      ver = so.get('versionNumberPymin','1')
      tempver = int(ver if ver.find('.') == -1 else ver.split('.')[-1])
      sbag = so.get('bagSave')
      sbagStack = so.get('bagStackSave')
      sstash = so.get('stashSave')
      sstashStack = so.get('stashStackSave')
      if (sbag is None):
         sbag = []
         sbagStack = []
         sstash = []
         sstashStack = []
         itemLoadFix = so['itemSave']
         stashLoadFix = so['stashSave']
         stackLoadFix = so['stackSave']
         stashStackLoadFix = so['stashStackSave']
         for i in range(1,len(itemLoadFix)):
            if (itemLoadFix[i] > 10):
               sbag.append(itemLoadFix[i])
               sbagStack.append(stackLoadFix[i])
         if len(sbag) < 27:
            l = [0 for i in range(27-len(sbag))]
            sbag.extend(l)
            sbagStack.extend(l)
         for i in range(1,len(stashLoadFix)):
            if (stashLoadFix[i] > 10):
               sstash.append(stashLoadFix[i])
               sstashStack.append(stashStackLoadFix[i])
         if len(sstash) < 27:
            l = [0 for i in range(27-len(sstash))]
            sstash.extend(l)
            sstashStack.extend(l)
      return {'track':{'currentState':strack[0],'currentZone':strack[1],'day':strack[2],'hour':strack[3],'currentDayCare':strack[4],'inDungeon':strack[5],'currentDungeon':strack[6],'v7':strack[7],'firstExplore':strack[8] if len(strack) > 8 else False},'version':{'original':so['versionNumber'],'port':ver},'stats':{'strength':sstats[0],'mentality':sstats[1],'libido':sstats[2],'sensitivity':sstats[3],'HP':sstats[4],'lust':sstats[5],'coin':sstats[6],'strMod':sstats[7],'mentMod':sstats[8],'libMod':sstats[9],'senMod':sstats[10],'hunger':sstats[11]},'level':{'SexP':slevel[0],'levelUP':slevel[1],'level':slevel[2],'babyFactLevel':slevel[3],'bodyBuildLevel':slevel[4],'hyperHappyLevel':slevel[5],'alchemistLevel':slevel[6],'fetishMasterLevel':slevel[7],'milkMaidLevel':slevel[8],'shapeshiftyLevel':slevel[9],'shapeshiftyFirst':slevel[10],'shapeshiftySecond':slevel[11]},'mod':{'runMod':smod[0],'rapeMod':smod[1],'cumMod':smod[2],'cockSizeMod':smod[3],'milkMod':smod[4],'carryMod':smod[5],'vagBellyMod':smod[6],'pregChanceMod':smod[7],'extraPregChance':smod[8],'pregTimeMod':smod[9],'enticeMod':smod[10],'milkHPMod':smod[11],'vagSizeMod':smod[12],'vagElastic':smod[13],'changeMod':smod[14],'HPMod':smod[15],'SexPMod':smod[16],'minLust':smod[17],'milkCap':smod[18],'coinMod':smod[19],'hipMod':smod[20],'buttMod':smod[21],'bellyMod':smod[22],'cockMoistMod':smod[23],'vagMoistMod':smod[24],'lockTail':smod[25],'lockFace':smod[26],'lockSkin':smod[27],'lockBreasts':smod[28],'lockEars':smod[29],'lockLegs':smod[30],'lockNipples':smod[31],'lockCock':smod[32]},'quality':{'gender':squality[0],'race':squality[1],'body':squality[2],'dominant':squality[3],'hips':squality[4],'butt':squality[5],'tallness':squality[6],'skinType':squality[7],'tail':squality[8],'ears':squality[9],'hair':squality[10],'hairColor':squality[11],'hairLength':squality[12],'legType':squality[13],'wings':squality[14],'faceType':squality[15],'skinColor':squality[16]},'cock':{'cockTotal':scock[0],'humanCocks':scock[1],'horseCocks':scock[2],'wolfCocks':scock[3],'catCocks':scock[4],'rabbitCocks':scock[5],'lizardCocks':scock[6],'cockSize':scock[7],'cockMoist':scock[8],'balls':scock[9],'ballSize':scock[10],'showBalls':scock[11],'knot':scock[12],'bugCocks':scock[13],'neuterizerHideBalls':scock[14] if len(scock) == 15 else False},'girl':{'breastSize':sgirl[0],'boobTotal':sgirl[1],'nippleSize':sgirl[2],'udders':sgirl[3],'udderSize':sgirl[4],'teatSize':sgirl[5],'clitSize':sgirl[6],'vagTotal':sgirl[7],'vagSize':sgirl[8],'vagMoist':sgirl[9],'vulvaSize':sgirl[10],'nipType':sgirl[11]},'gear':{'attireTop':sgear[0],'attireBot':sgear[1],'weapon':sgear[2]},'status':{'pregRate':sstatus[0],'pregnancyTime':sstatus[1],'pregStatus':sstatus[2],'eggLaying':sstatus[3],'eggMaxTime':sstatus[4],'eggTime':sstatus[4] if sstatus[5] > sstatus[4] and tempver < 10 else sstatus[5],'eggRate':sstatus[6],'exhaustion':sstatus[7],'exhaustionPenalty':sstatus[8],'milkEngorgement':sstatus[9],'milkEngorgementLevel':sstatus[10],'udderEngorgement':sstatus[11],'udderEngorgementLevel':sstatus[12],'heat':sstatus[13],'heatTime':sstatus[14],'heatMaxTime':sstatus[15],'lactation':sstatus[16],'udderLactation':sstatus[17],'nipplePlay':sstatus[18],'udderPlay':sstatus[19],'blueBalls':sstatus[20],'teatPump':sstatus[21],'nipPump':sstatus[22],'cockPump':sstatus[23],'clitPump':sstatus[24],'vulvaPump':sstatus[25],'masoPot':sstatus[26],'sMasoPot':sstatus[27],'babyFree':sstatus[28],'charmTime':sstatus[29],'pheromone':sstatus[30],'eggceleratorTime':sstatus[31],'eggceleratorDose':sstatus[32],'bodyOil':sstatus[33],'lustPenalty':sstatus[34],'fertileGel':sstatus[35],'snuggleBall':sstatus[36],'eggType':sstatus[37],'milkSuppressant':sstatus[38],'milkSuppressantLact':sstatus[39],'milkSuppressantUdder':sstatus[40],'suppHarness':sstatus[41],'fertilityStatueCurse':sstatus[42],'plumpQuats':sstatus[43],'lilaWetStatus':sstatus[44],'cockSnakePreg':sstatus[45],'milkCPoisonNip':sstatus[46],'milkCPoisonUdd':sstatus[47],'cockSnakeVenom':sstatus[48]},'affinity':{'humanAffinity':saffinity[0],'horseAffinity':saffinity[1],'wolfAffinity':saffinity[2],'catAffinity':saffinity[3],'cowAffinity':saffinity[4],'lizardAffinity':saffinity[5],'rabbitAffinity':saffinity[6],'fourBoobAffinity':saffinity[7],'mouseAffinity':saffinity[8],'birdAffinity':saffinity[9],'pigAffinity':saffinity[10],'twoBoobAffinity':saffinity[11],'sixBoobAffinity':saffinity[12],'eightBoobAffinity':saffinity[13],'tenBoobAffinity':saffinity[14],'cowTaurAffinity':saffinity[15],'humanTaurAffinity':saffinity[16],'skunkAffinity':saffinity[17],'bugAffinity':saffinity[18]},'rep':{'lilaRep':srep[0],'lilaVulva':srep[1],'lilaMilk':srep[2],'lilaPreg':srep[3],'malonRep':srep[4],'malonPreg':srep[5],'malonChildren':srep[6],'mistressRep':srep[7],'jamieRep':srep[8],'jamieSize':srep[9],'jamieChildren':srep[10],'silRep':srep[11],'silPreg':srep[12],'silRate':srep[13],'silLay':srep[14],'silGrowthTime':srep[15],'silTied':srep[16],'lilaUB':srep[17],'dairyFarmBrand':srep[18],'lilaWetness':srep[19],'jamieButt':srep[20],'jamieBreasts':srep[21],'jamieHair':srep[22]},'knowledge':{'foundSoftlik':sknowledge[0],'foundFirmshaft':sknowledge[1],'foundTieden':sknowledge[2],'foundSizCalit':sknowledge[3],'foundOviasis':sknowledge[4],'foundValley':sknowledge[5],'foundSanctuary':sknowledge[6],'usedSecretStairs':sknowledge[7] if len(sknowledge) == 8 else False},'boss':{'defeatedMinotaur':sboss[0],'defeatedFreakyGirl':sboss[1],'defeatedSuccubus':sboss[2]},'knowSimpleAlchemy':{'knowLustDraft':sknowSimpleAlchemy[0],'knowRejuvPot':sknowSimpleAlchemy[1],'knowExpPreg':sknowSimpleAlchemy[2],'knowBallSwell':sknowSimpleAlchemy[3],'knowMaleEnhance':sknowSimpleAlchemy[4]},'knowAdvancedAlchemy':{'knowSLustDraft':sknowAdvancedAlchemy[0],'knowSRejuvPot':sknowAdvancedAlchemy[1],'knowSExpPreg':sknowAdvancedAlchemy[2],'knowSBallSwell':sknowAdvancedAlchemy[3],'knowGenSwap':sknowAdvancedAlchemy[4],'knowMasoPot':sknowAdvancedAlchemy[5],'knowBabyFree':sknowAdvancedAlchemy[6],'knowPotPot':sknowAdvancedAlchemy[7],'knowMilkSuppress':sknowAdvancedAlchemy[8]},'knowComplexAlchemy':{'knowSGenSwap':sknowComplexAlchemy[0],'knowSMasoPot':sknowComplexAlchemy[1],'knowSBabyFree':sknowComplexAlchemy[2],'knowSPotPot':sknowComplexAlchemy[3],'knowPussJuice':sknowComplexAlchemy[4],'knowPheromone':sknowComplexAlchemy[5],'knowBazoomba':sknowComplexAlchemy[6]},'majorFetish':{'maleFetish':smajorFetish[0],'femaleFetish':smajorFetish[1],'hermFetish':smajorFetish[2],'narcissistFetish':smajorFetish[3],'dependentFetish':smajorFetish[4]},'moderateFetish':{'dominantFetish':smoderateFetish[0],'submissiveFetish':smoderateFetish[1],'lboobFetish':smoderateFetish[2],'sboobFetish':smoderateFetish[3],'furryFetish':smoderateFetish[4],'scalyFetish':smoderateFetish[5],'smoothyFetish':smoderateFetish[6]},'minorFetish':{'pregnancyFetish':sminorFetish[0],'bestialityFetish':sminorFetish[1],'milkFetish':sminorFetish[2],'sizeFetish':sminorFetish[3],'unbirthingFetish':sminorFetish[4],'ovipositionFetish':sminorFetish[5],'toyFetish':sminorFetish[6],'hyperFetish':sminorFetish[7]},'kid':{'humanChildren':skid[0],'equanChildren':skid[1],'lupanChildren':skid[2],'felinChildren':skid[3],'cowChildren':skid[4],'lizanChildren':skid[5],'lizanEggs':skid[6],'bunnionChildren':skid[7],'wolfPupChildren':skid[8],'miceChildren':skid[9],'birdEggs':skid[10],'birdChildren':skid[11],'pigChildren':skid[12],'calfChildren':skid[13],'bugEggs':skid[14],'bugChildren':skid[15],'skunkChildren':skid[16],'minotaurChildren':skid[17],'freakyGirlChildren':skid[18]},'trav':so['trav'],'bag':sbag,'bagStack':sbagStack,'stash':sstash,'stashStack':sstashStack,'preg':so['pregSave']}

   @staticmethod
   def loadXML(filename, origin: str = None):
      data = xmletree.parse(filename).getroot()
      if data is None:
         raise NullData()
      strack = data.find('track')
      sver = data.find('version')
      sver = ('0.975o','1') if sver is None else (sver.find('original').text,sver.find('port').text)
      tempver = int(sver[1] if sver[1].find('.') == -1 else sver[1].split('.')[-1])
      sstats = data.find('stats')
      slevel = data.find('level')
      smod = data.find('mod')
      squality = data.find('quality')
      scock = data.find('cock')
      sgirl = data.find('girl')
      sgear = data.find('gear')
      sstatus = data.find('status')
      saffinity = data.find('affinity')
      srep = data.find('rep')
      sknowledge = data.find('knowledge')
      sboss = data.find('boss')
      sknowSimpleAlchemy = data.find('knowSimpleAlchemy')
      sknowAdvancedAlchemy = data.find('knowAdvancedAlchemy')
      sknowComplexAlchemy = data.find('knowComplexAlchemy')
      smajorFetish = data.find('majorFetish')
      smoderateFetish = data.find('moderateFetish')
      sminorFetish = data.find('minorFetish')
      skid = data.find('kid')
      bag = data.find('bag')
      bagStack = data.find('bagStack')
      stash = data.find('stash')
      stashStack = data.find('stashStack')
      preg = data.find('preg')
      _bagArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      _bagStackArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      _stashArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      _stashStackArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      _preg = []
      for i in range(27):
         tempstr = f'slot{i}'
         _bagArray[i] = int(bag.find(tempstr).text)
         _bagStackArray[i] = int(bagStack.find(tempstr).text)
         _stashArray[i] = int(stash.find(tempstr).text)
         _stashStackArray[i] = int(stashStack.find(tempstr).text)
      for i in range(0,len(preg),5):
         _preg.extend((strtobool(preg.find(f'i{i}').text),int(preg.find(f'i{i+1}').text),int(preg.find(f'i{i+2}').text),int(preg.find(f'i{i+3}').text),int(preg.find(f'i{i+4}').text)))
      return {'track':{'currentState':int(strack.find('currentState').text),'currentZone':int(strack.find('currentZone').text),'day':int(strack.find('day').text),'hour':int(strack.find('hour').text),'currentDayCare':int(strack.find('currentDayCare').text),'inDungeon':strtobool(strack.find('inDungeon').text),'currentDungeon':int(strack.find('currentDungeon').text),'v7':str(strack.find('v7').text),'firstExplore':strtobool(strack.find('firstExplore').text) if strack.find('firstExplore') is not None else False},'version':{'original':sver[0],'port':sver[1]},'stats':{'strength':int(sstats.find('strength').text),'mentality':int(sstats.find('mentality').text),'libido':int(sstats.find('libido').text),'sensitivity':int(sstats.find('sensitivity').text),'HP':int(sstats.find('HP').text),'lust':int(sstats.find('lust').text),'coin':int(sstats.find('coin').text),'strMod':int(sstats.find('strMod').text),'mentMod':int(sstats.find('mentMod').text),'libMod':int(sstats.find('libMod').text),'senMod':int(sstats.find('senMod').text),'hunger':int(sstats.find('hunger').text)},'level':{'SexP':int(slevel.find('SexP').text),'levelUP':int(slevel.find('levelUP').text),'level':int(slevel.find('level').text),'babyFactLevel':int(slevel.find('babyFactLevel').text),'bodyBuildLevel':int(slevel.find('bodyBuildLevel').text),'hyperHappyLevel':int(slevel.find('hyperHappyLevel').text),'alchemistLevel':int(slevel.find('alchemistLevel').text),'fetishMasterLevel':int(slevel.find('fetishMasterLevel').text),'milkMaidLevel':int(slevel.find('milkMaidLevel').text),'shapeshiftyLevel':int(slevel.find('shapeshiftyLevel').text),'shapeshiftyFirst':'' if slevel.find('shapeshiftyFirst').text is None else str(slevel.find('shapeshiftyFirst').text),'shapeshiftySecond':'' if slevel.find('shapeshiftySecond').text is None else str(slevel.find('shapeshiftySecond').text)},'mod':{'runMod':int(smod.find('runMod').text),'rapeMod':int(smod.find('rapeMod').text),'cumMod':float(smod.find('cumMod').text),'cockSizeMod':float(smod.find('cockSizeMod').text),'milkMod':int(smod.find('milkMod').text),'carryMod':int(smod.find('carryMod').text),'vagBellyMod':int(smod.find('vagBellyMod').text),'pregChanceMod':int(smod.find('pregChanceMod').text),'extraPregChance':int(smod.find('extraPregChance').text),'pregTimeMod':int(smod.find('pregTimeMod').text),'enticeMod':int(smod.find('enticeMod').text),'milkHPMod':int(smod.find('milkHPMod').text),'vagSizeMod':float(smod.find('vagSizeMod').text),'vagElastic':float(smod.find('vagElastic').text),'changeMod':float(smod.find('changeMod').text),'HPMod':int(smod.find('HPMod').text),'SexPMod':float(smod.find('SexPMod').text),'minLust':int(smod.find('minLust').text),'milkCap':int(smod.find('milkCap').text),'coinMod':int(smod.find('coinMod').text),'hipMod':float(smod.find('hipMod').text),'buttMod':float(smod.find('buttMod').text),'bellyMod':int(smod.find('bellyMod').text),'cockMoistMod':int(smod.find('cockMoistMod').text),'vagMoistMod':int(smod.find('vagMoistMod').text),'lockTail':int(smod.find('lockTail').text),'lockFace':int(smod.find('lockFace').text),'lockSkin':int(smod.find('lockSkin').text),'lockBreasts':int(smod.find('lockBreasts').text),'lockEars':int(smod.find('lockEars').text),'lockLegs':int(smod.find('lockLegs').text),'lockNipples':int(smod.find('lockNipples').text),'lockCock':int(smod.find('lockCock').text)},'quality':{'gender':int(squality.find('gender').text),'race':int(squality.find('race').text),'body':int(squality.find('body').text),'dominant':int(squality.find('dominant').text),'hips':int(squality.find('hips').text),'butt':int(squality.find('butt').text),'tallness':int(squality.find('tallness').text),'skinType':int(squality.find('skinType').text),'tail':int(squality.find('tail').text),'ears':int(squality.find('ears').text),'hair':int(squality.find('hair').text),'hairColor':int(squality.find('hairColor').text),'hairLength':int(squality.find('hairLength').text),'legType':int(squality.find('legType').text),'wings':int(squality.find('wings').text),'faceType':int(squality.find('faceType').text),'skinColor':int(squality.find('skinColor').text)},'cock':{'cockTotal':int(scock.find('cockTotal').text),'humanCocks':int(scock.find('humanCocks').text),'horseCocks':int(scock.find('horseCocks').text),'wolfCocks':int(scock.find('wolfCocks').text),'catCocks':int(scock.find('catCocks').text),'rabbitCocks':int(scock.find('rabbitCocks').text),'lizardCocks':int(scock.find('lizardCocks').text),'cockSize':int(scock.find('cockSize').text),'cockMoist':int(scock.find('cockMoist').text),'balls':int(scock.find('balls').text),'ballSize':int(scock.find('ballSize').text),'showBalls':strtobool(scock.find('showBalls').text),'knot':strtobool(scock.find('knot').text),'bugCocks':int(scock.find('bugCocks').text),'neuterizerHideBalls':strtobool(scock.find('neuterizerHideBalls').text) if scock.find('nueterizerHideBalls') is not None else False},'girl':{'breastSize':int(sgirl.find('breastSize').text),'boobTotal':int(sgirl.find('boobTotal').text),'nippleSize':int(sgirl.find('nippleSize').text),'udders':strtobool(sgirl.find('udders').text),'udderSize':int(sgirl.find('udderSize').text),'teatSize':int(sgirl.find('teatSize').text),'clitSize':int(sgirl.find('clitSize').text),'vagTotal':int(sgirl.find('vagTotal').text),'vagSize':int(sgirl.find('vagSize').text),'vagMoist':int(sgirl.find('vagMoist').text),'vulvaSize':int(sgirl.find('vulvaSize').text),'nipType':int(sgirl.find('nipType').text)},'gear':{'attireTop':int(sgear.find('attireTop').text),'attireBot':int(sgear.find('attireBot').text),'weapon':int(sgear.find('weapon').text)},'status':{'pregRate':float(sstatus.find('pregRate').text),'pregnancyTime':int(sstatus.find('pregnancyTime').text),'pregStatus':int(sstatus.find('pregStatus').text),'eggLaying':int(sstatus.find('eggLaying').text),'eggMaxTime':int(sstatus.find('eggMaxTime').text),'eggTime':int(sstatus.find('eggMaxTime').text) if int(sstatus.find('eggTime').text) > int(sstatus.find('eggMaxTime').text) and tempver < 10 else int(sstatus.find('eggTime').text),'eggRate':int(sstatus.find('eggRate').text),'exhaustion':int(sstatus.find('exhaustion').text),'exhaustionPenalty':int(sstatus.find('exhaustionPenalty').text),'milkEngorgement':int(sstatus.find('milkEngorgement').text),'milkEngorgementLevel':int(sstatus.find('milkEngorgementLevel').text),'udderEngorgement':int(sstatus.find('udderEngorgement').text),'udderEngorgementLevel':int(sstatus.find('udderEngorgementLevel').text),'heat':int(sstatus.find('heat').text),'heatTime':int(sstatus.find('heatTime').text),'heatMaxTime':int(sstatus.find('heatMaxTime').text),'lactation':int(sstatus.find('lactation').text),'udderLactation':int(sstatus.find('udderLactation').text),'nipplePlay':float(sstatus.find('nipplePlay').text),'udderPlay':float(sstatus.find('udderPlay').text),'blueBalls':int(sstatus.find('blueBalls').text),'teatPump':int(sstatus.find('teatPump').text),'nipPump':int(sstatus.find('nipPump').text),'cockPump':int(sstatus.find('cockPump').text),'clitPump':int(sstatus.find('clitPump').text),'vulvaPump':int(sstatus.find('vulvaPump').text),'masoPot':int(sstatus.find('masoPot').text),'sMasoPot':int(sstatus.find('sMasoPot').text),'babyFree':int(sstatus.find('babyFree').text),'charmTime':int(sstatus.find('charmTime').text),'pheromone':int(sstatus.find('pheromone').text),'eggceleratorTime':int(sstatus.find('eggceleratorTime').text),'eggceleratorDose':int(sstatus.find('eggceleratorDose').text),'bodyOil':int(sstatus.find('bodyOil').text),'lustPenalty':int(sstatus.find('lustPenalty').text),'fertileGel':int(sstatus.find('fertileGel').text),'snuggleBall':strtobool(sstatus.find('snuggleBall').text),'eggType':int(sstatus.find('eggType').text),'milkSuppressant':int(sstatus.find('milkSuppressant').text),'milkSuppressantLact':int(sstatus.find('milkSuppressantLact').text),'milkSuppressantUdder':int(sstatus.find('milkSuppressantUdder').text),'suppHarness':strtobool(sstatus.find('suppHarness').text),'fertilityStatueCurse':int(sstatus.find('fertilityStatueCurse').text),'plumpQuats':int(sstatus.find('plumpQuats').text),'lilaWetStatus':int(sstatus.find('lilaWetStatus').text),'cockSnakePreg':int(sstatus.find('cockSnakePreg').text),'milkCPoisonNip':int(sstatus.find('milkCPoisonNip').text),'milkCPoisonUdd':int(sstatus.find('milkCPoisonUdd').text),'cockSnakeVenom':int(sstatus.find('cockSnakeVenom').text)},'affinity':{'humanAffinity':int(saffinity.find('humanAffinity').text),'horseAffinity':int(saffinity.find('horseAffinity').text),'wolfAffinity':int(saffinity.find('wolfAffinity').text),'catAffinity':int(saffinity.find('catAffinity').text),'cowAffinity':int(saffinity.find('cowAffinity').text),'lizardAffinity':int(saffinity.find('lizardAffinity').text),'rabbitAffinity':int(saffinity.find('rabbitAffinity').text),'fourBoobAffinity':int(saffinity.find('fourBoobAffinity').text),'mouseAffinity':int(saffinity.find('mouseAffinity').text),'birdAffinity':int(saffinity.find('birdAffinity').text),'pigAffinity':int(saffinity.find('pigAffinity').text),'twoBoobAffinity':int(saffinity.find('twoBoobAffinity').text),'sixBoobAffinity':int(saffinity.find('sixBoobAffinity').text),'eightBoobAffinity':int(saffinity.find('eightBoobAffinity').text),'tenBoobAffinity':int(saffinity.find('tenBoobAffinity').text),'cowTaurAffinity':int(saffinity.find('cowTaurAffinity').text),'humanTaurAffinity':int(saffinity.find('humanTaurAffinity').text),'skunkAffinity':int(saffinity.find('skunkAffinity').text),'bugAffinity':int(saffinity.find('bugAffinity').text)},'rep':{'lilaRep':int(srep.find('lilaRep').text),'lilaVulva':int(srep.find('lilaVulva').text),'lilaMilk':int(srep.find('lilaMilk').text),'lilaPreg':int(srep.find('lilaPreg').text),'malonRep':int(srep.find('malonRep').text),'malonPreg':int(srep.find('malonPreg').text),'malonChildren':int(srep.find('malonChildren').text),'mistressRep':int(srep.find('mistressRep').text),'jamieRep':int(srep.find('jamieRep').text),'jamieSize':int(srep.find('jamieSize').text),'jamieChildren':int(srep.find('jamieChildren').text),'silRep':int(srep.find('silRep').text),'silPreg':int(srep.find('silPreg').text),'silRate':int(srep.find('silRate').text),'silLay':int(srep.find('silLay').text),'silGrowthTime':int(srep.find('silGrowthTime').text),'silTied':strtobool(srep.find('silTied').text),'lilaUB':strtobool(srep.find('lilaUB').text),'dairyFarmBrand':strtobool(srep.find('dairyFarmBrand').text),'lilaWetness':int(srep.find('lilaWetness').text),'jamieButt':strtobool(srep.find('jamieButt').text),'jamieBreasts':strtobool(srep.find('jamieBreasts').text),'jamieHair':strtobool(srep.find('jamieHair').text)},'knowledge':{'foundSoftlik':strtobool(sknowledge.find('foundSoftlik').text),'foundFirmshaft':strtobool(sknowledge.find('foundFirmshaft').text),'foundTieden':strtobool(sknowledge.find('foundTieden').text),'foundSizCalit':strtobool(sknowledge.find('foundSizCalit').text),'foundOviasis':strtobool(sknowledge.find('foundOviasis').text),'foundValley':strtobool(sknowledge.find('foundValley').text),'foundSanctuary':strtobool(sknowledge.find('foundSanctuary').text),'usedSecretStairs':strtobool(sknowledge.find('usedSecretStairs').text) if sknowledge.find('usedSecretStairs') is not None else False},'boss':{'defeatedMinotaur':strtobool(sboss.find('defeatedMinotaur').text),'defeatedFreakyGirl':strtobool(sboss.find('defeatedFreakyGirl').text),'defeatedSuccubus':strtobool(sboss.find('defeatedSuccubus').text)},'knowSimpleAlchemy':{'knowLustDraft':strtobool(sknowSimpleAlchemy.find('knowLustDraft').text),'knowRejuvPot':strtobool(sknowSimpleAlchemy.find('knowRejuvPot').text),'knowExpPreg':strtobool(sknowSimpleAlchemy.find('knowExpPreg').text),'knowBallSwell':strtobool(sknowSimpleAlchemy.find('knowBallSwell').text),'knowMaleEnhance':strtobool(sknowSimpleAlchemy.find('knowMaleEnhance').text)},'knowAdvancedAlchemy':{'knowSLustDraft':strtobool(sknowAdvancedAlchemy.find('knowSLustDraft').text),'knowSRejuvPot':strtobool(sknowAdvancedAlchemy.find('knowSRejuvPot').text),'knowSExpPreg':strtobool(sknowAdvancedAlchemy.find('knowSExpPreg').text),'knowSBallSwell':strtobool(sknowAdvancedAlchemy.find('knowSBallSwell').text),'knowGenSwap':strtobool(sknowAdvancedAlchemy.find('knowGenSwap').text),'knowMasoPot':strtobool(sknowAdvancedAlchemy.find('knowMasoPot').text),'knowBabyFree':strtobool(sknowAdvancedAlchemy.find('knowBabyFree').text),'knowPotPot':strtobool(sknowAdvancedAlchemy.find('knowPotPot').text),'knowMilkSuppress':strtobool(sknowAdvancedAlchemy.find('knowMilkSuppress').text)},'knowComplexAlchemy':{'knowSGenSwap':strtobool(sknowComplexAlchemy.find('knowSGenSwap').text),'knowSMasoPot':strtobool(sknowComplexAlchemy.find('knowSMasoPot').text),'knowSBabyFree':strtobool(sknowComplexAlchemy.find('knowSBabyFree').text),'knowSPotPot':strtobool(sknowComplexAlchemy.find('knowSPotPot').text),'knowPussJuice':strtobool(sknowComplexAlchemy.find('knowPussJuice').text),'knowPheromone':strtobool(sknowComplexAlchemy.find('knowPheromone').text),'knowBazoomba':strtobool(sknowComplexAlchemy.find('knowBazoomba').text)},'majorFetish':{'maleFetish':float(smajorFetish.find('maleFetish').text),'femaleFetish':float(smajorFetish.find('femaleFetish').text),'hermFetish':float(smajorFetish.find('hermFetish').text),'narcissistFetish':float(smajorFetish.find('narcissistFetish').text),'dependentFetish':float(smajorFetish.find('dependentFetish').text)},'moderateFetish':{'dominantFetish':float(smoderateFetish.find('dominantFetish').text),'submissiveFetish':float(smoderateFetish.find('submissiveFetish').text),'lboobFetish':float(smoderateFetish.find('lboobFetish').text),'sboobFetish':float(smoderateFetish.find('sboobFetish').text),'furryFetish':float(smoderateFetish.find('furryFetish').text),'scalyFetish':float(smoderateFetish.find('scalyFetish').text),'smoothyFetish':float(smoderateFetish.find('smoothyFetish').text)},'minorFetish':{'pregnancyFetish':float(sminorFetish.find('pregnancyFetish').text),'bestialityFetish':float(sminorFetish.find('bestialityFetish').text),'milkFetish':float(sminorFetish.find('milkFetish').text),'sizeFetish':float(sminorFetish.find('sizeFetish').text),'unbirthingFetish':float(sminorFetish.find('unbirthingFetish').text),'ovipositionFetish':float(sminorFetish.find('ovipositionFetish').text),'toyFetish':float(sminorFetish.find('toyFetish').text),'hyperFetish':float(sminorFetish.find('hyperFetish').text)},'kid':{'humanChildren':int(skid.find('humanChildren').text),'equanChildren':int(skid.find('equanChildren').text),'lupanChildren':int(skid.find('lupanChildren').text),'felinChildren':int(skid.find('felinChildren').text),'cowChildren':int(skid.find('cowChildren').text),'lizanChildren':int(skid.find('lizanChildren').text),'lizanEggs':int(skid.find('lizanEggs').text),'bunnionChildren':int(skid.find('bunnionChildren').text),'wolfPupChildren':int(skid.find('wolfPupChildren').text),'miceChildren':int(skid.find('miceChildren').text),'birdEggs':int(skid.find('birdEggs').text),'birdChildren':int(skid.find('birdChildren').text),'pigChildren':int(skid.find('pigChildren').text),'calfChildren':int(skid.find('calfChildren').text),'bugEggs':int(skid.find('bugEggs').text),'bugChildren':int(skid.find('bugChildren').text),'skunkChildren':int(skid.find('skunkChildren').text),'minotaurChildren':int(skid.find('minotaurChildren').text),'freakyGirlChildren':int(skid.find('freakyGirlChildren').text)},'trav':[],'bag':_bagArray,'bagStack':_bagStackArray,'stash':_stashArray,'stashStack':_stashStackArray,'preg':_preg}

   @staticmethod
   def saveTOML(dictionary:dict, outputfile):
      TOML.write(outputfile, dictionary)

   @staticmethod
   def solGetFileName(path:str|Path):
      if path is None:
         return ''
      if isinstance(path,str):
         if platform == 'Windows':
            filename = path.split('\\')[-1].split('.')
         elif platform in {'Linux','Darwin'}:
            filename = path.split('/')[-1].split('.')
      else: #Is path object
         filename = path.resolve().name.split('.')
      if len(filename) == 1:
         return filename[0]
      if len(filename) > 1:
         return '.'.join(filename[:-1])

   def returnSOL(self, dictionary:dict, outputfile):
      try:
         data = sol.SOL(self.solGetFileName(outputfile))
         data['track'] = list(dictionary['track'].values())
         data['versionNumber'] = dictionary['version']['original']
         data['versionNumberPymin'] = dictionary['version']['port']
         data['stats'] = list(dictionary['stats'].values())
         data['level'] = list(dictionary['level'].values())
         data['mod'] = list(dictionary['mod'].values())
         data['quality'] = list(dictionary['quality'].values())
         data['cock'] = list(dictionary['cock'].values())
         if dictionary['cock'].get('neuterizerHideBalls') is not None:
            data['cock'].append(dictionary['cock'].get('neuterizerHideBalls'))
         data['girl'] = list(dictionary['girl'].values())
         data['gear'] = list(dictionary['gear'].values())
         data['status'] = list(dictionary['status'].values())
         data['affinity'] = list(dictionary['affinity'].values())
         data['rep'] = list(dictionary['rep'].values())
         data['knowledge'] = list(dictionary['knowledge'].values())
         data['boss'] = list(dictionary['boss'].values())
         data['knowSimpleAlchemy'] = list(dictionary['knowSimpleAlchemy'].values())
         data['knowAdvancedAlchemy'] = list(dictionary['knowAdvancedAlchemy'].values())
         data['knowComplexAlchemy'] = list(dictionary['knowComplexAlchemy'].values())
         data['majorFetish'] = list(dictionary['majorFetish'].values())
         data['moderateFetish'] = list(dictionary['moderateFetish'].values())
         data['minorFetish'] = list(dictionary['minorFetish'].values())
         data['kid'] = list(dictionary['kid'].values())
         data['trav'] = []
         data['bagSave'] = dictionary['bag']
         data['bagStackSave'] = dictionary['bagStack']
         data['stashSave'] = dictionary['stash']
         data['stashStackSave'] = dictionary['stashStack']
         data['pregSave'] = dictionary['preg']
         return data
      except Exception as e:
         raise NullData('returnSOL; Failed to convert data') from e

   def saveNIM(self, dictionary:dict, outputfile):
      so = {'data': self.returnSOL(dictionary, outputfile)}
      byteData = amf3.ByteArray()
      byteData.writeObject(so)
      with open(outputfile, 'wb') as f:
         f.write(byteData.getvalue())

   def saveSOL(self, dictionary:dict, outputfile):
      sol.save(self.returnSOL(dictionary, outputfile), str(outputfile), 3)

   @staticmethod
   def saveXML(dictionary:dict, outputfile):
      strack = list(dictionary['track'].values())
      sver = list(dictionary['version'].values())
      sstats = list(dictionary['stats'].values())
      slevel = list(dictionary['level'].values())
      smod = list(dictionary['mod'].values())
      squality = list(dictionary['quality'].values())
      scock = list(dictionary['cock'].values())
      sgirl = list(dictionary['girl'].values())
      sgear = list(dictionary['gear'].values())
      sstatus = list(dictionary['status'].values())
      saffinity = list(dictionary['affinity'].values())
      srep = list(dictionary['rep'].values())
      sknowledge = list(dictionary['knowledge'].values())
      sboss = list(dictionary['boss'].values())
      sknowSimpleAlchemy = list(dictionary['knowSimpleAlchemy'].values())
      sknowAdvancedAlchemy = list(dictionary['knowAdvancedAlchemy'].values())
      sknowComplexAlchemy = list(dictionary['knowComplexAlchemy'].values())
      smajorFetish = list(dictionary['majorFetish'].values())
      smoderateFetish = list(dictionary['moderateFetish'].values())
      sminorFetish = list(dictionary['minorFetish'].values())
      skid = list(dictionary['kid'].values())
      trav = dictionary['trav']
      _bagArray = dictionary['bag']
      _bagStackArray = dictionary['bagStack']
      _stashArray = dictionary['stash']
      _stashStackArray = dictionary['stashStack']
      _pregArray = dictionary['preg']
      with StringIO() as text:
         text.write(f'<data><track><currentState>{strack[0]}</currentState><currentZone>{strack[1]}</currentZone><day>{strack[2]}</day><hour>{strack[3]}</hour><currentDayCare>{strack[4]}</currentDayCare><inDungeon>{strack[5]}</inDungeon><currentDungeon>{strack[6]}</currentDungeon><v7>{strack[7]}</v7><firstExplore>{strack[8]}</firstExplore></track><version><original>{sver[0]}</original><port>{sver[1]}</port></version><stats><strength>{sstats[0]}</strength><mentality>{sstats[1]}</mentality><libido>{sstats[2]}</libido><sensitivity>{sstats[3]}</sensitivity><HP>{sstats[4]}</HP><lust>{sstats[5]}</lust><coin>{sstats[6]}</coin><strMod>{sstats[7]}</strMod><mentMod>{sstats[8]}</mentMod><libMod>{sstats[9]}</libMod><senMod>{sstats[10]}</senMod><hunger>{sstats[11]}</hunger></stats><level><SexP>{slevel[0]}</SexP><levelUP>{slevel[1]}</levelUP><level>{slevel[2]}</level><babyFactLevel>{slevel[3]}</babyFactLevel><bodyBuildLevel>{slevel[4]}</bodyBuildLevel><hyperHappyLevel>{slevel[5]}</hyperHappyLevel><alchemistLevel>{slevel[6]}</alchemistLevel><fetishMasterLevel>{slevel[7]}</fetishMasterLevel><milkMaidLevel>{slevel[8]}</milkMaidLevel><shapeshiftyLevel>{slevel[9]}</shapeshiftyLevel><shapeshiftyFirst>{slevel[10]}</shapeshiftyFirst><shapeshiftySecond>{slevel[11]}</shapeshiftySecond></level><mod><runMod>{smod[0]}</runMod><rapeMod>{smod[1]}</rapeMod><cumMod>{smod[2]}</cumMod><cockSizeMod>{smod[3]}</cockSizeMod><milkMod>{smod[4]}</milkMod><carryMod>{smod[5]}</carryMod><vagBellyMod>{smod[6]}</vagBellyMod><pregChanceMod>{smod[7]}</pregChanceMod><extraPregChance>{smod[8]}</extraPregChance><pregTimeMod>{smod[9]}</pregTimeMod><enticeMod>{smod[10]}</enticeMod><milkHPMod>{smod[11]}</milkHPMod><vagSizeMod>{smod[12]}</vagSizeMod><vagElastic>{smod[13]}</vagElastic><changeMod>{smod[14]}</changeMod><HPMod>{smod[15]}</HPMod><SexPMod>{smod[16]}</SexPMod><minLust>{smod[17]}</minLust><milkCap>{smod[18]}</milkCap><coinMod>{smod[19]}</coinMod><hipMod>{smod[20]}</hipMod><buttMod>{smod[21]}</buttMod><bellyMod>{smod[22]}</bellyMod><cockMoistMod>{smod[23]}</cockMoistMod><vagMoistMod>{smod[24]}</vagMoistMod><lockTail>{smod[25]}</lockTail><lockFace>{smod[26]}</lockFace><lockSkin>{smod[27]}</lockSkin><lockBreasts>{smod[28]}</lockBreasts><lockEars>{smod[29]}</lockEars><lockLegs>{smod[30]}</lockLegs><lockNipples>{smod[31]}</lockNipples><lockCock>{smod[32]}</lockCock></mod><quality><gender>{squality[0]}</gender><race>{squality[1]}</race><body>{squality[2]}</body><dominant>{squality[3]}</dominant><hips>{squality[4]}</hips><butt>{squality[5]}</butt><tallness>{squality[6]}</tallness><skinType>{squality[7]}</skinType><tail>{squality[8]}</tail><ears>{squality[9]}</ears><hair>{squality[10]}</hair><hairColor>{squality[11]}</hairColor><hairLength>{squality[12]}</hairLength><legType>{squality[13]}</legType><wings>{squality[14]}</wings><faceType>{squality[15]}</faceType><skinColor>{squality[16]}</skinColor></quality><cock><cockTotal>{scock[0]}</cockTotal><humanCocks>{scock[1]}</humanCocks><horseCocks>{scock[2]}</horseCocks><wolfCocks>{scock[3]}</wolfCocks><catCocks>{scock[4]}</catCocks><rabbitCocks>{scock[5]}</rabbitCocks><lizardCocks>{scock[6]}</lizardCocks><cockSize>{scock[7]}</cockSize><cockMoist>{scock[8]}</cockMoist><balls>{scock[9]}</balls><ballSize>{scock[10]}</ballSize><showBalls>{scock[11]}</showBalls><knot>{scock[12]}</knot><bugCocks>{scock[13]}</bugCocks>')
         if len(scock) == 15:
            text.write(f'<neuterizerHideBalls>{scock[14]}</neuterizerHideBalls>')
         text.write(f'</cock><girl><breastSize>{sgirl[0]}</breastSize><boobTotal>{sgirl[1]}</boobTotal><nippleSize>{sgirl[2]}</nippleSize><udders>{sgirl[3]}</udders><udderSize>{sgirl[4]}</udderSize><teatSize>{sgirl[5]}</teatSize><clitSize>{sgirl[6]}</clitSize><vagTotal>{sgirl[7]}</vagTotal><vagSize>{sgirl[8]}</vagSize><vagMoist>{sgirl[9]}</vagMoist><vulvaSize>{sgirl[10]}</vulvaSize><nipType>{sgirl[11]}</nipType></girl><gear><attireTop>{sgear[0]}</attireTop><attireBot>{sgear[1]}</attireBot><weapon>{sgear[2]}</weapon></gear><status><pregRate>{sstatus[0]}</pregRate><pregnancyTime>{sstatus[1]}</pregnancyTime><pregStatus>{sstatus[2]}</pregStatus><eggLaying>{sstatus[3]}</eggLaying><eggMaxTime>{sstatus[4]}</eggMaxTime><eggTime>{sstatus[5]}</eggTime><eggRate>{sstatus[6]}</eggRate><exhaustion>{sstatus[7]}</exhaustion><exhaustionPenalty>{sstatus[8]}</exhaustionPenalty><milkEngorgement>{sstatus[9]}</milkEngorgement><milkEngorgementLevel>{sstatus[10]}</milkEngorgementLevel><udderEngorgement>{sstatus[11]}</udderEngorgement><udderEngorgementLevel>{sstatus[12]}</udderEngorgementLevel><heat>{sstatus[13]}</heat><heatTime>{sstatus[14]}</heatTime><heatMaxTime>{sstatus[15]}</heatMaxTime><lactation>{sstatus[16]}</lactation><udderLactation>{sstatus[17]}</udderLactation><nipplePlay>{sstatus[18]}</nipplePlay><udderPlay>{sstatus[19]}</udderPlay><blueBalls>{sstatus[20]}</blueBalls><teatPump>{sstatus[21]}</teatPump><nipPump>{sstatus[22]}</nipPump><cockPump>{sstatus[23]}</cockPump><clitPump>{sstatus[24]}</clitPump><vulvaPump>{sstatus[25]}</vulvaPump><masoPot>{sstatus[26]}</masoPot><sMasoPot>{sstatus[27]}</sMasoPot><babyFree>{sstatus[28]}</babyFree><charmTime>{sstatus[29]}</charmTime><pheromone>{sstatus[30]}</pheromone><eggceleratorTime>{sstatus[31]}</eggceleratorTime><eggceleratorDose>{sstatus[32]}</eggceleratorDose><bodyOil>{sstatus[33]}</bodyOil><lustPenalty>{sstatus[34]}</lustPenalty><fertileGel>{sstatus[35]}</fertileGel><snuggleBall>{sstatus[36]}</snuggleBall><eggType>{sstatus[37]}</eggType><milkSuppressant>{sstatus[38]}</milkSuppressant><milkSuppressantLact>{sstatus[39]}</milkSuppressantLact><milkSuppressantUdder>{sstatus[40]}</milkSuppressantUdder><suppHarness>{sstatus[41]}</suppHarness><fertilityStatueCurse>{sstatus[42]}</fertilityStatueCurse><plumpQuats>{sstatus[43]}</plumpQuats><lilaWetStatus>{sstatus[44]}</lilaWetStatus><cockSnakePreg>{sstatus[45]}</cockSnakePreg><milkCPoisonNip>{sstatus[46]}</milkCPoisonNip><milkCPoisonUdd>{sstatus[47]}</milkCPoisonUdd><cockSnakeVenom>{sstatus[48]}</cockSnakeVenom></status><affinity><humanAffinity>{saffinity[0]}</humanAffinity><horseAffinity>{saffinity[1]}</horseAffinity><wolfAffinity>{saffinity[2]}</wolfAffinity><catAffinity>{saffinity[3]}</catAffinity><cowAffinity>{saffinity[4]}</cowAffinity><lizardAffinity>{saffinity[5]}</lizardAffinity><rabbitAffinity>{saffinity[6]}</rabbitAffinity><fourBoobAffinity>{saffinity[7]}</fourBoobAffinity><mouseAffinity>{saffinity[8]}</mouseAffinity><birdAffinity>{saffinity[9]}</birdAffinity><pigAffinity>{saffinity[10]}</pigAffinity><twoBoobAffinity>{saffinity[11]}</twoBoobAffinity><sixBoobAffinity>{saffinity[12]}</sixBoobAffinity><eightBoobAffinity>{saffinity[13]}</eightBoobAffinity><tenBoobAffinity>{saffinity[14]}</tenBoobAffinity><cowTaurAffinity>{saffinity[15]}</cowTaurAffinity><humanTaurAffinity>{saffinity[16]}</humanTaurAffinity><skunkAffinity>{saffinity[17]}</skunkAffinity><bugAffinity>{saffinity[18]}</bugAffinity></affinity><rep><lilaRep>{srep[0]}</lilaRep><lilaVulva>{srep[1]}</lilaVulva><lilaMilk>{srep[2]}</lilaMilk><lilaPreg>{srep[3]}</lilaPreg><malonRep>{srep[4]}</malonRep><malonPreg>{srep[5]}</malonPreg><malonChildren>{srep[6]}</malonChildren><mistressRep>{srep[7]}</mistressRep><jamieRep>{srep[8]}</jamieRep><jamieSize>{srep[9]}</jamieSize><jamieChildren>{srep[10]}</jamieChildren><silRep>{srep[11]}</silRep><silPreg>{srep[12]}</silPreg><silRate>{srep[13]}</silRate><silLay>{srep[14]}</silLay><silGrowthTime>{srep[15]}</silGrowthTime><silTied>{srep[16]}</silTied><lilaUB>{srep[17]}</lilaUB><dairyFarmBrand>{srep[18]}</dairyFarmBrand><lilaWetness>{srep[19]}</lilaWetness><jamieButt>{srep[20]}</jamieButt><jamieBreasts>{srep[21]}</jamieBreasts><jamieHair>{srep[22]}</jamieHair></rep><knowledge><foundSoftlik>{sknowledge[0]}</foundSoftlik><foundFirmshaft>{sknowledge[1]}</foundFirmshaft><foundTieden>{sknowledge[2]}</foundTieden><foundSizCalit>{sknowledge[3]}</foundSizCalit><foundOviasis>{sknowledge[4]}</foundOviasis><foundValley>{sknowledge[5]}</foundValley><foundSanctuary>{sknowledge[6]}</foundSanctuary></knowledge><boss><defeatedMinotaur>{sboss[0]}</defeatedMinotaur><defeatedFreakyGirl>{sboss[1]}</defeatedFreakyGirl><defeatedSuccubus>{sboss[2]}</defeatedSuccubus></boss><knowSimpleAlchemy><knowLustDraft>{sknowSimpleAlchemy[0]}</knowLustDraft><knowRejuvPot>{sknowSimpleAlchemy[1]}</knowRejuvPot><knowExpPreg>{sknowSimpleAlchemy[2]}</knowExpPreg><knowBallSwell>{sknowSimpleAlchemy[3]}</knowBallSwell><knowMaleEnhance>{sknowSimpleAlchemy[4]}</knowMaleEnhance></knowSimpleAlchemy><knowAdvancedAlchemy><knowSLustDraft>{sknowAdvancedAlchemy[0]}</knowSLustDraft><knowSRejuvPot>{sknowAdvancedAlchemy[1]}</knowSRejuvPot><knowSExpPreg>{sknowAdvancedAlchemy[2]}</knowSExpPreg><knowSBallSwell>{sknowAdvancedAlchemy[3]}</knowSBallSwell><knowGenSwap>{sknowAdvancedAlchemy[4]}</knowGenSwap><knowMasoPot>{sknowAdvancedAlchemy[5]}</knowMasoPot><knowBabyFree>{sknowAdvancedAlchemy[6]}</knowBabyFree><knowPotPot>{sknowAdvancedAlchemy[7]}</knowPotPot><knowMilkSuppress>{sknowAdvancedAlchemy[8]}</knowMilkSuppress></knowAdvancedAlchemy><knowComplexAlchemy><knowSGenSwap>{sknowComplexAlchemy[0]}</knowSGenSwap><knowSMasoPot>{sknowComplexAlchemy[1]}</knowSMasoPot><knowSBabyFree>{sknowComplexAlchemy[2]}</knowSBabyFree><knowSPotPot>{sknowComplexAlchemy[3]}</knowSPotPot><knowPussJuice>{sknowComplexAlchemy[4]}</knowPussJuice><knowPheromone>{sknowComplexAlchemy[5]}</knowPheromone><knowBazoomba>{sknowComplexAlchemy[6]}</knowBazoomba></knowComplexAlchemy><majorFetish><maleFetish>{smajorFetish[0]}</maleFetish><femaleFetish>{smajorFetish[1]}</femaleFetish><hermFetish>{smajorFetish[2]}</hermFetish><narcissistFetish>{smajorFetish[3]}</narcissistFetish><dependentFetish>{smajorFetish[4]}</dependentFetish></majorFetish><moderateFetish><dominantFetish>{smoderateFetish[0]}</dominantFetish><submissiveFetish>{smoderateFetish[1]}</submissiveFetish><lboobFetish>{smoderateFetish[2]}</lboobFetish><sboobFetish>{smoderateFetish[3]}</sboobFetish><furryFetish>{smoderateFetish[4]}</furryFetish><scalyFetish>{smoderateFetish[5]}</scalyFetish><smoothyFetish>{smoderateFetish[6]}</smoothyFetish></moderateFetish><minorFetish><pregnancyFetish>{sminorFetish[0]}</pregnancyFetish><bestialityFetish>{sminorFetish[1]}</bestialityFetish><milkFetish>{sminorFetish[2]}</milkFetish><sizeFetish>{sminorFetish[3]}</sizeFetish><unbirthingFetish>{sminorFetish[4]}</unbirthingFetish><ovipositionFetish>{sminorFetish[5]}</ovipositionFetish><toyFetish>{sminorFetish[6]}</toyFetish><hyperFetish>{sminorFetish[7]}</hyperFetish></minorFetish><kid><humanChildren>{skid[0]}</humanChildren><equanChildren>{skid[1]}</equanChildren><lupanChildren>{skid[2]}</lupanChildren><felinChildren>{skid[3]}</felinChildren><cowChildren>{skid[4]}</cowChildren><lizanChildren>{skid[5]}</lizanChildren><lizanEggs>{skid[6]}</lizanEggs><bunnionChildren>{skid[7]}</bunnionChildren><wolfPupChildren>{skid[8]}</wolfPupChildren><miceChildren>{skid[9]}</miceChildren><birdEggs>{skid[10]}</birdEggs><birdChildren>{skid[11]}</birdChildren><pigChildren>{skid[12]}</pigChildren><calfChildren>{skid[13]}</calfChildren><bugEggs>{skid[14]}</bugEggs><bugChildren>{skid[15]}</bugChildren><skunkChildren>{skid[16]}</skunkChildren><minotaurChildren>{skid[17]}</minotaurChildren><freakyGirlChildren>{skid[18]}</freakyGirlChildren></kid><trav></trav><bag>')
         text.write(f"{''.join([f'<slot{i}>{j}</slot{i}>' for i,j in enumerate(_bagArray)])}</bag><bagStack>{''.join([f'<slot{i}>{j}</slot{i}>' for i,j in enumerate(_bagStackArray)])}</bagStack><stash>{''.join([f'<slot{i}>{j}</slot{i}>' for i,j in enumerate(_stashArray)])}</stash><stashStack>{''.join([f'<slot{i}>{j}</slot{i}>' for i,j in enumerate(_stashStackArray)])}</stashStack><preg>{''.join([f'<i{i}>{j}</i{i}>' for i,j in enumerate(_pregArray)])}</preg></data>")
         data = xmletree.fromstring(text.getvalue())
      xml = xmletree.ElementTree(element=data)
      xmletree.indent(xml, space='\t')
      xml.write(outputfile, encoding='UTF-8', xml_declaration=True)

   def cli_checkInputFile(self, file):
      file = Path(file).resolve()
      if not file.exists():
         raise Exception('"%s" does not exist.' % file)
      self.cli_checkFile(file)

   def cli_checkOutputFile(self, file):
      file = Path(file).resolve()
      self.cli_checkFile(file)

   def cli_checkFile(self, file):
      file = Path(file).resolve()
      if file.is_dir():
         raise Exception('"%s" is not a file.' % file)
      if not file.name.endswith(('.xml', '.sol', '.nim', '.toml')):
         raise FileTypeError('"%s" is not of a supported file type' % file)
      name = file.name.split('.')
      if len(name) == 1:
         raise Exception('"%s" does not have an extension' % file)

   def command_single(self, inputfile, output):
      self.cli_checkInputFile(inputfile)
      inputfile = Path(inputfile).resolve()
      tempin = inputfile.name.split('.')
      if output in {'.xml', '.sol', '.nim', '.toml'}:
         if tempin[-1] == output:
            raise Exception('Input and output can not be of the same file type')
         outputfile = inputfile.parent / (inputfile.stem + output)
         self.cli_checkOutputFile(outputfile)
         if outputfile.exists():
            ans = input('Output file exists, would you like to overwrite it? (y/N) ')
            if ans.lower() in {'','n'}:
               print('Aborted')
               exit()
         self.convertSave(str(inputfile), 'detect', str(outputfile), output)
         print(self.message['text'])
      else:
         self.cli_checkOutputFile(output)
         outputfile = Path(output).resolve()
         tempout = outputfile.name.split('.')
         if tempout[-1] == tempin[-1]:
            raise Exception('Output file type can not be the same as input file type')
         if outputfile.exists():
            ans = input('Output file exists, would you like to overwrite it? (y/N) ')
            if ans.lower() in ('','n'):
               print('Aborted')
               exit()
         self.convertSave(str(inputfile), 'detect', str(outputfile), 'detect')
         print(self.message['text'])

   def command_many(self, outputformat, files):
      if not outputformat.startswith('.'):
         outputformat = '.' + outputformat
      for i in files:
         try:
            self.message['text'] = ''
            self.cli_checkInputFile(i)
            inputfile = Path(i)
            tempin = str(inputfile.name).split('.')
            if tempin[-1] == outputformat:
               raise Exception('Output file type can not be the same as input file type')
            outputfile = inputfile.parent / (inputfile.stem + outputformat)
            self.cli_checkOutputFile(outputfile)
            if outputfile.exists():
               ans = input('Output file exists, would you like to overwrite it? (y/N) ')
               if ans.lower() in {'', 'n'}:
                  print('[%s] Aborted' % i)
                  continue
            self.convertSave(str(inputfile), 'detect', str(outputfile), outputformat)
            if self.message['text'] != 'Success':
               print('[%s] %s' % (i, self.message['text']))
         except Exception as e:
            print('[%s] %s: %s' % (i, type(e).__name__, e))
      print('Done')

   def command_dir(self, directory, outputformat):
      dir_ = Path(directory).resolve()
      if not dir_.exists():
         raise Exception('Provided path does not exist')
      if not dir_.is_dir():
         raise Exception('Provided path must be a directory')
      outputformat = checkOutputFormat(outputformat)
      files = [str(f) for f in dir_.iterdir() if f.is_file() and f.name.endswith(('.xml','.sol','.nim','.toml')) and not f.name.endswith(outputformat)]
      c.command_many(outputformat, files)

def help():
   print('Nimin_Savefile_Converter.py <mode> [...args]\nModes:\n\t-s --single\tTakes two arguesments, inputfile and outputfile/format. If a format is used instead of an output file, the file will be of the same name as the original with the new format.\n\t-m --many\tConverts all specified files to a format. ... -m <extension> [...files]\n\t-d --dir\tConverts all files in a directory (non-recursive). ... -d <dir> <extension>')

def checkOutputFormat(outformat):
   if outformat in {'.xml', '.sol', '.nim', '.toml'}:
      return outformat
   raise Exception('Invalid output format "%s"' % outformat)

if __name__ == '__main__':
   from sys import argv
   c = Converter()
   if len(argv) == 1:
      c.path = Path(__file__).parent
      c.gui_open()
   else:  # Comandline args
      c.message = {'text': ''}
      if argv[1] == 'help' or '--help' in argv or '-h' in argv:
         help()
      elif argv[1] in {'-s', '--single'}:
         # One file then output file or output type
         c.command_single(argv[2], argv[3])
      elif argv[1] in {'-m', '--many'}:
         # Convert all after this
         if len(argv) < 4:
            raise Exception('Not enough arguements')
         c.command_many(checkOutputFormat(argv[2]), argv[3:])
      elif argv[1] in {'-d', '--dir'}:
         if len(argv) != 4:
            raise Exception('Incorrect number of arguements')
         c.command_dir(argv[2], argv[3])
      else:
         help()
