import math
A,B,H,M  =map(int,input().split(" "))
h = (H*60+M)/720 * 2 * math.pi
m = M/60 * 2*math.pi
# print(math.sin(h-m))
# s = A*B*abs(math.sin(h-m))/2
l  = A*A + B*B - 2*A*B*math.cos(h-m)
print(math.sqrt(l))

# AC23