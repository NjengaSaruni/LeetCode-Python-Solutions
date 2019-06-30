import unittest

from typing import List

if __name__ == '__main__':
    unittest.main()


def insertion_sort(array: List[int]):
    for i in range(len(array) - 1):
        j = i + 1
        index = i

        while j < len(array):
            if array[j] < array[index]:
                index = j
            j += 1

        array[i], array[index] = array[index], array[i]


class TestInsertionSort(unittest.TestCase):

    def test_short_array_or_unsorted_integers(self):
        array = [1, 3, 2, 4, 8, 5, 6]
        insertion_sort(array)

        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 8])
