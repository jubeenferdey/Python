#single inheritance
class Parent:
  def myfun_p(self):
      print("I'm the Parent")
class Child(Parent):
  def myfun_c(self):
      print("I'm the Child")
obj = Child()
obj.myfun_p()
obj.myfun_c()