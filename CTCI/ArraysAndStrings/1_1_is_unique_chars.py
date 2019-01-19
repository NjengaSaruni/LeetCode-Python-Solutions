import unittest
from typing import List


def all_unique(s):
    value: List[bool] = [False for _ in range(256)]

    for i in s:
        if value[ord(i)]:
            return False
        value[ord(i)] = True

    return True


if __name__ == '__main__':
    unittest.main()


class TestSolution(unittest.TestCase):
    def test_all_unique(self):
        self.assertTrue(all_unique('abcd'))

    def test_duplicated(self):
        self.assertFalse(all_unique('abcda'))
