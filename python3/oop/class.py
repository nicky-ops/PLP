# empty class
class Label:
  pass

'''
class attributes are variables defined directly in the class that are shared by all objects of the class
'''
class Person:
  def __init__(self):
    print("Constructor invoked!")
    name = "JDM"

output = Person()
print(output.name)