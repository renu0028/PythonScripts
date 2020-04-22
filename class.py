class Student:
 name="Renu"
 RollNo=10
 college="ACEIT"
 State:"Rajasthan"

#print(Student.name)
#print(Student.college)
#s1=Student()
#s1.name=input("enter:")
#print(s1.name)
#s2=Student()
#print(s2.name)
 def __init__(self,branch):
  self.branch=branch
# def pass(self):
#  self.branch="CSE!"
# def fail(self):
#  self.branch="IT"
s1=Student()
s2=Student()
s1.branch("CSE")
s2.branch("IT")
