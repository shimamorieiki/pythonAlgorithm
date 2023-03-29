# これこそどう考えてもdp
# と思ったけど、やってみると N^2 だからTLE

S = "UUD"
# S = input()
N = len(S)
inf = 10**9
dp = [[inf for _ in range(N)] for _ in range(N)]
print(dp)

# 初期化
for i in range(N):
    # 自分の階には0回で行ける
    dp[i][i] = 0
    # i 階のボタンが U なら i 階より上には全て1回で行ける
    if S[i] == "U":
        for j in range(i + 1, N):
            dp[i][j] = 1
    # i 階のボタンが D なら i 階より下には全て1回で行ける
    if S[i] == "D":
        for j in range(i):
            dp[i][j] = 1
            
for i in range(N):
    for j in range(N):
        if dp[i][j] == inf:
            # まだ決まっていないときは
            # 下の階から上がってくるときの最小回数と
            # 上の回から降りてくるときの最小回数のうち小さいほう 
            
print(dp)

# WA 
# 非常に頭が悪い