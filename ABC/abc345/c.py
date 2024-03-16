import sys
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

S = input()
if len(set(S)) == 1:
    print(1)
    sys.exit()

cnt = {}
for s in S:
    if s not in cnt:
        cnt[s] = 1
    else:
        cnt[s] += 1

d = 0
for key, value in cnt.items():
    if value != 1:
        d += value-1

print(cmb(len(S), 2) - d)