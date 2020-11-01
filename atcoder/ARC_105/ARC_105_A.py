def solve(a):
    flag=0
    for p in range(2):
        for q in range(2):
            for r in range(2):
                for s in range(2):
                    a1 = a[0] if p==0 else 0
                    a2 = a[1] if q==0 else 0
                    a3 = a[2] if r==0 else 0
                    a4 = a[3] if s==0 else 0
                    if a1+a2+a3+a4 == sum(a)/2:
                        flag = 1
    if flag == 0:
        print("no")
    else:
        print("yes")
                        

# a = [1,3,2,4]
a = [1,2,4,8]

solve(a)