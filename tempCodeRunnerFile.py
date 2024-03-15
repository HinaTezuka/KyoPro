from itertools import combinations
import copy

n, d, p = map(int, input().split())
f = list(map(int, input().split()))

# 全ての日程で通常料金を使用した場合
all_normal = sum(f)

# 全ての日程で周遊パス
pass_tot = 0 # 周遊パスの枚数
if n % d != 0:
    pass_tot = int(n / d + 1)
else:
    pass_tot = n // d
all_amount = pass_tot*p # 合計金額

# 与えられたリストを降順にソートする
f = sorted(f, reverse=True)
# fの累積和を計算する
f_sum = copy.deepcopy(f)
for i in range(1, len(f)):
    f_sum[i] += f_sum[i - 1]
# print(f_sum)

tot = 10**20
# for i in range(d, (pass_tot-1)*d):
#     for c in combinations(f, i):
#         tot = min(tot, sum(c)+round((n-i)/d)*p)

# f.sort()
for i in range(1, (pass_tot-1)*d):
    if i < d: n = 1
    else: n = i // d
    tot = min(tot, f_sum[-1]-f_sum[i]+(n*p))

print(min(tot, all_amount, all_normal))