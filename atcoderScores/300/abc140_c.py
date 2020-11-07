# 長さ N の値の分からない整数列 A があります。
# 長さ N−1 の整数列 B が与えられます。
# このとき、Bi≥max(Ai,Ai+1) が成立することが分かっています。
# A の要素の総和として考えられる値の最大値を求めてください。
# 制約
# 入力は全て整数
# 2≤N≤100
# 0≤Bi≤10^5

# 3
# 2 5

# 9

# N = 3
# b = [2,5]

N = int(input())
b = list(map(int,input().split(" ")))
m = b[0] + b[-1]
for i in range(N-2):
    m += min(b[i],b[i+1])
print(m)

# AC 13