def validateStackSequences(pushed, popped):

    stack = []
    j = 0
    for no in pushed:
        stack.append(no)
        if popped[j] == stack[-1]:
            while stack and j < len(popped) and popped[j] == stack[-1]:
                stack.pop()
                j += 1
    
    return (len(stack) == 0)

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))