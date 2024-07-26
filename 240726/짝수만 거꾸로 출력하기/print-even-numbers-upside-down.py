n = int(input())

arr = list(map(int, input().split()))

even = list()

for e in arr:
    if e%2 == 0:
        even.append(e)

for fin in even[::-1]:
    print(fin, end=" ")