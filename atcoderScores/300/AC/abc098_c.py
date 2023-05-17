# 累積和的なものでどうにかなるはず

N = int(input())
S = input()

W = [0]*(N+1)
E = [0]*(N+1)

for i in range(N):
    if S[i] == "W":
        W[i+1] = 1
for i in range(1,N):
    W[i] += W[i-1]

for i in range(1,N):
    if S[i] == "E":
        E[i-1] = 1

for i in reversed(range(N)):
    E[i] += E[i+1]


A = 10000000000

for i in range(N):
    A = min(A,W[i]+E[i])
print(A)

# AC 16