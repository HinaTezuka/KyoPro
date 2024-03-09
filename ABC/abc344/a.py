S = input()

idx1 = S.index('|')
idx2 = S[idx1+1:].index('|')
# print(idx2)

print(S[:idx1]+S[idx1+idx2+2:])