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

    def test_non_reocurring(self):
        self.assertEqual(first_reoccuring('abcd'), None)

    def test_long_reocurring(self):
        self.assertEqual(first_reoccuring('abcdjsdjsd'), 'd')

    def test_long_non_reocurring(self):
        self.assertEqual(first_reoccuring('abcdefghijklmnopqrstuvwxyz'), None)


if __name__ == '__main__':
    unittest.main()
