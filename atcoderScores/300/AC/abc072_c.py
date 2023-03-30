# 分かりやすい累積和じゃん

N = int(input())
A = list(map(int, input().split(" ")))

C = [0] * 200000

for i in range(N):
    C[A[i]] += 1
    C[A[i] + 3] -= 1

for i in range(1, len(C)):
    C[i] += C[i - 1]

print(max(C))

# AC 10m
