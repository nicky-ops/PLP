'''
program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
'''
info = {}
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_color = input("Enter your favourite color: ")

info['name'] = name
info['age'] = age
info['favourite color'] = fav_color

print(info)