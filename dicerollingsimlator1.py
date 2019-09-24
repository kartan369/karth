import random
min = 1

roll_again = "yes"

while roll_again == "yes":
    sides = input("Number of sides of the dices  ")
    max = int(sides)
    if max <= 0:
        print("The given input is not valid")
        print("Please enter a new number   ")
    else:
        print("The value is....")
        print(random.randint(min, max))
        roll_again = input("Roll the dice again?    ")
