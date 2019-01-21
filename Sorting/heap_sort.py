import unittest

def build_max_hip(ls):

    return ls
def heap_sort(ls):
    print(ls)

class TestHeapSort(unittest.TestCase):
    def test_simple_array(self):
        self.assertEqual(heap_sort([1, 4, 5, 3, 2]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()