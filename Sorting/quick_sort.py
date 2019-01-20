import unittest


def quick_sort(ls, left=0, right=None):
    if right is None:
        right = len(ls) - 1

    pivot = ls[right]
    i = left
    lock = left

    while i < right:
        if ls[i] <= pivot:
            ls[i], ls[lock] = ls[lock], ls[i]
            lock += 1

        i += 1

    if left < right:
        ls[lock], ls[right] = ls[right], ls[lock]
        quick_sort(ls, left, lock - 1)
        quick_sort(ls, lock + 1, right)

    return ls


class TestQuickSort(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(quick_sort([2, 3, 5, 1, 4, 9, 8, 1]), [1, 1, 2, 3, 4, 5, 8, 9])


if __name__ == '__main__':
    unittest.main()
