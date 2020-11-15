# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))

import itertools

N,K  = map(int,input().split(" "))
a = []
for i in range(N):
    a.append(list(map(int,input().split(" "))))
l = [i for i in range(2,N+1)]
count = 0
for v in itertools.permutations(l):
    v = list(v)
    v.insert(0,1)
    v.append(1)
    v = [j-1 for j in v]
    val = 0 
    for i in range(len(v)-1):
        val += a[v[i+1]][v[i]]
    if val == K:
        count +=1
print(count)