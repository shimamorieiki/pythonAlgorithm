# N 個の品物が与えられます。
# i 番目の品物の価値は vi(1≦i≦N) です。
# これらの品物から、A 個以上、B 個以下を選ばなければなりません。
# この制約下において、選んだ品物の価値の平均の最大値を求めてください。
# また、選んだ品物の平均が最大となるような品物の選び方が何通りあるかを求めてください。
# 制約
# 1≦N≦50
# 1≦A≦B≦N
# 1≦vi≦10^15
# vi は全て整数である。

# 5 2 2
# 1 2 3 4 5

# 4.500000
# 1

# N,A,B  = 5,2,2
# v = [0,1,2,3,4,5]

N,A,B = map(int,input().split(" "))
v = [0]
v.extend(list(map(int,input().split(" "))))
dp = [[[0]*2 for j in range(N+1)] for i in range(N+1)]
dp[1][1][1] =5
for i in range(1,N+1):
    dp[i][1][1] = i
    dp[i][i][1] = 1
print(dp)
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i][j][0] = max(dp[i-1][j][0],(dp[i-1][j-1][0]*(j-1)+v[i])/j)

        if dp[i-1][j][0] == (dp[i-1][j-1][0]*(j-1)+v[i])/j:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j-1][1]
        elif dp[i-1][j][0] > (dp[i-1][j-1][0]*(j-1)+v[i])/j:
            dp[i][j][1] = dp[i-1][j][1]
        else:
            dp[i][j][1] = dp[i-1][j-1][1]

# for i in range(1,N+1):
#     for j in range(1,i+1):
#         dp[i][j] = max(dp[i-1][j],(dp[i-1][j-1]*(j-1)+v[i])/j)

print(dp)
# print(max(dp[N][A:B+1][0]))
# print(dp[N][A:B+1][0].count(max(dp[N][A:B+1][0])))
# こういう価値がどうこうは完全にナップザックdpなのでそういうことだと思ってる
# dp[i][j][0] = v i番目までの品物のうちj個選んだときの価値の平均の最大値v
# dp[i][j][0] = v i番目までの品物のうちj個選んだときの価値の平均の最大値になるパターンがいくつあるか
# dp[i][j] = max( dp[i-1][j], (dp[i-1][j-1]*i + v[i]) / j)
# 求める価値の最大はmax(dp[N][A],...,dp[N][B])
# 方針はこれで良くて、区間が決まってるときの最大値も多分取れてるのであとはその個数だけ
# 個数入れるところが三重のfor文も更新もだめっぽい

# AC 諦めた
# なんか全然違う解法してる