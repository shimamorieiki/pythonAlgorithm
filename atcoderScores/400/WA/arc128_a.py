# 愚直はいくら何でも爆発する
# 自分でトレースしても何にも思いつかない
# dp_g[i] = i日目に所持している金の最大価値
# dp_s[i] = i日目に所持している銀の最大価値
# dp_g[i] = max(dp_g[i-1],dp_s[i-1]/A[i-1])
# dp_s[i] = max(dp_s[i-1],dp_g[i-1] * A[i-1])
# 最終的に欲しいのはdp_g[N]

N = int(input())
A = list(map(int, input().split(" ")))

dp_g = [-1] * (N + 1)
dp_s = [-1] * (N + 1)

dp_g[0] = 1
dp_s[0] = 0

for i in range(1, N + 1):
    dp_g[i] = max(dp_g[i - 1], dp_s[i - 1] / A[i - 1])
    dp_s[i] = max(dp_s[i - 1], dp_g[i - 1] * A[i - 1])

print(dp_g, dp_s)

# DPで最大値は分かったけどそれを実現する方法が分からん
# WA
# なんか全然違ったわ
