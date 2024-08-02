a = input()

arr = list(a)

m = a[0]
n = a[1]

for i in range(len(arr)):
    if arr[i] == n:
        arr[i] = m
a = ''.join(arr)
print(a)