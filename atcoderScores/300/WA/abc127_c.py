# N 枚の ID カードと M 個のゲートがあります。

# i 番目のゲートは Li,Li+1,...,Ri 番目の ID カードのうちどれか 1 枚を持っていれば通過できます。
# 1 枚だけで全てのゲートを通過できる ID カードは何枚あるでしょうか。
# 制約
# 入力は全て整数である。
# 1≤N≤10^5
# 1≤M≤10^5
# 1≤Li≤Ri≤N

# 4 2
# 1 3
# 2 4

# 2

N,M = 4,2
N,M = map(int,input().split(" "))
a = []
for i in range(M):
    a.append(list(map(int,input().split(" "))))
a.append([])

l = set([i for i in range(a[0][0],a[0][1]+1)])
for i in a[1:-1]:
    l = set([j for j in range(i[0],i[1]+1)]) & l
print(len(l))

# 10^10なら見つかるけどそれより計算量を落とすにはどうすればいいんだろうか
# 多分上は合ってるんだけどTLE
# AC 解答みた なるほど理解した
