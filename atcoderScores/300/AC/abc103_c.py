# N 個の正整数 a1,a2,...,aN が与えられます。
# 非負整数 m に対して、f(m)=(m mod a1)+(m mod a2)+...+(m mod aN) とします。
# ここで、X mod Y は X を Y で割った余りを表します。

# f の最大値を求めてください。
# 制約

# 入力は全て整数である
# 2≤N≤3000
# 2≤ai≤10^5

# 3
# 3 4 6
# N = 3
# a = [3,4,6]
N = int(input())
a = map(int,input().split(" "))
b = [i-1 for i in a]
print(sum(b))
# AC 10
