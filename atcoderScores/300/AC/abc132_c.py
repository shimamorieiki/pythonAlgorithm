# 高橋君は、 N 個の競技プログラミング用の問題をつくりました。
# それぞれの問題には 1 から N の番号がついており、
# 問題 i の難易度は整数 di で表されます(大きいほど難しいです)。

# 高橋君はある整数 K を決めることで、 
# 難易度が K 以上ならば「 ARC 用の問題」
# 難易度が K 未満ならば「 ABC 用の問題」
# という風に、これらの問題を二種類に分類しようとしています。

# 「ARC 用の問題」と「ABC 用の問題」が同じ数になるような整数 K の選び方は何通りあるでしょうか。
# 制約 
# 2≦N≦10^5
# N は偶数である。
# 1≦di≦10^5
# 入力は全て整数である。

# 6
# 9 1 4 4 6 7

# 2


# N = 6
# a = [9,1,4,4,6,7]

N = int(input())
a = list(map(int,input().split(" ")))

b = [0]*(max(a)+1)
for i in range(N):
    b[a[i]] += 1

# count = 0
for i in range(1,len(b)):
    b[i] = b[i-1] + b[i]
print(b.count(N//2))
# なんとなくバケツソートが有効な気がしている
# AC 12
# なんかもうちょっとさらっとした解答があった
