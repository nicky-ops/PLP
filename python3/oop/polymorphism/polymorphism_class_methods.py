class Ferrari:
  def fuel_type(self):
    print("Petrol")

  def max_speed(self):
    print("Max Speed: 350\n")
  def luxurious(self):
    print("True")

class BMW:
  def fuel_type(self):
    print("Diesel")

  def max_speed(self):
    print("Max Speed is 240")

  def luxurious(self):
    print("True")

ferrari = Ferrari()
bmw = BMW()

# for car in (ferrari,bmw):
#   car.fuel_type()
#   car.max_speed()

# with functions and objects
def details(obj):
  obj.luxurious()
  obj.max_speed()

details(ferrari)
details(bmw)