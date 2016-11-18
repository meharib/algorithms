import unittest
from .weighted_quick_union import WeightedQuickUnion


class TestQuickUnion(unittest.TestCase):
    def setUp(self):
        self.weighted_quick_union = WeightedQuickUnion(list(range(0, 10)))

    def perform_union(self):
        self.weighted_quick_union.union(4, 3)
        self.weighted_quick_union.union(3, 8)
        self.weighted_quick_union.union(6, 5)
        self.weighted_quick_union.union(9, 4)
        self.weighted_quick_union.union(2, 1)
        self.weighted_quick_union.union(5, 0)
        self.weighted_quick_union.union(7, 2)
        self.weighted_quick_union.union(6, 1)
        self.weighted_quick_union.union(7, 3)

    def test_connected(self):
        self.perform_union()
        self.assertEqual(10, self.weighted_quick_union.size[6]);
        self.assertEqual(4, self.weighted_quick_union.size[4]);
        self.assertEqual(3, self.weighted_quick_union.size[2]);

