'''
set collection of unique data
set has no particular order hence indexing has no meaning
'''

# empry set
empty_set = set ()
print(type(empty_set))

# no duplicates
my_set = {5,5,5,5,5,5,5,5,5}
print(my_set)

# add method - add items to a set
numbers = {5,6,7,11,233,54,3}
print(f'INITIAL SET: {numbers}')
numbers.add(558)
print(f"UPDATED SET: {numbers}")

# UPDATE METHOD - update set with items other collection types
companies = {'Safaricom', 'LockHeed Martin','Jumia','Centum Investmentse','Cytonn Group'}
tech_giants = ['Apple','Alphabet','Facebook', 'Amazon','AT&T']
companies.update(tech_giants)
print(companies)

manufacturing = {
  'USA' : 'Tesla Inc',
  'INDIA' : 'Mahindra',
  'SWEDEN' : 'Volvo',
  'GERMANY' : 'BMW'
}
companies.update(manufacturing)
print(companies)

# discard method
companies.discard('LockHeed Martin')
print(companies)

# all method
print(all(companies))

# any method
print(any(companies))

# enumerate
print(enumerate(numbers))

# len method
print(len(companies))

# max method
print(max(companies))

# min method 
print(min(companies))

# sorted method
print(sorted(companies))

# sum method
companies = {4,6,7,8,7}
print(sum(companies))