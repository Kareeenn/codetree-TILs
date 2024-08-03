n = int(input())
cnt = 0

for i in range(n):
    cnt += int(input())

n= str(cnt)

n = n[1:] + n[:1]
print(n)