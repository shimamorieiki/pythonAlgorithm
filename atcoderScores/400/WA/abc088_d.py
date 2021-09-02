H,W = map(int,input().split(" "))
a = []
for i in range(H):
    a.append(list(input()))

inf = float("inf")
visited = [[0]*W for _ in range(H)]
value = [[inf]*W for _ in range(H)]

def shortest_path(h,w):
    # 訪れていればその値を使う
    if visited[h][w] == 1:
        return value[h][w]

    if h == 0 and w == 0:
        return 1

    # 枠外なら何もしない
    if h >= H or w >= W or h < 0 or w < 0:
        return inf
    
    # 扉なら何もしない
    if a[h][w] == "#":
        return inf
    
    value[h][w-1] = shortest_path(h,w-1)
    visited[h][w-1] = 1

    value[h-1][w] = shortest_path(h-1,w)
    visited[h-1][w] = 1

    value[h][w+1] = shortest_path(h,w+1)
    visited[h][w+1] = 1
    
    value[h+1][w] = shortest_path(h+1,w)
    visited[h+1][w] = 1

    return min(value[h][w-1],value[h-1][w],value[h][w+1],value[h+1][w])+1

b = sum(a,[]).count(".")
ans = shortest_path(H-1,W-1)
if ans == inf:
    print(-1)
    exit()
print(b-ans)

# 幅優先探索と言われても
# 120分かけたけど解けなかった