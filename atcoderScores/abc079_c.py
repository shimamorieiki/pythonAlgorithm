# 駅の待合室に座っているjoisinoお姉ちゃんは、切符を眺めています。
# 切符には 4つの 0 以上 9 以下の整数 A,B,C,Dが整理番号としてこの順に書かれています。
# A op1 B op2 C op3 D = 7 となるように、
# op1,op2,op3に + か - を入れて式を作って下さい。
# なお、答えが存在しない入力は与えられず、
# また答えが複数存在する場合はどれを出力してもよいものとします。
# 制約

# 0≦A,B,C,D≦9
# 入力は整数からなる
# 答えが存在しない入力は与えられない

a,b,c,d = map(int,list(input()))
r1 = a + b + c + d
r2 = a + b + c - d
r3 = a + b - c + d
r4 = a + b - c - d
r5 = a - b + c + d
r6 = a - b + c - d
r7 = a - b - c + d
r8 = a - b - c - d

if r1==7:
    print(str(a)+"+"+str(b)+"+"+str(c)+"+"+str(d)+"=7")
elif r2==7:
    print(str(a)+"+"+str(b)+"+"+str(c)+"-"+str(d)+"=7")
elif r3==7:
    print(str(a)+"+"+str(b)+"-"+str(c)+"+"+str(d)+"=7")
elif r4==7:
    print(str(a)+"+"+str(b)+"-"+str(c)+"-"+str(d)+"=7")
elif r5==7:
    print(str(a)+"-"+str(b)+"+"+str(c)+"+"+str(d)+"=7")
elif r6==7:
    print(str(a)+"-"+str(b)+"+"+str(c)+"-"+str(d)+"=7")
elif r7==7:
    print(str(a)+"-"+str(b)+"-"+str(c)+"+"+str(d)+"=7")
elif r8==7:
    print(str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d)+"=7")

#AC 13