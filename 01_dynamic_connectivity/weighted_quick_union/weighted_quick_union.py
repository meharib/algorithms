class WeightedQuickUnion():
    def __init__(self, data):
        self.data=data
        self.size=[1]*10

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if self.size[p_root] < self.size[q_root]:
            self.data[p_root] = self.data[q_root]
            self.size[q_root] += self.size[p_root]
        else:
            self.data[q_root] = self.data[p_root]
            self.size[p_root] += self.size[q_root]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, i):
        v = self.data[i];
        return i if v == i else self.root(self.data[v])
