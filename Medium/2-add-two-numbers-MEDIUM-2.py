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

if __name__  == '__main__':
    l1 = ListNode(8)
    l1.extend(2)
    l1.extend(3)

    l2 = ListNode(2)
    l2.extend(3)
    l2.extend(9)
    l2.extend(9)
    l2.extend(1)
    l2.extend(3)

    temp1 = l1
    temp2 = l2
    carry = 0

    llAns = None
    temp = None
    while temp1 is not None or temp2 is not None or carry > 0:
        if temp1 is not None:
            carry += temp1.val
            temp1 = temp1.next
        if temp2 is not None:
            carry += temp2.val
            temp2 = temp2.next

        if llAns is None:
            llAns = ListNode(carry % 10)
            temp = llAns
        else:
            temp.next = ListNode(carry % 10)
            temp = temp.next

        carry = carry // 10

    print(llAns)


