#!/bin/python3

import math

class OurException(Exception):
	def print(self):
		print("We raise your exception!")

class Class:
	def __init__(self):
		pass
	
	def sqrt(self, num):
		if (num < 0 ):
			raise OurException()
		else:
			return math.sqrt(num)

if (__name__ == '__main__'): #main function
	mat = Class()
	print(mat.sqrt(4))
	
	try:
		a = mat.sqrt(4)
	except Exception as e:
		e.print()
	
	print(a)
