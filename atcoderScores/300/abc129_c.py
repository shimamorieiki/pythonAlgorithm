# N 段の階段があります。
# 高橋君は現在、上り口(0 段目)にいます。 
# 高橋君は一歩で 1 段か 2 段上ることができます。
# ただし、a1,a2,a3,....aM 段目の床は壊れており、その段に足を踏み入れることは危険です。
# 壊れている床を踏まないようにしながら、
# 最上段(N 段目)にたどりつくまでの移動方法は何通りあるでしょうか？ 
# 総数を 1,000,000,007 で割った余りを求めてください。
# 制約
# 1≦N≦10^5
# 0≦M≦N−1
# 1≦a1<a2< ... <aM≦N−1

# 6 1
# 3

# 4

N,M = map(int,input().split(" "))
a = [0]*(N+1)
for i in range(M):
    a[int(input())] = 1
dp  = [0]*(N+1)

dp[N-1] = 1 if a[N-1] == 0 else 0
if a[N-2] == 0:
    if a[N-1] == 0:
        dp[N-2] = 2
    else:
        dp[N-2] = 1
else:
    dp[N-2] = 0
for i in reversed(range(N-2)):
    dp[i]  = (dp[i+1] + dp[i+2]) if a[i]==0 else 0

print(dp[0]%(1000000007) )
# さすがにこれはdp
# dp[i] = v i段目にいるときにゴールまでの移動方法
# dp[i] = dp[i+1] + dp[i+2] if a[i] == 0 else 0
# AC 26
# listの走査は割と計算量が大きいらしいのでそれはしないほうがいい