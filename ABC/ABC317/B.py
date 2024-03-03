n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

for i in range(len(a_list) - 1):
    if a_list[i+1] != a_list[i] + 1:
        print(a_list[i] + 1)