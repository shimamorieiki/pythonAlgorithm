N = int(input())

A = []
B = []

for _ in range(N):
    a,b = map(float,input().split(" "))
    A.append(a)
    B.append(b)

moushobi = 0
manatubi = 0
natubi = 0
nettaiya = 0
huyubi = 0
mahuyubi = 0

for a,b in zip(A,B):
    if a >= 35.0:
        moushobi +=1
    
    if 35.0 > a >= 30.0:
        manatubi+=1
        
    if 30.0 > a >= 25.0:
        natubi+=1
        
    if b >= 25.0:
        nettaiya+=1
    
    if a>= 0 and b < 0:
        huyubi +=1
        
    if a < 0:
        mahuyubi +=1
        
print(" ".join(str(i) for i in [moushobi,manatubi,natubi,nettaiya,huyubi,mahuyubi]))

# AC 8m