Limit = 8 #ナップサックの重量制限
N = 5 #品物の種類
Min = 1 #重さの最小値

a = [["plum",4,4500],["apple",5,5700],["orange",2,2250],["strawberry",1,1100],["melon",6,6700]]
value = [0]*(Limit+1)
item =  [0]*(Limit+1)
newValue = 0

for i in range(N):
    for s in range(a[i][1],Limit+1):
        p = s - a[i][1]
        newValue = value[p] + a[i][2]
        if newValue  > value[s]:
            value[s] = newValue
            item[s] = i

print(max(value)) #品物の出力は本質ではなさそうなのでパス