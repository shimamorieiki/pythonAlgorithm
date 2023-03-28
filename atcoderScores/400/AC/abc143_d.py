# 愚直に全パターンを試すとTLE
# どれか1つを固定したい
# a <= b <= c としても一般性を失わない
# 最も長くない2辺(a,b)を先に選んだときに、
# 最長辺cとして取れるのは b <= c <= a+b-1 の範囲
# 同じ長さの辺を使用する場合がだいぶ面倒くさい
from bisect import bisect
from itertools import combinations

N = int(input())
L = sorted(list(map(int, input().split(" "))))

c = 0
for start, end in combinations(range(len(L)), 2):
    i = end + 1
    j = bisect(L, L[start] + L[end] - 1)
    c += j - i

print(c)

# AC 30m over
# 公式解説通りなのでOK