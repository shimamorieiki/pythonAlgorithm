N = int(input())
x = list(map(int,input().split(" ")))
xsum = sum(x)
x2sum = sum([i*i for i in x])
ans = 10000000
for i in range(1,max(x)+1):
    i * i * N - xsum*2*i
    if (i * i * N - xsum*2*i)<ans:
        ans = i * i * N - xsum*2*i
print(ans+x2sum)

# AC7