N = int(input())
a = list(map(int,input().split(" ")))
b = set(a)
if len(a) == len(b):
    print("YES")
else:
    print("NO")

# AC2