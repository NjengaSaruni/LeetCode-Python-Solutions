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
        return self.root == other.root

if __name__  == '__main__':
    sll = SinglyLinkedList()
    sll.create(values=[1, 4, 5, 6, 6, 7, 8, 10, 10])
    print(sll)




