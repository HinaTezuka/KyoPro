n = int(input())
G = [[] for _ in range(n)]
I = [None] * (n+1)
J = [None] * (n+1)

for i in range(n):
    l  = list(map(int, input().split()))
    # print(l)
    ans = ""
    for j in range(n):
        if l[j] == 1:
            ans += str(j+1) + " "
    print(ans[:-1])