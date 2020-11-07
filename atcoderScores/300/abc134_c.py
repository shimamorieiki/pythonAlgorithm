# 長さ N の数列 A1,A2,...,AN が与えられます。
#  1 以上 N 以下の各整数 i に対し、次の問いに答えてください。
# 数列中の Ai を除く N−1 個の要素のうちの最大の値を求めよ。

# 制約
# 2≤N≤200000
# 1≤Ai≤200000
# 入力中のすべての値は整数である。

# 3
# 1
# 4
# 3

# 4
# 3
# 4

# N = 3
# a = [1,4,3]

N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
maxnum = sorted(a)[-1]
second = sorted(a)[-2]

for i in a:
    if i == maxnum:
        print(second)
    else:
        print(maxnum)

# AC 10