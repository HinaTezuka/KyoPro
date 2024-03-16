import bisect
import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)
a.sort()

c = 0
while True:
    if n <= 1:
        c = 0
        break

    mn = heapq.heappop(a)
    mx = a[-1]
    
    if mx - mn <= 1:
        break

    heapq.heappush(a, mn + 1)
    mx_idx = bisect.bisect_left(a, mx)
    if mx_idx < len(a):
        a[mx_idx] -= 1
    
    c += 1

print(c)