# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))

a,b,c,d = map(int,input().split(" "))

print(a + (b/(b+d))*(c-a) )