def isPalindrome(head):

    """
    TC: O(n) | SC: O(1)
    """
    # values = []
    # ptr = head

    # while ptr:
    #     values.append(ptr.val)
    #     ptr = ptr.next

    # return values == values[::-1]

    """
    TC: O(n) | SC: O(1)
    """
    reverse = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        reverse, reverse.next, slow = slow, reverse, slow.next
    
    if fast:
        slow = slow.next
    
    while reverse and reverse.val == slow.val:
        reverse = reverse.next
        slow = slow.next
    
    return not reverse


