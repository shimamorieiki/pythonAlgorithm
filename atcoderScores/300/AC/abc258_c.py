# 愚直にやったら死ぬんか？

N, Q = map(int, input().split(" "))
S = input()
Query = []
for _ in range(Q):
    Query.append(list(map(int, input().split(" "))))

index = 0
for t, x in Query:
    if t == 1:
        index += x
    else:
        print(S[(x - index - 1) % N])

# AC 27
