import math
N = int(input())
rt = math.ceil(math.sqrt(N))
stac = []
for i in range(1,rt+1):
    if N%i == 0:
        stac.append(i)
        stac.append(N//i)
stac = list(set(stac))
stac.sort()
for i in stac:
    print(i)
# AC18
# 全体的には理解してたけどi^2の扱いとか忘れてた