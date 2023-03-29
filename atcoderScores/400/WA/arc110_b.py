# 全部探すというよりは T の開始文字で大体見当がつく気がする
# これはTが110を連結したものの部分文字列である場合のみ

N = int(input())
T = input()
mod_part = ["", "10", "0"]

if T[0:1] == "0":
    rep, mod = divmod(N - 1, 3)
    if len((T[1:] + mod_part[mod]).replace("110", "")) != 0:
        print(0)
        exit()
    c = 0 if mod == 0 else 1
    print(10**10 - rep - c)
    exit()

if T[0:2] == "10":
    rep, mod = divmod(N - 2, 3)
    if len((T[2:] + mod_part[mod]).replace("110", "")) != 0:
        print(0)
        exit()
    c = 0 if mod == 0 else 1
    print(10**10 - rep - c)
    exit()

if T[0:3] == "110":
    rep, mod = divmod(N, 3)
    if len((T + mod_part[mod]).replace("110", "")) != 0:
        print(0)
        exit()
    c = 0 if mod == 0 else 1
    print(10**10 - rep - c + 1)
    exit()

# WA
# 境界値～～
