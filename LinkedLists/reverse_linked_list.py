from LinkedLists.singly_linked_list import random_linked_list, print_linked_list

if __name__ == '__main__':
    head = random_linked_list(10)

    print_linked_list(head)
    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev

    print_linked_list(head)