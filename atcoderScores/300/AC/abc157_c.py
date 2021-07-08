N,M = map(int,input().split(" "))
a = [-1]*N
for _ in range(M):
    s,c = map(int,input().split(" "))
    if a[s-1] != -1 and a[s-1]!=c:
        print(-1)
        exit(0)
    else:
        a[s-1] = c
ans = ""

if N == 1 and (a[0] == -1 or a[0] == 0):
    print(0)
    exit(0)

if N >= 2 and a[0] == -1:
    a[0] = 1

for i in a:
    if i==-1:
        ans += "0"
    else:
        ans +=str(i)

if len(str(int(ans))) == N:
    print(ans)
else:
    print(-1)

# AC18