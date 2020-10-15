#学びたいのは上手にbacktrackする方法
num=1
def backtrack(i):
    global num
    if i>N: #N回目
        print("解",num)
        num += 1
        for y in range(N):
            for x in range(N):
                print(" Q",end='') if queen[y]==x else print(" .",end='')
            print("\n")
    else:
        for j in range(N):
            if column[j]==1 and rup[i+j]==1 and lup[i-j+N]==1:
                queen[i]=j #(i,j)が王妃の位置
                column[j] =  rup[i+j] = lup[i-j+N] = 0 #局面の変更
                backtrack(i+1)
                column[j] = rup[i+j] = lup[i-j+N] = 1 #局面の戻し
                # むずい



N = 8 #8 * 8のマス
column = [1]*N
rup = [1]*(2*N+1)
lup = [1]*(2*N+1)
queen = [0]*(N+1)
backtrack(1)

# print(column,rup,lup)
