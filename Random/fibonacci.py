import unittest

def fibonacci(order):
    a = 1
    b = 1

    for i in range(1, order):
        hold = b
        b = a + b
        a = hold

    return b

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.function = fibonacci

    def test_zero(self):
        self.assertEqual(self.function(0), 1)

    def test_two(self):
        self.assertEqual(self.function(1), 1)

    def test_two(self):
        self.assertEqual(self.function(2), 2)

    def test_five(self):
        self.assertEqual(self.function(8), 34)
