def splitInteger(num, parts):
    # Construct a list of items from the integer division of `num` and `parts`
    items = [num // parts for _ in range(parts)]

    # Get the remainder
    remainder = (num % parts) + 1

    # If remainder, iterate through from the back and keep adding one to items
    # in the list
    for i in range(-1, -remainder, -1):
        items[i] += 1


    "".split()
    return items

import unittest

class Test(unittest.TestCase):
    def test_should_handle_evenly_distributed_cases(self):
        self.assertEqual(splitInteger(23, 4), [5, 6, 6, 6])
        self.assertEqual(splitInteger(20, 4), [5, 5, 5, 5])