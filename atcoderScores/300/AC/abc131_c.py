# 整数 A,B,C,D が与えられます。
# A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
# 制約
# 1≤A≤B≤10^18
# 1≤C,D≤10^9
# 入力はすべて整数である

# 4 9 2 3

# 2

import math
A,B,C,D = map(int,input().split(" "))

lcmCD = (C*D)//math.gcd(C,D)
aCorD = (A-1)//C + (A-1)//D - (A-1)//lcmCD
bCorD = B//C + B//D - B//lcmCD
print(B - bCorD - (A - 1 - aCorD))

# AC 10