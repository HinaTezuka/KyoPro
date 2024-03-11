# https://atcoder.jp/contests/abc333/tasks/abc333_c
# https://atcoder.jp/contests/abc333/editorial/7982


"""
最初に必要な範囲の全パターンのレピュニットをリストにいれて、
組み合わせ全探索。
ただ、解説の方が単純なので、そっちを参照（普通の全探索で解ける）。
"""
n = int(input())

re = [] # レピュニットパターン
r = 1
for i in range(12):
    re.append(r)
    re.append(r)
    re.append(r)
    r = int(str(r)+'1')

from itertools import combinations
res = []
for comb in combinations(re, 3):
    res.append(sum(comb))
print(sorted(set(res))[n-1])