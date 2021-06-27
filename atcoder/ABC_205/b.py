N = int(input())
A = map(int,input().split(" "))
a = [0]*N
for i in A:
    a[i-1] +=1

if a.count(0) == 0:
    print("Yes")
else:
    print("No")