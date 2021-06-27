n = int(input())
ans = 0
for i in range(100000):
    ans += i
    if ans >= n:
        print(i)
        break