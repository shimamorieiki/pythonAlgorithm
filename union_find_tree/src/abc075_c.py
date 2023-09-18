from module.union_find_tree_nkmk import UnionFindNkmk

N, M = map(int, input().split(" "))
A = []
B = []
for _ in range(M):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)
print(N, M, A, B)

# 多分M**2でも計算量的には全然間に合う気がする
answer = 0
for i in range(M):
    uf = UnionFindNkmk(N)
    for index in range(M):
        if index == i:
            continue
        uf.unite(A[index] - 1, B[index] - 1)
    if uf.group_count() >= 2:
        answer += 1

print(answer)
