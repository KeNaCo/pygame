#!/bin/python3

class Class:
	__value = None
	
	def __init__(self, value = 0):
		self.__value = value
	
	def increase(self):
		self.__value += 1
	
	def print(self):
		print("Class value: ", self.__value)


if (__name__ == '__main__'): #main function
	b = Class(4)
	b.increase()
	b.increase()
	b.print()
	b.increase()
	b.print()
