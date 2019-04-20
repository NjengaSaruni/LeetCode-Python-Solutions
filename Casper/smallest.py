import unittest


def solution(M, A):
    N = len(A)
    count = [0] * M
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp >= maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]

if __name__ == '__main__':
    unittest.main()


class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(solution(6, [1, 3, 3, 4, 1, 2]), 1)

    def test_positives(self):
        self.assertEqual(solution(1, [1, 2, 3]), 4)

    def test_negatives(self):
        self.assertEqual(solution(1, [-1,  -3]), 1)
