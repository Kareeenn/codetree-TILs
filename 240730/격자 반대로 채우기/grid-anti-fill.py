n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for j in range(n-1, -1, -1): #열
    if j%2 == 0: 
        # 정방향
        for i in range(n):
            arr[i][j]= num
            num += 1
    else:
        #역방향
        for i in range(n-1, -1, -1): #행
            arr[i][j] = num
            num += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= " ")
    print()