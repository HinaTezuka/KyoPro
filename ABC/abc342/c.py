from string import ascii_lowercase

n = int(input())
s = input()
q = int(input())

mapping_from = ascii_lowercase
mapping_to = ascii_lowercase

for i in range(q):
    a, b = input().split()
    mapping_to = mapping_to.replace(a, b)

print(s.translate(str.maketrans(mapping_from, mapping_to)))