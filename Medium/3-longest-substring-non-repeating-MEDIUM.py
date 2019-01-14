import unittest

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


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
                if len(current) > len(longest):
                    longest = current
                continue

            current = current[current.find(i) + 1:] + i

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

    def test_two_chars(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('au'), 2)

    def test_non_repeating_after_first(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('aab'), 2)

    def test_non_repeating_after_trial(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('dvdf'), 3)


if __name__ == '__main__':
    unittest.main()
