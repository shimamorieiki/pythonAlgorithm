# AtCoder Beginner Contest 100 の開催にともなって,
#  AtCoder 社では長さ N の数列 a={a1,a2,a3,...,aN} が飾られることになった.
# 社員のすぬけ君は, この数列で遊んでみようと思った.

# 具体的には, 以下の操作をできるだけ多くの回数繰り返そうと思った.

# 1≤i≤Nを満たす全ての iに対して, それぞれ「aiの値を 2 で割る」「aiの値を 3 倍する」のどちらかを行う.  
# ただし, 全ての iに対して 3 倍することはできず, 操作後の ai の値は整数でなければならない.  
# 最大で何回の操作が可能か, 求めなさい.

# 制約

# Nは 1 以上 10 000 以下の整数
# aiは 1 以上 1 000 000 000 以下の整数

# 3
# 5 2 4

# 3

N = int(input())
a = list(map(int,input().split(" ")))

count = 0
for i in reversed(range(1,30)):
    for j in range(N):
        if a[j] % pow(2,i) ==0 and a[j]>= pow(2,i):
            count+=i
            a[j] = 0
print(count)
# 2^30 > 1 000 000 000
# 結局N個の数のうち2で割れる総数
# aiが大きすぎることを心配してるが、これは
# AC 12