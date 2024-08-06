n, m = tuple(map(int, input().split()))

# 수열 A
A = list(map(int, input().split())) #n개의 원소

#m개의 두 숫자쌍 a1, a2
for i in range(m):
    a1, a2 = tuple(map(int, input().split()))
    k = a1 - 1
    sum = 0
    while k <= a2-1:
        sum += A[k]
        k += 1
    print(sum)