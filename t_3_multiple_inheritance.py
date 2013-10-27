#!/bin/python3

class Base:
	def __init__(self, *args):
		pass

class A(Base):
	var1 = 1

	def __init__(self, x):
		super(A, self).__init__(x)
	
	def work(self):
		print("Method in class A.")

class B(Base):
	var1 = 2
	
	def __init__(self, x):
		super(B, self).__init__(x)
	
	def work(self):
		print("Method in class B.")

class X(A, B):
	def __init__(self):
		super(X, self).__init__(0)

class Y(B, A):
	def __init__(self):
		super(Y, self).__init__(2)

"""
#This class invoke an conflict to inheritance order, which invoke exception TypeError
class W(X, Y):
	def __init__(self):
		super(W, self).__init__()
"""

"""
#Solution of our inheritance problem should be simple extensions of classes:
class W():
	x = None
	y = None
	
	def __init__(self):
		self.x = X()
		self.y = Y()
"""

if (__name__ == '__main__'): #main function
	
	x = X()
	x.work()
	
	y = Y()
	y.work()

	w = W()
	print()
	print("Calls of methods from W:")
	w.x.work()
	w.y.work()
