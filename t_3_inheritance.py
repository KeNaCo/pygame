#!/bin/python3

class Parent:
	_phraze = None
	
	def __init__(self, phraze):
		self.__phraze = phraze

	def my_print(self):
		print("Its nice to say ", self._phraze, " every day :)")

class Child(Parent):
	def __init__(self, phraze):
		super().__init__(phraze)
	
class SlovakChild(Parent):
	def __init__(self, phraze):
		super.__init__(phraze)
	
	#redefinition of inherited method
	def my_print(self):
		print("Je pekné hovoriť každý deň", self._phraze) #we use protected variable from parent class

if (__name__ == '__main__'): #main function
	a = Parent("Hello")
	a.my_print()
	
	b = Child("Hello")
	b.my_print()
	
	c = SlovakChild("Ahoj")
	c.my_print()
