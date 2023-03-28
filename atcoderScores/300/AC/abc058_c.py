# つまり与えられた文字数に共通する文字をすべて抜き出せばよい
# 文字を抜き出してしまえば辞書順最小は直ぐに作れる
# 全探索で行けない？

N = int(input())
S = []
for _ in range(N):
    S.append(input())

T = [[0 for _ in range(26)] for _ in range(N)]
for i in range(N):
    for c in list(S[i]):
        T[i][ord(c) - 97] += 1

mins = T[0]
for t in T:
    for i in range(26):
        mins[i] = min(mins[i], t[i])
chars = []
for i, m in enumerate(mins):
    for _ in range(m):
        chars.append(chr(i + 97))

print("".join(chars))

# AC 13m