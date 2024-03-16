from bisect import bisect_left
import heapq

n = int(input())
a = list(map(int, input().split()))

# リストをヒープに変換する
heapq.heapify(a)

c = 0
# print(type(a))
while True:
    heapq.heapify(a)
    if n <= 1:
        c = 0
        break

    # 最小値と最大値を取得する
    mn = a[0]  # ヒープの先頭が最小値
    mx = a[-1]  # ヒープの末尾が最大値
    # print(mx)
    
    if mx - mn <= 1:
        break
    
    # 最大値を-1し、最小値を+1する
    # heapq.heappop(a)  # 最小値を取り出すことで削除
    # heapq.heappush(a, mn + 1)
    mn_idx = bisect_left(a, mn)
    mx_idx = bisect_left(a, mx)
    a[mn_idx] += 1
    a[mx_idx] -= 1
    # heapq.heappush(a, (mx - 1))  # 最大値を負の値にしたので、+1することで-1になる
    
    c += 1

print(c)