N = int(input())
S = input()

half = N // 2
c = 0
if N % 2 == 0:
    for i in range(half):
        if S[i] != S[i + half]:
            c += 1
else:
    print(-1)
    exit()
print(c)

# AC 7
