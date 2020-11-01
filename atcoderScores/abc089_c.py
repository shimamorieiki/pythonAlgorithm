# N 人の人がいて、i 番目の人の名前は Siです。
# この中から、以下の条件を満たすように 3人を選びたいです。

# 全ての人の名前が M,A,R,C,H のどれかから始まっている
# 同じ文字から始まる名前を持つ人が複数いない

# これらの条件を満たすように 3人を選ぶ方法が何通りあるか、求めてください。
# ただし、選ぶ順番は考えません。
# 答えが 32bit整数型に収まらない場合に注意してください。

# 制約
# 1≤N≤105
# Siは英大文字からなる
# 1≤|Si|≤10
# Si≠Sj(i≠j

# 5
# MASHIKE
# RUMOI
# OBIRA
# HABORO
# HOROKANAI

# 2

N = int(input())
c = 0
name = [0]*5
for i in range(N):
    x  = input()
    if x[0] == "M":
        name[0] += 1
    elif x[0] == "A":
        name[1] += 1
    elif x[0] == "R":
        name[2] += 1
    elif x[0] == "C":
        name[3] += 1
    elif x[0] == "H":
        name[4] += 1

if name[0]!=0 and name[1]!=0 and name[2]!=0:
    c += name[0] * name[1] * name[2] 
if name[0]!=0 and name[1]!=0 and name[3]!=0:
    c += name[0] * name[1] * name[3]
if name[0]!=0 and name[1]!=0 and name[4]!=0:
    c += name[0] * name[1] * name[4] 
if name[0]!=0 and name[2]!=0 and name[3]!=0:
    c += name[0] * name[2] * name[3] 
if name[0]!=0 and name[2]!=0 and name[4]!=0:
    c += name[0] * name[2] * name[4] 
if name[0]!=0 and name[3]!=0 and name[4]!=0:
    c += name[0] * name[3] * name[4] 
if name[1]!=0 and name[2]!=0 and name[3]!=0:
    c += name[1] * name[2] * name[3] 
if name[1]!=0 and name[2]!=0 and name[4]!=0:
    c += name[1] * name[2] * name[4]
if name[1]!=0 and name[3]!=0 and name[4]!=0:
    c += name[1] * name[3] * name[4] 
if name[2]!=0 and name[3]!=0 and name[4]!=0:
    c += name[2] * name[3] * name[4] 

print(c)

#AC 12