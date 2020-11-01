# N 頂点 M 辺の単純無向グラフが与えられます。 i 番目の辺は頂点 ci と頂点 diを結んでいます。
# はじめ、頂点 iには値 ai が書かれています。あなたは次の操作を 0 回以上行うことで、操作後の各頂点の値をそれぞれ b1,⋯,bNにしたいと思っています。
# 辺を 1つ選ぶ。選んだ辺が頂点 x と頂点 y を結んでいるとしたとき、次のいずれかを選んで行う。
# 値 axを −1 し、値 ay を +1 する
# 値 axを +1 し、値 ay を −1 する
# 適切に操作を行うことで目的を達成することが可能かどうかを判定してください。
# 制約

# 1≤N≤2×105
# 0≤M≤2×105
# −109≤ai,bi≤109
# 1≤ci,di≤N
# 与えられるグラフは単純グラフである。すなわち、自己ループや多重辺は存在しない。
# 入力はすべて整数である。

# 3 2
# 1 2 3
# 2 2 2
# 1 2
# 2 3

N,M = input().split(" ")
N = int(N) #頂点の数
M = int(M) #辺の数
a = [0]
b = [0]
xa = [int(i) for i in input().split(" ")]
xb = [int(i) for i in input().split(" ")]
a.extend(xa)
b.extend(xb)
G = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    c,d = input().split(" ")
    c = int(c)
    d = int(d)
    G[c][d] = 1
    G[d][c] = 1
flag = 0
if a==b:
    print("yes")
elif sum(a) != sum(b):#一致しなければだめ
    print("no")
else:#もしも一致したら
    for i in range(1,N+1):
        if a[i] != b[i]:
            G[i] = [0 if j < i else G[i][j] for j in range(0,N+1)]
            if 1 in G[i]:
                j = G[i].index(1)
                sub = b[i] - a[i]
                a[i] += sub #a[i]を合わせる
                a[j] -= sub #a[j]で無理やり調整
                print(a)
                print(b)
                if a == b:
                    
                    print("yes")
                    flag = 1
                    break
    if flag == 0:
        print("no")