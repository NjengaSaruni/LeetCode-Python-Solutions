# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

import unittest

if __name__ == '__main__':
    unittest.main()

class Solution(object):
    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ''
        carry = 0
        for i in range(len(num1) - 1, - 1, -1):
            for j in range(len(num2) - 1, -1, -1):
                carry, value = divmod(int(num1[i]) * int(num2[j]) + carry, 10)
                ans = str(value) + ans
                print(carry)

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.fn = Solution.multiply

    def test_twelve_times_twelve(self):
        self.assertEqual(self.fn('12', '12'), '144')
