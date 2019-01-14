# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while right > left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1

        return True

    def usingSlicing(self, s):
        longest = ''
        left = 0
        right = len(s)

        while left < right:
            i = right
            while i > left:
                if len(longest) >= i - left:
                    break
                sub = s[left:i]
                if self.isPalindrome(sub) and len(sub) > len(longest):
                    longest = sub
                i -= 1
            left += 1

        return longest


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        return self.usingSlicing(s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('arabricririrc'))
