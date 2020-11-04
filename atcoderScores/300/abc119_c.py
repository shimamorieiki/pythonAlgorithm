# あなたは N 本の竹を持っています。これらの長さはそれぞれ l1,l2,...,lN です (単位: センチメートル)。
# あなたの目的は、これらの竹のうち何本か (全部でもよい) を使い、長さが A,B,C
# であるような 3 本の竹を得ることです。
# そのために、以下の三種類の魔法を任意の順に何度でも使うことができます。
# 延長魔法: 1 MP (マジックポイント) を消費し、1 本の竹を選んでその長さを 1 増やす。
# 短縮魔法: 1 MP を消費し、1 本の長さ 2 以上の竹を選んでその長さを 1 減らす。
# 合成魔法: 10 MP を消費し、2 本の竹を選んで接続し 1 本の竹とする。
# この新たな竹の長さは接続した 2 本の竹の長さの合計に等しい。
# (以後、この竹に対してさらに魔法を使用することもできる。)

# 目的を達成するには、最小でいくつの MP が必要でしょうか？
# 制約
# 3≤N≤8
# 1≤C<B<A≤1000
# 1≤li≤1000
# 入力される値はすべて整数である。

# 5 100 90 80
# 98
# 40
# 30
# 21
# 80

# 23

# AC 意味がわからんかった
# とりあえず全探索すりゃいいのはわかったけど全くしっくりこない
