# 英小文字のみからなる文字列 S, T が与えられます。
# 文字列 S に対して、次の操作を何度でも行うことができます。
# 操作: 2つの異なる英小文字 c1 , c2 を選び、S に含まれる全ての c1 を c2 に、c2 を c1 に置き換える
# 0 回以上操作を行って、S を T に一致させられるか判定してください。
# 制約
# 1≤|S|≤2×105
# |S|=|T|
# S, T は英小文字のみからなる

# azzel
# apple

# Yes

# s = "azzel"
# t = "apple"

s = input()
t = input()
a = [[0]*26 for i in range(26)]
b = [[0]*26 for i in range(26)]
for i in range(len(s)):
    s_a = int(ord(s[i])-97)
    t_a = int(ord(t[i])-97)
    a[s_a][t_a] = 1
    b[t_a][s_a] = 1
    if a[s_a].count(1) >= 2 or b[t_a].count(1) >= 2:
        print("No")
        break
else:
    print("Yes")
# 頻度情報はあんまり有効じゃない
# 前から調べていけばたかだか26通り？
# S,T それぞれでどちらも単語の置換方法が２つ以上ないことを示せばいい？
# AC 30