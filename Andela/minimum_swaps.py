import unittest

class Test(unittest.TestCase):
  def test_minimum_swaps_should_handle_single_swap(self):
    self.assertEqual(minimum_swaps([3,1,2]), 1)
  def test_minimum_swaps_should_handle_multiple_swaps(self):
    self.assertEqual(minimum_swaps([3,1,2,4]), 2)


def minimum_swaps(ratings):
    index = 0
    size = len(ratings)
    swaps = 0

    # Brute force solution
    while index < size:
        to_swap = index
        for i in range(index, size):
            if ratings[i] > ratings[index]:
                to_swap = i

        if to_swap != index:
            ratings[i], ratings[index] = ratings[index], ratings[i]
            swaps += 1

        index += 1

    return swaps