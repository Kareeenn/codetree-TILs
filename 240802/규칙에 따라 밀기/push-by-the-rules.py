k = input()
cnt = 0 
n = input()

cnt = n.count('R') - n.count('L')

#cnt만큼 밀어야 돼

if cnt<0:
    k = k[-cnt:] + k[:-cnt]
else:
    k = k[-cnt:] + k[:-cnt]
print(k)