import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def extend(self, x):
        current = self
        previous = None
        while current is not None:
            previous = current
            current = current.next

        if isinstance(x, list):
            for i in x:
                previous.next = ListNode(i)
                previous = previous.next
        else:
            previous.next = ListNode(x)

    def __repr__(self):
        repr = ''
        current = self
        while current is not None:
            if current.next is not None:
                repr += '{} -> '.format(current.val)
                current = current.next
            else:
                return repr + str(current.val)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode"""

        pass


# class TestSolution(unittest.TestCase):
#     solution = Solution()
#
#     def test_simple(self):
#         pass


if __name__ == '__main__':
    # unittest.main()
    ln = ListNode(2)
    ln.extend(3)
    ln.extend([1,3,7])

    print(ln)
