N = int(input())
a = []

for i in range(N):
    s,t = input().split(" ")
    t = int(t)
    a.append([t,s])
a = sorted(a,reverse=True)
print(a[1][1])