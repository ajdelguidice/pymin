import math as m
import random as r
from numpy import nan
from numpy import inf
from numpy import NINF
"""
This library implements types as close to how they were implemented in ActionScript 3 as I could get them.
Currently only Array (lists in python) and Boolean methods.
These are full types so the you can define a variable as one of them and use the methods as you would in ActionScript3.
The length method is just to return the length so it can't be assigned as it can in ActionScript3
The inherited properties in ActionScript3 are too complex for me to implement or aren't documented very well so I won't be implementing most of them.
Since it is hard to have a class and function with the same name, I put the conversion functions inside of their respective class (ex: instead of String(expression) to convert to string, use String.String(expression)).
"""
def listtoarray(l:list):
   tempArray = Array()
   for i in range(0,len(l)):
      tempArray[i] = l[i]
   return tempArray

def isFinite(num):
   if num == inf or num == NINF:
      return False
   else:
      return True
def isNaN(num):
   if num == nan:
      return True
   else:
      return False
class Array:
   """
   Lets you create array objects similar to ActionScript3
   Instead of making two different init functions, I made init create an array based on the values passed to it and another method called toSize to make the array a specific size. toSize fills all empty slots with the None object (since python doesn't have a null or undefined type) or deletes excess slots if there are more. WARNING: If nothing is passed to this method and it is called while there is data inside the array, all data in the array will be erased.
   """
   CASEINSENSITIVE = 1
   DESCENDING = 2
   UNIQUESORT = 4
   RETURNINDEXEDARRAY =  8
   NUMERIC = 16
   def __init__(self, *values):
      self.array = []
      for i in range(0,len(values)):
         self.array.append(values[i])
   def __str__(self):
      return f'{self.array}'
   def __len__(self):
      return len(self.array)
   def __getitem__(self, item):
      try:
         if self.array[item] == None:
            return "undefined"
         else:
            return self.array[item]
      except:
         return ""
   def __setitem__(self, item, value):
      if item + 1 > len(self.array):
         self.toSize(item + 1)
      self.array[item] = value
   def toSize(self, numElements=0):
      """
      Instead of making two different init functions, I made init create an array based on the values passed to it and this method to make the array a specific size. This method fills all empty slots with the None object (since python doesn't have a null or undefined type) or deletes excess slots if there are more. WARNING: If nothing is passed to this method and it is called while there is data inside the array, all data in the array will be erased.
      """
      if numElements < 0:
         raise Exception("RangeError")
      elif numElements == 0:
         self.array = []
      elif len(self) > numElements:
         while len(self) > numElements:
            self.pop()
      elif len(self) < numElements:
         while len(self) < numElements:
            self.push(None)
   def length(self):
      return len(self.array)
   def concat(self, *args):
      """
      Concatenates the elements specified in the parameters with the elements in an array and creates a new array. If the parameters specify an array, the elements of that array are concatenated. If you don't pass any parameters, the new array is a duplicate (shallow clone) of the original array.
      Parameters:
         *args — A value of any data type (such as numbers, elements, or strings) to be concatenated in a new array.
      Returns:
         Array — An array that contains the elements from this array followed by elements from the parameters.
      """
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
   def every(self, callback):
      """
      Executes a test function on each item in the array until an item is reached that returns False for the specified function. You use this method to determine whether all items in an array meet a criterion, such as having values less than a particular number.
      Parameters:
         callback:Function — The function to run on each item in the array. This function can contain a simple comparison (for example, item < 20) or a more complex operation, and is invoked with three arguments; the value of an item, the index of an item, and the Array object:
         - function callback(item:*, index:int, array:Array)
      Returns:
         Boolean — A Boolean value of True if all items in the array return True for the specified function; otherwise, False.
      """
      tempBool = True
      for i in range(0,len(self)):
         if callback(self[i], i, self) == False:
            tempBool == False
            break
      return tempBool
   def filter(self, callback):
      """
      Executes a test function on each item in the array and constructs a new array for all items that return True for the specified function. If an item returns False, it is not included in the new array.
      Parameters:
         callback:Function — The function to run on each item in the array. This function can contain a simple comparison (for example, item < 20) or a more complex operation, and is invoked with three arguments; the value of an item, the index of an item, and the Array object:
         - function callback(item:*, index:int, array:Array)
      Returns:
         Array — A new array that contains all items from the original array that returned True. 
      """
      tempArray = Array()
      for i in range(0,len(self)):
         if callback(self[i], i, self) == True:
            tempArray.push(self[i])
      return tempArray
   def forEach(self, callback):
      """
      Executes a function on each item in the array.
      Parameters:
         callback:Function — The function to run on each item in the array. This function can contain a simple command (for example, a trace() statement) or a more complex operation, and is invoked with three arguments; the value of an item, the index of an item, and the Array object:
         - function callback(item:*, index:int, array:Array)
      """
      for i in range(0, len(self)):
         self[i] = callback(self[i], i, self)
   def indexOf(self, searchElement, fromIndex=0):
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
   def insertAt(self, index, element):
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
            result += str(self[i]) + str(sep)
         else:
            result += str(self[i])
         i += 1
      return result
   def lastIndexOf(self, searchElement, fromIndex=99*10^99):
      """
      Searches for an item in an array, working backward from the last item, and returns the index position of the matching item using ==.
      Parameters:
	      searchElement — The item to find in the array.
	      fromIndex:int (default = 99*10^99) — The location in the array from which to start searching for the item. The default is the maximum value allowed for an index. If you do not specify fromIndex, the search starts at the last item in the array.
      Returns:
	      int — A zero-based index position of the item in the array. If the searchElement argument is not found, the return value is -1.
      """
      index = -1
      for i in range(0,len(self)):
         l = len(self) - i - 1
         if self[l] == searchElement:
            index = l
            break
      return index
   def map(self, callback):
      """
      Executes a function on each item in an array, and constructs a new array of items corresponding to the results of the function on each item in the original array.
      Parameters:
         callback:Function — The function to run on each item in the array. This function can contain a simple command (such as changing the case of an array of strings) or a more complex operation, and is invoked with three arguments; the value of an item, the index of an item, and the Array object:
         - function callback(item:*, index:int, array:Array)
      Returns:
         Array — A new array that contains the results of the function on each item in the original array.
      """
      output = Array()
      output.toSize(len(self))
      for i in range(0,len(self)):
         output[i] = callback(self[i], i, self)
      return output
   def pop(self):
      """
      Removes the last element from an array and returns the value of that element.
      Returns:
         * — The value of the last element (of any data type) in the specified array.
      """
      i = len(self) - 1
      value = self[i]
      self.array.pop(i)
      return value
   def push(self, *args):
      """
      Adds one or more elements to the end of an array and returns the new length of the array.
      Parameters:
         *args — One or more values to append to the array. 
      """
      i = 0
      while i < len(args):
         self.array.append(args[i])
         i += 1
   def removeAt(self, index):
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
      """
      Removes the first element from an array and returns that element. The remaining array elements are moved from their original position, i, to i-1.
      Returns:
         * — The first element (of any data type) in an array. 
      """
      value = self[0]
      for i in range(0,len(self)):
         if i < len(self) - 1:
            self[i] = self[i+1]
         else:
            self.pop()
      return value
   def slice(self, startIndex=0, endIndex=99*10^99):
      """
      Returns a new array that consists of a range of elements from the original array, without modifying the original array. The returned array includes the startIndex element and all elements up to, but not including, the endIndex element.
      If you don't pass any parameters, the new array is a duplicate (shallow clone) of the original array.
      Parameters:
         startIndex:int (default = 0) — A number specifying the index of the starting point for the slice. If startIndex is a negative number, the starting point begins at the end of the array, where -1 is the last element.
         endIndex:int (default = 99*10^99) — A number specifying the index of the ending point for the slice. If you omit this parameter, the slice includes all elements from the starting point to the end of the array. If endIndex is a negative number, the ending point is specified from the end of the array, where -1 is the last element.
      Returns:
         Array — An array that consists of a range of elements from the original array.
      """
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
   def some(self, callback):
      """
      Executes a test function on each item in the array until an item is reached that returns True. Use this method to determine whether any items in an array meet a criterion, such as having a value less than a particular number.
      Parameters:
         callback:Function — The function to run on each item in the array. This function can contain a simple comparison (for example item < 20) or a more complex operation, and is invoked with three arguments; the value of an item, the index of an item, and the Array object:
         - function callback(item:*, index:int, array:Array)
      Returns:
         Boolean — A Boolean value of True if any items in the array return True for the specified function; otherwise False.
      """
      tempBool = False
      for i in range(0,len(self)):
         if callback(self[i], i, self) == Ture:
            tempBool == True
            break
      return tempBool
   def sort(sortOptions=0):
      """
      """
      if sortOptions == 0:
         raise Exception("Not yet implemented")
      elif sortOptions == 1:
         raise Exception("Not yet implemented")
      elif sortOptions == 2:
         raise Exception("Not yet implemented")
      elif sortOptions == 4:
         raise Exception("Not yet implemented")
         pass
      elif sortOptions == 8:
         raise Exception("Not yet implemented")
      elif sortOptions == 16:
         self.array.sort()
   def sortOn():
      pass
   def splice(self, startIndex, deleteCount, *values):
      """
      Adds elements to and removes elements from an array. This method modifies the array without making a copy.
      Parameters:
	      startIndex:int — An integer that specifies the index of the element in the array where the insertion or deletion begins. You can use a negative integer to specify a position relative to the end of the array (for example, -1 is the last element of the array).
	      deleteCount:int — An integer that specifies the number of elements to be deleted. This number includes the element specified in the startIndex parameter. If you do not specify a value for the deleteCount parameter, the method deletes all of the values from the startIndex element to the last element in the array. If the value is 0, no elements are deleted.
	      *values — An optional list of one or more comma-separated values to insert into the array at the position specified in the startIndex parameter. If an inserted value is of type Array, the array is kept intact and inserted as a single element. For example, if you splice an existing array of length three with another array of length three, the resulting array will have only four elements. One of the elements, however, will be an array of length three.
      Returns:
	      Array — An array containing the elements that were removed from the original array. 
      """
      removedValues = Array()
      i = deleteCount
      while i > 0:
         removedValues.push(self[startIndex])
         self.removeAt(startIndex)
         i -= 1
      if len(values) > 0:
         for i in range(0,len(values)):
            self.insertAt(startIndex + i, values[i])
      return removedValues
   def toLocaleString(self):
      """
      Returns a string that represents the elements in the specified array. Every element in the array, starting with index 0 and ending with the highest index, is converted to a concatenated string and separated by commas. In the ActionScript 3.0 implementation, this method returns the same value as the Array.toString() method.
      Returns:
	      String — A string of array elements. 
      """
      return self.toString()
   def toString(self):
      """
      Returns a string that represents the elements in the specified array. Every element in the array, starting with index 0 and ending with the highest index, is converted to a concatenated string and separated by commas. To specify a custom separator, use the Array.join() method.
      Returns:
	      String — A string of array elements. 
      """
      a = ""
      for i in range(0, len(l1)):
         if i == len(l1) - 1:
            a += str(self[i])
         else:
            a += str(self[i]) + ","
      return a
   def unshift(self, *args):
      """
      Adds one or more elements to the beginning of an array and returns the new length of the array. The other elements in the array are moved from their original position, i, to i+1.
      Parameters:
	      *args — One or more numbers, elements, or variables to be inserted at the beginning of the array.
      Returns:
	      int — An integer representing the new length of the array.
      """
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
class Boolean:
   """
   Lets you create boolean object similar to ActionScript3
   Since python is case sensitive the values are "True" or "False" instead of "true" or "false"
   """
   def __init__(self, expression=False):
      self.bool = self.Boolean(expression)
   def __str__(self):
      return f'{self.bool}'
   def __getitem__(self):
      return self.bool
   def __setitem__(self, value):
      self.bool = value
   def Boolean(self, expression):
      if type(expression) == int or type(expression) == float or type(expression) == Number:
         if expresssion == 0:
            result = False
         else:
            result = True
      if expression == "NaN":
         result = False
      if type(expresssion) == str or type(expression) == String:
         if exression == "":
            result = False
         else:
            result = True
      if expression == "null":
         result = False
      if expression == "undefined":
         result = False
      return result
   def toString(self):
      return str(self.bool)
   def valueOf(self):
      if self.bool == True:
         return True
      else:
         return False
class Math:
   E = 2.71828182845905
   LN10 = 2.302585092994046
   LN2 = 0.6931471805599453
   LOG10E = 0.4342944819032518
   LOG2E = 1.442695040888963387
   PI = 3.141592653589793
   SQRT1_2 = 0.7071067811865476
   SQRT2 = 1.4142135623730951
   def abs(val):
      return abs(val)
   def acos(val):
      return m.acos(val)
   def asin(val):
      return m.asin(val)
   def atan(val):
      return m.atan(val)
   def atan2(y, x):
      return m.atan2(y,x)
   def ceil(val):
      return m.ceil(val)
   def cos(angleRadians):
      return m.cos(angleRadians)
   def exp(val):
      return m.exp(val)
   def floor(val):
      return m.floor(val)
   def log(val):
      return m.log(val)
   def max(*values):
      return max(values)
   def min(*values):
      return min(values)
   def pow(base, pow):
      return m.pow(base,pow)
   def random():
      return r.random()
   def round(val):
      return round(val)
   def sin(angleRadians):
     return m.sin(angleRadians)
   def sqrt(val):
      return m.sqrt(val)
   def tan(angleRadians):
      return m.tan(angleRadians)
class Number:
   MAX_VALUE = 1.79e308
   MIN_VALUE = 5e-324
   NaN = nan
   NEGATIVE_INFINITY = inf
   POSITIVE_INFINITY = NINF
   def __init__(self, num):
      self.number = float(self.Number(num))
   def __str__(self):
      tempString = str(self.number)
      templist = tempString.split(".")
      if templist[1] == "0":
         return f'{int(templist[0])}'
      else:
         return f'{self.number}'
   def __getitem__(self):
      return self.number
   def __setitem__(self, value):
      self.number = value
   def __add__(self, value):
      try:
         return self.number + float(value)
      except ValueError:
         raise TypeError("can not add " + f'{type(value)}' + " to Number")
   def Number(self, expression):
      if type(expression) == int or type(expression) == float or type(expression) == Number:
         return expression
      elif expression == "undefined":
         return self.NaN
      elif expression == "null":
         return 0
      elif expression == self.NaN:
         return self.NaN
      elif type(expresssion) == bool or type(expression) == Boolean:
         if expression == True:
            return 1
         else:
            return 0
      elif type(expresssion) == str or type(expression) == String:
         if expression == "":
            return 0
         else:
            try:
               return float(expression)
            except:
               return self.NaN
   def toExponential(self, fractionDigits):
      if fractionDigits < 0 or fractionDigits > 20:
         raise Exception("RangeError: fractionDigits is outside of acceptable range")
      else:
         tempString = str(self.number)
         templist = tempString.split(".")
         tempExp = len(templist[0]) - 1
         pass
   def toFixed(self, fractionDigits):
      if fractionDigits < 0 or fractionDigits > 20:
         raise Exception("RangeError: fractionDigits is outside of acceptable range")
      else:
         tempString1 = str(self.number)
         templist = tempString1.split(".")
         if fractionDigits == 0:
            return templist[0]
         else:
            tempString2 = templist[0]
            tempString2 += "."
            tempString3 = templist[1]
            for i in range(0,fractionDigits):
               try:
                  tempString2 += tempString3[i]
               except IndexError:
                  tempString2 += "0"
            return tempString2
   def toPrecision():
      pass
   def toString(self, radix=10):
      #!
      return str(self.number)
   def valueOf(self):
      return self.number
class String:
   def __init__(self, value=""):
      self.string = self.String(value)
   def __str__(self):
      return self.string
   def __getitem__(self, item={}):
      if item == {}:
         return self.string
      else:
         return self.string[item]
   def __setitem__(self, value):
      self.string = value
   def __len__(self):
      return len(self.string)
   def __add__(self, value):
      return self.string + self.String(value)
   def length(self):
      len(self.string)
   def String(self, expression):
      if type(expression) == str or type(expression) == String:
         return expression
      elif expression == True:
         return "true"
      elif expression == False:
         return "false"
      elif expression == nan:
         return "NaN"
      elif type(expression) == Array or type(expression) == Boolean or type(expression) == Number:
         return expression.toString()
      else:
         return str(expression)
   def charAt(self, index=0):
      if index < 0 or index > len(self.string) - 1:
         return ""
      else:
         return self.string[index]
   def charCodeAt(self, index=0):
      if index < 0 or index > len(self.string) - 1:
         return nan
      else:
         return r'\u{:04X}'.format(ord(self.string[index]))
   def concat(self, *args):
      tempString = self.string
      for i in range(0, len(args)):
         tempString += self.String(args[i])
      return tempString
   def fromCharCode():
      pass
   def indexOf(self, val, startIndex=0):
      return self.string.find(val, startIndex)
   def lastIndexOf(self, val, startIndex={}):
      tempInt = len(self.string) - 1
      if startIndex == {} or startIndex > tempInt:
         return self.string.rfind(val,0,tempInt)
      else:
         return self.string.rfind(val,0,startIndex)
   def localeCompare():
      pass
   def match():
      pass
   def replace():
      pass
   def search():
      pass
   def slice():
      pass
   def split():
      pass
   def substring(self, startIndex=0, endIndex={}):
      tempInt = len(self.string)
      si = startIndex
      ei = endIndex
      tempString = String()
      if si < 0:
         si = 0
      if ei != {}:
         if ei < 0:
            ei = 0
      else:
         ei = tempInt
      if si > ei:
         temp = si
         si = ei
         ei = temp
      for i in range(si,ei):
         tempString += self.string[i]
      return tempString
   def toLocaleLowerCase(self):
      return self.toLowerCase()
   def toLocaleUpperCase(self):
      return self.toUpperCase()
   def toLowerCase(self):
      return self.string.lower()
   def toUpperCase(self):
      return self.string.upper()
   def valueOf(self):
      return self.string

def trace(*args):
   output = ""
   for i in range(0, len(args)):
      if len(args) == 1:
         output = str(args[0])
      else:
         if i == len(args) - 1:
            output += str(args[i])
         else:
            output += str(args[i]) + ", "
   print(output)

s1 = String("abcd")
print(s1.toUpperCase())