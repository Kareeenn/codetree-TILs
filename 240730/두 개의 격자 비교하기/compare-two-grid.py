k = input().split()
n, m = int(k[0]), int(k[1])

# 배열 입력
arr1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

#배열 2입력
arr2 = [
    list(map(int, input().split()))
    for _ in range(n)
]



#출력물
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()