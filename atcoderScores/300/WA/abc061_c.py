# 空の配列が 1 つあります。
# この配列に、整数を配列に挿入する操作を N 回行います。
# i(1≦i≦N) 回目の操作では、配列に整数 ai を bi 個挿入します。
# N 回の挿入操作後の配列の中で、K 番目に小さい数を求めてください。
# 例えば、配列が {1,2,2,3,3,3} の時、4 番目に小さい数は 3

# となります。
# 制約

# 1≦N≦10^5

# 1≦ai,bi≦10^5
# 1≦K≦b1…+…bn
# 入力は全て整数である。 

# N K
# a1 b1
# :
# aN bN

# 3 4
# 1 1
# 2 2
# 3 3

# 3

N,K = map(int,input().split(" "))
l = []
for i in range(N):
    a,b = map(int,input().split(" "))
    l.append([a,b])

limited = [l[0][0] for j in range(l[0][1])]
del l[0]
for i in l:
    if i[0]>=limited[-1]:
        pass
    else:
        ex = [i[0] for j in range(i[1])]
        limited.extend(ex)
        limited = sorted(limited)
        if len(limited) >= K:
            limited = limited[0:K]
print(limited[K-1])

# 原因は分かってるんだけど解決法が思いつかない
# AC 解答見た
# バケツソートとはなんですか