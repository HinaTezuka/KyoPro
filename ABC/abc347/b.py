S = input()

l = set()
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        l.add(S[i:j])

print(len(l))
