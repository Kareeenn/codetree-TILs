a,b = tuple(map(int, input().split()))

def king(a,b):
    a, b = min(a,b) +10 , max(a,b)*2
    return a,b

n, m = king(a,b)

print(f"{n} {m}")