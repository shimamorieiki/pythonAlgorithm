# 正規表現ゲーだったわ
import re

S = input()

a = re.match(r"^A?KIHA?BA?RA?$", S)
if a is not None:
    print("YES")
else:
    print("NO")

# AC 25m
