a = [10,2,4]
b = [1,5,7,3,8,9]
if len(a) < len(b):
    c = b.copy()
    c[:len(a)] += a
else:
    c = a.copy()
    c[:len(b)] += b

print(c)
