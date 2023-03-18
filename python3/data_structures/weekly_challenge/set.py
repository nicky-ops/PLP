'''
program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets
'''

set1 = set()
items = int(input("Enter number of integers for the first set: "))
for i in range(0,items):
  u_input =(int(input("enter your integers: ")))
  set1.add(u_input)


set2 = set()
items = int(input("Enter number of integers for the second set: "))
for i in range(0,items):
  u_input =(int(input("enter your integers: ")))
  set2.add(u_input)

set3 = (set1&set2)
print(set3)