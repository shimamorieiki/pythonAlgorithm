import math

K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        gcdij = math.gcd(i,j)
        if gcdij == 1:
            ans+=K
        else:
            for k in range(1,K+1):
                ans += math.gcd(gcdij,k)
print(ans)

# AC8