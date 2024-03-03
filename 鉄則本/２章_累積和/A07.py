d = int(input())
n = int(input())
R = [None] * n
L = [None] * n
for i in range(n):
    L[i], R[i] = map(int, input().split())

# 前日比の計算
ratio = [0] * (d+2)

for i in range(n):
    ratio[L[i]] += 1
    ratio[R[i]+1] -= 1

cumulationSum = [0] * (d+2) # 配列サイズは多めに設定しておかないとREになる可能性あり（実際なった。あと、append()もできればやめた方がいいかも。）
for i in range(1, len(ratio)):
    cumulationSum[i] = cumulationSum[i-1]+ratio[i]

for i in range(1, d+1):
    print(int(cumulationSum[i]))