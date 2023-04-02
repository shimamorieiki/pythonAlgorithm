# なんか見覚えがあるな
# 4つの点を全列挙すると余裕でTLE
# 左上と右下に相当するものを2つ取ってきて、
# 残り2頂点に相当するものが存在するかを調べる
import itertools

N = int(input())
Z = []

M = set()

for _ in range(N):
    x, y = map(int, input().split(" "))
    Z.append([x, y])
    M.add(str(x) + ":" + str(y))

Z = sorted(Z, key=lambda x: (x[0], x[1]))

count = 0
for lb, rt in itertools.combinations(Z, 2):
    lb_x, lb_y = lb
    rt_x, rt_y = rt
    if lb_x != rt_x and lb_y != rt_y:
        lt = [lb_x, rt_y]
        rb = [rt_x, lb_y]
        if str(lb_x) + ":" + str(rt_y) in M and str(rt_x) + ":" + str(lb_y) in M:
            count += 1
print(count // 2)

# AC 20m
# そういうことらしい
