# 全円順列で試すのは計算量的に不可能なので
# 何らかの成立条件があると思われる
# なんやかんや考察した結果、奇:偶=2:1 or 全部偶しか候補がないはず
# 考察が足りていない可能性がある

N = int(input())
A = list(map(int, input().split(" ")))

a_bool = [i % 2 for i in A]

while a_bool.count(0) == N:
    A = [a // 2 for a in A]
    a_bool = [i % 2 for i in A]

if not (N % 3 == 0 and a_bool.count(0) == N // 3):
    print("No")
    exit()

xor = 0
for a in A:
    xor ^= a

if xor == 0:
    print("Yes")
else:
    print("No")

# WA
# 考察が足りませんでした
