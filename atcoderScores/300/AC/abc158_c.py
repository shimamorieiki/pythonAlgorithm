A,B = map(int,input().split(" "))

for i in range(1,1010):
    if A <= i*0.08 <A+1 and B <= i*0.1<B+1:
        print(i)
        break
else:
    print(-1)

# AC4