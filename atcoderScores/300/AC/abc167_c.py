N,M,X = map(int,input().split(" "))
a = []
for i in range(N):
    a.append(list(map(int,input().split(" "))))
score = [0]*M
price= 0
minPrice = 10000000

for i in range(pow(2,N)):
    b = str(bin(i)[2:])
    b = b.rjust(N, '0')
    for index,bit in enumerate(b):
        if bit == "1":
            for j in range(M):
                score[j] += a[index][j+1]            
            price += a[index][0]

    if min(score) >= X and minPrice > price:
        minPrice = price
    price = 0
    score = [0]*M

if minPrice == 10000000:
    print(-1)
else:
    print(minPrice)

# AC50