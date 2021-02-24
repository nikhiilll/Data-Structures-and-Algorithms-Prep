class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    """
    TC: O(n)
    SC: O(1)
    """
    ptr = head
    for _ in range(k):
        ptr = ptr.next
    
    prev, curr = None, head
    while ptr:
        ptr, prev, curr = ptr.next, curr, curr.next
    
    if curr is head:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev.next = curr.next
    
    return head.next