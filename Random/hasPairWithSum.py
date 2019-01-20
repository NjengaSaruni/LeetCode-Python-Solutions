import unittest

if __name__ == '__main__':
    unittest.main()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.fn = Solution.has_pair_with_sum

    def test_short_list_true(self):
        self.assertTrue(self.fn([1, 2, 4, 4], 8))

    def test_short_list_false(self):
        self.assertFalse(self.fn([1, 2, 4, 4], 9))

    def test_long_list_true(self):
        self.assertTrue(self.fn([1, 2, 2, 4, 6, 7, 8, 8, 20, 23, 56, 565], 16))


class Solution:
    @staticmethod
    def has_pair_with_sum(ls, sm):
        low = 0
        high = len(ls) - 1

        while low < high:
            if ls[low] + ls[high] == sm:
                return True
            if ls[high] > sm - ls[low]:
                high -= 1
            else:
                low += 1

        return False
