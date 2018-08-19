import unittest


class Solution(object):
    def number_at_pos(self, pos):
        return self.fib(pos)

    def fib(self, pos):
        if pos <= 1:
            return pos
        else:
            return self.fib(pos - 1) + self.fib(pos - 2)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        self.assertEqual(self.solution.number_at_pos(7), 13)

if __name__ == '__main__':
    unittest.main()
