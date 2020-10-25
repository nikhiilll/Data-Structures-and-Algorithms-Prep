def scoreOfParentheses(S):

    stack = [0]

    for c in S:
        if c == "(":
            stack.append(0)
        else:
            last = stack.pop()
            stack[-1] += 2 * last or 1
    
    return stack.pop()

