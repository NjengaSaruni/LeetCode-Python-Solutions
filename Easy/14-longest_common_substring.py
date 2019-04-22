# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

import unittest

from typing import List


def longest_prefix(strs: List[str]) -> str:
    if not strs:
        return ''

    longest = 0
    string_a = strs[0]

    for i in range(len(string_a)):
        try:
            if all([item[i] == string_a[i] for item in strs]):
                longest += 1
                continue
        except IndexError:
            break
        break

    return string_a[:longest]


class TestLongestPrefix(unittest.TestCase):

    def test_prefix_fl(self):
        strings = ['flower', 'flow', 'flight']

        self.assertEqual(longest_prefix(strs=strings), 'fl')

    def test_prefix_aa(self):
        strings = ['aa', 'a']

        self.assertEqual(longest_prefix(strs=strings), 'a')


    def test_no_prefix(self):
        strings = ['dog', 'racecar', 'car']

        self.assertEqual(longest_prefix(strs=strings), '')

    def test_prefix_pre(self):
        strings = ['premedial', 'pre-historic', 'press']

        self.assertEqual(longest_prefix(strs=strings), 'pre')

if __name__ == '__main__':
    unittest.main()