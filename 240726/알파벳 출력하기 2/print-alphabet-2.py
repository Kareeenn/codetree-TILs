n = int(input())
a = ord('A')

for i in range(n):
    for j in range(i):
            print(" ", end=" ")
    for k in range(n-i):
        print(chr(a), end=" ")
        a += 1
        if a > ord('Z'):
            a = ord('A')
    print()