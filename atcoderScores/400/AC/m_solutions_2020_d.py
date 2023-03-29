# 安いときにめいいっぱい買って高いときにめいいっぱい売る
# 具体的には T[i]を i 日目から i+1 日目の間に
# 株価が上がったら +1
# 下がったら -1
# そのままなら T[i-1]と同じ
# としたときに、
# 1 から -1 となったときに持っている分を全部売り
# -1 から 1 となったときに有り金全部買う


N = int(input())
A = list(map(int, input().split(" ")))
T = []

A.append(0)

for n in range(N):
    if A[n + 1] - A[n] > 0:
        T.append(1)
    elif A[n + 1] - A[n] == 0:
        T.append(0)
    else:
        T.append(-1)

money = 1000
stock = 0
for i in range(N):
    # 次の日に比べると安いので
    # 今持っているお金で買えるだけ株を買う
    if T[i] == 1:
        div, mod = divmod(money, A[i])
        money = mod
        stock += div
    # 次の日に比べると高いので
    # 今持っている株を全部売る
    if T[i] == -1:
        money += stock * A[i]
        stock = 0

print(money)

# AC 40m
# 模範解答はよく分からん
