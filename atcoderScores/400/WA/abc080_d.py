# いもす法じゃありませんか?

N,C = map(int,input().split(" "))
stc = []
for i in range(N):
    stc.append(list(map(int,input().split(" "))))

# テレビが放送される時間
T = [0]*1000001

for s,t,c in stc:
    T[s*10-5] += 1
    T[t*10] -= 1

maxNum = 0
for i in range(1,len(T)):
    T[i] += T[i-1]
    if maxNum < T[i]:
        maxNum = T[i]
print(maxNum)

# ほとんど合ってるけど、なんかエッジケースが困ったことになってる?
# なんでこれで解けないんだろうか？
