import random
min = 1
max = 6
rollagain = "yes"
while rollagain=="yes":
    print("The dice has 6 sides")
    print("The value of dice")
    print(random.randint(min,max))
    rollagain = input("Roll the dice again?   ")
