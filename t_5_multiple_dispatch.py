#!/bin/python3

class Person:
	__name = None
	__surname = None
	__age = None
	
	def __init__(self, name, surname, age):
		self.__name = name
		self.__surname = surname
		self.__age = age
	
	def print(self):
		print("Hi, I am", self.__name, self.__surname, "and I'm", self.__age, "years old.")

class Man(Person):
	def __init__(self, name="John", surname="Doe", age="not known"):
		super(Man, self).__init__(name, surname, age)

class Woman(Person):
	def __init__(self, name="Jane", surname="Doe", age="not known"):
		super(Woman, self).__init__(name, surname, age)

if (__name__ == '__main__'): #main function
	a = Man()
	b = Man("Peter")
	c = Man("John", age=20)
	
	d = Woman(surname="Hilton")
	e = Woman("Patricia", "Welsh", 35)
	f = Woman(age=22, name="Kate", surname="McDonald")
	
	for person in [a,b,c,d,e,f]:
		person.print()
