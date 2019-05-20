import unittest


if __name__ == '__main__':
    unittest.main()


def is_matched(value: str) -> bool:
    stack = []
    lefty = '({['
    righty = ')}]'

    for char in value:
        if char in lefty:
            stack.append(char)
        elif char in righty and len(stack) > 0:
            if stack.pop() != lefty[righty.index(char)]:
                return False

    return len(stack) == 0


class TestMatchingParentheses(unittest.TestCase):

    def test_brackets_squares(self):
        self.assertTrue(is_matched('([{}])'))

    def test_brackets_squares_unmatched(self):
        self.assertFalse(is_matched('{()]'))

    def test_mathematical(self):
        self.assertTrue(is_matched('[(5+x)-(y+z)]'))
