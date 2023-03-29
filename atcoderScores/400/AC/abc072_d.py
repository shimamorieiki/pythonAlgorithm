# 色んな場合を考えると頭がこんがらがってくる場合は
# 全く別の手法で解くことが多い(体感)
# p_i=iのものが隣り合う時はそれらを入れ替える
# XOXのように位置と値が同じものの両端がp_i!=iのとき
# Xのうち片方を選ぶことで入れ替えられる
import math

N = int(input())
P = list(map(int, input().split(" ")))
counts = []
stack = 0
for i in range(N):
    if P[i] == i + 1:
        stack += 1
    else:
        if stack > 0:
            counts.append(stack)
            stack = 0
if stack > 0:
    counts.append(stack)
print(sum([math.ceil(c / 2) for c in counts]))

# AC 13m
# やろうとしていることは同じ
