def reverseWords(s):
    """
    TC: O(n)
    SC: O(n)
    """
    output = []
    stack = []

    for c in s:
        if c == ".":
            while stack:
                output.append(stack.pop())
            output.append(c)
        else:
            stack.append(c)
    
    while stack:
        output.append(stack.pop())
    
    return "".join(output)
    
