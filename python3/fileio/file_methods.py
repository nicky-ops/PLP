# read method
file = open('requirements.txt', "r")
content = file.read()
print(content)

# write method
file1 = open('myfile.txt', 'w')
content1 = file1.write("I wrote to this file using the write method")
file1 = open('myfile.txt', 'r')
contents1 = file1.read()
print(contents1)

# seek method
content2 = file1.seek(1, 0)
print(content2)

# tell method
print(file1.tell())

# file object methods
print(file.name)
print(file.closed)
print(file.mode)
print(type(file))

# closing a file
file.close()
file1.close()
print(file.closed)
print(file1.closed)
