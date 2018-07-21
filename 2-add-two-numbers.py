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
    ln1 = ListNode(2)
    ln1.extend([1, 3, 7, 4, 8, 3])

    print(ln1)

    ln2 = ListNode(6)
    ln2.extend([9, 9])

    print(ln2)

    answer = ListNode(0)

    print(answer)

    currentLN1 = ln1
    currentLN2 = ln2
    currentAnswerNode = answer

    while currentLN1 is not None or currentLN2 is not None:
        if currentLN1 is None and currentLN2 is not None:
            while currentLN2 is not None:
                total = currentLN2.val + currentAnswerNode.val
                currentAnswerNode.val = total % 10
                carry = total // 10

                currentLN2 = currentLN2.next
                currentAnswerNode.next = ListNode(carry)
                currentAnswerNode = currentAnswerNode.next

            break

        elif currentLN2 is None and currentLN1 is not None:
            while currentLN1 is not None:
                total = currentLN1.val + currentAnswerNode.val
                currentAnswerNode.val = total % 10
                carry = total // 10

                currentLN1 = currentLN1.next
                currentAnswerNode.next = ListNode(carry)
                currentAnswerNode = currentAnswerNode.next

            break

        else:
            total = currentLN1.val + currentLN2.val + currentAnswerNode.val
            currentAnswerNode.val = total % 10
            carry = total // 10

            currentLN1 = currentLN1.next
            currentLN2 = currentLN2.next
            currentAnswerNode.next = ListNode(carry)
            currentAnswerNode = currentAnswerNode.next


    print(answer)