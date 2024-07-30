n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

#n = 짝수
if n % 2 == 0:
    for j in range(n-1, -1, -1): #열
    # n = 홀수면, 짝수가 역방향 / n = 짝수면, 짝수가 정방향
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
else:
    for j in range(n-1, -1, -1): #열
# n = 홀수면, 짝수가 역방향 / n = 짝수면, 짝수가 정방향
        if j%2 != 0: 
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