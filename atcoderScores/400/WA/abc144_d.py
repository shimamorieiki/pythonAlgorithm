# y度傾けたときの水筒の体積は
# a^2*b*(1- tan(y)/2) (y <= 45度)
# a*b^2/(2tan(y)) (y >= 45度)

import math

A, B, X = map(int, input().split(" "))

if X * 2 >= A * A * B:
    print(math.degrees(math.atan(2 - (2 * X) / (A * A * B))))
else:
    print(math.degrees(math.atan(A * B * B / (2 * X))))

# WA
# 体積の計算もできない馬鹿
