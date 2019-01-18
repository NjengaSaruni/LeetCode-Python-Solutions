import unittest

if __name__ == '__main__':
    unittest.main()


class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(brackets('()'))

    def test_failure(self):
        self.assertFalse(brackets('())'))

    def test_longer(self):
        self.assertTrue(brackets('(())()'))


def brackets(s):
    left = 0
    for i in s:
        if i == '(':
            left += 1
        elif left == 0:
            return False
        else:
            left -= 1

    return left == 0
