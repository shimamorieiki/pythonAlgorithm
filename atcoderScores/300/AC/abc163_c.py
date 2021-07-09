N = int(input())
a = list(map(int,input().split(" ")))

x = [0]*(N+1)
for i in a:
    x[i] += 1

for i in x[1:]:
    print(i)

# AC7