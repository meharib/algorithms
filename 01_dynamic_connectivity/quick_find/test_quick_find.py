import unittest
from .quick_find import QuickFind


class TestQuickFind(unittest.TestCase):
    def setUp(self):
        self.quick_find = QuickFind(range(0, 10))

    def perform_union(self):
        self.quick_find.union_(5, 0)
        self.quick_find.union_(5, 6)
        self.quick_find.union_(2, 7)
        self.quick_find.union_(2, 1)
        self.quick_find.union_(3, 8)
        self.quick_find.union_(4, 9)
        self.quick_find.union_(3, 4)

    def test_connected(self):
        self.perform_union()
        assert (self.quick_find.connected(3, 9))
        assert (not self.quick_find.connected(5, 4))
        assert (self.quick_find.connected(8, 9))
