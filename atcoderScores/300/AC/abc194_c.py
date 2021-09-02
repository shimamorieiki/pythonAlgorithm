N = int(input())
a = list(map(int,input().split(" ")))
sumNum = 0
nijoNum = 0
for i in a:
    sumNum += i
    nijoNum += i*i
print(len(a)*nijoNum - sumNum * sumNum)

# AC12