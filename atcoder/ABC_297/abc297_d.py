# フィボナッチみをすごく感じる

A,B = map(int,input().split(" "))
c = 0
while A != B:
    if A > B:
        div,mod = divmod(A,B)
        if mod == 0:
            A = B
            c -=1
        else:    
            A = mod
        c +=div
    else:
        div,mod = divmod(B,A)
        if mod == 0:
            B = A
            c -=1
        else:
            B = mod
        c +=div
print(c)