"""
This library implements methods as close to how they were implemented in ActionScript 3 as I could get them.
Currently only Array (lists in python) methods.
These are full types so the you can define a variable as one of them and use the Methods as you would in ActionScript3.
The length method is just to return the length so it can't be assigned as it can in ActionScript3
"""
class Array:
   """
   Lets you create array objects similar to ActionScript3
   Instead of making two different init functions, I made init create an array based on the values passed to it and another method called toSize to make the array a specific size. toSize fills all empty slots with empty strings (since python doesn't have a null or undefined type) or deletes excess slots if there are more. WARNING: If nothing is passed to this method and it is called while there is data inside the array, all data in the array will be erased.
   """
   def __init__(self, *values):
      a = []
      for i in range(0,len(values)):
         a.append(values[i])
      self.array:list = a
   def __str__(self):
      return f'{self.array}'
   def __len__(self):
      return len(self.array)
   def __getitem__(self, item):
      return self.array[item]
   def __setitem__(self, item, value):
      self.array[item] = value
   def length(self):
      return len(self.array)
   def concat(self, *args):
      if len(args) == 0:
         raise Exception("Must have at least 1 arguments")
      else:
         for i in range(0,len(args)):
            if self.array == []:
               self.array = args[i]
            else:
               if type(args[i]) == list or type(args[i]) == tuple or type(args[i]) == Array:
                  b = args[i]
                  c = 0
                  for c in range(0,len(b)):
                     self.push(b[c])
               else:
                  self.push(args[i])
   def every():
      pass
   def filter():
      pass
   def forEach():
      pass
   def indexOf(self, searchElement, fromIndex:int=0):
      """
      Searches for an item in an array using == and returns the index position of the item.
      Parameters:
         searchElement — The item to find in the array.
         fromIndex:int (default = 0) — The location in the array from which to start searching for the item.
      Returns:
         index:int — A zero-based index position of the item in the array. If the searchElement argument is not found, the return value is -1.
      """
      index = -1
      i = fromIndex
      while i < len(self):
         if self[i] == searchElement:
            index = i
            i = len(self)
         else:
            i += 1
      return index
   def insertAt(self, index:int, element):
      """
      Insert a single element into an array.
      Parameters
	      index:int — An integer that specifies the position in the array where the element is to be inserted. You can use a negative integer to specify a position relative to the end of the array (for example, -1 is the last element of the array).
	      element — The element to be inserted.
      """
      if index < 0:
         self.array.insert((len(l1) - abs(index)), element)
      else:
         self.array.insert(index, element)
   def join(self, sep=","):
      """
      Converts the elements in an array to strings, inserts the specified separator between the elements, concatenates them, and returns the resulting string. A nested array is always separated by a comma (,), not by the separator passed to the join() method.
      Parameters:
	      sep (default = ",") — A character or string that separates array elements in the returned string. If you omit this parameter, a comma is used as the default separator.
      Returns:
	      String — A string consisting of the elements of an array converted to strings and separated by the specified parameter.
      """
      result = ""
      i = 0
      for i in range(0, len(self)):
         if i != len(self) - 1:
            if type(self[i+1]) == list or type(self[i+1]) == tuple or type(self[i+1]) == Array or type(self[i]) == list or type(self[i]) == tuple or type(self[i]) == Array:
               result += str(self[i]) + ","
            else:
               result += str(self[i]) + str(sep)
         else:
            result += str(self[i])
         i += 1
      return result
   def lastIndexOf(l1:list, searchElement, fromIndex:int = 99*10^99):
      #!
      """
      Searches for an item in an array, working backward from the last item, and returns the index position of the matching item using ==.
      Parameters:
	      searchElement — The item to find in the array.
	      fromIndex:int (default = 99*10^99) — The location in the array from which to start searching for the item. The default is the maximum value allowed for an index. If you do not specify fromIndex, the search starts at the last item in the array.
      Returns:
	      int — A zero-based index position of the item in the array. If the searchElement argument is not found, the return value is -1.
      """
      i = fromIndex
      a = l1
      a.reverse()
      if i >= len(l1):
         i = len(l1)
      ia = len(l1) - i
      index1 = Array.indexOf(a, searchElement, ia)
      if index1 != -1:
         index = len(l1) - index1 - 1
      else:
         index = index1
      return index
   def map():
      pass
   def pop(self):
      i = len(self) - 1
      value = self[i]
      self.array.pop(i)
      return value
   def push(self, *args):
      i = 0
      while i < len(args):
         self.array.append(args[i])
         i += 1
   def removeAt(self, index:int):
      """
      Remove a single element from an array. This method modifies the array without making a copy.
      Parameters:
	      index:int — An integer that specifies the index of the element in the array that is to be deleted. You can use a negative integer to specify a position relative to the end of the array (for example, -1 is the last element of the array).
      Returns:
	      * — The element that was removed from the original array.
      """
      if index >= 0:
         value = self[index]
         self.array.pop(index)
      else:
         i = len(self) - 1 + index
         value = self[i]
         self.array.pop(i)
      return value
   def reverse(self):
      """
      Reverses the array in place.
      Returns:
	      Array — The new array.
      """
      a = Array()
      for i in range(0, len(self)):
         a.array.append(self[len(self) - 1 - i])
      for i in range(0, len(self)):
         self[i] = a[i]
   def shift(self):
      value = self[0]
      for i in range(0,len(self)):
         if i < len(self) - 1:
            self[i] = self[i+1]
         else:
            self.pop()
      return value
   def slice(self, startIndex:int=0, endIndex:int=99*10^99):
      i = startIndex
      result = Array()
      if endIndex > len(self):
         ei = len(self)
      else:
         ei = endIndex
      while i < ei:
         result.push(self[i])
         i += 1
      return result
   def some():
      pass
   def sort():
      pass
   def sortOn():
      pass
   def splice():
      pass
   def toLocaleString(self):
      return self.toString()
   def toString(self):
      a = ""
      for i in range(0, len(l1)):
         if i == len(l1) - 1:
            a += str(self[i])
         else:
            a += str(self[i]) + ","
      return a
   def unshift(self, *args):
      a = Array()
      for i in range(0, len(args)):
         a.push(args[i])
      for i in range(0, len(self)):
         a.push(self[i])
      for i in range(0, len(self)):
         self[i] = a[i]
      for i in range(len(self), len(a)):
         self.push(a[i])
      return len(self)
   def toSize(self, numElements:int=0):
      if numElements == 0:
         self.array = []
      elif len(self) > numElements:
         while len(self) > numElements:
            self.pop()
      elif len(self) < numElements:
         while len(self) < numElements:
            self.push("")


l1 = Array(1,2,3)
l2 = Array(4,5,6)
l1.concat(l2)
l1.insertAt(2,8)
print(l1)
