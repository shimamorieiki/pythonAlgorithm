N = int(input())
S = input()

s = S.replace("MM","X").replace("FF","X")

if s.count("X") > 0:
    print("No")
else:
    print("Yes")
    