def smallestSubsequence(S):

    last_dict = {c: i for i, c in enumerate(S)}
    stack = []

    for i, c in enumerate(S):
        if c in stack:
            continue
        while stack and stack[-1] > c and i < last_dict[stack[-1]]:
            stack.pop()
        stack.append(c)
    
    return "".join(stack)

s = "cbacdcbc"
print(smallestSubsequence(s))