# 数字iから1に変更する最小手数をdp使えばいい？

H,W = map(int,input().split(" "))

c = []
for i in range(10):
    c.append(list(map(int,input().split(" "))))
a = []
for i in range(H):
    a.append(list(map(int,input().split(" "))))

dp = [1000]*10

dp[0] = c[0][1]
dp[1] = 0

for i in range(2,10):
    for j in range(i):
        if dp[j] + c[i][j] < c[i][1] :
            dp[i] = dp[j] + c[i][j]
        else:
            dp[i] = c[i][1]

answer = 0
for i in a:
    for j in i:
        if j != -1:
           answer += dp[j] 
print(dp)
print(answer)
# dpと思ったけどうまく行かなかった

# ワーシャルフロイド方とか言われても知らん