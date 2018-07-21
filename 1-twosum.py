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
            if keys.get(item) is None:
                keys[item] = [index]
            else:
                keys[item].append(index)

        for item, complement in complements.items():
            if (complements.get(complement)) is not None:
                if(keys.get(item) != keys.get(complement)):
                    return [keys.get(item)[0], keys.get(complement)[0]]
                else:
                    return [keys.get(item)[0], keys.get(item)[1]]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        ls = [1, 3, 2, 4, 3, 9, 11]
        target = 5
        self.assertEqual(self.solution.twoSum(ls, target), [0, 3])

    def test_repeating(self):
        ls = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(ls, target), [0, 1])

    def test_three_repeating(self):
        ls = [3, 3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(ls, target), [0, 1])

    def test_no_solution(self):
        ls = [1, 3, 2, 4, 3, 9]
        target = 20
        self.assertEqual(self.solution.twoSum(ls, target), None)


if __name__ == '__main__':
    unittest.main()
