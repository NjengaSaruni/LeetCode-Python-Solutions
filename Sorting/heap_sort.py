import unittest
from heapq import heappop, heappush, heapify


def build_max_hip(ls):
    return ls


def heap_sort(ls):
    print(ls)

def sorted(ls):
    for i in heapify(ls):
        yield i

def heapsort_inbuilt(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


class TestHeapSort(unittest.TestCase):
    def setUp(self):
        self.fn = sorted

    def test_simple_array(self):
        ans = [i for i in self.fn([1, 4, 5, 3, 2])]
        self.assertEqual(ans, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
