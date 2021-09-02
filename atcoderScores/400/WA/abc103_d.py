N,M = map(int,input().split(" "))
ab = []
for item in range(M):
    ab.append(list(map(int,input().split(" "))))

imos = [0]*N

for a,b in ab:
    imos[a-1]+=1
    imos[b-1]-=1

max = 0
for i in range(1,N):
    imos[i] += imos[i-1]

print(imos)


# 全然わかんね
# 中央から探すから面倒くさい。
# 右から削除すればそれでいい。