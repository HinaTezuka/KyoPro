n = int(input())
p = list(map(int, input().split()))
q = int(input())

for i in range(q):
    a, b = map(int, input().split())

    a_iti = p.index(a)
    b_iti = p.index(b)

    if a_iti > b_iti:
        print(b)
    else:
        print(a)