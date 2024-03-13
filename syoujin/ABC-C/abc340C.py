# https://atcoder.jp/contests/abc340/tasks/abc340_c
# https://scrapbox.io/kyopronikki/abc340_C_-_Divide_and_Divide_(ABC-C_%3E_abc340C.py)

import sys
sys.setrecursionlimit(10**6)

n = int(input())

nums = [n]
tot = 0
cache = {}
cache2 = {} # dpっぽく

def solve(x, nums, tot, cache, cache2):
    if x in cache2.keys():
        return tot+cache2[x]
    if len(nums) == 0:
        return tot
    x = nums.pop(0)
    tot += x
    if x in cache.keys():
        n1 = cache[x][0]
        n2 = cache[x][1]
    else:
        n1 = x//2
        n2 = 0
        if (x/2) % 1 == 0:
            n2 = (x//2)
        else:
            n2 = (x//2)+1
        cache[x] = [n1, n2]
    if n1 >= 2:
        nums.append(n1)
    if n2 >= 2:
        nums.append(n2)

    return solve(x, nums, tot, cache, cache2)

ans = 0
for i in range(2, n+1):
    cache2[i] = solve(i , nums, tot, cache, cache2)
    ans += cache2[i]
print(ans)