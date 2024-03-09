# https://atcoder.jp/contests/abc335/tasks/abc335_c
# https://atcoder.jp/contests/abc335/editorial/9026
"""
両端キューで座標を管理する
以下、解説より、
Pythonではdequeに対する添え字アクセスが遅い
(C++だとACするけど、Pythonだとむり)
「Python など、deque に対する添字アクセスが高速でない言語では、
配列をリバースし「先頭の要素を取り除く」処理を実際には行わない
ことで、すべての処理を高速に行うことができます。」

反省:dequeを使うことを思いつくまでに時間かかりすぎ。。。
"""
from collections import deque
import copy

# 各点の座標情報を更新
def command(c, xy) -> list:
    if c == 'R':
        xy[0] +=1
    if c == 'L':
        xy[0] -=1
    if c == 'U':
        xy[1] +=1
    if c == 'D':
        xy[1] -=1
    return xy

n, q = map(int, input().split())
Q = deque([i, 0] for i in range(1, n+1))

for i in range(q):
    x, c = map(str, input().split())
    if x == '1':
        head = copy.deepcopy(Q[0])
        new = command(c, head)
        Q.appendleft(new)
        Q.pop()
    else:
        c = int(c)
        print(Q[c-1][0], Q[c-1][1])


# 綺麗な回答(上にも書いた通り、Pythonでdequeを使っても間に合わない)
N, Q = map(int, input().split())
A = [(i+1,0) for i in range(N)][::-1]

for _ in range(Q):
  T, C = input().split()
  if T == "1":
    x, y = A[-1]
    if C == "U": y += 1
    if C == "D": y -= 1
    if C == "R": x += 1
    if C == "L":  x-= 1
    A.append((x,y))
  else:
    print(*A[-int(C)])