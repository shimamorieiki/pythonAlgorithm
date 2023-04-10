S = input()

B = []
R = 0

for i,s in enumerate(S):
    if s == "B":
        B.append(i)
    if s == "K" and R != 1:
        print("No")
        exit()
    if s == "R":
        R+=1

if (B[1] - B[0]) %2 == 1:
    print("Yes")
else:
    print("No")