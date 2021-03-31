def getNthFib(n):
    """
    TC: O(n)
    SC: O(1)
    """
    if  n < 3:
        return n - 1
    
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    
    return b