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

    def __str__(self):
        current = self.root

        string_representation = ''

        while current is not None:
            string_representation = f'{string_representation}{current.value} => '
            current = current.next

        return f'{string_representation}None'

    def print(self):
        """
        Prints the __str__ representation of the singly linked list
        :return: None
        """

        print(self)


if __name__  == '__main__':
    sll = SinglyLinkedList()
    sll.create(values=[1, 4, 5, 6, 6, 7, 8, 10, 10])
    print(sll)




