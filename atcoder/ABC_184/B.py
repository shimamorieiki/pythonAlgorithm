# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))
N,X = map(int,input().split(" "))
S = input()

for i in S:
    if i =="o":
        X +=1
    else:
        X = max(X-1,0)
print(X)
