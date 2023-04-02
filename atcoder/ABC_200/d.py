# 愚直なのはビット全探索
# 流石に2^200は現実的ではない。
# 要は和を200で割ったあまりが等しくなるような組み合わせがあるかどうか

# 何が困るってAのそれぞれが同じものがないとは一言も言っていないということ。
# 0, 100, 100 みたいなものが存在する。
# N = 200 なのがだいぶ救いがある気がするんだけど。

# 全探索以外に何も思いつかん
# 結局全ての組み合わせについて和を200で割ったあまりを求めることが必要そう。
# N個からi個選んで和のmod200がjになる をそこそこ早い計算量で解く必要がある？

# 存在しますか？だけなら、まだ二分探索とかも可能性ありそうだけど、
# 組み合わせを出せと言われるとなかなか厳しいものがある。

# 小さい例で成立しそうなのはいくつかあるけど、大きくなると途端に破綻する。
# give upかな