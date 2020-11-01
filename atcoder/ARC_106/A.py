# 整数 N が与えられます。 3^A+5^B=N を満たす正の整数の組 (A,B) が存在するか判定し、
# 存在する場合は1組求めてください。
# 制約

#     1≤N≤10^18

# 入力はすべて整数である。

N = int(input())
flag = 0
if(N % 2 != 0): #奇数のとき
    print(-1)
else: #偶数のとき
    c5 = 1
    while pow(5,c5) < N:
        if (N - pow(5,c5)) % 3 == 0:
            for i in range(100):
                if N - pow(5,c5) == pow(3,i):
                    print(i,c5)
                    flag = 1
                    break
        if flag == 1:
            break
        else:
            c5 += 1
    if flag == 0:
        print(-1)

