for i in range(1,6):
  print("Oya!")
print("")

i = 0
instructors = ["Nick", "Peter", "Debra", "Simon", "Sarah", "Duncan", "Jenny", "Theo", "Touker"]

for instructor in instructors:
  print(instructor)

while (i < len(instructors)):
  print(instructors[i])
  i += 1

# break and continue statements
# break terminates the loop
colors = ["blue", "green", "white", "yellow", "brown", "cream"]
choice = input("Enter choice of color: ").lower()

for color in colors:
  if color == choice:
    print("Done! ")
    break
  print(color)

count = 0
while count < len(colors):
  print(colors[count])

  if colors[count] == choice:
    print("DONE! ")
    break
  count += 1

# continue skips the current iteration
ages = [3,4,33,6,77,2,88,2,33,4,44,21,65]
for age in ages:
  if age < 21:
    continue
  print(age)



# nested loops
groups = [['Paul', "Mike", "Daniel"], ["Brian", "Sarah","Babra"]]

for group in groups:
  for name in group:
    print(name)