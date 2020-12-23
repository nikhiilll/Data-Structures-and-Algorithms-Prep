def removeNthNodeFromEnd(head, n):

    ptr1, ptr2 = head, head

    for _ in range(n):
        ptr2 = ptr2.next

    if ptr2 is None:
        return head.next
    
    while ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    ptr1.next = ptr1.next.next
    return head