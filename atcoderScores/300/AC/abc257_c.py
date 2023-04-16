N = int(input())
S = []
for _ in range(N):
    S.append(input())

A = [[0 for _ in range(10)] for _ in range(10)]

for i in range(N):
    for j in range(10):
        A[int(S[i][j])][j] += 1

# もし数字に重複があれば10を足す
print(min(max([j + (A[i][j] - 1) * 10 for j in range(10)]) for i in range(10)))

# AC 24m
# そういうことでした
