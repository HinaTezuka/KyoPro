import math

x = int(input())

if x > 0:
    if x % 10 == 0:
        print(x // 10)
    else:
        print((x // 10) + 1)
else:
    print(math.ceil(x / 10))
