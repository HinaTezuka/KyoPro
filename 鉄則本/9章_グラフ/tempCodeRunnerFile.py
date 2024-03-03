n, m  = map(int, input().split())

# 連接リストの作成(空のリストで初期化)
List = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    List[a-1].append(b)
    List[b-1].append(a)

# 出力
for i in range(len(List)):
	output = ''
	output += str(i)
	output += ': {'
	output += ', '.join(map(str, List[i])) # 例えば List[i] = { 2, 7, 5 } のとき、ここで "2, 7, 5" という文字列が output の後ろに連結される
	output += '}'
	print(output)