def large_power(base, exponent):
  result = base ** exponent
  if result > 5000:
    return True
  else:
    return False
output = large_power(3, 3)
print(output)