X,N = map(int,input().split(" "))
if N == 0:
    print(X)
    exit(0)

p = list(map(int,input().split(" ")))
a = [0]*102
for i in p:
    a[i] = 1000

for i in range(102):
    if a[i] != 1000:
        a[i] = abs(i-X)
minnum = 1000
for i in a:
    if minnum > i:
        minnum = i
for index,value in enumerate(a):
    if value == minnum:
        print(index)
        break

# AC