import unittest


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not isinstance(nums, list):
            return

        complements = {}
        keys = {}
        for index, item in enumerate(nums):
            complement = target - item
            complements[item] = complement
            if keys.get(item) is None:
                keys[item] = [index]
            else:
                keys[item].append(index)

            if complements.get(complement) is not None:
                complement_key = keys.get(complement)
                item_key = keys.get(item)

                if complement_key != item_key:
                    return [complement_key[0], index]
                else:
                    if len(complement_key) > 1:
                        return [complement_key[0], complement_key[1]]
                    continue


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        ls = [1, 3, 4, 3, 9, 11]
        target = 5
        self.assertEqual(self.solution.twoSum(ls, target), [0, 2])

    def test_null(self):
        ls = None
        target = 5
        self.assertEqual(self.solution.twoSum(ls, target), None)

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

    def test_no_list(self):
        ls = []
        target = 20
        self.assertEqual(self.solution.twoSum(ls, target), None)

    def test_one_item_in_list(self):
        ls = [1]
        target = 1
        self.assertEqual(self.solution.twoSum(ls, target), None)


if __name__ == '__main__':
    unittest.main()
