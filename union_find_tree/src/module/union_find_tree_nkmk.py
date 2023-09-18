from collections import defaultdict


class UnionFindNkmk:
    """_summary_
    nkmkの実装によるUF木
    https://note.nkmk.me/python-union-find/
    """

    def __init__(self, n: int):
        self.n = n
        # 各要素の親要素のインデックスを格納する
        # 自分がグループの根なら、-(グループの要素数) を持つ
        # 初期値は全要素がグループの根なのですべて -1(自分しか要素がない)
        self.parents: list[int] = [-1] * n

    def find(self, x: int):
        """_summary_
            要素xが属するグループの根の要素を返す
        Args:
            x (int): _description_

        Returns:
            _type_: _description_
        """
        # parents[x] < 0 つまり「自分自身が、何かのグループの根」の場合は自分自身を返す
        if self.parents[x] < 0:
            return x

        # それ以外 つまり「自分が何かのグループに(根ではなく)属している」場合は自分の親要素を返す(端的に言えば)
        # 実際は、再帰的にparentの値を更新しているので、そのグループ内の要素はすべて根を指すようになる
        # ex 3 -> 2 -> 4 -> 0(root)という木があった場合
        # parent = [-4,?,4,2,0] のような構造になっているが
        # find(3)を実行することで、3以上の階層でルートを指していないもの(3,2,4)はすべてルートを指すようになる
        # すなわち parent = [-4,?,0,0,0] となる
        # この考え方が「経路の圧縮」
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

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
        if self.size(x) < self.size(y):
            x, y = y, x

        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root

    def size(self, x: int):
        """_summary_
            xが含まれている集合の要素数を取得する
        Args:
            x (int): _description_

        Returns:
            _type_: _description_
        """
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        """_summary_
        xとyが同じ集合に含まれているかを判別する
        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            _type_: _description_
        """
        return self.find(x) == self.find(y)

    def members(self, x: int):
        """_summary_
        xと同じ集合に属する要素の一覧を取得する
        Args:
            x (int): _description_

        Returns:
            _type_: _description_
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """_summary_
        根の要素の一覧を取得する
        Returns:
            _type_: _description_
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """_summary_
        根の一覧の数 = 集合の数を取得する
        Returns:
            _type_: _description_
        """
        return len(self.roots())

    def all_group_members(self):
        """_summary_
        すべての集合のすべての要素を取得する
        Returns:
            _type_: _description_
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def main():
    uf = UnionFindNkmk(n=6)
    # uf.init()
    print(uf.parents)
    uf.unite(0, 2)
    print(uf)
    uf.unite(1, 3)
    print(uf.parents)
    uf.unite(4, 5)
    print(uf.parents)
    uf.unite(1, 4)
    print(uf.parents)
    print(uf)


if __name__ == "__main__":
    main()
