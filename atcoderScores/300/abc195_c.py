N = int(input())

n5 = 1000000000000000
n4 = 1000000000000
n3 = 1000000000
n2 = 1000000
n1 = 1000
if N == n5:
    print(5+ 4*(n5-n4) + 3*(n4-n3) + 2*(n3-n2) + (n2-n1))
elif N >= n4:
    print(4*(N-n4+1) + 3*(n4-n3) + 2*(n3-n2) + (n2-n1))
elif N >= n3:
    print(3*(N-n3+1) + 2*(n3-n2) + (n2-n1))
elif N >= n2:
    print(2*(N-n2+1) + (n2-n1))
elif N >= n1:
    print(N-n1+1)
else:
    print(0)

# AC24