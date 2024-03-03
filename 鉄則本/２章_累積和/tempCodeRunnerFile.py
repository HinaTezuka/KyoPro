d = int(input())
n = int(input())
attendances = []
for i in range(n):
    attendances.append(list(map(int, input().split())))

# 前日比の計算
ratio = [0 for _ in range(d+1)]

for i in range(len(attendances)):
    ratio[attendances[i][0]] += 1
    ratio[attendances[i][1]+1] -= 1

cumulationSum = []
for i in range(len(ratio)):
    if i == 0: cumulationSum.append(0)
    else:
        diff = cumulationSum[i-1]+ratio[i]
        cumulationSum.append(diff)
# print(cumulationSum[1:])

for i in range(len(cumulationSum)):
    if i == 0: continue
    print(cumulationSum[i])