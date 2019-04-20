class SinglyLinkedListNode:

    def __init__(self, data):
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
