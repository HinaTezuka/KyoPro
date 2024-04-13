from itertools import combinations
import sys
import copy

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
    if hmap.get(T[i].lower()) != None and len(hmap[T[i].lower()]) != 0:
        t_idx = hmap[S[i]].pop(0)
        tu.append(t_idx)
    else:
        if i < 2:
            print('No')
            sys.exit()
        elif i == 2:
            if tu[0] <= tu[1] and T[-1] == 'X':
                print('Yes')
                sys.exit()

sorted_tu = copy.deepcopy(tu).sort()
if tu == sorted_tu:
    print('Yes')