# Tが高々10個しかないのでそれは救い
# N が　9*10^18 とかなり大きいので愚直な方針はダメそう
# 素数 p^2 が出てくるのでここが攻めやすそう
# 多分二分探索なんだろうなということが分かった
# p が小さいときは上を削れるから良いとして、
# p が大きいときは結局 p_minからp_maxまでを全部調べる必要がありそこが遅い
import math

T = int(input())
Tests = []
for i in range(T):
    Tests.append(int(input()))

for test in Tests:
    p_min = 2
    p_max = test
    while True:
        p_mid = math.ceil((p_max + p_min) / 2)
        if p_mid * p_mid > test:
            p_max = p_mid
            continue
        for p in range(p_min, p_max):
            div, mod = divmod(test, p * p)
            if mod == 0:
                print("{} {}".format(p, div))
                break
        else:
            continue
        break

# WA 確かにそれはそうすぎる
