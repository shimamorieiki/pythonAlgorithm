# 高橋くんは N 人の生徒たちのいるクラスの担当教師です。
# 生徒たちには 1 から N までの出席番号が重複なく割り当てられています。
# 今日は全ての生徒たちが相異なるタイミングで登校しました。
# 高橋くんは、出席番号 i の生徒が登校した時点で、
# 教室に Ai 人の生徒たちがいたことを記録しています(出席番号 i の生徒を含む)。
# 記録された情報を元に、生徒たちの登校した順番を復元してください。
# 制約
# 1≤N≤10^5
# 1≤Ai≤N
# Ai≠Aj
# (i≠j)
# 入力はすべて整数

# 3
# 2 3 1

# 3 1 2

N = int(input())
a = list(map(int,input().split(" ")))
a = [[a[i],i+1] for i in range(N)]
a.sort()
a = [str(i[1]) for i in a]
print(" ".join(a))

# AC 6