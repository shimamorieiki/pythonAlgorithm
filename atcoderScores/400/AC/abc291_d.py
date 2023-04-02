# dpっぽさを感じる
# dp[i][j] = i 枚目 が 0(=A,1=B) を向いているときにそれより全て相異なるような選び方
# dp[i][0] = dp[i-1][0]

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

dp = [[0, 0] for _ in range(N)]

dp[0][0] = 1
dp[0][1] = 1
for i in range(1, N):
    a = 0 if A[i - 1] == A[i] else dp[i - 1][0]
    b = 0 if B[i - 1] == A[i] else dp[i - 1][1]
    dp[i][0] = (a + b) % 998244353

    c = 0 if A[i - 1] == B[i] else dp[i - 1][0]
    d = 0 if B[i - 1] == B[i] else dp[i - 1][1]
    dp[i][1] = (c + d) % 998244353

print((dp[N - 1][0] + dp[N - 1][1]) % 998244353)

# AC 23
# 適切にmodを取らないとTLE,MLEになる
