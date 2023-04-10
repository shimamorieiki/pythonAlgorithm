N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

B = [0] * 200001

for a in A:
    B[a] += 1

B = list(reversed(sorted(B)))
print(sum(B[K:]))

# AC 5
