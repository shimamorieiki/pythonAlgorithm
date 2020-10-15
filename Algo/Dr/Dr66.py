# 騎士巡歴

N = 6 # 5*5の盤面
dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]
m =  [[0] * (N+4) for i in range(N+4)]
count =0
num  = 0

def backtrack(x,y):
    # print(x,y)
    global count, num #グローバル変数のときはこうすればいいらしい
    if m[x][y]==0:
        count +=1
        m[x][y] = count #今(x,y)にいる
        ##################################################
        if count == N*N:
            num += 1
            print("解",num)
            for i in range(2,N+2):
                for j in range(2,N+2):
                    print(str(m[i][j]).rjust(4),end="")
                print("\n")
        else:
            #################################################################
            #ここで次の候補を調べてる
            #もし見つかればそれでいい
            #考えうるのをすべて探したけど見つからなかったらループから抜ける
            # => 次に行かないので終わる
            for k in range(8):
                backtrack(x+dx[k],y+dy[k])
            #################################################################
        ##################################################
        #上手く行かなかったらリセット
        m[x][y] = 0
        count -=1
    
for i in range(N+4):
    for j in range(N+4):
        m[i][j] = 0 if (2<=i and i<=N+1 and 2<=j and j<=N+1) else 1
backtrack(2,4)
