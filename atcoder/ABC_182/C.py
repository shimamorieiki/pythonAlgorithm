# map(int,input().split(" "))
# list(map(int,input().split(" ")))
# int(input())
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))

# 各桁に 0 が出現しないような正の整数 N が与えられます。
# N の桁数を k とします。N の桁を 0 個以上 k 個未満消して、
# 残った桁をそのままの順序で結合することで 3 の倍数を作りたいです。
# 3 の倍数を作ることができるか判定し、作ることができるなら作るのに必要な最少の消す桁数を求めてください。
# 制約
# 1≤N<1018
# Nは各桁に 0 が出現しない整数

# 35

# 1

N = int(input())
res = [0]*3
for i in str(N):
    res[int(i) % 3] +=1

m = len(str(N))+1
for i in range(res[1]+1):
    for j in range(res[2]+1):
        if (i + j*2) % 3 == 0 and sum(res) != (res[1]-i)+(res[2]-j):
            m = min(m,res[1] + res[2] -(i+j))
if m == len(str(N))+1:
    print(-1)
else:
    print(m)