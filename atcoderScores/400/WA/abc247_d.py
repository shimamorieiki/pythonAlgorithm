# dequeでも計算量が厳しそうだし累積和でも厳しそう
# xとcがどっちも大きすぎて何も思い浮かばない

Q = int(input())
QUERY = []

for q in range(Q):
    QUERY.append(list(map(int,input().split(" "))))
    
print(QUERY)

# WA
# そりゃそうって感じだけどなんか思いつかなかった
