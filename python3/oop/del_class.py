class Animal:
  def __init__(self, name, param = "pet" ):
    self.name = name
    self.param = param
  def display(self):
    print(f"{self.name} is a good {self.param}.")


p = Animal("Cat")
p.display()

del p.name
p.display()

del p
p.display()

del Animal
p = Animal("Mink")