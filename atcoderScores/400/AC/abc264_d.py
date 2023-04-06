S = input()

C = ["a", "t", "c", "o", "d", "e", "r"]

W = [C.index(s) for s in S]

ans = 0
for i in range(7):
    ans += W.index(i)
    W.remove(i)

print(ans)

# AC 10
# 転倒数とかいう概念があるらしい
