# とある世界では、今日はクリスマスイブです。

# 高羽氏の庭には N 本の木が植えられています。
# i 本目の木 (1≤i≤N) の高さは hiメートルです。

# 彼は、これらの木のうち K 本を選んで電飾を施すことにしました。
# より美しい光景をつくるために、できるだけ近い高さの木を飾り付けたいです。
# より具体的には、飾り付ける木のうち最も高いものの高さを hmaxメートル、
# 最も低いものの高さを hmin メートルとすると、hmax−hmin が小さいほど好ましいです。
# hmax−hmin は最小でいくつにすることができるでしょうか？
# 制約
# 2≤K<N≤105
# 1≤hi≤109
# hiは整数である。

# 5 3
# 10
# 15
# 11
# 14
# 12

# 2
# N = 5
# K = 3
# a = [10,15,11,14,12]

N,K = map(int,input().split(" "))
a = []
for i in range(N):
    a.append(int(input()))

a.sort()
res  ="undef"
for i in range(N-K+1):
    if res == "undef":
        res = a[K-1]-a[0]
    else:
        res = min(res,a[K-1]-a[0])
    del a[0]
print(res)

# AC 15