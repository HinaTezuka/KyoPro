n = int(input())
a = list(map(int, input().split()))
# s（最初の乗客数）を探索する方向に切り替える
s = 0
tot = 0
for i in range(n):
    tot += a[i]
    if s+tot < 0:
        s += abs(s+tot)

# print(s)
print(s+sum(a))