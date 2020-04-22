class Employee:
 def __init__(self,name):
  self.name=name
 def print(self):
  print(self.name)
 def __init__(self,name):
  self._name=name
 def print(self):
  print(self._name)
 def __init__(self,name):
  self.__name=name
 def print(self):
  print(self.__name)
first=Employee("Renu")
second=Employee("Simran")
third=Employee("Rakshi")

