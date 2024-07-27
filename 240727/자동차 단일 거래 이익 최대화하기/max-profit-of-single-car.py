n = int(input())
arr = list(map(int, input().split()))
k = max(arr)- min(arr)
if k >= 0:
    print(k)
else:
    print(0)