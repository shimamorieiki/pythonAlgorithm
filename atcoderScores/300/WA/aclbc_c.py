# UF木っぽさを感じる
# 要は閉じたグループがいくつあるかを判定すればよい
# 幅優先で行ける気がする

import queue

N, M = map(int, input().split(" "))
A = []
B = []

q = queue.Queue()
for _ in range(M):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

R = [-1] * N
G = [[0 for _ in range(N)] for _ in range(N)]
for a, b in zip(A, B):
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

print(G)
num = 0
q.put(0)

while q.qsize() > 0:
    v = q.get()
    print(v)
    if R[v] != -1:
        continue
    R[v] = num
    for i, value in enumerate(G[v]):
        if value == 1:
            q.put(i)
print(num, R)

# 全部連結されていないかどうかが分からない
# WA
# やっぱりそういうこと。それはそうとしてDFS,BFSでも解けるので勉強不足
