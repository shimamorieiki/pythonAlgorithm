# 1 から N までの番号がついた N 人の人がいます。
# 彼らはみな、必ず正しい証言を行う「正直者」か、
# 真偽不明の証言を行う「不親切な人」のいずれかです。
# 人 i は Ai 個の証言を行っています。
# 人 i の j 個目の証言は 2 つの整数 xij , yij で表され、
# yij=1 のときは「人 xij は正直者である」という証言であり、
# yij=0 のときは「人 xij は不親切な人である」という証言です。
# この N 人の中には最大で何人の正直者が存在し得るでしょうか？
# 制約
# 入力は全て整数
# 1≤N≤15
# 0≤Ai≤N−1
# 1≤xij≤N
# xij≠i
# xij1≠xij2(j1≠j2)
# yij=0,1

# 3
# 1
# 2 1
# 1
# 1 1
# 1
# 2 0

# 2

# あんまりやりたくない