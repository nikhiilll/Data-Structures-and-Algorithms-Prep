def flattenMultilevelDoublyLinkedList(head):

    if not head:
        return head
    
    prev = None
    stack = [head]

    while stack:
        node = stack.pop()
        node.prev = prev
        prev.next = node
        prev = node
        if node.next is not None:
            stack.append(node.next)
        if node.child is not None:
            stack.append(node.child)
            node.child = None
    
    head.prev = None
    return head