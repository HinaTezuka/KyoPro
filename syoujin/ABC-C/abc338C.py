N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**18

ans = 0
for x in range(max(Q) + 1):
    y = INF
    for i in range(N):
        if Q[i] < A[i] * x:
            y = -INF
        elif B[i] > 0:
            y = min(y, (Q[i] - A[i] * x) // B[i])
    ans = max(ans, x + y)
print(ans)

# 自分で解いたver.
# n = int(input())
# q = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# # Aで固定して全探索

# # 料理Aの作れる最大人数を探索
# max_a = 10**9
# for i in range(n):
#     if a[i] > 0:
#         max_a = min(max_a, q[i] // a[i])

# # max_aを元にbの最大人数、ansを探索
# ans = 0
# for i in range(max_a+1):
#     b_num = 10**9
#     for j in range(n):
#         if b[j] > 0:
#             b_num = min(b_num, (q[j] - (a[j]*i)) // b[j])
#     ans = max(ans, i+b_num)

# print(ans)