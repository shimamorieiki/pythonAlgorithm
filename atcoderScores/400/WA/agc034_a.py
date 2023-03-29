# SかFが先にゴールしてそれを石とみなしてよいかが怪しい
# 要は先にゴールしてしまうともう片方がゴールできないが、
# 一旦別の場所に退避してからならゴールできるとかだと話が面倒くさそう
# 多分だけど先にゴールして石とみなすで良いはず
# なんならゴールが遠いほうから先に攻めてよいはず
# とりあえずDPで良いと思う。

# 例題3がだめな(一旦退避する)例
# となったら、二次元でDPするしかなさそう
# dp[i][j] = すぬけがi、ふぬけがjのときにゴールできるかどうか(0/1)

N, A, B, C, D = map(int, input().split(" "))
S = input()

T = [-1 for _ in range(N)]

for i in range(N):
    if S[i] == "#":
        T[i] = 0
    else:
        T[i] = 1


def solve(start, goal, cants):
    R = [-1 for _ in range(N)]
    for cant in cants:
        R[cant - 1] = 0
    R[start - 1] = 1
    stack = []
    stack.extend([start, start + 1])
    while len(stack) > 0:
        next = stack.pop()
        if next < N and R[next] == -1:
            if T[next] == 1:
                R[next] = 1
                if R.count(-1) == 0:
                    break
                stack.insert(0, next + 1)
                stack.insert(0, next + 2)
            else:
                R[next] = 0
    return R[goal - 1] == 1


a = (solve(B, D, [A]) and solve(A, C, [D])) or (solve(A, C, [B]) and solve(B, D, [C]))

if a:
    print("Yes")
else:
    print("No")

# WA
# そんなばかな
