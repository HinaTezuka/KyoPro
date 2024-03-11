# t = int(input())

def re1(flag=True, i=7381, c=10**4):
    while True:
        i_s = str(i)
        if flag and c == case-1:
            return i
            break
        if len(i_s) > 1:
            for j in range(len(i_s)-1):
                if i_s[j] == i_s[j+1]:
                    flag = False
                    break
        if flag: 
            c += 1
        i+= 1

# for i in range(t):
#     case = int(input())
#     if case > 10**4:
#         print(re1())
#         continue
#     while True:
#         i_s = str(i)
#         if flag and c == case-1:
#             print(i)
#             break
#         if len(i_s) > 1:
#             for j in range(len(i_s)-1):
#                 if i_s[j] == i_s[j+1]:
#                     flag = False
#                     break
#         if flag: 
#             c += 1
#         i+= 1

# flag = True
# 10**4: 7381
i = 10**4
c = 7381
while True:
    i_s = str(i)
    flag = True
    if flag and i == 10**8:
        print(i)
        print(c)
        break
    if len(i_s) > 1:
        for j in range(len(i_s)-1):
            if i_s[j] == i_s[j+1]:
                flag = False
                break
    if flag: 
        c += 1
    i+= 1
