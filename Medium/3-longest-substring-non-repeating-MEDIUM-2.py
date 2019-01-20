# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
import unittest


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = ''

    i = 0
    length = len(s)

    while i < length:
        current = ''
        j = i

        while j < length:
            if s[j] not in current:
                current += s[j]
            else:
                break
            if len(current) > len(longest):
                longest = current

            j += 1
        i += 1
    print('\a')
    return len(longest)

def longest_window(str):
    _set = set()
    longest = 0
    left = 0
    right = 0

    while right < len(str):
        if str[right] in _set:
            longest = longest if longest > right - left else right - left
            reset = set(str[left])
            while str[left] != str[right]:
                left += 1
                reset.add(str[left])

            left += 1
            _set -= reset
        else:
            _set.add(str[right])
            right += 1

    return longest if longest > right - left else right - left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.function = longest_window

    def test_simple(self):
        self.assertEqual(self.function('abc'), 3)

    def test_empty_string(self):
        self.assertEqual(self.function(''), 0)

    def test_duplicates(self):
        self.assertEqual(self.function('aaadasdasdasdasdassaapoiy'), 5)


if __name__ == '__main__':
    unittest.main()


