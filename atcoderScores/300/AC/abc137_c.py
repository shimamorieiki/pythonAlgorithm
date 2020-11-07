# 文字列 a に含まれる文字を何らかの順序で並べることで得られる文字列を a の アナグラム と呼びます。
# 例えば、greenbin は beginner のアナグラムです。
# このように、同じ文字が複数回現れるときはその文字をちょうどその回数だけ使わなければなりません。
# N個の文字列 s1,s2,…,sN が与えられます。
# それぞれの文字列は長さが 10 で英小文字からなり、またこれらの文字列はすべて異なります。
# 二つの整数 i,j (1≤i<j≤N) の組であって、
# si が sj のアナグラムであるようなものの個数を求めてください。
# 制約
# 2≤N≤105
# siは長さ 10 の文字列である。
# si の各文字は英小文字である。
# s1,s2,…,sN はすべて異なる。

# 3
# acornistnt
# peanutbomb
# constraint

# 1

# N = 3
# s= ["acornistnt","peanutbomb","constraint"]

N = int(input())
s = []
for i in range(N):
    s.append(input())
dic = {}

for i in s:
    if "".join(sorted(i)) in dic:
        dic["".join(sorted(i))] += 1
    else:
        dic["".join(sorted(i))] = 1

res = 0
for i in dic.values():
    res += i*(i-1) //2
print(res)

# AC 13