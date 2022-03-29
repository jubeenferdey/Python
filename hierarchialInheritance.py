#hierarchial inheritance
# Python program to demonstrate
# Hierarchical inheritance


# Base class
class HOD:
	def func1(self):
		print("I'm the HOD")

# Derived class1
class CO_ORDINATOR(HOD):
	def func2(self):
		print("I'm the co-ordinator under HOD")

# Derivied class2
class staff(HOD):
	def func3(self):
		print("I'm a STAFF under HOD")

# Driver's code
o1 = CO_ORDINATOR()
o2 = staff()
o1.func1()
o1.func2()
o2.func3()
