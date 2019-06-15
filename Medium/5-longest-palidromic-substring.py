"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
from typing import Tuple


class Solution(object):
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring occurring in the string provided
        :type s: str
        :rtype: str
        """

        longest = ''

        palindromes = set()

        for i in range(len(s)):
            for j in range(len(s) - 1, i -1, -1):
                if j - i >= len(longest):
                    is_palindrome = self.isPalindrome(s, i, j, palindromes)
                    if is_palindrome:
                        palindromes.add((i, j))
                        if len(s[i:j+1]) > len(longest):
                            longest = s[i:j+1]
        return longest

    def isPalindrome(self, s, left, right, palindromes):
        """
        :param s:
        :param left:
        :param right:
        :param palindromes:
        :return:
        """
        if (left, right) in palindromes or left >= right:
            return True

        if s[left] == s[right]:
            return self.isPalindrome(s, left + 1, right - 1, palindromes)

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('abadaba'))
