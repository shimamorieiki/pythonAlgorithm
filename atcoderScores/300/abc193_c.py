import math
N = int(input())

# 1-rNまでなので10^5程度でループを回せる。

nijo = []
count = 0

for i in range(2,int(math.sqrt(N))+1):
    if i not in nijo:
        n = i*i
        while n <= N:
            nijo.append(n)
            count +=1
            n *= i
print(N- count)

# 昔の自分のほうが頭いいのなんでだろう
# そりゃ確かにlog使ったほうが頭いいに決まってるな