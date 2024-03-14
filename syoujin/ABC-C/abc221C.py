# https://atcoder.jp/contests/abc221/tasks/abc221_c
# https://atcoder.jp/contests/abc221/editorial/2720

"""
方針:
bit全探索で選ぶ数字の全通りを出す
→今回は順不同のため、その後順列全探索して、全パターンの
n1, n2(掛け合わせる2つの数）を探索し、積のmaxを求める
"""

from itertools import permutations

n = input()
k = len(n)

ans = 0
for num in range(1 << k):
    # 2つの数を初期化
    n1 = ''
    n2 = ''
    for shift in range(k):
        if num >> shift & 1 == 1:
            n1 += n[shift]
        else:
            n2 += n[shift]
    # ２つの数に分離できていない(000...0, 111...1など)ケースは排除
    if n1 == '' or n2 == '':
        continue

    # 順列全探索して掛け合わせる全パターンの数字（２つ）をつくり、積のmaxをもとめる
    for perm1 in permutations(n1):
        for perm2 in permutations(n2):
            n1 = ''.join(map(str, perm1))
            n2 = ''.join(map(str, perm2))
            # leading zeroははじく
            if n1[0] == '0' or n2[0] == '0':
                continue
            ans = max(ans, int(n1)*int(n2))

print(ans)

"""
より簡潔な解法:
積の最大値が答えなので、n1とn2を降順にソートして掛け合わせたものが各候補における最大値。
よって上のようにわざわざ順列全探索をする必要がない。
参考:https://qiita.com/sano192/items/61b815cb3e0ac494d504#c---select-mul
"""
n = input()
k = len(n)

ans = 0
for num in range(1 << k):
    # 2つの数を初期化
    n1 = ''
    n2 = ''
    for shift in range(k):
        if num >> shift & 1:
            n1 += n[shift]
        else:
            n2 += n[shift]
    # ２つの数に分離できていない(000...0, 111...1など)ケースは排除
    if n1 == '' or n2 == '':
        continue
    n1 = sorted(n1, reverse=True)
    n2 = sorted(n2, reverse=True)
    ans = max(ans, int(''.join(map(str, n1)))*int(''.join(map(str, n2))))

print(ans)


# 綺麗な解答(解説参照：https://atcoder.jp/contests/abc221/editorial/2720)
N = sorted(input(),reverse=True)
ans = 0
for i in range(1<<len(N)):
    l = 0
    r = 0
    for j in range(len(N)):
        if i & (1<<j):
            l = l*10+ord(N[j])-ord('0')
        else:
            r = r*10+ord(N[j])-ord('0')
    ans = max(ans,l*r)
print(ans)