def nextGreaterNodeInLinkedList(head):
    """
    TC: O(n^2) | SC: O(n)
    """
    # if not head:
    #     return []
    # if head.next is None:
    #     return [0]
    
    # answers = []
    # ptr1, ptr2 = head, head

    # while ptr1.next is not None:
    #     while ptr2.next is not None:
    #         ptr2 = ptr2.next
    #         if ptr2.val > ptr1.val:
    #             answers.append(ptr2.val)  
    #             break
    #     else:
    #         answers.append(0)
    #     ptr1 = ptr1.next
    #     ptr2 = ptr1
    
    # answers.append(0)
    # return answers



    """
    TC: O(n) | SC: O(n)
    """
    if not head:
        return []
    if head.next is None:
        return [0]
    
    answers = [0]
    stack = [(head.val, 0)]
    ptr = head.next
    posCounter = 0

    while ptr:
        answers.append(0)
        posCounter += 1
        while stack and ptr.val > stack[-1][0]:
            pos = stack.pop()
            answers[pos[1]] = ptr.val
        stack.append((ptr.val, posCounter))
        ptr = ptr.next

    return answers
    

    
