import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        complements = {}
        keys = {}
        for index, item in enumerate(nums):
            complements[item] = target - item
            keys[item] = index

        for item, complement in complements.items():
            if(complements.get(complement)) is not None:
                return [keys.get(item), keys.get(complement)]

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        ls = [1, 3, 2, 4, 3, 9, 11]
        target = 5
        self.assertEqual(self.solution.twoSum(ls, target), [0, 3])

    def test_no_solution(self):
        ls = [1, 3, 2, 4, 3, 9]
        target = 20
        self.assertEqual(self.solution.twoSum(ls, target), None)


if __name__ == '__main__':
    unittest.main()
