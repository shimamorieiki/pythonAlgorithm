# 直感はDP
# dp[i][j] = i回目の操作後にjの位置にいることができるか(T/F)
# dp[i][j] = dp[i-1][j-a_i] or dp[i-1][j-b_i]

N,X = map(int,input().split(" "))
A = []
B = []

for _ in range(N):
    a,b = map(int,input().split(" "))
    A.append(a)
    B.append(b)
    
dp = [[False]*(10001) for _ in range(N)]

dp[0][A[0]] = True
dp[0][B[0]] = True

for n in range(1,N):
    for x in range(2,X):
        if x-A[n]+1 >=0 and x-B[n]+1 >= 0:
            dp[n][x+1] = dp[n-1][x-A[n]+1] or dp[n-1][x-B[n]+1]
        elif x-A[n]+1 < 0:
            dp[n][x+1] = dp[n-1][x-B[n]+1]
        elif x-B[n]+1 < 0:
            dp[n][x+1] = dp[n-1][x-A[n]+1]
            
if dp[N-1][X]:
    print("Yes")
else:
    print("No")
    
# AC 21m