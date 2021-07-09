# 偶数回移動するしかなくて、左か右かその場。
# 左に移動しても右に移動しても差がない
# 最初の方で削る必要がありそう

X,K,D = map(int,input().split(" "))
if K %2 != 0:
    K -=1
    l = abs(X-D)
    r = abs(X+D)
    if abs(X) > l:
        X = l 
    elif abs(X) > r:
        X = r
delete = K / (2*D)
X -= K // delete
for i in range(K//2):
    l = abs(X-2*D)
    r = abs(X+2*D)
    if abs(X) > l:
        X = l 
    elif abs(X) > r:
        X = r
    else:
        print(X)
        exit(0)
print(X)