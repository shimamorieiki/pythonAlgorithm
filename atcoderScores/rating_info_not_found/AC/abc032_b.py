S = input()
K = int(input())
p = {}
for i in range(len(S) - K + 1):
    q = S[i : i + K]
    p.setdefault(q, 0)
    p[q] += 1

print(len(p))

# AC 5m
