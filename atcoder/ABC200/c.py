# 6
# 123 223 123 523 200 2000

N = int(input())
A = list(map(int,input().split(" ")))
c = [0] * 200
count = 0
for i in range(N):
    c[A[i]%200] +=1

for i in c:
    count += (i * (i-1)) /2
        
print(int(count))