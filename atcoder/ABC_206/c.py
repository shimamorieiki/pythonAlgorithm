n = int(input())
a = list(map(int,input().split(" ")))
a = sorted(a)
now = a[0]
last = a[-1]
ans = 0
count = 0
lastnum = a.count(a[-1])
for index,item in enumerate(a):
    if item != now:
        ans += count * (n - count)
        count = 1
        now = item
    else:
        count+=1
print((ans+ lastnum *(n-lastnum))//2)