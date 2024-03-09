# 入力
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

import bisect

l = []
for i in range(N):
    for j in range(M):
        for k in range(L):
            l.append(A[i]+B[j]+C[k])

l.sort()
for i in X:
    idx = bisect.bisect_left(l, i)
    if idx < len(l) and l[idx] == i:
        print('Yes')
    else:
        print('No')