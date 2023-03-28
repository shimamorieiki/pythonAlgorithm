S = input()
T = input()

for s, t in zip(S, T):
    if s == "@" and t == "@":
        continue

    if s == "@" and t != "@":
        if t in ["a", "t", "c", "o", "d", "e", "r"]:
            continue
        else:
            print("You will lose")
            exit()

    if s != "@" and t == "@":
        if s in ["a", "t", "c", "o", "d", "e", "r"]:
            continue
        else:
            print("You will lose")
            exit()

    if s != t:
        print("You will lose")
        exit()

print("You can win")

# AC 8