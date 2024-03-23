n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

import bisect

k_id = bisect.bisect_left(a, k)
a_sum = 0
if a[k_id] == k:
    a_sum = sum(a[:k_id+1])
else:
    a_sum = sum(a[:k_id])


k_sum = k*(k+1)//2

print(k_sum - a_sum)
