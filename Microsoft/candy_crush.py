import unittest
from typing import List


class ListNode(object):
    """
    Represents a singly linked list's node
    """

    def __init__(self, value):
        """
        Instantiate a ListNode
        :param value: The value to be stored at the node. This can an object of any type.
        """

        self.value = value
        self.next = None

    def __eq__(self, other):
        """
        Compare two ListNode instance for structural equality
        Two ListNode instance are considered equal if the values stored at their nodes
        are equal (by value for primitives and by reference for objects)
        :param other: The second ListNode instance to be compared
        :return: True if self and other are structurally equal, otherwise False
        """

        # Two ListNode instance cannot be considered equal if one is longer than the other
        if not other:
            return False

        # Performs a recursive comparison of next node if the values are the same
        # If the values are not the same then the nodes are not structurally unequal
        return self.value == other.value and self.next == other.next

    def __str__(self):
        """
        Create a string representation of values to be stored from self to the end of the linked list
        :return:
        """
        string_representation = ''
        current = self

        # Iteratively appends the current value of the ListNode to the string representation
        while current is not None:
            string_representation = f'{string_representation}{current.value} => '
            current = current.next

        return f'{string_representation}None'

    def candy_crush(self):
        """
        Removes all nodes in the linked list that have adjacent nodes with the same value
        :return: A candy crushed version of the ListNode
        """

        current = self

        # The candy crushed version of a linked list with just one node is itself
        if current and current.next:

            # If the next value in the node are different, then next is the candy crushed version of the next node
            if current.value != current.next.value:
                current.next = current.next.candy_crush()

            # Skip all elements until you find a dissimilar one
            else:
                while current.next and current.value == current.next.value:
                    current = current.next

                # The next node after the last adjacently similar element should be the next element candy crushed
                if current.next:
                    current = current.next.candy_crush()
                else:
                    current = None

        return current


class SinglyLinkedList(object):
    """
    Implements common functions in a singly linked list
    """

    def __init__(self, root: ListNode = None):
        """
        Instantiate a SinglyLinkedList
        :param root: The root of the tree. This should be a ListNode instance.
        """
        self.root = root

    def create(self, values: List[object]):
        """
        Creates a singly linked list serially from a list of values supplied to it
        :param values: The values to be stored serially at the nodes in the linked list
        :return: A SinglyLinkedList instance with the values in the values parameter stored serially at the nodes
                in the linked list.
        """
        if not values:
            return None

        # The root of the tree is created from the value of the first element in the list provided
        self.root = ListNode(values[0])

        # The rest of the nodes in the singly linked list are created sequentially till all the
        # items in the list are exhausted.

        current = self.root

        for index in range(1, len(values)):
            next = ListNode(values[index])
            current.next = next
            current = next

        return self

    def __str__(self) -> str:
        """
        Creates a string representation of a SinglyLinkedList
        :return: The str representation of a SinglyLinkedList from its root onwards
        """
        return str(self.root)

    def __eq__(self, other):
        """
        Compare two linked lists for structural inequality
        :param other:
        :return:
        """
        return self.root == other.root

    def candy_crush(self):
        """
        Returns the candy crushed version of the root node in the linked list
        :return: self, candy crushed serially from the root
        """
        self.root = self.root.candy_crush()

        return self


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:

        # Instantiate two empty linked lists to be reused in the tests
        self.ll1 = SinglyLinkedList()
        self.ll2 = SinglyLinkedList()

    def test_none_equality(self):
        """
        By default, empty linked lists should be considered equal
        :return:
        """

        self.assertEqual(self.ll1, self.ll2)

    def test_two_short_linked_lists(self):
        """
        Creating two linked lists from the same list should result in structurally equal linked lists
        :return:
        """

        values = [1, 3, 4, 6, 6, 8]
        self.assertEqual(self.ll1.create(values), self.ll2.create(values))

    def test_candy_crush_of_linked_list_starting_with_similar_elements(self):
        """
        All similar elements in the beginning of a linked list should be candily crushed out. d
        :return:
        """
        long = [1, 1, 1, 1, 5, 6, 6, 4, 3, 3, 10]
        crushed = [5, 4, 10]

        self.setUp()

        self.assertEqual(self.ll1.create(long).candy_crush(), self.ll2.create(crushed))

    def test_candy_crush_of_linked_list_ending_with_similar_elements(self):
        """
        All similar elements in the end of a linked list should be candily crushed out. d
        :return:
        """
        long = [1, 1, 1, 1, 5, 6, 6, 4, 3, 3, 10, 10, 10]
        crushed = [5, 4]

        self.setUp()

        self.assertEqual(self.ll1.create(long).candy_crush(), self.ll2.create(crushed))


if __name__ == '__main__':
    unittest.main()
