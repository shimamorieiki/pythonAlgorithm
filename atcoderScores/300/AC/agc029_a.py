# 自分の右にいくつWが連続するかを右のBから調べる?
# 連続してなくても別にいいな

S = list(input())
A = [0] * len(S)

for i in range(len(S)):
    if S[i] == "W":
        A[i] += 1

for i in reversed(range(1, len(S))):
    A[i - 1] += A[i]

ans = 0
for i in range(len(A)):
    if S[i] == "B":
        ans += A[i]
print(ans)

# AC 20
# そういうことやな
