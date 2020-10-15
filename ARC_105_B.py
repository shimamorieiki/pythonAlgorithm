def solve(N,a):
    X = max(a)
    x = min(a)
    while x != X :
        a = list(set(a))
        for i in range(len(a)):
            if a[i] == X:
                a[i] = X-x
        X = max(a)
        x = min(a)
    print(max(a))


# a = [2,6,6]
a = [546,3192,1932,630,2100,4116,3906,3234,1302,1806,3528,3780,252,1008,588]
N= len(a)
solve(N,a)
