import math
N = int(input())
a = math.floor(math.log10(N))+1

index = 1
sum = 0
while index < a+1:
    mn = int("1"+"0"*(index-1))
    mx = int("9"*index)
    if N > mx:
        sum += (2 + mx-mn)*(mx - mn +1)//2
    else:
        sum += (2 + N-mn)*(N - mn +1)//2
    index+=1
    
print(sum % 998244353)

# AC 20m