import math

N = int(input())

c = 0
for i in range(1, math.ceil(math.sqrt(2 * N))):
    if (2 * N) % i != 0:
        continue

    if ((2 * N) // i - i - 1) % 2 == 1:
        continue

    c += 1

print(c * 2)

# AC 30m
# まあ、そういうことでしょう
