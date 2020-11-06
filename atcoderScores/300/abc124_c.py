# 左右一列に N 枚のタイルが並んでおり、各タイルの初めの色は長さ N の文字列 S で表されます。
# 左から i 番目のタイルは、S の i 番目の文字が 0 のとき黒色で、1 のとき白色で塗られています。
# あなたは、いくつかのタイルを黒色または白色に塗り替えることで、
# どの隣り合う 2 枚のタイルも異なる色で塗られているようにしたいです。
# 最小で何枚のタイルを塗り替えることで条件を満たすようにできるでしょうか。
# 制約
# 1≤|S|≤10^5
# Siは 0 または 1 である。

# 000

# 1

# S = "000"
S = input()

countl0 = 0
countl1 = 0
for i in range(len(S)):
    if (i % 2 == 0 and S[i] == "0") or (i % 2 == 1 and S[i] == "1"):
        countl0 += 1
    
    if (i % 2 == 0 and S[i] == "1") or (i % 2 == 1 and S[i] == "0"):
        countl1 += 1
        
print(min(countl0,countl1))

# AC 10