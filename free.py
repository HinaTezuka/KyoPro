n = int(input())
a = []
b = []
for i in range(n*2):
    if i < n:
        a.append(list(input()))
    else:
        b.append(list(input()))

for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] != b[i][j]:
            print(i+1, j+1)
            break
