import os 
filename = 'deleted'
if os.path.exists(filename):
  os.remove(filename)
  print(f"{filename} has been deleted. ")
else:
  print(f"{filename} does not exist")

file = open('os.py', 'r')
content = file.read()
