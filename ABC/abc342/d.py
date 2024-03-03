n = int(input())
import math

a = list(map(int, input().split()))

last = a[-1]

c = 0
for i in range(1, n+1):
    if a[i-1] == 0: continue
    h = i**i
    for j in range(1, math.floor(math.sqrt(h))):
        if h / j in (a[:i-1]+a[i:]):
            c += 1

print(c)