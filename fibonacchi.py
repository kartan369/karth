def f(i):
    if(i <= 1):
        return i
    else:
        return (f(i-1) + f(i-2))

i = int(input("Enter the number:"))

print("Fibonacci sequence for :")
for n in range(i):
    print(f(n))
