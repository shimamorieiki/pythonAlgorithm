# 問題文

# 日本でよく使われる紙幣は、10000 円札、5000 円札、1000円札です。
# 以下、「お札」とはこれらのみを指します。

# 青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N枚入っていて、
# 合計で Y円だったそうですが、嘘かもしれません。
# このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。
# なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

# 制約

# 1≤N≤2000
# 1000≤Y≤2×107
# N は整数である。
# Y は 1000 の倍数である。

# 9 45000
# 4 0 5
N,Y  =map(int,input().split(" "))
resi,resj,resk = -1,-1,-1

for i in range(min(Y//10000+1,N+1)):
    xf = 10000*i
    for j in range(min((Y-xf)//5000+1,N+1)):
        xh = 5000*j
        if 10000*i+5000*j+1000*(N-i-j)==Y:
                resi,resj,resk = i,j,(N-i-j)
            

print("{0} {1} {2}".format(resi,resj,resk))

# 大きい方から取っていって貪欲法でいけそうなきがしてるんだけどだめかな
# AC 33