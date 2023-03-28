# ぱっと思いついたのは、A_i,B_iの差が最も大きいものから
# A_i < B_i のものに割り振っていくこと
from bisect import bisect

N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

# A のうち B に足りていない点数の総和を取得する
C = []
# A のうち B に過剰な点数を取得する
S = []
for a, b in zip(A, B):
    if a < b:
        C.append(b - a)
    if a > b:
        S.append(a - b)

# もしlen(C) == 0
# すなわち不足分がないときは何もしなくてよい
if len(C) == 0:
    print(0)
    exit()

# もしsum(C) > sum(S)
# すなわち過剰分で不足分を補えないときはどうやっても
# 全ての試験に合格することが出来ない
if sum(C) > sum(S):
    print(-1)
    exit()

S = list(reversed(sorted(S)))


# Sのうち i 番目までの和
T = [0] * len(S)
T[0] = S[0]
for i in range(1, len(S)):
    T[i] += T[i - 1] + S[i]

i = bisect(T, sum(C))

print(len(C) + i + 1)


# AC 30m
# 模範解答通り