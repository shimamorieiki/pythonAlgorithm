# 全部見ようとすると爆発的に組み合わせが増える
# 何となく累積和っぽいのが見える
# give up 30m

a = "ABCCAABBACCAABCAAABBC"

b = [[[] for _ in range(len(a))] for _ in range(len(a))]

print(b)

for i,v in enumerate(a):
    print(i,v)
    
# 