# a,b,c の mod K が全て0 or 全て K/2 (K=2n)

N, K = map(int, input().split(" "))

n = 0

# mod K が全て0
n += pow(N // K, 3)

# K が偶数の時は、a,b,cは全てK/2の倍数
if K % 2 == 0:
    c = 0
    for i in range(1, N + 1):
        if i % K == K // 2:
            c += 1
    n += pow(c, 3)

print(n)

# AC27
