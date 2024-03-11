h, w = map(int, input().split())
S = []
for i in range(h):
    S.append(input())

z = [] # '#'の座標
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            z.append((i+1, j+1))

