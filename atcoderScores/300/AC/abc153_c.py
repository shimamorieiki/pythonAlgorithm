N,K = map(int,input().split(" "))
h = list(map(int,input().split(" ")))

h  =reversed(sorted(h))
sum = 0
for index,value in enumerate(h):
    if index >= K:
       sum += value 
print(sum)

# AC5