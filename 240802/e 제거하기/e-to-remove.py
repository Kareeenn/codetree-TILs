k = input()

a = k.find('e')


k = k[:a] + k[a+1:]
print(k)