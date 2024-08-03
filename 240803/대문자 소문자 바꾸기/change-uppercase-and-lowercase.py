n = input()
n = list(n)

for i in range(len(n)):
    if 'A' <= n[i] and n[i] <= 'Z':
        n[i] = n[i].lower()
    else:
        n[i] = n[i].upper()
n = ''.join(n)
print(n)