S = input()

r = 0
l = 0
flag = True
for i in range(len(S)):
    if S[0] != '<':
        flag = False
        break
    if S[i] == '<':
        r += 1
    if S[len(S)-1] != '>':
        flag = False
        break
    if S[i] == '>':
        l += 1

if not flag or r != 1 or l != 1:
    print('No')
else:
    print('Yes')