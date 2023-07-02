import tkinter
import pyminlib.as3toplevel as as3

keys = as3.Array()
jskeys = as3.Array()
jskeys[8] = "backspace"
keys[22] = 8
jskeys[9] = "tab"
keys[23] = 9
jskeys[13] = "enter"
keys[36] = 13
keys[104] = 13
jskeys[16] = "shift"
keys[50] = 16
keys[62] = 16
jskeys[17] = "ctrl"
keys[37] = 17
keys[105] = 17
jskeys[18] = "alt"
keys[64] = 18
keys[108] = 18
jskeys[19] = "pause/break"
keys[127] = 19
jskeys[20] = "caps lock"
keys[66] = 20
jskeys[27] = "escape"
keys[9] = 27
jskeys[32] = "Space"
keys[65] = 32
jskeys[33] = "page up"
keys[112] = 33
jskeys[34] = "page down"
keys[117] = 34
jskeys[35] = "end"
keys[115] = 35
jskeys[36] = "home"
keys[110] = 36
jskeys[37] = "arrow left"
keys[113] = 37
jskeys[38] = "arrow up"
keys[111] = 38
jskeys[39] = "arrow right"
keys[114] = 39
jskeys[40] = "arrow down"
keys[116] = 40
jskeys[44] = "print screen"
#!
jskeys[45] = "insert"
keys[118] = 45
jskeys[46] = "delete"
keys[119] = 46
jskeys[48] = "0"
keys[19] = 48
jskeys[49] = "1"
keys[10] = 49
jskeys[50] = "2"
keys[11] = 50
jskeys[51] = "3"
keys[12] = 51
jskeys[52] = "4"
keys[13] = 52
jskeys[53] = "5"
keys[14] = 53
jskeys[54] = "6"
keys[15] = 54
jskeys[55] = "7"
keys[16] = 55
jskeys[56] = "8"
keys[17] = 56
jskeys[57] = "9"
keys[18] = 57
jskeys[65] = "a"
keys[38] = 65
jskeys[66] = "b"
keys[56] = 66
jskeys[67] = "c"
keys[54] = 67
jskeys[68] = "d"
keys[40] = 68
jskeys[69] = "e"
keys[26] = 69
jskeys[70] = "f"
keys[41] = 70
jskeys[71] = "g"
keys[42] = 71
jskeys[72] = "h"
keys[43] = 72
jskeys[73] = "i"
keys[31] = 73
jskeys[74] = "j"
keys[44] = 74
jskeys[75] = "k"
keys[45] = 75
jskeys[76] = "l"
keys[46] = 76
jskeys[77] = "m"
keys[58] = 77
jskeys[78] = "n"
keys[57] = 78
jskeys[79] = "o"
keys[32] = 79
jskeys[80] = "p"
keys[33] = 80
jskeys[81] = "q"
keys[24] = 81
jskeys[82] = "r"
keys[27] = 82
jskeys[83] = "s"
keys[39] = 83
jskeys[84] = "t"
keys[28] = 84
jskeys[85] = "u"
keys[30] = 85
jskeys[86] = "v"
keys[55] = 86
jskeys[87] = "w"
keys[25] = 87
jskeys[88] = "x"
keys[53] = 88
jskeys[89] = "y"
keys[29] = 89
jskeys[90] = "z"
keys[52] = 90
jskeys[91] = "left window key"
#!
jskeys[92] = "right window key"
#!
jskeys[93] = "select key"
#!
jskeys[96] = "numpad 0"
keys[90] = 96
jskeys[97] = "numpad 1"
keys[87] = 97
jskeys[98] = "numpad 2"
keys[88] = 98
jskeys[99] = "numpad 3"
keys[89] = 99
jskeys[100] = "numpad 4"
keys[83] = 100
jskeys[101] = "numpad 5"
keys[84] = 101
jskeys[102] = "numpad 6"
keys[85] = 102
jskeys[103] = "numpad 7"
keys[79] = 103
jskeys[104] = "numpad 8"
keys[80] = 104
jskeys[105] = "numpad 9"
keys[81] = 105
jskeys[106] = "multiply"
keys[63] = 106
jskeys[107] = "add"
keys[86] = 107
jskeys[109] = "subtract"
keys[82] = 109
jskeys[110] = "decimal point"
keys[91] = 110
jskeys[111] = "divide"
keys[106] = 111
jskeys[112] = "f1"
keys[67] = 112
jskeys[113] = "f2"
keys[68] = 113
jskeys[114] = "f3"
keys[69] = 114
jskeys[115] = "f4"
keys[70] = 115
jskeys[116] = "f5"
keys[71] = 116
jskeys[117] = "f6"
keys[72] = 117
jskeys[118] = "f7"
keys[73] = 118
jskeys[119] = "f8"
keys[74] = 119
jskeys[120] = "f9"
keys[75] = 120
jskeys[121] = "f10"
keys[76] = 121
jskeys[122] = "f11"
keys[95] = 122
jskeys[123] = "f12"
keys[96] = 123
jskeys[144] = "num lock"
keys[77] = 144
jskeys[145] = "scroll lock"
keys[78] = 145
jskeys[182] = "My Computer (multimedia keyboard)"
#!
jskeys[183] = "My Calculator (multimedia keyboard)"
#!
jskeys[186] = "semi-colon"
keys[47] = 186
jskeys[187] = "equal sign"
keys[21] = 187
jskeys[188] = "comma"
keys[59] = 188
jskeys[189] = "dash"
keys[20] = 189
jskeys[190] = "period"
keys[60] = 190
jskeys[191] = "forward slash"
keys[61] = 191
jskeys[192] = "grave"
keys[49] = 192
jskeys[219] = "open bracket"
keys[34] = 219
jskeys[220] = "back slash"
keys[51] = 220
jskeys[221] = "close braket"
keys[35] = 221
jskeys[222] = "single quote"
keys[48] = 222
print(keys,jskeys)

def key_press(e):
   global jskeys, keys
   print(e.keycode)
   if keys[e.keycode] == "undefined":
      print("u")
   else:
      print(jskeys[keys[e.keycode]],keys[e.keycode])
root = tkinter.Tk()
root.geometry("400x400")

root.bind('<KeyPress>',key_press)

root.mainloop()
