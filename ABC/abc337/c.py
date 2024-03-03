n = int(input())
a = list(map(int, input().split()))

hashMap = {}
for i in range(n):
    hashMap[a[i]] = i+1

c = 0
output = []
head = -1
for i in range(n):
    output.append(str(hashMap[head]))
    head = hashMap[head]
    c += 1
print(' '.join(output))