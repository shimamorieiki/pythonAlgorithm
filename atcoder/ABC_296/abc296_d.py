# 答えでんにぶたんみを感じる
# 感じるんだけどこれでやると X が素数の時ににぶたんが止まる
# Nが10^12 くらいあるから
# ある x が x = a*b(a,b <= N)の形で表すことができるかの判定がどうやってもTLE

import math
 
def check(x):
    # x = a*b(a,b <= N)の形で表すことができる
    for i in range(1,math.ceil(math.sqrt(x))+1):
        if x % i == 0 and x // i <= N and i <= N:
            return True
 
    return False
 
N,M = map(int,input().split(" "))
 
if M > N*N:
    print(-1)
    exit()
    
 
left = M
right = math.ceil(math.sqrt(M))**2
 
for x in range(left,right+1):
    if check(x):
        print(x)
        exit()

# import math

# def check(x):
#     # x より大きいもので M < x' = a*b(a,b <= N)
#     # をみたすものが存在するかどうか
#     return math.floor(math.sqrt(x)) <= N

# N,M = map(int,input().split(" "))

# if M > N*N:
#     print(-1)
#     exit()
    

# left = M
# right = N*N
# X = (left + right) //2

# while right - left > 1:
#     if math.floor(math.sqrt(X)) <= N:
#         # まだ小さい数を探してよい
#         right = X
#         print("check true")
#     else:
#         # 今より大きい数を探す
#         left = X
#         print("check false")
#     X = (left + right) //2
    
#     print(X,left,right)

# print(X)