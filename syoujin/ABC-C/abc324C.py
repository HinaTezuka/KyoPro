from string import ascii_lowercase
import bisect

n, T_dash = map(str, input().split())
n = int(n)

# 各条件用(条件２〜４）の配列
potensial_Ts = set()
if len(potensial_Ts) < 27:
    for i in range(len(T_dash)):
            for j in ascii_lowercase:
                potensial_Ts.add(T_dash[:i]+j+T_dash[i:])
                potensial_Ts.add(T_dash[:i]+T_dash[i+1:])
                potensial_Ts.add(T_dash[:i]+j+T_dash[i+1:])
else:
    for i in range(len(T_dash)):
        potensial_Ts.add(T_dash[:i]+ascii_lowercase[i%26]+T_dash[i:])
        potensial_Ts.add(T_dash[:i]+T_dash[i+1:])
        potensial_Ts.add(T_dash[:i]+ascii_lowercase[i%26]+T_dash[i+1:])

# potensial_Ts = list(set(potensial_Ts))
# potensial_Ts = list(potensial_Ts)
# potensial_Ts.sort()
potensial_Ts = sorted(potensial_Ts)
ans = []
for i in range(n):
    s = input()
    if s == T_dash:
        ans.append(i+1)
        continue
    s_idx = bisect.bisect_left(potensial_Ts, s)
    if s_idx <= len(potensial_Ts) and potensial_Ts[s_idx] == s:
        ans.append(i+1)

# print(len(potensial_Ts))
print(*ans) if len(ans) > 0 else print(0)