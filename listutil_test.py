import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([], unique([]))
    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
    def test_same_item_many_times(self):
        self.assertEqual([7], unique([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
    def test_multi_item_list(self):
        self.assertEqual([[2], [1], [3]], unique([[2], [1], [2], [3], [1]]))
    def test_string_integer_list(self):
        self.assertEqual([0, '3', '0', 3], unique([0, "3", "0", 3]))
    def test_list_of_empty_list(self):
        self.assertEqual([[]], unique([[]]))
    def test_list_of_same_integer_list(self):
        self.assertEqual([[1, 2, 3], [3, 2, 1]], unique([[1, 2, 3],[3, 2, 1]]))
    def test_large_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))



if __name__ == '__main__':
    unittest.main()