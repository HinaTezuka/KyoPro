w, b = map(int, input().split())
S = ''
# for i in range(50):
#     S += 'wbwbwwbwbwbw' # 12(7, 5)
# print(S)
import sys
from collections import Counter

S = ''
Wc = 0
Bc = 0
c = 0
while(True):
    if Wc == w and Bc == b:
        print('Yes')
        sys.exit()
    # if Wc > w and Bc > b:
    #     break
    if c > 100:
        break
    Wc += 7
    Bc += 5
    c += 1


print('No')