# イルカは x 軸正方向を右、y 軸正方向を上とする 2 次元座標平面にいます。
# イルカは現在点 (sx,sy) にいて、1 秒あたり上下左右に距離 1 だけ進むことができます。
# このとき、移動前と移動後の x 座標、y 座標はともに整数でなければなりません。
# イルカはここから sx<tx と sy<ty を満たす点 (tx,ty) に行き、
# その後点 (sx,sy) に戻り、また点 (tx,ty) に行き、その後点 (sx,sy) に戻ります。
# このとき、イルカは点 (sx,sy) と点 (tx,ty) を除いて、
# 途中で同じ座標を複数回通らないように移動しなければなりません。
# このような条件を満たすイルカの最短経路を 1つ求めてください。
# 制約
#−1000≦sx<tx≦1000
# −1000≦sy<ty≦1000
# sx,sy,tx,ty は整数である。

# sx sy tx ty
# 0 0 1 2
# UURDDLLUUURRDRDDDLLU
def rep(c,num):
    s =  ""
    for i in range(num):
      s = s + c  
    return s

sx,sy,tx,ty = map(int,input().split(" "))
dx = tx - sx
dy = ty - sy
print(
    rep("R",dx)+rep("U",dy)+
    rep("L",dx)+rep("D",dy)+
    rep("D",1)+rep("R",dx+1)+rep("U",dy+1)+rep("L",1)+
    rep("U",1)+rep("L",dx+1)+rep("D",dy+1)+rep("R",1)
)
# AC16