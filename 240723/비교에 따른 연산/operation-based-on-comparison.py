k = input()
k = k.split()
a = int(k[0])
b = int(k[1])

if a>b:
    print(a*b)
else:
    print(b//a)