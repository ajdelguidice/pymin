from pathlib import Path
from sys import argv


def validatePath(path):
   path = Path(path).resolve()
   if path.is_dir():
      raise Exception(f'Path "{path}" must be a file.')
   return path


def convertFile(inputfile, outputfile=None):
   inputfile = validatePath(inputfile)
   if not inputfile.exists():
      raise Exception(f'Path "{inputfile}" does not exist.')
   with inputfile.open('rb') as f:
      inputbytes = bytearray(f.read())
   if outputfile is None:  # Print
      print(inputbytes)
   else:
      outputfile = validatePath(outputfile)
      if not outputfile.name.endswith('.txt'):
         raise Exception('Output file must be a txt file.')
      if outputfile.exists():
         with open(outputfile, 'a') as f:
            f.write(f'\n{inputbytes}')
      else:
         with open(outputfile, 'w') as f:
            f.write(str(inputbytes))


if __name__ == '__main__':
   hmsg = 'Outputs the a string of bytes that represent the input.\nUsage: imagetobytes.py inputfile outputfile'
   largs = len(argv)
   if largs == 1 or '-h' in argv or '--help' in argv:
      print(hmsg)
   elif largs == 2:
      convertFile(argv[1])
   elif largs == 3:
      convertFile(argv[1], argv[2])
   else:
      print(hmsg)
