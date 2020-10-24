def makeGood(s):

    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif c.islower() and stack[-1].isupper() and stack[-1].lower() == c:
            stack.pop()
        elif c.isupper() and stack[-1].islower() and stack[-1].upper() == c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

s = "leEeetcode"
print(makeGood(s))