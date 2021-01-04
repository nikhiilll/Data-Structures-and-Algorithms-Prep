def __init__(self):
    self.prev = None

def flatten(root):
    """
    TC: O(n)
    SC: O(n)
    """
    if not root:
        return
    
    prevptr, ptr = root, None
    stack = [root.right, root.left]
    
    while stack:
        ptr = stack.pop()
        if not ptr:
            continue
        prevptr.right = ptr
        prevptr.left = None
        stack.append(ptr.right)
        stack.append(ptr.left)
        prevptr = ptr
    
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    
    if not root:
        return
    self.flatten(root.right)
    self.flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root
    