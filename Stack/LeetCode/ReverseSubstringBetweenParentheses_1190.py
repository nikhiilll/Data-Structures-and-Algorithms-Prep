def reverseParentheses(s):

    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif c == ")" and stack:
            temp = []
            while stack[-1] != "(":
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(c)
    
    return "".join(stack)

s = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s))