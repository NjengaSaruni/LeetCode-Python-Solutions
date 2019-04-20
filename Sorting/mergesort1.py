import unittest

from typing import List

def combine(list_a: List[int], list_b: List[int]) -> List[int]:
    combined = []
    while list_a and list_b:
        if list_a[0] < list_b[0]:
            combined.append(list_a[0])
            del list_a[0]
        else:
            combined.append(list_b[0])
            del list_b[0]

    combined.extend(list_a)
    combined.extend(list_b)

    return combined

def mergesort(nums: List[int]) -> List[int]:
    return _mergeSort(nums)

def _mergeSort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    list_a = _mergeSort(nums[0: len(nums) // 2])
    list_b = _mergeSort(nums[len(nums) // 2: len(nums)])

    return combine(list_a, list_b)

class TestMergeSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(mergesort([1, 3, 0, 2, 1, 1]), [0, 1, 1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()