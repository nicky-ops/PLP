# Data types in python

# int data type
num = 33
print('variable num, is a',type(num))

# float data type
price = 1.99
print('variable price, is a',type(price))

# complex data type
vector = 3+1j
print('variable vector, is a',type(vector))

#list
cars = ['BMW', 'Rolls Royce','Skoda','Mercedes','Toyota','Dodge']
print("variable cars is a", type(cars))

#tuple - cannot be modified
vehicles = ('BMW', 'Rolls Royce','Skoda','Mercedes','Toyota','Dodge')
print('variable vehicles is a ',type(vehicles))

#set - ordered
motor_vehicle = {10,11,28,1,88,77,3,6,5,44,3,60,1,5,8887,5,5,}
print(motor_vehicle);
print("Variable motor_vehicle is a", type(motor_vehicle))

#dictionary
animal = {
  'name':'Zepphyrr',
  'sound': 'meouw',
  'class': 'cat family',
  'age': 3
}
print(animal['name'])
print("variable animal is of",type(animal))

#string
message = "Never Give Up!"
print('variable message is of', type(message))
print('\n', message)