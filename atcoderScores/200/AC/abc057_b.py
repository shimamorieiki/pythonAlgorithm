N, M = map(int, input().split(" "))

A = []
B = []
C = []
D = []

for i in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

for i in range(M):
    c, d = map(int, input().split(" "))
    C.append(c)
    D.append(d)

for i in range(N):
    rowest_num = 0
    rowest_score = 1000000000
    for j in reversed(range(M)):
        man = abs(A[i] - C[j]) + abs(B[i] - D[j])
        if man <= rowest_score:
            rowest_score = man
            rowest_num = j
    print(rowest_num + 1)

# AC 10m
