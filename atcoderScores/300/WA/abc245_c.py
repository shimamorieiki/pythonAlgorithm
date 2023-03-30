# 答えでにぶたんみがある
# あったけど、Kが固定だから考えなくていい気がしてきた
# 全パターンを考えるのは流石に非効率
# 差が小さい方とかを貪欲に選んでも仕方ない
# dp ?
# dp[i][j] = i(0or1)のj番目にいるときのコストの最小値
# dp[0][j+1] = min(|dp[0][j] - A[j]|,|dp[1][j]- A[j]|)
# dp[1][j+1] = min(|dp[0][j] - B[j]|,|dp[1][j]- B[j]|)
N = 5
K = 4
A = [9, 8, 3, 7, 2]
B = [1, 6, 2, 9, 5]

dp = [[0 for _ in range(N)] for _ in range(2)]
print(dp)

dp[0][0] = A[0]
dp[1][0] = B[0]
for i in range(1, N):
    dp[0][i] = min(
        max(dp[0][i - 1], abs(A[i - 1] - A[i])), max(dp[1][i - 1], abs(B[i - 1] - A[i]))
    )
    dp[1][i] = min(
        max(dp[0][i - 1], abs(A[i - 1] - B[i])), max(dp[1][i - 1], abs(B[i - 1] - B[i]))
    )

print(dp)
if min(dp[0][N - 1], dp[1][N - 1]) <= K:
    print("Yes")
else:
    print("No")

# WA
# いまいちどうすればよかったかがしっくりこない
