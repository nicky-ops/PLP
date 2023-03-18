'''
1. tuple is immutable
2. a tuple can have any number of items and they may be of different types i.e. integer, float, list, string., etc.
'''

instructors = ("Jenny","Peter","Duncan","Sarah","Debra","Theo","Touker","Nick","Tej")
print(instructors)
print(instructors[4])
print(instructors[-3])

'''
when creating a tuple with one element, include a trailing comma before the crossing parenthesis
'''
var = ("East",)

# slicing
age = (2,4,5,6,7,4,42,6,77,2,2,2,2,2,2,2)
print(age[4:5])

# tuple methods
print(age.count(2))
print(age.index(6))
