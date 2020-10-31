# あんまり意味が分かっていないけど疲れた

N = 8
M = 9999

a = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,7,2,M,M,M,M],
    [0,1,0,M,M,2,4,M,M],
    [0,7,M,0,M,M,2,3,M],
    [0,2,M,M,0,M,M,5,M],
    [0,M,2,M,M,0,1,M,M],
    [0,M,4,2,M,1,0,M,6],
    [0,M,M,3,5,M,M,0,2],
    [0,M,M,M,M,M,6,2,0]
]
            
leng = [M]*(N+1)
v = [0]*(N+1)
start = 1
leng[start] = 0

for i in range(1,N+1):
    minV = M
    for k in range(1,N+1):
        if v[k]==0 and leng[k] < minV:
            p = k
            minV = leng[k]
    v[p] = 1
    if minV == M:
        print("グラフは連結ではない")
        # exit(1)
    
    for k in range(N+1):
        if (leng[p] + a[p][k]) < leng[k]:
            leng[k] = leng[p] + a[p][k]

for j in range(1,N+1):
    print(start," => ",j," : ",leng[j])

