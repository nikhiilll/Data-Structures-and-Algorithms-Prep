class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    """
    TC: O(n)
    SC: O(1)
    """

    if not head or not head.next or k == 0:
        return head
    
    ptr = head
    count = 1

    while ptr.next:
        count += 1
        ptr = ptr.next
    
    offset = abs(k) % count
    if offset == 0:
        return head

    toLoop = offset if k < 0 else (count - offset)

    curr = head
    for _ in range(1, toLoop):
        curr = curr.next
    
    ptr.next = head
    head = curr.next
    curr.next = None

    return head