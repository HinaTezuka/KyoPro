# 自分で解いた方（dequeをスタックとして使用)
from collections import deque

S = input()

q = deque()
for i in range(len(S)):
    if S[i] == '(':
        q.append(i+1)
    elif S[i] == ')':
        print(q[-1], i+1)
        q.pop()

# 解答例（リストを使ってスタックを実装）
# 入力
# S = input()

# # 左から順番に見ていく
# # 文字列は 0 文字目から始まることに注意
# Stack = []
# for i in range(len(S)):
# 	if S[i] == '(':
# 		Stack.append(i + 1)
# 	if S[i] == ')':
# 		print(Stack.pop(), i + 1)