# 左右一列に N 個のマスが並んでおり、左から i 番目のマスの高さは Hi です。
# あなたは各マスについて 1 度ずつ次のいずれかの操作を行います。
# マスの高さを 1 低くする。
# 何もしない。
# 操作をうまく行うことでマスの高さを左から右に向かって単調非減少にできるか求めてください。
# 制約
# 入力は全て整数である。
# 1≤N≤10^5
# 1≤Hi≤10

# 4
# 1 3 2 1

# N = 4
# h = [1,3,2,1]
N =int(input())
h = list(map(int,input().split(" ")))
m = h[0]
flag = 0
for i in range(1,N):
    if m - h[i] >= 2:
        flag = 1
        break
    else:
        m = max(m,h[i])
print("Yes" if flag == 0 else "No")

# AC 13