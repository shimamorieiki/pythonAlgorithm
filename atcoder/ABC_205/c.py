A,B,C = map(int,input().split(" "))

if C % 2 == 0: #Cが偶数
    if abs(A) > abs(B):
        print(">")
    elif abs(A) < abs(B):
        print("<")
    else:
        print("=")
else: #Cが奇数
    if A>0 and B>0:
        if A > B:
            print(">")
        elif A<B:
            print("<")
        else:
            print("=")
    elif A>0 and B<0:
        print(">")
    elif A<0 and B>0:
        print("<")
    elif A<0 and B>0:
        if A > B:
            print("<")
        elif A<B:
            print(">")
        else:
            print("=")
    elif A == 0:
        if B == 0:
            print("=")
        elif B>0:
            print("<")
        else:
            print(">")
    elif A == 0:
        if B == 0:
            print("=")
        elif B>0:
            print("<")
        else:
            print(">")
    elif B == 0:
        if A == 0:
            print("=")
        elif B>0:
            print("<")
        else:
            print(">")