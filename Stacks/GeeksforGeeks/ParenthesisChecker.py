def parenthesisChecker(x):
    """
    TC: O(n)
    SC: O(n)
    """
    brackets = {"]" : "[", "}" : "{", ")" : "("}
    stack = []

    for c in x:
        if c in "[{(":
            stack.append(c)
        else:
            if not stack or stack[-1] != brackets[c]:
                return False
            stack.pop()
    
    return len(stack) == 0