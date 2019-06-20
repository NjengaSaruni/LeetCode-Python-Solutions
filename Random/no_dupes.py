import unittest

if __name__ == '__main__':
    unittest.main()


def spiral(order):
    bound = order // 2

    matrix = [[0] * order for _ in range(order)]

    value = 1
    matrix[bound][bound] = value
    row = bound
    col = bound

    while bound > 0:
        value += 1
        matrix[row][col] = value


