#multiple inheritance
class Name:
  name = ""
def myfun1(self):
  print(self.name)
class Surname:
  surname = ""
def myfun2(self):
  print(self.surname)
# Multi Child class
class Student(Name, Surname):
  def parents(self):
    print("Name :", self.name)
    print("Surname :", self.surname)
stud = Student()
stud.name = "Kewin"
stud.surname = "Sebaasti"
stud.parents()
