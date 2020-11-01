# joisinoお姉ちゃんは、ある商店街に店を開こうとしています。

# その商店街の店は、月曜日から金曜日の 5つの曜日を午前と午後の 2 つの時間帯に分けて、
# これら 10 個の時間帯それぞれについて店を営業するか否かを決めることとなっています。
# ただし、1つ以上の時間帯で店を営業しなければなりません。

# 商店街には既に N個の店があり、1 から Nまでの番号がついています。

# これらの店の営業時間の情報として Fi,j,k が与えられ、
# 月曜日 = 曜日 1、火曜日 = 曜日 2、水曜日 = 曜日 3、木曜日 = 曜日 4、金曜日 = 曜日 5、
# 午前 = 時間帯 1、午後 = 時間帯 2 と対応させたとき、
# Fi,j,k=1 なら曜日 j の時間帯 k に店 i が営業しており、
# Fi,j,k=0 なら営業していないことを意味します。

# 店 i とjoisinoお姉ちゃんの開く店の両方が営業している時間帯の個数を ci としたとき
# joisinoお姉ちゃんの店の利益は P1,c1+P2,c2+...+PN,cN となります。
# ただし、利益は負にもなりうることに注意してください。

# 1つ以上の時間帯で店を営業しなければならないことに注意しつつ、
# 10個の時間帯それぞれについて店を営業するか否かを決めるとき、
# joisinoお姉ちゃんの店の利益のあり得る最大値を求めてください。

# 制約
# 1≦N≦100
# 0≦Fi,j,k≦1
# 1≦i≦N を満たす全ての整数 i に対して、Fi,j,k=1 を満たす (j,k) が必ず 1つ以上存在する
# −10^7≦Pi,j≦10^7
# 入力は全て整数

# 1
# 1 1 0 1 0 0 0 1 0 1
# 3 4 5 6 7 8 9 -2 -3 4 -2

# 8


N = int(input())
# N = 1
shop = []
value = []


for i in range(N):
    x = list(map(int,input().split(" ")))
    shop.append(x)
for i in range(N):
    x = list(map(int,input().split(" ")))
    value.append(x)
shop.append([])
value.append([])

scoreMax = "undef"
for i in range(1,1024):
    score = 0
    iarry = list(map(int,list(format(i,"010b"))))
    for j in range(len(shop[:-1])):
        c=0
        for k in range(10):
            if shop[j][k] == iarry[k] and iarry[k]==1:
                c+=1
        score += value[j][c]
    if scoreMax == "undef":
        scoreMax = score
    else:
        scoreMax = max(score,scoreMax)
print(scoreMax)
# 店出すかどうかは高々1024通りしかないのよな
# 総当りするかな

# 二進数の変換 and で同時に出店してる店の個数を求めて
# それぞれを計算して和を求め1023個のうちの最大を答えにしようとした
# 二進数のandが上手く働かなかったのでlistの1の個数を調べるあんまり頭が良くない解法になってしまった

# AC 60以上