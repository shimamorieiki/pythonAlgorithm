# 多分、これで問題になっているのって
# TTTTの時はPCPCの方がTPCTよりたくさん置けるよねだと思う。

H,W = map(int,input().split(" "))
S = []
for i in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W-1):
        if S[i][j] == "T" and S[i][j+1] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"
for i in S:
    print("".join(i))