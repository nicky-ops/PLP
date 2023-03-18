capital_cities = {
  "Kenya"  : "Nairobi",
  "Uganda" : "Kampala",
  "Rwanda" : "Kigali",
  "Italy"  : "Rome",
  "England": "London"
}
print(capital_cities)

rationale = {
  3 : "Neigh",
  5 : "Collossal",
  6 : "Punt",
  7 : "Smoke",
  9 : 404
}
print(f"INITIAL DICTIONARY: {rationale}")
rationale[4] = "Abject"
rationale[7] = "Superb"
print(f"UPDATED DICTIONARY: {rationale}")

# del method
del rationale[3]
print(rationale)

# accessing elements in a dictionary
print(rationale[9])

# all method
print (all(rationale))
# any method
print(any(rationale))

# len method
print(len(rationale))

# sorted method
print(sorted(rationale))

# clear method
indices = {
  5 : 5,
  6 : 9,
  9 : 10
}
print(f"INDICES BEFORE CLEAR: {indices}")
indices.clear()
print(f"INDICES AFTER CLEAR: {indices}")

# keys method 
print(rationale.keys())

# values method
print(rationale.values())

# keys membership test
print(5 in rationale)
print(9 in rationale)

# iterating through a dictionary
for i in rationale:
  print(rationale[i])

