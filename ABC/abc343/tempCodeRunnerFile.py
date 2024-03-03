import math

n = int(input())

l = []
for i in range(1, math.floor(math.sqrt(n))): # n+1
    if i**3 <= n:
        l.append(i**3)
# print(l)

def isKaibun(num) -> bool:
    num = str(num)
    if len(num) == 1: return True
    for i in range(len(num)):
        for j in range(len(num)-1, -1, -1):
            if len(num) % 2 == 0:
                if i+1 == j and num[i] == num[j]:
                    return True
            else:
                if i+2 == j and num[i] == num[j]:
                    return True

    return False

for i in range(len(l)-1, -1, -1):
    if isKaibun(l[i]):
        print(l[i])
        break