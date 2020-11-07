# on と off の状態を持つ N 個の スイッチと、M 個の電球があります。
# スイッチには 1 から N の、電球には 1 から M の番号がついています。

# 電球 i は ki 個のスイッチに繋がっており、スイッチ si1,si2,...,siki のうち 
# on になっているスイッチの個数を 2 で割った余りが pi に等しい時に点灯します。
# 全ての電球が点灯するようなスイッチの on/off の状態の組み合わせは何通りあるでしょうか。
# 制約
# 1≤N,M≤10
# 1≤ki≤N
# 1≤sij≤N
# sia≠sib(a≠b)
# pi は 0 または 1
# 入力は全て整数である

# 2 2
# 2 1 2
# 1 2
# 0 1

# 1

N,M = map(int,input().split(" "))
k = []
for i in range(M):
    k.append(list(map(int,input().split(" "))))
k.append([])
p = list(map(int,input().split(" ")))

res = 0
for i in range(pow(2,N)):
    v = [int(i) for i in str(bin(i)).replace("0b","").rjust(10,"0")]
    v.reverse()
    count = 0
    z = 0
    for m in range(len(k)-1):
        for j in k[m][1:]:
            if v[j-1]==1:
                count +=1
        if count % 2 == p[m]:
            z += 1
    if z == len(k)-1:
        res += 1
print(res)
# たかだか1024通りしかないんだから全列挙でいいんじゃない？
# AC 方針はいいけど上手く行かなかった