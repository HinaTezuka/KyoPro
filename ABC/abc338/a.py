s = input()
h = s[0].upper()
b = 'Yes'
if s[0] != h: b = 'No'
for i in s[1:]:
    l = i.lower()
    # print(i)
    # print(l)
    if i != l: b= 'No'

print(b)