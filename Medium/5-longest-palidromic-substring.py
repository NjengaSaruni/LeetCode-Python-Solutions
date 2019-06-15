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

        mid = len(s) // 2
        left_even = mid - 1
        right_even = mid
        best = (mid, mid)

        left_odd, right_odd = self.longestPalindromeMiddleOutOdd(s, mid)
        if left_even >= 0 and s[left_even] == s[right_even]:
            left_even, right_even = self.longestPalindromeMiddleOutEven(s, mid)

        if right_even - left_even > right_odd - left_odd:
            best = (left_even, right_even)
        else:
            best = (left_odd, right_odd)

        return s[best[0]: best[1] + 1]

    def max(self, best1: Tuple[int], best2: Tuple[int]):
        if best1[1] - best1[0] > best2[1] - best2[0]:
            return best1
        return best2


    def isPalindrome(self, s: str, left: int, right: int):
        """
        :param s:
        :param left:
        :param right:
        :return:
        """
        if left >= right:
            return True

        if s[left] == s[right]:
            return self.isPalindrome(s, left + 1, right - 1)

        return False

    def longestPalindromeMiddleOutEven(self, s: str, mid: int):
        left = mid - 1
        right = mid

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindromeMiddleOutOdd(self, s: str, mid: int):
        left = mid
        right = mid

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('bcabaaababc'))
