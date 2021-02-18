def removeDuplicateLetters(s):
    """
    TC: O(n)
    SC: O(n)
    """
    n = len(s)
    if n < 2:
        return s
    
    added = set()
    count = {}

    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    
    stack = []
    for c in s:
        if c not in added and count[c] > 0:
            while stack and ord(stack[-1]) > ord(c) and count[stack[-1]] != 0:
                j = stack.pop()
                added.remove(j)
            stack.append(c)
            added.add(c)
        count[c] -= 1
    
    return "".join(stack)