from itertools import product
"""
0, 2, 4, 6, 8, 20, 22, 24, 26, 28, 40, 42, ....
"""
n = int(input())
d = 0
amari = 0
if n / 5 % 1 == 0:
    d = n / 5
else: 
    d = int(n / 5)
    amari = n % 5

nums = ['0', '2', '4', '6', '8']
print((d%5)+)
# l = set()
# for perm in product(nums, repeat=5):
#     l.add(int(''.join(map(str, perm))))
# l = sorted(l)
# print(len(l))