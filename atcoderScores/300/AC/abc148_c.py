# 高橋君はパーティを企画しています。
# パーティーでは参加者に 1 人 1 個以上のお菓子を配る予定です。
# 高橋君は参加者の人数が A 人か B 人のどちらかになるだろうという予想を立てました。
# どちらの場合でも均等に配りきることができるようなお菓子の個数の最小値を求めてください。
# ただし、 1 個のお菓子を分割して複数人で分けることはできないものとします。
# 制約
# 1≤A,B≤105
# A≠B
# 入力はすべて整数

# 2 3

# 6

import math
A,B = map(int,input().split(" "))
print(A*B // math.gcd(A,B))

# 最小公倍数求めるだけやん
# AC 1