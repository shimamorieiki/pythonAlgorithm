# N 日間の夏休みです。i 日目には、
# A: 海で泳ぐ。幸福度 ai を加算
# B: 山で虫取りする。幸福度 biを加算
# C: 家で宿題をする。幸福度 ciを加算
# の三択の中から好きなものを選ぶことができます。
# ただし、2 日連続で A, B, C のうちの同一種類の活動を選択をすることはできません。
# この制約下で最終的に得られる幸福度の総和を最大にせよ。
# 1≤N≤10^5

# dp[i][x] i日目に x(y,z) をして過ごしたときのそれまでの幸福度の最大
# dp[i][x] = max(dp[i-1][y] , dp[i-1][z]) + xi

def solve(n,abc):
    dp = [[0]*3 for i in range(n+1)]
    dp[1] = abc[0]
    for j in range(2,n+1):
        dp[j][0] = max(dp[j-1][1],dp[j-1][2])+abc[j-1][0]
        dp[j][1] = max(dp[j-1][0],dp[j-1][2])+abc[j-1][1]
        dp[j][2] = max(dp[j-1][0],dp[j-1][1])+abc[j-1][2]
        # print(dp[j])
    print(max(dp[n]))

# abc = [[10,40,70],
#       [20,50,80],
#       [30,60,90]]

abc = [[6,7,8],
       [8,8,3],
       [2,5,2],
       [7,8,6],
       [4,6,8],
       [2,3,4],
       [7,5,1]]
n = len(abc)


solve(n,abc)

