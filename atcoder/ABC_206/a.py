import math
a = int(input())
atax = math.floor(a * 1.08)

if atax == 206:
    print("so-so")
elif atax > 206:
    print(":(")    
else:
    print("Yay!")
