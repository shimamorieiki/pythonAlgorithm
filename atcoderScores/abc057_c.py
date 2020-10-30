# 整数 N が与えられます。
# ここで、2 つの正の整数 A,B に対して、
# F(A,B) を「10 進表記における、A の桁数と B の桁数のうち大きい方」と定義します。
# 例えば、F(3,11) の値は、3 は 1 桁、11 は 2 桁であるため、F(3,11)=2 となります。
# 2 つの正の整数の組 (A,B) が N=A×B を満たすように動くとき、F(A,B) の最小値を求めてください。
#  制約

#     1≦N≦10^10

# Nは整数である。

# N
# 10000
# 3

import math
N = int(input())
minLen = len(str(N))
leng = 0
gN = math.ceil(math.sqrt(N))
for i in range(2,gN+1):
    if N % i == 0:
        minLen = min(max(len(str(int(N/i))),len(str(i))),minLen)

print(minLen)
#AC16