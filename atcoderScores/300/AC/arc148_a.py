# 単調増加とかではないから答えでにぶたんとかは使えない
# Mが2以上なので、要素数は最大でも2までしか取れない
# mod 2 が0,1の2種類しか存在しないため
# 1種類になるのは全てa*n + b の形式で表せるとき
import math

N = int(input())
A = list(map(int, input().split(" ")))
T = [a - A[0] for a in A[1:]]
ans = T[0]
for t in range(N - 2):
    ans = math.gcd(ans, T[t + 1])

if ans == 1:
    print(2)
else:
    print(1)

# AC 40m
# 模範解答通り
