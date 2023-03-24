# function without a name

snack = lambda : print("Njugu")
snack()

square = lambda num : print(num ** 2)

square(9)

def isPalindrome(string):
  if (string == string[::-1]):
    print("A Palindrome ")
  else:
    print ("Not a palindrome")

string = input("enter a string ")

isPalindrome(string)