import unittest
from .quick_union import QuickUnion


class TestQuickUnion(unittest.TestCase):
    def setUp(self):
        self.quick_union = QuickUnion(list(range(0, 10)))

    def perform_union(self):
        self.quick_union.union(5, 0)
        self.quick_union.union(5, 6)
        self.quick_union.union(2, 7)
        self.quick_union.union(2, 1)
        self.quick_union.union(3, 8)
        self.quick_union.union(4, 9)
        self.quick_union.union(3, 4)

    def test_connected(self):
        self.perform_union()
        print(self.quick_union.data)
        assert (self.quick_union.connected(3, 9))
        assert (not self.quick_union.connected(5, 4))
        assert (self.quick_union.connected(8, 9))
