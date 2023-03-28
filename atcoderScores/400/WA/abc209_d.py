# 街aから街bまでの長さが偶数ならRoad,奇数ならTown
# 街がN個に対して道がN-1本しかないということは閉路が存在しない？
# ということは街から街への移動は1通りしかない
# 一度全ての経路を計算して、各クエリについてはO(1)で判定したい
# 既に判明している道をもとにDFSで求める

N = 4
Q = 1
A = [[1, 2], [2, 3], [2, 4]]
C = [[1, 2]]
inf = N + 1

# 経路を計算するための二次元配列
R = [[inf for _ in range(N)] for _ in range(N)]

# 探索したかを管理する二次元配列
G = [[0 for _ in range(N)] for _ in range(N)]


def dfs(start, end):
    # 既に頂点を探索済の時は反対側も探索済として終了
    if G[start][end] == 1:
        return

    # 頂点を探索したことの印
    G[start][end] = 1
    G[end][start] = 1
    
    # 道が明らかとなっていないときは中間までを計算する
    m = []
    for i in range(N):
        if R[start][i] == inf:
            
    [dfs(start, i) + dfs(i, end) ]
    return min()


print(R)

for a, b in A:
    R[a - 1][b - 1] = 1
    R[b - 1][a - 1] = 1

print(R)


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        # i,j間の経路を計算する
        R[i][j] = dfs(i, j)
        R[j][i] = R[i][j]
print(R)

# 経路長を求めるより経路長の偶奇を求めるだけで良い
# dfsで良いのはその通り
# 再帰のdfsが難しいのでどっかのタイミングでもう少しちゃんと勉強する