H,W,D = map(int,input().split(" "))
A = []
for i in range(H):
    A.append(list(map(int,input().split(" "))))

Q = int(input())
LR = []
for i in range(Q):
    LR.append(list(map(int,input().split(" "))))

# Aを値を昇順のリストに変換する
b = []
for h in range(H):
    for w in range(W):
        b.append([A[h][w],h,w])

b.sort()
# Dが全部で同じなので、相変わらずrまでからlまでを引けば良い
# c[i]は1からiまでのD個飛ばしたときのスコアの和
# D = 3 のとき c[4] = 1-4 c[10] = 1-4-7-10
# 4-10 のスコアが知りたければ c[10] - c[4]
c = [0]*(H*W)

for i in range(H*W-D):
    c[i+D] = c[i] + abs(b[i+D][1]-b[i][1]) + abs(b[i+D][2]-b[i][2])

for l,r in LR:
    ans = c[r-1] - c[l-1]
    print(ans)

# AC45