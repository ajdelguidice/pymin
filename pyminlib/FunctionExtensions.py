class lists:
   def splice(a, b:int, c:int="", d:list=(())):
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
