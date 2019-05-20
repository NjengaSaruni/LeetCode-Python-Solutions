import unittest

from typing import List

# [1, 8, 2, 4, 3]

if __name__ == '__main__':
    unittest.main()


def insertion_sort(array: List[int]) -> None:
    for i in range(len(array) - 1):
        j = i + 1
        while j >= 1 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


class TestInsertionSort(unittest.TestCase):

    def test_five_elements(self):
        array = [1, 8, 2, 4, 3]
        insertion_sort(array)
        self.assertEqual(array, [1, 2, 3, 4, 8])

    def test_empty(self):
        array = []
        insertion_sort(array)
        self.assertEqual(array, [])

    def test_many_elements(self):
        array = [9, 1, 4, 2, 6, 8, 3, 5, 7]
        insertion_sort(array)

        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9])
