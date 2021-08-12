import random

compnum = random.randrange(1,101)
print("compnum : ", compnum)
guess = int(input("Enter a number : "))
trial = 1

while (compnum != guess):
    guess = int(input("Enter a number : "))
    trial += 1
    
print("Well done, you took %d attempts." %trial)