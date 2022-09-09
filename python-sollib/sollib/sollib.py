from dataclasses import dataclass
import io
import codecs
import encodings
import binascii
import base64
import numpy
import os
from textwrap import wrap
import pyamf

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
            g = pyamf.sol.decode(f)
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
            #final_data = list((magic, LSO_length_bytes, TCSO, header_padding, LSO_name,))
            #print(f)
            print(g)

def test():
    a = sol('/home/ajdel/.macromedia/Flash_Player/#SharedObjects/FFU46DVQ/localhost/Nimin_Save1.sol', None)
    a.Decode()

test()