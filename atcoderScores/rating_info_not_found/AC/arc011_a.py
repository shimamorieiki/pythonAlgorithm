# 愚直に計算しても間に合う気がする

m, n, N = map(int, input().split(" "))
c = N
short = N

while short >= m:
    c += (short // m) * n
    short = short % m + (short // m) * n
print(c)

# AC 18m