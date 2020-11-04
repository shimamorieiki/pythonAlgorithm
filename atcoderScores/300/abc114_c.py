# 整数 N が与えられます。1 以上 N 以下の整数のうち、七五三数 は何個あるでしょうか？
# ここで、七五三数とは以下の条件を満たす正の整数です。
# 十進法で表記したとき、数字 7, 5, 3 がそれぞれ 1 回以上現れ、これら以外の数字は現れない。
# 制約
# 1≤N<10^9
# Nは整数である。

# 575

# 4

# N = 5758

# N = int(input())

# a = [357,375,537,573,735,753]
# count = 0
# if len(str(N)) <= 3:
#     for i in a:
#         if N >= i:
#             count += 1
#     print(count)
# else:
#     temp3 = []
#     temp5 = []
#     temp7 = []
#     res  = a.copy()
#     for i in range(len(str(N))-3):
#         temp = []
#         temp3 = [int(str(i)+"3") for i in a]
#         temp.extend(temp3)
#         temp5 = [int(str(i)+"5") for i in a]
#         temp.extend(temp5)
#         temp7 = [int(str(i)+"7") for i in a]
#         temp.extend(temp7)
#         res.extend(list(set(temp)))
#         a = list(set(temp)).copy()
#     print(res)
#     for i in res:
#         if N >= i:
#             count += 1
#     print(count)

# これで上手く行かないなら知らない
# AC 解答見た

N=int(input())
def dfs(s):#文字列sで始まる七五三数の個数
    if int(s)>N:
        return 0
    ret=1 if all(s.count(c)>0 for c in "753")else 0
    # s自体が七五三数なら+
    # s自体が七五三数でなくてもそれより大きい桁で七五三数になることもあるってことか
    for c in "753":
        ret+=dfs(s+c)
    return ret
print(dfs("0"))#本当はdfs(  )と書きたいが4行目でのエラーを防ぐため仕方なく

# 何を理解するのかはよくわからんけど all() とかいう演算子は初めて見た
# 確かに凖七五三数とかはわかった気がする