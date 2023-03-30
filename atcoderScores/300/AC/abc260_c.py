# よく分からんけど、そもそも交換手順が1通りしかないのでは？

N, X, Y = map(int, input().split(" "))

RED = [0] * (N + 1)
BLUE = [0] * (N + 1)

RED[N] = 1

for i in reversed(range(1, N)):
    # A[i+1]の分配
    RED[i] += RED[i + 1]
    BLUE[i + 1] += RED[i + 1] * X
    # B[i+1]の分配
    RED[i] += BLUE[i + 1]
    BLUE[i] += BLUE[i + 1] * Y

print(BLUE[1])

# AC 22m
