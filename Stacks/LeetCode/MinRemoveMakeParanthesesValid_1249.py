def minRemoveToMakeValid(s):

    stack_open = []
    S = list(s)

    for i in range(len(S)):
        if S[i] == "(":
            stack_open.append(i)
        elif S[i] == ")":
            if stack_open:
                stack_open.pop()
            else:
                S[i] = ""
    
    for i in stack_open:
        S[i] = ""
    
    return "".join(S)



s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))
