s = input()

for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if 'A' * a + 'B' * b + 'C' * c == s:
                print('Yes')
                exit()
print('No')