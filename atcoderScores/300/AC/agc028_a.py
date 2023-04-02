# L = lcm(N,M)
# S[]
# 最小公倍数あたりが関係しそう
# lcmを回すとTLE

import math

N, M = map(int, input().split(" "))
S = input()
T = input()

lcm = N * M // math.gcd(N, M)
a = (lcm // N) * (lcm // M)
for i in range(lcm // a):
    if S[i * (lcm // M)] != T[i * (lcm // N)]:
        print(-1)
        exit()

print(lcm)

# AC over 30m
# 解説が何言ってるか分からないけどやっていることは合っているのでOK
