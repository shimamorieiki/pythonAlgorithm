import math
t,N = map(int,input().split(" "))
print(math.ceil(N*100 / t -1)+N)