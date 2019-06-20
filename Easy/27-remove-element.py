"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
"""

import unittest
from typing import List

if __name__ == '__main__':
    unittest.main()


def remove_element(value: int, array: List[int]) -> int:
    """
    Returns the length of the new array after the removal of
    :param value: The element to be remove
    :param array: An array of elements with the element to be removed.
    :return:
    """

    slow = -1
    fast = 0

    while fast < len(array):
        if array[fast] != value:
            slow += 1
            array[slow] = array[fast]
        fast += 1

    return slow + 1

class TestRemoveElement(unittest.TestCase):

    def test_short_array(self):
        self.assertEqual(remove_element(2, [2, 2, 3, 2, 3, 4, 2, 4, 4, 4]), 6)

    def test_empty_array(self):
        self.assertEqual(remove_element(2, []), 0)

    def test_to_empty_array(self):
        self.assertEqual(remove_element(2, [2, 2, 2]), 0)