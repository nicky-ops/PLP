class Vehicle:
  def vehicle_info(self):
    print("All vehicles have engines")

class Car(Vehicle):
  def car_info(self):
    print("Not all cars are automatic")

class SportsCar(Car):
  def sports_car_info(self):
    print("All sports cars are supercharged")

s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()