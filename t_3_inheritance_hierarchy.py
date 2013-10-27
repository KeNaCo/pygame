#!/bin/python3

class Parent:
	def print(self):
		print("Parent")
	
class Child2(Parent):
	pass

class Child(Parent):
	def print(self):
		print("Childer rewriten print")

	def child_print(self):
		print("Child")

class GrandChild(Child):
	def grand_child_print(self):
		print("Grand Child")

class Grand2Child(GrandChild):
	def grand_2_child_print(self):
		print("Grand Grand Child")

if (__name__ == '__main__'): #main function
	a = Parent()
	b = Child()
	c = GrandChild()
	d = Grand2Child()
	
	print("Parent methods:")
	a.print()
	
	print("\nChild methods:")
	b.print()
	b.child_print()
	
	print("\nGrand child methods:")
	c.print()
	c.child_print()
	c.grand_child_print()
	
	print("\nGrand grand child methods:")
	d.print()
	d.child_print()
	d.grand_child_print()
	d.grand_2_child_print()
	
	print("\n2nd Child call:")
	e = Child2()
	e.print()
