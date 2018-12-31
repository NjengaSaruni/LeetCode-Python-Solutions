import unittest

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def getLocationOfMedian(self, number, sortedArray):
        sortedArrayLength = len(sortedArray)
        halfSortedArrayLength = sortedArrayLength // 2

        numberOfItemsLeft = halfSortedArrayLength
        numberOfItemsRight = halfSortedArrayLength - 1

        pivot = sortedArray[halfSortedArrayLength]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenOfNums1 = len(nums1)
        lenOfNums2 = len(nums2)


        if lenOfNums1 % 2 == 0:
            median1 = (nums1[lenOfNums1 // 2] + nums1[lenOfNums1 // 2 - 1]) / 2
        else:
            median1 = nums1[lenOfNums1 // 2]

        if lenOfNums2 % 2 == 0:
            median2 = (nums2[lenOfNums2 // 2] + nums2[lenOfNums2 // 2 - 1]) / 2
        else:
            median2 = nums2[lenOfNums2 // 2]

        self.getLocationOfMedian(median1, nums2)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1], [1]), 1)


if __name__ == '__main__':
    solution = Solution()

    arr1 = [1, 7, 12, 12]
    arr2 = [2, 5, 5, 8, 9]

    solution.findMedianSortedArrays(arr1, arr2)
