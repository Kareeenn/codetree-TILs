input = input()
input = input.split()
a = int(input[0])
b= int(input[1])
c = int(input[2])

if a>b and a>c: 
    if b>c:
        print(b)
    else:
        print(c)
elif b>c and b>a:
    if c>a:
        print(c)
    else:
        print(a)
else:
    if a>b:
        print(a)
    else :
        print(b)