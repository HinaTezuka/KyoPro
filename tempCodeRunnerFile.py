from decimal import Decimal, getcontext
from re import T
getcontext().prec = 100

n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

res = {}

for i in range(1, n+1):
    a, b = map(int, input().split())
    d = a/(a+b)
    if d not in res:
        res[d] = [i]
    else:
        res[d].append(i)

res = dict(sorted(res.items(), reverse=True))
ans = ''
for key, value in res.items():
    ans += str(''.join(map(str, value)))

print(*ans)