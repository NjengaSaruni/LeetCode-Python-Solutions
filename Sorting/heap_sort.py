import unittest
from heapq import heappop, heappush

def build_max_hip(ls):

    return ls
def heap_sort(ls):
    print(ls)

def heapsort_inbuilt(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

class TestHeapSort(unittest.TestCase):
    def setUp(self):
        self.fn = heapsort_inbuilt

    def test_simple_array(self):
        self.assertEqual(self.fn([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()