N = int(input())
a = []
for i in range(N):
    x,y =map(int,input().split(" "))
    a.append([x,y])

for i in range(len(a)):
   for j in range(i+1,len(a)):
       for k in range(j+1,len(a)):
            b = (a[i][0]-a[j][0])* (a[j][1]-a[k][1])
            c = (a[i][1]-a[j][1])* (a[j][0]-a[k][0])
            if b == c:
                print("Yes")
                exit(0)
else:
    print("No")
# AC10