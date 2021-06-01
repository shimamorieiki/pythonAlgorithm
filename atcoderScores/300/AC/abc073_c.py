# あなたは、joisinoお姉ちゃんと以下のようなゲームをしています。
# 最初、何も書いていない紙がある。
# joisinoお姉ちゃんが一つの数字を言うので、その数字が紙に書いてあれば紙からその数字を消し、
# 書いていなければその数字を紙に書く。これを N回繰り返す。
# その後、紙に書かれている数字がいくつあるかを答える。

# joisinoお姉ちゃんが言った数字が、言った順番に A1,...,ANとして与えられるので、
# ゲーム終了後に紙に書かれている数字がいくつあるか答えてください。
# 制約

# 1≦N≦100000
# 1≦Ai≦1000000000(=10^9)
# 入力は全て整数である。

# N
# A1
# :
# AN

# 3
# 6
# 2
# 6

# 1
# 二回目
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

a = sorted(a)

s = a[0]
count = 0
ans = 0
for i in range(1,len(a)):
    if s == a[i]:
        count+=1
    else:
        if count % 2 == 0:
            ans +=1
        count =0
    s = a[i]
else:
    if count % 2 == 0:
        ans +=1
print(ans)
# 一回目
# result = []
# N = int(input())
# for i in range(N):
#     x = int(input())
#     if result.count(x)==0:
#         result.append(x) #ここがresult内を走査してるから計算量O(1)じゃないってことか
#     else: 
#         result.remove(x)
# print(len(result))

# result = [0]*(10**9) が大きすぎるらしい
# バケツソートの方法で頑張ろうとした
#取ったりぬいたりするなら結局最終的に偶数個あるか奇数個あるかの判断でいいはずなのよね
# 計算量を減らす方法がわからなかった
# ソートして左から見ればいいらしい
#AC16 解答見た