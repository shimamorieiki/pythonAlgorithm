# 最低でも#が2つ以上連続しているところに1手目を置かないと可能性は0
# 斜めは (N-6) * (N-6) のマスを探索し
# それぞれで対角線上の#の個数を求める(N^2には間に合う)
# というか単純に(0,0)から(N-6,N)までの全ての始点について縦横斜めの6連続にある
# #の個数を求めれば済む話なのでは？

N = int(input())
S = []
for _ in range(N):
    S.append(input())

dp_yoko = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            dp_yoko[i][j] += 1
        if j >= 1:
            dp_yoko[i][j] += dp_yoko[i][j - 1]

for i in range(N):
    for j in range(5, N):
        if j == 5 and dp_yoko[i][j] >= 4:
            print("Yes")
            exit()
        if dp_yoko[i][j] - dp_yoko[i][j - 6] >= 4:
            print("Yes")
            exit()

dp_tate = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            dp_tate[i][j] += 1
        if i >= 1:
            dp_tate[i][j] += dp_tate[i - 1][j]

for i in range(5, N):
    for j in range(N):
        if i == 5 and dp_tate[i][j] >= 4:
            print("Yes")
            exit()
        if dp_tate[i][j] - dp_tate[i - 6][j] >= 4:
            print("Yes")
            exit()

for i in range(N - 5):
    for j in range(N - 5):
        r = [
            S[i][j],
            S[i + 1][j + 1],
            S[i + 2][j + 2],
            S[i + 3][j + 3],
            S[i + 4][j + 4],
            S[i + 5][j + 5],
        ]
        l = [
            S[i + 5][j],
            S[i + 4][j + 1],
            S[i + 3][j + 2],
            S[i + 2][j + 3],
            S[i + 1][j + 4],
            S[i][j + 5],
        ]
        if r.count("#") >= 4 or l.count("#") >= 4:
            print("Yes")
            exit()


print("No")

# AC 実装にだいぶ時間がかかってしまった
# 累積和を使って無駄な一般化をしてしまったみたい
# 計算量を正しく見積もれば全探索でも通ることが分かるので
# 今後は気を配るようにする(Cの解法にしては複雑なことを見抜かないといけない)
