#multi-level inheritance
class Principal:
  def principal(self):
    print("I’m the Principal")
class Teacher(Principal):
  def teacher(self):
    print("I’m a Teacher")
class Student(Teacher):
  def student(self):
    print("I’m a student")
d = Student()
d.principal()
d.teacher()
d.student()
