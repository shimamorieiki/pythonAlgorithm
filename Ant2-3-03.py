# 最長共通部分文字列LCS
# DPで解く解法 P56参照


def dp(n,m,s,t):
    # s,t 文字列s,t
    # n 文字列sの文長
    # m 文字列tの文長
    a = [ [0]*(n+1) for i in range(m+1) ]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i]==t[j]:
                a[i+1][j+1] = max(a[i][j]+1,a[i+1][j],a[i][j+1])
            else:
                a[i+1][j+1] = max(a[i][j+1],a[i+1][j])
    print(a[n][m])


s = "abcdefd"
t = "becdffd"
n = len(s)
m = len(t)
dp(n,m,s,t)