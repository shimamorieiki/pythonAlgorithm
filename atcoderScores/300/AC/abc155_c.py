N = int(input())
dic = {}
maxNum = 0
for _ in range(N):
    i = input()
    dic.setdefault(i,0)
    dic[i]+=1
    if dic[i] > maxNum:
        maxNum = dic[i]
keys = sorted(dic)
for i in keys:
    if dic[i] == maxNum:
        print(i)
# AC9