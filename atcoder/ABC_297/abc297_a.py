N,D= map(int,input().split(" "))
T = list(map(int,input().split(" ")))

for i in range(1,N-1):
    if T[i] - T[i-1] <= D:
        print(T[i])
        exit()
print(-1)