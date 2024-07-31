arr = input()

arr2 = []

for i in range(1,len(arr),2):
    arr2.append(arr[i])

for a in arr2[::-1]:
    print(a, end="")