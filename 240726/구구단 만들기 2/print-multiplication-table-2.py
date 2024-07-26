k = input()
k = k.split()
a = int(k[0])
b = int(k[1])
c = b

for i in range(2,9,2):
    while c >= a:
        if c > a:
            print(f"{c} * {i} = {c*i}", end=" / ")
        else:
            print(f"{c} * {i} = {c*i}", end=" ")
        c -= 1
    print()
    c = b