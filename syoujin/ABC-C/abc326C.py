# https://atcoder.jp/contests/abc326/tasks/abc326_c
# https://atcoder.jp/contests/abc326/editorial/7537

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
a.append(9000000000000)

res = 0
r = 0
for l in range(0,n):
    while a[r] < a[l]+m:
        r += 1
    res = max(res,r-l)

print(res)