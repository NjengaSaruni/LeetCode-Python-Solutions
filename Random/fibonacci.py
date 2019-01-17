import unittest
import timeit
import functools

def fibonacci(order):
    a = 1
    b = 1

    for i in range(1, order):
        hold = b
        b = a + b
        a = hold

    return b


def fibonacciRecursive(order):
    if order <= 1:
        return 1
    return fibonacci(order - 1) + fibonacci(order - 2)

def _getFibonacci(memo, order):
    if memo.__contains__(order):
        return memo[order]
    value = _getFibonacci(memo, order - 1) + _getFibonacci(memo, order - 2)
    memo[order] = value
    return value

def fibonacciRecursiveMemoized(order):
    d = {
        0: 1,
        1: 1
    }
    return _getFibonacci(d, order)

# class TestSolution(unittest.TestCase):
#     def setUp(self):
#         self.function = fibonacciRecursiveMemoized
#
#     def test_zero(self):
#         self.assertEqual(self.function(0), 1)
#
#     def test_two(self):
#         self.assertEqual(self.function(1), 1)
#
#     def test_five(self):
#         self.assertEqual(self.function(8), 34)


if __name__ == '__main__':
    # iterative = timeit.Timer(functools.partial(fibonacci, 121))
    recursive = timeit.Timer(functools.partial(fibonacciRecursive, 121))
    amoized = timeit.Timer(functools.partial(fibonacciRecursiveMemoized, 121))

    # print('Iterative: ', iterative.timeit())
    print('Recursive: ', recursive.timeit())
    print('Amoized: ', amoized.timeit())
