N = int(input())

# 5回操作をするごとに先頭のものが末尾に来る
S = N // 5

# S を 6セットするごとに始めの状態に戻る
T = S % 6

# 5で割った余りの回数だけ試せばよい
U = N % 5

a = [1, 2, 3, 4, 5, 6]

for _ in range(T):
    a.append(a.pop(0))

for i in range(U):
    a[i], a[i + 1] = a[i + 1], a[i]

print("".join([str(i) for i in a]))

# AC 15m
