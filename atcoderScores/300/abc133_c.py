# 非負整数 L,R が与えられます。 
# 2 つの整数 i,j を L≤i<j≤R を満たすように選びます。 
# (i×j) mod 2019 の最小値を求めてください。
# 制約
# 入力は全て整数
# 0≤L<R≤2×10^9

# 2020 2040

# 2

# L,R = 1,2019
L,R = map(int,input().split(" "))
l = L % 2019
r = R % 2019
s = 2020

if L-R >= 2020:
    print(0)
else:
    if (l<r):
        for i in range(2020):
            for j in range(2020):
                if ((l<=i and i<=r and l<=j and j<=r) and i != j):
                    s = min((i * j) %2019,s)
    elif (l>r):
        for i in range(2020):
            for j in range(2020):
                if (
                    (i != j) and
                    (0<=i and i<=r and l<=j and j<=2019) or
                    (l<=i and i<=2019 and 0<=j and j<=r)or
                    (l<=i and i<=2019 and l<=j and j<=2019)or
                    (0<=i and i<=r and 0<=j and j<=r)
                ):
                    s = min((i * j) %2019,s)

    print(s)
# 方法があるにはあるけど前処理が面倒くさそう
# それが終われば2019*2019 = 4*10^6 くらいの計算量になりそう
# 方針は合ってるはずなのにひとつだけWAが出る
# AC 56 解答見た