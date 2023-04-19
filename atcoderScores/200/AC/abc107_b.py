H, W = map(int, input().split(" "))
A = []
for i in range(H):
    A.append(list(input()))

R = []
Q = []

for i in range(H):
    if A[i].count("#") > 0:
        R.append(A[i])

R_t = [list(x) for x in zip(*R)]

C = []
for i in range(len(R_t)):
    if R_t[i].count("#") > 0:
        C.append(R_t[i])

C_t = [list(x) for x in zip(*C)]

for i in C_t:
    print("".join(i))

# AC 20m
# 実装するだけ
