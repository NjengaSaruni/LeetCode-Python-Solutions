# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

import unittest


class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        leftA = len(a) - 1
        leftB = len(b) - 1
        ans = ''
        carry = 0
        while leftA >= 0 and leftB >= 0:
            if a[leftA] == '0' and b[leftB] == '0':
                carry += 0
            elif a[leftA] == '1' and b[leftB] == '1':
                carry += 2
            else:
                carry += 1

            if carry == 0:
                ans = '0' + ans
            if carry == 1:
                ans = '1' + ans
                carry = 0
            if carry == 2:
                ans = '0' + ans
                carry = 1
            if carry == 3:
                ans = '1' + ans
                carry = 1

            leftA -= 1
            leftB -= 1

        while leftA >= 0:
            if a[leftA] == '1':
                carry += 1

            if carry == 0:
                ans = '0' + ans
            if carry == 1:
                ans = '1' + ans
                carry = 0
            if carry == 2:
                ans = '0' + ans
                carry = 1

            leftA -= 1

        while leftB >= 0:
            if b[leftB] == '1':
                carry += 1

            if carry == 0:
                ans = '0' + ans
            if carry == 1:
                ans = '1' + ans
                carry = 0
            if carry == 2:
                ans = '0' + ans
                carry = 1

            leftB -= 1

        if carry == 1:
            ans = '1' + ans

        return ans

if __name__ == '__main__':
    unittest.main()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_add_four_and_four(self):
        self.assertEqual(self.solution.addBinary2('100', '100'), '1000')

    def test_add_four_and_fifteen(self):
        self.assertEqual(self.solution.addBinary2('100', '1111'), '10011')
