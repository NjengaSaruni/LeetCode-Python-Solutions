import unittest

def first_reoccuring(s):
    _set = set()
    for i in s:
        if i in _set:
            return i
        _set.add(i)

    return None


class TestSolution(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(first_reoccuring('abca'), 'a')

    def test_non_recurring(self):
        self.assertEqual(first_reoccuring('abcd'), None)

    def test_long_recurring(self):
        self.assertEqual(first_reoccuring('abcdjsdjsd'), 'd')


if __name__ == '__main__':
    unittest.main()
