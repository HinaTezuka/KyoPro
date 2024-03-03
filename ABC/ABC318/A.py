n, m, p = map(int, input().split())
# print(n, m, p)
c = 1
if n < m:
    print(0)
else:
    m = n - m
    print(c + (m // p))