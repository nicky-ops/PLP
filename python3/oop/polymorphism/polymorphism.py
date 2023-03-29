"""
Polymorphism is the ability of an object to take many forms
"""

# Method Overriding
class Vehicle:
  def __init__(self, name, color, price):
    self.name = name
    self.color = color
    self.price = price
    
  def speed(self):
    print("Maximum Speed: 150")

  def change_gear(self):
    print("5 gear")

  def show(self):
    print(f"Details: {self.name}, {self.color}, {self.price}")

class Car(Vehicle):
  def speed(self):
    print("Max speed: 240")

  def change_gear(self):
    print("6 gear")

class Truck(Vehicle):
  def speed(self):
    print("Max Speed: 200")

  def change_gear(self):
    print("8 gear")

car1 = Car("M1 Competition", "Red", 200000)
car1.speed()

truck1 = Truck("Kamaz 240", "Beige", "75000")
truck1.speed()

car1.show()
truck1.show()

# Overriding Built in functions
class Shopping:
  def __init__(self, basket, buyer):
    self.basket = list(basket)
    self.buyer = buyer

  def __len__(self):
    print("Redifining length")
    count = len(self.basket)
    return count * 2

shopping = Shopping(['shoes', 'dress'], 'Zena')
print(len(shopping))