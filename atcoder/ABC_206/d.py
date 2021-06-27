n = int(input())
s = list(map(int,input().split(" ")))
c = []
path = []
for i in range(n // 2 + n%2):
    if s[i] < s[n-i-1]:
        path.append([s[i],s[n-i-1]])
    elif s[i] > s[n-i-1]:
        path.append([s[n-i-1],s[i]])
if len(path) == 0:
    print(0)
    exit()
count = 1
c = set(path[0])
for i in path[1:]:
    if c.issuperset(i):
        pass
    else:
        c = c | set(i)
        count += 1

print(count)

# 変換しないといけないものをグラフのパスだと見て幅優先探索
# 計算量がオーバーする気がする
# 最終的なパスの数が変換しないといけない回数
# グラフを書きたくない理由は、頂点が数字順になっておらず、パスの関係を記述すると二重ループになるから。