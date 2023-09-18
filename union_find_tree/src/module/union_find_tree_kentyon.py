from collections import defaultdict


class UnionFindKentyon:
    """_summary_
    けんちょん本の実装によるUF木
    """

    def __init__(self, n: int):
        self.n = n
        # 各要素の親要素のインデックスを格納する
        # 自分がグループの根なら、-(グループの要素数) を持つ
        # 初期値は全要素がグループの根なのですべて -1(自分しか要素がない)
        self.parents: list[int] = [-1] * n
        self.size: list[int] = [1] * n

    def root(self, x: int):
        """_summary_
            要素xが属するグループの根の要素を返す
        Args:
            x (int): _description_

        Returns:
            _type_: _description_
        """
        # parents[x] == -1 つまり「自分自身が、何かのグループの根」の場合は自分自身を返す
        if self.parents[x] == -1:
            return x

        # それ以外 つまり「自分が何かのグループに(根ではなく)属している」場合は自分の親要素を返す(端的に言えば)
        # 実際は、再帰的にparentの値を更新しているので、そのグループ内の要素はすべて根を指すようになる
        # ex 3 -> 2 -> 4 -> 0(root)という木があった場合
        # parent = [-4,?,4,2,0] のような構造になっているが
        # find(3)を実行することで、3以上の階層でルートを指していないもの(3,2,4)はすべてルートを指すようになる
        # すなわち parent = [-4,?,0,0,0] となる
        # この考え方が「経路の圧縮」
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def same(self, x: int, y: int):
        """_summary_
        xとyが同じ集合に含まれているかを判別する
        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            _type_: _description_
        """
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        """_summary_
            xとyの属する集合を併合する
        Args:
            x (int): _description_
            y (int): _description_
        """
        # ルートが同じならすでに同じ集合に属しているため何もしない
        if self.same(x, y):
            return

        # ルートが同じではない場合
        # 「異なる集合に属している場合」として良い？
        # find()関数の操作により、同じ集合に属しているすべての要素は
        # 同じルートの値を指すようになる
        # (
        #     3->2->1->0(root)のときにx = 3,y = 2を入力としても
        #     x_root = 2, y_root = 1 みたいなことが起こらない
        # )

        # xが含まれている&要素数が多い集合に、yが含まれている&要素数が少ない集合を併合しようとしている
        # これは「union by size」といい、計算量を下げる効果がある(らしい)
        # なので、もしyの方が要素数が多かった場合にはxとyを入れ替えようとしている
        if self.size[x] < self.size[y]:
            x, y = y, x

        x_root = self.root(x)
        y_root = self.root(y)
        self.parents[y_root] = x_root
        self.size[x_root] += self.size[y_root]

    def get_size(self, x: int):
        """_summary_
            xが含まれている集合の要素数を取得する
        Args:
            x (int): _description_

        Returns:
            _type_: _description_
        """
        return self.size[self.root(x)]


def main():
    uf = UnionFindKentyon(n=6)
    print(uf.parents)
    uf.unite(0, 2)
    uf.unite(1, 3)
    print(uf.parents)
    print(uf.same(0,1))
    print(uf.same(0,2))
    print(uf.same(1,2))
    print(uf.same(1,3))

if __name__ == "__main__":
    main()
