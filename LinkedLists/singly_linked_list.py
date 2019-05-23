import random


class SinglyLinkedListNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None


def add_to_linked_list(linked_list: SinglyLinkedListNode, data: int) -> SinglyLinkedListNode:
    linked_list.next = SinglyLinkedListNode(data=data)

    return linked_list.next


def print_linked_list(head: SinglyLinkedListNode):
    string_rep = f'{head.data}'
    current = head.next
    while current is not None:
        string_rep = f'{string_rep} => {current.data}'
        current = current.next

    print(f'{string_rep} => None')
    return f'{string_rep} => None'


def random_linked_list(length: int) -> SinglyLinkedListNode:
    head = SinglyLinkedListNode(random.randint(0, 100))

    current = head
    for i in range(length - 1):
        value = random.randint(0, 100)
        current.next = add_to_linked_list(current, value)
        current = current.next

    return head
