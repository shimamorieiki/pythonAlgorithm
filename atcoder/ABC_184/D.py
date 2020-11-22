# int(input())
# list(map(int,input().split(" ")))
# map(int,input().split(" "))
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))# map(int,input().split(" "))

# 袋の中に金貨が A 枚、銀貨が B 枚、銅貨が C 枚入っています。
# 袋の中にあるいずれかの種類の硬貨が 100 枚になるまで以下の操作を繰り返します。
# 操作：袋の中から硬貨をランダムに 1 枚取り出す。(どの硬貨も等確率で選ばれる。) 
# 取り出した硬貨と同じ種類の硬貨を 2 枚袋に戻す。
# 操作回数の期待値を求めてください。
# 制約
# 0≤A,B,C≤99
# A+B+C≥1

# A,B,C = map(int,input().split(" "))
A,B,C = 31,41,59

s = A+B+C
print(((100-A)*A + (100-B)*B+(100-C)*C)/s)

x = 2 * 98 /(98+99+99) + 99 /(98+99+99)+ 99 /(98+99+99)
print(x)


# dpなんだろうなどうせ
# dp[A][B][C] = A,B,C枚のときの期待値
# dp[A][B][C] = dp[A+1][B][C]
# これはdpであることまで分かってたのに頭が悪かった