class QuickFind():
    def __init__(self, data):
        self.data = data
        print (self.data)

    def connected(self, p, q):
        return self.data[p] == self.data[q]

    def update(self, x, v, q):
        return q if x == v else x

    def union_(self, p, q):
        if not self.connected(p, q):
            self.data = [self.update(x, self.data[p], self.data[q]) for x in self.data]


qf = QuickFind(range(0, 10))

