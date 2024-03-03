n, k = map(int, input().split())
a = list(map(int, input().split()))

# しゃくとり法
# left = 0(indexed)からスタート、a[right]-left <= k を満たしている間はright
# をインクリメント

right = 0
tot = 0
for left in range(n):
    while right < n-1 and a[right+1] - a[left] <= k:
        right += 1
    tot += right-left

print(tot)