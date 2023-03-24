#  a function is a modular piece of code that can be used repeatedly. It allows for abstraction. It has a return value
# *args arbitrary arguments returns a tuple of arguments
# **kwargs arbitrary keyword arguments 
def addition(*args):
  sum = 0
  for item in args:
    sum += item
  print(sum)

addition(9,3,3,4,5,6,4,43,3)


def sum_age(**age):
  sum = 0
  for k, v in age.items():
    sum += v
  return sum
print(f"Total: {sum_age(mutemi = 23, skinny = 88, ahmed = 54)}")