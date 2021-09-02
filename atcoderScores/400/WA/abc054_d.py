# イルカは、微量の物質Cを生成したいと考えています。
# 物質Cを生成するためには、タイプAの物質とタイプBの物質の混合比が Ma:Mb となる溶液を用意する必要があります。
# しかし、イルカは薬品を1つも持っていないため、薬局へ薬品を買いに行くことにしました。
# 薬局では、N 種類の薬品を取り扱っており、各薬品 i の在庫はちょうど1つです。
# 各薬品 i は、タイプAの物質 ai グラム、タイプBの物質 bi グラム含んでおり、価格 ci 円で売られています。
# イルカは、いくつかの薬品を薬局で買います。買った薬品は全て使わなければなりません。
# 物質Cを生成するために、必要な最小予算を求めてください。
# 薬局で売られている薬品の組み合わせで、物質Cを生成できない場合はそれを報告してください。
# 制約
# 1≦N≦40
# 1≦ai,bi≦10
# 1≦ci≦100
# 1≦Ma,Mb≦10
# gcd(Ma,Mb)=1
# ai、bi、ci、Ma、Mbは整数である。

# 3 1 1
# 1 2 1
# 2 1 2
# 3 3 10

# 3
import math

N,Ma,Mb = map(int,input().split(" "))
l = []
for i in range(N):
    l.append(list(map(int,input().split(" "))))
l.append([])

# ra = [[0]*11]
# ra.extend([[math.inf]*11 for i in range(11)])
# for i in ra:
#     i[0] = 0
ra = [[math.inf]*11 for i in range(11)]
ra[0][0]=0

for i in l[:-1]:
    rac = ra.copy()
    for a in range(1,11):
        for b in range(1,11):
            if (a-i[0]>=0 and b-i[1]>=0):
                if ra[a-i[0]][b-i[1]]!= math.inf:
                    val = ra[a-i[0]][b-i[1]]+i[2]
                else:
                    val = math.inf
            else:
                val = math.inf
            rac[a][b] = min(ra[a][b],val) #現在の値と新しい値のうち小さいほう
    ra = rac.copy()
res = "undef"
for a in range(1,11):
    for b in range(1,11):
        if a//math.gcd(a,b) == Ma and b//math.gcd(a,b) == Mb:
            if res == "undef":
                res = ra[a][b]
            else:
                res = min(ra[a][b],res)
if res == math.inf:
    print(-1)
else:
    print(res)
# print(ra[Ma][Mb])
# 40個の薬品それぞれについて取るか取らないかは2^40でオーバーするから方針が悪い
# 値段ごとで行けるかいけないかなら少しは方針がいいか？ 40通り
# Ma:Mb でdpすべきか 多分これ
# AC 諦めた
# 方針は合ってたみたいだけどdpの実装が上手く行かなかったみたい