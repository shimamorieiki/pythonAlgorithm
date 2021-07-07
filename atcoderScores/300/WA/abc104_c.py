# プログラミングコンペティションサイト AtCode は、アルゴリズムの問題集を提供しています。
# それぞれの問題には、難易度に応じて点数が付けられています。
# 現在、1 以上 D 以下のそれぞれの整数 i に対して、100i 点を付けられた問題が pi 問存在します。
# これらの p1+…+pD 問が AtCode に収録された問題のすべてです。
# AtCode のユーザーは 総合スコア と呼ばれる値を持ちます。 ユーザーの総合スコアは、以下の 2 つの要素の和です。
# 基本スコア: ユーザーが解いた問題すべての配点の合計です。
# コンプリートボーナス: 100i 点を付けられた pi 問の問題すべてを解いたユーザーは、基本スコアと別にコンプリートボーナス ci 点を獲得します (1≤i≤D)。
# AtCode の新たなユーザーとなった高橋くんは、まだ問題を 1 問も解いていません。
# 彼の目標は、総合スコアを G点以上にすることです。
# このためには、少なくとも何問の問題を解く必要があるでしょうか？
# 制約
# 1≤D≤10
# 1≤pi≤100
# 100≤ci≤10^6
# 100≤G

# 入力中のすべての値は整数である。
# ci,G はすべて 100 の倍数である。
# 総合スコアを G点以上にすることは可能である。

# 2 700
# 3 500
# 5 800

# 3

# 二回目の解答
D,G = map(int,input().split(" "))
score = []
bonus = []
for i in range(D):
    p,c = map(int,input().split(" "))
    score.append(p)
    bonus.append(c)
for i in range(1000):
    for j in range(D):
        total = (j+1)*score[j]       

# N問を解いたときの合計点の最高がM点
# 何も思いつかない。
# DPか〜〜〜。
# 出てくる文字の桁数を落とせば計算量が間に合うらしい
# 下の解法でも解けそう。惜しかった。

#一回目の解答
D,G = 2,700
a = [[3,500],[5,800]]
b = [i[0] for i in a]
# D,G = map(int,input().split(" "))
# a =[]
# for i in range(D):
#     a.append(list(map(int,input().split(" "))))
# a.append([])
resmax = 0
count = 0
while resmax < G:
    count += 1
    for i in range(D):
        if b[i]:
            pass   


# X問を解いたときの最高点数 最高でも1000問しかないし
# X問を解いたときとX+1問を解いたときの問題が全く違う可能性がある
# 全く思いつかない

# 中途半端に解く配点は1種類以下であり、それ以外の配点は完全に解くかまったく解かない。
# 中途半端に解く配点があるなら、それは完全に解く配点以外の配点の中で最も高い配点である。
# 確かに......
