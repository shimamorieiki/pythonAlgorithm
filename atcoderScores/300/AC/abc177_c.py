N = int(input())
a = list(map(int,input().split(" ")))

suma= sum(a)
a2 = suma * suma
b = [i*i for i in a]
sumb = sum(b)

print((a2 - sumb)//2 % 1000000007)

# AC4