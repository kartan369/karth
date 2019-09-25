import random
min = 1
max = 6
a=b=c=0
roll_again = "yes"
while roll_again == "yes":
    print("Rolling the dices...")
    print("The values are....")
    a = random.randint(min, max)
    b = random.randint(min, max)
    print(b)
    print(a)
    c = a+b
    if c%2==0:
        print("c is an even number ",(c))
        exit()
    elif c%2==1:
        print("c is an odd number",(c))
