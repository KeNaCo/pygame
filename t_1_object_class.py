#!/bin/python3

class Class:
	my_property = None
	
	def __init__(self, value):
		self.my_property = value
	
	def __del__(self):
		pass
	
	def my_print(self):
		print("My property value is: ", self.my_property)

if (__name__ == '__main__'): #main function
	object1 = Class("one")
	object2 = Class(42)
	
	object1.my_print()
	object2.my_print()
