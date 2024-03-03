# https://atcoder.jp/contests/typical90/tasks/typical90_d
# 

"""
方針：横方向、縦方向それぞれの累積和を作る
その後、i(h), j(w)それぞれのリストの最後の値を足しあわせ、最後にgrid[i][j]を引く
"""
import copy

h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(map(int, input().split())))

h_s = copy.deepcopy(grid)
w_s = copy.deepcopy(grid)

# h_s：縦方向の累積和
for i in range(1, h):
    for j in range(w):
        h_s[i][j] += h_s[i-1][j]

# w_s：横方向の累積和
for i in range(h):
    for j in range(1, w):
        w_s[i][j] += w_s[i][j-1]

ans = [[None] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = w_s[i][-1] + h_s[-1][j] - grid[i][j]

for i in range(h):
    res = ""
    for j in range(w):
        if j != w-1:
            res += str(ans[i][j]) + " "
        else:
            res += str(ans[i][j])
    print(res)