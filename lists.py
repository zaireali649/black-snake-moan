var = []

print(var)
print(type(var))

var_2 = [151, 251, 386, 493, "009"]

print(var_2)

var_2.append(649)

print(var_2)

#print(dir(var_2))

numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number*number)
    
numbers2 = list(range(0,100))

print(numbers2)

print(len(numbers2))

print(numbers2[50])

var_3 = []

var_3.append(list(range(0,10)))
var_3.append(list(range(10,20)))
var_3.append(list(range(20,30)))

print(var_3)

for x in var_3:
    print(x)
    for y in x:
        print(y)