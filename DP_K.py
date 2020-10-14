# N 個の正整数からなる集合 A={a1,a2,…,aN}があります。
# 太郎君と次郎君が次のゲームで勝負します。
# 最初に、K個の石からなる山を用意します。
# 二人は次の操作を交互に行います。
# 先手は太郎君です。
# Aの元 x をひとつ選び、山からちょうど x個の石を取り去る。
# 先に操作を行えなくなった人が負けです。
# 二人が最適に行動すると仮定したとき、どちらが勝つかを判定してください。
# 入力はすべて整数である。
# 1≤N≤100
# 1≤K≤10^5
# 1≤a1<a2<⋯<aN≤K

# 操作数が固定されていないのに操作数で考える必要はない
# 最適に行動するってことは下手に動くと負ける可能性がある
# d[j]=true 石の数がj個のときに先手に回ってきたときに先手必勝 d[j]=false 後手必勝
# d[j+x] = d[j] if j+x -a[y] < min(a) になるものが存在しない 自分がa[y]を選んだときに相手が勝てない
# N*Nで先手が絶対にどれかを取れる手が作れる

# わからん
# 答え読んだら考え方は同じだった後は実装するだけだった。悔しい


def solve(N,K,a):
    fwin = []
    dp = [0]*(N+1)
    print(N,K,a)
    for i in range(N):
        for j in range(N):
            if (a[i]+a[j] ) not in fwin:
                fwin.append(a[i]+a[j])
    print(fwin)
    for f in fwin:
        dp[]

K = 4
a = [2,3]
N = len(a)

solve(N,K,a)