# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0

import unittest
from typing import List


class TestInsertSolution(unittest.TestCase):
    def test_target_present(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)

    def test_target_absent(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)

    def test_target_absent_large(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)

    def test_target_absent_small(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 0), 0)

    def test_target_absent_largest(self):
        self.assertEqual(searchInsert([1, 3, 5, 6, 8, 10, 11, 13, 25], 56), 9)


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if target > nums[mid - 1]:
                return mid
            right = mid - 1
        else:
            if mid < len(nums) - 1 and target < nums[mid + 1]:
                return mid + 1
            left = mid + 1

    return 0 if target < nums[0] else len(nums)


if __name__ == '__main__':
    unittest.main()