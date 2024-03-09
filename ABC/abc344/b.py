l = []
while True:
    a = input()
    if a == '0':
        l.append(int(a))
        break
    l.append(int(a))

for i in range(len(l)-1, -1, -1):
    print(l[i])