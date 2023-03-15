var = [5,6,7,"Hello", "World"]

print(var)
print(var[0],var[-1])

# slicing a list
languages = ['Swift',"Python","Java","Objective C","Go","Javascript","Dart","PHP","RUST","C","C++"]

print(languages[0:3])

# list methods
languages.append("Kotlin")
print(languages[-1])

# extend method
prime_numbers = [2,3,5,7]
even_numbers = [2,4,6,8,10]

even_numbers.extend(prime_numbers)
print(even_numbers)

# del method
del even_numbers[0:2]
print(even_numbers)

# remove method
languages.remove("Objective C")
print(languages)

# pop method
languages.pop(1)
print(languages)

# clear method
even_numbers.clear()
print(even_numbers)