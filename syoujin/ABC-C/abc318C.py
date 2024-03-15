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

# 与えられたリストを降順にソート
f = sorted(f, reverse=True)
# fの累積和
f_sum = copy.deepcopy(f)
for i in range(1, len(f)):
    f_sum[i] += f_sum[i - 1]

tot = 10**20
for i in range(1, (pass_tot)):
    tot = min(tot, f_sum[-1]-f_sum[(i*d)-1]+(i*p))
