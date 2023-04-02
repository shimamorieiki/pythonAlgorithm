# 全通り見るのはTLE
import bisect
N,X = map(int,input().split(" "))
A = list(map(int,input().split(" ")))

A.sort()
for a in A:
    candidate = bisect.bisect_left(A, a+X)
    for j in range(candidate,N):
        if A[j] - a == X:
            print("Yes")
            exit()
        
        if A[j] - a > X:
            break
else:
    print("No")