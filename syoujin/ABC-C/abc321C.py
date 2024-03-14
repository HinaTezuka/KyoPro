k = int(input())
"""
combinationを使った解法
→自分で解いた時はこっちを使った
"""
p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

from itertools import combinations

a = []
for i in range(1, len(p)+1):
    for c in combinations(p, i):
        l = list(''.join(map(str, sorted(c, reverse=True))))
        if l not in a:
            a.append(int(''.join(l)))

a.sort()
print(a[k])

"""
bit全探索（解説見たらこれでも解けるっぽいからやってみる）
"""
mx = '9876543210'
len_mx = len(mx)
ans_candidates = []

for num in range(1<<len_mx):
    tmp = ''
    for shift in range(len_mx):
        if num >> shift & 1 == 1:
            tmp += mx[shift]
    if len(tmp) > 0:
        ans_candidates.append(int(tmp))

# ans_candidates = list(set(ans_candidates))
ans_candidates.sort()
print(ans_candidates[k])