# import math
# N = 3
# M = 3
# a = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 3], [0, 1, 3, 0]]

# # N,M = map(int,input().split(" "))
# # a = [[0]*(N+1) for i in range(N+1)]
# # for i in range(M):
# #     x,y,v = map(int,input().split(" "))
# #     a[x][y] = v
# #     a[y][x] = v
# # print(a)

# f = [math.inf]*(N+1) # スタートからその道にたどり着くまでの現段階での最短経路
# # 今回は連結なのですべての道を通れるということでいいんだと思う
# def shortest(v1,v2):
#     global f,a
#     # 最短経路で進んだときの経路を出力する
#     # 距離重み付きだから最短経路 != 通る頂点数最小
#     # ダイクストラ法？
#     if v1 == v2:
#         return 0
#     for i in range(1,len(a[v1])):
#         if a[v1][i] != 0:
#             f[i] = min(f[v1] + a[v1][i],f[i])
#             shortest(i,v2)

# s = 1
# g = 2
# f[s] = 0
# shortest(s,g)
# print(f)
# 方針としてはダイクストラで最短経路出す ワーシャルフロイド？
# そのそれぞれの経路について通った道を列挙して最初のグラフをコピーした配列に加算する
# その時にもとと同じグラフに加算すると重みの値が変化するのでだめ
# 一回も加算されていない辺の個数を数える
# 方針はわかったが実装が重そうなのでもう少ししてから考える
# AC 解答見た



# 全頂点間の最短経路問題なのでワーシャるフロイドだとは思う。
# どうやって最短経路で使った道を探すんだろうか？
import copy

N,M = map(int,input().split(" "))
a = []
for i in range(M):
    a.append(list(map(int,input().split(" "))))

inf = float("inf")
dp = [[inf]*N for _ in range(N)]
# 自分から自分への移動はコスト0
for i in range(M):
    dp[a[i][0]-1][a[i][1]-1] = a[i][2]
    dp[a[i][1]-1][a[i][0]-1] = a[i][2]

for i in range(N):
    dp[i][i] = 0

bef_dp = copy.deepcopy(dp)

for k in range(N):
    for n in range(N):
        for m in range(N):
            dp[n][m] = min(dp[n][m],dp[n][k] + dp[k][m])

# 最小値のパスが変更されたものを探す
# 最小値のパスが変更されたってことはもともとのパスが利用されなくなったということ・
# もともとがinfで他の数字に変更されたということはそのパスが使われたということ
s = sum(bef_dp, [])
t = sum(dp, [])
count = 0
for i,j in zip(s,t):
    if i!=j and i != inf:
        count +=1

print(count//2)

# AC43