class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    """
    TC: O(n)
    SC: O(1)
    """
    if not head:
        return

    head1 = ptr1 = LinkedList(0)
    head2 = ptr2 = LinkedList(0)
    ptr = head

    while ptr:
        if ptr.value == k:
            if ptr2 is head2:
                ptr2.next = ptr
                ptr2 = ptr2.next
            else:
                temp = head2.next
                head2.next = ptr
                ptr = ptr.next
                head2.next.next = temp
                continue
        elif ptr.value < k:
            ptr1.next = ptr
            ptr1 = ptr1.next
        else:
            ptr2.next = ptr
            ptr2 = ptr2.next
        ptr = ptr.next

    ptr2.next = None
    ptr1.next = head2.next
    return head1.next
