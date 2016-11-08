class QuickUnion():
    def __init__(self, data):
        self.data=data

    def union(self, p, q):
        self.data[self.root(p)] = self.data[self.root(q)]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, i):
        v = self.data[i];
        return i if v == i else self.root(self.data[v])
