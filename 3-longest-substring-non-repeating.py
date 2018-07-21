import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = ''
        current = ''
        for i in s:
            if i not in current:
                current += i
                continue

            if len(current) > len(longest):
                longest = current

            current = i

        return longest

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 'abc')

    def test_single_char(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbbbbb'), 'b')

    def test_longest_in_middle(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('pwwkew'), 'wke')

if __name__ == '__main__':
    unittest.main()