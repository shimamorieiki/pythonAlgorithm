# 正規表現ゲーでは？
import re

S = input()

a = list(set(re.findall(r"@[a-z]+", S)))
for i in sorted(a):
    print(i.replace("@", ""))

# AC 10m
# 正規表現ゲーじゃん
