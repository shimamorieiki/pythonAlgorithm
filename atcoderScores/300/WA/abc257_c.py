# 必ずしもXを求める必要はない
# Xを求めるとしてもw_iの値のどれかについて検討すれば十分

# give up 40m
N = int(input())
S = list(map(int, list(input())))
W = list(map(int, input().split(" ")))

T = []
for t in range(N):
    T.append([W[t], S[t]])

# 自分より左(自分自身は含む)にいくつ0,1がそれぞれ存在するか
L = [[0, 0] for _ in range(N + 1)]

# 自分より右(自分自身は含む)にいくつ0,1がそれぞれ存在するか
R = [[0, 0] for _ in range(N + 1)]

for i, [w, s] in enumerate(sorted(T)):
    L[i + 1][0] += L[i][0]
    L[i + 1][1] += L[i][1]
    if s == 0:
        L[i + 1][0] += 1
    if s == 1:
        L[i + 1][1] += 1

for i, [w, s] in enumerate(reversed(sorted(T))):
    R[i + 1][0] += R[i][0]
    R[i + 1][1] += R[i][1]
    if s == 0:
        R[i + 1][0] += 1
    if s == 1:
        R[i + 1][1] += 1

R = list(reversed(R))

c = 0
for l, r in zip(L, R):
    c = max(c, l[0] + r[1])

print(c)

# 体重の重複がない限り上手く動いた
# 公式解説のように増減を計算するか
# ユーザ解説のように増減を計算するかはどっちでもよさそう
