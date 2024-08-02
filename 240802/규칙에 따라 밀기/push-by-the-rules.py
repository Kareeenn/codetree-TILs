k = input()
n = input()

for i in n:
    if i == 'L':
        k = k[+1:] + k[:+1]
    else:
         k = k[-1:] + k[:-1]



print(k)

# 이런 반례
#qebh
#LLLLL