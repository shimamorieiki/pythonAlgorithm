Node = 4
Root = 6
Start = 1

# 各要素は連結されている辺の数
a = [
    [0,0,0,0,0],
    [0,0,1,0,1],
    [0,1,0,1,2],
    [0,0,1,0,1],
    [0,1,2,1,0]
]
v = [0]*(Root+1)
success = 0
n = Root

def visit(i):
    global v,success,n
    v[n] = i
    if n==0 and i ==Start:
        print("解 ",success,":",end="")
        success += 1
        for i in range(Root+1):
            print(v[i],end="")
        print("\n")
    else:
        for j in range(1,Node+1):
            if a[i][j]!=0:
                a[i][j] -=1
                a[j][i] -=1
                n -=1
                visit(j)
                a[i][j] +=1
                a[j][i] +=1
                n +=1

visit(Start)
if success == 0:
    print("解なし")
