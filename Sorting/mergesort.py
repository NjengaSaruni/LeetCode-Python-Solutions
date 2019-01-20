import unittest


def mergeSort(ls):
    if len(ls) <= 1:
        return ls

    ans = []

    mid = len(ls) // 2
    left = mergeSort(ls[:mid])
    right = mergeSort(ls[mid:])

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    while i < len(left):
        ans.append(left[i])
        i += 1

    while j < len(right):
        ans.append(right[j])
        j += 1

    return ans


class TestMergeSort(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mergeSort([1, 5, 2, 3, 4, 8, 1]), [1, 1, 2, 3, 4, 5, 8])


if __name__ == '__main__':
    unittest.main()
