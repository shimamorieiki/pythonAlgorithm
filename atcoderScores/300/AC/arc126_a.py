# 3の枝は偶数本しか使えないのでそこから削るべき？

T = int(input())
CASE = []
for t in range(T):
    CASE.append(list(map(int,input().split(" "))))

for n2,n3,n4 in CASE:
    count = 0
    # n3とn4でいくつペアを作れるか
    a = min(n3//2,n4)
    count += a
    n4 -= a
    n3 -= a*2
    
    # n3とn2でいくつペアを作れるか
    b = min(n3//2,n2//2)
    count +=b
    n2 -= b*2
    n3 -= b*2
    
    # n2とn4でいくつペアを作れるか
    c = min(n2,n4//2)
    count +=c
    n2 -= c
    n4 -= c*2
    
    # n2とn4でいくつペアを作れるか
    d = min(n2//3,n4)
    count +=d
    n2 -= d*3
    n4 -= d
    
    # n2でいくつペアを作れるか
    # n2とn4でいくつペアを作れるか
    e = n2//5
    count +=e
    print(count)
    
# AC 25m
# 途中の過程はともかく最終的にはそれっぽいことを言っているので多分合ってる