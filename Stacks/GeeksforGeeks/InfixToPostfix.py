def InfixtoPostfix(exp):
    """
    TC: O(n)
    SC: O(n)
    """
    output = []
    precedence = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3}
    stack = []

    for c in exp:

        if c.isalpha():
            output.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[c]:
                output.append(stack.pop())
            stack.append(c)
    
    while stack:
        output.append(stack.pop())
    
    return "".join(output)