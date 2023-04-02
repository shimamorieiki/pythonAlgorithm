# ぱっとみDPっぽかったけど
# N回目までの最適行動が、必ずしもN+K回目までの最適行動とならない可能性がある
# ということで dp[i][r(,s,t)] = i回目に「手r」を出したときのコストの最大値として
# dp[i][r] = max(dp[i-K][s]+R,dp[i-K][p]+R)
# dp[i][s] = max(dp[i-K][r]+S,dp[i-K][p]+S)
# dp[i][p] = max(dp[i-K][r]+P,dp[i-K][s]+P)
# 最後にN-K+1~N回までのそれぞれの mod K での最大値を求めて足す
# じゃんけんに勝たないと点数が入らないのが少しややこしかった

N, K = map(int, input().split(" "))
R, S, P = map(int, input().split(" "))
T = input()

A = [P, R, S]
B = ["r", "s", "p"]

dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    if i < K:
        for j in range(3):
            if B.index(T[i]) == j:
                dp[i][j] = A[j]
    else:
        for j in range(3):
            if B.index(T[i]) == j:
                dp[i][j] = max(
                    dp[i - K][(j + 1) % 3] + A[j], dp[i - K][(j + 2) % 3] + A[j]
                )
            else:
                dp[i][j] = max(dp[i - K][(j + 1) % 3], dp[i - K][(j + 2) % 3])
s = 0
for i in range(N - K, N):
    s += max(dp[i])
print(s)


# AC over 30m
# 面倒くさいけど実装しきった
