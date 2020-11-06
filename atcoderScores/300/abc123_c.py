# AtCoder 社は成長し、2028 年になってついに 6 つの都市 
# (都市 1,2,3,4,5,6 ) からなる AtCoder 帝国を作りました！

# AtCoder 帝国には 5 つの交通機関があります。
# 電車：都市 1 から 2 まで 1 分で移動する。1 つの電車には A 人まで乗ることができる。
# バス：都市 2 から 3 まで 1 分で移動する。1 つのバスには B 人まで乗ることができる。
# タクシー：都市 3 から 4 まで 1 分で移動する。1 つのタクシーには C 人まで乗ることができる。
# 飛行機：都市 4 から 5 まで 1 分で移動する。1 つの飛行機には D 人まで乗ることができる。
# 船：都市 5 から 6 までを 1 分で移動する。1 つの船には E 人まで乗ることができる。

# それぞれの交通機関は、各整数時刻 (0,1,2,3,...) に、都市から出発します。
# いま、N 人のグループが都市 1 におり、全員都市 6 まで移動したいです。
# 全員が都市 6 に到着するまでに最短で何分かかるでしょうか？
# なお、乗り継ぎにかかる時間を考える必要はありません。
# 制約

# 1≤N,A,B,C,D,E≤1015
# 入力中の値はすべて整数である。

# 5
# 3
# 2
# 4
# 3
# 5

# 7



# N = int(input())
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())

# c = [0]*7
# c[1] = N
# cp = c.copy()
# count = 0
# while c[6] < N:
#     count+=1
#     cp[1] = c[1]               - min(c[1],A)
#     cp[2] = c[2] + min(c[1],A) - min(c[2],B)
#     cp[3] = c[3] + min(c[2],B) - min(c[3],C)
#     cp[4] = c[4] + min(c[3],C) - min(c[4],D)
#     cp[5] = c[5] + min(c[4],D) - min(c[5],E)
#     cp[6] = c[6] + min(c[5],E) 
#     c = cp.copy()
# print(count)
import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
m = [A,B,C,D,E]
print(math.ceil(N/min(m)) + 4)
# TLEとか言われてるけどそうなんだろうな〜
# 明らかに一番遅いのがボトルネックなので
# AC 42 なんでかと聞かれてもよくわからん
# 確かにおんなじこと言ってる