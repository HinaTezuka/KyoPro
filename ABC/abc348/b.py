import math

n = int(input())

hmap = {}
l = []
for i in range(n):
    x, y = map(int, input().split())
    if i not in hmap:
        hmap[(x, y)] = i
    l.append((x, y))
print(hmap)
for i in range(n):
    ans = -10**9
    n1 = l[i]
    l2 = list(l[:i]+l[i+1:])
    # print(l2)
    for j in range(len(l2)):
        n2 = l2[j]
        k = math.sqrt(((n1[0]-n2[0])**2)+((n1[1]-n2[1]))**2)
        if k > ans:
            ans = hmap[n2]
    print(ans)