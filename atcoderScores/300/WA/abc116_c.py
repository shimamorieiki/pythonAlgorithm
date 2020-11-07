# 花壇に N 本の花が咲いており、それぞれ 1,2,......,N と番号が振られています。
# 最初、全ての花の高さは 0 です。 数列 h={h1,h2,h3,......} が入力として与えられます。
# 以下の「水やり」操作を繰り返すことで、すべての k(1≦k≦N) に対して花 k の高さを hkにしたいです。
# 整数 l,rを指定する。l≦x≦r を満たすすべての x に対して、花 x の高さを 1高くする。

# 条件を満たすための最小の「水やり」操作の回数を求めてください。
# 制約
# 1≦N≦100
# 0≦hi≦100
# 入力はすべて整数である。

# 4
# 1 2 2 1

# 2
def mizuyari(l): #リストを入れて何回でそれが[0,...,0]になるか
    global count
    if l[0]==0:
        del l[0]
    if l[-1] == 0:
        del l[-1]

    if len(l)==1:
        count += l[0]
    elif len(l)==0:
        pass
    else:
        if l.count(0)>0:
            zp = l.index(0)
            mizuyari(l[:zp])
            mizuyari(l[zp:])
        else:
            minl = min(l)
            l = [i - minl for i in l]
            count += minl
            mizuyari(l)

count = 0
N = int(input())
a = list(map(int,input().split(" ")))

mizuyari(a)
print(count)
# 多分再帰でいいと思う
# ほとんどできたけど実行時エラーが出るやつがある。
# 理由がわからん
