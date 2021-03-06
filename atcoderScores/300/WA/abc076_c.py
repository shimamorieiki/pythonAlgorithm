# E869120 は、宝物が入ってそうな箱を見つけました。
# しかし、これには鍵がかかっており、鍵を開けるためには英小文字からなる文字列 S が必要です。
# 彼は文字列 S′ を見つけ、これは文字列 S の 0 個以上 |S| 個以内の文字が ? に置き換わった文字列であることも分かりました。
# ただし、文字列 A に対して、|A| を「文字列 Aの長さ」とします。

# そこで、E869120 はヒントとなる紙を見つけました。

# 条件1：文字列 Sの中に連続する部分文字列として英小文字から成る文字列 Tが含まれている。
# 条件2：Sは、条件1を満たす文字列の中で辞書順最小の文字列である。
# そのとき、鍵となる文字列 Sを出力しなさい。
# ただし、そのような文字列 S が存在しない場合は代わりに UNRESTORABLE と出力しなさい。
# 制約
# 1≤|S′|,|T|≤50
# S′は英小文字と ? から成る
# T は英小文字から成る

# S′
# T

# ?tc????
# coder

# atcoder
# 2回目
S = list(input())
T = list(input())
sB = S[:]
ans = []
if len(T) > len(S):
    print("UNRESTORABLE")
else:
    for i in range(len(S)-len(T)+1):
        s = sB[:]
        for j in range(len(T)):
            if  s[i+j] == T[j] or s[i+j] == "?":
                s[i+j] = T[j]
            else:
                break
        else:
            ans.append("".join(s).replace("?","a"))
            
if len(ans) == 0:
    print("UNRESTORABLE")
else:
    ans = sorted(ans)
    print(ans[0])
# 二回目反省
# ?b??
# ab
# のときに abaaにならない。
# なんか上手く行かない。


# 1回目
# S = "?tc????"
# T = "coder"

# srv = "".join(list(reversed(S)))
# trv = "".join(list(reversed(T)))
# print(srv,trv)
# dp = [[0]*(len(srv)) for i in len(trv)]

# for i in range(1,len(srv)):
#     if trv[0]==srv[i] or srv[i]=="?":
#         dp[0][i] = trv[0]

# for i in range(1,len(trv)):
#     for j in range(1,len(srv)):
#         if trv[i]==srv[j] or srv[j]=="?":
#             dp[i][j] = dp[i-1][j-1]+trv[i]



# これあれだ。共有する文字列の最長みたいなやつ
# dp使うやつ
# dp[i][j] = srvがi文字 trvがj文字目のときに　trvの先頭j文字が?含め一致しているときの文字列
# dp[i][j] = dp[i-1][j-1] + trv[j] if(srv[i] = trv[j] or srv[i]="?")
# 方針はこんなのでいい気がするけど上手く行かない

# dp使わなかった
# 可能性のある区間全体で考えてその中の最小値を見つければ良さそう
#AC 解答見た