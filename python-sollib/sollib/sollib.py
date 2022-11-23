from dataclasses import dataclass
import io
import codecs
import encodings
import binascii
import base64
import numpy
import os
from textwrap import wrap

class sol:
   def __init__(self, filepath, data):
      self.filepath = filepath
      self.data = data

   def Encode(self):
      """
      Encodes data to the sol file format (AMF3)
      """
      if self.data == None:
         return 'Error. No data'
      else:
          a = self.data  

   def Decode(self):
      """
      Decodes data from the sol file format (AMF3)
      """
      if self.filepath == None:
         return 'Error. No filepath'
      else:
         a = self.filepath
         b = open(self.filepath, "rb")
         c = str(binascii.hexlify(b.read()))
         d = c.replace("b'", "")
         e = d.replace("'", "")
         f = wrap(e, 2)
         magic = list(()) #unsignedShort
         LSO_length_bytes = list(()) #unsignedInt #FullFileLength(Bytes)
         TCSO = list(())
         Padding1_length_hex = list(())
         Padding1_length = ""
         Padding1 = list(())
         LSO_name_length_hex = list(())
         LSO_name_length = ""
         LSO_name_hex = list(())
         LSO_name = ""
         AMF_version_hex = list(())
         i = 0
         while i <= 1:
            magic.append(f[i])
            i += 1
         while i > 1 and i <= 5:
            LSO_length_bytes.append(f[i])
            i += 1
         LSO_length = int(''.join(LSO_length_bytes), base=16)
         while i > 5 and i <= 9:
            TCSO.append(f[i])
            i += 1
         while i > 9 and i <= 11:
            Padding1_length_hex.append(f[i])
            i += 1
         Padding1Temp = ''.join(Padding1_length_hex)
         Padding1_length = int(Padding1Temp, base=16)
         i2 = 11 + Padding1_length
         i3 = i2 + 2
         while i > 11 and i <= i2:
            Padding1.append(f[i])
            i += 1
         while i > i2 and i <= i3:
            LSO_name_length_hex.append(f[i])
            i += 1
         LSO_name_length = int(''.join(LSO_name_length_hex), base=16)
         i4 = i3 + LSO_name_length
         while i > i3 and i <= i4:
            LSO_name_hex.append(f[i])
            i += 1
         LSOnametemp1 = ''.join(LSO_name_hex)
         LSO_name = bytes.fromhex(LSOnametemp1).decode("ASCII")
         while i > i4 and i <= (i4 + 4):
            AMF_version_hex.append(f[i])
            i += 1
         if AMF_version_hex[4] == "00":
            while i <= LSO_length:

         if AMF_version_hex[4] == "03":
            while i <= LSO_length:

         """
         #bytes 0-15 are header, bytes onward are data
         magic = list((f[0], f[1]))
         LSO_length_bytes = list((f[2], f[3], f[4], f[5]))
         LSO_length_bin1 = ''.join(LSO_length_bytes)
         LSO_length_bin = bin(int(LSO_length_bin1, 16))[2:]
         #bin(int(LSO_length_bin1, 16))[2:].zfill(len(LSO_length_bytes) * )
         LSO_length = int(LSO_length_bin, 2)
         TCSO_bytes = list((f[6], f[7], f[8], f[9]))
         TCSO = bytes.fromhex(''.join(TCSO_bytes)).decode("ASCII")
         header_padding = list((f[10], f[11], f[12], f[13], f[14], f[15]))
         #LSO_name_end = 18 + LSO_length
         LSO_name = list(())
         #for i in range(18, LSO_name_end):
             #LSO_name.append(f[i])
         #var1 = bytes.fromhex(''.join(LSO_name)).decode("ASCII")
         #AMF_Version = list((f[LSO_name_end + 1], f[LSO_name_end + 2], f[LSO_name_end + 3], f[LSO_name_end + 4]))
         """
         #final_data = list((magic, LSO_length_bytes, TCSO, Padding1_length_hex, Padding1))
         #print(final_data)
      """
      def Length(ver, byte):
         if ver == "00":
            if byte = "00":
            if byte = "01":
            if byte = "02":
            if byte = "03":
            if byte = "05":
            if byte = "06":
            if byte = "07":
            if byte = "08":
            if byte = "09":
            if byte = "0a":
            if byte = "0b":
            if byte = "0c":
         if ver == "03":
            if byte = "00":
            if byte = "01":
            if byte = "02":
            if byte = "03":
            if byte = "04":
            if byte = "05":
            if byte = "06":
            if byte = "08":
            if byte = "09":
            if byte = "0a":
            if byte = "0c":
            if byte = "0d":
            if byte = "0d":
            if byte = "0d":
            if byte = "0d":
      """
def test():
    a = sol('/home/ajdel/.macromedia/Flash_Player/#SharedObjects/FFU46DVQ/localhost/Nimin_Save1.sol', None)
    a.Decode()

test()