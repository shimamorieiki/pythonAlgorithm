# 有向グラフの最短経路なのでベルマンフォードが使えそう。
# ダイクストラが使えないのはなんで？-> グラフに負の辺が含まれるときはベルマンフォード

N,M = map(int,input().split(" "))

# 辺と頂点を管理する
edge = []
edge.append([])
for i in range(M):
    edge.append(list(map(int,input().split(" "))))

# 始点sから各頂点への最短距離を十分大きい数で初期化する
intMax = float('inf')
d = [intMax] * (N+1)

# 負の閉路があるかを判断する
negative = [False]*(N+1)

# s番目の頂点から各頂点への最短距離を求める
def shortest_path(s:int):
    # sからsまでの距離は0
    d[s] = 0
    for _ in range(N-1):
        # 更新したかどうか？
        update = False
        for e in edge[1:]:
            if d[e[0]] != intMax and d[e[1]]>d[e[0]] - e[2]:
                d[e[1]] = d[e[0]] - e[2]
                update = True
        if not update:
            break
    return d

def negative_check(s:int):
    # sからsまでの距離は0
    d[s] = 0
    print("init: ",d)
    for _ in range(N):
        for e in edge[1:]:
            if d[e[0]] != intMax and d[e[1]]>d[e[0]] - e[2]:
                d[e[1]] = d[e[0]] - e[2]
                negative[e[1]]= True
        if negative[e[0]]:
            negative[e[1]] = True
    return negative

ans = shortest_path(1)
negative_check(1)

if negative[N]:
    print('inf')
else:
    print(-ans[N])

# 最短経路問題で頂点間の距離の最大値を求めるときは正負を反転させる-> たしかにそう
# 最短経路問題において負の閉路がある場合は最小値がいくらでも小さくなるので負の閉路を判定するのは重要
# でも最終ゴールまでのどこかで閉路になっていない限り最短経路は変化しないのでは？-> それはそう。だからnegativeはN回回してる
# 閉路がない場合に繰り返しがN-1回でいいことの直感的な理解がまだ腑に落ちてない

# 今回の問題においては正の閉路があると最大値がいくらでも増加してしまう。
# 正負を反転させると「負の閉路」になるので負の閉路判定が使える

# negative_checkの話
# 負の閉路がないときはN-1回しか更新されない。
# ansを求めるときにN-1回の更新をしているので、負の閉路がないときはそこから何回ループしてもそれ以上の更新はされないはず
# ただ、開始点から終了点までのルートのどこかに負の閉路があるときは、更にNループすると終了点が更新される。
# どこかに負の経路があるだけならN回ループを回さなくてもいい。(適当な箇所でnegative = Trueならその点が更新されている。)
# 「開始から終了までのパス」に負の経路があることを確かめるにはN回回さないと判断できない。
# それは「すべての点を必ず1回は通る」ことを保証するのがN-1回だから