# n番目からm番目までの和はn番目までとm番目までを全て求めて引く(区間和TLE)
# s[j] - s[i] がMの倍数ということはs[j] % M == s[i] % M(バケツソートTLE)
# バケツソートだと必要以上に確保しすぎる事があるのでdictでよい


N = 10
M = 400000000
a = [
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
    1000000000,
]

N, M = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

s = [0 for _ in range(len(a) + 1)]

s[0] = 0

for i in range(len(a)):
    s[i + 1] = (a[i] + s[i]) % M

c = 0
b = [0 for _ in range(M)]
for i in s:
    b[i] += 1
for i in b:
    c += i * (i - 1) // 2
print(c)
