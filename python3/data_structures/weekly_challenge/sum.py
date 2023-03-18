'''
this program accepts user input and stores it in a list then sums all the integers in the list
'''
lst = []
sum = 0
items = int(input("Enter the number of integers: "))
for i in range(0,items):
  lst.append(int(input("Enter   a number ")))
  sum +=lst[i]
print(sum)

