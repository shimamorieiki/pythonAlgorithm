# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))

# 数列 A1,A2,A3,…,AN が与えられます。 この数列は負の要素を含むかもしれません。
# 数直線上の座標 0 に置かれているロボットが、以下の動作を順に行います。
# 正の向きに A1 進む。
# 正の向きに A1 進み、正の向きに A2 進む。
# 正の向きに A1 進み、正の向きに A2 進み、正の向きに A3 進む。
# ⋮
# 正の向きに A1 進み、正の向きに A2 進み、正の向きに A3 進み、… 、正の向きに AN 進む。

# 動作開始時から終了時までのロボットの座標の最大値を求めてください。
# 制約
# 1≤N≤200000
# −10^8≤Ai≤10^8
# 入力はすべて整数

# 3
# 2 -1 -2

# N = 3
# a = [2,-1,-2]
N = int(input())
a = list(map(int,input().split(" ")))
res = [0]*N #各ステップにおいてどこまで行けば最大値か
wlk = [0]*N #各ステップごとの合計
rui = [0]*N
res[0] = a[0]
wlk[0] = a[0]
rui[0] = a[0]
for i in range(1,N):
    res[i] = max(res[i-1],wlk[i-1]+a[i])
    wlk[i] = wlk[i-1]+a[i]
    rui[i] = rui[i-1]+wlk[i]
# print(res,wlk,rui)
dp = [0]*N
dp[0] = res[0]
for i in range(1,N):
    dp[i] = max(dp[i-1],rui[i-1]+res[i]) #このsumさえなくせればd問題も解けたことになる
print(max(max(dp),0))