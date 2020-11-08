# 大きさ N の順列 ((1, 2, ..., N) を並び替えてできる数列) P, Q があります。
# 大きさ N の順列は N! 通り考えられます。
# このうち、P が辞書順で a 番目に小さく、Q が辞書順で b 番目に小さいとして、|a−b| を求めてください。
# 注記
# 2 つの数列 X, Y について、ある整数 k が存在して Xi=Yi (1≤i<k) かつ Xk<Yk が成り立つとき、
# X は Y より辞書順で小さいと定義されます。
# 制約
# 2≤N≤8
# P, Q は大きさ N の順列である。
# 入力は全て整数である。

# 3
# 1 3 2
# 3 1 2

# 3


# N = 3
# P = [1,3,2]
# Q = [3,1,2]

import itertools

N = int(input())
P = list(map(int,input().split(" ")))
Q = list(map(int,input().split(" ")))

a = itertools.permutations(sorted(P))
count = 1
for i in a:
    if P == list(i):
        cp = count
    if Q == list(i):
        cq = count
    count+=1

print(abs(cp-cq))

# AC 9