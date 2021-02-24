def removeLoop(head):

    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    try:
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
    except:
        return head
    
    slow = head
    slow = slow.next
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    while slow is not fast.next:
        fast = fast.next
    
    fast.next = None
    return head
