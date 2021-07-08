K,N = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
a.sort()
a.append(K+a[0])
dis = 0
for i in range(len(a)-1):
    if a[i+1] - a[i]  > dis:
        dis = a[i+1] - a[i]
print(K-dis)
# AC6