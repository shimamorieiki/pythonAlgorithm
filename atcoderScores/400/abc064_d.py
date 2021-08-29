# ()の話はヒューリスティックでどうにかなった記憶がある。e8先生のやつ。
# 常に"("は")"より多い
# 正しい列なら"("と")"は同数

N = int(input())
S = input()
s = 0
e = 0
ans = ""

for i in S:
    if i == "(":
        s += 1
        ans += i
    else:
        e += 1
        if e > s:
            ans = "(" + ans + i
            s += 1
        else:
            ans = ans + i

for i in range(s - e):
    ans += ")"

print(ans)

# AC