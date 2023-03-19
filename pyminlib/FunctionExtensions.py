import math

class lists:
   def splice(a:list, b:int, c:int="", d:list=[]):
      """
      ActionScript Array.splice()
      a is a list. (required)
      b is the element to start at (refers to the first element as 1 instead of 0). (required)
      c is the number of elements to remove (including b). If c is not provided, all elements from b on will be removed. (optional)
      d is a list of elements to be added at b after b to b+c is deleted. (optional)
      """
      templist = a
      if c == "":
         del templist[b:]
      elif c != 0:
         for i in range(c, 0, -1):
            templist.pop(b+i-1)
      if d != []:
         for i in range(0, len(d)):
            templist.insert(b+i, d[i])
      return templist
   def indexOf(a:list, b):
      try:
         x = a.index(b)
      except:
         x = -1
      return x
class logic:
   def inv(a:bool):
      "Returns the inverse of a boolean"
      if (a == True):
         return False
      if (a == False):
         return True
   def land(a:bool, b:bool):
      "Logical and of two booleans"
      if (a == True) and (b == True):
         return True
      else:
         return False
   def lor(a:bool, b:bool):
      "Logical or of two booleans"
      if (a == True) or (b == True):
         return True
      else:
         return False
   def nand(a:bool, b:bool):
      "Logical nand of two booleans"
      c = logic.inv(logic.land(a, b))
      return c
   def nor(a:bool, b:bool):
      "Logical nor of two booleans"
      c = logic.inv(logic.lor(a, b))
      return c
   def xor(a:bool, b:bool):
      "Logical xor of two booleans"
      c = logic.land(logic.nand(a, b), logic.lor(a, b))
      return c
   def xnor(a:bool, b:bool):
      "Logical xnor of two booleans"
      c = logic.lor(logic.nand(a, b), logic.land(a, b))
      return c

class operations:
   def roundup(a:float, b:float=""):
      """
      rounds a up to every b.
      if b is not provided, assumes b is 10
      """
      if b == "":
         b = 10
      c = a / b
      d = math.ceil(c)
      e = d * b
      return e
   def rounddown(a:float, b:float=""):
      """
      rounds a down to every b.
      if b is not provided, assumes b is 10
      """
      if b == "":
         b = 10
      c = a / b
      d = math.floor(c)
      e = d * b
      return e
   def plusplus1(a):
      b = a
      b += 1
      return b
   #def plusplus2(a, b:str):
   #   global str(b)
   #   str(b) += 1
   #   return a
