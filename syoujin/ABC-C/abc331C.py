import bisect
import copy

n = int(input())
a = list(map(int, input().split()))

# cumulative sum
sorted_a = copy.deepcopy(a)
sorted_a.sort()
a_sum = copy.deepcopy(sorted_a)
for i in range(1, n):
    a_sum[i] += a_sum[i-1]

ans = []
for i in range(1, n+1):
    idx = bisect.bisect_right(sorted_a, a[i-1])
    ans.append(a_sum[-1]-a_sum[idx-1])
print(*ans)