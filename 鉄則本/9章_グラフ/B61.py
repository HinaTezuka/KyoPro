import sys

sys.setrecursionlimit(120000)

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 深さ優先探索
visited = [ False ] * (n + 1)
dfs(1, G, visited)

# 連結かどうかの判定（answer == True のとき連結）
ans = True
for i in range(1, n+1):
    if visited[i] == False:
        ans = False
        break

# 答えの出力
if ans == True:
	print("The graph is connected.")
else:
	print("The graph is not connected.")