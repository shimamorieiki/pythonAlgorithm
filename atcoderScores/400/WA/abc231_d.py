# 閉路があるとダメ、1人に3人が結びつくとダメ
# 閉路判定をしようとしたけどunion-findなのか
# DFS をしようとしたけど N^2 は TLE なのでだめっぽい

N, M = map(int, input().split(" "))
A = []
B = []
for _ in range(M):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

print(N, M, A, B)

# WA
# UnionFindを勉強します
