# 要は、以下の条件を満たす組が1つでもあればYes
# - Y座標が同じ
# - 進行方向が逆
# - X_r < X_l
# Y軸で走査したかったけど計算量的に厳しい


N = 3
X = [2, 1, 4]
Y = [3, 1, 1]
S = "RRL"

A = {}
for i in range(N):
    A.setdefault(Y[i], set())
    A[Y[i]].add(S[i])

# WA
# 考察が足りない
