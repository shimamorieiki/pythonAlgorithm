# ある銀行では、お金の引き出しを難しくするために、
# 一回の操作で引き出せる金額が以下のいずれかとなっています。

# 1円
# 6円、6^2(=36) 円、6^3(=216) 円、...
# 9円、9^2(=81) 円、9^3(=729) 円、...

# この銀行からちょうど N 円を引き出すには少なくとも何回の操作が必要か求めてください。

# ただし、一度引き出したお金を再び預け入れてはならないとします。
# 制約

# 1≤N≤100000

# N は整数

# 127
# 4
import math
N = int(input())

max6 = int(math.log(N,6))
max9 = int(math.log(N,9))
l6 = [pow(6,i) for i in range(max6+1)]
l9 = [pow(9,i) for i in range(max9+1)]
l6.extend(l9)
a= sorted(list(set(l6)))
res = a.copy()
temp = []
count=1
while N not in res:
    count+=1 
    for i in a:
        temp.extend([j+i for j in res])
    res = list(set(temp.copy()))
print(count)


# いいと思ったけどN*Nで回してしまう
# バケツ的な回し方をすれば多分計算量Nでいいと思う
# 1回で取りうる値を入れる
# 2回目で取りうるものは一回で取りうるものにマージ
# これでいいと思ったけど普通にオーバーしてしまった
# n進法の考え方でやればいいらしいけど意味がわからん
# AC 解答見た