# 最大でも街の数*2(=N*2)通りの魔法を使えれば題意を満たす
# そのうえで互いに素になるように規則を絞ればよい
# (1,2) と (2,4) は同じなので (1,2) を採用する

from itertools import combinations
import math

N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split(" "))

    X.append(x)
    Y.append(y)

routes = set()

for i, j in combinations(range(N), 2):
    gcd = math.gcd(abs(X[i] - X[j]), abs(Y[i] - Y[j]))
    routes.add(str((X[i] - X[j]) // gcd) + str((Y[i] - Y[j]) // gcd))
    routes.add(str((X[j] - X[i]) // gcd) + str((Y[j] - Y[i]) // gcd))

print(len(routes))

# WA 解けているはずなのになぜかだめ
