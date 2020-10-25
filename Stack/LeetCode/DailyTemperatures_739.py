def dailyTemperatures(T):

    # stack = []
    # result = {}

    # for i, temp in enumerate(T): 
    #     if len(stack) == 0:
    #         stack.append((temp, i))
    #     elif temp < stack[-1][0]:
    #         stack.append((temp, i))
    #     else:
    #         while stack and temp > stack[-1][0]:
    #             result[stack.pop()] = i - stack[-1][1]
    #         stack.append((temp, i))
    
    # return [result[v, i] if (v, i) in result else 0 for i, v in enumerate(T)]

    stack = []
    result = [0] * len(T)

    for i, temp in enumerate(T):
        if len(stack) == 0:
            stack.append(i)
        elif temp < T[stack[-1]]:
            stack.append(i)
        else:
            while stack and temp > T[stack[-1]]:
                current = stack.pop()
                result[current] = i - current
            stack.append(i)
    
    return result


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))
                