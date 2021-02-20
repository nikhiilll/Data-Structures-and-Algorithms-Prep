def countHomogenous(s):
    """
    TC: O(n)
    SC: O(1)
    """
    if not s:
        return 0

    count = 1
    stack = [(s[0], 1)]
    i = 1

    while i < len(s):
        current = 1
        if stack and stack[-1][0] == s[i]:
            current += stack[-1][1]
        stack.pop()
        stack.append((s[i], current))
        count += current 
        i += 1

    return (count % (10**9 + 7))