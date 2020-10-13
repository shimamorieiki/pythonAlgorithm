#要素の重複禁止

def dp(N,wv,W):
    # N 要素の個数
    # wv 要素のリスト
    # W 重さの最大値

    value = [0]*(W+1) #価値のリスト
    updatedValue  = [0]*(W+1)

    for i in range(N):
        for s in range(wv[i][0],W+1):
            p = s - wv[i][0]
            updatedValue[s] = max(value[p] + wv[i][1],value[s])
        value = updatedValue.copy()
        # value = updatedValue だと２つは同じものなので
        # valueの変更がupdatedValueにも反映されてしまう
    print(max(value))

wv = [[2,3],[1,2],[3,4],[2,2]]
dp(4,wv,5)