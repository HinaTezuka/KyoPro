H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

# グリッド上の陸（.）の座標を格納
# 外周は必ず海なので無視
riku = [] # 陸のマスの座標を（i, j）として格納
for i in range(1, H):
    for j in range(1, W-1):
        if S[i][j] == '.':
            riku.append((i, j))

# L,R,U,Dそれぞれの操作をする関数
# r=現在地の座標(tuple)、s=操作の文字
def move(r, s) -> tuple:
    result = ()
    if s == 'L': result = (r[0], r[1]-1)
    elif s == 'R': result = (r[0], r[1]+1)
    elif s == 'U': result = (r[0]-1, r[1])
    elif s == 'D': result = (r[0]+1, r[1])
    return result

# 答えを求める
c = 0
for i in range(len(riku)):
    current = (riku[i][0], riku[i][1]) # 現在地の座標
    for j in range(len(T)):
        if S[current[0]][current[1]] == '#':
            break
        current = move(current, T[j])
        if j == len(T)-1 and S[current[0]][current[1]] != '#':
            c += 1
            break
print(c)