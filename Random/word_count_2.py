import unittest


def count(s):
    count = 0
    last_character = ' '

    for i in s:
        if i == ' ' and not last_character == ' ':
            count += 1
        last_character = i

    if last_character != ' ':
        count += 1

    return count


class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count(' There was a man '), 4)



if __name__ == '__main__':
    unittest.main()