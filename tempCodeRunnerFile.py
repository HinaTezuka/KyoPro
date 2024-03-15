# from string import ascii_lowercase
from itertools import groupby
import bisect

def runLengthEncode(S: str) -> list:
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

def check(T, S) -> int:
    diff = abs(len(T) - len(S))  # 初期化時に文字列の長さの違いを計算

    # 両方の文字列の各文字を比較し、違いの数を数える
    for i in range(min(len(T), len(S))):
        if T[i] != S[i]:
            diff += 1

    return diff

n, T_dash = map(str, input().split())
n = int(n)
T_dash_coded = runLengthEncode(T_dash)

ans = []
for i in range(n):
    s = input()
    s_coded = runLengthEncode(s)
    if check(T_dash_coded, s_coded) <= 1:
        ans.append(i+1)
print(*ans)