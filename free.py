from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (n+1)
dist[1] = 0
q = deque()
q.append(1)

# bfs
while len(q) >= 1:
    pos = q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos]+1
            q.append(nex)

for i in range(1, n + 1):
	print(dist[i])