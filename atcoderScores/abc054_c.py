# 自己ループと二重辺を含まない N 頂点 M 辺の重み無し無向グラフが与えられます。
# i(1≦i≦M) 番目の辺は頂点 ai と頂点 bi を結びます。
# ここで、自己ループは ai=bi(1≦i≦M) となる辺のことを表します。
# また、二重辺は ai=aj かつ bi=bj(1≦i<j≦M) となる辺のことを表します。
# 頂点 1 を始点として、全ての頂点を1度だけ訪れるパスは何通りありますか。
# ただし、パスの始点と終点の頂点も訪れたものとみなします。 

# 2≦N≦8
# 0≦M≦N(N−1)/2
# 1≦ai<bi≦N
# 与えられるグラフは自己ループと二重辺を含まない。

# N M
# a1 b1
# a2 b2
# :   :
# aM bM

  
# 3 3
# 1 2
# 1 3
# 2 3

# 2

# 終わるか続けるかを分離すべき？
def visit(i):
    global v,count
    if v.count(1) == len(v)-1:
        count+=1
    else:
        for j in range(1,N+1):
            if (v[j]==0 and g[i][j] ==1):#まだ来たことがない and iからの道が存在する
                v[j]=1  #入り組ませるからいけない
                visit(j)#自分が存在した痕跡は
                v[j]=0  #すぐ消せ


N,M = map(int,input().split(" "))
g = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split(" "))
    g[a][b] = 1
    g[b][a] = 1
v = [0]*(N+1)
count = 0

# print(N,M,g)
v[1] = 1
visit(1)
print(count)
# AC 解答見た
    