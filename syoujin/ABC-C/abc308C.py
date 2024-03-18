
# 綺麗ver.
from decimal import Decimal, getcontext
getcontext().prec = 100
N = int(input())
X = []
for i in range(N):
    a, b = map(Decimal, input().split())
    X.append((-a / (a + b), i))

X.sort()
print(*[i + 1 for x, i in X])

# 初見で解いたver.
from decimal import Decimal, getcontext
getcontext().prec = 100
n = int(input())

def culc_rate(a, b):
    return (a/(a+b))

res = {}

for i in range(1, n+1):
    a, b = map(Decimal, input().split())
    score = culc_rate(a, b)
    if score not in res:
        res[score] = [i]
    else:
        res[score].append(i)

ans = []
sorted_dict = dict(sorted(res.items(), key=lambda x: x[0], reverse=True))
for key, value in sorted_dict.items():
    ans.append(' '.join(map(str, value)))

print(*ans)