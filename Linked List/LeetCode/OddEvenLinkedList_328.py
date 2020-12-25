def oddEvenLinkedList(head):
    """
    TC: O(n) | SC: O(1)
    """
    if not head:
        return head
    
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    
    odd.next = evenHead

    return head