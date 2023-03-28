# A = 1000 だと B = 999 の時でも
# A^5 - B^5 が 10^12のオーダーなので、
# Aは最大でも1000
import math

X = int(input())
is_minus = False
for a in range(1, 1000):
    b = pow(a, 5) - X
    if X - pow(a, 5):
        is_minus = True
    b_5 = abs(b)
    b__2 = int(math.sqrt(b_5))
    b__4 = int(math.sqrt(b__2))
    b__8 = int(math.sqrt(b__4))
    for i in range(b__8, b__4 + 1):
        if pow(i, 5) == b_5:
            if is_minus:
                print(str(a) + " " + str(-i))
            else:
                print(str(a) + " " + str(i))
            exit()

# WA
# そういうことなんだけど精度が不十分
