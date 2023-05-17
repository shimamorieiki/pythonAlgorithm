# 直感的に、どこからか総当たりするしかない気がするんだけど
import math
n = int(input())
s = 10000000000000000000000000000000
for w in range(1,math.floor(math.sqrt(n)+1)):
    h = n // w
    s = min(s,n - w*h + abs(w-h))
print(s)

# AC 12