def removeOuterParentheses(S):

    result_string, brackets_opened = [], 0

    for s in S:
        if s == '(' and brackets_opened > 0: 
            result_string.append(s)
        elif s == ')' and brackets_opened > 1:
            result_string.append(s)
        brackets_opened += 1 if s == '(' else -1
    
    return "".join(result_string)

S = "(()())(())(()(()))"
print(removeOuterParentheses(S))

