# |M-N| >= 2 のときは絶対に不可能

# |M-N| == 1 のときは多いほうから開始して多いほうで終了する

# |M-N| == 0 のときは AB,BAのいずれでも並べることができる
# ただしこれは AB として求めたものを2倍するだけなので本質的には同じ

N, M = map(int, input().split(" "))

if abs(N - M) >= 2:
    print(0)
    exit(0)

n_j = 1
for i in range(1, N + 1):
    n_j *= i
    n_j %= 1000000007

m_j = 1
for i in range(1, M + 1):
    m_j *= i
    m_j %= 1000000007

if abs(N - M) == 1:
    # N! * M!
    print((n_j * m_j) % 1000000007)
    exit(0)

if abs(N - M) == 0:
    # N! * M! * 2
    print((n_j * m_j * 2) % 1000000007)
    exit(0)

# AC 15m
