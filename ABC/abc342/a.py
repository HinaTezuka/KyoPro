s = input()
map = {}

for i in range(len(s)):
    if s[i] not in map:
        map[s[i]] = [1, i+1]
    elif s[i] in map:
        map[s[i]][0] += 1
        continue

for value in map.values():
    if value[0] == 1:
        print(value[1])