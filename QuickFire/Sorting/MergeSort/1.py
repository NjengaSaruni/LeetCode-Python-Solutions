"""
Author: Peter Njenga (https://github.com/NjengaSaruni)
"""

import unittest
from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """
    Use the divide and conquer approach to sort a list of integers
    :param array: The array to be sorted
    :return: A sorted version of the array of integers provided
    """
    length = len(array)

    # Base case, an array of zero or 1 elements is already sorted
    if length <= 1:
        return array

    # Partition the array into two sub arrays, via the middle and merge_sort them recursively
    mid = length // 2
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:length])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays by creating a larger version of the two
    :param left: The left subarray
    :param right: The right subarray
    :return: A merged version of right and left, with the elements in sorted order
    """
    MAX_LEFT = len(left)
    MAX_RIGHT = len(right)

    left_pointer = 0
    right_pointer = 0

    merged = []

    while left_pointer < MAX_LEFT and right_pointer < MAX_RIGHT:

        # Append the lesser element and move on
        if left[left_pointer] <= right[right_pointer]:
            merged.append(left[left_pointer])
            left_pointer += 1

        else:
            merged.append(right[right_pointer])
            right_pointer += 1

    if left_pointer < MAX_LEFT:
        merged.extend(left[left_pointer:MAX_RIGHT])

    if right_pointer < MAX_RIGHT:
        merged.extend(right[right_pointer:MAX_RIGHT])

    return merged

class TestMergeSort(unittest.TestCase):

    def test_short_array_or_unsorted_integers(self):
        array = [1, 3, 2, 4, 8, 5, 6]

        self.assertEqual(merge_sort(array), [1, 2, 3, 4, 5, 6, 8])
