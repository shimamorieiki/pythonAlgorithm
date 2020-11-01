# 長さ N の整数列 A=(A1,A2,⋯,AN) と整数 K

# が与えられます。

# 1≤X≤K
# を満たす整数 X

# それぞれについて、以下の値を求めてください。

# (N−1∑L=1N∑R=L+1(AL+AR)X)mod


N ,K = input().split(" ")
N = int(N)
K = int(K)
a = [int(i) for i in input().split(" ")]
print(sum(a)*(len(a)-1))
for i in range(K-1):
    print(0)