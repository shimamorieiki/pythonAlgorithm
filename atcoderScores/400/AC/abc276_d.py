# N個の数の最大公約数を求める
# それぞれをgcdで割って、3,2

import functools
import math

N = int(input())
A = list(map(int, input().split(" ")))


def gcd(*integers):
    return functools.reduce(math.gcd, integers)


def div_n(i, n):
    for j in range(50):
        if i % n == 0:
            i //= n
        else:
            return i, j


gcd_ = gcd(*A)
c = 0
for i in range(N):
    a = A[i] // gcd_
    a, div_3 = div_n(a, 3)
    a, div_2 = div_n(a, 2)
    if a != 1:
        print(-1)
        exit()
    else:
        c += div_3 + div_2
print(c)

# AC 24m
# そういうことっぽい
