from typing import Pattern


def detectCycle(head):
    """
    TC: O(n)
    SC: O(1)
    """
    if not head:
        return
    
    slow, fast = head, head.next

    try:
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
    except:
        return None
    
    ptr = head
    slow = slow.next
    while ptr is not slow:
        slow = slow.next
        ptr = ptr.next

    return ptr