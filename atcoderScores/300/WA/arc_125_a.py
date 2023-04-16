# a が0(1)のみなのに b が1(0)のみのときはどうやっても作れないので-1
# a が0(1)のみなのに b が0(1)のみのときは現在の状態からbに移すだけなのでM
# それ以外ならどうにでも作れるので手順を考えるべき
# どっちも含まれるということなら0,1が連続する箇所が存在するので
# 入れ替わるたびに +1, 移すのに +1 を行えばよい

N, M = map(int, input().split(" "))
S = list(map(int, input().split(" ")))
T = list(map(int, input().split(" ")))

if S.count(0) == 0 and T.count(1) == 0:
    print(-1)
    exit()

if S.count(1) == 0 and T.count(0) == 0:
    print(-1)
    exit()

if S.count(0) == 0 and T.count(0) == 0:
    print(M)
    exit()

if S.count(1) == 0 and T.count(1) == 0:
    print(M)
    exit()

count = 0

start = S[0]
nearest = min(S.index((start + 1) % 2), list(reversed(S)).index((start + 1) % 2) + 1)

count += nearest
count += M
for i in range(N - 1):
    if S[i] != S[i + 1]:
        count += 1
print(count)

# そういうことのはずなんだけど実装力が足らなかった
# WA 30m
