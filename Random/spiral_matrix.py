import unittest


def spiral(order):
    mid = order // 2
    matrix = [[0 for i in range(order)] for j in range(order)]

    value = 1
    right = mid + 1
    top = mid - 1
    left = mid - 1
    bottom = mid + 1

    col = mid
    row = mid

    matrix[row][col] = value

    while right <= order - 1:
        while col < right:
            col += 1
            value += 1
            matrix[row][col] = value

        while row > top:
            row -= 1
            value += 1
            matrix[row][col] = value

        while col > left:
            col -= 1
            value += 1
            matrix[row][col] = value

        while row < bottom:
            row += 1
            value += 1
            matrix[row][col] = value

        while col < right:
            col += 1
            value += 1
            matrix[row][col] = value

        right += 1
        left -= 1
        bottom += 1
        top -= 1

    return matrix


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.function = spiral

    def test_one(self):
        self.assertEqual(
            self.function(1),
            [
                [1]
            ]
        )

    def test_three(self):
        self.assertEqual(
            self.function(3),
            [
                [5, 4, 3],
                [6, 1, 2],
                [7, 8, 9]
            ]
        )

    def test_five(self):
        self.assertEqual(
            self.function(5),
            [
                [17, 16, 15, 14, 13],
                [18, 5, 4, 3, 12],
                [19, 6, 1, 2, 11],
                [20, 7, 8, 9, 10],
                [21, 22, 23, 24, 25]
            ]
        )


if __name__ == '__main__':
    unittest.main()
