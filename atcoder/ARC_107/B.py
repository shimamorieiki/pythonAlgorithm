# 整数 N,K が与えられます． 
# 4 つの整数の組 (a,b,c,d)であって，以下の条件を両方満たすものは何個あるでしょうか．

# 1≤a,b,c,d≤N
# a+b−c−d=K

# 制約
# 1≤N≤10^5
# −2(N−1)≤K≤2(N−1)
# 入力される数はすべて整数．

# 2 1
# 4

# a-c + b-d = K
# と捉えるとゆうてそんなに大変じゃない
N,K = map(int,input().split(" "))

# 1,2の組み合わせで1を作る
# 0,1 しかない 偶奇は必要そう
# 2数の差がiになる組み合わせはN-i個
K = abs(K)
count = 0
if K%2==0:
    c = int(K/2)
    for i in range(c):
        count += ((N-i) * (N-(K-i)))*2
    count += (N-c)*(N-c)
    print(count)
else:
    c =int((K + 1)/2)
    for i in range(c):
        count += ((N-i) * (N-(K-i)))*2
    print(count)
    

# 方針は分かってるはずなんだけどなんだか上手く行かないので諦めようとしてる