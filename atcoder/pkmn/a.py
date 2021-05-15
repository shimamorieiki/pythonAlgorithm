import sys
import math

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

# def step1(N,A,K,TS):

# def step2(N,A,K,TS):
    
# def step3(N,A,K,TS):

if __name__ == '__main__':
    step = int(input())
    if step == 1:
        N = int(input())
        A = list(map(int,input().split(" ")))
        total = 0 # 経過時間の合計
        mn = 1000000000 # 経過時間の最小値
        
        for j in range(N):
            K = int(input())
            for i in range(K):
                t, s = map(int,input().split(" "))
                tm = math.ceil((math.sqrt((2*s-1) ** 2 + 8 * A[j])+1) / 2 - s) + t#合計時間
                if tm < mn:
                    mn = tm
            total += mn
            mn = 1000000000
        print(total)