def calPoints(ops):

    stack = []

    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
    
    return sum(stack)

ops = ["1","C","-62","-45","-68"]
print(calPoints(ops))