# まあ、多分だけどこれは単純にやったらTLEなんだろうな
# 昇順にソートして累積和でよさそう

N = int(input())
A = list(map(int, input().split(" ")))
A.sort()
B = [0] * N
B[0] = A[0]
for i in range(1, N):
    B[i] += B[i - 1] + A[i]

C = 0
for i in range(N - 1):
    C += B[N - 1] - B[i] - (N - i - 1) * A[i]
print(C)

# AC 15m
# ですよね
