# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#                     [1, 0, -1, -2, 1, 4]
#  []
# [
#  [-1, 1],
# ]
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# [
# ]
#
#
#
#
#

import unittest

def threeSum(nums):
    complements = {}

    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i != j:
                if complements.get(a + b):
                    complements[a + b] = complements[a + b].extend([i, j])
                else:
                    complements[a + b] = [i, j]

    print(complements)

    for i in nums:
        if 0 - i in complements:
            print(i)


class TestThreeSum(unittest.TestCase):
    def setUp(self) -> None:
        self.fn = threeSum

    def test_small_list(self):
        array = [-1, 0, 1, 2, -1, -4, 7]
        self.assertEqual(
            self.fn(array),
            [
              [-1, 0, 1],
              [-1, -1, 2]
            ]
        )


if __name__ == '__main__':
    unittest.main()