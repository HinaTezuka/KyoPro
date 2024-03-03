# Consecutive
# https://atcoder.jp/contests/abc328/tasks/abc328_c

from itertools import accumulate

n, q = map(int, input().split())
s = input()
l = [None] * q
r = [None] * q

# 同じ文字が連続したときは（2文字目のindex）1, それ以外は0の配列を作る
same = [0] * len(s)
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        same[i] = 1
    else:
        same[i] = 0

# sameの累積和
acc = list(accumulate(same))

for i in range(q):
    l[i], r[i] = map(int, input().split())
    print(acc[r[i]-1] - acc[l[i]-1])