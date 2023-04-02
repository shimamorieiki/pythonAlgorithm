S = []
for _ in range(8):
    S.append(input())
    
S.reverse()

col = ["a","b","c","d","e","f","g","h"]

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(col[j]+str(i+1))
            exit()
            