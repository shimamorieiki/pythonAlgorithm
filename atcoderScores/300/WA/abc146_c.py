# 高橋くんは整数を 1 つ買いに整数屋さんに行きました。
# 整数屋さんには 1 以上 10^9 以下の整数が売られていて、
# 整数 N を買うためには A×N+B×d(N) 円が必要です。ここで、d(N) は N の十進表記での桁数です。
# 高橋くんの所持金が X 円のとき、高橋くんの買うことのできる最も大きい整数を求めてください。
# ただし、買うことのできる整数が 1 つもない場合は 0 を出力してください。
# 制約
# 入力は全て整数である。
# 1≤A≤10^9
# 1≤B≤10^9
# 1≤X≤10^18
# 10 7 100

# 9

# A,B,X = 10,7,100

A,B,X = map(int,input().split(" "))
start = 1
end = 10**9
i = 5*10**8
while True:
    if A*i+B*len(str(i)) > X:
        end = i
        i = (start + end)//2        
    else:
        start = i
        i = (start + end)//2
    if end == start :
        break
print(start)
# if A*start+B*len(str(start))>X:
#     print(0)
# elif A*end+B*len(str(end))>X:
#     print(10**9)
# else:
#     for k in range(start,end+1):  
#         if A*k+B*len(str(k)) >= X:
#             print(A*k+B*len(str(k)))
#             break
#     else:
#         print(10**9)
# そりゃ全部10^9で回せばいいのはそうなんだけど計算量が間に合わないので
# 二分探索でも使ってみようかね
# AC 解答見た
# あんまりおもいつかなかった
# やっぱり二分探索やないかい これは単純に実装力の問題