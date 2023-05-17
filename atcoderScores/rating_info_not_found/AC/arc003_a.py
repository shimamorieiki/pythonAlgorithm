N = int(input())
S = input()

sum = 0
for s in S:
    if s == "A":
        sum += 4
    elif s == "B":
        sum += 3
    elif s == "C":
        sum += 2
    elif s == "D":
        sum += 1
    elif s == "F":
        sum += 0

print(sum / N)

# AC 5m
