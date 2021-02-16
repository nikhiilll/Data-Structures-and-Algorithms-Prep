def minAddToMakeValid(S):

    stack = []

    for c in S:
        if c == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    
    return len(stack)

S = "()"
print(minAddToMakeValid(S))