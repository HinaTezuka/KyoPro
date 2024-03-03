n = int(input())
s = input()
mx = [0] * 26

l = 0
while l < n:
    r = l + 1
    while r < n and s[l] == s[r]:
        r += 1
    c = ord(s[l]) - ord('a')
    #この行は、文字 s[l] の Unicode コードポイントから文字 'a' の Unicode コードポイントを引いた結果を変数 c に代入しています。具体的には、文字 'a' は Unicode コードポイントで 97 です。例えば、文字 'b' の Unicode コードポイントは 98 なので、ord('b') - ord('a') は 98 - 97 となり、結果は 1 になります。これにより、各文字の相対的な位置（0-indexed）が求められます。
    mx[c] = max(mx[c], r - l)
    l = r

ans = sum(mx)
print(ans)