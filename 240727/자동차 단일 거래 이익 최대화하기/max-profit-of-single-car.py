n = int(input())
arr = list(map(int, input().split()))

if n <= 1:
    print(0)
else:
    k = arr[1] - arr[0]

    for i in range(1, n): # 팔기
        for j in range(0, i): # 사기
            if k < (arr[i] - arr[j]):
                k = arr[i] - arr[j]

    if k >= 0:
        print(k)
    else:
        print(0)