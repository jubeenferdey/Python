class College:
	def func1(self):
		print("Loyola College")

class Student1(College):
	def func2(self):
		print("This function is in student 1. ")

class Student2(College):
	def func3(self):
		print("This function is in student 2.")

class Student3(Student1, College):
	def func4(self):
		print("This function is in student 3.")

# Driver's code
o = Student3()
o.func1()
o.func2()





