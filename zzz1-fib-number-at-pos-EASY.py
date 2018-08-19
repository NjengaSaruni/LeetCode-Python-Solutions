import unittest


class Solution(object):
    def number_at_pos(self, pos):
        return self.fib(pos)

    def number_at_pos_iter(self, pos):
        prev1 = 0
        prev2 = 1

        i = 0

        if pos <= 1:
            return pos

        sm = 0

        while i < pos:
            prev1 = prev2
            prev2 = sm
            sm = prev1 + prev2
            i += 1

        return sm

    def fib(self, pos):
        if pos <= 1:
            return pos
        else:
            return self.fib(pos - 1) + self.fib(pos - 2)




class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        self.assertEqual(self.solution.number_at_pos(7), 13)

    def test_simple_iter(self):
        self.assertEqual(self.solution.number_at_pos_iter(7), 13)

    def test_at_2_iter(self):
        self.assertEqual(self.solution.number_at_pos_iter(2), 1)


if __name__ == '__main__':
    unittest.main()
