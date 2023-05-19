# 有向グラフで目的の場所まで行けるかどうか

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
    
G = [False]*N

index = 0
G[index] = True
count = 0
while True:
    if G[A[index]-1]:
        print(-1)
        exit()
    index = A[index]-1
    G[index] = True
    count += 1
    if index == 1:
        print(count)
        exit()
        
# AC 10m