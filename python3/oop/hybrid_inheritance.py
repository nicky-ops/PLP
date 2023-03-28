class Vehicle:
  def info(self):
    print("This is a vehicle")

class Car(Vehicle):
  def car_info(self, name):
    print(f"Car name is: {name}")

class Truck(Vehicle):
  def truck_info(self, name):
    print(f"Truck name is: {name}")

class SportsCar(Car, Vehicle):
  def s_car_info(self):
    print("inside sports car \n")


obj1 = SportsCar()
obj1.info()
obj1.car_info('Porsche')
obj1.s_car_info()

obj2 = Truck()
obj2.info()
obj2.truck_info('Kamaz')
