n = int(input())
ans = ''
for i in range(1, n+1):
    if i > 0 and i % 3 == 0:
        ans += 'x'
    else:
        ans += 'o'

print(ans)