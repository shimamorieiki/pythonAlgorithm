# int(input())
# list(map(int,input().split(" ")))
# map(int,input().split(" "))
# a = []
# for i in a:
#     a.append(list(map(int,input().split(" "))))# map(int,input().split(" "))


# 給湯器が 1 つあり、毎分 W リットルのお湯を供給することができます。
# N 人の人がいます。
# i 番目の人は時刻 Si から Ti までの間 (時刻 Ti ちょうどを除く)、
# この湯沸かし器で沸かしたお湯を毎分 Pi リットル使おうと計画しています。
# お湯はすぐ冷めてしまうので、溜めておくことはできません。
# すべての人に計画通りにお湯を供給することはできますか？
# 制約
# 1≤N≤2×10^5
# 0≤Si<Ti≤2×10^5
# 1≤W,Pi≤10^9
# 入力はすべて整数

N,W = 4,10
a = [[1, 3, 5], [2, 4, 4], [3, 10, 6], [2, 4, 1]]
# N,W = map(int,input().split(" "))
# a = []
# for i in range(N):
#     a.append(list(map(int,input().split(" "))))

b = [0]*(2*(10**5))
for i in a:
    

if max(b) <=W:
    print("Yes")
else:
    print("No")
# これがLTEなことくらい最初から分かってた
# 多分自分の知ってるテクニックでは解けないんだと思う
# 以上!!
# 範囲が定まっており、その内側を全部埋めないといけないときが難しい
# こういうときは右端から左端を引けばどうにかなりそうだが、思いつかない