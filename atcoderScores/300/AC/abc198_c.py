# (0,0)と(X,Y)の距離をRで割ればよい
import math

R, X, Y = map(int, input().split(" "))

if X * X + Y * Y < R * R:
    print(2)
    exit()
print(math.ceil(math.sqrt(X * X + Y * Y) / R))

# AC 10
