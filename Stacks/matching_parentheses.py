import unittest


if __name__ == '__main__':
    unittest.main()


def is_matched(value: str) -> bool:
    if len(value) % 2 == 1:
        return False

    stack = []
    lefty = '({['
    righty = ')}]'

    for char in value:
        if char in lefty:
            stack.append(char)
        elif char in righty and len(stack) > 0:
            if stack.pop() != lefty[righty.index(char)]:
                return False
        else:
            return False

    return len(stack) == 0


class TestMatchingParenteses(unittest.TestCase):

    def test_brackets_squares(self):
        self.assertTrue(is_matched('([{}])'))

    def test_brackets_squares_unmatched(self):
        self.assertFalse(is_matched('{()]'))
