import math
N,H = map(int,input().split(" "))
itigeki = []
tuujou = []
for item in range(N):
    t,i = map(int,input().split(" "))
    itigeki.append(i)
    tuujou.append(t)

itigeki.sort(reverse=True)
tuujou.sort(reverse=True)

count = 0
for i in itigeki:
    if i > tuujou[0]:
        H -= i
        count += 1
    else:
        break

count += math.ceil(H / tuujou[0])
print(count)

# 方針はあってるのにコーナーケースがうまく行かない