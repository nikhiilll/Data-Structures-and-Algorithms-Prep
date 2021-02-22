def mergeTwoLists(l1, l2):
    """
    TC: O(n + m)
    SC: O(1)
    """
    if not l1:
        return l2
    if not l2:
        return l1

    head = tail = ListNode(0)
    ptr1, ptr2 = l1, l2

    while ptr1 and ptr2:
        if ptr1.val < ptr2.val:
            tail.next, ptr1 = ptr1, ptr1.next
        else:
            tail.next, ptr2 = ptr2, ptr2.next
        tail = tail.next
    
    tail.next = ptr1 or ptr2
    return head.next


