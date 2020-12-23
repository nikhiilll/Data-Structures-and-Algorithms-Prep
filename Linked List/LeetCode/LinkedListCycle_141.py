def linkedListCycle(head):
    """
    TC: O(n) | SC: O(1)
    """
    # visitedNodes = set()
    # ptr = head

    # while ptr:
    #     if ptr in visitedNodes:
    #         return True
    #     visitedNodes.add(ptr)
    #     ptr = ptr.next
    
    # return False
    """
    TC: O(n) | SC: O(1)
    """
    first, second = head.next, head.next.next

    while first != second:
        first = first.next
        second = second.next.next

    first = head

    while first != second:
        first = first.next
        second = second.next
    
    return first
