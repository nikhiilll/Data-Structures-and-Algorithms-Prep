def reverseLinkedList(head):
    """
    TC: O(n) | SC: O(1)
    """
    
    previous = None
    current = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous