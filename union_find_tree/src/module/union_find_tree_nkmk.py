from collections import defaultdict


class UnionFindNkmk:
    """_summary_
    nkmkの実装によるUF木
    https://note.nkmk.me/python-union-find/
    """

    def __init__(self, n: int):
        self.n = n
        self.parents: list[int] = [-1] * n

    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x: int, y: int):
        """_summary_
            xとyの属する集合を併合する
        Args:
            x (int): _description_
            y (int): _description_
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        return self.find[x] == self.find[y]

    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
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
