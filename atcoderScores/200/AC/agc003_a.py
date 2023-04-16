S = input()

# n,e,s,w
R = [0, 0, 0, 0]
for s in list(S):
    if s == "N":
        R[0] = 1
    if s == "E":
        R[1] = 1
    if s == "S":
        R[2] = 1
    if s == "W":
        R[3] = 1

if R[0] == R[2] and R[1] == R[3]:
    print("Yes")
else:
    print("No")

# AC 6
