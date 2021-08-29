N,K = map(int,input().split(" "))
f = N
bucket =  [0]*10
for j in range(K):
    bucket =  [0]*10
    for i in list(str(f)):
        bucket[int(i)] +=1

    minNum = ""
    maxNum = ""
    for num,count in enumerate(bucket):
        minNum += str(num) * count
        maxNum = str(num) * count + maxNum

    f = int(maxNum)-int(minNum)

print(f)

# AC12
# 二回解いてた