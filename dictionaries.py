var = {}

print(var)
print(type(var))

var_2 = {"fruit": "apple", "juice":"cranberry"}

print(var_2)

var_2["drank"] = "tequila"

print(var_2)

var_2["drank"] = "purple drank"

print(var_2)

del var_2["drank"]

print(var_2)

print(dir(var_2))

print(list(var_2.keys()))
print(list(var_2.values()))

for key, value in var_2.items():
    print(key, value)
    
var_2["dranks"] = ["tequila", "purple drank", "vodka"]

for key, value in var_2.items():
    print(key, value)
    
for drank in var_2["dranks"]:
    print(drank)
    
print(var_2["dranks"][1]) # How would you print a specific element within a list that's in a dictionary?