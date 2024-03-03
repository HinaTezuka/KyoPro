n = int(input())
a = map(int, input().split())
s = [None] * (n-1)
t = [None] * (n-1)
for i in range(n-1):
    s[i], t[i] = map(int, input().split())

# a[n-1]を最大にする
# a[n-1]を増やすにはa[n-2]を支払うしかない。
# a[n-1]を最大にする <- a[n-2]を最大にするということ。 <- a[n-3]を最大にするということ。 <- ....
# なお、A[1]は無視していい。A[1]を増やすことはできない。

# 通貨交換操作を行う関数
def implement(a, next, s, t) -> list:
    result = []
    if a >= s:
        a -= s
        result.append(next+t)
    return result