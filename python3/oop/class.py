# empty class
class Label:
  pass

'''
class attributes are variables defined directly in the class that are shared by all objects of the class
'''
class Person:
  def __init__(self,name,age, route = "MSA"):
    print("Constructor invoked!")
    self.name = name
    self.age = age
    self.route = route
  def display(self):
    print(f"Personal Name: {self.name}, Age: {self.age} ")

output = Person('Javan', '33')
output.display()