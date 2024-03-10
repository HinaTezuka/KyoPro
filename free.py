def m_inp():
    return map(int, input().split())

n, m = m_inp()
a = [None] * m
b = [None] * m
G = [[] for _ in range(n)]
for i in range(n):
    a, b = m_inp()
    G[a].append(b)
    G[b].append(a)

