# ソートして大きい人数から順に現時点で空いている最も大きい部屋に割り振る

N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

if N < M:
    print("NO")
    exit()

A.sort()
B.sort()

for i in reversed(range(M)):
    if B[i] <= A[-1]:
        A.pop()
    else:
        print("NO")
        exit()
print("YES")

# AC 14m
