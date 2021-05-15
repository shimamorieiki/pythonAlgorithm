import sys
import math

if __name__ == '__main__':
    step = int(input())
    if step == 2:
        N = int(input())
        A = list(map(int,input().split(" ")))
        total = 0 # 経過時間の合計
        mn = 1000000000 # 経過時間の最小値
        TS = [[] for i in range(N)]
        for j in range(N):
            K = int(input())
            for i in range(K):
                t, s = map(int,input().split(" "))
                TS[j].append([t,s])

        Q = int(input())
        for i in range(Q):
            L = int(input())
            for i in range(len(TS)):
                for j in TS[i]:
                    t = j[0]
                    s = j[1]
                    tm = math.ceil((math.sqrt((2*s-1) ** 2 + 8 * (A[i]-L))+1) / 2 - s) + t #合計時間
                    print("t,s,tm",t,s,tm)
                    if tm < mn:
                        mn = tm
                total += mn
            mn = 1000000000
            print("total",total)
            total = 0
            break