import unittest


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
                if keys.get(complement) != keys.get(item):
                    return [keys.get(complement)[0], index]
                else:
                    if len(keys.get(complement)) > 1:
                        return [keys.get(complement)[0], keys.get(complement)[1]]
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
