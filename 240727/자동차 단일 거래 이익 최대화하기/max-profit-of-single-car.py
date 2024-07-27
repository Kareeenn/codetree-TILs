n = int(input())
arr = list(map(int, input().split()))

#k = max(arr)- min(arr)
#팔기(i) - 사기(j)
#사기가 더 먼저
if n >1:
    k = arr[1]-arr[0]
#print(len(arr))

for i in range(1,n): #팔기
    #print(i)
    for j in range(0, i):
        #print(f"{k} = arr[{i}] - arr[{j}]")
        #print(f"{k} = {arr[i]} - {arr[j]}") #사기
        if k < (arr[i] - arr[j]):
            k = arr[i] - arr[j]


if k >= 0:
    print(k)
else:
    print(0)