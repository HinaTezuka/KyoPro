import sys
sys.setrecursionlimit(10**6)

n = int(input())
G = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 小さい順に回らなきゃなのでG[i]をsortしておく
for i in range(n+1):
    G[i].sort()

def dfs(now, pre) -> None:
    visited.append(now)
    for edge in G[now]:
        if edge != pre: # edge!=preなので、どんどん奥へ進んでいく
            dfs(edge, now)
            visited.append(now)

visited = []
dfs(1, -1)
print(*visited)
