k = list(map(int, input().split()))
n, m = k[0], k[1]

def guess_min(n,m):
    a = 1
    cnt = 0
    x, y = 0, 0
    for i in range(1, min(n,m)+1):
        x = n % i 
        y = m % i
        if x == 0 and y == 0:
            n = n // i
            m = m // i
            cnt += 1
            a = a*i
    a = a*x*y
    print(a)

guess_min(n,m)