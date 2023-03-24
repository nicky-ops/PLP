# local scope - variable declared inside a function i.e. variable sum below
def add_nums(a,b):
  sum = a + b 
  print(sum)
add_nums(4,5)

# enclosing scope - is a nested function i.e. double_it() below
def difference(a,b):
  ans = a - b
  def double_it():
    double = ans * 2
    print (double)
  double_it()
  print(ans)

difference(8, 4)

# global scope variable declared outside a function
global_code = 12
def phones(a,b):
  index = a ^ b + global_code
  print(index)

phones(4, 6)

# built in scope
'''
the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth. Functions with built-in scope can be accessed at any level.
'''