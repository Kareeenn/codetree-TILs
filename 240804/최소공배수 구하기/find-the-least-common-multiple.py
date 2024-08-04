k = list(map(int, input().split()))
n, m = k[0], k[1]

def guess_min(n,m):
    a = 1
    cnt = 0
    x, y = 0, 0
    i = 2
    while i <= min(n,m):
        x = n % i 
        y = m % i
        if x == 0 and y == 0:
            n = n // i
            m = m // i
            cnt += 1
            a = a*i
            # 같은 i로 실행되게 해야 돼
        else:
            i += 1
    #print(f"{a} * {n} * {m}")
    a = a*n*m
    print(a)

guess_min(n,m)