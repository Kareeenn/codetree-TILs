n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for k, char in enumerate(arr):
    if char == 2:
        cnt +=1
    if cnt == 3:
        print(k+1)
        break