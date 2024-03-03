n = int(input())
data_list = []
for _ in range(n):
    data_list.append(list(map(int, input().split())))

t = 0
a = 0
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        if j == 0: t += data_list[i][j]
        if j == 1: a += data_list[i][j]
if t > a: print('Takahashi')
if a > t: print('Aoki')
if a == t: print('Draw')