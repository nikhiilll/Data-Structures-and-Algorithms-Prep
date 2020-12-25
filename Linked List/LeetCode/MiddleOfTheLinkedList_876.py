def middleNode(head):
    """
    TC: O(n) | SC: O(1)
    """
    first, second = head, head

    while second and second.next:
        first = first.next
        second = second.next.next

    return first