N,D,H = map(int,input().split(" "))
b = []
tall = [0]
for i in range(N):
    d,h = map(int,input().split(" "))
    tall.append((D*h-H*d)/(D-d))
print(max(tall))