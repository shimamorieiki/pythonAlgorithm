# 直感的にビット全探索を思った
# 交点に黒がある場合は二重で削除することになる

H, W, K = map(int, input().split(" "))
C = []
for _ in range(H):
    C.append(input())

row_black = [0] * H
col_black = [0] * W
blacks = set()
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            row_black[i] += 1
            col_black[j] += 1
            blacks.add(int(str(i) + str(j)))

n = H + W
count = 0
for i in range(2 ** (H + W)):
    row_paste = []
    col_paste = []
    reds = set()
    b_num = 0
    B = "{0:0>{1}s}".format(format(i, "b"), n)
    ROW = B[:H]
    COL = B[H:]
    for row_index in range(H):
        if ROW[row_index] == "1":
            b_num += row_black[row_index]
            row_paste.append(row_index)
    for col_index in range(W):
        if COL[col_index] == "1":
            b_num += col_black[col_index]
            col_paste.append(col_index)
    for p in row_paste:
        for q in col_paste:
            reds.add(int(str(p) + str(q)))
    if len(blacks) - b_num + len(reds & blacks) == K:
        count += 1

print(count)

# AC 40
# ただの実装問題にしては時間がかかりすぎ
# 面倒くさいことを考えずに対象を実際に塗りつぶせばよかったのか
