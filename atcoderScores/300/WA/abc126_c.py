# すぬけ君は 1 〜 N の整数が等確率で出る N 面サイコロと表と裏が等確率で出るコインを持っています。
# すぬけ君は、このサイコロとコインを使って今から次のようなゲームをします。
# まず、サイコロを 1 回振り、出た目を現在の得点とする。
# 得点が 1 以上 K−1 以下である限り、すぬけ君はコインを振り続ける。
# 表が出たら得点は 2 倍になり、裏が出たら得点は 0 になる。
# 得点が 0 になった、もしくは K 以上になった時点でゲームが終了する。
# このとき、得点が K 以上である場合すぬけ君の勝ち、 0 である場合すぬけ君の負けである。
# N と K が与えられるので、このゲームですぬけ君が勝つ確率を求めてください。
# 制約
# 1≤N≤10^5
# 1≤K≤10^5

# 入力はすべて整数

# 3 10

# 0.145833333333

import math

N,K = map(int,input().split(" "))

pro = 0
for i in range(1,N+1):
    if i < K:
        if math.log((K-i)/i) < 0:
            pro += 1/(2*N)
        else:
            pro += 1/(pow(2,math.ceil(math.log((K-i)/i))+1)*N)
    else:
        pro += 1/N

print(pro)

# AC 33 これでいいはずなのになんかエラーが出てる
# 解答読んだけど意味がわからん。logは使ってないけどおんなじこと言ってる気がする