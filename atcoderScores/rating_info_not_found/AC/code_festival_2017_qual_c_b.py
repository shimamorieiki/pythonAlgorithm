# 全ての項の積が偶数ということは項のどれか1つが偶数
# 全ての組み合わせからすべて奇数の組み合わせを引く

N = int(input())
A = list(map(int, input().split(" ")))

c = 1
for a in A:
    if a % 2 == 0:
        c *= 2

print(3**N - c)

# AC 7
