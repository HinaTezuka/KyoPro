import sys
import copy

n, c = map(int, input().split())
a = list(map(int, input().split()))
# 累積和
c_sum = copy.deepcopy(a)
for i in range(1, n):
    c_sum[i] += c_sum[i-1]

# cが正負のどちらか
isCMinus = False if c > 0 else True
lis = copy.deepcopy(a)
lis.sort()
# 全ての要素が負
isAllMinus = False
isAllOver = False
if lis[-1] < 0:
    isAllMinus = True
elif lis[0] >= 0:
    isAllOver = True
if isAllMinus and isCMinus:
    tot = 0
    for i in range(n):
        a[i] *= c
        tot += a[i]
    print(tot)
    sys.exit()
if isAllMinus and not isCMinus:
    print(c_sum[-1])
    sys.exit()

# 全ての要素が正の場合
if isAllOver and not isCMinus:
    tot = 0
    for i in range(n):
        a[i] *= c
        tot += a[i]
    print(tot)
    sys.exit()
elif isAllOver and isCMinus:
    print(c_sum[-1])
    sys.exit()

# 正負が混在している場合

sum_a = c_sum[-1] # 1回も操作をしない場合 

def multiply_elements_in_range(start_idx, end_idx, multiplier):
    return (c_sum[start_idx-1])+((c_sum[end_idx]-c_sum[start_idx-1])*multiplier)+(c_sum[-1]-c_sum[end_idx])

mi = []
pl = []
for i in range(n):
    if a[i] > 0: pl.append(i)
    else: mi.append(i)

ans = -10**18

# from itertools import combinations
# # a = list(set(a))
# # l = [x for x in range(int(n))]
# if c >= 0:
#     for co in combinations(pl, 2):
#         ans = max(ans, multiply_elements_in_range(co[0], co[1], c))
# elif c < 0:
#     for co in combinations(mi, 2):
#         ans = max(ans, multiply_elements_in_range(co[0], co[1], c))

if c >= 0:
    for i in range(len(pl)):
        for j in range(i, len(pl)):
            ans = max(ans, multiply_elements_in_range(pl[i], pl[j], c))
else:
    for i in range(len(mi)):
        for j in range(i, len(mi)):
            ans = max(ans, multiply_elements_in_range(mi[i], mi[j], c))

print(ans) if ans > sum_a else print(sum_a)