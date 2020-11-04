# A, C, G, T からなる長さ N の文字列 S が与えられます。
# 以下の Q 個の問いに答えてください。

# 問 i (1≤i≤Q): 整数 li,ri (1≤li<ri≤N) が与えられる。
# S の先頭から li 文字目から ri 文字目までの (両端含む) 部分文字列を考える。
# この文字列に AC は部分文字列として何回現れるか。

# 注記
# 文字列 T の部分文字列とは、T の先頭と末尾から 0 文字以上を取り去って得られる文字列です。
# 例えば、ATCODER の部分文字列には TCO, AT, CODER, ATCODER, (空文字列) が含まれ、AC は含まれません。
# 制約
# 2≤N≤10^5
# 1≤Q≤10^5
# S は長さ N の文字列である。
# S の各文字は A, C, G, T のいずれかである。
# 1≤li<ri≤N

# 8 3
# ACACTACG
# 3 7
# 2 3
# 1 8

# 2
# 0
# 3

# N,Q = 8,3
# s = "ACACTACG"
# a = [[3,7],[2,3],[1,8]]

# for i in a[:-1]:
#     x = s[i[0]-1:i[1]].count("AC")
#     print(x)

# これがTLEなんか言われても知らんがなとは思うけどもまあ仕方ない

# for i in range(N+1): #先頭i文字目までにACが出てきた回数
#     num[i] = s[:i].count("AC")

# for i in a[:-1]:
#     print(num[i[1]] - num[i[0]])

# 長いsについてそれぞれ調べてるからまずいのか

N,Q = map(int,input().split(" "))
s = input()
a = []
num = [0]*(N+1)

for i in range(Q):
    a.append(list(map(int,input().split(" "))))
a.append([])

dp = [0]*(N)
for i in range(1,N): #先頭i文字目までにACが出てきた回数
    if s[i] == "C" and s[i-1] == "A":
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

for i in a[:-1]:
    print(dp[i[1]-1] - dp[i[0]-1])

# 今回は見抜けたけど常にdpは疑う必要がありそう
# 計算量が大きすぎると怒られたけど実質必要なのは一つ前との関係だけなのでdpを使えばいい
# AC 35