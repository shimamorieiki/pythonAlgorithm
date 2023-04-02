# いわゆるDFS(深さ優先探索)ですかね？
# 再帰でない方法で実装したいですね
# stackを使って実装したらTLEなんだが？
# というかGを作る時点ですでにTLEなのか

N = int(input())
A = []
B = []

for i in range(N - 1):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

G = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N - 1):
    G[A[i] - 1][B[i] - 1] = 0
    G[B[i] - 1][A[i] - 1] = 0

routes = []
stack = [1]
while len(stack) > 0:
    now_at = stack.pop()
    routes.append(now_at)
    for i in range(N):
        if G[now_at - 1][i] == 0:
            # 1つ積んだらその積んだものを調べる
            stack.append(now_at)
            stack.append(i + 1)
            G[now_at - 1][i] = 1
            G[i][now_at - 1] = 1
            break

print(" ".join([str(i) for i in routes]))

# WA 木のDFSとやららしい
# 精進します。
