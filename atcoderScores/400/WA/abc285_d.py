# 直感的にはSとTが完全に一致していたら変更できないが
# 1つでも異なっているものが存在したら変更できると思う
# 1つでも異なっているものが[0,1,2],[1,0,3]の場合はダメ
# つまり両方に共通しているものが閉じていたらだめ

N = int(input())
S = [0] * N
T = [0] * N
for i in range(N):
    S[i], T[i] = input().split(" ")

and_ = set(S) & set(T)

# S,Tの各要素が完全に一致している
if len(and_) == N:
    print("No")
    exit()

d = set()
count = 0
for s, t in zip(S, T):
    if s in and_ and t in and_:
        d.add("".join(sorted([s, t])))
        count += 1

# もしlen(d) != count なら
# 両方に共通するものが巡回している
if len(d) == count:
    print("Yes")
else:
    print("No")

# WA 方針は合っている
# 出来ていないのは閉路検出
