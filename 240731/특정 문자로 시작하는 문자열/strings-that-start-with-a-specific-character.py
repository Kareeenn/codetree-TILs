n = int(input())

arr = [
    input()
    for _ in range(n)
]

k = input()

count = 0
sum = 0

for a in arr:
    if a[0] == k:
        count += 1
        sum += len(a)

avg = sum / count

print(f"{count} {avg:.2f}")