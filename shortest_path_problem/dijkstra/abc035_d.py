# N,M,T = map(int,input().split(" "))
# A = list(map(int,input().split(" ")))
# # パスの情報
# edge = []
# for i in range(M):
#     edge.append(list(map(int,input().split(" "))))

# def shorest_path(start,goal):
#     """
#     startからgoalまでの最短距離
#     """
#     # 頂点1から各頂点へ所要時間の最小値
#     inf = float('inf')
#     d = [inf]*(N+1)

#     # その点の最小値を更新したか
#     used = [False]*(N+1)
#     used[1] = True

#     # 1から1への移動コストは0
#     d[start] = 0
#     for _ in range(N-1):
#         for e in edge:
#             if d[e[0]] != inf and d[e[1]] > d[e[0]] + e[2]:
#                 d[e[1]] = d[e[0]] + e[2]
#     return d[goal]

# max = A[0] * T
# for i in range(2,N+1):
#     time = shorest_path(1,i) + shorest_path(i,1)
#     if max < A[i-1] * (T-time):
#             max = A[i-1] * (T-time)
# print(max)
# コストを最大化するので、移動に必要な時間の正負を反転させれば最短経路問題になる
# これはすべてのパスに対して移動時間を求めて、それらのどこかの頂点で余った時間待機するのが一番効率良さそう？
# ここまで考えが思い浮かんだのに以下に気が付かないのは普通に頭が悪い
# -> 頂点1からある頂点iに最も早く移動し、最も早く頂点1に帰ってくる
# このとき、移動にかからない時間はすべてiに滞在する。これをすべての頂点に対して行い、もっともスコアが上がる頂点を探す

# N,M,T = map(int,input().split(" "))
# A = list(map(int,input().split(" ")))
# # パスの情報
# inf = float('inf')
# edge = [[inf]*(N+1) for i in range(N+1)]
# # print(edge)
# for i in range(M):
#     x,y,c = map(int,input().split(" "))
#     edge[x][y] = c
# print(edge)

# def shorest_path(start,goal):
#     """
#     startからgoalまでの最短距離
#     """
#     # 頂点1から各頂点へ所要時間の最小値
#     inf = float('inf')
#     d = [inf]*(N+1)

#     # その点の最小値を更新したか
#     used = [False]*(N+1)

#     # 1から1への移動コストは0
#     d[start] = 0
#     for _ in range(N+1):

#         # まだ使っていない頂点のうち頂点からの距離が最小のもの
#         # 今回の更新でこれ以上更新されないことが確定する
#         v = -1
#         for u in range(1,N+1):
#             if (not used[u] and (v == -1 or d[u] < d[v])):
#                 v = u
        
#         if v == -1:
#             break

#         used[v] = True

#         for i in range(1,N+1):
#             d[i] = min(d[i],d[v]+edge[v][i])

#     return d[goal]

# # ans = shorest_path(1,2)
# # print(ans)

# max = A[0] * T
# for i in range(2,N+1):
#     time = shorest_path(1,i) + shorest_path(i,1)
#     if max < A[i-1] * (T-time):
#             max = A[i-1] * (T-time)
# print(max)

# pathの和がinfになる可能性があるのか
# これは計算量がかかる方のダイクストラ
# さらにこの問題では1->iとi->1を求める必要がある
# 1->iは1回の操作で求まるが、i->1は頂点の回数分求める必要があり遅くなる
# 有向グラフなんだったら、グラフの向きを変えるのが一番早くて、一回のメソッド実行で済む


# ここからheapqを使って計算量を減らしたときのダイクストラ
import heapq

N,M,T = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
edge = [list(map(int,input().split(" "))) for _ in range(M)]
# パスの情報
inf = float('inf')

# 行きの順の有向グラフ
# 帰りの順の有向グラフ
go =[[] for i in range(N)]
back = [[] for i in range(N)]
for a,b,c in edge:
    go[a-1].append([b-1,c])
    back[b-1].append([a-1,c])
    
# 行きの1からiまでの最短経路
d_go = [inf]*N

# 帰りの1からiまでの最短経路
d_back = [inf]*N

# その点の最小値を更新したか
used = [False]*(N+1)

# 1から1への移動コストは0
d_go[0] = 0
d_back[0] = 0

pQue = []

# スタート地点からからd[1]へ移動するコストが0
heapq.heappush(pQue, [0, 0])

# パスの最小値を更新
while len(pQue) > 0:

    # 1からnodeまでのcostが最小のものの(node,cost)
    cost,node = heapq.heappop(pQue)

    # 取り出したコストがパスの最小でなかったら飛ばす
    # 現在の1からnodeまでの最短経路 < 1からnodeに移動するコストなら更新は生じないのでcontinue
    if cost > d_go[node]:
        continue

    # 次の最小コストのパスを取得
    for next_node,new_cost in go[node]:
        # 現在の最小コストより、新しい経路のほうがコストが減るなら更新
        if d_go[next_node]>new_cost+d_go[node]:
            d_go[next_node] = new_cost+d_go[node]
            heapq.heappush(pQue, [new_cost,next_node])


# スタート地点からからd[1]へ移動するコストが0
heapq.heappush(pQue, [0, 0])

# 帰りのパスの最小値を更新
while len(pQue) > 0:

    # 1からnodeまでのcostが最小のものの(node,cost)
    cost,node = heapq.heappop(pQue)

    # 取り出したコストがパスの最小でなかったら飛ばす
    # 現在の1からnodeまでの最短経路 < 1からnodeに移動するコストなら更新は生じないのでcontinue
    if cost > d_back[node]:
        continue

    # 次の最小コストのパスを取得
    for next_node,new_cost in back[node]:
        # 現在の最小コストより、新しい経路のほうがコストが減るなら更新
        if d_back[next_node]>new_cost+d_back[node]:
            d_back[next_node] = new_cost+d_back[node]
            heapq.heappush(pQue, [new_cost,next_node])

max = A[0] * T
for i in range(N):
    time = d_go[i] + d_back[i]
    if time == inf:
        continue
    if max < A[i] * (T-time):
            max = A[i] * (T-time)
print(max)