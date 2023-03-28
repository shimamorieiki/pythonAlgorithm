# 一番入力が大きい時ですらkは10^4のオーダーなので二乗までは計算時間に余裕がある

A = int(input())
answers = []

for i in range(10, 10000):
    if len(str(i)) == 2:
        s = str(i)
        a = int(s[0]) * i + int(s[1])
        answers.append(a)
    if len(str(i)) == 3:
        s = str(i)
        a = int(s[0]) * i**2 + int(s[1]) * i + int(s[2])
        answers.append(a)
    if len(str(i)) == 4:
        s = str(i)
        a = int(s[0]) * i**3 + int(s[1]) * i**2 + int(s[2]) * i + int(s[3])
        answers.append(a)

answers.append(10000000000000000)

if A in answers:
    print(answers.index(A) + 10)
else:
    print(-1)

# AC 28m
