a = input()
b = input()
n= 0

for i in range(len(a)):
    a = a[len(a)-1:] + a[:len(a)-1]
    n += 1
    if a == b:
        print(n)
        break
    else:
        if i == len(a)-1:
            print(-1)