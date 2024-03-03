# https://atcoder.jp/contests/abc112/tasks/abc112_c

"""
制約から、0 <= Cx, Cy <= 100なので、これを元に全探索して、
各i, jを問題文中のmax()の式に代入する。
その上で、座標Xi, Yiとそれに対する高度hの情報をテストケースとして使い、
hに一致するものがあればそれが答え？
"""

n = int(input())
x = [None] * n
y = [None] * n
h = [None] * n
for i in range(n):
    x[i], y[i], h[i] = map(int, input().split())

"""
問題文より、(Xi, Yi)の高度はmax(H - |Xi-Cx| - |Yi-Cy|, 0)
仮にH - |Xi-Cx| - |Yi-Cy| > 0だった場合、
H - |Xi-Cx| - |Yi-Cy| = hiということ。変形して、
H = hi + |Xi-Cx| + |Yi-Cy|となる。これを元にHを求める
"""

H = 1
ans = ""
for Cx in range(101):
    if ans != "": break
    for Cy in range(101):
        if ans != "": break
        for i in range(n):
            # 仮にH - |Xi-Cx| - |Yi-Cy| > 0だった場合、
            # H - |Xi-Cx| - |Yi-Cy| = hiより、変形して
            if h[i] > 0:
                H = h[i] + abs(x[i] - Cx) + abs(y[i] - Cy)
                if H < 1: break
                koudo = max(H - abs(x[i]-Cx) - abs(y[i]-Cy), 0)
            else:
                koudo = 0
            if i == n-1:
                ans = str(Cx) + " " + str(Cy) + " " + str(H)
                break
            if h[i] == koudo: continue
            else: break

print(ans) 