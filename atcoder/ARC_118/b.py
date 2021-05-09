# 3 7 20
# 1 2 4
import math
K,N,M = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
b = [] # 整数部分
c = [] # 小数部分
d = 0  # 和
count = 0
for i in a:
    n = M * i / N
    m = math.floor(n)
    l = n - m
    b.append(m)
    c.append([(m / M) - (i/N),count])
    d += m
    count +=1
for i in range(M-d):
    c = sorted(c)
    b[c[i][1]] += 1
    c[i][0] += 1/M
print(" ".join(map(str,b)))

# maxのminは二分探索らしいけど、答えが整数値じゃないから無理じゃない？
# 全体的には貪欲法でそんなに問題ないと思ってたけど。
# これで貪欲じゃないと言われたら悲しいし、貪欲だったら、実装力がゴミということで
# 二回以上同じものに追加することがあるのかと聞かれたら、なさそうだけどありそう

# dpなのか？