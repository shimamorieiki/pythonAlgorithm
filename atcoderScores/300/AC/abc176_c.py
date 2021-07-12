N = int(input())
a = list(map(int,input().split(" ")))

minHeight = a[0]
count = 0
for i in a[1:]:
    if i > minHeight:
        minHeight = i
    else:
        count += minHeight-i
print(count)

# AC7