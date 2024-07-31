k = input().split()
n, m = int(k[0]), int(k[1])
arr = []

for _ in range(m):
    arr.append(tuple(map(int, input().split())))

arr2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i, j) in arr: #헷갈림
            arr2[i-1][j-1] = i*j

for i in range(n):
    for j in range(n):
        print(arr2[i][j], end =" ")
    print()