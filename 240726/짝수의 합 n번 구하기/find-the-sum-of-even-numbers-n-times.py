n = int(input())

for i in range(n):
    cnt = 0
    k = input()
    k = k.split()
    a, b = int(k[0]), int(k[1])
    if a%2 == 0: 
        for j in range(a,b+1, 2):
            cnt += j
    else:
        for j in range(a+1,b+1, 2):
            cnt += j
    print(cnt)