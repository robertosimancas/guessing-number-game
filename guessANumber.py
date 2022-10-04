import random
n = random.randrange(1,10)
number = int(input("Enter any number: "))
while n!= number:
    if number < n:
        print("Too low")
        number = int(input("Enter number again: "))
    elif number > n:
        print("Too high!")
        number = int(input("Enter number again: "))
    else:
      break
