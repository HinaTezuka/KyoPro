s = input()
hashMap = {}

for i in s:
    if i not in hashMap:
        hashMap[i] = 1
    else: 
        hashMap[i] +=1

max = max(hashMap.values())
# print(max)
ans = []
for key, value in hashMap.items():
    if max == value:
        ans.append(ord(key))

print(chr(min(ans)))