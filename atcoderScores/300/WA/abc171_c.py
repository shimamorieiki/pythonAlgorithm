# 26進数の計算をすればいい？
N = int(input())
ans = ""
conv = {
    "1":"a",
    "2":"b",
    "3":"c"
}

while N>=26:
    # 商と余り
    s,t = divmod(N, 26)
    N = (N-t)//26
    ans += str(t)+":"

ans += str(s)+":"
print(ans)