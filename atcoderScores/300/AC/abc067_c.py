# 累積和っぽいな

N = int(input())
A = list(map(int, input().split(" ")))

L = [0] * N
L[0] = A[0]
for i in range(1, N):
    L[i] = L[i - 1] + A[i]

ans = 10**20
for i in range(N - 1):
    ans = min(ans, abs(L[N - 1] - L[i] * 2))
print(ans)

# AC 7
# まあ解けているし良いや
