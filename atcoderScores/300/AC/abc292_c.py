# いわゆる半分全列挙だろうな
# そうじゃん
# Aが最小、C<Dと仮定しても一般性を失わない。
# すなわち A <= B, C <= D, A <= C
# このとき A=B=C=D としたら 2A^2 = Nより A <= (N/2)^(1/2) = 10^2.5
N = int(input())
B = [0] * (N + 1)

count = 0
for a in range(1, N + 1):
    for b in range(a, (N // a) + 1):
        if a == b:
            B[a * b] += 1
        else:
            B[a * b] += 2

for i in range(1, (N // 2) + 1):
    if i == N - i:
        count += B[i] * B[N - i]
    else:
        count += 2 * B[i] * B[N - i]
print(count)

# AC 30m
# 時間かかりすぎやろ