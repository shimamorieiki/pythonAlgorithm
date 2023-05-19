N = int(input())
A = list(map(int,input().split(" ")))

c = 0
for i in range(N):
    if A[A[i]-1] == i+1:
        c +=1
print(c//2)

# AC 18m