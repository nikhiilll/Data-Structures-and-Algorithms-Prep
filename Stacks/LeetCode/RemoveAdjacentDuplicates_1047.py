def removeDuplicates(S):

    stack = []

    for c in S:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

S = "abbaca"
print(removeDuplicates(S))