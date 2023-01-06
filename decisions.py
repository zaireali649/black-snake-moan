import random

number = random.uniform(6,9)

print(number)

if(number < 7):
    print("Small number")
elif(number >= 8):
    print("Big number")
else:
    print("number is", number)