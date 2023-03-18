'''
program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
'''
words = ['Hello','Mike','John','Django','Microphone','Book','words','Milky','Mbuzi','Toto Wolf','Enigmatic']
lst = []
for word in words:
  if (len(word)%2 != 0):
    lst.append(word)

print(lst)