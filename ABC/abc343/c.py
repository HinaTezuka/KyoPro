import math

def isKaibun(num) -> bool:
    num = str(num)
    if len(num) == 1:
        return True

    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False

    return True

n = int(input())

for i in range(int(n**0.35), -1, -1):
    rippou = pow(i, 3)
    if rippou <= n:
        if isKaibun(rippou):
            print(rippou)
            break