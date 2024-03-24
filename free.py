w, b = map(int, input().split())
S = ''
# for i in range(50):
#     S += 'wbwbwwbwbwbw' # 12(7, 5)
# print(S)
import sys
from collections import Counter

S = ''
s = []
for i in range(120):
    S += 'wbwbwwbwbwbw'
for i in range(len(S)):
    for j in range(i+1, len(S)):
        s.append(S[i:j+1])

for i in s:
    Wc = 0
    Bc = 0
    for j in range(len(i)):
        if i[j] == 'w': Wc += 1
        else: Bc += 1
    if Wc == w and Bc == b:
        print('Yes')
        sys.exit()


print('No')