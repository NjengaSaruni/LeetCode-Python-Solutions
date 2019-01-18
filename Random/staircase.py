import unittest

def staircase(height):
    if height == 1:
        return 1
    if height == 2:
        return 2
    return staircase(height - 1) + staircase(height - 2)


class TestSolution(unittest.TestCase):
    def test_height_three(self):
        self.assertEqual(staircase(3), 3)

    def test_height_five(self):
        self.assertEqual(staircase(5), 8)
