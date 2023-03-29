# N が小さければ全探索するが、この制約だと無理
# 「どこも演説しない」状態から、演説することで一番票が動く街から貪欲？

N = int(input())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

aoki = sum(A)
takahashi = 0
C = [[2 * A[i] + B[i], i] for i in range(N)]
C = list(reversed(sorted(C)))
for i in range(N):
    aoki -= A[C[i][1]]
    takahashi += A[C[i][1]] + B[C[i][1]]
    if takahashi > aoki:
        print(i + 1)
        exit()

# AC 18m
# 想定解答
