n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    #시작 
    for k in range(i):
        print("*", end=" ")
    print()
    
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    #시작 
    for k in range(i):
        print("*", end=" ")
    print()