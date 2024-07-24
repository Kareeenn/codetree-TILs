n = int(input())

for i in range(n):
    print("*", end="")
    for j in range(1, i+1):
        print("**", end="")
    print()