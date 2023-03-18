# for loop
fruits = {"Mangoes","Apples","Peach","Oranges","Pinneaples","Guavas"}
for fruit in fruits:
  print(fruit)

# len method
even_nums = {2,4,6,8}
print(f'Set: {even_nums}')
print(f"Total Elements: {len(even_nums)}")

'''
  SET OPERATIONS
'''
# union of two sets
a = {66, 7,7,3,2,5,6}
b = {6,27,7,34,22,77,5}

print(f'Union: {a|b}')
print(f"Union: {a.union(b)}")

# set intersection
print(f"Intersection: {a&b}")
print(f"Intersection: {a.intersection(b)}")

# set difference
print(f"Difference: {b - a}")
print(f"Difference: {a.difference(b)}")

# symmetric difference
print(f"symmetric diff: {a^b}")
print(f"symmetric difference: {a.symmetric_difference(b)}")

# check if two sets are equal
if a == b:
  print("Equal")
else:
  print("Not Equal")
