import sys
import pathlib

def convert(image, file=0):
   """
   Manual function to use if this file is imported.
   'image' is the path to the image (Required)
   'file' is the path to the output file (Optional)
   """
   pconvert(image, file)

def phelp():
   print("Image to bytes converts a given image to a bytes object\nsyntax: imagetobytes.py [-h][-i][-o] or imagetobytes.py IMAGE FILE\n\t-h\t\tPrints this message\n\t-i IMAGE\t(Required) The path to the image (relative or absolute)\n\t-o FILE\t\t(Optional) The path to the file that the bytes are stored in (relative or absolute)")

def imgfile(image, file=0):
   if (pathlib.Path(args[image]).is_dir() == True):
      print("The input path provided is a directory not a file")
   elif ((pathlib.Path(args[file]).is_dir() == True) and (file != 0)):
      print("The output path provided is a directory not a file")
   elif (pathlib.Path(args[image]).is_file() == True):
      if (file == 0):
         pconvert(args[image], 0)
      else:
         pconvert(args[image], args[file])
   else:
      phelp()

def pconvert(image, file):
   if (type(file) == str):
      if (file.find("/") == True):
         fsep = file.split("/")
      elif (file.find("\\") == True):
         fsep = file.split("\\")
      fname = fsep[len(fsep) - 1]
      fext = fname.split(".")
   with open(image, "rb") as i:
      a = i.read()
      b = bytearray(a)
      if (file != 0):
         if (len(fext) > 1):
            if ((pathlib.Path(file).is_file() == True) and (fext[len(fext) -1] == "txt")):
               with open(file, "a") as f:
                  f.write("\n" + str(b))
            elif ((pathlib.Path(file).is_file() == False)):
               with open(file, "w") as f:
                  f.write(str(b))
            else:
               print("Output file exists and is not a txt file so it can't be written to.")
         else:
            print("Output file must be a txt file")
      else:
         print(b)

if __name__ == "__main__":
   args = sys.argv
   image = 0
   file = 0
   if ((len(args) == 1) or ((len(args) == 2) and (args[1] == "-h"))):
      phelp()
   elif (len(args) == 2):
      if ((args[1].find("/") != -1) or (args[1].find("\\") != -1)):
         imgfile(1)
      else:
         phelp()
   elif (len(args) == 3):
      if (args[1] == "-i"):
         imgfile(2)
      elif (((args[1].find("/") != -1) or (args[1].find("\\") != -1)) and ((args[2].find("/") != -1) or (args[2].find("\\") != -1))):
         imgfile(1, 2)
      else:
         phelp()
   elif ((len(args) == 5)):
      if ((args[1] == "-i") and (args[3] == "-o")):
         if (((args[2].find("/") != -1) or (args[2].find("\\") != -1)) and ((args[4].find("/") != -1) or (args[4].find("\\") != -1))):
            imgfile(2, 4)
         else:
            phelp()
      else:
         phelp()
