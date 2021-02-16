def isValid(s):

    opening_brackets = "({["
    closing_brackets = ")}]"
    stack = []

    for c in s:
        if c in opening_brackets:
            stack.append(c)
        else:
            if not stack:
                return False
            elif opening_brackets.index(stack[-1]) != closing_brackets.index(c):
                return False
            else:
                stack.pop()
    
    return (len(stack) == 0)

s = "(]"
print(isValid(s))