# 古代すぬけ国では, AtCoder 社長「高橋君」の権威を高めるために, ピラミッドが建てられていた.
# ピラミッドには 中心座標 (CX,CY) と 高さ H が定まっており, 座標 (X,Y) の高度は max(H−|X−CX|−|Y−CY|,0)であった.

# 探検家の青木君は, このピラミッドの中心座標と高さを求めるために調査を行った. その結果, 次のような情報が得られた.
# CX,CYは 0 以上 100 以下の整数で, H は 1 以上の整数であった.
# 上記と別に N 個の情報が得られた. そのうち i 個目の情報は, 「座標 (xi,yi) の高度は hi である」
# この情報は, ピラミッドの中心座標と高さを特定するのに十分であった. 情報を手掛かりに, これらの値を求めなさい.
# 制約
# Nは 1 以上 100 以下の整数
# xi, yi は 0 以上 100 以下の整数
# hiは 0 以上 10^9 以下の整数
# N 個の座標 (x1,y1),(x2,y2),(x3,y3),...,(xN,yN) はすべて異なる
# ピラミッドの中心座標と高さをちょうど 1 つに特定することができる

# 4
# 2 3 5
# 2 1 5
# 1 2 5
# 3 2 5

#  2 2 6

# 2回目
N = int(input())
a = []
for i in range(N):
    xyh = list(map(int, input().split()))
    a.append(xyh)
    if xyh[2]:
        x, y, h = xyh

for i in range(101):
    for j in range(101):
        H = h+abs(x-i)+abs(y-j)
        if all(h == max(H-abs(x-i)-abs(y-j),0) for x,y,h in a):
            print(i,j,H)
            exit(0)

# 上手く行かなかった原因はHが0になる可能性が残ってたから。
# H>0のものを決めてから比較すればどうにかなりそう

# 1回目
# N = 4
# a = [[2,3,5],[2,1,5],[1,2,5],[3,2,5]]
# a.sort(key=lambda a:a[2])

N = int(input())
a = []
for i in range(N):
   a.append(list(map(int,input().split(" "))))
a.append([])

for cx in range(101):
    for cy in range(101):
        H= "undef"
        for i in a[:-1]:
            x = i[0]
            y = i[1]
            h = i[2]
            if h!=0:
                if H =="undef":
                    H = abs(cx-x) + abs(cy-y) + h
                elif H != abs(cx-x) + abs(cy-y) + h:
                    break
        else:
            print(cx,cy,H)
            break
# 多分だけど Cx,Cyがともに1~100なので単純に二重ループでも10^4程度なので間に合うんだと思う
# それはそうなんだけど、h = 0 のときの扱いが多分だいぶうざい気がする
# なんか上手く行かなかったのはなんでだ
# AC 40 解答見た
# 方針は合ってるはずだけどなんでうまくいかんのや