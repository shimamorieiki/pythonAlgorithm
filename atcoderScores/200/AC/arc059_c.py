# Nが100と小さいので少しは余裕がある
# どの数字に書き換えるか を決めずに最小コストを見積もれるのか？
# 多分だけど要素の平均に一番近い整数が候補だと思う
import math

N = int(input())
A = list(map(int, input().split(" ")))

ave_floor = math.floor(sum(A) / len(A))
ave_ceil = math.ceil(sum(A) / len(A))
sum_floor = 0
sum_ceil = 0
for a in A:
    sum_floor += (a - ave_floor) ** 2
    sum_ceil += (a - ave_ceil) ** 2

print(min(sum_ceil, sum_floor))

# AC 12
# 絞り込んだけど全探索でも可
