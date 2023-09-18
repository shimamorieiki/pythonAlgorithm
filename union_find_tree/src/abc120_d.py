from module.union_find_tree_nkmk import UnionFindNkmk

N, M = map(int, input().split(" "))
A = []
B = []
for _ in range(M):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

# 不便さ
# 橋が1本もない状態から逆算して追加していくので
# 最終的には逆順にして表示
hubensas = [N * (N - 1) // 2]

uf = UnionFindNkmk(N)
for i in range(M):
    reversed_index = M - i - 1
    # このUF木はrootが自分の集合のサイズを持つのでそれを利用する
    # 持たないタイプの実装の場合は、sizeなりrankなりで同様の機能を持つ配列が別に存在するはず
    a_size = uf.parents[uf.find(A[reversed_index] - 1)]
    b_size = uf.parents[uf.find(B[reversed_index] - 1)]
    uf.unite(A[reversed_index] - 1, B[reversed_index] - 1)
    hubensa = max(hubensas[-1] - a_size * b_size, 0)
    hubensas.append(hubensa)

for v in reversed(hubensas[:-1]):
    print(v)
