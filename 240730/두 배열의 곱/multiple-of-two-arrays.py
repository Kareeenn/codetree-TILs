arr1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

n = input()

arr2 = []
for _ in range(3):
    row =  list(map(int, input().split()))
    arr2.append(row)

for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j], end = " ")
    print()