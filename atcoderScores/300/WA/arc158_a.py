# 3,5,7を足すことは本質ではなくて 0,2,4 を足すことを考える
# あと少しなんだけど 0,x,yまで減らした後が上手く行かない

T = 4
CASE = [
    [2, 8, 8],
    [1, 1, 1],
    [5, 5, 10],
    [10, 100, 1000],
]

for a in CASE:
    i, j, k = sorted(a)
    sum = 0
    j_ = j - i
    k_ = k - i

    # 片方が0になるまで引ききりたい

    if j_ // 2 < k_ // 4:
        # jの方が先に0になる
        j_div = j_ // 2
        j_ = 0
        k_ = k_ - 4 * j_div
    else:
        j_div = k_ // 4
        k_ = j_ - j_div * 2
        j_ = 0

    k_div, k_mod = divmod(k_, 6)
    print(j_, k_, j_div, k_div, k_mod)
    if k_mod == 0:
        print(sum + j_div + k_div * 2)
    else:
        print(-1)

# WA
# 考察が不十分
