# python strings are immutable
greeting = "Hello"
print(greeting[2])
print(greeting[0:2])

# multiline string
chant = '''
This is my rifle this is my gun, this is for fighting this is for fun!
'''
print(chant)

# compare two strings
str1 = "Hello World"
str2 = "Hello World"
print(str1 == str2)

# concatenate strings
print(str1 + str2)

# iterate through a string
for letter in str1:
  print(letter)

# string membership
print('This' in chant)

# upper method
print(chant.upper())

# lower method
print(chant.lower())

# partition method
print(chant.partition('is'))

# rstrip() removes trailing characters
print(chant.rstrip())

# split method
print(chant.split())

# isnumeric method
print(chant.isnumeric())

# index method
print(chant.index("This"))

# escape character /
print('He said, "What\'s there?"')
print('\ooo')