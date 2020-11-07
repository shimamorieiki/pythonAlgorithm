# 栄養ドリンクにレーティング上昇効果があると聞いた高橋くんは、
# M 本の栄養ドリンクを買い集めることにしました。

# 栄養ドリンクが売られている店は N 軒あり、
# i 軒目の店では 1 本 Ai 円の栄養ドリンクを Bi 本まで買うことができます。

# 最小で何円あれば M 本の栄養ドリンクを買い集めることができるでしょうか。

# なお、与えられる入力では、十分なお金があれば M 本の栄養ドリンクを買い集められることが保証されます。
# 制約
# 入力は全て整数である。
# 1≤N,M≤10^5

# 1≤Ai≤10^9
# 1≤Bi≤10^5
# B1+...+BN≥M

# 4 30
# 6 18
# 2 5
# 3 10
# 7 9

# 130


N,M = map(int,input().split(" "))
a = []
for i in range(N):
    a.append(list(map(int,input().split(" "))))

if N != 1:
    a.sort()
a.append([])

count = 0
res = 0
for i in a[:-1]:
    num = min(M-count,i[1])
    res += i[0] * num 
    count  += num
    if count >= M:
        break
print(res)

# AC 12