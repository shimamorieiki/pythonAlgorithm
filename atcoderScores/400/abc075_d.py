# 2次元座標上に N 個の点があります。
# i(1≦i≦N) 番目の点の座標は (xi,yi) です。
# 長方形の内部に N 点のうち K 個以上の点を含みつつ、それぞれの辺がX軸かY軸に平行な長方形を考えます。
# このとき、長方形の辺上の点は長方形の内部に含みます。
# それらの長方形の中で、最小の面積となるような長方形の面積を求めてください。
# 制約
# 2≦K≦N≦50
# −10^9≦xi,yi≦10^9(1≦i≦N)
# xi≠xj(1≦i<j≦N)yi≠yj(1≦i<j≦N)
# 入力値はすべて整数である。(21:50 追記)

# 最初は長方形が出てきたから二次元いもすかと思ったけど、多分違いそう。
# K個以上ってことは実質K個ギリギリで文句ないだろ？
# 何も思いつかん
# 長方形の候補で全探索かけられるのか。
# 候補の点が少ないことから気がつくべきだった？