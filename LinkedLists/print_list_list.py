from LinkedLists.singly_linked_list import SinglyLinkedListNode, add_to_linked_list, print_linked_list

import random
if __name__ == '__main__':
    head = SinglyLinkedListNode(10)

    current = head
    for i in range(10):
        value = random.randint(0, 100)
        current.next = add_to_linked_list(current, value)
        current = current.next

    print_linked_list(head)

