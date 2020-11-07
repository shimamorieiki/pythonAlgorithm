# 高橋君は早押しクイズの大会を開くことにしました。
# スコアボードの作成を任されたキザハシ君は、
# 次のルールを持つラウンドのポイントを管理するプログラムを書くのに苦戦しています。

# このラウンドの参加者は N 人であり、1 から N までの番号がついています。
# ラウンド開始時点では全員が K ポイントを持っています。
# 誰かが問題に正解すると、その人以外の N−1 人のポイントが 1 減ります。
# これ以外によるポイントの変動はありません。
# ラウンド終了時にポイントが 0 以下の参加者は敗退し、残りの参加者が勝ち抜けます。

# このラウンドでは Q 回の正解が出て、i 番目に正解したのは参加者 Ai でした。
# キザハシ君の代わりに、
# N 人の参加者のそれぞれが勝ち抜けたか敗退したかを求めるプログラムを作成してください。
# 制約
# 入力はすべて整数
# 2≤N≤10^5
# 1≤K≤10^9
# 1≤Q≤10^5
# 1≤Ai≤N (1≤i≤Q)

# 6 3 4
# 3
# 1
# 3
# 2
# N,K,Q = 6,3,4
# a = [3,1,3,2]

N,K,Q = map(int,input().split(" "))
a = []
for i in range(Q):
    a.append(int(input()))

r = [0]*(N+1)
for i in a:
    r[i] +=1
for i in r[1:]:
    if K -(Q-i) > 0:
        print("Yes")
    else:
        print("No")

# AC 6