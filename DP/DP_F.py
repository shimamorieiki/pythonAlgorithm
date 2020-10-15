#文字列 s および t が与えられます。
# sの部分列かつtの部分列であるような文字列のうち、最長のものをひとつ求めてください。
# 文字列 xの部分列とは、x から 0個以上の文字を取り除いた後、
# 残りの文字を元の順序で連結して得られる文字列のことです。
# sおよびtは英小文字からなる文字列である。
# 1≤|s|,|t|≤3000

# dp[i][j] sのi文字目 tのj文字目までの最長部分文字列
# dp[i][j] = dp[i-1][j-1] + 1 if s[i] == t[j]
#            dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]  if s[i] != t[j]

def solve(s,t):
    dp = [[""]*(len(t)+1) for i in range(len(s)+1)]
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + s[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]
    print(dp[len(s)][len(t)])
    

# s = "axyb"
# t = "abyxb"

s = "abracadabra"
t = "avadakedavra"


solve(s,t)