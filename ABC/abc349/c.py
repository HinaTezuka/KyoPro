import sys

S = input()
T = input()

hmap = {}
for i in range(len(S)):
    if S[i] not in hmap:
        hmap[S[i]] = [i]
    else:
        hmap[S[i]].append(i)
tu = []
for i in range(3):
    t = T[i].lower()
    if hmap.get(t) != None and len(hmap[t]) > 0:
        t_idx = hmap[t].pop(0)
        tu.append(t_idx)
    else:
        if i == 2:
            if tu[0] < tu[1] and T[-1] == 'X':
                print('Yes')
                sys.exit()
        else:
            print('No')
            sys.exit()

if len(tu) == 3 and tu[0] < tu[1] and tu[1] < tu[2]:
    print('Yes')
else:
    print('No')