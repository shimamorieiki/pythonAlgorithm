# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))

# 3
# 3 12 7

N = int(input())
a = list(map(int,input().split(" ")))

res = 0
num = 0
res = [0]*(max(a)+1)
for i in range(2,max(a)+1):
    b = [j % i for j in a]
    res[i] = b.count(0)
print(res.index(max(res)))