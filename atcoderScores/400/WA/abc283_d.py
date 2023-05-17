# やることは分かった。
# 実装するだけ問題？
# 全ての閉じ括弧について適切な開き括弧の位置は分かる
# 区間和的なものだと思ったけどsetの区間和的なものの扱いが分からなかった。
# 全てのステップごとでsetを持てば良さそうだけど最悪N^2(TLE)になりそうな気がした

S = input()
paren_left_index = []
paren_right_index = {}
chars = ["" for _ in range(len(S))]

for index, s in enumerate(list(S)):
    print(index, s)
    if s == "(":
        paren_left_index.append(index)
    elif s == ")":
        paren_right_index.setdefault(index, paren_left_index.pop())
    else:
        chars[index] = s
print(paren_right_index)
print(chars)

for i in range(1, len(chars)):
    chars[i] = chars[i - 1] + chars[i]
print(chars)

numbers = []
for index, s in enumerate(list(S)):
    if s == "(":
        pass
    elif s == ")":
        numbers = list(chars[len(chars[paren_right_index[index]]) :])
        print("numbers: ", numbers)
        if len(numbers) != len(list(set(numbers))):
            print("No")
            exit()

# WA 30m
# 全ての状態に対してsetを作る必要はないのか。
# 確かに括弧で囲まれているものについてsetを作れば作る量は減る
