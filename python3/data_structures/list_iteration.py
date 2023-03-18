languages = ["Swift","Python","C++","Java"]
for language in languages:
  print(language)

print("C" in languages)
print("C++" in languages)

# length of list
print(len(languages))

# list comprehension
nums = [number*number for number in range(1,7)]
print(nums)

nums1 = []
for x in range(1,7):
  nums1.append(x * x)
