import unittest


def staircase(height):
    if height == 1:
        return 1
    if height == 2:
        return 2
    return staircase(height - 1) + staircase(height - 2)


def staircase_dp(height):
    ls = [1 for i in range(height + 1)]

    for i in range(2, height + 1):
        ls[i] = ls[i - 1] + ls[i - 2]

    return ls[height]


class TestSolution(unittest.TestCase):
    def test_height_3(self):
        self.assertEqual(staircase_dp(3), 3)

    def test_height_5(self):
        self.assertEqual(staircase_dp(5), 8)

    def test_height_8(self):
        self.assertEqual(staircase_dp(8), 34)
