# 全通りを総当たりすれば良いのはそうなんだけど
# いわゆるビットDP的な雰囲気も感じる

import itertools

H, W = map(int, input().split(" "))
A = []
for _ in range(H):
    A.append(list(map(int, input().split(" "))))

c = 0

for i in itertools.combinations(range(H + W - 2), W - 1):
    S = set()
    h = 0
    w = 0

    for j in range(H + W - 2):
        S.add(A[h][w])
        if j in i:
            w += 1
        else:
            h += 1
    S.add(A[h][w])
    if len(S) == H + W - 1:
        c += 1
print(c)

# AC 30m
# 通るんかい！！
