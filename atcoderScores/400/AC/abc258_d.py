# 問題の感じから苦手なにおいがする
# 何となく答えでにぶたんの匂いもする
# dp[i][j] = ステージ i を一回でもクリアして
# 合計 j ステージクリアする最小時間
# dp[i][j] = min(dp[i][j-1] + min(B[:i+1]),dp[i-1][j-1] + A[i] + B[i])
# min(b[:i+1])はメモ化すればどうにかなる？
# dpで回そうとしたけどXが思ったより大きかった
# 答えでにぶたんできるのって、解答候補の数字Xが分かったら
# Xで実現できるかどうかを割と簡単に確認出来るときのみ
# 今回は結局どういう手順を取るかを選ぶのかが自明ではないので不適切だと思う。
# ステージiまで進んでX回クリアする最小値は割と自明に求まる
# 最初の１回だけステージiまでやって、あとは一番時間がかからないものを全部すればよい


N, X = map(int, input().split(" "))
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

# A,Bの累積和
A_r = list(A)
B_r = list(B)
for i in range(1, N):
    A_r[i] += A_r[i - 1]
    B_r[i] += B_r[i - 1]

B_min = list(B)
for i in range(1, N):
    B_min[i] = min(B_min[i], B_min[i - 1])

c = 10**20
for i in range(N):
    c = min(c, A_r[i] + B_r[i] + (X - (i + 1)) * B_min[i])
print(c)

# 十分大きい数として想定していた10**10が小さかったらしい
# AC 40m
