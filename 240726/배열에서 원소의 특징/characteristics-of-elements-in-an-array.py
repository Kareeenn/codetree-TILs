arr = list(map(int, input().split()))
h = len(arr)

for i in range(h):
    if arr[i]%3 == 0:
        print(arr[i-1])
        break