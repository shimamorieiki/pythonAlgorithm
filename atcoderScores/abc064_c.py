# AtCoderでは、コンテストに参加すると「色」が付き、これはレートによって次のように変化します：
# レート 1-399：灰色
# レート 400-799：茶色
# レート 800-1199：緑色
# レート 1200-1599：水色
# レート 1600-1999：青色
# レート 2000-2399：黄色
# レート 2400-2799：橙色
# レート 2800-3199：赤色

# また、レートが 3200以上になると色を自由に変えることができます。
# 現在 N 人の人がAtCoderのコンテストに参加したことがあり、i 人目の人のレートは aiです。
# そのとき、色の種類数の最小値と最大値を求めなさい。
# 制約

# 1≤N≤100
# 1≤ai≤4800
# aiは整数である。

# N
# a1 a2 ... aN

# 4
# 2100 2500 2700 2700

# 2 2

def color(c):
    global rate,ov
    if 1 <= c and c<=399:
        rate[0] += 1
    elif 400 <= c and c<=799:
        rate[1] += 1
    elif 800 <= c and c<=1199:
        rate[2] += 1
    elif 1200 <= c and c<=1599:
        rate[3] += 1
    elif 1600 <= c and c<=1999:
        rate[4] += 1
    elif 2000 <= c and c<=2399:
        rate[5] += 1
    elif 2400 <= c and c<=2799:
        rate[6] += 1
    elif 2800 <= c and c<=3199:
        rate[7] += 1
    elif 3200 <= c and c<=4800:
        ov += 1

ov = 0
rate = [0]*8
resultmin = 0
resultmax = 0
N = int(input())
a = [int(i) for i in input().split()]
for i in a:
    color(i)

zeronum = rate.count(0) #0の個数
if zeronum == 8:#全部3200オーバー
    resultmin = 1
    resultmax = ov
else:
    resultmin = 8-zeronum
    resultmax = 8-zeronum + ov
print(resultmin," ",resultmax)

# これで合ってるはずなのにwaが起こる
# 3200以上の人は元々設定がない色から選べるのね
#AC 30