# 1つだけ上手く行かないものがある
# 多分 fofoxxのように入れ子になっているものだとは思う

N = int(input())
s = input()

while True:
    bef_s = s
    s = s.replace("fox", "")
    if bef_s == s:
        break

print(len(s))

# WA 15m
# なるほど
# 本質はネストのところであっていたみたい
# これは推論とテクニックの中間くらいみたいなところだった
