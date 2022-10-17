class string:
   def splice(a, b, c=""):
      templist = a
      if c == "":
         del templist[b:]
      elif c != 0:
         for i in range(c, 0, -1):
            templist.pop(b+i-1)
      return templist
#      tempArray2 = tempArray1[b:b+c]
#      tempArray3 = 
#      return tempArray2

l1 = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(string.splice(l1, 3, 5))
print(string.splice(l1, 3))
#string.test()