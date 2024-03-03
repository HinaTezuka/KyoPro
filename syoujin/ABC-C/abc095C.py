# https://atcoder.jp/contests/abc095/tasks/arc096_a
# 

# 枚数で全探索←どこか固定して探索数をへらす

a, b, c, x, y = map(int, input().split())
INF = 10000000000000
"""
ABピザの枚数で固定して探索(そうすれば、自ずとAピザとBピザの枚数が決まり、
探索数を大幅に減らせる)
"""
ans = INF
ab = max(x, y) * 2
# ABピザは2枚買わないと1枚を作れないため、２つ飛ばしで探索してOK <- こっちの方が探索すうが1/2になる
for i in range(0, ab+1, 2):
    # A, Bピザの必要な枚数
    ab_num = i // 2
    a_num = max(x - ab_num, 0)
    b_num = max(y - ab_num, 0)
    # if a_num < 0:
    #     a_num = 0
    # if b_num < 0:
    #     b_num = 0
    
    # total金額の計算
    tot = c*i + (a*a_num) + (b*b_num)
    ans = min(ans, tot)

print(ans)