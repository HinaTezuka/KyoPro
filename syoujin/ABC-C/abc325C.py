from collections import deque

h, w = map(int, input().split())
z = [] # '#'の座標
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '#':
            z.append((i+1, j+1))       

# '#'の連接リスト
G = [[] for _ in range(len(z))]
for i in range(len(z)):
    for j in z[:i]+z[i+1:]:
        if max(abs(z[i][0]-j[0]), abs(z[i][1]-j[1])) == 1:
            j_idx = z.index(j)
            G[j_idx].append(i)

def bfs(i, visited) -> list:
    q = deque()
    q.append(i)
    while len(q) >= 1:
        pos = q.popleft()
        for i in G[pos]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return sorted(visited)

visited = []
res = []
for i in range(len(z)):
    if i in res:
        continue
    res = bfs(i, [])
    if res not in visited:
        visited.append(res)

print(len(visited))