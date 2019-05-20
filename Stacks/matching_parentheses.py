import unittest


if __name__ == '__main__':
    unittest.main()


def is_matched(value: str) -> bool:
    if len(value) % 2 == 1:
        return False

    stack = []
    for char in value:
        if char == '(':
            stack.append('(')
        elif char == '{':
            stack.append('{')
        elif char == '[':
            stack.append('[')
        elif char in [')', '}', ']'] and len(stack) > 0:
            if char == ')' and stack.pop() != '(':
                return False
            if char == '}' and stack.pop() != '{':
                return False
            if char == ']' and stack.pop() != '[':
                return False
        else:
            return False

    return len(stack) == 0

class TestMatchingParenteses(unittest.TestCase):

    def test_brackets(self):
        self.assertTrue(is_matched('{()}'))