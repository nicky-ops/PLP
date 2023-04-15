# reading line(s) from a file
file = open("requirements.txt", "r")
x = file.readline()
print(x)
y = file.readlines()
print(y)

file.close()