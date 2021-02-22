def reverseBetween(head, left, right):
    """
    TC: O(right)
    SC: O(1)
    """
    if left == right or not head:
        return head
    
    ptr = None
    p1 = head
    count = 1

    while count != left:
        ptr = p1
        p1 = p1.next
        count += 1
    
    p2 = p1.next
    while count != right:
        temp = p2.next
        p2.next = p1
        p1 = p2
        p2 = temp
        count += 1
    
    if left == 1:
        head.next = p2
        head = p1
    else:
        ptr.next.next = p2
        ptr.next = p1
    
    return head