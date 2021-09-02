import math

def isPrime(n):
    if n == 1:
        return True
    
    for j in range(2,int(math.sqrt(i))+1):
        if n % j == 0:
            return False

    return True
    
# 素数判定をそれなりに早く行う
Q = int(input())
q = []
for i in range(Q):
    q.append(list(map(int,input().split(" "))))

sosu1 = []
sosu2 = []
maxNum = 10**5
for i in range(3,maxNum):
    if isPrime(i) and isPrime((i+1)//2):
        sosu1.append(i)

a = [0]*100001

for i in sosu1:
    a[i] += 1

for i in range(1,100001):
    a[i] += a[i-1]

for l,r in q:
    index_r = a[r]
    index_l = a[l-1]
    print(index_r-index_l)

# AC90