A = [0] * 21
A[0] = 100
A[1] = 100
A[2] = 200

for i in range(3, 21):
    A[i] = A[i - 1] + A[i - 2] + A[i - 3]
print(A[19])

# AC 10m
# 変なミスをしすぎ
