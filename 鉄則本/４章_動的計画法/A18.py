# NとSをそれぞれ分解する←２次元DP
n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s+1) for _ in range(n+1)]
dp[0][0] = True

# i枚までのカードの組み合わせで、jになるものがあればTrueにしていく
# -> i-1枚目までの時点でjになる組み合わせがある or A[i]を足せばjになるパターン
for i  in range(1, n+1):
    for j in range(s+1):
        if j < a[i-1] and dp[i-1][j] == True: dp[i][j] = True
        elif j >= a[i-1]:
            if dp[i-1][j] == True or dp[i-1][j-a[i-1]] == True:
                dp[i][j] = True

print('Yes') if dp[n][s] == True else print('No')