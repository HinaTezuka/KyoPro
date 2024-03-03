import math

# x**2, y**2を限りなくdに近づければ良い。
# xを固定して全探索
d = int(input())

X = 0
Y = 0
list = []
# for x in range(100):
#     y = math.sqrt(abs(d - (x**2)))
#     if y > 0 and y % 1 == 0:
#         list.append([x, int(y)])

for x in range(100):
    for y in range(100):
        list.append(abs(d - ((x**2)+(y**2))))

print(min(list))
