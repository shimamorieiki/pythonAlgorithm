# 数字iから1に変更する最小手数をdp使えばいい？

# H,W = map(int,input().split(" "))

# c = []
# for i in range(10):
#     c.append(list(map(int,input().split(" "))))
# a = []
# for i in range(H):
#     a.append(list(map(int,input().split(" "))))

# dp = [1000]*10

# dp[0] = c[0][1]
# dp[1] = 0

# for i in range(2,10):
#     for j in range(i):
#         if dp[j] + c[i][j] < c[i][1] :
#             dp[i] = dp[j] + c[i][j]
#         else:
#             dp[i] = c[i][1]

# answer = 0
# for i in a:
#     for j in i:
#         if j != -1:
#            answer += dp[j] 
# print(dp)
# print(answer)
# dpと思ったけどうまく行かなかった

# ワーシャルフロイド方とか言われても知らん

# すべての頂点iに対してi->1の有向グラフの最短経路を求める問題なので
# ワーシャルフロイドが使える
# 更に頂点は1-9の9個しかないのでN^3でも余裕で間に合う。

H,W = map(int,input().split(" "))

c = []
for i in range(10):
    c.append(list(map(int,input().split(" "))))
a = []
for i in range(H):
    a.extend(list(map(int,input().split(" "))))

# ワーシャルフロイドは頂点1-kを使うときにi->jの移動を
# dp[k][i][j] = 0-kの頂点を使ってi->jに移動するときの最小コストで管理する
# 今回の問題は使用する頂点数に制限がないので最初からすべての頂点を使うと考えてよい

dp = [[]*10 for _ in range(10)]
for i in range(10):
    dp[i] = c[i]

for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

ans = 0
for i in a:
    if i != -1:
        ans += dp[i][1]
print(ans)