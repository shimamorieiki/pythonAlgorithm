# 最大は c,d,e
# 二番目は b,d,eか

A,B,C,D,E = map(int,input().split(" "))

G = [A+B+C,A+B+D,A+B+E,A+C+D,A+C+E,A+D+E,B+C+D,B+C+E,B+D+E,C+D+E]

G = list(reversed(sorted(G)))
print(G[2])

# AC 5m