a, b = map(int, input().split())

for i in range(10):
    if i != a+b:
        print(i)
        break