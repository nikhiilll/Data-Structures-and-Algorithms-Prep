def minOperations(logs):

    stack = []

    for log in logs:
        if log == "../":
            if stack:
             stack.pop()
        elif log == "./":
            continue
        else:
            stack.append(log)
    
    return len(stack)

logs = ["./","../","./"]
print(minOperations(logs))
