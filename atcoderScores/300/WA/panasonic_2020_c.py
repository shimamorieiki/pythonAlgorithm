# 何か式変形したらルートが無くなったけどこれでええんか？

# A, B, C = map(int, input().split(" "))
# a = (A - B) ** 2 + (B - C) ** 2 + (C - A) ** 2
# b = A**2 + B**2 + C**2
# if a-b > 0:
#     print("Yes")
# else:
#     print("No")

A, B, C = map(int, input().split(" "))
a = A * A + B * B + C * C
b = 2 * (A * B + B * C + C * A)
if a - b > 0 and C - A - B > 0:
    print("Yes")
else:
    print("No")

# WA 数弱でごめんなさい
# C - A - B > 0 の条件を見逃していた
