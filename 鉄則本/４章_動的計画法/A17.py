N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, len(dp)):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# 復元
Answer = []
currentRoom = N
while True:
    Answer.append(currentRoom)
    if currentRoom == 1: break
    if dp[currentRoom] == dp[currentRoom-1] + A[currentRoom-2]:
        currentRoom -= 1
    else:
        currentRoom -= 2

ans = ''
for i in range(len(Answer)-1, -1, -1):
    if i == 0: ans += str(Answer[i])
    else: ans += str(Answer[i])+' '

print(len(Answer))
print(ans)