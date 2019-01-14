import unittest

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


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
    def addStrings(self, l1, l2):
        str_1 = ''
        str_2 = ''

        temp = l1
        while temp is not None:
            str_1 = str(l1.val) + str_1
            temp = temp.next

        temp = l2
        while temp is not None:
            str_2 = str(l2.val) + str_2
            temp = temp.next

        a = int(str_1)
        b = int(str_2)

        print(a + b)


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode"""

        currentLN1 = l1
        currentLN2 = l2

        answer = ListNode(0)
        currentAnswerNode = answer

        while currentLN1 is not None or currentLN2 is not None:
            if currentLN1 is None and currentLN2 is not None:
                if currentLN2.val == 9:
                    while currentLN2 is not None:
                        total = currentLN2.val + currentAnswerNode.val
                        currentAnswerNode.val = total % 10
                        carry = total // 10

                        currentLN2 = currentLN2.next

                        if currentLN2 is not None:
                            currentAnswerNode.next = ListNode(carry)
                            currentAnswerNode = currentAnswerNode.next
                        elif carry > 0:
                            currentAnswerNode.next = ListNode(carry)
                else:
                    currentAnswerNode.val = currentLN2.val + currentAnswerNode.val
                    currentAnswerNode.next = currentLN2.next
                break

            elif currentLN2 is None and currentLN1 is not None:
                if currentLN1.val == 9:
                    while currentLN1 is not None:
                        total = currentLN1.val + currentAnswerNode.val
                        currentAnswerNode.val = total % 10
                        carry = total // 10

                        currentLN1 = currentLN1.next
                        if currentLN1 is not None:
                            currentAnswerNode.next = ListNode(carry)
                            currentAnswerNode = currentAnswerNode.next
                        elif carry > 0:
                            currentAnswerNode.next = ListNode(carry)
                else:
                    currentAnswerNode.val = currentLN1.val + currentAnswerNode.val
                    currentAnswerNode.next = currentLN1.next
                break

            else:
                total = currentLN1.val + currentLN2.val + currentAnswerNode.val
                currentAnswerNode.val = total % 10
                carry = total // 10

                currentLN1 = currentLN1.next
                currentLN2 = currentLN2.next

                if currentLN1 is not None or currentLN2 is not None:
                    currentAnswerNode.next = ListNode(carry)
                    currentAnswerNode = currentAnswerNode.next
                elif carry > 0:
                    currentAnswerNode.next = ListNode(carry)

        return answer.__repr__()


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_simple(self):
        ln1 = ListNode(2)
        ln1.extend([1, 3, 7, 4, 8, 3])

        ln2 = ListNode(6)
        ln2.extend([9, 9, 6, 4, 3, 5, 3])

        llAns = ListNode(8)
        llAns.extend([0, 3, 4, 9, 1, 9, 3])

        self.assertEqual(self.solution.addStrings(ln1, ln2), llAns.__repr__())

    def test_single_node_ll(self):
        ln1 = ListNode(5)

        ln2 = ListNode(5)

        llAns = ListNode(0)
        llAns.extend([1])

        self.assertEqual(self.solution.addStrings(ln1, ln2), llAns.__repr__())

    def test_ones_and_nines(self):
        ln1 = ListNode(1)

        ln2 = ListNode(9)
        ln2.extend(9)

        llAns = ListNode(0)
        llAns.extend([0, 1])

        self.assertEqual(self.solution.addStrings(ln1, ln2), llAns.__repr__())


if __name__ == '__main__':
    unittest.main()
