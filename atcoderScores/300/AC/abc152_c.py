# 1,…,N の順列 P1,…,PN が与えられます。
# 次の条件を満たす整数 i(1≤i≤N) の個数を数えてください。
# 任意の整数 j(1≤j≤i) に対して、 Pi≤Pj

# 制約
# 1≤N≤2×10^5
# P1,…,PN は 1,…,N の順列である。
# 入力はすべて整数である。

# 5
# 4 2 5 1 3

# 3

N = int(input())
a = list(map(int,input().split(" ")))
m  = a[0]
count = 1
for i in range(1,N):
    if a[i] < m:
        m = a[i]
        count+=1
print(count)
# AC 7
# 解けたは解けたけどこれは何をしてるんだろうね