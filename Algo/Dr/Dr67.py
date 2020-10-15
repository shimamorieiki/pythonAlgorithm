Limit = 42 #容量、限界
N = 3 #要素の種類数

size = [1,10,25]
value = [i for i in range(Limit+1)]
item = [0]*(Limit+1)
newValue = 0

for i in range(N): #用意されている要素数文Loopを回す
    for s in range(size[i],Limit+1):
        p = s - size[i]
        newValue = value[p] + 1
        if newValue <= value[s]: #更新部分
            value[s] = newValue
            item[s]  = i

print(value[Limit])        