k = input().split()
a,b = int(k[0]), int(k[1])
arr = [0]*10

while a >1:
    cnt = a % b
    arr[cnt]+= 1
    a = a // b
sum = 0
for n in arr:
    sum += n**2
print(sum)