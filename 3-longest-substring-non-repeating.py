import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = s[0]
        current = ''
        for i in s:
            if i not in current:
                current += i
                continue

            if len(current) > len(longest):
                longest = current

            current = i

        return len(longest)

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_repeating_chars(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbbbbb'), 1)

    def test_single_char(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('b'), 1)

    def test_longest_in_middle(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('pwwkew'), 3)

if __name__ == '__main__':
    unittest.main()