import unittest

if __name__ == '__main__':
    unittest.main()


def is_pal_number(n):
    number = 0
    origin = n

    while n > 0:
        number = number * 10 + n % 10
        n //= 10

    return origin == number


class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_pal_number(12421))

    def test_simple_false(self):
        self.assertFalse(is_pal_number(1222))
