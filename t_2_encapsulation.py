#!/bin/python3

from t_2_blackbox import BlackBox

class Conventions:
	__special__ = None #dont use!!!
	__private = None
	_protected = None
	public = None
	
	def __special__(self): pass
	def __private(self): pass
	def _protected(self): pass
	def public(self): pass

"""
This is only public api of Blackbox class which is in t_2_blackbox.pyc bytecode file, so you can't see the code of this class (example of close source in python)

class Blackbox:
	__init__(self, listOfNumbers)
	__del__(self)
	output(self)
	input(self, listOfNumbers)
"""

class WhiteBox:
	listOfValues = None
	
	def __init__(self, listOfNumbers):
		self.listOfValues = listOfNumbers
	
	def output(self):
		return sum(self.listOfValues)
	
	def input(self, listOfNumbers):
		self.listOfValues += listOfNumbers

if (__name__ == '__main__'): #main function
	
	a = WhiteBox([1,2,3])
	a.input([7,8,9])
	
	#here we access to an internal variable, we should not, but we have knowledge about this class and we can.. 
	#PS: internal variables should be protected, then this construction invoke error exception
	a.listOfValues += [4,6]
	print("This is sum of our list: ", a.output())
	
	b = BlackBox([1,2,3])
	b.input([4,5])
	b.output()
