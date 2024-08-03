a = list(input())
b = list(input())

arr= []
arr2 = []

for n in a:
    if n.isdigit():
        arr.append(n)

for n in b:
    if n.isdigit():
        arr2.append(n)
        
arr = int(''.join(arr))
arr2 = int(''.join(arr2))

print(arr+arr2)