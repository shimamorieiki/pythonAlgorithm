#個数制限付き部分和問題
def dp(n,a,m,K):
    # n 文字種
    # ai 数字
    # mi 使える数
    # K 作れるか判定したい数
    Num  = [0]*(K+1) #その値が存在すれば1 存在しなければ0
    # DPの本質は帰納法と漸化式
     
    for i in range(n): #数
        for j in range(m[j]): #その数の使用可能数
            pass

    print(n,a,m,K)


a = [3,5,8]
m = [3,2,2]
K = 17
n = len(a)
dp(n,a,m,K)