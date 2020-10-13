def dp(N,wv,W):
    # N 要素の個数
    # wv 要素のリスト
    # W 重さの最大値

    value = [0]*(W+1) #価値のリスト
    newValue = 0

    for i in range(N):
        for s in range(wv[i][0],W+1):
            p = s - wv[i][0]
            value[s] = max(value[p] + wv[i][1],value[s])
    print(max(value))
    
    #どう見ても同じものを二回入れているように見えるけどその理由がよくわかんない
    #これはvalue[2] = 3をvalue[4]のときに使ってる => いわゆる重複ありのときだから

wv = [[2,3],[1,2],[3,4],[2,2]]
dp(4,wv,5)