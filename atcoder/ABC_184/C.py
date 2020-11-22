# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))
r1,c1 = map(int,input().split(" "))
r2,c2 = map(int,input().split(" "))
x,y = r2-r1,c2-c1
if r1==r2 and c1==c2:
    print(0)
elif (abs(r1-r2) + abs(c1-c2) <= 3) or (r1+r2 == c1+c2) or (r1-r2 == c1-c2):
    print(1)
else:
    if abs(y-x) %2 == 0 or abs(y+x) % 2 == 0:
        print(2)
    else:
        print(3)

# なんかそんな気はしていたが、条件を理解することができなかった
# 3手以下なのは確かにそうだった。どこに行けてどこに行けないのかをちゃんと考えるべきだった
